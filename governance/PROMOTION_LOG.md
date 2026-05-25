# Promotion Log

**Phase:** 1.2 — Governed Curated Promotion  
**Date:** 2026-05-25  
**Policy:** `governance/PROMOTION_STRATEGY.md`

---

| Date | File | Source | Decision | Governance Reference |
| ---- | ---- | ------ | -------- | -------------------- |
| 2026-05-25 | `agent-os/02_memory/frozen-memory-snapshot.md` | `experiments/hermes-agent-review/memory/MEMORY_SYSTEM_OVERVIEW.md` | PROMOTE_NOW | PROMOTION_REVIEW.md §3.1 |
| 2026-05-25 | `agent-os/02_memory/memory-char-limits.md` | `experiments/hermes-agent-review/memory/MEMORY.md` | PROMOTE_NOW | PROMOTION_REVIEW.md §3.1 |
| 2026-05-25 | `agent-os/02_memory/profile-isolation.md` | `experiments/hermes-agent-review/notes/DIGITAL_TWIN_IMPLICATIONS.md` | PROMOTE_NOW | PROMOTION_REVIEW.md §3.6 |
| 2026-05-25 | `agent-os/02_memory/memory-provider-boundaries.md` | `experiments/hermes-agent-review/memory/MEMORY_PROVIDERS.md` | PROMOTE_NOW | PROMOTION_REVIEW.md §3.1 |
| 2026-05-25 | `agent-os/04_multi-agent/kanban-vs-delegate.md` | `experiments/hermes-agent-review/multi-agent/TASK_ORCHESTRATION.md` | PROMOTE_NOW | PROMOTION_REVIEW.md §3.8 |
| 2026-05-25 | `agent-os/04_multi-agent/subagent-tool-restrictions.md` | `experiments/hermes-agent-review/multi-agent/SUBAGENTS.md` | PROMOTE_NOW | PROMOTION_REVIEW.md §3.8 |
| 2026-05-25 | `agent-os/04_multi-agent/durable-task-coordination.md` | `experiments/hermes-agent-review/multi-agent/KANBAN.md` | PROMOTE_NOW | governance/NEXT_PHASE_ROADMAP.md Batch B |
| 2026-05-25 | `agent-os/01_agent-runtime/gui-agent-loop.md` | `experiments/mobile-agent-review/extracted-patterns/screen-reason-action-feedback-loop.md` | PROMOTE_NOW | PROMOTION_REVIEW.md §4.1 |
| 2026-05-25 | `agent-os/01_agent-runtime/visual-grounding.md` | `experiments/mobile-agent-review/extracted-patterns/visual-grounding-pattern.md` | PROMOTE_NOW | PROMOTION_REVIEW.md §4.2 |
| 2026-05-25 | `agent-os/00_foundations/visual-verification.md` | `experiments/mobile-agent-review/extracted-patterns/action-verification-pattern.md` | PROMOTE_NOW | PROMOTION_REVIEW.md §4.4 |
| 2026-05-25 | `agent-os/09_antipatterns/unverified-gui-clicks.md` | `experiments/mobile-agent-review/anti-patterns/unverified-clicks.md` | PROMOTE_NOW | PROMOTION_REVIEW.md §4.8 |
| 2026-05-25 | `agent-os/09_antipatterns/brittle-gui-automation.md` | `experiments/mobile-agent-review/anti-patterns/brittle-gui-automation.md` | PROMOTE_NOW | PROMOTION_REVIEW.md §4.8 |
| 2026-05-25 | `agent-os/09_antipatterns/mid-session-memory-injection.md` | `experiments/hermes-agent-review/anti-patterns/ANTI_PATTERNS.md` §2 | PROMOTE_NOW | PROMOTION_REVIEW.md §3.2 |
| 2026-05-25 | `agent-os/09_antipatterns/unbounded-memory-growth.md` | `experiments/hermes-agent-review/anti-patterns/ANTI_PATTERNS.md` §1 | PROMOTE_NOW | PROMOTION_REVIEW.md §3.2 |
| 2026-05-25 | `agent-os/09_antipatterns/recursive-self-improvement.md` | `experiments/hermes-agent-review/anti-patterns/ANTI_PATTERNS.md` §9, §11 | PROMOTE_NOW | governance/CANONICAL_DIRECTION.md |
| 2026-05-25 | `agent-os/08_patterns/progressive-skill-disclosure.md` | `experiments/hermes-agent-review/skills/SKILLS_SYSTEM_OVERVIEW.md` | PROMOTE_NOW | PROMOTION_REVIEW.md §3.4 |
| 2026-05-25 | `agent-os/08_patterns/memory-aware-execution.md` | Hermes memory + `Books/brain-os/patterns/memory-aware-routing.md` | PROMOTE_NOW | governance/PROMOTION_STRATEGY.md |
| 2026-05-25 | `agent-os/08_patterns/verification-before-writeback.md` | `Books/brain-os/patterns/evaluation-before-writeback.md` | PROMOTE_NOW | governance/PROMOTION_STRATEGY.md |
| 2026-05-25 | `agent-os/08_patterns/fail-closed-agent-loop.md` | Claude ch05/ch06 + MobileAgent verification | PROMOTE_NOW | governance/PROMOTION_STRATEGY.md |
| 2026-05-25 | `agent-os/12_diagrams/gui-agent-loop.md` | `experiments/mobile-agent-review/diagrams/gui-agent-loop.md` | PROMOTE_NOW | Phase 1.2 diagrams |
| 2026-05-25 | `agent-os/12_diagrams/memory-governance.md` | Hermes memory overview | PROMOTE_NOW | Phase 1.2 diagrams |
| 2026-05-25 | `agent-os/12_diagrams/promotion-pipeline.md` | `governance/PROMOTION_STRATEGY.md` | PROMOTE_NOW | governance/PROMOTION_STRATEGY.md |

