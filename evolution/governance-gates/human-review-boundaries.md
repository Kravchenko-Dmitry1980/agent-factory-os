# Human Review Boundaries

Humans required when automation must **not** decide alone.

## Always Human

- External publish / send
- High-risk GUI actions
- Promotion to canonical agent-os
- Override after escalation
- Policy exception to fail-closed

## Never "Human Optional"

Because internal, staging, or trusted user.

## Change Review

If proposal removes human step → **risk 5** — reject unless new stronger gate replaces.

## Observability

Trace must show `approval_requested` before external `task_completed`.

## Alignment

- `Books/swarm-playbooks/hitl/`
- `integrations-real/telegram-review-gate/`
