# Escalation Patterns

| Pattern | Trigger | Visible event | Wrong response |
|---------|---------|---------------|----------------|
| **Retry exhaustion** | `retry_count >= max` | `retry_exhausted`, `escalation_triggered` | Silent drop |
| **Approval timeout** | No human in window | `approval_timeout` | Auto-approve |
| **Uncertainty** | Critic/LLM uncertain | `escalation_triggered` | Treat as pass |
| **Repeated verification fail** | Same gate fails N times | `verification_failed` chain | Infinite retry |
| **Queue dead-end** | No consumer / corrupt | `task_failed` or corrupt flag | Restart without audit |

## Repository References

- `prototypes/integrations/escalation-workflow/`
- `integrations-real/telegram-review-gate/` — timeout deny
- `integrations-real/local-queue-worker/` — SQLite escalation

## Diagnostic Question

> Did escalation fire **before** unsafe continuation?

If continuation happened first — governance bug, not ops issue.
