#!/usr/bin/env python3
"""Verify observability example traces contain required canonical events.

Reads text files only — no trace parser framework.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EXAMPLES = ROOT / "observability" / "examples"


@dataclass(frozen=True)
class TraceExpectation:
    filename: str
    required_events: tuple[str, ...]
    description: str


EXPECTATIONS: list[TraceExpectation] = [
    TraceExpectation(
        "successful-review-trace.txt",
        ("task_started", "verification_passed", "approval_requested", "task_completed"),
        "Happy path review publish",
    ),
    TraceExpectation(
        "failed-review-trace.txt",
        ("approval_requested", "approval_denied", "task_failed"),
        "Human approval denied",
    ),
    TraceExpectation(
        "escalation-trace.txt",
        ("retry_triggered", "retry_exhausted", "escalation_triggered", "unsafe_action_blocked"),
        "Retry exhaustion and escalation",
    ),
    TraceExpectation(
        "malformed-llm-trace.txt",
        ("llm_malformed_output", "verification_failed", "governance_rejection"),
        "Malformed LLM output rejected",
    ),
    TraceExpectation(
        "unsafe-gui-action-trace.txt",
        ("verification_failed", "unsafe_action_blocked"),
        "GUI mismatch blocks action",
    ),
    TraceExpectation(
        "queue-recovery-trace.txt",
        ("queue_recovered", "task_started", "task_completed"),
        "Queue recovery after crash",
    ),
]


def check_trace(path: Path, required: tuple[str, ...]) -> tuple[bool, list[str]]:
    if not path.exists():
        return False, [f"file missing: {path.name}"]

    text = path.read_text(encoding="utf-8")
    missing = [event for event in required if event not in text]
    return len(missing) == 0, missing


def main() -> int:
    print("=== Expected Text Trace Check (Phase 2.5) ===")
    print(f"Examples dir: {EXAMPLES}\n")

    passed = 0
    failed = 0
    for item in EXPECTATIONS:
        path = EXAMPLES / item.filename
        ok, missing = check_trace(path, item.required_events)
        if ok:
            passed += 1
            print(f"PASS  {item.filename:32}  {item.description}")
        else:
            failed += 1
            detail = ", ".join(missing) if missing else "unknown"
            print(f"FAIL  {item.filename:32}  missing: {detail}")

    print(f"\nSummary: PASS={passed} FAIL={failed} total={len(EXPECTATIONS)}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
