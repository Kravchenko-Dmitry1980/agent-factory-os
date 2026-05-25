#!/usr/bin/env python3
"""Print human-readable summary of evaluation coverage and local check status."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EVAL = ROOT / "evaluation"


def count_markdown(folder: Path) -> int:
    if not folder.is_dir():
        return 0
    return len(list(folder.glob("*.md")))


def run_script(rel_path: str) -> str:
    script = ROOT / rel_path
    if not script.exists():
        return "NOT_RUN (script missing)"
    result = subprocess.run(
        [sys.executable, str(script)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=300,
        check=False,
    )
    last_line = ""
    for line in (result.stdout + result.stderr).splitlines():
        if line.startswith("Summary:"):
            last_line = line
    if not last_line and result.returncode == 0:
        last_line = "completed (no summary line)"
    elif not last_line:
        last_line = f"exit {result.returncode}"
    return last_line


def main() -> int:
    print("=== Evaluation Status Summary (Phase 2.5) ===\n")

    modules = {
        "scenarios": EVAL / "scenarios",
        "expected-outcomes": EVAL / "expected-outcomes",
        "trace-comparison": EVAL / "trace-comparison",
        "regression-matrix": EVAL / "regression-matrix",
        "quality-gates": EVAL / "quality-gates",
        "manual-review": EVAL / "manual-review",
        "failure-injection": EVAL / "failure-injection",
        "diagrams": EVAL / "diagrams",
        "governance": EVAL / "governance",
        "scripts": EVAL / "scripts",
    }

    print("Documentation modules:")
    for name, path in modules.items():
        if name == "scripts":
            py_count = len(list(path.glob("*.py"))) if path.is_dir() else 0
            print(f"  {name:22}  {py_count} script(s)")
        else:
            print(f"  {name:22}  {count_markdown(path)} file(s)")

    print("\nRequired scenario files (8):")
    required_scenarios = [
        "review-loop-scenarios.md",
        "bounded-memory-scenarios.md",
        "queue-orchestration-scenarios.md",
        "fail-closed-action-scenarios.md",
        "gui-verification-scenarios.md",
        "promotion-pipeline-scenarios.md",
        "real-adapter-scenarios.md",
        "evolution-change-scenarios.md",
    ]
    missing_scenarios = [
        name for name in required_scenarios if not (EVAL / "scenarios" / name).exists()
    ]
    if missing_scenarios:
        print(f"  MISSING: {', '.join(missing_scenarios)}")
    else:
        print("  All present")

    print("\nQuality gates (7 + checklist):")
    gate_files = list((EVAL / "quality-gates").glob("*.md")) if (EVAL / "quality-gates").is_dir() else []
    print(f"  {len(gate_files)} gate file(s)")

    print("\nObservability example traces:")
    examples = ROOT / "observability" / "examples"
    trace_count = len(list(examples.glob("*-trace.txt"))) if examples.is_dir() else 0
    print(f"  {trace_count} example trace file(s)")

    print("\nLocal script runs (optional quick status):")
    print(f"  smoke checks: {run_script('evaluation/scripts/run_demo_smoke_checks.py')}")
    print(f"  trace check:  {run_script('evaluation/scripts/check_expected_text_traces.py')}")

    print("\nBoundaries:")
    print("  - Local only (no CI/CD in evaluation/)")
    print("  - No benchmark platform")
    print("  - Human review required for verdict on changes")

    print("\nNext steps for reviewer:")
    print("  1. evaluation/quality-gates/quality-gate-checklist.md")
    print("  2. evaluation/manual-review/reviewer-checklist.md")
    print("  3. evaluation/regression-matrix/regression-matrix.md")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
