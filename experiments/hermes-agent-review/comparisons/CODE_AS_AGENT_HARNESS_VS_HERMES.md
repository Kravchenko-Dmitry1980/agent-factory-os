# Code-as-Agent-Harness vs Hermes Agent

**Survey:** arXiv 2605.18747 "Code as Agent Harness"  
**Location:** `Books/agents/`  
**Comparison date:** 2026-05-25

---

## Survey Framework

The survey organizes harness interface around three roles of code:

1. **Code for reasoning** — externalize logic into verifiable computation
2. **Code for acting** — translate intent into executable operations
3. **Code for environment modeling** — represent world state through program states

---

## Mapping Hermes to Survey Framework

### Code for Reasoning

| Survey Concept | Hermes Implementation |
|----------------|----------------------|
| External interpreters | `execute_code` RPC tool |
| Symbolic solvers | Not built-in (via MCP) |
| Execution traces | Session DB message history |
| Process rewards | Curator skill evaluation |
| Verifiable outcomes | Tool result validation |

**Hermes strength:** `execute_code` collapses multi-step reasoning into single turn with zero context cost for intermediates.

**Gap:** No built-in symbolic reasoning; relies on LLM + tools.

---

### Code for Acting

| Survey Concept | Hermes Implementation |
|----------------|----------------------|
| Tool definitions | 70+ tools, 28 toolsets |
| API schemas | Tool registry with JSON schemas |
| Terminal execution | 7 sandbox backends |
| Browser automation | 5 browser backends |
| MCP tool use | Dynamic MCP client |

**Hermes strength:** Rich tool ecosystem; pluggable execution backends.

**Alignment:** Tools are code-defined schemas — direct match to survey's "code for acting."

---

### Code for Environment Modeling

| Survey Concept | Hermes Implementation |
|----------------|----------------------|
| Program states | Session DB (SQLite) |
| Repositories | File tools + git worktrees |
| Simulators | Sandbox backends |
| Tests | Not built-in (via terminal) |
| Logs/traces | Session message history |
| Configuration files | config.yaml, SOUL.md, skills |

**Hermes strength:** Multi-layer state (session, memory, skills, kanban).

**Gap:** No formal environment simulator; relies on real execution.

---

## Multi-Agent Orchestration (Survey Ch.4)

| Survey Concept | Hermes |
|----------------|--------|
| Hierarchical delegation | delegate_task |
| Peer coordination | Kanban |
| Swarm patterns | Kanban swarm topology |
| Synchronization | Kanban dispatcher + atomic claim |
| Task decomposition | kanban_decompose |

**Hermes contribution:** Explicit distinction between RPC delegation and durable work queue — not covered in survey.

---

## Memory & Planning (Survey Ch.3)

| Survey Mechanism | Hermes |
|------------------|--------|
| Planning | Skills (plan skill), subagent goals |
| Memory taxonomy | MEMORY/USER + providers + skills |
| Context management | Compression + on_pre_compress |
| Persistent state | SQLite + profiles |

**Hermes addition:** Self-improving skills (curator) as procedural memory evolution.

---

## Emerging Fields (Survey Ch.5)

| Open Problem | Hermes Approach |
|--------------|-----------------|
| Long-horizon tasks | Kanban durable queue |
| Multi-agent alignment | Honcho dialectic modeling |
| Skill acquisition | Agent-created skills + curator |
| Evaluation | Batch trajectory generation |

---

## Key Insight

Hermes is a **concrete instantiation** of the survey's harness interface:

- Code for acting → tool registry + MCP
- Code for environment modeling → session DB + memory files + kanban
- Code for reasoning → execute_code + subagent delegation

The survey is theoretical; Hermes is production implementation with trade-offs visible.

---

## Patterns to Extract for Agent-OS

1. **execute_code RPC** — reasoning compression pattern
2. **Dual multi-agent primitives** — extends survey's orchestration chapter
3. **Curator** — procedural memory evolution (not in survey)
4. **Profile isolation** — environment modeling per agent instance
5. **Frozen memory snapshot** — bounded state representation

---

## Gaps Hermes Doesn't Address (Survey Open Problems)

- Formal verification of reasoning steps
- Symbolic computation integration
- Standardized evaluation benchmarks
- Theoretical guarantees on memory consistency

These remain research directions, not production features.
