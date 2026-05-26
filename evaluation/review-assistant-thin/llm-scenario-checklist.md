# LLM Scenario Checklist — Review Assistant Thin

| Scenario | Command | Expected decision | Required events | Pass criteria |
|----------|---------|-------------------|-----------------|---------------|
| llm_valid_draft | `... --scenario llm_valid_draft` | DELIVERED | llm_request_started, llm_parse_passed, verification_passed, approval_granted, task_completed | exit 0; delivered=True |
| llm_malformed_output | `... --scenario llm_malformed_output` | FAILED | llm_parse_failed, task_failed | exit 0; no approval_granted |
| llm_timeout | `... --scenario llm_timeout` | ESCALATED | llm_timeout, escalation_triggered, task_failed | exit 0; no draft from timeout |
| llm_uncertain | `... --scenario llm_uncertain` | ESCALATED | llm_uncertain, escalation_triggered | exit 0; delivered=False |
| llm_unsafe_output | `... --scenario llm_unsafe_output` | FAILED | llm_unsafe_output, unsafe_action_blocked | exit 0; delivered=False |

## Automated

```powershell
python evaluation/scripts/check_review_assistant_llm_mock.py
```

Expected: `Summary: PASS=5 FAIL=0`

## Regression

```powershell
python evaluation/scripts/check_review_assistant_thin.py
python evaluation/scripts/run_demo_smoke_checks.py
python evaluation/scripts/check_expected_text_traces.py
```
