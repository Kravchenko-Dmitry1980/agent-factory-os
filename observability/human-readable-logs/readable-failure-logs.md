# Readable Failure Logs

## Template

```
[TIME] FAILURE_TYPE  actor=<gate|verifier|supervisor>
  workflow=<name>
  reason=<plain language>
  last_good_event=<canonical event>
  next_action=<retry|escalate|deny|human>
```

## Examples

### Approval Timeout

```
[20:02:01] approval_timeout  actor=gate
  workflow=telegram-review-gate
  reason=no human response within 2s (deny-by-default)
  last_good_event=approval_requested
  next_action=deny + escalate (high risk)
```

### LLM Malformed

```
[20:02:18] llm_malformed_output  actor=verifier
  workflow=llm-verification-adapter
  reason=JSON parse failed
  last_good_event=llm response received (untrusted)
  next_action=reject (fail-closed)
```

### Queue Exhausted

```
[20:02:18] retry_exhausted  actor=queue
  workflow=local-queue-worker
  reason=verification failed 3 times
  last_good_event=retry_triggered retry=3
  next_action=escalation_triggered
```
