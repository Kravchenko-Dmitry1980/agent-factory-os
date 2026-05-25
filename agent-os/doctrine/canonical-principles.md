# Canonical Principles

Consolidated principles for Agent-OS. Each principle is **already supported** by curated notes (`00–09/`), governance audits, or governed promotion evidence. This document synthesizes; it does not introduce new taxonomy or concepts.

Cross-walk: [doctrine-map.md](doctrine-map.md) | [architecture-worldview.md](architecture-worldview.md)

---

# Principle 1 — Verification-first

## Definition

No agent loop, orchestration stage, or durable write is treated as complete until **verification passes** at the appropriate modality — hooks, tests, visual delta, evaluation gate, or human review for high-risk domains.

## Why It Exists

Models self-report completion; transport success ≠ task success. Verification is the harness responsibility, not the model's claim.

## What It Prevents

- Silent wrong completion ([[fail-closed-agent-loop]])
- Unverified GUI clicks ([[unverified-gui-clicks]])
- Polluted durable memory ([[verification-before-writeback]])
- Critic-as-truth substitution (operational corpus warning; see [verification-first.md](verification-first.md))

## Supporting Patterns

- [[verification-before-writeback]]
- [[fail-closed-agent-loop]]
- [[visual-verification]]
- [[execution-verification]]

## Related Anti-patterns

- [[unverified-gui-clicks]]
- [[infinite-retry-loops]] (when retry replaces verify)
- critic-as-fake-verification (operational reference: `Books/swarm-playbooks/`)

## Operational Implications

- Every modality needs an explicit verify step before terminal state.
- Critique may precede review but **does not replace** verification.
- GUI: observe–act–verify loop ([[gui-agent-loop]]).

## Governance Implications

- Verification cluster is P0 consolidation target ([governance/CONSOLIDATION_CANDIDATES.md](../../governance/CONSOLIDATION_CANDIDATES.md)).
- Brain OS trace-first / evaluation-before-writeback remain **research** until contract spec exists.

## Sources

- `agent-os/00_foundations/verification.md`
- `agent-os/08_patterns/verification-before-writeback.md`
- `agent-os/graph/cluster-indexes/verification-cluster.md`
- `governance/CONSOLIDATION_CANDIDATES.md`

---

# Principle 2 — Governance-before-autonomy

## Definition

Autonomy expands **only** under explicit governance: permission modes, promotion gates, approval boundaries, tool restrictions, and human escalation — never by default prompt trust.

## Why It Exists

Ungoverned autonomy scales harm, cost, and irreversible side effects faster than value.

## What It Prevents

- [[recursive-self-improvement]] without depth limits
- Unbounded external actions
- Prompt-only policy ([[permission-modes]] exist precisely to avoid this)
- Self-modifying skills/memory without rollback

## Supporting Patterns

- [[subagent-tool-restrictions]]
- [[fail-closed-defaults]]
- [[progressive-skill-disclosure]] (tiered capability exposure)
- human-escalation-gate (research; Brain OS — not curated)

## Related Anti-patterns

- [[recursive-self-improvement]]
- unbounded-agent-autonomy (operational reference)
- prompt-only governance (operational reference)

## Operational Implications

- External publish/send/pay class actions require explicit approval gate.
- Progressive autonomy: MVP → orchestration only when proven ([[kanban-vs-delegate]] decision informed).

## Governance Implications

- No auto-promotion; no stage skipping ([governance/PROMOTION_STRATEGY.md](../../governance/PROMOTION_STRATEGY.md)).
- Phase 1.4 freeze: no new promotions while doctrine stabilizes.

## Sources

- `agent-os/09_antipatterns/recursive-self-improvement.md`
- `agent-os/03_harness-engineering/permission-modes.md`
- `governance/PROMOTION_STRATEGY.md`
- `Books/swarm-playbooks/hitl/safe-autonomy.md` (operational reference only)

---

# Principle 3 — Fail-closed execution

## Definition

On ambiguity, parse failure, permission denial, or verification failure, the system **defaults to safe non-completion** — serial/safe tool paths, blocked termination, no unchecked writeback — until explicitly resolved.

## Why It Exists

Fail-open behavior optimizes for apparent progress; production agents need the opposite default.

## What It Prevents

- Corrupted state from parallel unsafe tools ([[fail-closed-defaults]])
- Premature loop exit ([[fail-closed-agent-loop]])
- Wrong GUI state accepted as success
- Silent memory writes after failed verify

## Supporting Patterns

- [[fail-closed-defaults]] — tool metadata and batching defaults
- [[fail-closed-agent-loop]] — loop termination and side effects
- [[withholding-errors]] — recoverable errors held until resolved
- [[verification-before-writeback]]

## Related Anti-patterns

- [[unverified-gui-clicks]]
- [[infinite-retry-loops]] (fail-closed without retry budget)
- [[scattered-permission-sync]]

## Operational Implications

- **Disambiguate the pair:** defaults = tool layer; agent loop = lifecycle layer (see [fail-closed-execution.md](fail-closed-execution.md)).
- User-visible stall preferred over silent wrong completion.

