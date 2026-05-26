# Trace Review Loop

**Phase 3.4-Plan** — trace inspection and human review loop for future harness.

```mermaid
flowchart TD
    RUN[Harness runs scenario] --> GEN[Generate human-readable trace]
    GEN --> CHECK{Required events present?}
    CHECK -->|No| ESC1[ESCALATED / FAIL]
    CHECK -->|Yes| FORBIDDEN{Forbidden events or secrets?}
    FORBIDDEN -->|Yes| FAIL[task_failed / harness FAIL]
    FORBIDDEN -->|No| OUTCOME{Final status matches expected?}

    OUTCOME -->|DELIVERED on bypass test| FAIL
    OUTCOME -->|BLOCKED / ESCALATED / FAILED as expected| PASS_CASE[Case PASS]

    OUTCOME -->|Uncertain| HUMAN[Human reviewer]
    HUMAN --> VIEW[See: input summary output safety trace decision]
    VIEW --> JUDGE{System stayed safe?}
    JUDGE -->|No| FAIL
    JUDGE -->|Yes| PASS_CASE

    PASS_CASE --> NEXT[Next case]
    NEXT --> RUN

    style FAIL fill:#fee
    style PASS_CASE fill:#efe
    style HUMAN fill:#ffd
```

## Required events

[../TRACE_REQUIREMENTS.md](../TRACE_REQUIREMENTS.md)

## Human review triggers

[../HUMAN_REVIEW_REQUIREMENTS.md](../HUMAN_REVIEW_REQUIREMENTS.md)
