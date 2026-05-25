# Provenance Lineage Diagram

```mermaid
flowchart TB
    T0[T0 Frozen Books/claude agents]
    T1[T1 Research brain-os experiments swarm]
    T3[T3 Catalog 10_research]

    T0 --> EXT[Extract]
    T1 --> EXT
    EXT --> SCORE[Score PROMOTION_REVIEW]
    SCORE --> GOV[Governance review]
    GOV --> T2[T2 Curated 00-09]
    T2 --> DOC[Phase 1.4 doctrine synthesis]

    T1 -.x direct copy .x T2
    T3 --> LINK[Links only]

    PL[PROMOTION_LOG audit trail]
    GOV --> PL

    style T2 fill:#dcfce7
    style DOC fill:#dbeafe
    style T1 fill:#fef3c7
```

See [provenance-first.md](../provenance-first.md).
