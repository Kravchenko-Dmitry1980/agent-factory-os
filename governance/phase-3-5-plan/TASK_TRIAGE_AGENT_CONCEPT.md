# Task Triage Agent — Concept

**Date:** 2026-05-26  
**Status:** PLAN_ONLY

---

## What it is

A **text-only agent** that classifies incoming tasks and proposes safe next steps for a human decision-maker.

It sits **upstream** of implementation, review, and delivery agents.

---

## What it does

| Step | Action |
|------|--------|
| 1 | Reads a task description (and optional context label) |
| 2 | Classifies task type |
| 3 | Detects risk level |
| 4 | Detects missing information |
| 5 | Suggests next step (advisory) |
| 6 | Recommends whether human approval is needed |
| 7 | Recommends escalation or deferral if appropriate |
| 8 | Emits human-readable trace |
| 9 | Returns final triage decision |

---

## What it does not do

| Forbidden | Detail |
|-----------|--------|
| Execute task | No code, files, commands |
| Call tools | No MCP, shell, APIs |
| Assign people | No ownership routing |
| Create tickets | No Jira/Linear/etc. |
| Start agents | No "launch Review Assistant now" |
| Modify files | No repo writes |
| Send messages | No email/Telegram/Slack |
| Route automatically | No multi-agent dispatch |
| Trigger automation | No workflows, queues, cron |

---

## Example input

```text
Нужно добавить LLM adapter к Review Assistant, но не сломать mock default.
```

---

## Example output (advisory)

| Field | Value |
|-------|-------|
| Task type | implementation / architecture-change |
| Risk | medium |
| Missing info | provider choice, data policy, rollback plan, eval impact |
| Suggested next step | create implementation plan; confirm no provider-by-default |
| Human approval required | yes |
| Escalation | no (unless frozen spec touch proposed) |
| Final decision | **TRIAGED** |

Trace includes: `task_received`, `task_type_classified`, `risk_detected`, `missing_info_detected`, `next_step_proposed`, `approval_required`, `triage_completed`.

---

## Position in agent ecosystem

```text
Human task
    ↓
Task Triage Agent  ← classify, advise (this agent)
    ↓
Human decision
    ↓
(plan / impl / review / defer)
    ↓
Review Assistant (when content review needed)
```

Triage does **not** connect directly to execution.

---

## Design principles

1. **Advisory only** — triage ≠ permission to act
2. **Fail closed on unsafe** — REJECT_UNSAFE / BLOCKED for policy violations
3. **Missing info explicit** — vague tasks → NEEDS_CLARIFICATION
4. **No hidden delegation** — never "I assigned this to X"
5. **Trace every decision** — human-readable, no silent routing

---

## Related

- [TASK_TRIAGE_AGENT_SCOPE.md](TASK_TRIAGE_AGENT_SCOPE.md)
- [TASK_TRIAGE_AGENT_CONTRACT.md](TASK_TRIAGE_AGENT_CONTRACT.md)
