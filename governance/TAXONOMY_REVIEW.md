# Taxonomy Review

**Дата:** 2026-05-25  
**Scope:** `agent-os/00` … `12` + pressure from corpora/experiments

---

## Section Analysis

| Section | Load | Strength | Weakness | Duplication | Verdict |
|---------|------|----------|----------|-------------|---------|
| `00_foundations/` | Medium | Golden path, harness, verification | No GUI-as-environment | Overlap with 01 on loops | **Keep — core** |
| `01_agent-runtime/` | Medium | Query loop, tools, recovery | No GUI loop | query-loop glossary dup | **Keep — extend for GUI notes first** |
| `02_memory/` | Medium | Taxonomy, compaction | No char limits / frozen snapshot | Claude vs future Hermes | **Keep — priority extension** |
| `03_harness-engineering/` | Medium | Permissions, hooks | ch12 skills/hooks incomplete | verification vs foundations | **Keep — finish ch12** |
| `04_multi-agent/` | Low-Med | Subagents, swarms | No durable queue | Brain OS Kanban overlap | **Keep — add 1–2 notes max** |
| `05_mcp/` | Low | Protocol, transports | Remote bridges partial | — | **Keep — finish ch16** |
| `06_digital-twins/` | Low | Identity, personas | Speculative depth | Hermes profiles overlap | **Keep thin — no inflation** |
| `07_projects/` | Low | Applied examples | Not ontology | — | **Keep — non-canonical examples** |
| `08_patterns/` | Medium | 7 strong patterns | Missing skill disclosure | Some pattern/concept blur | **Keep — controlled adds** |
| `09_antipatterns/` | **Underloaded** | 5 entries | GUI, routing, idempotency missing | Pairs incomplete vs plan | **Priority expansion** |
| `10_research/` | Medium | Stubs, plans | Stale sources policy | — | **Update policy not structure** |
| `11_glossary/` | **Underloaded** | Pointers | Stub-only entries | Duplicates 00 concepts | **Pointers only — enforce rule** |
| `12_diagrams/` | **Underloaded** | 3 diagrams | Code-only | — | **Add after promotions** |

---

## Overloaded Sections

**None critically overloaded.** Closest: `00_foundations/` + `01_agent-runtime/` if GUI + verification notes land without split — monitor file count (threshold: **15 notes/section** → consider sub-index).

---

## Underdeveloped Sections

1. **`09_antipatterns/`** — 5 vs 14+ in extraction plan
2. **`11_glossary/`** — 5 stubs
3. **`12_diagrams/`** — no GUI, no promotion pipeline
4. **`06_digital-twins/`** — concepts without operational contracts

---

## Duplicated Concepts (known)

| Concept | Locations | Resolution |
|---------|-----------|------------|
| harness | 00_foundations, 11_glossary | Glossary → pointer only ✅ by design |
| query-loop | 01_agent-runtime, 11_glossary | Same |
| six-abstractions | 00_foundations, 12_diagrams | Concept vs diagram ✅ |
| verification | 00_foundations, 03_harness-engineering | Clarify scope in Phase 1.2 |
| orchestration | 00_foundations, Brain OS corpus | **Do not merge** — Brain OS research-only |

---

## Missing Sections (evaluated)

| Proposed | Decision | Evidence |
|----------|----------|----------|
| `13_gui-agents/` | **LATER** | PROMOTION_REVIEW: need ≥5 GUI notes in 01/00 first; MobileAgent 22 PROMOTE_NOW includes GUI but fits existing sections |
| `14_control-plane/` | **REJECT** | Brain OS branding; overlaps 00 orchestration + 01 runtime |
| `15_governance/` | **Optional repo root** | Use `governance/` at repo root, not agent-os taxonomy |

---

## Critical Question: `13_gui-agents/` now or later?

### Decision: **LATER**

### Threshold criteria (all required before YES)

| # | Criterion | Current |
|---|-----------|---------|
| 1 | ≥5 GUI atomic notes promoted to curated layer | 0 |
| 2 | Visual verification note in foundations/runtime | 0 |
| 3 | ≥3 GUI antipatterns in 09 | 0 |
| 4 | GUI golden path diagram in 12_diagrams | 0 |
| 5 | `01_agent-runtime/index.md` navigation strain OR ≥12 runtime notes | 11 notes — below threshold |
| 6 | Governance charter for GUI modality approved | Missing |

### Interim home (Phase 1.2–1.3)

- `01_agent-runtime/gui-agent-loop.md`
- `01_agent-runtime/visual-grounding.md`
- `00_foundations/visual-verification.md`
- `09_antipatterns/unverified-gui-clicks.md`

---

## Ontology Conflicts

| Conflict | Parties | Mitigation |
|----------|---------|------------|
| Harness vs GUI harness | Claude vs MobileAgent | Sub-modality under runtime, not parallel OS |
| Control plane vs harness | Brain OS vs Agent-OS | Brain OS stays Books/ only |
| Twin vs subagent | 06 vs 04 | Explicit boundary note in promotion |
| Memory taxonomy vs MEMORY.md bounds | Claude ch11 vs Hermes | Extend 02 without renaming taxonomy types |

---

## Abstraction Leaks

- **Digital twin** language in 06 without replay contract → mark speculative in My Notes
- **Self-improving** (Hermes curator, Brain OS adaptation) near 06/08 → RESEARCH_ONLY until governance
- **Multi-agent template** (Analyst/Critic/…) from Brain OS → reject as universal pattern

---

## Up

- [FULL_SYSTEM_AUDIT.md](FULL_SYSTEM_AUDIT.md)
- [CANONICAL_DIRECTION.md](CANONICAL_DIRECTION.md)
