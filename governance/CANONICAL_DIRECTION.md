# Canonical Direction

**Дата:** 2026-05-25  
**Principle:** Narrow canonical core, wide research perimeter

---

## What Is Canonical Now

| Layer | Path | Canonical meaning |
|-------|------|-------------------|
| Primary source | `Books/claude/` | Immutable extraction source |
| Secondary source | `Books/agents/` (PDF + chapters) | Immutable; QA pending |
| Curated concepts | `agent-os/00–09/` | **Partial canonical knowledge** (~85 notes) |
| Patterns | `agent-os/08_patterns/` | Canonical patterns (Claude-derived) |
| Antipatterns | `agent-os/09_antipatterns/` | Canonical failures (partial set) |
| Catalog | `agent-os/10_research/` | Meta — plans + stubs, not body text |
| Template | `agent-os/templates/concept-note-template.md` | Contract for new canonical notes |

**Canonical spine:** Claude Code **production agent harness** — query loop, tools, permissions, memory file model, MCP, subagents.

---

## What Is Research-Only

| Layer | Path | Rule |
|-------|------|------|
| Brain OS KB | `Books/brain-os/` | Author draft; maturity labels; no curated promotion without gate |
| Hermes sandbox | `experiments/hermes-agent-review/` | Pattern extraction source |
| MobileAgent sandbox | `experiments/mobile-agent-review/` | GUI modality research |
| Upstream clones | `experiments/*/source/` | Reference only; not knowledge |
| Harness chapters | `Books/agents/chapters/` | Source until QA + catalog |
| Promotion backlog | `PROMOTION_REVIEW.md` | Recommendations, not canonical |

---

## What Is Speculative

- Brain OS: adaptation-service, Honcho-style planes, full ER as normative
- Hermes: gateway matrix, 8 memory providers, bundled skills catalog
- MobileAgent: GUI-Owl weights, MA-E self-evolution, OCR pipelines
- Agent-OS `06_digital-twins/` deep operational claims without replay
- GUI-MCP hybrid routing (model policy, not harness spec)

Mark as **speculative** in any future curated note `## My Notes`.

---

## What Should NEVER Become Canonical

| Item | Why |
|------|-----|
| Upstream product code (Hermes, MobileAgent repos) | Not knowledge layer |
| Brain OS plane branding without IPC contracts | branding-only |
| Universal Analyst/Critic/Strategist/Synthesizer | weak-abstraction |
| Runtime deployment configs (Modal, gateway adapters) | Product-specific |
| marketing «cognitive platform» language without contracts | hype |
| Duplicate glossary definitions | Breaks one-concept-one-file |
| Auto-merged comparison tables from experiments | Loses provenance |

---

## What Should Become Foundational (curated, phased)

**Phase 1.2 (PROMOTE_NOW from PROMOTION_REVIEW):**

- Frozen memory snapshot, memory char limits
- Kanban vs delegate, subagent tool restrictions
- Progressive skill disclosure
- Profile isolation (digital twin instance)
- GUI agent loop, visual verification A/B/C
- Core GUI + orchestration antipatterns

**Phase 1.3 (PROMOTE_LATER):**

- Curator pattern (with governance invariants)
- Kanban orchestration detail
- Harness survey extraction (after catalog)
- Brain OS: trace-first, deterministic routing (stripped of branding)

---

## Concept Cluster Classification

| Cluster | Canonical | Research | Experimental | Reject | Why |
|---------|-----------|----------|--------------|--------|-----|
| Control planes | Partial (orchestration.md) | Brain OS full stack | Hermes gateway as CP | Brain OS plane names as entities | Curated = harness CP not product CP |
| Routing systems | Partial (runtime paths) | Brain OS choose_mode | Adaptive routing v0.3 | LLM-only router | Need deterministic rules first |
| Memory systems | **Yes** (taxonomy, recall) | Hermes bounds, providers | Honcho dialectic | Unbounded memory | Core Claude + bounded extensions |
| Execution supervision | Partial (recovery ladder) | Brain OS supervisor | — | — | Extend ladder, don't fork OS |
| GUI agents | No | **MobileAgent** | v3.5 monolithic VLM | OCR v1/v2 default | Modality not in canonical yet |
| MCP orchestration | **Yes** (protocol partial) | Hermes client patterns | GUI-MCP hybrid | OAuth impl detail | Finish ch15–16 first |
| Digital twins | Thin canonical | Hermes profiles, Mobile surfaces | MA-E evolution | Twin without replay | Ground before expand |
| Evolving memory | Partial | Curator, Brain adaptation | Self-write without gate | Uncontrolled adaptation | Governance required |
| Self-improving agents | No | Hermes curator | MA-E, UI-S1 RL | Auto-delete skills | Safety-first promotion |
| Role systems | Partial (04) | Brain 4-role template | — | Universal template | Domain-specific roles |
| Multi-agent orchestration | **Yes** (subagents, swarms) | Kanban, InfoPool | Mixture of agents | Recursive delegation | Add durable queue carefully |
| Verification systems | **Yes** (hooks, verification) | Visual A/B/C | GUI-Critic pre-op | Unverified clicks | Extend modality |
| Embodied agents | No | MobileAgent loop | ADB runners | Raw pixel scripts | Harness patterns only |

---

## Up

- [PROMOTION_STRATEGY.md](PROMOTION_STRATEGY.md)
- [TAXONOMY_REVIEW.md](TAXONOMY_REVIEW.md)
