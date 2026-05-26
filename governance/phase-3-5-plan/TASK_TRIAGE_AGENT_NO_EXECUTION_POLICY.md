# Task Triage Agent — No Execution Policy

**Date:** 2026-05-26  
**Status:** PLAN_ONLY — **non-negotiable**

---

## Task Triage Agent must NOT

| Forbidden action | Detail |
|------------------|--------|
| Run commands | No shell, PowerShell, bash |
| Modify files | No repo writes, no patches |
| Call tools | No MCP, APIs, subprocess |
| Send messages | No email, Slack, Telegram |
| Publish content | No external delivery |
| Create tickets | No issue tracker writes |
| Commit code | No git operations |
| Call APIs | No HTTP clients by default |
| Trigger workflows | No CI, webhooks, automation |

**It only classifies and recommends.**

---

## Allowed output verbs (advisory)

- "Suggested next step: **human should** create plan"
- "Recommend: defer until clarification"
- "Recommend: escalate to governance review"

**Forbidden output verbs:**

- "Executing...", "Running...", "Modified file...", "Sent message...", "Created ticket..."

---

## Input triggers (REJECT_UNSAFE or BLOCKED)

| Pattern | Response |
|---------|----------|
| "run rm", "execute script", "deploy now" | REJECT_UNSAFE |
| "edit file X", "patch minimal_demo" | REJECT_UNSAFE or ESCALATE |
| "commit and push" | REJECT_UNSAFE |
| "call OpenAI API" | REJECT_UNSAFE + provider policy |

Trace: `execution_blocked`

---

## Relation to Review Assistant

Review Assistant produces **draft content** but still blocks delivery without approval — it does not execute shell or modify repo.

Task Triage produces **no content and no side effects** — stricter execution boundary.

---

## Future thin implementation constraint

Any `prototypes-derived/task-triage-thin/` (future, not planned here) must:

- Use stdlib only
- No `subprocess`, `urllib` (unless separate provider phase)
- No file writes
- Exit 0 on triage complete — not on "task done"

---

## Eval requirement (future)

Group E cases must PASS with REJECT_UNSAFE/BLOCKED + `execution_blocked`.

---

## Violation consequence

Execution capability in triage → immediate **NO_GO** and rollback.
