# Integrations Shared — Strictly Bounded

**This folder is NOT a framework.**

## Allowed

- `repo_path.py` — optional reference snippet (demos inline path setup instead)

## Forbidden

- Base workflow classes
- Step registries
- Plugin loaders
- Universal orchestration helpers
- Abstract agent interfaces

## Use Instead

Import from Phase 2.0 `prototypes/shared/`:

- `AuditLog`
- `fail_closed`, `require_approval`
- `GateResult`, `VisualOutcome`

If you need a helper for two workflows, **duplicate it** rather than abstract it.

See [../governance/anti-framework-rules.md](../governance/anti-framework-rules.md).
