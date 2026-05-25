# Governance Failure Analysis

When gates exist on paper but not in traces.

## Failure Modes

| Failure | Evidence |
|---------|----------|
| Gate bypass | Missing canonical event |
| Rubber-stamp human | Instant approve, no review time |
| Escalation black hole | ESCALATED status never triaged |
| Promotion without scan | integrate before scan event |
| Rollback without audit | history gap |

## Postmortem Template

1. Expected gate sequence
2. Actual trace
3. First missing event
4. Change that introduced gap
5. Rollback + prevention

## Systemic Cause

Often **speed over governance** — see [../governance/governance-over-speed.md](../governance/governance-over-speed.md).

## Fix Location

Workflow code or change process — not new monitoring SaaS.
