# Canonical Workflow Events

Minimal event vocabulary for Phase 2.3 observability.

Format (conceptual):

```
[timestamp] EVENT_NAME actor=... detail=...
```

---

## Lifecycle

| Event | Meaning | Typical actor |
|-------|---------|---------------|
| `task_started` | Work unit accepted | orchestrator, queue |
| `task_completed` | Verified success terminal | worker, publisher |
| `task_failed` | Hard fail terminal | worker, gate |

## Retry & Queue

| Event | Meaning |
|-------|---------|
| `retry_triggered` | Bounded retry began |
| `retry_exhausted` | Max retries reached |
| `queue_recovered` | Pending tasks reloaded after crash |

## Verification

| Event | Meaning |
|-------|---------|
| `verification_passed` | Gate allowed progress |
| `verification_failed` | Gate blocked progress |

## Approval & HITL

| Event | Meaning |
|-------|---------|
| `approval_requested` | Human decision required |
| `approval_denied` | Explicit reject |
| `approval_timeout` | Deny-by-default (no response) |

## Escalation & Governance

| Event | Meaning |
|-------|---------|
| `escalation_triggered` | Automation stopped; human/supervisor path |
| `governance_rejection` | Policy stage blocked (promotion, scan) |
| `unsafe_action_blocked` | External/GUI action denied |

## Memory

| Event | Meaning |
|-------|---------|
| `memory_write_rejected` | Writeback failed (unverified, overflow) |

## LLM (Real Adapters)

| Event | Meaning |
|-------|---------|
| `llm_timeout` | Model call exceeded timeout |
| `llm_malformed_output` | Unparseable or schema-invalid response |

---

## Mapping from Repository Demos

| Demo location | Example audit action → canonical |
|---------------|----------------------------------|
| `prototypes/review-loop-agent/` | `blocked` → escalation or verification_failed |
| `integrations-real/telegram-review-gate/` | `timeout_denied` → approval_timeout |
| `integrations-real/llm-verification-adapter/` | `reject` + malformed → llm_malformed_output |
| `integrations-real/local-queue-worker/` | `escalated` → retry_exhausted + escalation_triggered |

Alignment is **documentary**, not enforced by runtime.
