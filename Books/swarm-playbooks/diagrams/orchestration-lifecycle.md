# Orchestration Lifecycle Diagram

---
classification: operational-guidance
source_tier: operational-playbook
promotion_status: unreviewed
canonical_status: non-canonical
origin: swarm-playbooks
---

```mermaid
flowchart LR
    G[Goal] --> P[Planning]
    P --> D[Decomposition]
    D --> E[Execution]
    E --> C[Critique]
    C --> R[Review]
    R --> A[Approval]
    A --> Pub[Publish]

    P -. large run .-> H1{{Human: Approve Plan}}
    H1 -. approved .-> D

    E -. waiting_question .-> H2{{Human: Answer}}
    H2 -. resume .-> E

    C -. fail & round < max .-> E
    C -. fail & round exhausted .-> R

    R --> H3{{Human: Approve / Rework}}
    H3 -. rework .-> E
    H3 -. approve .-> A

    style H1 fill:#fef3c7
    style H2 fill:#fef3c7
    style H3 fill:#fef3c7
    style Pub fill:#dcfce7
```

## Legend

- Yellow: human intervention points
- Green: external effect phase
- Dotted: conditional paths

See [lifecycle/orchestration-lifecycle.md](../lifecycle/orchestration-lifecycle.md).
