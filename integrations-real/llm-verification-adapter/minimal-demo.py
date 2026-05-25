#!/usr/bin/env python3
"""LLM verification adapter: prompt → LLM → verify → accept/reject/escalate.

CRITICAL: LLM output != truth
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SHARED = ROOT / "integrations-real" / "shared"
sys.path.insert(0, str(SHARED))
import local_paths  # noqa: E402


class VerificationResult(str, Enum):
    PASS = "pass"
    FAIL = "fail"
    UNCERTAIN = "uncertain"


class Decision(str, Enum):
    ACCEPT = "accept"
    REJECT = "reject"
    ESCALATE = "escalate"


def _audit(event: dict) -> None:
    path = local_paths.adapter_dir("llm-verification-adapter") / "audit.jsonl"
    event["timestamp"] = datetime.now(timezone.utc).isoformat()
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, ensure_ascii=False) + "\n")


def mock_llm(prompt: str, scenario: str) -> str:
    if scenario == "malformed":
        return "{ not valid json"
    if scenario == "uncertain":
        return json.dumps({"answer": "maybe", "confidence": "low"})
    return json.dumps({"answer": f"Summary for: {prompt[:40]}", "confidence": "high"})


def real_llm(prompt: str, timeout: int) -> str:
    api_key = os.environ.get("OPENAI_API_KEY", "")
    base = os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1").rstrip("/")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY missing")

    body = json.dumps(
        {
            "model": os.environ.get("OPENAI_MODEL", "gpt-4o-mini"),
            "messages": [
                {"role": "system", "content": "Respond with JSON: {\"answer\": str, \"confidence\": \"high\"|\"low\"}"},
                {"role": "user", "content": prompt},
            ],
            "temperature": 0,
        }
    ).encode()
    req = urllib.request.Request(
        f"{base}/chat/completions",
        data=body,
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = json.loads(resp.read().decode())
    content = data["choices"][0]["message"]["content"]
    return content


def verify_response(raw: str) -> tuple[VerificationResult, str]:
    """LLM output is untrusted — parse and evaluate separately."""
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError:
        return VerificationResult.FAIL, "malformed JSON from LLM"

    if not isinstance(parsed, dict) or "answer" not in parsed:
        return VerificationResult.FAIL, "missing answer field"

    confidence = str(parsed.get("confidence", "")).lower()
    if confidence == "low" or parsed.get("answer") == "maybe":
        return VerificationResult.UNCERTAIN, "low confidence — not truth"

    if len(str(parsed["answer"])) < 3:
        return VerificationResult.FAIL, "answer too short"

    return VerificationResult.PASS, "structured answer verified (not factual truth)"


def decide(verification: VerificationResult, reason: str) -> tuple[Decision, str]:
    if verification == VerificationResult.PASS:
        _audit({"actor": "gate", "action": "accept", "note": "LLM output != truth; format OK only"})
        return Decision.ACCEPT, f"accept (format only): {reason}"
    if verification == VerificationResult.UNCERTAIN:
        _audit({"actor": "supervisor", "action": "escalate", "reason": reason})
        return Decision.ESCALATE, f"escalate: {reason}"
    _audit({"actor": "gate", "action": "reject", "reason": reason})
    return Decision.REJECT, f"reject: {reason}"


def run(prompt: str, *, scenario: str, real: bool, timeout: int) -> None:
    _audit({"actor": "workflow", "action": "prompt", "length": len(prompt)})

    try:
        if real:
            raw = real_llm(prompt, timeout)
        else:
            raw = mock_llm(prompt, scenario)
    except (urllib.error.URLError, TimeoutError, RuntimeError, KeyError) as exc:
        _audit({"actor": "llm", "action": "error", "error": str(exc)})
        print(f"  LLM error: {exc}")
        print(f"  Decision: {Decision.ESCALATE.value} (fail-closed)")
        return

    _audit({"actor": "llm", "action": "response", "raw_len": len(raw)})
    print(f"  LLM raw (untrusted): {raw[:120]}...")

    verification, reason = verify_response(raw)
    decision, msg = decide(verification, reason)
    print(f"  Verification: {verification.value} — {reason}")
    print(f"  Decision: {decision.value} — {msg}")
    print("\n  Reminder: LLM output != truth")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--real", action="store_true")
    parser.add_argument("--scenario", default="happy", choices=["happy", "malformed", "uncertain"])
    parser.add_argument("--timeout", type=int, default=20)
    args = parser.parse_args()

    print("=== LLM Verification Adapter (Phase 2.2) ===")
    print("Principle: LLM output != truth\n")

    run(
        "Summarize governance rules for external publication",
        scenario=args.scenario,
        real=args.real,
        timeout=args.timeout,
    )


if __name__ == "__main__":
    main()