## Governance Implications

- Doctrine must not merge the two fail-closed notes into one concept file.
- Semantic linking audit flagged merge confusion as drift risk.

## Sources

- `agent-os/08_patterns/fail-closed-defaults.md`
- `agent-os/08_patterns/fail-closed-agent-loop.md`
- `governance/SEMANTIC_LINKING_AUDIT.md`

---

# Principle 4 — Bounded memory

## Definition

Memory is **typed, capped, scoped, and injection-safe** — frozen at session bootstrap, written only through governed paths, never unbounded or mid-session prompt mutation.

## Why It Exists

Infinite context and uncontrolled writeback are fantasies that produce cost blowups, stale parallel state, and cache invalidation.

## What It Prevents

- [[unbounded-memory-growth]]
- [[mid-session-memory-injection]]
- [[memory-as-crutch]] (live codebase duplicated in memory)
- [[cache-busting-sections]]

## Supporting Patterns

- [[frozen-memory-snapshot]]
- [[memory-char-limits]]
- [[profile-isolation]]
- [[memory-provider-boundaries]]
- [[memory-aware-execution]]
- [[prompt-cache-as-constraint]]

## Related Anti-patterns

- [[unbounded-memory-growth]]
- [[mid-session-memory-injection]]
- [[memory-as-crutch]]
- CLAUDE.md-as-memory-plane (operational warning)

## Operational Implications

- Four memory types only: user, feedback, project, reference ([[memory-taxonomy]]).
- Writes persist; injection refreshes next session unless explicit recall tools surface live state.

## Governance Implications

- Memory governance cluster is fully curated (Phase 1.2).
- No promotion of auto-memory inflation patterns from research corpora.

## Sources

- `agent-os/02_memory/` curated set
- `agent-os/graph/cluster-indexes/memory-governance-cluster.md`
- `governance/CONSOLIDATION_CANDIDATES.md`

---

# Principle 5 — Provenance-first

## Definition

Every curated claim traces to **source tier, promotion decision, and corpus boundary** — frozen upstream, canonical curated, or research-only — with no silent merges.

## Why It Exists

Multi-corpus repositories decay without lineage: hype repos, duplicate definitions, and research marked canonical.

## What It Prevents

- Research wikilinked as canonical truth
- Duplicate canonical definitions across files
- Unscored experiment → agent-os copy
- Brain OS plane branding entering curated without strip

## Supporting Patterns

- Promotion pipeline (governance)
- [[memory-aware-execution]] (routing by need, not by hype)
- Graph [provenance-graph](../graph/provenance-graph.md)

## Related Anti-patterns

- Tutorial-driven architecture (stack mistaken for design)
- Taxonomy inflation via ungoverned copy-paste

## Operational Implications

- Cite `Books/claude/` for harness spine conflicts.
- Swarm-playbooks = operational reference; metadata `canonical_status: non-canonical`.

## Governance Implications

- `PROMOTION_LOG.md` is audit trail for curated integration.
- `canonical-vs-research-map.md` defines traversal rules.

## Sources

- `agent-os/graph/provenance-graph.md`
- `agent-os/graph/canonical-vs-research-map.md`
- `governance/PROMOTION_STRATEGY.md`
- `governance/PROMOTION_LOG.md`

---

# Principle 6 — Human escalation boundaries

## Definition

High-risk, ambiguous, or external-effect outcomes require **human decision authority** at defined escalation points — not optional reviewer presence.

## Why It Exists

Automation accelerates drafts; accountability for release and harm remains human in production systems.

## What It Prevents

- External action without approval
- Rubber-stamp critic pass → publish
- Ungoverned `waiting_question` stalls without operator path

## Supporting Patterns

- [[permission-modes]]
- [[verification-before-writeback]] (human gate for high-risk stores)
- [[durable-task-coordination]] (human unblock for queued work)
- human-escalation-gate (research — contract pending)

## Related Anti-patterns

- [[automation-without-review]] (operational)
- [[recursive-self-improvement]]

## Operational Implications

- Review queue distinct from critic loop (swarm operational alignment).
- GUI and code paths share escalation **discipline**, different UX.

## Governance Implications

- HITL doctrine references operational corpus; **no auto-promote** in Phase 1.4.
- Brain OS human-escalation deferred until IPC contract exists.

## Sources

- `agent-os/03_harness-engineering/permission-modes.md`
- `Books/swarm-playbooks/hitl/` (reference)
- `governance/CONSOLIDATION_CANDIDATES.md`

---

# Principle 7 — Promotion discipline

## Definition

Ideas enter the curated layer **only** through scored, logged, governed promotion — no auto-promote, no stage skip, no direct experiment copy.

## Why It Exists

Curated layer is the contract surface for architecture cognition; ungoverned intake causes semantic drift and duplicate truth.

## What It Prevents

- Research leakage into canonical wikilinks
- Batch 2 (PROMOTE_LATER) executed without review
- Swarm patterns copied verbatim into agent-os
- Diagram-before-concept inflation

## Supporting Patterns

- Concept note template + index updates
- Anti-pattern adjacency (every AP links fix pattern)
- Promotion-governance semantic cluster

