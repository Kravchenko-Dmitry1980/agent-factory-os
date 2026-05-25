# Lesson: Retry and Escalation

## What is this?

**Retry** = try again after failure, up to a **limit**. **Escalation** = stop automation and involve a human when the limit is hit.

## Why does it matter?

Infinite retries hide bugs. Silent failure after retries leaves nobody informed.

## What can go wrong?

- MAX_RETRIES increased "temporarily"
- retry_exhausted → task_completed (silent)
- Escalation step removed

## How do we check it?

Trace shows retry_triggered, retry_exhausted, escalation_triggered in order.

```powershell
python prototypes/integrations/escalation-workflow/minimal-demo.py --scenario retry-storm
```

Trace: `observability/examples/escalation-trace.txt`

## Which demo shows it?

- queue-orchestration (max-retries)
- escalation-workflow
- local-queue-worker (recovery)
