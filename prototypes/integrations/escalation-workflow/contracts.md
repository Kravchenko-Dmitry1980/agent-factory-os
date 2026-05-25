# Escalation — Contracts

## Inputs

| Field | Type | Required |
|-------|------|----------|
| `task` | string | yes |
| `max_retries` | int | default 3 |
| `escalation_threshold` | int | default 3 |

## Outputs

| Field | Type | When |
|-------|------|------|
| `status` | running/retry/escalated/stopped/completed | terminal |
| `retry_count` | int | each attempt |
| `denial_reason` | string | if stopped |

## Verification Points

- Confidence check after execution
- Retry only on recoverable uncertain (not on hard fail)

## Escalation Points

- retry_count >= max_retries
- Immediate uncertainty (scenario)

## Approval Boundaries

- No auto-continue after escalation
- Human must acknowledge (mock: stop state)

## Failure States

| State | Meaning |
|-------|---------|
| `DENIED` | Fail-closed stop |
| `ESCALATED` | Human required |
| `RETRY_EXHAUSTED` | Ceiling hit |
