# Future RAG Readiness

What Phase 1.3 prepares for deferred infrastructure — and what must **not** be built yet.

---

## Already Ready (no new infrastructure)

| Capability | Evidence in repo |
|------------|------------------|
| Atomic notes | One concept per file, kebab-case |
| Stable taxonomy | Sections `00–12`, no explosion |
| Wikilinks | Obsidian-compatible `[[concept]]` |
| Provenance tables | `graph/provenance-graph.md`, `PROMOTION_LOG.md` |
| Semantic clusters | `graph/concept-clusters.md` + indexes |
| Layer separation | `canonical-vs-research-map.md` |
| Maturity metadata | Promotion Metadata YAML on Phase 1.2 notes |
| Anti-pattern ↔ pattern edges | Standardized Related sections |
| Governance audit trail | PROMOTION_REVIEW → PROMOTION_LOG |

**Implication:** Future RAG can chunk by note + cluster tag + provenance frontmatter without graph DB.

---

## Ready After Phase 1.3 (link discipline)

- Orphan-free promoted note set
- Cluster-index navigation for retrieval scoping
- Glossary as disambiguation layer (pointers only)
- Concept maps for adjacency-aware context expansion

---

## NOT Ready — Do Not Implement Yet

| Capability | Why defer |
|------------|-----------|
| Embeddings / vector DB | Duplicate nodes if dedup incomplete |
| Auto-chunking all corpora | Research + canonical would pollute index |
| Ontology engine (OWL/RDF) | Branding nodes risk from Brain OS |
| MCP memory tool runtime | No harness spec for agent consumption |
| Link validation automation | Manual audit first; script after stable registry |
| Semantic equivalence (Claude ↔ Hermes ↔ MobileAgent) | Needs canonical node registry |
| RAG over `Books/brain-os/` whole corpus | Author draft, immature |

---

## Recommended Future Sequence

1. **Link validator** — grep broken `[[wikilinks]]` against file registry
2. **Canonical node registry** — YAML list of curated note IDs + cluster tags
3. **Chunk policy** — curated only first; research chunks tagged non-canonical
4. **Embeddings** — after registry + validator green
5. **Agent MCP read API** — after chunk policy proven

---

## Chunk Metadata Template (future, optional)

```yaml
cluster: memory-governance
canonical: true
source_tier: research
promotion_decision: PROMOTE_NOW
upstream:
  - experiments/hermes-agent-review/memory/MEMORY.md
```

Do not auto-generate until promotion discipline holds for Phase 1.3+ notes.

---

## Up

- [governance/KNOWLEDGE_GRAPH_DIRECTION.md](../../governance/KNOWLEDGE_GRAPH_DIRECTION.md)
- [semantic-linking-rules.md](semantic-linking-rules.md)
