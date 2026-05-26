# prototypes-derived

**Derived local demos** — not runtime, not factory.

---

## What this is

`prototypes-derived/` holds **thin implementations** inspired by Phase 2 prototypes and frozen Agent Builder Kit templates. Each folder is a **standalone demo** that proves a frozen spec can run locally with gates and traces.

---

## Why it exists

Phase 3.1 plan chose **Option B** ([FILE_BOUNDARY_PLAN.md](../governance/phase-3-1-plan/FILE_BOUNDARY_PLAN.md)): keep `agent-builder-kit/` **spec-only** and place code under `prototypes-derived/` to avoid kit → runtime confusion.

---

## Why it is not runtime

- No shared engine across demos
- No registry, factory, or plugin system
- No imports from a `prototypes-derived/shared/` package
- Each implementation is one folder, one entry script

---

## Current implementations

| Folder | Template | Status |
|--------|----------|--------|
| [review-assistant-thin/](review-assistant-thin/README.md) | Review Assistant Agent v0.1 (frozen) | Phase 3.1 thin demo |

---

## Rules

- Do **not** edit `prototypes/` — reference only
- Do **not** modify frozen template spec body without change proposal
- Stdlib-only unless explicitly approved
- See each impl `governance.md`
