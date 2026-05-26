# Trace Examples — Review Assistant Thin

Expected trace shape per scenario (run demo to compare).

---

## happy

```text
TRACE
- task_started: scenario=happy, task=...
- draft_created: draft_id=local-draft-hap
- critique_completed: result=OK, advisory=True
- verification_passed: checks=basic_safety
- approval_requested: mode=mock
- approval_granted: source=scenario
- task_completed: decision=DELIVERED

FINAL decision=DELIVERED delivered=True
```

---

## missing_approval

```text
TRACE
- task_started: scenario=missing_approval, ...
- draft_created: ...
- critique_completed: result=OK, advisory=True
- verification_passed: checks=basic_safety
- approval_requested: mode=mock
- approval_timeout: policy=deny_by_default
- task_failed: decision=BLOCKED, reason=approval_timeout

FINAL decision=BLOCKED delivered=False
```

---

## critic_uncertain

```text
TRACE
- task_started: scenario=critic_uncertain, ...
- draft_created: ...
- critique_completed: result=UNCERTAIN, advisory=True
- escalation_triggered: reason=critic_uncertain
- verification_passed: checks=basic_safety_with_caution
- approval_requested: mode=mock
- approval_denied: reason=approval_missing
- task_failed: decision=ESCALATED, reason=no_delivery_without_approval_after_uncertainty

FINAL decision=ESCALATED delivered=False
```

---

## bad_draft

```text
TRACE
- task_started: scenario=bad_draft, ...
- draft_created: draft_id=local-draft-bad
- critique_completed: result=BAD_DRAFT, advisory=True
- verification_failed: reason=draft_empty
- task_failed: decision=FAILED, reason=verification_failed

FINAL decision=FAILED delivered=False
```

Note: approval not reached — verification blocks first.

---

## unsafe_publish_attempt

```text
TRACE
- task_started: scenario=unsafe_publish_attempt, ...
- unsafe_action_blocked: reason=bypass_not_allowed
- task_failed: decision=FAILED, reason=unsafe_publish_attempt

FINAL decision=FAILED delivered=False
```

---

## LLM mock scenarios (Phase 3.2)

See [llm_boundary.md](llm_boundary.md) and `evaluation/review-assistant-thin/llm-expected-events.md`.

### llm_valid_draft

`llm_request_started` → `llm_parse_passed` → `verification_passed` → `approval_granted` → `task_completed` → DELIVERED

### llm_malformed_output

`llm_parse_failed` → `task_failed` — no approval

### llm_timeout

`llm_timeout` → `escalation_triggered` → ESCALATED — no response received

### llm_uncertain

`llm_uncertain` → `escalation_triggered` → ESCALATED

### llm_unsafe_output

`llm_unsafe_output` → `unsafe_action_blocked` → FAILED

---

## Canonical alignment

Event names align with `observability/event-taxonomy/canonical-events.md` where applicable.

Frozen template reference: `agent-builder-kit/templates/review-assistant-agent/expected-traces.md`
