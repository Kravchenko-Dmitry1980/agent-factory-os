# Queue Orchestration

**Purpose:** Validate durable tasks, orchestration lifecycle, retry boundaries, escalation.

## Flow

```
goal → enqueue → worker → verify → (retry | escalate | complete)
```

## Run

```powershell
python prototypes/queue-orchestration/minimal-demo.py
python prototypes/queue-orchestration/minimal-demo.py --scenario max-retries
```

## Doctrine Links

- `Books/swarm-playbooks/patterns/queue-backed-execution.md`
- `agent-os/04_multi-agent/durable-task-coordination.md`
