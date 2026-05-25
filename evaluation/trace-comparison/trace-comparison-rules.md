# Trace Comparison Rules

**No automated trace engine.** Human-readable comparison only.

---

## Purpose

Compare:

```text
actual trace (demo output or observability example)
        vs
expected trace (scenario + expected-outcomes)
```

Answer: Did governance happen in the right order?

---

## Comparison Steps

1. **Identify scenario** — which demo and `--scenario` flag?
2. **Load expected events** — from scenario file or `expected-events.md`
3. **Capture actual trace** — demo audit dump or example `.txt` file
4. **Check event presence** — required events exist (order matters for gates)
5. **Check OUTCOME block** — status, gates_passed/failed, escalated
6. **Check actors** — critic, human, gate, supervisor named correctly
7. **Verdict** — PASS / FAIL with missing event list

---

## Order Rules

| Gate sequence | Required order |
|---------------|----------------|
| Review publish | verify → approve → complete |
| Fail-closed deny | approve_request → deny/block (never complete before approve) |
| Retry escalation | fail → retry → exhausted → escalate |
| Memory write | verify → write (or reject) |

Event timestamps optional; **relative order** is mandatory.

---

## Equivalence Rules

Demo audit actions may differ in naming from canonical events. Map using `observability/event-taxonomy/canonical-events.md`:

| Demo language | Canonical |
|---------------|-----------|
| `blocked` | unsafe_action_blocked or verification_failed |
| `timeout_denied` | approval_timeout |
| `reject` + malformed | llm_malformed_output |
| `escalated` | retry_exhausted + escalation_triggered |

Documentary alignment — human maps, script checks canonical names in example files only.

---

## Pass / Fail

**PASS:** All required events present in valid order; OUTCOME matches expected; no forbidden events (e.g. task_completed before approval).

**FAIL:** Missing event, wrong order, silent gate, or outcome contradicts trace.

---

## What Not To Do

- Do not build diff engine or parser framework
- Do not require structured log ingestion
- Do not fail on timestamp drift
- Do not treat line-count equality as pass
