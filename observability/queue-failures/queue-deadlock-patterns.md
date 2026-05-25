# Queue Deadlock Patterns

| Pattern | Symptom | Event gap |
|---------|---------|-----------|
| **Pending forever** | Tasks in pending, no worker | No `task_started` after enqueue |
| **Running stuck** | Status running, no complete | No terminal event |
| **Corrupt head** | Dequeue fails | `queue corruption` / missing dequeue |
| **Escalation loop** | Re-enqueue escalated tasks | Missing terminal deny |

## integrations-real/local-queue-worker

Corruption and recovery scenarios emit audit — compare:

- Happy: `enqueued → running → completed`
- Dead: `enqueued → (silence)`

## Human Diagnostic

Open SQLite / JSONL — count rows by status. No dashboard required.

```powershell
# Example: inspect integrations-real/.data/local-queue-worker/audit.jsonl
```

## Not Deadlock

Escalated task waiting for human — status `escalated`, outcome documented.
