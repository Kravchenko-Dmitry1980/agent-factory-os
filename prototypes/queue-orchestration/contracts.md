# Queue Orchestration — Contracts

## Inputs

| Field | Type | Required |
|-------|------|----------|
| `goal` | string | yes |
| `task_id` | string | auto |
| `max_retries` | int | default 3 |

## Outputs

| Field | Type | When |
|-------|------|------|
| `status` | enum | terminal |
| `retry_count` | int | each attempt |
| `verification_result` | pass/fail | after worker |
| `escalated` | bool | after max retries |

## Verification Points

- Worker output checked before marking complete
- Retry only on verification fail, not on success

## Failure States

| State | Meaning |
|-------|---------|
| `VERIFY_FAIL` | Worker output invalid |
| `RETRY_EXHAUSTED` | Max retries reached |
| `ESCALATED` | Human/supervisor notified |

## Escalation Points

- `retry_count >= max_retries` → escalate, stop retry (fail-closed)
