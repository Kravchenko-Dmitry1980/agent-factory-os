---
classification: operational-guidance
source_tier: operational-playbook
promotion_status: unreviewed
canonical_status: non-canonical
origin: swarm-playbooks
---

# Orchestration Lifecycle

Операционный lifecycle multi-agent execution, извлечённый из playbook-источников.  
**Не** canonical state machine — см. Agent-OS task lifecycle для governance-grade spec.

## Canonical Flow

```
goal → planning → decomposition → execution → critique → review → approval → publish
```

## Phase Detail

### 1. Goal

**Owner:** Human operator  
**Input:** Natural language objective (+ project profile / brand context in advanced setups)  
**Output:** Run record with goal text, optional budget cap  
**Exit criteria:** Run created; size classification (small vs large)

**Human intervention:** Defines what success looks like; may attach fixtures from ЗАДАЧА.md era.

**Failure modes:** Vague goal → bad plan → wasted run cost. Mitigation: вход/выход/критерии до automation.

---

### 2. Planning

**Owner:** Orchestrator agent (Стратег)  
**Input:** Goal, active agent roster, project profile  
**Output:** Task graph proposal (description, assignee, dependencies)  
**Exit criteria:** Plan persisted; small runs auto-continue; **large runs → awaiting_plan_approval**

**Human intervention:** Reviews plan for large runs; may edit/delete/reassign tasks (Prompt 4).

**Failure modes:** Over-decomposition; wrong agent assignment; missing dependencies.  
**Verification:** Plan structure review — not truth verification.

---

### 3. Decomposition

**Owner:** Orchestrator + persistence layer  
**Input:** Approved plan  
**Output:** `tasks` rows in queue-ready state  
**Exit criteria:** All tasks `queued` with valid dependencies resolved

**Human intervention:** Optional plan edit before queue start.

**Failure modes:** Circular dependencies; orphan tasks; no executor for role.

**Queues matter:** Tasks enter persistent queue — not immediate parallel LLM fan-out in UI thread.

---

### 4. Execution

**Owner:** Queue worker + executor agents  
**Input:** Queued task, tools scoped to run/task  
**Output:** Task result artifact, cost/token fields  
**Exit criteria:** Task `completed` or `waiting_question` or `failed`

**Human intervention:** Answer agent questions (`waiting_question` status).

**Failure modes:** Tool timeout; model error; context overflow; runaway retries.

**Queues matter:** Sequential/controlled processing; **recovery on backend restart** picks up incomplete tasks.

---

### 5. Critique

**Owner:** Critic agent (automated)  
**Input:** Task result  
**Output:** Verdict (pass / rework), optional comments  
**Exit criteria:** Pass, or rework count ≤ cap (playbook: **2 rounds**), then escalate to review anyway

**Human intervention:** None in automated loop.

**Failure modes:** False pass; false fail loop; critic-executor collusion.  
**Verification matters:** Critique ≠ verification — see `critique/critique-vs-verification.md`.

---

### 6. Review

**Owner:** Human operator  
**Input:** Run summary + per-task artifacts in «На проверке» queue  
**Output:** Per-item approve or rework-with-comment  
**Exit criteria:** All items dispositioned

**Human intervention:** **Mandatory** before treated as done.

**Failure modes:** Queue backlog; summary mismatch; rubber-stamp approvals.

---

### 7. Approval

**Owner:** Human operator (may equal reviewer in solo setup)  
**Input:** Reviewed artifacts designated for external effect  
**Output:** Approval event on record  
**Exit criteria:** Explicit consent for publish/send/pay class actions

**Human intervention:** **Gate for external actions** — fail-closed default.

**Failure modes:** Approve wrong version; bypass via ungated tool.

---

### 8. Publish

**Owner:** System integration (Telegram, CMS, etc.)  
**Input:** Approved artifact  
**Output:** External publication + downstream records (e.g. content_draft → content_plan)  
**Exit criteria:** Publish ack or structured failure

**Human intervention:** Already occurred at approval; optional post-publish monitoring.

**Failure modes:** Partial publish; wrong channel; irreversible send.

---

## Where Humans Intervene (Summary)

| Phase | Required? | Optional? |
|-------|-----------|-----------|
| goal | ✓ define | |
| planning | ✓ (large runs) | edit plan |
| decomposition | | edit before queue |
| execution | | answer questions |
| critique | | |
| review | ✓ | |
| approval | ✓ (external) | |
| publish | | monitor |

## Where Failures Happen (Heat Map)

| Phase | Frequency | Severity |
|-------|-----------|----------|
| goal | High ( vagueness ) | High |
| planning | High | Medium |
| execution | High | Medium |
| critique | Medium ( false confidence ) | High |
| review | Low ( process ) | High if skipped |
| approval | Low | Critical |
| publish | Low | Critical |

## Where Queues Matter

- Between **decomposition → execution**: async work, UI responsive
- **Recovery**: incomplete tasks after crash
- **Review queue**: human batch processing separate from task queue

## Where Verification Matters

- **Not** in critic phase alone
- **At** review: human judgment
- **Before publish:** approval + optional deterministic checks (links, schema) — **not in playbooks formally**
- Canonical systems: evaluation-before-writeback, trace records, contracts

## Related

- [patterns/orchestration-lifecycle.md](../patterns/orchestration-lifecycle.md)
- [diagrams/orchestration-lifecycle.md](../diagrams/orchestration-lifecycle.md)
- [hitl/review-before-publish.md](../hitl/review-before-publish.md)
