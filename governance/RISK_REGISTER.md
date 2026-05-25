# Risk Register

**Дата:** 2026-05-25  
**Review cycle:** Per phase gate

---

## Risk Table

| ID | Risk | Severity | Likelihood | Cause | Mitigation | Owner phase |
|----|------|----------|------------|-------|------------|-------------|
| R1 | Taxonomy explosion | High | Medium | GUI + CP + twin sections | Threshold before `13_gui-agents/` | 1.4 |
| R2 | Canonical drift from Brain OS | High | Medium | Similar vocabulary (routing, trace) | RESEARCH_ONLY default; strip branding | 1.2+ |
| R3 | Hermes overfitting | Medium | Medium | 22 PROMOTE_NOW items | Batch promote; reject gateway/providers | 1.2 |
| R4 | MobileAgent modality drift | Medium | Medium | GUI without harness permissions | Antipatterns first; no ADB in agent-os | 1.2 |
| R5 | Research → curated leakage | High | Low | Skipping promotion gate | PROMOTION_STRATEGY pipeline | Ongoing |
| R6 | Duplicated concepts | Medium | High | Multi-corpus same idea | Grep + one-concept-one-file | 1.2 |
| R7 | Stale sources policy | Medium | High | sources.md lists 2 corpora | Update research tier registry | 1.2 |
| R8 | Extraction plan drift | Medium | Medium | No per-file status | extraction_status field | 1.3 |
| R9 | Git history without baseline tag | Low | Done | Incremental commits | Tag baseline post-audit | 1.2 |
| R10 | Large upstream clones in repo | Medium | Done | Shallow clones committed | Document clone policy; optional gitignore | 1.3 |
| R11 | Harness QA incomplete | Medium | Medium | PDF conversion untested tables | Manual QA before extraction | 1.3 |
| R12 | Digital twin overclaim | Medium | Medium | 06 section thin | Mark speculative; defer replay | 1.4 |
| R13 | Self-improving agents ungoverned | High | Low | Curator/MA-E promotion | Curator invariants first | 1.3 |
| R14 | MCP overexpansion | Medium | Low | GUI-MCP + Hermes OAuth | Finish ch15–16 first | 1.3 |
| R15 | RAG before graph discipline | Medium | Medium | Premature embeddings | Defer RAG | 2.x |
| R16 | Governance doc sprawl | Low | Medium | Root + governance split | Single index | 1.2 |
| R17 | Architecture inflation narrative | Medium | Medium | «Cognitive platform» language | Engineering tone in reviews | Ongoing |
| R18 | Weak antipattern coverage | Medium | High | 5 files only | Phase 1.2 antipattern batch | 1.2 |
| R19 | Idempotency unspecified | Medium | Medium | Brain OS NFR only | Pattern note if promoted | 1.3 |
| R20 | Obsidian broken graph | Low | Medium | Partial wikilinks | Link pass after promotions | 1.3 |

---

## Top 5 Risks (by severity × likelihood)

1. **R1** Taxonomy explosion  
2. **R2** Canonical drift from Brain OS  
3. **R5** Research → curated leakage  
4. **R6** Duplicated concepts  
5. **R7** Stale sources policy  

---

## Risk Acceptance

| Risk | Accept temporarily? | Until |
|------|---------------------|-------|
| Partial Claude extraction | Yes | Wave 1 complete |
| No GUI section | Yes | ≥5 GUI notes promoted |
| Thin digital twins | Yes | Replay model drafted |
| Brain OS not in sources.md | **No** | Phase 1.2 doc update |

---

## Up

- [ARCHITECTURE_HEALTH_REPORT.md](ARCHITECTURE_HEALTH_REPORT.md)
- [GOVERNANCE_GAPS.md](GOVERNANCE_GAPS.md)
