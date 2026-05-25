# Local-First Evolution

## Rules

1. Changes validated on developer machine
2. Rollback = git + file restore, not cloud rollback API
3. No required external services to validate governance
4. Examples and traces stay in repo markdown
5. `.data/` artifacts disposable

## Promotion Path

Knowledge evolves in:

- `evolution/` (change discipline)
- `observability/` (visibility)
- `governance/` (policy reviews)
- `agent-os/` (canonical, via promotion only)

## Not Local-First

Adding Jenkins/GitHub Actions **as product** of this phase — forbidden.

Existing repo CI (if any) untouched by Phase 2.4 scope.
