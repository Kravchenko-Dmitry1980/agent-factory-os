# Architecture Worldview

Unified philosophy for the Agent-OS repository — why it exists and how design choices compound.

---

## Why Architecture Matters

Agent engineering collapses into prompt folklore without **decomposed, linked, production-oriented** architecture notes. Monolithic docs do not scale; duplicated paragraphs drift; teams cannot find the boundary between harness, model, and ops UX.

Agent-OS treats architecture as **long-lived engineering knowledge** — one concept per file, contracts over prose, links over duplication.

---

## Why Governance Matters

A wide research perimeter is valuable only if **curated truth stays narrow**. Governance (promotion scoring, logs, freeze rules, canonical direction) prevents:

- research becoming false production spec
- hype topologies entering defaults
- semantic drift via careless wikilinks

Governance is not overhead — it **is** the product for architects.

---

## Why Anti-patterns Matter

Patterns without failures are untested. Anti-patterns without fixes are noise. Paired discipline ([anti-pattern-families.md](anti-pattern-families.md)) captures **operational wisdom and operational danger** from Claude harness, experiments, and isolated operational corpora.

---

## Why Verification Matters

Verification is the **backbone** ([verification-first.md](verification-first.md)). Memory bounds, fail-closed, and governance all assume something checks completion before terminal state and writeback. Remove verification → architecture becomes LLM theater.

---

## Why Operational Discipline Matters

Building agents is staged: MVP, bounded tools, verify, then scale coordination. Operational playbooks (`Books/swarm-playbooks/`) capture HITL and lifecycle UX **without** contaminating canonical layer. Discipline = right tier for right audience.

---

## Why Restraint Matters

Repository evolution favors:

- **coherent worldview** over **larger repository size**
- consolidation over taxonomy inflation
- doctrine synthesis over promotion bursts
- graph navigation docs over ontology products
- readiness declarations over premature infrastructure

Phase 1.4 is restraint made explicit.

---

## Repository Evolution (Condensed)

| Phase | Focus |
|-------|-------|
| 0–1 | Baseline KB bootstrap |
| 1.1 | Promotion scoring (PROMOTION_REVIEW) |
| 1.2 | Governed curated promotion (22 notes) |
| 1.3 | Knowledge graph hardening (semantic clusters) |
| SWARM-EXTRACTION | Operational corpus isolation |
| 1.3R | Governance re-audit, conditional GO |
| **1.4** | **Doctrine synthesis (this layer)** |

Next work (not Phase 1.4): Batch 2 PROMOTE_LATER review, stale governance refresh, optional link linter — **not** runtime buildout.

---

## Design Choices Explained

### Claude harness as spine

Production-proven query loop, tools, permissions — primary conflict winner per promotion strategy.

### Dual golden path

Code and GUI share invariants, different instrumentation — avoids `13_gui-agents/` fork.

### Semantic clusters cross-cut taxonomy

Folders organize by domain; clusters organize by **invariant** (verification, memory, orchestration).

### Doctrine separate from curated notes

Synthesis without rewriting 22+ promoted bodies or creating duplicate definitions.

### Research isolation

Brain OS, Hermes, MobileAgent, swarm — ideas and warnings, not defaults.

---

## Unified Philosophy Statement

Agent-OS is a **governed architecture cognition system**: learn deeply, promote carefully, verify relentlessly, bound memory and autonomy, document failures alongside fixes, and refuse platform inflation.

---

## Sources

- [agent-os/README.md](../README.md) — Architectural Philosophy
- [governance/REPOSITORY_EVOLUTION_MAP.md](../../governance/REPOSITORY_EVOLUTION_MAP.md) (historical)
- [governance/REAUDIT_2026_05_25.md](../../governance/REAUDIT_2026_05_25.md)
- [system-positioning.md](system-positioning.md)
