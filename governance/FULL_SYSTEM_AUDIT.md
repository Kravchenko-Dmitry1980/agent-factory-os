# Full System Audit — Agent-OS Governance

**Дата:** 2026-05-25  
**Workspace:** `C:\Dima\Projects\CURSOR\AGENT`  
**Тип:** governance / architecture / knowledge-system audit  
**Метод:** read-only inventory + cross-document analysis  
**Изменения в репозитории:** только `governance/` (новые файлы)

---

## 0. Executive Verdict

| Вопрос | Ответ |
|--------|--------|
| Agent-OS coherent? | **Да**, как code-harness Knowledge OS — с **растущим modality gap** (GUI, control-plane ideas) |
| Taxonomy healthy? | **Умеренно** — 00–12 стабильны; давление на расширение без `13_gui-agents/` пока обоснованно отложено |
| Premature complexity? | **Частично** — Brain OS + Hermes feature surface создают cognitive load; isolation корректна |
| Architecture inflation? | **Риск средний** — mitigated если promotion discipline соблюдается |
| Эволюция к chaos? | **Нет**, при условии закрытия governance gaps (sources policy, promotion gate, git baseline) |

**Главный вывод:** проект эволюционирует **правильно по слоям** (source → research → curated), но **governance layer отстаёт от content layer**. Требуется Phase 1.2–1.3 с жёстким promotion pipeline, не taxonomy expansion.

---

## 1. Repository Layer Model

```
AGENT/
├── Books/              ← SOURCE + derived research KB (3 corpora)
├── experiments/        ← ISOLATED sandboxes (upstream clones + review MD)
├── agent-os/           ← CURATED knowledge (partial extraction)
├── governance/         ← GOVERNANCE (this audit)
├── *.md (root)         ← BASELINE + PROMOTION reviews
└── .venv/              ← local tooling (gitignored)
```

| Layer | Mutability | Canonical? |
|-------|------------|------------|
| `Books/claude/` | Immutable source | **Yes** (primary) |
| `Books/agents/` | PDF immutable; MD generated | **Yes** (secondary, QA pending) |
| `Books/brain-os/` | source docx immutable | **No** — research-only |
| `experiments/` | Read/analyze only | **No** |
| `agent-os/00–09/` | Curated, governed promotion | **Yes** (partial) |
| `agent-os/10_research/` | Catalog + plans | Meta-canonical |
| `governance/` | Governance artifacts | Process-canonical |

---

## 2. Corpora Inventory

### 2.1 Claude Code (`Books/claude/`)

| Dimension | Assessment |
|-----------|------------|
| **Role** | Primary canonical source for Agent-OS extraction |
| **Maturity** | Production-grade source text (18 chapters) |
| **Status** | Integrated: stubs in `10_research/chapters/` |
| **Canonicality** | **Canonical source** |
| **Extraction completeness** | 🟡 Partial (~85 atomic notes; ch9,12–14,16–18 ⬜) |
| **Governance level** | High — `sources.md` policy explicit |
| **Integration level** | Strong — drives 00–09 taxonomy |
| **Duplication risks** | Low (stubs ≠ chapter bodies) |
| **Promotion readiness** | N/A (source, not promoted) |

### 2.2 Harness Survey (`Books/agents/`)

| Dimension | Assessment |
|-----------|------------|
| **Role** | Secondary canonical survey (arXiv 2605.18747) |
| **Maturity** | PDF + pipeline OK; MD QA pending |
| **Status** | Listed in `sources.md`; **no** `10_research/` chapter stubs |
| **Canonicality** | **Canonical source** (immature catalog) |
| **Extraction completeness** | ⬜ Not started in agent-os |
| **Governance level** | Medium — policy exists, catalog gap |
| **Integration level** | Weak — README/sources only |
| **Duplication risks** | Medium — overlaps Claude on harness concepts |
| **Promotion readiness** | Low until catalog + QA |

