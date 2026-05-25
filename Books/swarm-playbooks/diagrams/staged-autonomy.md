# Staged Autonomy Diagram

---
classification: operational-guidance
source_tier: operational-playbook
promotion_status: unreviewed
canonical_status: non-canonical
origin: swarm-playbooks
---

```mermaid
flowchart TB
    S0[Stage 0: Tools & skeleton] --> S1[Stage 1: Single agent MVP]
    S1 --> S2[Stage 2: Multi chat personas]
    S2 --> S3[Stage 3: Orchestrated runs + critic]
    S3 --> S4[Stage 4: Content loop + budget]
    S4 --> S5[Stage 5: Platform features]

    S1 -.- H1[Human approves all outputs]
    S3 -.- H2[Human review queue]
    S4 -.- H3[Human approves publish]
    S5 -.- H4[Strict external tool policy]

    SKIP{{Skip stages?}} -.->|anti-pattern| S5

    style SKIP fill:#fee2e2
    style S1 fill:#dcfce7
    style S3 fill:#dbeafe
```

See [patterns/progressive-autonomy.md](../patterns/progressive-autonomy.md) and [anti-patterns/premature-agent-swarm.md](../anti-patterns/premature-agent-swarm.md).
