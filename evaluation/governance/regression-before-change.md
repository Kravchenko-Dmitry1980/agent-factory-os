# Regression Before Change

**Rule:** Check behavior **before** declaring a change safe — not only after production incident.

---

## Before Coding (Light)

- Identify affected critical behaviors (`regression-matrix/critical-behavior-matrix.md`)
- Note baseline scenario commands

---

## Before Accepting Change (Required)

1. Run `evaluation/scripts/run_demo_smoke_checks.py`
2. Run affected scenario demos manually
3. Compare trace to baseline or `observability/examples/`
4. Complete applicable quality gates
5. Human reviewer checklist

---

## After Change (If FAIL)

1. Rollback (`git revert` or file restore)
2. Document in `evolution/change-proposals/` if governance touched
3. Re-run smoke to confirm rollback restored behavior

---

## Link to Evolution Phase

Phase 2.4 = change discipline  
Phase 2.5 = behavioral proof

Together:

```text
propose → impact analysis → implement → evaluate (2.5) → accept or rollback
```

Evaluation does not replace evolution governance — it **verifies** it.

---

## Anti-Pattern

"Ship now, add tests later" → governance regression accumulates.

Correct: small change + immediate local scenario re-run.
