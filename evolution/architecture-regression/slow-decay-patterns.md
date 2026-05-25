# Slow Decay Patterns

| Pattern | Timeline | Symptom |
|---------|----------|---------|
| **Temporary retry bump** | Week 1 → permanent | Storms in prod-like tests |
| **Shared helper extraction** | Month 1 | Framework drift |
| **Doc rot** | Ongoing | failure-modes stale |
| **Happy-path only CI** | Sprint | Gates silently break |
| **Real default-on** | Release | Mock path bitrots |
| **Event rename** | Cleanup | Postmortem confusion |

## Detection

Compare current demo to Phase 2.0 review docs — line count, shared/, scenario count.

## Reverse

Rollback + freeze zone — not another refactor.
