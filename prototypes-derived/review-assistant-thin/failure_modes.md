# Failure Modes — Review Assistant Thin

| Failure | Symptom | Guard in impl |
|---------|---------|---------------|
| Critic treated as truth | Delivery on critique OK without approval | approval gate after verification |
| Missing approval bypass | Delivery without approval_granted | apply_approval + fail-closed |
| Bad draft delivered | Empty draft reaches user | verification_failed on empty |
| Trace missing | No TRACE block | print_trace always called |
| Unsafe publish | Bypass succeeds | unsafe_publish_attempt → unsafe_action_blocked first |
| Runtime drift | shared/, factory/, registry/ appear | forbidden by governance — single script |
| Auto-publish on timeout | delivery after timeout | timeout → task_failed, delivered=False |
| Uncertainty auto-resolved | delivery on UNCERTAIN without approval | escalation + no grant in scenario |
| Malformed LLM output | parse fail reaches approval | llm_parse_failed → task_failed |
| LLM timeout fallback | draft after timeout | llm_timeout only; no llm_response_received |
| Unsafe LLM output | destructive text delivered | llm_unsafe_output + unsafe_action_blocked |
| Over-trusting model | skip verification after llm_parse | verification still required |
| Prompt injection style | "ignore rules" in draft | unsafe flag in mock; real TBD |
| Hidden command suggestion | shell cmd in LLM text | unsafe_action_blocked in llm_unsafe scenario |
| Key leakage | API key in trace/log | env-only; never print RA_LLM_* values |
| Provider timeout fallback | draft after live timeout | provider_timeout → escalate; no draft |
| Malformed live response | bad JSON from endpoint | provider_parse_failed |
| Provider output as command | execute model text | blocked; no subprocess from provider |
| Approval bypass via provider | model says "approved" | approval_granted only from scenario gate |
| Real call by default | network without flag | provider_disabled |

## Operator checks

1. Every run prints `TRACE` section
2. Only `happy`, `llm_valid_draft`, and live `real_provider_synthetic` may have `delivered=True`
3. Critic/LLM lines marked advisory / unverified

## If failure observed

See [rollback.md](rollback.md) — do not patch frozen specs or prototypes.
