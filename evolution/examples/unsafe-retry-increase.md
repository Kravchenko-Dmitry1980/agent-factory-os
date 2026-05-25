# Example: Unsafe Retry Increase

## Change

`MAX_RETRIES` 3 → 10 in `local-queue-worker` "to reduce escalations."

## Intent

Fewer human interruptions.

## Risk

Masks verification bugs; cost storm; escalation rare → ops blind.

## Trace Before

```
retry_exhausted → escalation_triggered
```

## Trace After (regression)

```
retry_triggered retry=9 ... (no escalation yet)
```

## Governance Impact

Escalation gate weakened.

## Rollback

Restore `MAX_RETRIES = 3`; re-run `--scenario retry-exhaustion`.

## Lesson

Fix verification, not ceiling — [queue-impact.md](../impact-analysis/queue-impact.md).
