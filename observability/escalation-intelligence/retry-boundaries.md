# Retry Boundaries

## Rules (from prototypes + integrations)

| Layer | Typical max | After ceiling |
|-------|-------------|---------------|
| Critic rework | 2 | Human / blocked |
| Queue worker | 3 | Escalate |
| LLM call | 1 (demo) | Escalate, no retry storm |
| Telegram approval poll | 3 | Timeout deny |

## Observable Retry Sequence

```
retry_triggered retry=1
retry_triggered retry=2
retry_triggered retry=3
retry_exhausted
escalation_triggered
```

## Retry Storm Signature

- Many `retry_triggered`
- No increasing `retry=` metadata
- No `escalation_triggered`
- CPU/log volume up, outcome unchanged

## Fix Location

Workflow code ceiling — not horizontal scale.
