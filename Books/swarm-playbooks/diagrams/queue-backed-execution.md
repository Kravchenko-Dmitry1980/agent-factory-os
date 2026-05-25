# Queue-Backed Execution Diagram

---
classification: operational-guidance
source_tier: operational-playbook
promotion_status: unreviewed
canonical_status: non-canonical
origin: swarm-playbooks
---

```mermaid
flowchart LR
    UI[Dashboard / API] -->|create run| ORCH[Orchestrator]
    ORCH -->|enqueue tasks| Q[(Task Queue DB)]
    Q --> W[Worker]
    W -->|one at a time| AG[Executor Agent]
    AG -->|result| Q
    W -->|crash/restart| REC[Recovery: resume incomplete]
    REC --> Q
    Q -->|all done| REV[Review state]

    UI -. non-blocking .-> Q

    style Q fill:#dbeafe
    style REC fill:#fef3c7
```

## Properties (from sources)

- Tasks processed without blocking UI
- Incomplete tasks picked up after backend restart
- Sequential processing default (playbook)

See [patterns/queue-backed-execution.md](../patterns/queue-backed-execution.md).
