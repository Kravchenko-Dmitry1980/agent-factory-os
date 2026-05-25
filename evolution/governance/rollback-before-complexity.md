# Rollback Before Complexity

When under pressure:

```
Option A: 4 patches + new abstraction
Option B: git revert + rethink proposal
```

**Choose B** when:

- Gates regressed
- shared/ grew
- Escalation or HITL touched
- Trace missing events

## Complexity Debt

Each forward patch without rollback plan increases entropy — [architecture-entropy.md](../architecture-regression/architecture-entropy.md).

## Mantra

Stop before chaos. Restore known-good governance. Then change incrementally.
