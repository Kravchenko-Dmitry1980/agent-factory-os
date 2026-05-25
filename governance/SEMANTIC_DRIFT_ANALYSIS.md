# Semantic Drift Analysis

**Phase:** 1.3  
**Date:** 2026-05-25

---

## Overlinked Concepts (risk)

| Concept | Risk | Mitigation |
|---------|------|------------|
| [[fail-closed-agent-loop]] | Bridge to 3 clusters — link spam if every note links it | Link only from verification, orchestration, GUI verify paths |
| [[visual-verification]] | Central GUI+verify hub | Cap Related Concepts at 6–8 |
| [[prompt-cache-as-constraint]] | Memory + API cross-links | Keep memory cluster primary |

**Current state:** Acceptable after Phase 1.3 — no note exceeds 8 intentional Related links.

---

## Weak Clusters

| Cluster | Weakness | Strength |
|---------|----------|----------|
| **Verification** | trace-first, human-escalation not curated | Strong GUI+hook spine |
| **Promotion governance** | Meta-only — no runtime | Strong audit trail |
| **GUI modality** | Only 3 core concepts | Tight anti-pattern pairing |
| **Orchestration** | Kanban detail PROMOTE_LATER | Primitive matrix clear |
| **Memory governance** | Strongest — 7 curated + 4 anti-patterns | **Strongest cluster** |

---

## Duplicated Semantic Zones

1. **Verification trilogy** — `verification`, `execution-verification`, `visual-verification` — differentiated in verification-map (foundation / harness / GUI).
2. **Fail-closed pair** — tool defaults vs loop lifecycle — drift if merged; kept separate.
3. **Identity** — `profile-isolation` (memory) vs `persistent-identity` (session) — intentional split; watch for merge pressure.

---

## Unstable Terminology

| Term | Variants | Canonical |
|------|----------|-----------|
| Kanban vs durable queue | Kanban, task board, queue | [[durable-task-coordination]] |
| A/B/C | reflect outcomes, verification taxonomy | [[visual-verification]] |
| Frozen snapshot | static memory, inject once | [[frozen-memory-snapshot]] |
| Fail-closed | fail-safe defaults, stop on verify fail | disambiguate via glossary |

---

## Weak Provenance

- `memory-aware-execution` — dual Hermes + Brain OS origin must stay explicit
- `verification-before-writeback` — Brain OS stripped; do not reintroduce event envelope names
- ch12 `progressive-skill-disclosure` — Claude extraction still ⬜; Hermes-primary until ch12 lands

---

## Hidden Taxonomy Expansion Signals

| Signal | Status |
|--------|--------|
| `13_gui-agents/` pressure | **Blocked** — 3 GUI notes in 01/00 sufficient |
| New memory provider notes | **Blocked** — boundaries concept covers |
| Brain OS plane entities | **Blocked** — research map |
| Graph DB folder | **Blocked** — graph/ is docs only |

---

## Graph-Noise Risks

| Risk | Severity | Control |
|------|----------|---------|
| Auto-backlink every index mention | High | Manual Related sections only |
| Wikilink to research as canonical | High | canonical-vs-research-map |
| Concept maps duplicate note bodies | Medium | Maps link only, no definitions |
| Glossary re-definitions | Medium | Pointer-only rule |

---

## Concept Inflation

- Phase 1.2 added 22 nodes — within PROMOTE_NOW budget ✅
- Phase 1.3 adds 0 concepts — graph layer only ✅
- **Most dangerous drift:** promoting Brain OS trace-first + human-escalation as curated without contract spec — **deferred**

---

## Strongest Semantic Cluster

**Memory governance** — highest node density, clearest anti-pattern adjacency, provenance from Hermes, Claude cache cross-link.

---

## Most Dangerous Semantic Drift

**Treating GUI modality as third taxonomy spine without verification cluster** — would produce unverified-click production paths. Mitigated by mandatory GUI ↔ visual-verification ↔ unverified-gui-clicks triangle.

---

## Governance Violations Found

**None** in Phase 1.3 scope — no new concepts, no Books/experiments edits, no infrastructure.

---

## Up

- [SEMANTIC_LINKING_AUDIT.md](SEMANTIC_LINKING_AUDIT.md)
- [agent-os/graph/concept-clusters.md](../agent-os/graph/concept-clusters.md)
