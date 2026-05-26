# Observability Trace Spec

Text-first trace requirements for agent templates.

**No telemetry platform.** Traces are human-readable documents aligned with repository canonical events.

Source: `observability/event-taxonomy/canonical-events.md`

---

## Required Events

Every agent template trace must be mappable to these events (minimum):

| Event | When |
|-------|------|
| `task_started` | Work unit accepted |
| `verification_passed` | Gate allowed progress |
| `verification_failed` | Gate blocked progress |
| `approval_requested` | Human decision required |
| `approval_denied` | Explicit reject |
| `approval_timeout` | Deny-by-default (no response) |
| `escalation_triggered` | Automation stopped; human path |
| `unsafe_action_blocked` | External/action denied |
| `governance_rejection` | Policy blocked action |
| `task_completed` | Verified success terminal |
| `task_failed` | Hard fail terminal |

Optional but recommended: `retry_triggered`, `llm_malformed_output`, `memory_write_rejected`

---

## Trace Format (Conceptual)

```
[timestamp] EVENT_NAME actor=... detail=...
```

Example references:

- `observability/examples/successful-review-trace.txt`
- `observability/examples/failed-review-trace.txt`

---

## Trace Readability

Good traces allow an operator to answer in **under 2 minutes**:

1. What was the task?
2. Which gates passed/failed?
3. Was human approval requested and obtained?
4. What was the terminal outcome?
5. Was anything blocked and why?

---

## Good Trace

```
TRACE id=rev-001 workflow=review-assistant scenario=happy
────────────────────────────────────────────────────────
[19:56:59] task_started         actor=orchestrator  task_id=cb81 goal=blog_post
[19:56:59] verification_passed  actor=critic        advisory=true
[19:56:59] approval_requested   actor=human         required=true
[19:56:59] verification_passed  actor=human         decision=approve
[19:56:59] task_completed       actor=publisher     published=true
────────────────────────────────────────────────────────
OUTCOME status=completed
GOVERNANCE gates_passed=3 gates_failed=0 escalated=no
```

**Why good:** chronological, actors named, advisory critic flagged, human gate visible, outcome summary.

---

## Bad Trace

```
Done. Published.
```

**Why bad:** no events, no gates, no approval proof, not auditable.

---

## Trace Review Checklist

- [ ] `task_started` present
- [ ] Every gate emits pass or fail event
- [ ] `approval_requested` before risky action
- [ ] Terminal event (`task_completed` or `task_failed`)
- [ ] OUTCOME summary with gate counts
- [ ] No gap where publish could happen invisibly
- [ ] Critic marked advisory if used

See [evaluation-checklists/trace-review-checklist.md](../evaluation-checklists/trace-review-checklist.md)

---

## Related

- [trace-templates/](../trace-templates/README.md)
- `observability/event-taxonomy/event-lineage.md`
- `observability/event-taxonomy/anti-pattern-events.md`
