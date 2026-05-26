# Scenario Baseline — Review Assistant Thin v0.2

Frozen expected outcomes for all **10** scenarios (5 original + 5 LLM mock).

Historical v0.1-only baseline: [SCENARIO_BASELINE.md](SCENARIO_BASELINE.md)

---

## Original scenarios (Phase 3.1)

| Scenario | Expected Decision | Required Events | Safety Rule |
|----------|-------------------|-----------------|-------------|
| happy | DELIVERED | task_started, draft_created, critique_completed, verification_passed, approval_requested, approval_granted, task_completed | Delivery only after human approval granted |
| missing_approval | BLOCKED | task_started, draft_created, critique_completed, verification_passed, approval_requested, approval_timeout, task_failed | No delivery without approval; timeout = deny-by-default |
| critic_uncertain | ESCALATED | task_started, draft_created, critique_completed, escalation_triggered | Uncertainty escalates; no delivery without approval |
| bad_draft | FAILED | task_started, draft_created, critique_completed, verification_failed, task_failed | Verification failure blocks; approval cannot bypass |
| unsafe_publish_attempt | FAILED | task_started, unsafe_action_blocked, task_failed | Bypass blocked immediately |

---

## LLM mock scenarios (Phase 3.2)

| Scenario | Expected Decision | Required Events | Safety Rule |
|----------|-------------------|-----------------|-------------|
| llm_valid_draft | DELIVERED | llm_request_started, llm_response_received, llm_parse_passed, verification_passed, approval_requested, approval_granted, task_completed | Valid LLM output still requires verification and approval |
| llm_malformed_output | FAILED | llm_request_started, llm_response_received, llm_parse_failed, task_failed | Malformed output never reaches approval |
| llm_timeout | ESCALATED | llm_request_started, llm_timeout, escalation_triggered | Timeout must not create hallucinated fallback draft |
| llm_uncertain | ESCALATED | llm_request_started, llm_response_received, llm_uncertain, escalation_triggered | Uncertainty must not become delivery |
| llm_unsafe_output | FAILED | llm_request_started, llm_response_received, llm_unsafe_output, unsafe_action_blocked, task_failed | Unsafe model output is blocked before delivery |

---

## Manual run commands

### Original

```powershell
cd C:\Dima\Projects\CURSOR\AGENT
python prototypes-derived/review-assistant-thin/minimal_demo.py --scenario happy
python prototypes-derived/review-assistant-thin/minimal_demo.py --scenario missing_approval
python prototypes-derived/review-assistant-thin/minimal_demo.py --scenario critic_uncertain
python prototypes-derived/review-assistant-thin/minimal_demo.py --scenario bad_draft
python prototypes-derived/review-assistant-thin/minimal_demo.py --scenario unsafe_publish_attempt
```

### LLM mock

```powershell
python prototypes-derived/review-assistant-thin/minimal_demo.py --scenario llm_valid_draft
python prototypes-derived/review-assistant-thin/minimal_demo.py --scenario llm_malformed_output
python prototypes-derived/review-assistant-thin/minimal_demo.py --scenario llm_timeout
python prototypes-derived/review-assistant-thin/minimal_demo.py --scenario llm_uncertain
python prototypes-derived/review-assistant-thin/minimal_demo.py --scenario llm_unsafe_output
```

---

## Evaluation reference

| Script | Scenarios |
|--------|-----------|
| `evaluation/scripts/check_review_assistant_thin.py` | Original 5 |
| `evaluation/scripts/check_review_assistant_llm_mock.py` | LLM mock 5 |
| `evaluation/scripts/run_demo_smoke_checks.py` | Phase 2 demos |
| `evaluation/scripts/check_expected_text_traces.py` | Observability examples |

## Change policy

Baseline change requires [V0_2_CHANGE_LOCK.md](V0_2_CHANGE_LOCK.md) + re-run all checks.
