# Run Evaluation Checks

## Purpose

Locally verify demos still run and example traces still contain required events.

## When to Use

- Start of work session (optional habit)
- **Required** after changing prototypes, shared gates, or adapters
- Before accepting a change proposal

## Commands

```powershell
cd C:\Dima\Projects\CURSOR\AGENT

python evaluation/scripts/run_demo_smoke_checks.py
python evaluation/scripts/check_expected_text_traces.py
python evaluation/scripts/summarize_evaluation_status.py
```

## Expected Result

```
Smoke: PASS=12 FAIL=0 NOT_RUN=0  (count may vary if checks list grows)
Trace: PASS=6 FAIL=0 total=6
Summary: lists modules and script status
```

Smoke FAIL is not panic — inspect which demo failed.

## Common Failures

See [../troubleshooting/evaluation-fails.md](../troubleshooting/evaluation-fails.md)

## What to Do If It Fails

1. Read FAIL line — which demo?
2. Run that demo alone — see stdout
3. Compare to [../../evaluation/scenarios/](../../evaluation/scenarios/)
4. If your change caused it — rollback first

## What NOT to Do

- Do not add CI to run these automatically (Phase 2.5 rule)
- Do not weaken smoke expectations to get green
- Do not treat smoke PASS as full behavioral proof — still do manual trace compare for gate changes

Reference: [../../evaluation/README.md](../../evaluation/README.md)
