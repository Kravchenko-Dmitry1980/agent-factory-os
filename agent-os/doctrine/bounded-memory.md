# Bounded Memory Doctrine

Memory is a **governed resource**, not infinite context.

---

## Core Thesis

Agents do not have unbounded reliable recall. Production systems bound memory by **type, size, scope, injection timing, and write gates**. Fantasies of infinite context or auto-growing memory produce cost explosions, stale parallel state, and cache invalidation bugs.

---

## Consolidated Memory Discipline

### Frozen snapshots

[[frozen-memory-snapshot]] — inject curated memory **once** at session start; no mid-session system prompt mutation.

Writes persist immediately; reasoning context refreshes next session or via explicit recall tools.

### Character limits

[[memory-char-limits]] — hard caps on curated stores; predictable cost and consolidation pressure.

### Provider boundaries

[[memory-provider-boundaries]] — which backends active; who owns write/recall paths.

### Profile isolation

[[profile-isolation]] — separate stores/skills/history per agent instance/role; prevents cross-contamination.

### Memory-aware execution

[[memory-aware-execution]] — route work by memory **need**, not always-on injection.

### Taxonomy discipline

[[memory-taxonomy]] — exactly four types: user, feedback, project, reference. No ad hoc category inflation in doctrine.

### Prompt cache constraint

[[prompt-cache-as-constraint]] — memory sections belong in static prefix boundary when injected at bootstrap.

### Verification before writeback

[[verification-before-writeback]] — durable memory writes require verify pass; pairs with bounded stores.

---

## Memory Anti-patterns (Curated)

| Anti-pattern | Failure |
|--------------|---------|
| [[unbounded-memory-growth]] | Noise, cost, retrieval degradation |
| [[mid-session-memory-injection]] | Cache bust, inconsistent behavior |
| [[memory-as-crutch]] | Stale duplicate of live codebase |
| [[cache-busting-sections]] | Prefix instability |

Operational inverse: CLAUDE.md / session file treated as memory plane — **reject** as governance pattern.

---

## Explicitly Rejected

### Infinite context fantasy

No doctrine principle assumes full-repo or unbounded history in prompt. Compaction and recall are explicit ([[memory-compaction]], [[memory-recall]]).

### Uncontrolled memory writeback

Raw chat dumps, unverified agent output, failed-attempt residue → durable store. Blocked by verification-before-writeback.

### Auto-memory inflation

Systems that grow memory automatically without char limits, consolidation policy, and write gates. Maps to [[unbounded-memory-growth]] and [[recursive-self-improvement]] adjacency.

---

## Operational Implications

- Operators must understand snapshot semantics: “saved” ≠ “in current reasoning prefix.”
- Subagents should not writeback to shared stores ([[subagent-tool-restrictions]]).
- Digital twin “evolving memory” remains **curator-governed** — no replay model = no production twin claim ([[persistent-identity]] scope).

---

## Sources

- `agent-os/02_memory/` curated notes
- `agent-os/graph/cluster-indexes/memory-governance-cluster.md`
- `agent-os/09_antipatterns/` memory family
- `governance/CONSOLIDATION_CANDIDATES.md`

See also: [diagrams/bounded-memory.md](diagrams/bounded-memory.md)