---

## Cross-refs updated (not new promotions)

| Date | File | Change |
| ---- | ---- | ------ |
| 2026-05-25 | `agent-os/10_research/sources.md` | Added research-tier sandboxes + brain-os |
| 2026-05-25 | Section `index.md` files | Navigation for 22 promoted notes |
| 2026-05-25 | `verification.md`, `prompt-cache-as-constraint.md`, `cache-busting-sections.md`, `subagents.md`, `memory-taxonomy.md`, `persistent-identity.md` | Bidirectional wikilinks |

---

## Explicitly NOT promoted (Phase 1.2 boundary)

- `13_gui-agents/` section
- `one-external-provider-rule.md` as separate file (merged into `memory-provider-boundaries.md`)
- `profile-isolation.md` in `06_digital-twins/` (placed in `02_memory/` per Phase 1.2 spec)
- PROMOTE_LATER items: curator-pattern, kanban-orchestration detail, gui-as-environment, coordinate-spaces
- RESEARCH_ONLY: Honcho, GUI-MCP hybrid, adaptation-service, GUI-Critic pre-op

---

## Up

- [PROMOTION_STRATEGY.md](PROMOTION_STRATEGY.md)
- [PROMOTION_REVIEW.md](../PROMOTION_REVIEW.md)
- [SEMANTIC_LINKING_AUDIT.md](SEMANTIC_LINKING_AUDIT.md)
- [SEMANTIC_DRIFT_ANALYSIS.md](SEMANTIC_DRIFT_ANALYSIS.md)

---

## Phase 1.3 — Graph Hardening (2026-05-25)

| Action | Artifact |
|--------|----------|
| Semantic linking audit | `governance/SEMANTIC_LINKING_AUDIT.md` |
| Drift analysis | `governance/SEMANTIC_DRIFT_ANALYSIS.md` |
| Graph layer | `agent-os/graph/` |
| Promoted note footers | 22 Phase 1.2 notes + verification hub notes |
| Glossary pointers | 8 new glossary entries |
