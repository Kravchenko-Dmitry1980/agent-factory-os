# Provider Evaluation Flow

**Phase 3.4-Plan** — future minimal safety evaluation (plan only).

```mermaid
flowchart TD
    START([Start evaluation run]) --> MODE{Run mode?}
    MODE -->|Default| MOCK[Mock provider outputs]
    MODE -->|Opt-in flag| LIVE[Local provider optional]

    MOCK --> CASES[Fixed synthetic cases A-G]
    LIVE --> CASES

    CASES --> CHAIN[Review Assistant v0.3 safety chain]
    CHAIN --> PARSE[Parse]
    PARSE --> SAFETY[Safety check]
    SAFETY --> VERIFY[Verification]
    VERIFY --> APPROVAL[Human approval]
    APPROVAL --> OUTCOME{DELIVERED / BLOCKED / ESCALATED / FAILED}

    OUTCOME --> TRACE[Inspect trace events]
    TRACE --> SECRET{Secrets in trace?}
    SECRET -->|Yes| FAIL([Harness FAIL])
    SECRET -->|No| EXPECT{Matches expected safe response?}
    EXPECT -->|No| FAIL
    EXPECT -->|Yes| BASELINE[Run baseline regression scripts]
    BASELINE --> REG{All PASS?}
    REG -->|No| FAIL
    REG -->|Yes| PASS([Harness PASS])

    style FAIL fill:#fee
    style PASS fill:#efe
```

## Notes

- Provider output is never truth.
- Expected outcome is per test spec, not model quality score.
- No benchmark leaderboard at any step.
