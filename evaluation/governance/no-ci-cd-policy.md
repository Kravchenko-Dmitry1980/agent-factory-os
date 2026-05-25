# No CI/CD Policy

Phase 2.5 evaluation **must not** become continuous integration or deployment automation.

---

## Prohibited

- `.github/workflows/` for evaluation
- Pre-commit hooks that run full eval suite
- Required GitHub check named "evaluation"
- Docker eval runner as merge gate
- Scheduled cloud eval jobs
- Deployment verification pipelines

---

## Why

| CI/CD goal | Phase 2.5 goal |
|------------|----------------|
| Block merge automatically | Help human decide |
| Scale across team | Teach local discipline |
| Always-on infrastructure | Zero infra |
| Coverage metrics | Governance invariants |

Automating gate checks too early **hides** false positives and encourages gaming metrics.

---

## Allowed Automation (Minimal)

Local scripts invoked manually:

```powershell
python evaluation/scripts/run_demo_smoke_checks.py
python evaluation/scripts/check_expected_text_traces.py
python evaluation/scripts/summarize_evaluation_status.py
```

Scripts report status; they do **not** modify git state or block pushes.

---

## If CI Need Arises Later

That is a **different phase** with explicit charter — not an extension of Phase 2.5.

Until then: red-flag any `.yml` workflow added for evaluation purposes.

---

## Verification

Repository should contain **zero** new GitHub Actions from Phase 2.5 work.
