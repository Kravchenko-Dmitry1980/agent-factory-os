# Template Versioning Policy

## Version Format

`v<major>.<minor>` in folder name or frontmatter.

- **major** — breaking safety/gate/workflow change
- **minor** — clarifications, additional scenarios, non-breaking docs

## Examples

- `review-assistant-agent` v0.1 — Phase 3.0 initial spec
- v0.2 — added scenario, unchanged gates

## Rules

- Accepted templates must declare version
- Frozen templates immutable except via proposal
- Git history is source of truth for diffs
- Rollback = checkout previous version + rerun eval checklists

## Not Allowed

- Silent overwrite of frozen template
- Version skip without review

See [template-freeze-policy.md](template-freeze-policy.md)
