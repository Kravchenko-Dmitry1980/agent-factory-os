# Module 11 — Safe Evolution

## Goal

Change the system without silently removing gates.

## Simple Explanation

**Safe evolution** = propose change → check impact → small edit → evaluate → accept or **rollback**. Forward patches under pressure often hide regressions.

## Key Ideas

- Change proposals required for gate touches
- Rollback before complexity
- Drift detection (retry creep, auto-approve)
- Impact analysis on shared modules

## Files to Read

- `evolution/README.md`
- `evolution/change-proposals/change-template.md`
- [../operator-playbooks/change-guides/how-to-change-safely.md](../operator-playbooks/change-guides/how-to-change-safely.md)

## Commands to Run

Before/after any practice change (with mentor):

```powershell
python evaluation/scripts/run_demo_smoke_checks.py
```

## Exercise

[../exercises/exercise-write-change-proposal.md](../exercises/exercise-write-change-proposal.md)  
[../exercises/exercise-decide-rollback.md](../exercises/exercise-decide-rollback.md)

## Common Mistakes

- Skip proposal for "tiny" gate change
- Stack fixes without rollback
- Shared runtime extraction

## Checkpoint Questions

1. What must a change proposal answer about gates?
2. When rollback before debug?
3. Name one drift early warning signal.

## Expected Outcome

Student drafts a one-page change proposal for a hypothetical retry limit change.
