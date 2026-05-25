# Exercise: Trigger Escalation

## Purpose

See bounded retries and escalation — not infinite loop.

## Time

20 minutes

## Steps

1. Read [../lessons/lesson-retry-and-escalation.md](../lessons/lesson-retry-and-escalation.md)
2. Run:

```powershell
python prototypes/integrations/escalation-workflow/minimal-demo.py --scenario retry-storm
python prototypes/queue-orchestration/minimal-demo.py --scenario max-retries
```

3. Read `observability/examples/escalation-trace.txt` line by line

## Expected Result

Retries visible; escalation or exhaustion; no fake success after storm.

## What To Observe

- retry_triggered count bounded
- escalation_triggered on integration demo
- unsafe_action_blocked if auto-complete attempted

## Questions

1. What happens at retry ceiling?
2. Why not retry forever?

## Pass Criteria

Walks through escalation trace; names three events in order.

## Fail Criteria

Cannot find retry/escalation in output; thinks completed after storm.
