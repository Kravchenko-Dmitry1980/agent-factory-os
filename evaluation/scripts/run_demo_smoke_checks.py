#!/usr/bin/env python3
"""Run selected demo commands and report PASS / FAIL / NOT_RUN.

Local smoke checks only — not a test framework. No pytest. No CI.
"""

from __future__ import annotations

import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


@dataclass(frozen=True)
class DemoCheck:
    name: str
    command: list[str]
    expect_in_output: tuple[str, ...] = ()


CHECKS: list[DemoCheck] = [
    DemoCheck(
        "review-loop happy",
        [sys.executable, "prototypes/review-loop-agent/minimal-demo.py", "--scenario", "happy"],
        ("Published: True", "Audit"),
    ),
    DemoCheck(
        "review-loop bypass blocked",
        [sys.executable, "prototypes/review-loop-agent/minimal-demo.py", "--scenario", "bypass-attempt"],
        ("Published: False", "bypass"),
    ),
    DemoCheck(
        "fail-closed no-approval",
        [sys.executable, "prototypes/fail-closed-external-action/minimal-demo.py", "--scenario", "no-approval"],
        ("denied", "Audit"),
    ),
    DemoCheck(
        "bounded-memory overflow",
        [sys.executable, "prototypes/bounded-memory-agent/minimal-demo.py", "--scenario", "overflow"],
        ("Audit",),
    ),
    DemoCheck(
        "queue max-retries",
        [sys.executable, "prototypes/queue-orchestration/minimal-demo.py", "--scenario", "max-retries"],
        ("Retries:", "Audit"),
    ),
    DemoCheck(
        "gui outcome-b mismatch",
        [sys.executable, "prototypes/gui-verification-loop/minimal-demo.py", "--scenario", "outcome-b"],
        ("Audit",),
    ),
    DemoCheck(
        "promotion reject",
        [sys.executable, "prototypes/promotion-pipeline-simulator/minimal-demo.py", "--scenario", "reject"],
        ("Decision:", "Audit"),
    ),
    DemoCheck(
        "llm malformed",
        [
            sys.executable,
            "integrations-real/llm-verification-adapter/minimal-demo.py",
            "--scenario",
            "malformed",
        ],
        ("reject", "LLM output != truth"),
    ),
    DemoCheck(
        "review-queue approval-denied",
        [
            sys.executable,
            "prototypes/integrations/review-queue-workflow/minimal-demo.py",
            "--scenario",
            "approval-denied",
        ],
        ("Audit",),
    ),
    DemoCheck(
        "escalation retry-storm",
        [
            sys.executable,
            "prototypes/integrations/escalation-workflow/minimal-demo.py",
            "--scenario",
            "retry-storm",
        ],
        ("Audit",),
    ),
    DemoCheck(
        "local-queue recovery",
        [
            sys.executable,
            "integrations-real/local-queue-worker/minimal-demo.py",
            "--scenario",
            "recovery",
        ],
        ("recovery", "completed"),
    ),
    DemoCheck(
        "filesystem audit log",
        [sys.executable, "integrations-real/filesystem-audit-log/minimal-demo.py", "--scenario", "happy"],
        ("Audit",),
    ),
]


def run_check(check: DemoCheck) -> tuple[str, str]:
    """Return (status, detail) where status is PASS, FAIL, or NOT_RUN."""
    cmd = check.command
    script_path = ROOT / cmd[1]
    if not script_path.exists():
        return "NOT_RUN", f"missing script: {cmd[1]}"

    try:
        result = subprocess.run(
            cmd,
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=120,
            check=False,
        )
    except subprocess.TimeoutExpired:
        return "FAIL", "timeout after 120s"
    except OSError as exc:
        return "NOT_RUN", str(exc)

    combined = (result.stdout + result.stderr).lower()
    if result.returncode != 0:
        return "FAIL", f"exit {result.returncode}"

    for needle in check.expect_in_output:
        if needle.lower() not in combined:
            return "FAIL", f"missing expected text: {needle!r}"

    return "PASS", "ok"


def main() -> int:
    print("=== Demo Smoke Checks (Phase 2.5 evaluation) ===")
    print(f"Repository: {ROOT}\n")

    counts = {"PASS": 0, "FAIL": 0, "NOT_RUN": 0}
    for check in CHECKS:
        status, detail = run_check(check)
        counts[status] += 1
        print(f"{status:8}  {check.name:32}  {detail}")

    print(f"\nSummary: PASS={counts['PASS']} FAIL={counts['FAIL']} NOT_RUN={counts['NOT_RUN']}")
    return 1 if counts["FAIL"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
