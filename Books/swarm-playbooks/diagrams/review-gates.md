# Review Gates Diagram

---
classification: operational-guidance
source_tier: operational-playbook
promotion_status: unreviewed
canonical_status: non-canonical
origin: swarm-playbooks
---

```mermaid
flowchart TB
    subgraph automated [Automated Zone]
        EX[Executors]
        CR[Critic]
        EX --> CR
    end

    subgraph gates [Human Gates]
        PG[Plan Gate<br/>large runs only]
        RQ[Review Queue<br/>На проверке]
        AG[Approval Gate<br/>external actions]
    end

    PLAN[Orchestrator Plan] --> PG
    PG -->|approved| EX
    CR -->|pass| RQ
    RQ -->|approve item| AG
    RQ -->|rework + comment| EX
    AG -->|confirmed| EXT[Publish / Send / Pay]

    CR -.->|NOT a gate| EXT

    style PG fill:#fef3c7
    style RQ fill:#fef3c7
    style AG fill:#fca5a5
    style EXT fill:#dcfce7
```

## Key Rule

Critic output **never** connects directly to external effects.

See [hitl/human-approval-boundaries.md](../hitl/human-approval-boundaries.md).
