# Real Provider Expected Events

Required stdout substrings per scenario.

---

## real_provider_forbidden_without_flag

```text
provider_request_prepared
provider_disabled
task_failed
decision=FAILED
delivered=False
```

Must **not** include `provider_request_started`.

---

## real_provider_missing_config

```text
provider_request_prepared
provider_config_missing
task_failed
decision=FAILED
delivered=False
```

Must **not** include `provider_request_started`.

Run with `--real-provider` and `RA_LLM_BASE_URL` unset.

---

## real_provider_synthetic (success path)

```text
provider_request_prepared
provider_request_started
provider_response_received
provider_parse_passed
draft_created
verification_passed
approval_requested
approval_granted
task_completed
decision=DELIVERED
delivered=True
```

Requires `--real-provider` and valid `RA_LLM_BASE_URL`.

---

## real_provider_synthetic (failure paths)

One of:

```text
provider_timeout
escalation_triggered
```

```text
provider_error
task_failed
```

```text
provider_parse_failed
task_failed
```

```text
provider_unsafe_output
unsafe_action_blocked
```

No delivery without verification + approval.

---

Encoded in: `evaluation/scripts/check_review_assistant_real_provider_contract.py`
