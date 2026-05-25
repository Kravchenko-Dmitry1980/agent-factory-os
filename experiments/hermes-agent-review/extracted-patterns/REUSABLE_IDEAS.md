# Reusable Ideas

Conceptual ideas from Hermes worth considering for agent architecture design.

---

## Closed Learning Loop

Agent that learns from its own experience:
1. Completes complex task
2. Creates skill encoding the workflow
3. Uses skill in future sessions
4. Curator maintains skill quality
5. Memory captures key facts
6. Session search enables cross-session recall

**Idea:** Agent as accumulating knowledge system, not stateless executor.

---

## Digital Twin via Profiles

Named agent instances with persistent identity:
- Own personality (SOUL.md)
- Own user model (USER.md + Honcho)
- Own procedural memory (skills)
- Own task history (Kanban assignments)

**Idea:** Multiple specialized twins on one machine, not one generic agent.

---

## Dual Multi-Agent Primitives

Not one multi-agent model — two:
- **RPC (delegate):** Parent needs answer now
- **Queue (Kanban):** Work survives restarts, crosses boundaries

**Idea:** Match primitive to coordination need, don't force one model.

---

## Self-Improving Without User Intervention

Curator runs on inactivity:
- Reviews agent-created skills
- Archives stale, pins valuable
- Never deletes (recoverable archive)

**Idea:** Procedural memory evolves autonomously with guardrails.

---

## Bounded Memory as Feature

Hard limits (2200/1375 chars) are not bugs — they force curation.

**Idea:** Unbounded memory leads to noise; limits lead to signal.

---

## Frozen Snapshot for Performance

Memory injected once at session start preserves prompt cache.

**Idea:** Separate persistence timing from injection timing.

---

## Progressive Loading for Scale

88+ skills loaded via 3-level disclosure. Agent sees list, loads on demand.

**Idea:** Skill libraries can scale if loading is tiered.

---

## Agent Context Awareness

Memory providers know if they're serving primary agent, subagent, or cron job.

**Idea:** Context-aware side effects prevent corruption.

---

## Comment Protocol for Coordination

Kanban tasks have comment threads. Workers read full thread on spawn.

**Idea:** Async multi-agent coordination via durable messages, not shared context.

---

## Gateway as First-Class Entry Point

20+ messaging platforms from single gateway process. Same agent, many interfaces.

**Idea:** Agent accessibility > agent interface.

---

## Experimental Ideas (Higher Risk)

1. **Mixture of Agents** — parallel multi-LLM with aggregator
2. **Trajectory compression** — training data from agent runs
3. **Honcho dialectic** — LLM-synthesized user modeling
4. **Cross-session mirroring** — gateway message relay between sessions
5. **Skin engine** — CLI theming as agent personality extension

These need deeper evaluation before pattern extraction.
