# Multi-Agent Overview

**Primitives:** `delegate_task` (RPC) + Kanban (durable queue)  
**Code:** `tools/delegate_tool.py`, `hermes_cli/kanban*.py`, `tools/kanban_tools.py`

---

## Two Multi-Agent Models

Hermes has **two distinct multi-agent primitives** — not interchangeable:

| | `delegate_task` | Kanban |
|---|---|---|
| **Shape** | RPC (fork → join) | Durable message queue |
| **Parent** | Blocks until child returns | Fire-and-forget after create |
| **Child identity** | Anonymous subagent | Named profile with memory |
| **Resumability** | None — failed = failed | Block → unblock → re-run |
| **Human in loop** | Not supported | Comment/unblock anytime |
| **Agents per task** | One call = one subagent | N agents over task lifetime |
| **Audit trail** | Lost on compression | Durable SQLite rows |
| **Coordination** | Hierarchical | Peer (any profile reads/writes) |

**One sentence:** `delegate_task` is a function call; Kanban is a work queue.

---

## Subagent Delegation (`delegate_task`)

### Architecture

```
Parent AIAgent
  → delegate_task(goal, context, toolsets)
    → spawn child AIAgent
      ├── Fresh conversation (zero parent history)
      ├── Restricted toolset
      ├── Own terminal session
      └── Blocked: delegate, memory write, clarify, send_message
    → child runs until completion
    → return summary ONLY to parent
    → on_delegation() memory hook
```

### Single Task

```python
delegate_task(
    goal="Debug why tests fail",
    context="Error: assertion in test_foo.py line 42",
    toolsets=["terminal", "file"]
)
```

### Parallel Batch

```python
delegate_task(tasks=[
    {"goal": "Research A", "toolsets": ["web"]},
    {"goal": "Research B", "toolsets": ["web"]},
    {"goal": "Fix build", "toolsets": ["terminal", "file"]}
])
```

- Default max concurrency: 3 (configurable)
- ThreadPoolExecutor
- Results sorted by task index
- Interrupt propagation to all children

### Model Override

```yaml
delegation:
  model: "google/gemini-flash-2.0"
  provider: "openrouter"
```

Subagents can use cheaper/faster model than parent.

### Critical Rule

Subagents know **nothing** except `goal` + `context`. Parent must pass everything needed.

---

## Kanban Multi-Agent

### Architecture

```
┌─────────────────────────────────────────────────────────┐
│ Kanban Board (~/.hermes/kanban.db)                      │
│                                                          │
│  Task → Assignee (profile) → Status → Comments          │
│                                                          │
│  Dispatcher (every 60s)                                   │
│    → reclaim stale/crashed                              │
│    → promote ready tasks                                │
│    → spawn profile process                              │
│      → HERMES_KANBAN_BOARD env pinned                   │
│      → kanban_* tools enabled                           │
└─────────────────────────────────────────────────────────┘
```

### Task Lifecycle

```
triage → todo → ready → running → done
                    ↓
                 blocked → (unblock) → ready
```

### Core Concepts

| Concept | Description |
|---------|-------------|
| **Board** | Standalone queue with own SQLite DB |
| **Task** | Row with title, body, assignee, status |
| **Link** | Parent → child dependency |
| **Comment** | Inter-agent protocol (full thread on spawn) |
| **Workspace** | scratch (ephemeral) / dir:/path / worktree: |
| **Profile** | Named agent instance with persistent memory |
| **Tenant** | Soft namespace within board |

### Kanban Swarm Topology

```
Orchestrator profile
  → decompose task
  → create kanban tasks
  → assign to worker profiles
Workers (parallel)
  → complete tasks
  → comment findings
Verifier profile
  → review outputs
Synthesizer profile
  → aggregate results
```

### Use Cases Kanban Covers (delegate can't)

- Research triage with human-in-loop
- Scheduled ops building journal over weeks
- Digital twins (persistent named assistants)
- Engineering pipelines (decompose → implement → review → PR)
- Fleet work (one specialist, N subjects)

---

## Mixture of Agents

**Code:** `tools/mixture_of_agents_tool.py`

Parallel multi-LLM calls + aggregator (OpenRouter):
- Different models answer same question
- Aggregator synthesizes best answer
- Not subagents — parallel inference, not delegation

---

## Background Review Agents

**Code:** `agent/background_review.py`, `agent/curator.py`

Forked auxiliary agents for:
- Skill maintenance (curator)
- Post-turn review
- Not user-facing delegation

---

## When to Use What

| Scenario | Use |
|----------|-----|
| Parent needs answer before continuing | `delegate_task` |
| Parallel research, no human needed | `delegate_task` (batch) |
| Work crosses agent boundaries | Kanban |
| Needs to survive restarts | Kanban |
| Human input mid-task | Kanban |
| Different role picks up later | Kanban |
| Digital twin accumulation | Kanban + Profiles |
| Short reasoning subtask | `delegate_task` |

**Coexistence:** Kanban worker may call `delegate_task` internally.

---

## Agent-OS Mapping

| Agent-OS | Hermes |
|----------|--------|
| `04_multi-agent/subagents.md` | delegate_task |
| `04_multi-agent/coordination.md` | Kanban comment protocol |
| `04_multi-agent/swarms.md` | Kanban swarm topology |
| `04_multi-agent/synchronization.md` | Kanban dispatcher + atomic claim |

See also: `multi-agent/SUBAGENTS.md`, `multi-agent/KANBAN.md`, `multi-agent/TASK_ORCHESTRATION.md`
