# Prompt Injection Safety Flow

**Phase 3.4-Plan** — how injection-shaped output must be handled (system view).

```mermaid
flowchart TD
    PO[Provider output received] --> INJ{Injection-shaped content?}
    INJ -->|No| NORMAL[Normal parse path]
    INJ -->|Yes| PARSE2[Parse may still succeed]

    NORMAL --> SAFETY1[Safety check]
    PARSE2 --> SAFETY2[Safety check]

    SAFETY1 --> V1[Verification]
    SAFETY2 --> DETECT{Unsafe / bypass / command / secret?}

    DETECT -->|Yes| BLOCK[BLOCKED unsafe_action_blocked]
    DETECT -->|Uncertain| ESC[ESCALATED human review]
    DETECT -->|Missed - bug| RISK[CRITICAL: must not deliver]

    V1 --> APP1[Approval gate]
    APP1 --> DEL1[DELIVERED only if all gates pass]

    BLOCK --> TRACE1[Trace + no delivery]
    ESC --> TRACE2[Trace + human review]
    RISK --> FAIL([Harness FAIL if delivered])

    style BLOCK fill:#fdd
    style ESC fill:#ffd
    style FAIL fill:#fee
    style DEL1 fill:#dfd
```

## Principle

Model may comply with injection. System must still **fail closed**.

## Categories

See [../PROMPT_INJECTION_TAXONOMY.md](../PROMPT_INJECTION_TAXONOMY.md).
