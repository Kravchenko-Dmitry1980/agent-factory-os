# Retry Storms

## Definition

Retries continue without progress, escalation, or changing inputs.

## Trace Signature

```
retry_triggered retry=1
retry_triggered retry=2
retry_triggered retry=3
retry_triggered retry=4   ← ceiling bug if no escalation_triggered
```

## Cost Signals (Human-Readable)

- Same `task_id` repeated
- Same `reason=` on each retry
- Growing token/API usage mentioned in postmortem notes — **not** metric dashboards

## Correct Pattern

```
retry_triggered retry=3
retry_exhausted
escalation_triggered
OUTCOME status=escalated
```

## Fix

Lower ceiling, change input, or escalate — not add workers.
