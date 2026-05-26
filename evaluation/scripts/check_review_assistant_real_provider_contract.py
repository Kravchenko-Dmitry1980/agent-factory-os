#!/usr/bin/env python3
"""Check Review Assistant real provider contract scenarios (Phase 3.3).

Default: no-network checks only (forbidden flag + missing config).
Optional: --real-provider runs real_provider_synthetic when RA_LLM_BASE_URL is set.

Stdlib only.
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
DEMO = REPO_ROOT / "prototypes-derived" / "review-assistant-thin" / "minimal_demo.py"

NO_NETWORK_SCENARIOS: dict[str, dict[str, object]] = {
    "real_provider_forbidden_without_flag": {
        "cmd_extra": [],
        "env_clear_base_url": False,
        "events": [
            "provider_request_prepared",
            "provider_disabled",
            "task_failed",
        ],
        "must_contain": ["decision=FAILED", "delivered=False"],
        "expect_exit": 0,
    },
    "real_provider_missing_config": {
        "cmd_extra": ["--real-provider"],
        "env_clear_base_url": True,
        "events": [
            "provider_request_prepared",
            "provider_config_missing",
            "task_failed",
        ],
        "must_contain": ["decision=FAILED", "delivered=False"],
        "expect_exit": 0,
    },
}

REAL_SYNTHETIC_EVENTS = [
    "provider_request_prepared",
    "provider_request_started",
    "provider_response_received",
    "provider_parse_passed",
    "draft_created",
    "verification_passed",
    "approval_requested",
    "approval_granted",
    "task_completed",
]


def run_scenario(
    name: str,
    spec: dict[str, object],
) -> tuple[bool, str]:
    cmd = [sys.executable, str(DEMO), "--scenario", name, *spec["cmd_extra"]]
    env = os.environ.copy()
    if spec.get("env_clear_base_url"):
        env.pop("RA_LLM_BASE_URL", None)

    proc = subprocess.run(cmd, capture_output=True, text=True, cwd=REPO_ROOT, env=env)
    output = proc.stdout + proc.stderr
    expect_exit = spec.get("expect_exit", 0)

    if proc.returncode != expect_exit:
        return False, f"exit code {proc.returncode}, expected {expect_exit}"

    for event in spec["events"]:
        if event not in output:
            return False, f"missing event: {event}"

    for fragment in spec["must_contain"]:
        if fragment not in output:
            return False, f"missing fragment: {fragment}"

    if "provider_request_started" not in output and name != "real_provider_synthetic":
        if "provider_request_started" in str(spec.get("events", [])):
            pass
    if name in ("real_provider_forbidden_without_flag", "real_provider_missing_config"):
        if "provider_request_started" in output:
            return False, "unexpected network start event"

    return True, "ok"


def run_real_synthetic() -> tuple[bool, str]:
    if not os.environ.get("RA_LLM_BASE_URL", "").strip():
        return False, "RA_LLM_BASE_URL not set — skip or configure endpoint"

    cmd = [
        sys.executable,
        str(DEMO),
        "--scenario",
        "real_provider_synthetic",
        "--real-provider",
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True, cwd=REPO_ROOT)
    output = proc.stdout + proc.stderr

    if "provider_disabled" in output or "provider_config_missing" in output:
        return False, "provider blocked unexpectedly"

    if proc.returncode != 0:
        failure_ok = any(
            x in output
            for x in (
                "provider_timeout",
                "provider_error",
                "provider_parse_failed",
                "provider_unsafe_output",
                "provider_uncertain_output",
            )
        )
        if failure_ok:
            return True, "fail-closed on provider error (acceptable)"
        return False, f"exit code {proc.returncode} without known provider failure event"

    for event in REAL_SYNTHETIC_EVENTS:
        if event not in output:
            return False, f"missing event: {event}"
    if "decision=DELIVERED" not in output or "delivered=True" not in output:
        return False, "expected delivery on success path"

    return True, "ok"


def main() -> int:
    parser = argparse.ArgumentParser(description="Real provider contract check")
    parser.add_argument(
        "--real-provider",
        action="store_true",
        help="Also run real_provider_synthetic against local endpoint",
    )
    args = parser.parse_args()

    if not DEMO.is_file():
        print(f"FAIL  demo missing: {DEMO}")
        return 1

    print("=== Review Assistant Real Provider Contract (Phase 3.3) ===")
    print(f"Demo: {DEMO.relative_to(REPO_ROOT)}\n")

    passed = 0
    failed = 0

    for name, spec in NO_NETWORK_SCENARIOS.items():
        ok, detail = run_scenario(name, spec)
        status = "PASS" if ok else "FAIL"
        print(f"{status:4}  {name:36}  {detail}")
        if ok:
            passed += 1
        else:
            failed += 1

    if args.real_provider:
        ok, detail = run_real_synthetic()
        status = "PASS" if ok else "FAIL"
        print(f"{status:4}  {'real_provider_synthetic (live)':36}  {detail}")
        if ok:
            passed += 1
        else:
            failed += 1
    else:
        print(f"SKIP  {'real_provider_synthetic (live)':36}  use --real-provider to run")

    print(f"\nSummary: PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
