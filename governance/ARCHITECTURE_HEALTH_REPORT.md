# Architecture Health Report

**Дата:** 2026-05-25  
**Scope:** Agent-OS + repository layers  
**Scale:** 1 = critical weakness, 10 = production-grade discipline

---

## Domain Scores

| Domain | Score | Evidence | Risks | Recommendation |
|--------|------:|----------|-------|----------------|
| Knowledge architecture | 7 | Clear Books → agent-os layering; 3 corpora + 2 sandboxes | Policy doc stale; no unified layer map | Update `sources.md`; add fourth/fifth corpus entries as **research** |
| Governance | 5 | PROMOTION_REVIEW scoring; concept template | No formal promotion gate in repo; split root/governance docs | Implement `governance/PROMOTION_STRATEGY.md` workflow; single governance index |
| Taxonomy | 7 | Stable 00–12; one-concept-one-file | GUI/modality gap; 06_digital-twins thin | Extend within existing sections before `13_gui-agents/` |
| Source separation | 8 | Claude immutable; experiments isolated; brain-os isolated | Harness generated/raw mixed; orphan READA.md | Complete Harness catalog; document orphans |
| Canonicalization discipline | 6 | Partial extraction only from Claude | Brain OS/Hermes leakage risk if rushed | Enforce RESEARCH_ONLY default for non-Claude |
| Provenance tracking | 5 | `## Sources` in notes; brain-os has Provenance tables | No frontmatter maturity/status on agent-os notes | Add optional frontmatter to template |
| Promotion discipline | 7 | Phase 1.1 scored 65 candidates | Phase 1.2 not executed; no PR checklist | Execute PROMOTE_NOW batch with acceptance criteria |
| Anti-pattern coverage | 5 | 5 antipatterns vs 14+ planned in extraction-plan | GUI, routing, idempotency gaps | Add 3–5 antipatterns Phase 1.2 (from PROMOTION_REVIEW) |
| Digital twin foundations | 4 | 6 notes in 06_digital-twins | No replay, weak verification link | Ground in Claude ch11 + Hermes profile **later** |
| MCP foundations | 6 | 7 notes; ch15 partial | ch16 remote partial; GUI-MCP unresearched in curated | Finish ch15–16 extraction before GUI-MCP |
| Memory architecture | 7 | Taxonomy, recall, compaction | Missing bounded injection, provider rules | Hermes patterns Phase 1.2 (curated only) |
| Multi-agent architecture | 6 | Subagents, swarms, task SM | No Kanban/durable queue; Brain OS overlap | Add kanban-vs-delegate note; reject Brain OS branding |
| GUI-agent readiness | 3 | MobileAgent sandbox only | No curated GUI notes | Defer section; 5 notes in 01/00 first |
| Research isolation | 8 | experiments/ + Books/brain-os/ boundaries respected | Large upstream clones in git | `.gitignore` or document clone policy |
| Navigation quality | 7 | agent-os README + indexes | No cross-layer index until governance/ | Maintain governance/index |
| Scalability | 7 | Atomic notes, kebab-case | Wikilink validation not automated | Phase 3: link linter |
| Maintainability | 6 | Extraction plans exist | Plans may drift from files | Sync extraction_status |
| Future RAG readiness | 6 | Atomic structure, sections | No chunk metadata, no embeddings pipeline | Add frontmatter before RAG |
| Future MCP-memory readiness | 5 | MCP docs exist | No memory-MCP bridge note | Research only until MCP extraction complete |
| Cursor usability | 8 | Markdown, clear paths, skills-friendly | Many files in experiments clones | Point Cursor to review MD paths |
| Obsidian graph readiness | 6 | Wikilinks in template | Incomplete bidirectional links | Link pass after Phase 1.2 |

---

## Aggregate Health

| Metric | Value |
|--------|-------|
| **Mean score** | **6.2 / 10** |
| **Median** | 6.5 |
| **Lowest domains** | GUI readiness (3), digital twins (4), governance (5) |
| **Highest domains** | Source separation (8), research isolation (8), Cursor usability (8) |

## Interpretation

Agent-OS **здоров для ранней стадии Knowledge OS**, но **не зрел для platform/runtime claims**. Система сильна в **discipline of separation** и слаба в **governance automation** и **modality extension governance**.

## Priority Fixes (non-invasive)

1. Update corpora policy (document brain-os, experiments as research)
2. Execute Phase 1.2 PROMOTE_NOW (22 items) with gate
3. Harness survey catalog stubs
4. Anti-pattern + GUI foundation notes without new section
5. Git baseline + extraction_status field

---

## Up

- [FULL_SYSTEM_AUDIT.md](FULL_SYSTEM_AUDIT.md)
