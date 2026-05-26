#!/usr/bin/env python3
"""Check Review Assistant mock LLM scenarios (Phase 3.2).

Runs 5 LLM mock scenarios; checks exit code, events, and decision fragments.
Stdlib only. No external services.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
DEMO = REPO_ROOT / "prototypes-derived" / "review-assistant-thin" / "minimal_demo.py"

LLM_SCENARIOS: dict[str, dict[str, object]] = {
    "llm_valid_draft": {
        "events": [
            "llm_request_started",
            "llm_response_received",
            "llm_parse_passed",
            "draft_created",
            "verification_passed",
            "approval_requested",
            "approval_granted",
            "task_completed",
        ],
        "must_contain": ["decision=DELIVERED", "delivered=True"],
    },
    "llm_malformed_output": {
        "events": [
            "llm_request_started",
            "llm_response_received",
            "llm_parse_failed",
            "task_failed",
        ],
        "must_contain": ["decision=FAILED", "delivered=False"],
    },
    "llm_timeout": {
        "events": [
            "llm_request_started",
            "llm_timeout",
            "escalation_triggered",
            "task_failed",
        ],
        "must_contain": ["decision=ESCALATED", "delivered=False"],
    },
    "llm_uncertain": {
        "events": [
            "llm_request_started",
            "llm_response_received",
            "llm_uncertain",
            "escalation_triggered",
            "task_failed",
        ],
        "must_contain": ["decision=ESCALATED", "delivered=False"],
    },
    "llm_unsafe_output": {
        "events": [
            "llm_request_started",
            "llm_response_received",
            "llm_unsafe_output",
            "unsafe_action_blocked",
            "task_failed",
        ],
        "must_contain": ["decision=FAILED", "delivered=False"],
    },
}


def run_scenario(name: str) -> tuple[bool, str]:
    spec = LLM_SCENARIOS[name]
    cmd = [sys.executable, str(DEMO), "--scenario", name]
    proc = subprocess.run(cmd, capture_output=True, text=True, cwd=REPO_ROOT)
    output = proc.stdout + proc.stderr

    if proc.returncode != 0:
        return False, f"exit code {proc.returncode}"

    for event in spec["events"]:
        if event not in output:
            return False, f"missing event: {event}"

    for fragment in spec["must_contain"]:
        if fragment not in output:
            return False, f"missing fragment: {fragment}"

    if "approval_granted" in output and name != "llm_valid_draft":
        return False, "unexpected approval_granted on failure scenario"

    return True, "ok"


def main() -> int:
    if not DEMO.is_file():
        print(f"FAIL  demo missing: {DEMO}")
        return 1

    print("=== Review Assistant LLM Mock Check (Phase 3.2) ===")
    print(f"Demo: {DEMO.relative_to(REPO_ROOT)}\n")

    passed = 0
    failed = 0

    for name in LLM_SCENARIOS:
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
