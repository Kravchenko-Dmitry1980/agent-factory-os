# Expected Events — Review Assistant Thin

Required **substring** presence in stdout trace (matches [SCENARIO_BASELINE.md](../../prototypes-derived/review-assistant-thin/freeze/SCENARIO_BASELINE.md)).

---

## happy

```text
task_started
draft_created
critique_completed
verification_passed
approval_requested
approval_granted
task_completed
decision=DELIVERED
delivered=True
```

---

## missing_approval

```text
task_started
draft_created
critique_completed
verification_passed
approval_requested
approval_timeout
task_failed
decision=BLOCKED
delivered=False
```

---

## critic_uncertain

```text
task_started
draft_created
critique_completed
escalation_triggered
decision=ESCALATED
delivered=False
```

---

## bad_draft

```text
task_started
draft_created
critique_completed
verification_failed
task_failed
decision=FAILED
delivered=False
```

---

## unsafe_publish_attempt

```text
task_started
unsafe_action_blocked
task_failed
decision=FAILED
delivered=False
```

---

## Script

`evaluation/scripts/check_review_assistant_thin.py` encodes these checks.

Event names align with `observability/event-taxonomy/canonical-events.md` where applicable.
