# After Changing Workflow

- [ ] Smoke checks re-run — PASS or explained FAIL
- [ ] Trace compare for affected scenarios
- [ ] Quality gate checklist (`evaluation/quality-gates/quality-gate-checklist.md`)
- [ ] Fail-path demo still fails correctly
- [ ] No new dependencies without justification
- [ ] Change proposal updated with results
- [ ] If FAIL → rollback, do not stack fixes

```powershell
python evaluation/scripts/run_demo_smoke_checks.py
python evaluation/scripts/check_expected_text_traces.py
```

Human sign-off for gate-touching changes.
