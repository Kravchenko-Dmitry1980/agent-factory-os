# Onboarding for Project Lead

You need orientation, not every demo memorized.

---

## 5-minute pitch

This repo teaches **governed AI workflows**: verify first, fail closed, human approval, bounded memory, readable traces. It is **not** a product you deploy.

---

## What to expect from team

| Role | Minimum |
|------|---------|
| Intern | Pass assessment week 1; no solo shared code |
| Developer | Smoke + trace compare on gate changes |
| Everyone | No platform extraction without review |

---

## Your review questions on changes

1. Which gate moved?
2. Did evaluation run?
3. Can trace explain the decision?
4. Is rollback defined?

---

## Key docs

- [../README.md](../README.md)
- `governance/PROMOTION_STRATEGY.md`
- `governance/PHASE_2_5_EVALUATION_REVIEW.md`
- [../governance/operator-boundaries.md](../governance/operator-boundaries.md)

---

## One command for health

```powershell
python evaluation/scripts/summarize_evaluation_status.py
```

---

## Risk to watch

Team pressure to productize prototypes → redirect to operator boundaries.
