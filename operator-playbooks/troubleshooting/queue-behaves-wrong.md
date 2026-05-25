# Queue Behaves Wrong

## Symptom

Retries never stop, task completes after failures, no recovery, duplicate tasks.

## Prototype queue

```powershell
python prototypes/queue-orchestration/minimal-demo.py --scenario max-retries
```

Expect: retries bounded, final status not falsely "completed".

## Integration escalation

```powershell
python prototypes/integrations/escalation-workflow/minimal-demo.py --scenario retry-storm
```

Expect: escalation in audit; no silent complete.

## Real adapter

```powershell
python integrations-real/local-queue-worker/minimal-demo.py --scenario recovery
```

Expect: recovery message, task completes after reload.

## Compare trace

`observability/examples/escalation-trace.txt`  
`observability/examples/queue-recovery-trace.txt`

## If wrong after your change

Check retry constants — common regression. Rollback.

Guide: [../scenario-guides/scenario-local-queue.md](../scenario-guides/scenario-local-queue.md)

`evolution/examples/unsafe-retry-increase.md`
