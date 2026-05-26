# Task Triage Agent — No Orchestrator Policy

**Date:** 2026-05-26  
**Status:** PLAN_ONLY — **non-negotiable**

---

## Task Triage Agent is NOT

| Forbidden role | Detail |
|----------------|--------|
| Orchestrator | Does not coordinate multiple agents |
| Router | Does not dispatch work to agents/services |
| Planner-executor | Plans only — never executes plan |
| Task queue | No backlog, queue, or scheduling |
| PM platform | No sprints, tickets, assignments |
| Multi-agent controller | No "agent A then agent B" automation |
| Workflow engine | No triggers, cron, or pipelines |

---

## What it MAY recommend (advisory text only)

| Recommendation | Example |
|----------------|---------|
| Needs review | "Suggested next step: governance review" |
| Needs implementation plan | "Create plan before code" |
| Needs escalation | "Escalate to architecture owner" |
| Blocked by missing info | "Clarify target file and acceptance criteria" |
| Defer | "Wait until v0.1 tag committed" |

Recommendations are **strings for humans** — not machine routing commands.

---

## What it MAY NOT do

| Forbidden | Example task |
|-----------|--------------|
| Start another agent | "Launch Review Assistant on this" |
| Assign work | "Assign to developer X" |
| Create queue | "Add to sprint backlog" |
| Execute plan | "Implement the adapter now" |
| Auto-route | "Best agent is Task X — routing..." |

**Response:** `BLOCKED` + `orchestrator_boundary_enforced`

---

## Language blocklist (task input)

Triggers orchestrator gate:

- "route to", "dispatch to", "send to agent"
- "start Review Assistant", "invoke agent"
- "create ticket", "Jira", "Linear", "backlog"
- "assign to", "delegate to"
- "orchestrate", "workflow", "pipeline trigger"
- "multi-agent", "agent swarm"

---

## Eval requirement (future)

Group D cases in [TASK_TRIAGE_AGENT_EVALUATION_PLAN.md](TASK_TRIAGE_AGENT_EVALUATION_PLAN.md) must always PASS with BLOCKED + orchestrator trace.

---

## Diagram

See [diagrams/no-orchestrator-boundary.md](diagrams/no-orchestrator-boundary.md).

---

## Violation consequence

Template or impl that adds routing/delegation → **rollback** per [ROLLBACK_AND_FREEZE_PLAN.md](ROLLBACK_AND_FREEZE_PLAN.md).
