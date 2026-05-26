# Rollback Gate

## Purpose

Ensure every template change has a documented path to revert to a known-good frozen version.

## When Required

Before applying any change to **accepted** or **frozen** templates.

## Pass Condition

- Change proposal completed (see [change-proposal-spec.md](../template-specs/change-proposal-spec.md))
- Previous version identified
- Rollback steps documented
- Eval scenarios to rerun listed
- Approver named

## Fail Condition

- In-place edit of frozen template without proposal
- No version identifier
- No eval rerun plan

## Example

Review Assistant v0.1 → v0.2: rollback = restore v0.1 folder snapshot from git tag; rerun all five evaluation scenarios.

## Related Anti-patterns

- Platform drift
- Framework extraction
- Missing evaluation
