# Canonical vs Research Map

Explicit layer separation for Agent-OS knowledge system. Prevents research leakage into canonical traversal.

---

## Layer Definitions

| Layer | Meaning | Location | Link as canonical? |
|-------|---------|----------|-------------------|
| **Frozen** | Immutable source corpora | `Books/claude/`, `Books/agents/` (PDF) | Cite only — not curated body |
| **Canonical** | Governance-approved curated concepts | `agent-os/00–09/` promoted notes | Yes — primary wikilink targets |
| **Research** | Scored sandboxes, Brain OS draft | `experiments/`, `Books/brain-os/` | No — path reference only |
| **Experimental** | Unverified ideas, local prototypes | `experiments/*/experiments/`, open questions | No |
| **Rejected** | Governance-blocked promotion | PROMOTION_REVIEW REJECT rows | Document only — no wikilink |

---

## Canonical (Phase 1.2 promotion set)

### Memory governance
- [[frozen-memory-snapshot]], [[memory-char-limits]], [[profile-isolation]], [[memory-provider-boundaries]]

### Orchestration
- [[kanban-vs-delegate]], [[subagent-tool-restrictions]], [[durable-task-coordination]]

### GUI modality
- [[gui-agent-loop]], [[visual-grounding]], [[visual-verification]]

### Patterns
- [[progressive-skill-disclosure]], [[memory-aware-execution]], [[verification-before-writeback]], [[fail-closed-agent-loop]]

### Anti-patterns
- [[unverified-gui-clicks]], [[brittle-gui-automation]], [[mid-session-memory-injection]], [[unbounded-memory-growth]], [[recursive-self-improvement]]

### Pre-existing canonical (Claude-derived, not Phase 1.2)
- Query loop, harness, MCP, subagents (baseline), Claude patterns in `08_patterns/`

---

## Research (promotion-gated)

| Path | Status | Curated? |
|------|--------|----------|
| `Books/brain-os/` | Author draft | Partial ideas only (stripped) |
| `experiments/hermes-agent-review/` | Sandbox | Patterns promoted; runtime rejected |
| `experiments/mobile-agent-review/` | Sandbox | GUI concepts promoted; scripts rejected |
| trace-first-architecture | Brain OS pattern | **Not curated** — cluster adjacency only |
| human-escalation-gate | Brain OS pattern | **Not curated** — cluster adjacency only |
| adaptation-service | Brain OS | **Rejected** frozen |
| GUI-MCP hybrid routing | MobileAgent | RESEARCH_ONLY |
| Honcho dialectic | Hermes | RESEARCH_ONLY |

---

## Experimental

- Hermes gateway adapters, sandbox backend matrix
- MobileAgent OCR pipelines, UI-S1 training, GUI-Critic pre-op integration
- Local MCP mock contracts (not in repo root)

---

## Rejected (do not link as canonical)

| Item | Reason |
|------|--------|
| Hermes gateway 20+ adapters | Product surface |
| MobileAgent run scripts / weights | Runtime not knowledge |
| Brain OS plane branding as entities | Branding without contracts |
| `13_gui-agents/` section | Taxonomy threshold not met |
| adaptation-service without governance | CANONICAL_DIRECTION frozen |

---

## Traversal Rule

When navigating via [[graph/navigation/cluster-navigation|cluster navigation]]:

1. Prefer **canonical** wikilinks
2. Research nodes → plain path + `(research)` label
3. Rejected → mention in drift analysis only

---

## Up

- [provenance-graph.md](provenance-graph.md)
- [agent-os/10_research/sources.md](../10_research/sources.md)
- [governance/CANONICAL_DIRECTION.md](../../governance/CANONICAL_DIRECTION.md)
