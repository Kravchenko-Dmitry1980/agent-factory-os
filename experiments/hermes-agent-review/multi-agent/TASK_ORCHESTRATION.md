# Task Orchestration

**Primitives:** delegate_task + Kanban + Cron  
**Docs:** delegation.md, kanban.md, cron docs

---

## Orchestration Spectrum

```
Ephemeral ←────────────────────────────────→ Durable

delegate_task          Cron              Kanban
(RPC, blocks)     (scheduled, fresh)   (queue, persistent)
     │                  │                    │
     └──────────────────┴────────────────────┘
              All use AIAgent.run_conversation()
```

---

## delegate_task Orchestration

**Pattern:** Parent orchestrates, subagents execute, parent synthesizes.

```
Parent receives task
  → decompose mentally
  → delegate_task(tasks=[A, B, C])  # parallel
  → receive summaries
  → synthesize final answer
  → continue or respond
```

**Constraints:**
- Max 3 concurrent (default)
- Parent must pass complete context
- Results are summaries only

---

## Kanban Orchestration

**Pattern:** Dispatcher orchestrates, profiles execute, board coordinates.

```
Orchestrator profile
  → kanban_create tasks with dependencies
  → kanban_link parent → child
  → dispatcher promotes ready → running
  → workers complete, comment
  → verifier reviews
  → synthesizer aggregates
  → human unblocks if needed
```

**Topologies:**
- Solo worker
- Parallel workers
- Role pipeline (research → implement → review)
- Fleet (one specialist, N subjects)
- Swarm (orchestrator + workers + verifier + synthesizer)

---

## Cron Orchestration

**Pattern:** Scheduler triggers, fresh agent executes, delivers result.

```
Scheduler tick
  → load job from jobs.json
  → fresh AIAgent (no history)
  → inject attached skills
  → run prompt
  → deliver to platform
  → update next_run
```

**Use cases:** Daily reports, nightly backups, weekly audits.

---

## Mixture of Agents

**Pattern:** Parallel multi-LLM inference, aggregator synthesizes.

Not orchestration in task sense — parallel reasoning, not delegation.

---

## Decision Guide

| Question | Answer → Primitive |
|----------|-------------------|
| Parent needs result before continuing? | Yes → delegate |
| Work survives agent restart? | Yes → Kanban |
| Human input mid-task? | Yes → Kanban |
| Scheduled unattended? | Yes → Cron |
| Multiple roles over task lifetime? | Yes → Kanban |
| Quick parallel research? | Yes → delegate batch |
| Persistent agent identity? | Yes → Kanban + Profile |

---

## Agent-OS Mapping

| Agent-OS | Hermes Orchestration |
|----------|---------------------|
| `00_foundations/orchestration.md` | Multi-primitive model |
| `04_multi-agent/coordination.md` | Kanban comment protocol |
| `04_multi-agent/swarms.md` | Kanban swarm topology |

See `diagrams/ARCHITECTURE_DIAGRAMS.md` for decision flowchart.
