# Governance Gaps

**Дата:** 2026-05-25  
**Purpose:** Missing standards, workflows, and metadata for a governance-first Knowledge OS

---

## Gap Register

| # | Gap | Severity | Current state | Required artifact |
|---|-----|----------|---------------|-------------------|
| G1 | **Corpora registry incomplete** | High | `sources.md` = 2 corpora | Extend policy: brain-os, experiments as research tier |
| G2 | **Promotion workflow** | High | PROMOTION_REVIEW only | `PROMOTION_STRATEGY.md` + checklist |
| G3 | **Note metadata standard** | Medium | Template lacks maturity/status | Optional YAML frontmatter |
| G4 | **Extraction sync** | Medium | Status only in extraction-plan | Per-file `extraction_status` |
| G5 | **Canonicalization workflow** | High | Informal | research → score → governance → promote |
| G6 | **Ontology rules** | Medium | Implicit folders | Written rules: concept vs pattern vs project |
| G7 | **Naming conventions** | Low | kebab-case documented | Enforce on promotion PR |
| G8 | **Anti-pattern governance** | Medium | 5 files vs plan 14+ | Pair every antipattern with fix pattern |
| G9 | **Review workflow** | Medium | Ad hoc sandboxes | Sandbox exit criteria template |
| G10 | **Graph-linking standards** | Medium | Wikilinks optional | Bidirectional + index update mandatory |
| G11 | **Citation standards** | Medium | `## Sources` freeform | Source path + section + confidence |
| G12 | **Versioning strategy** | High | No note versioning | Git + optional note `version:` field |
| G13 | **Contracts (Agent-OS)** | Medium | Concept prose only | Reference contracts in 10_research for cross-corpus |
| G14 | **Maturity policy** | Medium | brain-os only | Adopt labels repo-wide |
| G15 | **Safety escalation matrix** | Medium | Partial in Brain OS | Curated doc if promoted |
| G16 | **Benchmark strategy** | Low | Mentioned in Brain OS v0.3 | RESEARCH_ONLY until harness eval exists |
| G17 | **Governance doc location** | Low | Split root/governance | Index linking all |
| G18 | **Clone / upstream policy** | Medium | Large trees in git | Document: shallow clone, no curation of upstream |
| G19 | **Initial baseline commit** | Medium | Evolved commits | Tag `baseline-v0` after audit |
| G20 | **Link linter** | Low | None | Phase 3 tooling |

---

## Missing Contracts (cross-corpus)

| Contract | Brain OS | Agent-OS | Experiments |
|----------|----------|----------|-------------|
| OpenAPI | Claimed backlog | N/A | N/A |
| Evaluator | Missing | Partial (verification) | Mobile A/B/C informal |
| Memory writeback | Event only | Claude two-step | Hermes frozen snapshot |
| Idempotency | NFR claim | Partial | Not specified |
| Replay / twin reproducibility | Missing | Missing | Benchmark-only |

**Do not import** Brain OS JSON contracts into curated layer without normalization.

---

## Standards to Adopt (minimal)

### 1. Corpus tier standard

| Tier | Paths | Promotion |
|------|-------|-----------|
| T0 Canonical source | Books/claude, Books/agents PDF | Extract only |
| T1 Research source | Books/brain-os, experiments | Score before any promote |
| T2 Curated | agent-os/00–09 | Governance gate |
| T3 Catalog | agent-os/10_research | Links only |

### 2. Promotion gate checklist

See [PROMOTION_STRATEGY.md](PROMOTION_STRATEGY.md) — derived from PROMOTION_REVIEW §10.

### 3. Maturity labels (repo-wide)

`production-relevant` | `reusable-pattern` | `promising` | `speculative` | `weak-abstraction` | `branding-only` | `reject`

### 4. Provenance minimum

```
source_file | source_section | extraction_date | confidence | promotion_decision
```

---

## Up

- [PROMOTION_STRATEGY.md](PROMOTION_STRATEGY.md)
- [ARCHITECTURAL_DRIFT_REPORT.md](ARCHITECTURAL_DRIFT_REPORT.md)
