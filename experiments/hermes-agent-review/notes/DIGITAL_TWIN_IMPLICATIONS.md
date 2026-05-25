# Digital Twin Implications

How Hermes architecture informs digital twin design in Agent-OS.

---

## Digital Twin Definition (Agent-OS Context)

Persistent agent instance with:
- Stable identity across sessions
- Accumulating user model
- Evolving procedural knowledge
- Task-oriented coordination

---

## Hermes Digital Twin Stack

```
┌─────────────────────────────────────────────────────────┐
│                    Digital Twin Instance                 │
│                    (Profile: "researcher")               │
│                                                          │
│  Identity Layer                                          │
│  ├── SOUL.md (personality)                              │
│  └── Profile command alias                              │
│                                                          │
│  User Model Layer                                        │
│  ├── USER.md (bounded, 1375 chars)                      │
│  └── Honcho peer card (dialectic, deep)                 │
│                                                          │
│  Episodic Memory Layer                                   │
│  ├── Session DB (SQLite + FTS5)                         │
│  └── Session search (cross-session recall)              │
│                                                          │
│  Procedural Memory Layer                                 │
│  ├── Skills (agent-created + bundled)                   │
│  └── Curator (lifecycle maintenance)                    │
│                                                          │
│  Task Layer                                              │
│  ├── Kanban assignments (durable)                       │
│  └── Comment protocol (coordination)                    │
│                                                          │
│  Environment Layer                                       │
│  ├── Workspace (dir:/path, worktree:, scratch)          │
│  └── Sandbox backend (7 options)                        │
└─────────────────────────────────────────────────────────┘
```

---

## Key Implications

### 1. Profile = Twin Instance

Not subagent (ephemeral), not default agent (generic).

```bash
hermes profile create inbox-triage --description "Email triage assistant"
```

Each profile accumulates its own memory, skills, task history.

### 2. Bounded User Model Forces Curation

USER.md at 1375 chars means twin knows **essential** user facts, not everything.

Forces quality over quantity in user modeling.

### 3. Skills as Evolving Competency

Curator maintains agent-created skills:
- Stale skills archived
- Valuable skills pinned
- Overlapping skills consolidated

Twin's capabilities evolve without manual skill authoring.

### 4. Kanban as Twin Coordination

Twins don't just chat — they work:
- Assigned tasks on shared board
- Comment threads for handoffs
- Human unblock for oversight
- Audit trail forever

### 5. Honcho for Deep User Modeling

Beyond USER.md:
- Dialectic reasoning about user
- Session-scoped context
- Persistent conclusions
- Multi-profile shared workspace

---

## Twin Fleet Patterns (from Kanban)

| Pattern | Twins | Use Case |
|---------|-------|----------|
| Solo | 1 profile | Personal assistant |
| Pipeline | researcher → coder → reviewer | Engineering workflow |
| Fleet | 1 specialist × N subjects | Social accounts, services |
| Swarm | orchestrator + workers + verifier | Complex projects |

---

## Agent-OS Enrichment Targets

| Current Agent-OS Doc | Hermes Enrichment |
|---------------------|-------------------|
| `persistent-identity.md` | Profile isolation model |
| `evolving-memory.md` | Curator + Honcho patterns |
| `skill-graphs.md` | Progressive disclosure + lifecycle |

---

## Twin Design Principles (Extracted)

1. **Isolation by default** — profile boundaries prevent cross-contamination
2. **Bounded memory** — force curation, prevent noise
3. **Evolving skills** — procedural memory improves autonomously
4. **Durable tasks** — Kanban survives restarts
5. **Human oversight** — comment/unblock protocol
6. **Named identity** — profile name + description for routing

---

## What Hermes Doesn't Provide

- Formal twin lifecycle (birth/death/split/merge)
- Twin-to-twin direct communication (only via Kanban)
- Shared memory between profiles (by design — isolation)
- Twin replication/forking (manual --clone-all)

These remain design opportunities for Agent-OS.