**Gap:** `extraction-plan.md` still Claude-only roadmap; Harness ch1–6 not mapped.

### 2.3 Brain OS (`Books/brain-os/`)

| Dimension | Assessment |
|-----------|------------|
| **Role** | Author control-plane design draft (docx → 67 MD notes) |
| **Maturity** | Design v0.1 — contracts as JSON examples, no OpenAPI |
| **Status** | Self-contained KB; **not** in `agent-os/10_research/sources.md` |
| **Canonicality** | **Research-only** (correct isolation) |
| **Extraction completeness** | Internal KB complete (13 concepts, 8 contracts, review/) |
| **Governance level** | Self-governed (`review/`, maturity labels) |
| **Integration level** | Zero curated integration (by design) |
| **Duplication risks** | High **if promoted early** — overlaps orchestration, routing, trace, multi-agent |
| **Promotion readiness** | **PROMOTE_LATER / RESEARCH_ONLY** per `Books/brain-os/review/promotion-candidates.md` |

**Verdict:** ingestion **корректна** как отдельный corpus; premature promotion **опасна**.

---

## 3. Experiments Inventory

### 3.1 Hermes (`experiments/hermes-agent-review/`)

| Dimension | Assessment |
|-----------|------------|
| **Architectural relevance** | High — memory injection, skills, Kanban, profiles, MCP consumer |
| **Overlap with Agent-OS** | Fills gaps in 02_memory, 04_multi-agent, 06_digital-twins, 08_patterns |
| **Reusable patterns** | 22 PROMOTE_NOW candidates (`PROMOTION_REVIEW.md`) |
| **Dangerous abstractions** | Gateway 20+ platforms, 8 memory providers, god entry points |
| **Taxonomy pressure** | Medium — Kanban primitive, curator, profile isolation |
| **Future direction** | Durable orchestration + bounded memory for digital twins |

**Upstream clone:** `source/hermes-agent/` inflates file count (~1300+ MD in tree) — **not** curated content.

### 3.2 MobileAgent (`experiments/mobile-agent-review/`)

| Dimension | Assessment |
|-----------|------------|
| **Architectural relevance** | High — GUI loop, visual verification, grounding |
| **Overlap with Agent-OS** | Extends verification, runtime; **no** existing GUI section |
| **Reusable patterns** | GUI loop, A/B/C verification, coordinate spaces |
| **Dangerous abstractions** | OCR pipeline, ADB runners, monolithic VLM loop as canonical |
| **Taxonomy pressure** | **High** — pushes for `13_gui-agents/` |
| **Future direction** | Embodied agent modality alongside code harness |

**Verdict:** sandboxes **correctly isolated**; `PROMOTION_REVIEW.md` Phase 1.1 done properly.

---

## 4. Curated Layer (`agent-os/`)

### 4.1 Section Health Summary

| Section | Files | Health | Notes |
|---------|------:|--------|-------|
| `00_foundations/` | 11 | 🟢 Strong | Core ontology anchor |
| `01_agent-runtime/` | 11 | 🟢 Strong | Query loop complete |
| `02_memory/` | 9 | 🟡 Good | Missing Hermes-style bounds/injection |
| `03_harness-engineering/` | 10 | 🟢 Strong | ch12 hooks pending |
| `04_multi-agent/` | 7 | 🟡 Good | No durable queue primitive |
| `05_mcp/` | 7 | 🟡 Good | ch16 partial |
| `06_digital-twins/` | 6 | 🟠 Thin | Conceptual; weak grounding |
| `07_projects/` | 6 | 🟡 OK | Applied, not core ontology |
| `08_patterns/` | 8 | 🟢 Strong | 7 patterns + index |
| `09_antipatterns/` | 6 | 🟠 Thin | 5 antipatterns vs many gaps |
| `10_research/` | 30 | 🟡 Catalog | Stubs OK; corpora policy stale |
| `11_glossary/` | 5 | 🟠 Thin | Pointer stubs |
| `12_diagrams/` | 4 | 🟠 Thin | Code-centric only |

