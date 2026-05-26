# No Benchmark Boundary

**Phase 3.4-Plan** — what safety evaluation is vs what benchmark platform is.

```mermaid
flowchart LR
    subgraph IN_SCOPE [In scope - Phase 3.4]
        S1[Pass/fail per synthetic case]
        S2[Trace event verification]
        S3[Fail-closed gate checks]
        S4[Regression vs v0.3 baseline]
    end

    subgraph OUT_SCOPE [Out of scope - forbidden]
        O1[Model leaderboard]
        O2[Accuracy scores]
        O3[Latency/cost benchmarks]
        O4[Multi-provider ranking]
        O5[Automated winner selection]
    end

    HARNESS[Future minimal harness] --> IN_SCOPE
    HARNESS -.->|must not become| OUT_SCOPE

    OUT_SCOPE --> ROLLBACK[Rollback trigger]
```

## Policy

[../NO_BENCHMARK_POLICY.md](../NO_BENCHMARK_POLICY.md)

## Question we answer

**Can the system stay safe?** — not **Which model is smartest?**
