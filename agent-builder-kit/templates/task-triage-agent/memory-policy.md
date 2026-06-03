# Task Triage Agent — Memory Policy

**Status:** SPEC_DRAFT

---

## Default

**No persistent memory.**

Task Triage Agent operates on the **current task only**. Each triage is independent unless a future governance phase explicitly approves memory expansion.

---

## Allowed (session-scoped)

| Data | Scope |
|------|-------|
| Current task text | Single triage request |
| Current classification | Output of current triage |
| Current trace | Output of current triage |

These exist only for the duration of one triage operation. No writeback to storage.

---

## Forbidden

| Memory type | Why forbidden |
|-------------|---------------|
| Long-term backlog | PM platform drift |
| Hidden project memory | Unbounded context, privacy risk |
| Automatic writeback | Silent state mutation |
| Profile mutation | User/team profiling |
| Task history storage | Persistent store without governance |
| User/team performance memory | Surveillance drift |
| Cross-session task correlation | Privacy and scope creep |
| RAG / knowledge retrieval | Separate phase |

---

## Input assumptions

The agent must not rely on memory of prior tasks to fill missing information. If owner, criteria, or constraints are missing from **current input**, mark as `missing_information`.

---

## Trace rules

- No memory write events in trace
- No reference to prior triage sessions unless explicitly provided in `task_text` or optional fields
- No secrets stored in trace

See [expected-traces.md](expected-traces.md).

---

## Future memory expansion

Requires:

1. Separate governance phase
2. [change-proposal.md](change-proposal.md)
3. Bounded memory specification (max items, TTL, redaction)
4. Human approval policy update
5. Evaluation cases for memory leak and stale context

**Not in v0.1 specs.**

---

## Comparison to Review Assistant

Review Assistant: task context only — see [memory-boundaries.md](../review-assistant-agent/memory-boundaries.md).

Task Triage: **stricter** — classification-only, no draft retention, no cross-task state.
