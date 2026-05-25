# Anti-Monitoring-Platform Rules

1. **No metrics backend** — counters are not the product of this layer
2. **No dashboards as deliverable** — Mermaid in docs only
3. **No alert rules** — escalation belongs in workflow gates
4. **No sampling / cardinality docs** — out of scope
5. **No SLO templates** — educational postmortems instead
6. **No log shipping** — local files only
7. **No "observability stack" docker-compose**

## If You Need Production Monitoring

That is a **different project** with different governance. Export canonical event *names* only — not this folder as infra.

## Test

> Did we install a daemon?

If yes — Phase 2.3 boundaries violated.
