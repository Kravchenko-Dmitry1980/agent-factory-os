# Promotion Governance Cluster Diagram

```mermaid
flowchart LR
    BO[Books/brain-os research]
    HE[hermes sandbox]
    MA[mobileagent sandbox]
    CL[Books/claude frozen]
    BO --> PR[PROMOTION_REVIEW]
    HE --> PR
    MA --> PR
    PR --> PS[PROMOTION_STRATEGY]
    PS --> PL[PROMOTION_LOG]
    PL --> AO[agent-os note]
    CL --> AO
    AO --> SL[semantic-linking-rules]
    SL --> CC[concept-clusters]
    AO --> AP[anti-pattern edge]
```

## Up

- [promotion-governance-cluster.md](../cluster-indexes/promotion-governance-cluster.md)
