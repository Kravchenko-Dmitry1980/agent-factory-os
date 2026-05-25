# Kanban — Durable Multi-Agent Queue

**Code:** `hermes_cli/kanban_db.py`, `hermes_cli/kanban.py`, `tools/kanban_tools.py`  
**DB:** `~/.hermes/kanban.db`  
**Docs:** `website/docs/user-guide/features/kanban.md`

---

## Core Distinction

Kanban is **not** subagent delegation. It is a durable work queue where:
- Every handoff is a SQLite row
- Every worker is a named profile with persistent memory
- Humans can comment/unblock at any point
- Work survives restarts

---

## Task States

```
triage → todo → ready → running → done → archived
                    ↓
                 blocked → (unblock) → ready
```

---

## Kanban Tools (Agent-Facing)

| Tool | Purpose |
|------|---------|
| `kanban_show` | View task details + comments |
| `kanban_list` | List tasks by status/assignee |
| `kanban_create` | Create new task |
| `kanban_complete` | Mark task done |
| `kanban_block` | Block with reason |
| `kanban_unblock` | Unblock task |
| `kanban_comment` | Add to comment thread |
| `kanban_heartbeat` | Signal worker alive |
| `kanban_link` | Create dependency |
| `kanban_unblock` | Remove block |

Agents use tools, not CLI. CLI is for humans/scripts.

---

## Workspace Types

| Type | Persistence | Use Case |
|------|-------------|----------|
| `scratch` | Deleted on complete | Ephemeral exploration |
| `dir:/absolute/path` | Preserved | Shared directories |
| `worktree:` | Preserved | Git worktrees for coding |

---

## Dispatcher

Long-lived loop (default 60s interval):
1. Reclaim stale/crashed claims
2. Promote tasks when dependencies done
3. Atomically claim ready tasks
4. Spawn assigned profile processes

Runs inside gateway by default.

**Failure limit:** After 2 consecutive spawn failures, task auto-blocked.

---

## Multi-Board Support

```
~/.hermes/kanban.db              # default board
~/.hermes/kanban/boards/<slug>/  # additional boards
```

Workers pinned to board via `HERMES_KANBAN_BOARD` env.

---

## Swarm Topology

```
Orchestrator → decompose → create tasks
Workers (parallel) → complete → comment
Verifier → review outputs
Synthesizer → aggregate results
```

See `multi-agent/TASK_ORCHESTRATION.md` for decision guide.

---

## Digital Twin Use Case

Kanban enables persistent named assistants:

```bash
hermes profile create inbox-triage --description "Email triage"
hermes kanban create "Process inbox" --assignee inbox-triage
```

Twin accumulates memory across tasks, not just sessions.

---

## Agent-OS Relevance

New primitive for `04_multi-agent/` — distinct from subagents documented in Claude Code corpus.
