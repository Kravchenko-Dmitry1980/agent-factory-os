# Verification Gate

## Purpose

Explicit check that output meets policy, format, and factual constraints **before** progress or delivery.

## When Required

Before human review handoff and before any external action.

## Pass Condition

- Emit `verification_passed` with actor and scope
- Checks documented in template
- Failed checks emit `verification_failed` and stop pipeline

## Fail Condition

- Skip verification on "happy" critic pass
- Conflate critique with verification
- Publish on verification failure without human override + audit

## Example

Draft passes format check → `verification_passed actor=validator`. Hallucinated claim detected → `verification_failed actor=validator reason=unverified_fact`.

## Related Anti-patterns

- Critic treated as truth
- LLM output treated as truth
- Missing audit
