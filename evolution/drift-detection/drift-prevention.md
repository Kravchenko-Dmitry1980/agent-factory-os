# Drift Prevention

## Design Rules (from Phases 2.0–2.4)

1. One lesson per prototype/adapter
2. Duplicate over abstract
3. Fail-closed default on change
4. Failure scenarios in every demo
5. Append-only audit
6. Text traces for visibility
7. Change template before code
8. Rollback plan mandatory for risk ≥ 3

## Review Gates

Periodic read (no automation):

- [governance-gates/gate-checklists.md](../governance-gates/gate-checklists.md)
- [early-warning-signals.md](early-warning-signals.md)
- Phase review docs in `governance/`

## Freeze Zones

Consider freeze (changes docs-only):

- `prototypes/shared/` API surface
- Canonical event names
- MAX_RETRIES defaults across demos

## Culture

**Governance over speed** — [../governance/governance-over-speed.md](../governance/governance-over-speed.md)
