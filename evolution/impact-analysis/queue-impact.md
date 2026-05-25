# Queue Impact

## Sensitive Changes

- Raise `MAX_RETRIES` without escalation review
- Remove `ESCALATED` terminal state
- Drop audit on retry
- Durable queue without recovery test
- Parallel workers (out of scope — platform drift)

## Side Effects

| Change | Symptom |
|--------|---------|
| +retries | Cost, masked bugs |
| No escalation | Silent drop |
| Corrupt handling removed | Double processing |

## Test Scenarios

- `retry-exhaustion` integration demos
- `recovery` local-queue-worker
- Trace must show `retry_exhausted` → `escalation_triggered`

## Reference

[observability/queue-failures/](../../observability/queue-failures/)
