#!/usr/bin/env python3
"""Minimal check for Review Assistant thin demo (Phase 3.1.1).

Runs 5 scenarios, checks exit code and required trace event substrings.
Stdlib only. No repo mutation. No external services.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
DEMO = REPO_ROOT / "prototypes-derived" / "review-assistant-thin" / "minimal_demo.py"

SCENARIOS: dict[str, dict[str, object]] = {
    "happy": {
        "events": [
            "task_started",
            "draft_created",
            "critique_completed",
            "verification_passed",
            "approval_requested",
            "approval_granted",
            "task_completed",
        ],
        "must_contain": ["decision=DELIVERED", "delivered=True"],
    },
    "missing_approval": {
        "events": [
            "task_started",
            "draft_created",
            "critique_completed",
            "verification_passed",
            "approval_requested",
            "approval_timeout",
            "task_failed",
        ],
        "must_contain": ["decision=BLOCKED", "delivered=False"],
    },
    "critic_uncertain": {
        "events": [
            "task_started",
            "draft_created",
            "critique_completed",
            "escalation_triggered",
        ],
        "must_contain": ["decision=ESCALATED", "delivered=False"],
    },
    "bad_draft": {
        "events": [
            "task_started",
            "draft_created",
            "critique_completed",
            "verification_failed",
            "task_failed",
        ],
        "must_contain": ["decision=FAILED", "delivered=False"],
    },
    "unsafe_publish_attempt": {
        "events": [
            "task_started",
            "unsafe_action_blocked",
            "task_failed",
        ],
        "must_contain": ["decision=FAILED", "delivered=False"],
    },
}


def run_scenario(name: str) -> tuple[bool, str]:
    spec = SCENARIOS[name]
    cmd = [sys.executable, str(DEMO), "--scenario", name]
    proc = subprocess.run(cmd, capture_output=True, text=True, cwd=REPO_ROOT)
    output = proc.stdout + proc.stderr

    if proc.returncode != 0:
        return False, f"exit code {proc.returncode}"

    for event in spec["events"]:
        if event not in output:
            return False, f"missing event substring: {event}"

    for fragment in spec["must_contain"]:
        if fragment not in output:
            return False, f"missing output fragment: {fragment}"

    return True, "ok"


def main() -> int:
    if not DEMO.is_file():
        print(f"FAIL  demo missing: {DEMO}")
        return 1

    print("=== Review Assistant Thin Check (Phase 3.1.1) ===")
    print(f"Demo: {DEMO.relative_to(REPO_ROOT)}\n")

    passed = 0
    failed = 0

    for name in SCENARIOS:
        ok, detail = run_scenario(name)
        status = "PASS" if ok else "FAIL"
        print(f"{status:4}  {name:24}  {detail}")
        if ok:
            passed += 1
        else:
            failed += 1

    print(f"\nSummary: PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
