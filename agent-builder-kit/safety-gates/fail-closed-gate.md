# Fail-Closed Gate

## Purpose

Default to **stop** when uncertain, unverified, or unapproved. Never assume success.

## When Required

Every agent template. Non-negotiable.

## Pass Condition

- Ambiguity → block or escalate, not auto-proceed
- Missing approval → no risky action
- Verification unknown → treat as failed
- Timeout → deny-by-default

## Fail Condition

- Auto-proceed on uncertainty
- Silent skip of gates
- Default-allow for external actions

## Example

Critic returns `uncertain` on fabricated revenue figures → workflow stops → `verification_failed` → human must decide.

Reference: `evaluation/scenarios/review-loop-scenarios.md` (Critic Uncertain)

## Related Anti-patterns

- LLM output treated as truth
- Missing approval
- Hidden autonomy
- Critic treated as truth
