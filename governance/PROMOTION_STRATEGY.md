# Promotion Strategy

**Дата:** 2026-05-25  
**Status:** Governance policy — **no auto-promotion**

---

## Safe Promotion Pipeline

```mermaid
flowchart LR
    R[Research sandbox / Books research] --> E[Extraction draft]
    E --> S[Scoring: Value Maturity Fit Risk]
    S --> PR[PROMOTION_REVIEW / corpus review]
    PR --> GR[Governance review]
    GR --> PC[Canonical candidate]
    PC --> INT[Curated integration agent-os/]
    INT --> VAL[Validation: dedup links provenance]
```

### Stage definitions

| Stage | Location | Output |
|-------|----------|--------|
| Research | `experiments/`, `Books/brain-os/` | Review MD, patterns |
| Extraction | Draft using template | Proposed note path |
| Review | `PROMOTION_REVIEW.md`, `Books/brain-os/review/` | Scored decision |
| Governance | `governance/` audit | Approve batch |
| Canonical candidate | Checklist pass | Ready file list |
| Curated integration | `agent-os/00–09/` | Atomic note + index |

**Hard rule:** No stage skipping. No direct experiment → agent-os copy.

---

## Decision Matrix (from Phase 1.1)

| Decision | Rule |
|----------|------|
| **PROMOTE_NOW** | Value ≥4, Fit ≥4, Risk ≤2 |
| **PROMOTE_LATER** | Value ≥4, Maturity <4 or Risk ≥3 |
| **RESEARCH_ONLY** | Interesting, immature |
| **REJECT** | Chaos, duplication, branding |

---

## Promotion Criteria by Artifact Type

### Patterns (`08_patterns/`)

- [ ] Fixable failure mode documented
- [ ] Not duplicate of existing pattern
- [ ] Production Implications section
- [ ] Source: Claude preferred; Hermes/Mobile second with provenance
- [ ] Paired antipattern or risk note

### Anti-patterns (`09_antipatterns/`)

- [ ] Named failure, not vendor rant
- [ ] Fix pattern linked in Related Concepts
- [ ] Evidence from production or strong research sandbox
- [ ] Max 1 file per failure mode

### Contracts

- **Default:** stay in `Books/*/contracts/` or `10_research/` — **not** `00–06`
- Curated layer = concepts, not OpenAPI
- Exception: reference envelope in `10_research/` with `research-only` tag

### Glossary (`11_glossary/`)

- [ ] Pointer only — no second definition
- [ ] Links to canonical concept in 00–06

### Architecture concepts (`00–06/`)

- [ ] One concept per file
- [ ] Clear boundary vs adjacent section
- [ ] No plane branding (CAIM/VGP2) as concept names

### Diagrams (`12_diagrams/`)

- [ ] After concept promoted
- [ ] Mermaid + Related Concepts
- [ ] No diagram without canonical nodes

### Digital twin concepts (`06_digital-twins/`)

- [ ] No replay claims without replay model
- [ ] Profile isolation OK with Hermes provenance
- [ ] Curator only with never-auto-delete governance

### GUI concepts

- [ ] First wave in `01_agent-runtime/` + `00_foundations/`
- [ ] Antipattern for each failure mode promoted
- [ ] No `13_gui-agents/` until taxonomy threshold met

---

## Source Priority (when concepts conflict)

1. `Books/claude/` — **wins** on harness/runtime conflicts
2. `Books/agents/` — survey framing, multi-agent scaling
3. `experiments/hermes-agent-review/` — memory, orchestration, twins
4. `experiments/mobile-agent-review/` — GUI modality
5. `Books/brain-os/` — control-plane **ideas** only, strip branding

---

## Batch Plan (from PROMOTION_REVIEW)

### Batch 1 — Phase 1.2 PROMOTE_NOW (22 items)

Hermes memory/orchestration (9) + Mobile GUI (6) + antipatterns (7) — see PROMOTION_REVIEW §9.

### Batch 2 — Phase 1.3 PROMOTE_LATER (24 items)

Curator, Kanban detail, Harness extraction, Brain OS trace-first/routing stripped.

### Frozen (no promotion)

- Brain OS plane entities as canonical
- Hermes gateway, provider matrix
- MobileAgent runtime scripts, weights
- adaptation without governance

---

## Post-Promotion Validation

1. Grep agent-os for duplicate headings
2. Update section `index.md`
3. Bidirectional wikilinks
4. Add to governance promotion log (table below)
5. Do **not** update `Books/` or `experiments/`

### Promotion log (template)

See [PROMOTION_LOG.md](PROMOTION_LOG.md) for Phase 1.2 entries.

| Date | File | Source | Decision | Reviewer |
|------|------|--------|----------|----------|
| 2026-05-25 | Phase 1.2 batch (22 notes) | Hermes + MobileAgent + Brain OS (stripped) | PROMOTE_NOW | governance/ |

---

## Up

- [PROMOTION_REVIEW.md](../PROMOTION_REVIEW.md)
- [CANONICAL_DIRECTION.md](CANONICAL_DIRECTION.md)
- [NEXT_PHASE_ROADMAP.md](NEXT_PHASE_ROADMAP.md)
