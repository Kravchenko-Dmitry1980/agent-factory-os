# Memory Boundary Gate

## Purpose

Prevent unbounded, hidden, or unapproved memory growth.

## When Required

Any template that reads or writes memory beyond ephemeral task context.

## Pass Condition

- Memory policy documented
- Writes emit audit events
- Persistent writeback requires human approval
- Over-limit writes → `memory_write_rejected`

## Fail Condition

- Infinite conversation memory
- Automatic profile mutation
- Silent long-term writeback
- No reset policy

## Example

Review Assistant v0.1: task context only. Attempt to save user profile without approval → `memory_write_rejected reason=no_approval`.

## Related Anti-patterns

- Unbounded memory
- Hidden autonomy
- Missing audit
