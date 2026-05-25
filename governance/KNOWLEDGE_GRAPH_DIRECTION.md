# Knowledge Graph Direction

**Дата:** 2026-05-25  
**Scope:** From hierarchical markdown today → semantic graph tomorrow

---

## Current State

| Capability | Exists | Quality |
|------------|--------|---------|
| Hierarchical folders (00–12) | ✅ | Strong |
| Atomic notes (one concept/file) | ✅ | Strong |
| Wikilinks `[[concept]]` | ✅ Partial | Not validated |
| Section indexes | ✅ | Good |
| Provenance in `## Sources` | ✅ Partial | Inconsistent across notes |
| Cross-corpus links | ❌ | Books ↔ agent-os manual |
| Promotion graph | ❌ | PROMOTION_REVIEW text only |
| Maturity metadata | ❌ | brain-os only |
| Ontology layer | ❌ | Implicit in folder numbers |

**Assessment:** **Hierarchical markdown storage with latent graph** — not yet a knowledge graph system.

---

## Target State (phased)

### Phase A — Link discipline (safe, now)

- Bidirectional Related Concepts
- Glossary = pointers only
- Promotion candidates linked to target paths
- `governance/` as meta-layer index

### Phase B — Provenance graph (safe, next)

Optional frontmatter:

```yaml
maturity: production-relevant | reusable-pattern | research-only
sources:
  - path: Books/claude/ch05-agent-loop.md
    status: canonical
promotion:
  decision: PROMOTE_LATER
  review: PROMOTION_REVIEW.md
```

### Phase C — Pattern / anti-pattern graph

- Every antipattern → fix pattern edge
- Cluster tags: memory, multi-agent, gui, mcp, twin

### Phase D — Semantic graph (defer)

- OWL/RDF or lightweight YAML ontology
- Embeddings + RAG chunk graph
- Cross-source concept equivalence (Claude ↔ Harness ↔ Hermes)

**Danger if too early:** ontology explosion, duplicate nodes, branding nodes (CAIM, VGP2) as first-class entities.

---

## Graph Types Needed

| Graph | Purpose | Priority |
|-------|---------|----------|
| Navigation graph | Human/Obsidian | Now |
| Provenance graph | Audit trail | Next |
| Promotion graph | Governance | Next |
| Pattern graph | Engineering reuse | Phase 1.2+ |
| Anti-pattern graph | Failure prevention | Phase 1.2+ |
| Semantic equivalence | Multi-corpus | Defer |
| RAG chunk graph | Retrieval | Defer until provenance stable |

---

## What Already Exists (use, don't rebuild)

- `agent-os/templates/concept-note-template.md`
- `10_research/extraction-plan.md` chapter matrix
- `PROMOTION_REVIEW.md` scored edges
- `Books/brain-os/index.md` full navigation
- Experiments `integration-candidates.md` / comparisons

---

## What Is Missing

1. Link validation script (broken wikilinks)
2. Canonical node registry (single source of truth per concept)
3. Corpus → concept mapping table (maintained)
4. Graph export for Obsidian (optional)
5. MCP-memory tool schema for future agent consumption

---

## Dangerous Early Implementations

| Action | Risk |
|--------|------|
| Auto-generate ontology from all corpora | Branding + duplicate clusters |
| Embed all markdown before dedup | RAG pollution |
| Merge Brain OS planes into graph as peers of Claude concepts | Canonical drift |
| Graph DB before promotion discipline | Frozen wrong abstractions |

---

## Recommended Next Graph Step

**Phase 1.3 (complete):** Semantic graph documentation layer — `agent-os/graph/`, standardized linking on promoted notes, glossary pointers, governance audits.

**Phase 1.4 (defer):** Link validation script, canonical node registry YAML, optional frontmatter on all notes.

---

## Diagram

See [diagrams/knowledge-graph-direction.md](diagrams/knowledge-graph-direction.md)

---

## Up

- [CANONICAL_DIRECTION.md](CANONICAL_DIRECTION.md)
- [GOVERNANCE_GAPS.md](GOVERNANCE_GAPS.md)
