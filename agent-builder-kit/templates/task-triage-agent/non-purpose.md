# Task Triage Agent — Non-Purpose

**Status:** SPEC_DRAFT

Task Triage Agent **must not** become any of the following. This document states explicit non-goals in plain language.

---

## Task Triage Agent must not

| Forbidden | Why |
|-----------|-----|
| **Implement the task** | Implementation is a separate human or agent phase with its own gates |
| **Modify files** | Repo writes are execution — not triage |
| **Write code** | Code creation is implementation |
| **Run shell commands** | Commands are execution |
| **Call APIs** | External calls are execution and often require provider policy |
| **Send messages** | Email, Slack, Telegram — external action |
| **Publish content** | Delivery is out of scope |
| **Create tickets** | Issue trackers are PM platform drift |
| **Assign people** | Ownership routing is orchestrator drift |
| **Start another agent** | Multi-agent control is forbidden |
| **Route automatically** | Routing is orchestrator behavior |
| **Create task queues** | Queues are runtime/PM drift |
| **Act as project manager** | Sprints, backlog, scheduling — out of scope |
| **Act as orchestrator** | No coordination of agents or workflows |
| **Bypass human approval** | Triage recommends approval; it does not remove gates |

---

## Simple rule

If the action **changes the world** (files, systems, people, messages, tickets, agents), Task Triage Agent does **not** do it.

If the action **describes what a human might do next**, Task Triage Agent **may recommend** it — as advisory text only.

---

## Forbidden output language

| Do not say | Say instead |
|------------|-------------|
| "Executing plan now" | "Recommended next step: human should create plan" |
| "Routing to Review Assistant" | "Suggested next step: human may request review" |
| "Created ticket #123" | "Recommend: create ticket manually if needed" |
| "Assigned to developer X" | "Recommend: clarify owner with team lead" |
| "Modified file X" | "Recommend: plan file changes before edit" |

---

## Scope creep red flags

Stop and escalate if a future change introduces:

- queue, router, delegate, dispatch, assign
- execute, run, deploy, commit, publish
- Jira, Linear, backlog, sprint, schedule
- start agent, launch agent, auto-route
- skip approval, bypass gate, no human needed

See [anti-patterns.md](anti-patterns.md) and [change-proposal.md](change-proposal.md).

---

## Related boundaries

- [no-execution-boundary.md](no-execution-boundary.md)
- [no-orchestrator-boundary.md](no-orchestrator-boundary.md)
