# Example: Rollback Success

## Situation

Review-queue change broke `approval-denied` scenario.

## Action

1. Git revert single commit
2. Re-run all `--scenario` flags
3. Append audit note: `rollback change CHG-107`
4. Update change proposal: rejected forward fix

## Result

Traces match [observability/examples/failed-review-trace.txt](../../observability/examples/failed-review-trace.txt).

## Time

< 20 minutes.

## Lesson

[rollback-first-rollout.md](../safe-rollouts/rollback-first-rollout.md) validated.
