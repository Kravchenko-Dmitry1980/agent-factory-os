# Harness Scope Boundary

**Phase 3.4-Plan** — allowed future harness vs forbidden expansion.

```mermaid
flowchart TB
    subgraph ALLOWED [Allowed - Option B]
        A1[One stdlib script]
        A2[Fixed synthetic cases]
        A3[Mock default]
        A4[Opt-in local provider]
        A5[Pass/fail output]
    end

    subgraph FORBIDDEN [Forbidden - rollback]
        F1[pytest / CI suite]
        F2[Benchmark platform]
        F3[Red-team corpus]
        F4[Provider framework]
        F5[Multi-file package]
        F6[Model scoring]
    end

    IMPL[Phase 3.4-Impl future] --> ALLOWED
    ALLOWED --> FREEZE[Freeze harness v0.1]
    ALLOWED -.->|scope creep| FORBIDDEN
    FORBIDDEN --> RB[Remove harness keep v0.3]

    style FORBIDDEN fill:#fee
    style ALLOWED fill:#efe
```

## Documents

- [../RECOMMENDED_HARNESS_SCOPE.md](../RECOMMENDED_HARNESS_SCOPE.md)
- [../HARNESS_ARCHITECTURE_OPTIONS.md](../HARNESS_ARCHITECTURE_OPTIONS.md)
- [../ROLLBACK_AND_FREEZE_PLAN.md](../ROLLBACK_AND_FREEZE_PLAN.md)
