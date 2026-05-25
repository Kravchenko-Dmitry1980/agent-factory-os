#!/usr/bin/env python3
"""Filesystem audit log: append-only JSONL, lineage, immutable records."""

from __future__ import annotations

import argparse
import json
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SHARED = ROOT / "integrations-real" / "shared"
sys.path.insert(0, str(SHARED))
import local_paths  # noqa: E402


class AuditLog:
    """Append-only — no update/delete (anti-tamper by API shape)."""

    def __init__(self, name: str = "filesystem-audit-log") -> None:
        self.path = local_paths.adapter_dir(name) / "events.jsonl"

    def append(self, actor: str, action: str, *, parent_id: str | None = None, **detail: object) -> str:
        event_id = str(uuid.uuid4())[:12]
        record = {
            "event_id": event_id,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "actor": actor,
            "action": action,
            "parent_id": parent_id,
            **detail,
        }
        try:
            with self.path.open("a", encoding="utf-8") as f:
                f.write(json.dumps(record, ensure_ascii=False) + "\n")
        except OSError as exc:
            raise RuntimeError(f"audit append failed: {exc}") from exc
        return event_id

    def read_all(self) -> list[dict]:
        if not self.path.exists():
            return []
        events: list[dict] = []
        for i, line in enumerate(self.path.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                events.append(json.loads(line))
            except json.JSONDecodeError:
                events.append({"corrupt_line": i, "action": "corrupt_line_warning"})
        return events

    def lineage(self, event_id: str) -> list[str]:
        events = {e.get("event_id"): e for e in self.read_all() if "event_id" in e}
        chain: list[str] = []
        current = event_id
        while current:
            chain.append(current)
            ev = events.get(current)
            if not ev:
                break
            current = ev.get("parent_id") or ""
        return list(reversed(chain))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scenario", default="happy", choices=["happy", "corruption-attempt"])
    args = parser.parse_args()

    print("=== Filesystem Audit Log (Phase 2.2) ===\n")
    log = AuditLog()

    e1 = log.append("workflow", "task_received", task="promotion review")
    e2 = log.append("reviewer", "review_pass", parent_id=e1, artifact="pattern-x")
    e3 = log.append("human", "approval", parent_id=e2, fingerprint="abc123")
    e4 = log.append("gate", "failure", parent_id=e3, reason="verification failed")
    log.append("supervisor", "escalated", parent_id=e4, reason="human required")

    if args.scenario == "corruption-attempt":
        print("  tamper attempt: AuditLog has no update() — append-only API")
        try:
            log.update  # type: ignore[attr-defined]
        except AttributeError:
            print("  tamper blocked by design")

    chain = log.lineage(e4)
    print(f"  lineage to failure event: {chain}")
    print(f"  total events: {len(log.read_all())}")
    print("\n  Last 3 events:")
    for ev in log.read_all()[-3:]:
        print(f"    {ev.get('action')}: {ev.get('actor')} @ {ev.get('timestamp', '')[:19]}")


if __name__ == "__main__":
    main()
