# Unsafe Memory Patterns

| Pattern | Event should fire |
|---------|-------------------|
| Unverified writeback | `memory_write_rejected reason=unverified` |
| Mid-session snapshot mutation | anti-pattern — should not occur |
| Unbounded growth | `memory_write_rejected reason=overflow` |
| Raw chat dump to durable | `governance_rejection` |
| Recursive self-improvement write | `memory_write_rejected` |

## Context Overload

Not always a separate event — infer from:

- `context_load` size metadata
- Truncation in trace notes
- Repeated task_failed after long session

## Observability Rule

Every durable mutation → one audit event minimum.
