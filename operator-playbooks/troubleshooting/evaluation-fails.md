# Evaluation Fails

## Symptom

`run_demo_smoke_checks.py` shows FAIL or `check_expected_text_traces.py` missing events.

## Smoke FAIL

1. Read which check failed (name column)
2. Run that demo alone — read stdout
3. If `missing expected text` — demo output changed (maybe regression)
4. If `exit non-zero` — demo broken — [demo-does-not-run.md](demo-does-not-run.md)

## Trace check FAIL

Example trace file edited or corrupted. Compare to git version:

```powershell
git diff observability/examples/
```

Required events listed in `evaluation/scripts/check_expected_text_traces.py`.

## After your change

**Assume regression until proven otherwise.** Rollback → re-run smoke.

## If FAIL without your change

- Environment issue (Python path)
- Report to lead with command output

## What NOT to do

- Edit smoke script to weaken expectations without governance review
- Add pytest to replace evaluation layer

See [../runbooks/run-evaluation-checks.md](../runbooks/run-evaluation-checks.md)
