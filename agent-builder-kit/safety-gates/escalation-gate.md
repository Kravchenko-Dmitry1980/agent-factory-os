# Escalation Gate

## Purpose

Route unresolved ambiguity, policy conflict, or repeated failure to a human operator.

## When Required

When verification fails with uncertainty, human denies repeatedly, or automation cannot proceed safely.

## Pass Condition

- Emit `escalation_triggered` with reason
- Automation stops
- Human/supervisor path documented
- Terminal decision recorded in trace

## Fail Condition

- Infinite retry loop without escalation
- Uncertainty auto-resolved by LLM
- Escalation without audit trail

## Example

Critic uncertain + verification failed → `escalation_triggered reason=critic_uncertain` → held for human.

## Related Anti-patterns

- Missing escalation
- Unbounded revision loop
- Critic treated as truth
