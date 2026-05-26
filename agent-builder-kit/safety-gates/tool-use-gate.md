# Tool-Use Gate

## Purpose

Constrain which tools an agent may invoke and require approval for dangerous tools.

## When Required

Any template listing tools beyond pure text generation.

## Pass Condition

- Allowlist documented
- Each tool has permission level and approval rule
- Out-of-list invocation → `unsafe_action_blocked`
- Production writes require human gate

## Fail Condition

- Unrestricted shell
- Unrestricted filesystem
- External API action without approval
- Bypass path for publish

## Example

Bypass publish attempt → `unsafe_action_blocked reason=bypass_not_allowed` → `task_failed`.

Reference: `evaluation/scenarios/review-loop-scenarios.md` (Bypass Attempt Blocked)

## Related Anti-patterns

- Unsafe tool use
- Hidden autonomy
- Missing approval
