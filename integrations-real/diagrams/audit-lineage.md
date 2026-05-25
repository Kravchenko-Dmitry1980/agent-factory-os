# Audit Lineage

```mermaid
flowchart LR
    E1[task_received] --> E2[review_pass]
    E2 --> E3[approval]
    E3 --> E4[failure]
    E4 --> E5[escalated]
    E5 --> L[lineage chain query]
    E1 -.->|parent_id links| E2
    E2 -.-> E3
    E3 -.-> E4
    E4 -.-> E5
```

Append-only JSONL — no update/delete path.
