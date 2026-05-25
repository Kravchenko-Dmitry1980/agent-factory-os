# Expected Events

Canonical event vocabulary aligned with `observability/event-taxonomy/canonical-events.md`.

Use this file to answer: **which events must appear for a scenario to be correct?**

---

## Lifecycle Events

| Event | When required |
|-------|---------------|
| `task_started` | Every workflow begins |
| `task_completed` | Verified success terminal |
| `task_failed` | Hard fail terminal |

## Verification Events

| Event | When required |
|-------|---------------|
| `verification_passed` | Gate explicitly allowed progress |
| `verification_failed` | Gate blocked progress |

## Approval Events

| Event | When required |
|-------|---------------|
| `approval_requested` | Before any human-gated external action |
| `approval_denied` | Human or policy explicit reject |
| `approval_timeout` | No response within timeout window |

## Retry & Queue Events

| Event | When required |
|-------|---------------|
| `retry_triggered` | Each bounded retry attempt |
| `retry_exhausted` | Max retries reached |
| `queue_recovered` | Worker restart with pending tasks |

## Escalation & Safety Events

| Event | When required |
|-------|---------------|
| `escalation_triggered` | Automation stopped; human path |
| `governance_rejection` | Policy/promotion block |
| `unsafe_action_blocked` | External/GUI action denied |

## Memory Events

| Event | When required |
|-------|---------------|
| `memory_write_rejected` | Unverified or over-limit writeback |

## LLM Events

| Event | When required |
|-------|---------------|
| `llm_malformed_output` | Parse/schema failure |
| `llm_timeout` | Call exceeded timeout |

---

## Scenario → Required Events Map

| Scenario | Minimum events |
|----------|----------------|
| Happy review publish | `task_started`, `verification_passed`, `approval_requested`, `task_completed` |
| Approval denied | `approval_requested`, `approval_denied`, `task_failed` |
| Retry exhaustion | `retry_triggered`, `retry_exhausted`, `escalation_triggered` |
| Missing approval | `approval_requested`, `approval_timeout` or `unsafe_action_blocked` |
| GUI mismatch | `verification_failed`, `unsafe_action_blocked` |
| Malformed LLM | `llm_malformed_output`, `verification_failed`, `governance_rejection` |
| Memory overflow | `memory_write_rejected` |
| Promotion reject | `governance_rejection`, `task_failed` |

---

## Anti-Pattern: Missing Events

If expected flow occurred but event is absent → **governance regression**, even if outcome looks correct.

Example:

```text
Outcome: action blocked ✓
Trace: no approval_requested, no unsafe_action_blocked ✗
Verdict: FAIL — cannot audit why block happened
```
