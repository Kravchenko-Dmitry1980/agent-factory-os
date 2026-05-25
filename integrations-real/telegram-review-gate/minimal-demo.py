#!/usr/bin/env python3
"""Telegram review gate: workflow → review request → approve/reject → continue OR stop."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SHARED = ROOT / "integrations-real" / "shared"
if str(SHARED) not in sys.path:
    sys.path.insert(0, str(SHARED))

import local_paths  # noqa: E402


def _fingerprint(action_type: str, payload: dict) -> str:
    raw = json.dumps({"type": action_type, "payload": payload}, sort_keys=True)
    return hashlib.sha256(raw.encode()).hexdigest()[:16]


def _audit(event: dict) -> None:
    path = local_paths.adapter_dir("telegram-review-gate") / "audit.jsonl"
    event["timestamp"] = datetime.now(timezone.utc).isoformat()
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, ensure_ascii=False) + "\n")


def _telegram_api(token: str, method: str, payload: dict) -> dict:
    url = f"https://api.telegram.org/bot{token}/{method}"
    data = json.dumps(payload).encode()
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        body = json.loads(resp.read().decode())
    if not body.get("ok"):
        raise RuntimeError(body.get("description", "telegram error"))
    return body


@dataclass
class ReviewRequest:
    fingerprint: str
    action_type: str
    payload: dict
    risk: str = "high"


def request_review(req: ReviewRequest, *, real: bool, token: str, chat_id: str) -> None:
    pending_path = local_paths.adapter_dir("telegram-review-gate") / "pending.json"
    pending_path.write_text(
        json.dumps({"fingerprint": req.fingerprint, "action": req.action_type}, indent=2),
        encoding="utf-8",
    )
    _audit({"actor": "workflow", "action": "review_requested", "fingerprint": req.fingerprint})
    if real and token and chat_id:
        text = f"Review required\nAction: {req.action_type}\nFP: {req.fingerprint}\nReply: /approve {req.fingerprint} or /reject {req.fingerprint}"
        _telegram_api(token, "sendMessage", {"chat_id": chat_id, "text": text})
        _audit({"actor": "telegram", "action": "message_sent", "chat_id": chat_id})


def wait_approval(
    req: ReviewRequest,
    *,
    timeout: float,
    mock: str | None,
    real: bool,
    token: str,
) -> tuple[bool | None, str]:
    """Returns (approved, reason). None = timeout deny."""
    if mock == "approve":
        _audit({"actor": "human", "action": "mock_approve", "fingerprint": req.fingerprint})
        return True, "mock approved"
    if mock == "reject":
        _audit({"actor": "human", "action": "mock_reject", "fingerprint": req.fingerprint})
        return False, "mock rejected"

    deadline = time.monotonic() + timeout
    polls = 0
    max_polls = 3

    while time.monotonic() < deadline and polls < max_polls:
        polls += 1
        if real and token:
            try:
                body = _telegram_api(token, "getUpdates", {"timeout": 0, "limit": 5})
                for upd in body.get("result", []):
                    msg = upd.get("message", {})
                    text = (msg.get("text") or "").strip()
                    if text.startswith("/approve "):
                        fp = text.split(maxsplit=1)[1] if len(text.split()) > 1 else ""
                        if fp == req.fingerprint:
                            return True, "telegram approved"
                        return None, "invalid approval fingerprint"
                    if text.startswith("/reject "):
                        return False, "telegram rejected"
            except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
                _audit({"actor": "telegram", "action": "network_error", "error": str(exc)})
                return None, f"network failure: {exc}"
        time.sleep(min(1.0, timeout / max_polls))

    _audit({"actor": "gate", "action": "timeout_denied", "fingerprint": req.fingerprint})
    if req.risk == "high":
        _audit({"actor": "supervisor", "action": "escalated", "reason": "approval timeout"})
    return None, "deny-by-default: approval timeout"


def continue_workflow(approved: bool | None, reason: str, fingerprint: str) -> tuple[bool, str]:
    if approved is True:
        _audit({"actor": "workflow", "action": "continued", "fingerprint": fingerprint})
        return True, f"continued: {reason}"
    if approved is False:
        _audit({"actor": "workflow", "action": "stopped", "reason": reason})
        return False, f"stopped: {reason}"
    _audit({"actor": "gate", "action": "denied", "reason": reason})
    return False, f"fail-closed: {reason}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--real", action="store_true", help="Use Telegram API")
    parser.add_argument("--mock-approve", action="store_true")
    parser.add_argument("--mock-reject", action="store_true")
    parser.add_argument("--timeout", type=float, default=2.0)
    args = parser.parse_args()

    mock = "approve" if args.mock_approve else "reject" if args.mock_reject else None
    token = os.environ.get("TELEGRAM_BOT_TOKEN", "")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID", "")
    real = args.real and bool(token)

    print("=== Telegram Review Gate (Phase 2.2) ===")
    print(f"Mode: {'real' if real else 'mock'}\n")

    req = ReviewRequest(
        fingerprint="",
        action_type="publish_blog_post",
        payload={"title": "Q1 metrics", "channel": "external"},
    )
    req.fingerprint = _fingerprint(req.action_type, req.payload)

    request_review(req, real=real, token=token, chat_id=chat_id)
    approved, reason = wait_approval(
        req, timeout=args.timeout, mock=mock, real=real, token=token
    )
    ok, msg = continue_workflow(approved, reason, req.fingerprint)
    print(f"Fingerprint: {req.fingerprint}")
    print(f"Result: {msg}")


if __name__ == "__main__":
    main()
