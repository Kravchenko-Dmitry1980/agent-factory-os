# Onboarding for AI Developer

For developers who will edit prototypes/adapters and use Cursor heavily.

---

## Path

1. [../learning-paths/ai-architect-path.md](../learning-paths/ai-architect-path.md)
2. [../learning-paths/cursor-operator-path.md](../learning-paths/cursor-operator-path.md)
3. [../change-guides/how-to-change-safely.md](../change-guides/how-to-change-safely.md)

---

## Daily habit

```powershell
python evaluation/scripts/run_demo_smoke_checks.py
```

After every behavioral edit — run again.

---

## Read once

- All `prototypes/*/contracts.md` for demos you touch
- `evaluation/regression-matrix/critical-behavior-matrix.md`
- `evolution/impact-analysis/hidden-coupling-analysis.md`

---

## Cursor rules

- Reject framework extraction PRs from AI
- Require fail-path demo still fails after change
- Link change proposal in commit message for gate changes

---

## Assessment

[onboarding-assessment.md](onboarding-assessment.md) — self + peer review
