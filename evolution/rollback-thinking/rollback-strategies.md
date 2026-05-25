# Rollback Strategies

| Strategy | When | Action |
|----------|------|--------|
| **Git revert** | Code gate regression | Restore prior demo behavior |
| **Behavior flag** | Demo scenario only | Default to safe mock path |
| **Disable adapter** | Real I/O failure | Run mock mode only |
| **Freeze promotion** | Governance doc drift | Stop agent-os integration |
| **Restore constants** | Retry/ceiling change | MAX_RETRIES back to known value |
| **Doc rollback** | Wrong observability taxonomy | Revert canonical event rename |

## Not a Strategy

"Fix forward" under incident without gate analysis — adds entropy.

## Audit During Rollback

Append rollback events — never delete audit history:

```
governance_rejection reason=rollback initiated
task_failed reason=reverted change CHG-042
```

## Local-First

No K8s rollout undo — file-level revert sufficient for this repository.
