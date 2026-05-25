# Bounded Memory Diagram

```mermaid
flowchart LR
    subgraph write [Write Path]
        AG[Agent output] --> VG{Verify gate}
        VG -->|pass| STORE[(Bounded store)]
        VG -->|fail| DIS[Discard]
    end

    subgraph inject [Injection Path]
        BOOT[Session bootstrap] --> SNAP[Frozen snapshot]
        SNAP --> PROMPT[System prompt prefix]
    end

    STORE -.->|next session| SNAP
    STORE -.x mid-session .x PROMPT

    LIMIT[Char limits]
    TAX[4-type taxonomy]
    PROF[Profile isolation]

    LIMIT --> STORE
    TAX --> STORE
    PROF --> STORE

    AP1[[unbounded-memory-growth]]
    AP2[[mid-session-memory-injection]]
    AP1 -.-> DIS
    AP2 -.x PROMPT

    style SNAP fill:#dcfce7
    style AP1 fill:#fee2e2
    style AP2 fill:#fee2e2
```

See [bounded-memory.md](../bounded-memory.md).
