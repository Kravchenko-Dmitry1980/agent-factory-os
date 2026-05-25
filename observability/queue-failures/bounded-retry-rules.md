# Bounded Retry Rules

| System | Max retries | Terminal event |
|--------|-------------|----------------|
| Review rework | 2 | escalate / human |
| Queue worker | 3 | `escalation_triggered` |
| GUI outcome C | 2 strikes | circuit breaker |
| LLM adapter | 0 retries | escalate on fail |
| Telegram poll | 3 | `approval_timeout` |

## Observability Requirement

Every retry increment → `retry_triggered` with `retry=N`.

Every ceiling hit → `retry_exhausted` before `escalation_triggered`.

## Anti-Pattern

Generic `error` log in loop without retry metadata.
