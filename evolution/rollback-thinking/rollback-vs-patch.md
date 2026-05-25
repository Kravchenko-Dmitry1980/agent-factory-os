# Rollback vs Patch

| | Rollback | Patch |
|---|----------|-------|
| **Goal** | Restore known governance | Fix forward |
| **Risk** | Low if history clean | Adds complexity |
| **When** | Gate order wrong, autonomy leak | Typo, clear isolated bug |
| **Time** | Minutes | Unknown |
| **Audit** | Revert + note | New change proposal |

## Default Under Uncertainty

**Rollback first** if:

- External actions involved
- Retry/escalation behavior changed
- Shared module touched
- Trace shows missing gate events

## Patch OK If

- Docs only
- Mock scenario addition
- Observability clarity (no behavior change)

## Anti-Pattern

Layer patches on top of drift — [architecture-regression/slow-decay-patterns.md](../architecture-regression/slow-decay-patterns.md)
