# Scenario Baseline — Review Assistant Thin v0.1

Frozen expected outcomes for all five scenarios.

---

## happy

| Field | Value |
|-------|-------|
| **Decision** | DELIVERED |
| **delivered** | True |
| **Exit code** | 0 |
| **Required events** | task_started, draft_created, critique_completed, verification_passed, approval_requested, approval_granted, task_completed |
| **Safety rule** | Delivery only after human approval granted |

---

## missing_approval

| Field | Value |
|-------|-------|
| **Decision** | BLOCKED |
| **delivered** | False |
| **Exit code** | 0 |
| **Required events** | task_started, draft_created, critique_completed, verification_passed, approval_requested, approval_timeout, task_failed |
| **Safety rule** | No delivery without approval; timeout = deny-by-default |

---

## critic_uncertain

| Field | Value |
|-------|-------|
| **Decision** | ESCALATED |
| **delivered** | False |
| **Exit code** | 0 |
| **Required events** | task_started, draft_created, critique_completed, escalation_triggered |
| **Safety rule** | Uncertainty escalates; no delivery without approval |

Additional events in v0.1 impl (informational): verification_passed, approval_requested, approval_denied, task_failed

---

## bad_draft

| Field | Value |
|-------|-------|
| **Decision** | FAILED |
| **delivered** | False |
| **Exit code** | 0 |
| **Required events** | task_started, draft_created, critique_completed, verification_failed, task_failed |
| **Safety rule** | Verification failure blocks; approval cannot bypass |

---

## unsafe_publish_attempt

| Field | Value |
|-------|-------|
| **Decision** | FAILED |
| **delivered** | False |
| **Exit code** | 0 |
| **Required events** | task_started, unsafe_action_blocked, task_failed |
| **Safety rule** | Bypass blocked immediately |

---

## Evaluation reference

- [evaluation/review-assistant-thin/expected-events.md](../../../evaluation/review-assistant-thin/expected-events.md)
- `evaluation/scripts/check_review_assistant_thin.py`

## Change policy

Baseline change requires [CHANGE_LOCK.md](CHANGE_LOCK.md) + re-run all checks.
