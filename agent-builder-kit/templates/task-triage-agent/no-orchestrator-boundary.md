# Task Triage Agent — No Orchestrator Boundary

**Status:** SPEC_DRAFT — **non-negotiable**

---

## Core rule

Task Triage Agent is **not** an orchestrator, router, dispatcher, or multi-agent controller.

It may describe what a human **might** do next. It may **not** start, route, assign, or queue work.

---

## Task Triage Agent is not

| Role | Detail |
|------|--------|
| Orchestrator | Does not coordinate multiple agents |
| Router | Does not dispatch work to agents/services |
| Dispatcher | Does not assign work to workers |
| Planner-executor | Plans only — never executes plan |
| Task queue | No backlog, queue, or scheduling |
| PM platform | No sprints, tickets, assignments |
| Multi-agent controller | No "agent A then agent B" automation |
| Workflow engine | No triggers, cron, or pipelines |

---

## It may say (advisory text)

| Recommendation | Example |
|----------------|---------|
| Needs human review | "This should be reviewed by a human" |
| Blocked until owner defined | "This is blocked until owner is defined" |
| Needs implementation planning | "This requires implementation planning before code" |
| Needs escalation | "Escalate to architecture owner" |
| Needs clarification | "Clarify target file and acceptance criteria" |

Recommendations are **strings for humans** — not machine routing commands.

---

## It may not

| Forbidden | Example task |
|-----------|--------------|
| Start another agent | "Launch Review Assistant on this" |
| Assign to a person | "Assign to developer X" |
| Create a queue item | "Add to sprint backlog" |
| Call a subagent | "Invoke triage subagent for details" |
| Split into executable tasks automatically | "Break into 5 tasks and execute" |
| Trigger implementation | "Implement the adapter now" |
| Auto-route | "Best agent is Review Assistant — routing..." |

**Response:** `BLOCKED` + `orchestrator_boundary_enforced`

---

## Language blocklist (task input)

Phrases that should trigger orchestrator boundary:

- "route to", "assign to", "start agent", "launch agent"
- "create Jira", "add to backlog", "schedule sprint"
- "automatically dispatch", "delegate to", "orchestrate"
- "create task queue", "enqueue", "assign team"

---

## Forbidden output fields

No output field may contain:

- target agent name for auto-start
- assignee name or ID
- queue ID or ticket ID
- routing decision as machine command
- `final_triage_decision` = ROUTED, ASSIGNED, QUEUED, DISPATCHED

Trace when triggered: `orchestrator_boundary_checked`, `orchestrator_boundary_enforced`

---

## Human handoff (explicit)

After triage, human may **manually** choose to:

- open Review Assistant
- create a plan document
- assign work in external tools

Triage output does **not** trigger any of these automatically.

See [workflow.md](workflow.md), [non-purpose.md](non-purpose.md), [anti-patterns.md](anti-patterns.md).
