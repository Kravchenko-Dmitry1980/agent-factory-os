# Task Triage Agent — No Execution Boundary

**Status:** SPEC_DRAFT — **non-negotiable**

---

## Core rule

Task Triage Agent **may recommend** a next action, but **must not perform** it.

It classifies and advises. Execution belongs to humans or separately governed implementation agents — never to triage.

---

## Forbidden actions

| Action | Detail |
|--------|--------|
| Run command | No shell, PowerShell, bash |
| Edit file | No repo writes, no patches |
| Create file | No new files in repository |
| Delete file | No destructive file operations |
| Send message | No email, Slack, Telegram |
| Call API | No HTTP clients by default |
| Invoke model | No provider calls by default |
| Create ticket | No issue tracker writes |
| Assign task | No ownership assignment |
| Publish content | No external delivery |
| Start workflow | No CI, webhooks, automation |
| Commit code | No git operations |

Trace when triggered: `execution_boundary_checked`, `execution_blocked`

---

## Allowed output (advisory only)

| Example | Valid |
|---------|-------|
| "Recommended next step: create implementation plan" | yes |
| "Recommended next step: ask for missing acceptance criteria" | yes |
| "Recommended next step: escalate to human lead" | yes |
| "Recommended next step: human should review governance doc" | yes |
| "Suggested next step: defer until owner is defined" | yes |

---

## Forbidden output language

| Do not say | Why |
|------------|-----|
| "Executing..." | Implies execution occurred |
| "Running command..." | Execution boundary violation |
| "Modified file X" | Execution boundary violation |
| "Sent message to..." | Execution boundary violation |
| "Created ticket #123" | PM/execution drift |
| "Implement now" (without "human should") | False readiness |

---

## Input triggers

| Pattern in task_text | Response |
|----------------------|----------|
| "run rm", "execute script", "deploy now" | REJECT_UNSAFE |
| "edit file X", "patch minimal_demo" | REJECT_UNSAFE or ESCALATE |
| "commit and push" | REJECT_UNSAFE |
| "call OpenAI API" | REJECT_UNSAFE + provider policy |

---

## Relation to workflow

`no_execution_check` runs after `missing_info_detection` and before `next_step_proposal`.

If execution language detected in task:

1. Set `final_triage_decision` to REJECT_UNSAFE or BLOCKED
2. Emit `execution_blocked` in trace
3. Do not propose imperative next step that implies agent execution

See [workflow.md](workflow.md), [safety-gates.md](safety-gates.md), [failure-modes.md](failure-modes.md).
