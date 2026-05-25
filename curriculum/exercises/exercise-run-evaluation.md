# Exercise: Run Evaluation

## Purpose

Use Phase 2.5 evaluation scripts as a student — understand PASS/FAIL meaning.

## Time

15 minutes

## Steps

1. Read `evaluation/README.md` (skim boundaries — not CI)
2. Run:

```powershell
python evaluation/scripts/run_demo_smoke_checks.py
python evaluation/scripts/check_expected_text_traces.py
python evaluation/scripts/summarize_evaluation_status.py
```

3. Pick one FAIL line (if any) and investigate with runbook

## Expected Result

Mostly PASS on clean repo. Summary lists modules.

## What To Observe

- Smoke checks multiple demos
- Trace check validates example files
- Scripts do not modify repo

## Questions

1. Smoke PASS means what — and what does it NOT mean?
2. Why not CI?

## Pass Criteria

Runs all three; explains smoke vs full behavioral proof.

## Fail Criteria

Cannot run scripts; thinks smoke replaces human review entirely.
