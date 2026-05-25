# Semantic Linking Rules

**Phase:** 1.3  
**Scope:** Curated notes in `agent-os/00–09/`, graph layer, glossary pointers

---

## What Deserves a Semantic Link

Link when the relationship is **architecture-relevant**:

| Relationship | Example |
|--------------|---------|
| Fix ↔ failure | `[[visual-verification]]` ↔ `[[unverified-gui-clicks]]` |
| Pattern ↔ enabling concept | `[[frozen-memory-snapshot]]` ↔ `[[prompt-cache-as-constraint]]` |
| Primitive choice | `[[kanban-vs-delegate]]` ↔ `[[durable-task-coordination]]` |
| Modality parallel | `[[query-loop]]` ↔ `[[gui-agent-loop]]` |
| Governance lineage | promoted note → `PROMOTION_REVIEW.md` path in Upstream Sources |
| Cluster membership | Semantic Cluster field on promoted notes |

**Target:** 3–8 intentional wikilinks per note in Related sections — not body spam.

---

## What Should NOT Be Linked

- Research-only Brain OS plane entities as canonical peers
- Upstream product features (Hermes gateway, MobileAgent ADB scripts)
- Every note in the same folder (taxonomy ≠ cluster)
- Glossary duplicates (glossary points to one canonical note)
- Circular pairs without semantic difference (A↔B only when both directions add meaning)
- Non-existent `[[wikilinks]]` to concepts without curated notes (use plain path for research)

---

## Canonical Linking Rules

1. **One definition per concept** — canonical note in `00–06` or `08/09`; glossary pointer only.
2. **Wikilink format:** `[[kebab-case-note-name]]` matching filename without `.md`.
3. **Required sections** on Phase 1.2+ promoted notes:
   - Related Concepts
   - Related Anti-patterns
   - Related Patterns
   - Upstream Sources
   - Governance References
   - Semantic Cluster
4. **Bidirectional discipline:** if A lists B in Related Concepts, B should list A (when semantically true).
5. **Sources vs Upstream:** Upstream = lineage paths; keep `## Sources` for backward compatibility or merge into Upstream Sources.

---

## Anti-Pattern Adjacency Rules

Every promoted anti-pattern MUST link to:

- ≥1 fix pattern or enabling concept
- ≥1 cluster sibling anti-pattern OR parent failure catalog
- Semantic Cluster assignment

Every fix pattern in verification/memory/orchestration/GUI SHOULD link to ≥1 anti-pattern it mitigates.

---

## Provenance Rules

- Curated note from sandbox → Upstream Sources includes `experiments/...` path
- Curated note from Claude → `Books/claude/chXX-*.md`
- Brain OS ideas → `Books/brain-os/...` + mark stripped in Governance References
- Never mark research sandbox as canonical in Upstream Sources

---

## Glossary Linking Rules

- Glossary entry = 1–3 sentences + link to canonical note
- `(research-only)` suffix for non-curated concepts
- No second definition in glossary

---

## Cross-Cluster Linking Rules

- Max 2 cross-cluster links in Related Concepts unless node is explicit bridge (e.g. `fail-closed-agent-loop`)
- Cross-cluster links must state relationship in concept map, not only wikilink
- GUI cluster links to verification cluster; does not link to MCP or digital-twin unless action surface requires it

---

## GUI Linking Constraints

- No links to runtime drivers, ADB, Playwright implementation notes
- Always pair GUI loop concepts with verification + anti-pattern neighbors
- Do not create `13_gui-agents/` via links — stay in `01_agent-runtime/` + `00_foundations/`

---

## Brain OS Stripping Rules

When linking Brain OS research:

- Strip plane branding (CAIM, VGP2, control-plane product names) from curated text
- Link pattern idea only after governance promotion
- `trace-first-architecture`, `human-escalation-gate` — cluster adjacency as **research**, not `[[wikilink]]` until curated
- `evaluation-before-writeback` promoted as `[[verification-before-writeback]]` — do not duplicate Brain OS node

---

## Up

- [concept-clusters.md](concept-clusters.md)
- [governance/SEMANTIC_LINKING_AUDIT.md](../../governance/SEMANTIC_LINKING_AUDIT.md)
