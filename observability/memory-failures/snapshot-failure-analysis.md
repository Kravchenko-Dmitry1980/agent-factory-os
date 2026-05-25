# Snapshot Failure Analysis

## Frozen Snapshot Semantics

1. Snapshot created at session start
2. Mid-session writes go to durable only
3. Agent reasoning uses snapshot unless explicit reload

## Failure Scenarios

| Scenario | Symptom | Trace fix |
|----------|---------|-----------|
| Operator expects instant recall | "Forgot" | Log `snapshot_unchanged=true` |
| Reload skipped | Wrong facts | Log `context_load` with query |
| Rollback needed | Bad write rejected | No durable change — log reject |
| Session never reset | Long stale period | Log `session_reset` on boundary |

## Good Trace

```
snapshot_frozen
execute
critique
verification_passed
memory_write_accepted snapshot_unchanged=true
```

## Bad Trace

```
saved memory
(later) confused agent
```

No causal link.
