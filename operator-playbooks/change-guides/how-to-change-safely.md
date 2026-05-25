# How to Change Safely

## Rule

**Small change → verify behavior → accept or rollback.** Never stack unverified fixes.

---

## Steps

1. **Read** [../start-here/what-not-to-touch.md](../start-here/what-not-to-touch.md)
2. **Propose** — [how-to-write-change-proposal.md](how-to-write-change-proposal.md)
3. **Baseline** — `python evaluation/scripts/run_demo_smoke_checks.py`
4. **Impact** — [how-to-check-impact.md](how-to-check-impact.md)
5. **Implement** — one invariant at a time
6. **Regress** — [how-to-run-regression-check.md](how-to-run-regression-check.md)
7. **Decide** — accept or [how-to-decide-rollback.md](how-to-decide-rollback.md)

---

## Checklists

- [../operator-checklists/before-changing-workflow.md](../operator-checklists/before-changing-workflow.md)
- [../operator-checklists/after-changing-workflow.md](../operator-checklists/after-changing-workflow.md)

---

## Runbook

[../runbooks/perform-safe-change.md](../runbooks/perform-safe-change.md)

---

## If Using Cursor / AI

- Reject suggestions that merge demos into framework
- Reject gate removal for "simplicity"
- Always re-run smoke after AI edits

[../learning-paths/cursor-operator-path.md](../learning-paths/cursor-operator-path.md)

---

## Evolution Layer

- `evolution/change-proposals/`
- `evolution/governance-gates/gate-checklists.md`
