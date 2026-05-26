# LLM Expected Events — Review Assistant Thin

Required substrings in stdout per mock LLM scenario.

---

## llm_valid_draft

```text
llm_request_started
llm_response_received
llm_parse_passed
draft_created
verification_passed
approval_requested
approval_granted
task_completed
decision=DELIVERED
delivered=True
```

---

## llm_malformed_output

```text
llm_request_started
llm_response_received
llm_parse_failed
task_failed
decision=FAILED
delivered=False
```

Must **not** include `approval_granted`.

---

## llm_timeout

```text
llm_request_started
llm_timeout
escalation_triggered
task_failed
decision=ESCALATED
delivered=False
```

Must **not** include `llm_response_received` or fallback draft.

---

## llm_uncertain

```text
llm_request_started
llm_response_received
llm_uncertain
escalation_triggered
task_failed
decision=ESCALATED
delivered=False
```

---

## llm_unsafe_output

```text
llm_request_started
llm_response_received
llm_unsafe_output
unsafe_action_blocked
task_failed
decision=FAILED
delivered=False
```

Must **not** reach `verification_passed` or `approval_granted`.

---

Encoded in: `evaluation/scripts/check_review_assistant_llm_mock.py`

Baseline: [prototypes-derived/review-assistant-thin/freeze/SCENARIO_BASELINE.md](../../prototypes-derived/review-assistant-thin/freeze/SCENARIO_BASELINE.md) (legacy scenarios only)
