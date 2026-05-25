# Anti-Patterns

Observed or implied anti-patterns in Hermes context — lessons for agent design.

---

## 1. Unbounded Memory

**Problem:** Letting agent memory grow without limits leads to noise, cost, and prompt bloat.

**Hermes solution:** Hard char limits (2200/1375). Force curation.

**Agent-OS relevance:** `09_antipatterns/memory-as-crutch.md`

---

## 2. Mid-Session Memory Injection

**Problem:** Updating system prompt mid-session invalidates prefix cache, increases cost.

**Hermes solution:** Frozen snapshot at session start. Writes persist but don't inject.

**Lesson:** Separate persistence from injection timing.

---

## 3. Multiple External Memory Providers

**Problem:** Multiple providers → tool schema bloat, conflicting writes, unpredictable behavior.

**Hermes solution:** One-external-provider rule enforced by MemoryManager.

**Lesson:** Enforce single external backend or explicit priority.

---

## 4. Subagent Memory Writes

**Problem:** Subagent writing to user memory corrupts user model with task-specific ephemera.

**Hermes solution:** Block memory tool in subagents. Tag agent_context.

**Lesson:** Scope memory writes to primary agent context.

---

## 5. Cron Agent Memory Writes

**Problem:** Scheduled jobs with system prompts writing to user memory corrupt representation.

**Hermes solution:** agent_context: cron → providers skip writes.

**Lesson:** Tag agent contexts and restrict side effects.

---

## 6. Using Delegate for Long-Running Work

**Problem:** delegate_task blocks parent, no resumability, no human-in-loop.

**Hermes solution:** Kanban for durable work. Decision matrix in docs.

**Lesson:** Match multi-agent primitive to workflow duration and coordination needs.

---

## 7. Using Kanban for Quick Answers

**Problem:** Kanban overhead (DB, dispatcher, profile spawn) for simple subtask.

**Hermes solution:** delegate_task for parent-needs-answer-now scenarios.

**Lesson:** Don't over-engineer simple delegation.

---

## 8. Subagent Without Context

**Problem:** Subagent knows nothing except goal. Vague goals fail.

**Hermes solution:** Documentation emphasizes context passing. Still user error prone.

**Lesson:** Validate context completeness before delegation.

---

## 9. Recursive Subagent Delegation

**Problem:** Subagent spawning subagent → unbounded depth, cost explosion.

**Hermes solution:** Block delegate_task in subagents.

**Lesson:** Enforce delegation depth limits.

---

## 10. Skill Catalog Without Progressive Loading

**Problem:** Loading 160+ full skills into prompt → token explosion.

**Hermes solution:** Progressive disclosure (list → view → reference).

**Lesson:** Tier skill loading by necessity.

---

## 11. Auto-Deleting Skills

**Problem:** Curator or agent deleting skills loses recoverable knowledge.

**Hermes solution:** Archive only, never auto-delete. Pinned bypass.

**Lesson:** Prefer archive over delete for agent-created content.

---

## 12. OAuth in Auto-Reload Context

**Problem:** Config auto-reload with 30s timeout fails OAuth flow.

**Hermes solution:** Separate `hermes mcp login` command with 5min timeout.

**Lesson:** Interactive auth needs dedicated flow, not background reload.

---

## 13. Central Orchestrator God Object

**Problem:** Single file handling all CLI commands → unmaintainable.

**Hermes exhibits:** main.py (~14k lines).

**Agent-OS relevance:** `09_antipatterns/central-orchestrator-god-object.md`

**Lesson:** Split entry points early, even if startup cost is higher.

---

## 14. Infinite Retry Loops

**Problem:** Agent retrying failed task indefinitely.

**Hermes mitigation:** Kanban failure_limit (default 2) auto-blocks task.

**Agent-OS relevance:** `09_antipatterns/infinite-retry-loops.md`

---

## Summary Table

| Anti-Pattern | Hermes Mitigation | Extract to Agent-OS |
|--------------|-------------------|---------------------|
| Unbounded memory | Char limits | Yes |
| Mid-session injection | Frozen snapshot | Yes |
| Multi-provider conflict | One-provider rule | Yes |
| Subagent memory writes | Tool block | Yes |
| Wrong multi-agent primitive | Decision matrix | Yes |
| Recursive delegation | Tool block | Yes |
| Skill token explosion | Progressive disclosure | Yes |
| Auto-delete skills | Archive only | Yes |
| God object entry point | (Not mitigated) | Yes (as anti-pattern) |
