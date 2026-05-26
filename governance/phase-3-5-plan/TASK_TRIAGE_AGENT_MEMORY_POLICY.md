# Task Triage Agent — Memory Policy

**Date:** 2026-05-26  
**Status:** PLAN_ONLY

---

## Default

| Rule | Value |
|------|-------|
| Persistent memory | **Forbidden** |
| Long-term task history | **Forbidden** |
| User profile mutation | **Forbidden** |
| Hidden project memory | **Forbidden** |
| Automatic writeback | **Forbidden** |
| Task backlog memory | **Forbidden** |

---

## Allowed (session-scoped only)

| Item | Scope |
|------|-------|
| Current task text | Single triage invocation |
| Current classification fields | Same invocation output |
| Current trace | Same invocation |
| Optional context label | Provided by human per task — not stored |

Memory ends when triage completes. No cross-task recall.

---

## Forbidden patterns

- "Remember this task for next sprint"
- SQLite/Redis/file store of triage history
- Embedding index of past tasks (RAG)
- Learning from user corrections without governance
- Writing triage results to repo automatically

---

## Future memory (requires separate governance phase)

Any persistent memory requires:

1. Change proposal
2. Data safety review
3. Retention policy
4. User consent model
5. Rollback plan
6. Explicit NO by default until approved

---

## Comparison to Review Assistant

Review Assistant template: [memory-boundaries.md](../../agent-builder-kit/templates/review-assistant-agent/memory-boundaries.md) — session/task scoped, no unbounded writeback.

Task Triage is **stricter**: classification-only agent should retain **less** than Review Assistant, not more.
