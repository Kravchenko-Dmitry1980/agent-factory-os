# Second Template Implementation Options — Phase 3.5

**Date:** 2026-05-26  
**Status:** PLAN_ONLY

---

## Options compared

| Option | Description | Pros | Cons | Risk |
|--------|-------------|------|------|------|
| **A — Specs only** | Create `agent-builder-kit/templates/task-triage-agent/` Markdown only | Safest; mirrors Review Assistant path; clear freeze point | Slower feedback; no runnable demo yet | **Low** |
| B — Specs + thin together | Template + `prototypes-derived/task-triage-thin/` in one phase | Faster feedback; eval script possible sooner | Skips spec sign-off discipline; dual surface | **Medium–High** |
| C — Thin implementation first | Code before template | Fast hack | Inverts governance; untraceable spec drift | **High — Reject** |

---

## Option A — Specs only (recommended)

### Deliverables (future Phase 3.5-Impl)

```
agent-builder-kit/templates/task-triage-agent/
├── README.md
├── agent-card.md
├── workflow.md
├── safety-gates.md
├── memory-boundaries.md
├── human-approval.md
├── evaluation.md
├── expected-traces.md
├── failure-modes.md
├── anti-patterns.md
├── change-proposal.md
├── acceptance-criteria.md
└── sign-off/ (after review)
```

**No Python. No prototypes-derived/. No eval script.**

### Sequence after specs

```text
Phase 3.5-Impl     → specs only
Phase 3.5-Review   → template sign-off
Phase 3.5-Freeze   → task-triage-agent-v0.1
Phase 3.6-Plan     → thin implementation plan (optional)
Phase 3.6-Impl     → thin demo (explicit approval)
```

---

## Option B — Specs + thin together

### Why not recommended now

- Review Assistant took **template → thin → mock → provider → harness** sequentially
- Skipping steps increased orchestrator drift risk for Task Triage
- Two artifacts harder to rollback independently

### When reconsider

Only if specs frozen v0.1 AND user explicitly requests combined impl with expanded preconditions.

---

## Option C — Thin first

**Rejected.**

Reason: code before contract → factory/runtime drift. Violates Agent Builder Kit doctrine.

---

## Recommendation

# Option A — Specs only first

Follow same discipline as Review Assistant Agent Template v0.1.

User prompt for next phase:

> Start Phase 3.5-Impl Task Triage Agent specs only.

Plus [PRECONDITIONS_FOR_3_5_IMPL.md](PRECONDITIONS_FOR_3_5_IMPL.md).

---

## Explicitly not recommended

| Path | Reason |
|------|--------|
| Generator for second template | Factory drift |
| Shared runtime for both agents | Orchestrator drift |
| Template + provider + thin in one prompt | Scope explosion |