### 4.2 Cross-Cutting Issues

| Issue | Severity |
|-------|----------|
| No `extraction_status` on atomic notes | Medium |
| `sources.md` lists 2 corpora only | **High** |
| Glossary vs concept overlap (harness, query-loop) | Medium |
| No GUI modality in curated layer | Expected gap |
| Digital twin notes ahead of verification/replay | Medium |
| Wikilinks present but no graph governance | Medium |

### 4.3 Navigation Quality

- Section `index.md` files exist (14 sections)
- Root `agent-os/README.md` — strong navigation
- **Missing:** unified map Books → experiments → agent-os
- **Missing:** governance index until this audit

---

## 5. Governance Documents (pre-audit)

| Document | Location | Role | Status |
|----------|----------|------|--------|
| CURRENT_STATE_AUDIT.md | root | Baseline inventory | Snapshot 2026-05-21; partially stale |
| BASELINE_STATUS.md | root | Phase 0.1 status | Commits now exist |
| PROMOTION_REVIEW.md | root | Phase 1.1 | Complete, actionable |
| governance/* | governance/ | Full audit | **This phase** |

**Drift:** governance docs split between root and `governance/` — consolidate references in Phase 2.

---

## 6. Critical Questions — Answers

| # | Question | Answer |
|---|----------|--------|
| 1 | Coherent? | Yes as harness KB; modality extension pending |
| 2 | Taxonomy healthy? | Moderate — stable skeleton, content gaps |
| 3 | Premature complexity? | Research layer yes; curated layer no |
| 4 | Architecture inflation? | Risk if Brain OS/Hermes promoted wholesale |
| 5 | GUI ready for canonical? | **No** — threshold ≥5 notes + verification first |
| 6 | Digital twins grounded? | Partial — identity/memory concepts, no replay |
| 7 | Brain OS too speculative? | **Yes for canonical**; OK as isolated corpus |
| 8 | Hermes overfitting taxonomy? | **Risk** if runtime features promoted |
| 9 | MobileAgent modality drift? | **Risk** without GUI governance charter |
| 10 | True foundation? | **Claude Code harness + extraction discipline** |
| 11 | Evolution direction? | **Architecture OS + research library** — not runtime chaos |

---

## 7. Related Governance Artifacts

| Document | Purpose |
|----------|---------|
| [ARCHITECTURE_HEALTH_REPORT.md](ARCHITECTURE_HEALTH_REPORT.md) | Domain scoring |
| [TAXONOMY_REVIEW.md](TAXONOMY_REVIEW.md) | Section analysis |
| [PHASE_ALIGNMENT_REVIEW.md](PHASE_ALIGNMENT_REVIEW.md) | Phase validation |
| [CANONICAL_DIRECTION.md](CANONICAL_DIRECTION.md) | What is canonical |
| [GOVERNANCE_GAPS.md](GOVERNANCE_GAPS.md) | Missing standards |
| [ARCHITECTURAL_DRIFT_REPORT.md](ARCHITECTURAL_DRIFT_REPORT.md) | Drift analysis |
| [PROMOTION_STRATEGY.md](PROMOTION_STRATEGY.md) | Safe promotion |
| [NEXT_PHASE_ROADMAP.md](NEXT_PHASE_ROADMAP.md) | Next steps |
| [RISK_REGISTER.md](RISK_REGISTER.md) | Risk tracking |
| [REPOSITORY_EVOLUTION_MAP.md](REPOSITORY_EVOLUTION_MAP.md) | Evolution narrative |
| [KNOWLEDGE_GRAPH_DIRECTION.md](KNOWLEDGE_GRAPH_DIRECTION.md) | Graph future |
| [diagrams/](diagrams/) | Mermaid diagrams |

---

*Read-only audit. No changes to agent-os/, Books/, experiments/.*
