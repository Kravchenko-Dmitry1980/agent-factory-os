# Semantic Traversal Guide

How to navigate Agent-OS as a connected knowledge system — not a folder tree.

---

## Traversal modes

### 1. Taxonomy traversal (structural)

Follow section indexes: `00_foundations` → `01_agent-runtime` → …

Use when: learning harness baseline (Claude-derived spine).

### 2. Cluster traversal (semantic)

Start at [cluster-navigation.md](cluster-navigation.md) → cluster index → concept map → atomic note.

Use when: solving architecture problem (memory, verify, orchestrate, GUI).

### 3. Provenance traversal (audit)

Start at [provenance-graph.md](../provenance-graph.md) → Upstream Sources on note → sandbox.

Use when: validating promotion lineage or research vs canonical.

### 4. Failure-first traversal

Start at `09_antipatterns/` index → Related Patterns → fix concept.

Use when: incident postmortem or design review.

---

## Recommended paths

**New GUI harness designer:**  
[[gui-agent-loop]] → [[visual-grounding]] → [[visual-verification]] → [[unverified-gui-clicks]]

**Memory system designer:**  
[[memory-taxonomy]] → [[frozen-memory-snapshot]] → [[memory-provider-boundaries]] → [[mid-session-memory-injection]]

**Multi-agent operator:**  
[[subagents]] → [[subagent-tool-restrictions]] → [[kanban-vs-delegate]] → [[durable-task-coordination]]

---

## Stop rules (avoid graph noise)

- Do not traverse into `experiments/*/source/` from curated wikilinks
- Do not treat `Books/brain-os/` as canonical without PROMOTE entry
- Max depth 3 hops from cluster index before returning to map

---

## Up

- [cluster-navigation.md](cluster-navigation.md)
- [semantic-linking-rules.md](../semantic-linking-rules.md)
