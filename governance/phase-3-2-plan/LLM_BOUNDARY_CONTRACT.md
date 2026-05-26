# LLM Boundary Contract — Phase 3.2 (Future)

**Normative for:** future mock/real LLM adapter — **not implemented in Phase 3.2-Plan**

---

## Inputs

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `task_text` | string | yes | User task |
| `prompt_type` | enum | yes | `draft` \| `critique` |
| `scenario_mode` | string | no | mock behavior selector |
| `mock_response` | string | no | Inject for tests |
| `timeout_seconds` | number | no | Default bounded (e.g. 30) |
| `provider_mode` | enum | yes | `mock` (default) \| `real` (opt-in) |

---

## Outputs

| Field | Type | Notes |
|-------|------|-------|
| `raw_output` | string | Unverified model text |
| `parsed_draft` | string | optional |
| `parsed_critique` | string | optional |
| `confidence` | enum | `high` \| `low` \| `unknown` |
| `uncertainty_flag` | bool | Triggers escalation path |
| `parse_status` | enum | `ok` \| `malformed` \| `empty` \| `unsafe` |
| `failure_reason` | string | When parse_status != ok |

---

## Required failure states

| State | Meaning |
|-------|---------|
| `timeout` | Provider/mock exceeded deadline |
| `malformed_output` | Cannot parse expected shape |
| `empty_output` | Zero usable content |
| `unsafe_output` | Policy block (instructions, secrets request) |
| `uncertain_output` | Model expresses or heuristic detects uncertainty |
| `schema_mismatch` | Structured parse failed |
| `provider_error` | Real provider failure (future) |

Map to trace: `llm_timeout`, `llm_malformed_output`, `llm_uncertain`, `llm_unsafe_output`

---

## Required safe behavior

| Rule | Enforcement |
|------|-------------|
| Malformed output rejected | No pass to delivery; verification_failed |
| Timeout blocks or escalates | fail-closed; no partial auto-delivery |
| Uncertain output escalates | escalation_triggered; human required |
| Unsafe output blocks | unsafe_action_blocked or verification_failed |
| LLM never bypasses verification | Adapter output → verification gate only |
| LLM never bypasses human approval | approval_requested before delivery |
| Raw output never logged with secrets | Redact in trace detail |

---

## Adapter interface (conceptual)

```text
llm_adapter.request(task, prompt_type, mode=mock) → LLMResult
```

No plugin registry. No multi-provider router in Phase 3.2 scope.

---

## References

- `observability/event-taxonomy/canonical-events.md`
- Frozen [human-approval.md](../../agent-builder-kit/templates/review-assistant-agent/human-approval.md)
- [LLM_FAILURE_MODES.md](LLM_FAILURE_MODES.md)
