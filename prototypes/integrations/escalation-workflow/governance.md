# Escalation — Governance

| Parameter | Default |
|-----------|---------|
| MAX_RETRIES | 3 |
| Escalation threshold | same as max retries |
| Uncertainty handling | retry then escalate |
| Terminal stop | No auto-complete after escalate |

## Fail-Closed

After escalation: status=ESCALATED, completed=False, audit records denial.

## Alignment

- `Books/swarm-playbooks/hitl/escalation-to-human.md`
- `prototypes/queue-orchestration/`
