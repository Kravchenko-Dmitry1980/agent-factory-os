# Integrations-Real Shared — Strictly Bounded

**NOT a platform SDK.**

## Allowed

- `local_paths.py` — resolves `integrations-real/.data/` directory

## Forbidden

- Universal adapter base classes
- Plugin registry
- Shared HTTP client framework
- Cross-adapter orchestration engine

Each adapter owns its I/O code. Duplicate small helpers rather than abstract.
