# How to Run Regression Check

Local only — no CI.

---

## Quick check (5 min)

```powershell
python evaluation/scripts/run_demo_smoke_checks.py
python evaluation/scripts/check_expected_text_traces.py
```

---

## Full check (gate-touching change)

1. Smoke scripts above
2. Run scenarios from `evaluation/scenarios/` for affected area
3. Manual trace compare — `evaluation/trace-comparison/trace-diff-checklist.md`
4. Quality gates — `evaluation/quality-gates/quality-gate-checklist.md`
5. Red flags — `evaluation/manual-review/red-flag-checklist.md`

---

## Compare traces

Before change: save demo output (optional)  
After change: same command, same scenario

Read: `evaluation/trace-comparison/good-trace-vs-bad-trace.md`

---

## Verdict

| Result | Action |
|--------|--------|
| All pass | Human sign-off |
| Smoke fail | Rollback |
| Trace thin | Rollback or fix audit |

Runbook: [../runbooks/run-evaluation-checks.md](../runbooks/run-evaluation-checks.md)
