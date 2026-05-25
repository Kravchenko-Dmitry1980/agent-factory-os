# Project Lead Path

---

## Goal

Orient without running every demo: understand risks, promotion discipline, operator safety, change governance.

## Estimated Time

3–4 hours

---

## What to Read

| Priority | Document |
|----------|----------|
| High | [../README.md](../README.md) |
| High | `agent-os/doctrine/system-positioning.md` |
| High | `governance/PROMOTION_STRATEGY.md` |
| High | [../governance/operator-boundaries.md](../governance/operator-boundaries.md) |
| Medium | `evolution/README.md` |
| Medium | `evaluation/regression-matrix/safety-regression-matrix.md` |
| Medium | [../onboarding/onboarding-for-project-lead.md](../onboarding/onboarding-for-project-lead.md) |

---

## What to Run (Minimal)

```powershell
python evaluation/scripts/summarize_evaluation_status.py
```

Optional: one happy + one fail demo with team member narrating.

---

## What to Avoid

- Pressure to "productize" prototypes for deadline
- Skipping evaluation before merge on gate-touching changes
- Letting team add CI without new phase charter
- Confusing research corpus (`Books/`) with canonical doctrine

---

## Expected Outcome

- Can explain repo to stakeholder in 5 minutes
- Knows what interns must not touch
- Can ask right questions on change proposals (which gate moves?)

---

## Checkpoint Questions

1. What is the promotion path into agent-os?
2. What are top 3 safety regressions from evaluation matrix?
3. Is this repo a deployment platform?
4. What must remain human-operated?

Answers in [../onboarding/onboarding-for-project-lead.md](../onboarding/onboarding-for-project-lead.md)
