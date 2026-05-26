# Review Assistant Agent — Expected Traces

Human-readable traces using canonical events from `observability/event-taxonomy/canonical-events.md`.

---

## Happy Path (Good Draft Approved)

```
TRACE id=ra-001 workflow=review-assistant scenario=good-draft-approved
────────────────────────────────────────────────────────
[10:00:01] task_started         actor=orchestrator  task_id=cb81 goal=blog_post_q1
[10:00:02] task_started         actor=worker        action=draft_created
[10:00:03] verification_passed  actor=critic        advisory=true facts_verified=false
[10:00:03] approval_requested   actor=human         required=true artifact_id=draft-cb81
[10:00:15] verification_passed  actor=human         decision=approve
[10:00:15] task_completed       actor=delivery      delivered=true
────────────────────────────────────────────────────────
OUTCOME status=completed
GOVERNANCE gates_passed=3 gates_failed=0 escalated=no
```

Source alignment: `observability/examples/successful-review-trace.txt`

---

## Rejection Path (Bad Draft Rejected)

```
TRACE id=ra-002 workflow=review-assistant scenario=bad-draft-rejected
────────────────────────────────────────────────────────
[10:05:01] task_started         actor=orchestrator  task_id=a1b2
[10:05:02] verification_passed  actor=critic        advisory=true verdict=pass
[10:05:02] approval_requested   actor=human         required=true
[10:05:10] approval_denied      actor=human         reason=factual_errors
[10:05:10] task_failed          actor=system        reason=approval_denied
────────────────────────────────────────────────────────
OUTCOME status=rejected
GOVERNANCE gates_passed=1 gates_failed=1 escalated=no
```

Note: critic passed — human caught error. **critic ≠ truth.**

Source alignment: `observability/examples/failed-review-trace.txt`

---

## Uncertain Critic (Fail-Closed)

```
TRACE id=ra-003 workflow=review-assistant scenario=critic-uncertain
────────────────────────────────────────────────────────
[10:10:01] task_started         actor=orchestrator  task_id=x9y8 goal=revenue_report
[10:10:03] verification_failed  actor=critic        advisory=true verdict=uncertain reason=unverified_figures
[10:10:03] escalation_triggered actor=system        reason=critic_uncertain
[10:10:03] approval_requested   actor=human         required=true
────────────────────────────────────────────────────────
OUTCOME status=held
GOVERNANCE gates_passed=0 gates_failed=1 escalated=yes
```

No `task_completed` until human explicitly approves after review.

---

## Bypass Blocked

```
TRACE id=ra-004 workflow=review-assistant scenario=bypass-blocked
────────────────────────────────────────────────────────
[10:15:01] task_started         actor=orchestrator  task_id=z7w6
[10:15:02] unsafe_action_blocked actor=gate          reason=bypass_not_allowed
[10:15:02] task_failed          actor=system        reason=unsafe_action_blocked
────────────────────────────────────────────────────────
OUTCOME status=failed
GOVERNANCE gates_passed=0 gates_failed=1 escalated=no
```

---

## Templates

See [trace-templates/](../../trace-templates/README.md) for blank forms.
