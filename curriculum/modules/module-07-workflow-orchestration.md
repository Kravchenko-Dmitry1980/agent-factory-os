# Module 07 — Workflow Orchestration

## Goal

Understand multi-step workflows: queue, retry, escalation — without building a platform.

## Simple Explanation

**Orchestration** here means ordered steps with durable state: enqueue task → process → verify → retry if needed → escalate if stuck. Not a cloud worker fleet.

## Key Ideas

- Task lifecycle (started → completed/failed/escalated)
- Bounded retries
- Escalation at ceiling
- Queue recovery after crash

## Files to Read

- `prototypes/queue-orchestration/README.md`
- `prototypes/integrations/escalation-workflow/README.md`
- [../lessons/lesson-retry-and-escalation.md](../lessons/lesson-retry-and-escalation.md)

## Commands to Run

```powershell
python prototypes/queue-orchestration/minimal-demo.py --scenario happy
python prototypes/queue-orchestration/minimal-demo.py --scenario max-retries
python prototypes/integrations/escalation-workflow/minimal-demo.py --scenario retry-storm
```

## Exercise

[../exercises/exercise-trigger-escalation.md](../exercises/exercise-trigger-escalation.md)

## Common Mistakes

- Infinite retries
- Removing escalation to green demos
- One orchestrator to rule all demos

## Checkpoint Questions

1. What event marks retry ceiling?
2. What happens after retry_exhausted in escalation demo?
3. Why not one shared engine for all prototypes?

## Expected Outcome

Student reads escalation trace and explains each event.
