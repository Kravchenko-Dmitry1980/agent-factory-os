# Next Phase Roadmap

**Дата:** 2026-05-25  
**Horizon:** Immediate → 3 phases → freeze zones

---

## Immediate Next Safe Step

**Phase 1.2 — Governed Curated Promotion (PROMOTE_NOW only)**

1. Approve promotion batch from `PROMOTION_REVIEW.md` (22 items)
2. Create notes in existing sections only — **no `13_gui-agents/`**
3. Update `agent-os/10_research/sources.md` — add **research tier** entries (brain-os, experiments) without elevating to canonical source
4. Tag git baseline: commit curated promotions as single logical batch
5. Update section indexes + wikilinks

**Estimated scope:** ~15–22 new/updated files in `agent-os/` — **requires explicit user approval** (not auto).

---

## Next 3 Phases

### Phase 1.2 — Safe Curated Promotions (weeks 1–2)

- Execute PROMOTE_NOW
- Add 3–5 GUI antipatterns
- Cross-ref prompt-cache + frozen memory
- **Exit criteria:** PROMOTION_REVIEW §10 checklist per file

### Phase 1.3 — Deferred Promotions + Catalog (weeks 3–6)

- Harness survey stubs in `10_research/`
- PDF/chapters QA
- PROMOTE_LATER batch (curator, kanban orchestration, shared pool)
- Extraction wave 1: ch9, ch12, ch17
- Optional: Brain OS trace-first / deterministic routing as **stripped** patterns

### Phase 1.4 — Research Backlog + Graph Discipline (weeks 7–10)

- RESEARCH_ONLY items stay in sandboxes
- Link linter + extraction_status
- `12_diagrams/` updates for GUI + promotion pipeline
- Evaluate `13_gui-agents/` threshold (need scorecard)

---

## Dangerous Future Directions

| Direction | Risk |
|-----------|------|
| Implement Brain OS microservices | Confuses KB with product |
| Merge experiments upstream into monorepo root | Governance collapse |
| Auto-RAG all markdown | Duplicate embeddings |
| New taxonomy section per corpus | Taxonomy explosion |
| Canonicalize self-adaptation | Uncontrolled drift |
| GUI ADB tools in agent-os | Runtime leakage |
| Replace Claude spine with multi-corpus merge | Loss of coherence |

---

## Recommended Focus

1. **Finish Claude extraction spine** (ch9,12,14,16,17,18)
2. **Execute scored promotions** — Hermes memory + Mobile GUI verification
3. **Expand antipatterns** — cheap, high leverage
4. **Governance hygiene** — sources policy, promotion log
5. **Harness catalog** — second canonical source properly integrated

---

## What NOT To Do

- Create `13_gui-agents/` now
- Promote Brain OS planes (CAIM, MirrorMind, …) as Agent-OS concepts
- Copy Hermes/MobileAgent code into repo root
- Rewrite existing curated notes wholesale
- Add OpenAPI specs to agent-os as if production
- Skip scoring for «obvious good ideas»

---

## What To Postpone

- Semantic ontology layer
- RAG embedding pipeline
- MCP-memory integration notes
- Digital twin replay architecture
- adaptation-service / curator automation
- OSWorld-MCP external repo ingestion

---

## What To Freeze

| Zone | Freeze rule |
|------|-------------|
| `Books/claude/` | Immutable |
| `Books/agents/all.pdf` | Immutable |
| `Books/brain-os/source/` | Immutable docx |
| `agent-os/` taxonomy 00–12 | No renumbering |
| `experiments/` boundaries | No agent-os edits from sandboxes without promotion |
| Upstream clones | No curation of vendor trees |

---

## Up

- [PHASE_ALIGNMENT_REVIEW.md](PHASE_ALIGNMENT_REVIEW.md)
- [PROMOTION_STRATEGY.md](PROMOTION_STRATEGY.md)
- [RISK_REGISTER.md](RISK_REGISTER.md)
