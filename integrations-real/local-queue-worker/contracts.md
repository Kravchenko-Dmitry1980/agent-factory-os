# Local Queue Worker — Contracts

## Inputs

| Field | Type | Required |
|-------|------|----------|
| `goal` | string | enqueue |
| `max_retries` | int | default 3 |

## Outputs

| Field | Type | When |
|-------|------|------|
| `task_id` | string | enqueue |
| `status` | enum | terminal |
| `retry_count` | int | each attempt |

## Verification

- Worker output checked before complete

## Approval Boundaries

N/A — internal queue

## Escalation

- retry_count >= max → escalated

## Failure States

| State | Meaning |
|-------|---------|
| ESCALATED | Max retries |
| CORRUPT | Invalid row |
| STOPPED | Fail-closed |
