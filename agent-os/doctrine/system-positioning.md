# System Positioning

**Most important doctrine document.** Defines what Agent-OS is and explicitly what it is not.

Phase 1.4 consolidation — no platform inflation.

---

# What Agent-OS IS

## Architecture cognition system

A structured way to **think about, document, and govern** agent harness architecture — through atomic curated notes, semantic clusters, patterns paired with anti-patterns, and promotion discipline. cognition substrate, not running agent fleet.

## Governance-driven knowledge substrate

Knowledge enters the curated layer (`00–09/`) only through [governance/PROMOTION_STRATEGY.md](../../governance/PROMOTION_STRATEGY.md): scoring, review, logging, validation. The repository **is** the governance artifact for architecture decisions.

## Architecture research and consolidation framework

Wide research perimeter (`experiments/`, `Books/*`, operational playbooks) feeds **narrow canonical core**. Phase 1.4 adds [doctrine/](README.md) as synthesis worldview — still not runtime.

## Engineering knowledge OS for agent harness architecture

Primary spine: Claude production harness ([Books/claude/](../../Books/claude/)) decomposed into query loop, tools, permissions, memory file model, MCP, subagents. Dual golden path: [[query-loop]] ∥ [[gui-agent-loop]].

## Semantic graph for navigation

[graph/](../graph/README.md) layer (Phase 1.3) — clusters, maps, provenance, traversal rules. **Documentation navigation**, not intelligence simulation or graph database product.

## Anti-pattern + pattern paired discipline

Every failure mode should adjacency-link mitigations ([anti-pattern-families.md](anti-pattern-families.md)). Production implications required in curated notes.

## Future-ready substrate (declarative only)

README states RAG-ready, MCP-ready, digital-twin-ready **as note structure goals** — not implemented pipelines in this repository phase.

---

# What Agent-OS IS NOT

Explicit rejections — doctrine and positioning guardrails:

| Claim | Rejection |
|-------|-----------|
| **Autonomous AI operating system** | No runtime OS; knowledge + governance |
| **AGI platform** | No general intelligence claims |
| **Self-improving intelligence** | [[recursive-self-improvement]] is anti-pattern |
| **Production orchestration runtime** | No Hermes/MobileAgent/swarm stack execution |
| **Universal agent framework** | Not install-and-run multi-agent product |
| **Digital twin runtime** | No replay model; [[persistent-identity]] curated scope only |
| **Autonomous ontology engine** | Graph = markdown navigation; no ontology DB |
| **8-agent swarm blueprint** | Operational tutorial topology — NEVER canonical default |
| **Critic-as-verification substitute** | Critique ≠ verify ([verification-first.md](verification-first.md)) |
| **Tutorial / install scaffold docs** | Beginner prompts ≠ architecture |
| **RAG / embedding pipeline** | Readiness notes only; not built here |
| **MCP runtime product** | Reference material for protocol |
| **Brain OS control plane product** | Research ideas; strip plane branding |

---

# Layer Model

```
┌─────────────────────────────────────────┐
│  doctrine/ (Phase 1.4 synthesis)        │
├─────────────────────────────────────────┤
│  agent-os/00–09 curated canonical       │
├─────────────────────────────────────────┤
│  agent-os/graph semantic navigation     │
├─────────────────────────────────────────┤
│  governance/ promotion & audit          │
├─────────────────────────────────────────┤
│  Books/* + experiments/ research        │
├─────────────────────────────────────────┤
│  Books/swarm-playbooks operational      │
└─────────────────────────────────────────┘
```

---

# Audience Positioning

| Audience | Entry |
|----------|-------|
| Agent engineer | [golden-path](../00_foundations/golden-path.md) → [query-loop](../01_agent-runtime/query-loop.md) |
| Architect | [architecture-worldview.md](architecture-worldview.md) → [canonical-principles.md](canonical-principles.md) |
| Governance reviewer | [governance/REAUDIT_2026_05_25.md](../../governance/REAUDIT_2026_05_25.md) |
| Operator (non-canonical ops) | `Books/swarm-playbooks/README.md` |

---

# Phase 1.4 Scope Boundary

This document ** consolidates positioning** — it does not expand product scope. NR1–NR6 risks in [governance/UPDATED_RISK_REGISTER_DELTA.md](../../governance/UPDATED_RISK_REGISTER_DELTA.md) monitor positioning drift.

---

# Sources

- [agent-os/README.md](../README.md)
- [governance/CANONICAL_DIRECTION.md](../../governance/CANONICAL_DIRECTION.md)
- [governance/CONSOLIDATION_CANDIDATES.md](../../governance/CONSOLIDATION_CANDIDATES.md) § System Positioning
- [governance/PHASE_1_4_READINESS.md](../../governance/PHASE_1_4_READINESS.md)

See also: [diagrams/system-positioning.md](diagrams/system-positioning.md)