## Related Anti-patterns

- Duplicate headings across curated files
- Glossary bodies duplicating concept definitions

## Operational Implications

- Phase 1.4 creates doctrine, **not** new promoted notes.
- PROMOTE_LATER backlog (~24) remains queued.

## Governance Implications

- Decision matrix: PROMOTE_NOW / LATER / RESEARCH / REJECT ([PROMOTION_REVIEW.md](../../PROMOTION_REVIEW.md)).
- Post-promotion validation checklist in PROMOTION_STRATEGY.

## Sources

- `governance/PROMOTION_STRATEGY.md`
- `governance/PROMOTION_LOG.md`
- `PROMOTION_REVIEW.md`
- `agent-os/graph/cluster-indexes/promotion-governance-cluster.md`

---

# Principle 8 — Anti-pattern adjacency

## Definition

Every documented failure mode in `09_antipatterns/` **pairs** with mitigation patterns, related concepts, or doctrine guidance — warnings are not orphan scare quotes.

## Why It Exists

Anti-patterns without fixes become folklore; fixes without failures become untested dogma.

## What It Prevents

- Orphan warnings in graph traversal
- Pattern promotion without failure mode
- Repeated failure modes under different names

## Supporting Patterns

- All `09_antipatterns/` notes include Related Patterns / Concepts (template discipline)
- [anti-pattern-families.md](anti-pattern-families.md) groups by root cause

## Related Anti-patterns

- N/A (meta-principle)

## Operational Implications

- When citing a failure in doctrine, cite family + mitigation path.
- Swarm operational anti-patterns stay in `Books/swarm-playbooks/` unless separately scored.

## Governance Implications

- `semantic-linking-rules.md`: maps link only, no definitions.
- Family review in [governance/ANTIPATTERN_FAMILY_REVIEW.md](../../governance/ANTIPATTERN_FAMILY_REVIEW.md).

## Sources

- `agent-os/graph/semantic-linking-rules.md`
- `agent-os/09_antipatterns/index.md`
- `governance/SEMANTIC_DRIFT_ANALYSIS.md`

---

# Principle 9 — Modality-unified execution

## Definition

Code and GUI agent execution share the **same harness invariants** — verification, fail-closed loops, permissions, memory bounds — implemented as **parallel golden paths**, not separate taxonomies.

## Why It Exists

GUI modality is an extension of agent runtime ([[gui-agent-loop]] ∥ [[query-loop]]), not a third architecture spine.

## What It Prevents

- GUI runtime creep into separate `13_gui-agents/` without threshold
- Code-only verification culture ignoring visual delta
- Duplicate contradictory definitions per modality

## Supporting Patterns

- [[query-loop]] — code golden path
- [[gui-agent-loop]] — embodied golden path
- [[visual-verification]] shared with code [[verification]]
- [[visual-grounding]]

## Related Anti-patterns

- [[brittle-gui-automation]]
- [[unverified-gui-clicks]]

## Operational Implications

- Observe–act–verify for GUI; prepare–model–tools–verify for code.
- Same writeback and memory rules both paths.

## Governance Implications

- TAXONOMY_REVIEW: `13_gui-agents/` = LATER, not Phase 1.4.
- GUI cluster lives under `01_agent-runtime/` + verification cluster.

## Sources

- `agent-os/01_agent-runtime/gui-agent-loop.md`
- `agent-os/graph/cluster-indexes/gui-modality-cluster.md`
- `governance/TAXONOMY_REVIEW.md`
- `governance/CONSOLIDATION_CANDIDATES.md` (dual golden path)

---

# Principle 10 — Research isolation

## Definition

Research corpora (`experiments/`, `Books/brain-os/`, `Books/swarm-playbooks/`, unscored extracts) remain **outside curated truth** — referenced by path and tier, not wikilinked as canonical definitions.

## Why It Exists

Wide research perimeter + narrow canonical core preserves experimentation without contaminating contract surface.

## What It Prevents

- Brain OS plane branding in curated notes
- 8-agent swarm as default blueprint
- Hermes/MobileAgent runtime copied as architecture
- Hype repo patterns marked production-ready

## Supporting Patterns

- `10_research/` as catalog and extraction plans
- [canonical-vs-research-map](../graph/canonical-vs-research-map.md)
- Source priority on conflict (Claude harness wins)

## Related Anti-patterns

- [[central-orchestrator-god-object]] (often imported from immature research stacks)
- tutorial-driven-architecture

## Operational Implications

- Doctrine may **reference** swarm lifecycle as operational alignment.
- Never copy swarm NEVER PROMOTE list items into principles as defaults.

## Governance Implications

- Corpus tier T0–T3 ([governance/GOVERNANCE_GAPS.md](../../governance/GOVERNANCE_GAPS.md)).
- NR2/NR3 risks in Phase 1.4: swarm leakage, 8-agent topology bleed.

## Sources

- `governance/CANONICAL_DIRECTION.md`
- `agent-os/graph/canonical-vs-research-map.md`
- `Books/swarm-playbooks/governance/corpus-positioning.md`
