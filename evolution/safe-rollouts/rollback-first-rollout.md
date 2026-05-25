# Rollback-First Rollout

Before expanding change, **practice rollback once**.

## Steps

1. Tag or note current commit hash
2. Apply change
3. Run validation stages
4. Execute rollback procedure
5. Confirm failure scenarios still pass on reverted code
6. Re-apply change if still desired

## Why

Proves rollback plan is real — not fantasy.

## Time Box

If rollback takes > 15 minutes to figure out — simplify change.

## Tie-In

[rollback-thinking/rollback-triggers.md](../rollback-thinking/rollback-triggers.md)
