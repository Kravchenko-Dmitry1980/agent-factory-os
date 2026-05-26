# Contracts — Review Assistant Thin

## Inputs

| Field | Type | Required |
|-------|------|----------|
| `--scenario` | enum | yes (CLI) |
| `task` | string | yes (from scenario config) |

Scenarios: `happy`, `missing_approval`, `critic_uncertain`, `bad_draft`, `unsafe_publish_attempt`, `llm_valid_draft`, `llm_malformed_output`, `llm_timeout`, `llm_uncertain`, `llm_unsafe_output`

## LLM input contract (mock)

| Field | Type | Notes |
|-------|------|-------|
| `scenario` | string | Selects mock payload |
| Mock dict | `{status, draft, critique, uncertain, unsafe}` | Local only |

## LLM output contract (mock)

| Field | Type | Verified |
|-------|------|----------|
| `raw` | dict | no |
| `parsed draft` | string | no — until verification |
| `parse_status` | ok / fail | gate |

## Parse failure states

`missing_payload`, `invalid_shape`, `unsupported_status`, `missing_draft`, `wrong_draft_type`, `empty_output`, `wrong_critique_type`

Trace: `llm_parse_failed`

## Outputs

| Field | Type | When |
|-------|------|------|
| `draft_id` | string | after draft |
| `draft_text` | string | after draft |
| `critique` | OK \| UNCERTAIN \| BAD_DRAFT | advisory |
| `verification_passed` | bool | after verification |
| `approval_status` | string | after approval gate |
| `final_decision` | DELIVERED \| BLOCKED \| ESCALATED \| FAILED | terminal |
| `delivered` | bool | terminal |
| `trace` | list of events | always |

## States

RECEIVED → DRAFTED → CRITIQUED → VERIFIED → APPROVAL_REQUESTED → terminal

Terminal: COMPLETED (delivered), FAILED, BLOCKED, ESCALATED

## Decisions

| Decision | Condition |
|----------|-----------|
| DELIVERED | verification passed + approval granted + no bypass |
| BLOCKED | approval missing/timeout/denied |
| ESCALATED | critic uncertain + no approval |
| FAILED | verification failed or unsafe bypass |

## Trace events

**Core:** `task_started`, `draft_created`, `critique_completed`, `verification_passed`, `verification_failed`, `approval_requested`, `approval_granted`, `approval_denied`, `approval_timeout`, `escalation_triggered`, `unsafe_action_blocked`, `task_completed`, `task_failed`

**LLM mock (Phase 3.2):** `llm_request_started`, `llm_response_received`, `llm_parse_passed`, `llm_parse_failed`, `llm_timeout`, `llm_uncertain`, `llm_unsafe_output`

**Real provider (Phase 3.3):** `provider_request_prepared`, `provider_disabled`, `provider_config_missing`, `provider_request_started`, `provider_response_received`, `provider_parse_passed`, `provider_parse_failed`, `provider_timeout`, `provider_error`, `provider_rate_limited`, `provider_unsafe_output`, `provider_uncertain_output`

## Real provider contract (Phase 3.3)

| Input | Notes |
|-------|-------|
| `task_text` | Synthetic only for real mode |
| `provider_mode` | real only with `--real-provider` |
| `RA_LLM_BASE_URL` | Required for network |
| `RA_LLM_API_KEY` | Optional |
| `RA_LLM_MODEL` | Optional |

| Output state | Meaning |
|--------------|---------|
| PROVIDER_DISABLED | No `--real-provider` flag |
| PROVIDER_CONFIG_MISSING | Missing base URL |
| PROVIDER_PARSE_FAILED | Malformed live response |
| PROVIDER_TIMEOUT | Escalate, no fallback draft |
| PROVIDER_ERROR | Fail closed |

## Failure states

| State | Trigger |
|-------|---------|
| VERIFICATION_FAILED | empty/bad draft |
| APPROVAL_BLOCKED | timeout, missing, denied |
| UNSAFE_BLOCKED | bypass attempt |
| LLM_PARSE_FAILED | malformed mock payload |
| LLM_TIMEOUT | mock timeout — no fallback draft |
| LLM_UNSAFE | unsafe mock content |
| LLM_UNCERTAIN | uncertain flag — escalate |
| PROVIDER_DISABLED | real flag not set |
| PROVIDER_CONFIG_MISSING | RA_LLM_BASE_URL missing |
| PROVIDER_PARSE_FAILED | live response invalid |
| PROVIDER_TIMEOUT | network timeout — escalate |
| PROVIDER_UNSAFE | unsafe live content |

Aligned with frozen template and `prototypes/review-loop-agent/contracts.md` (reference).
