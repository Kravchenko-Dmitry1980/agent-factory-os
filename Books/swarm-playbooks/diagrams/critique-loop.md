# Critique Loop Diagram

---
classification: operational-guidance
source_tier: operational-playbook
promotion_status: unreviewed
canonical_status: non-canonical
origin: swarm-playbooks
---

```mermaid
flowchart TD
    START([Task ready]) --> EXEC[Executor produces result]
    EXEC --> CRIT[Critic verdict]
    CRIT -->|pass| DONE([To review queue])
    CRIT -->|fail| CHECK{round < max?}
    CHECK -->|yes| INC[Increment round]
    INC --> EXEC
    CHECK -->|no| ESC([Escalate to human review])
    DONE --> NOTE[! NOT verification !]
    NOTE --> HR[Human review still required]

    style NOTE fill:#fee2e2
    style ESC fill:#fef3c7
    style HR fill:#fef3c7
```

Max rounds in playbook sources: **2**.

See [critique/critic-loop.md](../critique/critic-loop.md) and [critique/critique-limitations.md](../critique/critique-limitations.md).
