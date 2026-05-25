# Review Loop — Architecture

## Components

| Role | Responsibility | Forbidden |
|------|----------------|-----------|
| **Executor** | Produces draft from task | Publish, external actions |
| **Critic** | Scores draft quality | Publish, override human |
| **Human reviewer** | Approve/reject for release | Skip on "critic pass" alone |
| **Publisher** | Writes output after approval | Run without approval token |

## State Machine

```
RECEIVED → DRAFTED → CRITIQUED → IN_REVIEW → APPROVED → PUBLISHED
                              ↘ REWORK (bounded)
                              ↘ BLOCKED (fail-closed)
IN_REVIEW → REJECTED
```

## Boundaries

- Critic output is **advisory** (`CritiqueVerdict`), stored for audit
- Human gate is **mandatory** — `approved_by_human: bool` required
- Uncertain critic verdict → **BLOCKED**, not auto-rework forever
- Max rework rounds: 2 (then escalate to human with blocked flag)

## Non-Goals

- No LLM integration
- No multi-agent framework
- No automatic publish on high critic score
