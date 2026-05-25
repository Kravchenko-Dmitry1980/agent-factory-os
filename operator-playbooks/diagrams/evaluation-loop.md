# Evaluation Loop (Operator View)

```mermaid
flowchart LR
    A[Run demo] --> B[Read audit / trace]
    B --> C[Compare expected outcomes]
    C --> D[Smoke scripts optional]
    D --> E{Safe behavior?}
    E -->|yes| F[Accept or continue learning]
    E -->|no| G[Troubleshoot or rollback]
```

Operator uses existing Phase 2.5 scripts — does not build new automation.

Detail: `evaluation/diagrams/evaluation-loop.md`

Runbook: [../runbooks/run-evaluation-checks.md](../runbooks/run-evaluation-checks.md)
