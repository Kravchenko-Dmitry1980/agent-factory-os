# Exercise: Decide Rollback

## Purpose

Practice rollback judgment using narratives — not live breaking code.

## Time

20 minutes

## Steps

1. Read `evolution/examples/unsafe-retry-increase.md`
2. Read `evolution/examples/rollback-success.md`
3. Scenario card (mentor or self):

   *Smoke passed but approval_requested missing from review demo audit after teammate's change.*

4. Write decision: rollback yes/no + 3 bullet reasoning
5. Compare to [../operator-playbooks/runbooks/rollback-after-failure.md](../operator-playbooks/runbooks/rollback-after-failure.md)

## Expected Result

Decision: **rollback first** — missing approval is critical regression.

## What To Observe

- Exit code 0 can still be governance FAIL
- Rollback restores known-good gates

## Questions

1. Rollback vs forward fix under deadline?
2. What smoke would you re-run after revert?

## Pass Criteria

Chooses rollback for missing approval; cites audit/thin trace; re-run smoke mentioned.

## Fail Criteria

"Ship anyway"; patch approval check without revert.
