# Bounded Failure Patterns

Failures contained by design — from Phases 2.0–2.2.

| Pattern | Bound |
|---------|-------|
| Retry ceiling | MAX_RETRIES |
| Memory cap | MAX_MEMORY_CHARS |
| Rework cap | MAX_REWORK = 2 |
| GUI circuit breaker | 2× C outcome |
| LLM single attempt | No retry storm |
| Approval timeout | Deny, don't wait forever |

## Property

Worst case is **visible escalation**, not unbounded harm.

## Evolution Rule

Never remove bound without adding stronger gate elsewhere.

## Test

Every bound has a `--scenario` that hits it.
