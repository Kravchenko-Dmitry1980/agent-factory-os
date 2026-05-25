# Queue Recovery Analysis

## Recovery Event

`queue_recovered` — worker restarted, pending tasks reloaded from durable store.

## Trace (Recovery)

```
task_started (enqueued)
verification_failed
retry_triggered
(task_running interrupted — process exit)
queue_recovered pending_count=1
task_started (same task_id)
verification_passed
task_completed
```

## What Must Be Visible

1. Pre-crash last known status
2. Recovery action
3. Retry count preserved or reset (document which)

## Phase 2.2 Demo

`integrations-real/local-queue-worker/minimal-demo.py --scenario recovery`

## Failure

Recovery without audit → operator cannot trust queue state.
