# Fail-Closed External Action — Governance

| Rule | Behavior |
|------|----------|
| Deny-by-default | `approval=None` → deny |
| No auto-execution | All paths through gate |
| Audit logging | Every propose/verify/gate/execute |
| Uncertainty = deny | Fail-closed |
| High-risk HITL | `risk_level=high` requires explicit True |

## Alignment

- `Books/swarm-playbooks/hitl/human-approval-boundaries.md`
- `agent-os/08_patterns/fail-closed-agent-loop.md`
