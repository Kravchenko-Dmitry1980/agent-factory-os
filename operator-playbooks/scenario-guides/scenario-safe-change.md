# Scenario: Safe Change

## What It Teaches

How to modify behavior without erasing gates — propose → implement small → evaluate → accept or rollback.

## What Can Go Wrong

- Large refactor + behavior change together
- Skip evaluation because "small change"
- Fix failing demo by removing escalation

## Correct Safe Behavior

- Baseline smoke PASS
- Change proposal answers "which gate moves?"
- Post-change smoke + trace compare
- FAIL → rollback first

## Files to Run

```powershell
# Before
python evaluation/scripts/run_demo_smoke_checks.py

# After change
python evaluation/scripts/run_demo_smoke_checks.py
python evaluation/scripts/check_expected_text_traces.py
```

## Traces to Inspect

- Before/after demo audit for affected scenario
- `evaluation/trace-comparison/trace-regression-examples.md`

## Evaluation Checks

- `evaluation/scenarios/evolution-change-scenarios.md`
- `evaluation/quality-gates/quality-gate-checklist.md`

## Deep Docs

- [../change-guides/how-to-change-safely.md](../change-guides/how-to-change-safely.md)
- [../runbooks/perform-safe-change.md](../runbooks/perform-safe-change.md)
- `evolution/README.md`
