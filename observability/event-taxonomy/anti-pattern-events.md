# Anti-Pattern Events

Events that indicate **observability or governance regression**.

| Anti-pattern event | Why it is bad |
|--------------------|---------------|
| `silent_complete` | Terminal success without verification event |
| `auto_approved` | No `approval_requested` before external action |
| `critic_equals_truth` | Publish after critique only, no human/verify |
| `retry_without_audit` | Retry count increases, no `retry_triggered` |
| `memory_write_silent` | Durable store changed, no write event |
| `escalation_suppressed` | Max retries hit, no `escalation_triggered` |
| `metric_only_failure` | Error counted in dashboard, no readable reason |

## Detection (Manual)

Review audit JSONL or trace files for:

1. Missing gate events between stages
2. Jumps from `task_started` → `task_completed`
3. High retry count with single log line

## Response

Fix workflow instrumentation in demo/adapter — not add Prometheus counter.
