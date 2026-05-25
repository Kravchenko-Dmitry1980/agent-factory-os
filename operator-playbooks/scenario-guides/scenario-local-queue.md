# Scenario: Local Queue

## What It Teaches

Durable tasks, bounded retries, escalation at ceiling, recovery after crash.

## What Can Go Wrong

- Infinite retries
- Silent complete after failures
- Lost tasks on restart

## Correct Safe Behavior

- Retries capped
- Escalation after exhaustion
- `queue_recovered` on restart scenario

## Files to Run

```powershell
python prototypes/queue-orchestration/minimal-demo.py --scenario max-retries
python prototypes/integrations/escalation-workflow/minimal-demo.py --scenario retry-storm
python integrations-real/local-queue-worker/minimal-demo.py --scenario recovery
```

## Traces to Inspect

- `observability/examples/escalation-trace.txt`
- `observability/examples/queue-recovery-trace.txt`

## Evaluation Checks

- `evaluation/scenarios/queue-orchestration-scenarios.md`
- Smoke: `queue max-retries`, `escalation retry-storm`, `local-queue recovery`

## Troubleshooting

- [../troubleshooting/queue-behaves-wrong.md](../troubleshooting/queue-behaves-wrong.md)
