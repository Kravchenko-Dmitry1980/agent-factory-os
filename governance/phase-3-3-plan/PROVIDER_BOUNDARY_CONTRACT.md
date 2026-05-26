# Provider Boundary Contract

**Phase 3.3-Plan** — future normative contract. **Not implemented in plan phase.**

Extends mock v0.2 chain. Provider output is **untrusted** — same as mock.

---

## Inputs

| Field | Required | Notes |
|-------|----------|-------|
| `task_text` | yes | Bounded length; redacted per data policy |
| `prompt_template` | yes | Fixed template version; no user secrets embedded |
| `provider_mode` | yes | `mock` (default) \| `real` (opt-in) |
| `timeout_seconds` | yes | Bounded (e.g. 30s default, max 120s) |
| `max_output_tokens` / size cap | yes | Prevent unbounded response |
| `safe_context_only` | yes | Must pass allowed-data check before send |

---

## Outputs

| Field | Notes |
|-------|-------|
| `raw_provider_response` | Unverified; never used as truth |
| `parsed_response` | Structured draft/critique fields if parse ok |
| `parse_status` | ok \| malformed \| empty \| unsafe \| uncertain |
| `error_status` | none \| timeout \| rate_limit \| auth \| network \| provider_unknown |
| `safety_flags` | unsafe \| uncertain \| injection_suspect |
| `trace_events` | See [REAL_PROVIDER_TRACE_PLAN.md](REAL_PROVIDER_TRACE_PLAN.md) |

---

## Required states (trace-aligned)

| State | Meaning |
|-------|---------|
| `PROVIDER_REQUEST_PREPARED` | Data policy check passed; prompt bounded |
| `PROVIDER_REQUEST_STARTED` | Request initiated (real: network call begins) |
| `PROVIDER_RESPONSE_RECEIVED` | Raw response available |
| `PROVIDER_PARSE_PASSED` | Structured parse ok |
| `PROVIDER_PARSE_FAILED` | Cannot use output |
| `PROVIDER_TIMEOUT` | Deadline exceeded |
| `PROVIDER_ERROR` | Provider/API error |
| `PROVIDER_UNSAFE_OUTPUT` | Policy block |
| `PROVIDER_UNCERTAIN_OUTPUT` | Low confidence / hedge language |

Legacy v0.2 events (`llm_*`) may map 1:1 for mock mode compatibility.

---

## Safe behavior (mandatory)

| Rule | Enforcement |
|------|-------------|
| Provider output is untrusted | Always parse + verify |
| Parse failure blocks | → `task_failed`; no approval |
| Timeout escalates | → `escalation_triggered`; **no hallucinated fallback draft** |
| Provider error escalates or fails closed | No silent retry loop |
| Unsafe output blocks | → `unsafe_action_blocked` or fail |
| Uncertain output escalates | No auto-delivery |
| Valid parse still → verification | `verification_passed` required |
| Verification still → approval | `approval_granted` before `task_completed` |
| No auto-publish | Delivery flag only after both gates |

---

## Conceptual interface (future — not a framework)

```text
provider_boundary.request(task, mode=mock|real) → ProviderResult
```

Single module. No plugin registry. No `Provider` ABC with N implementations in Phase 3.3.

---

## References

- Frozen template: `agent-builder-kit/templates/review-assistant-agent/`
- Mock baseline: `prototypes-derived/review-assistant-thin/freeze/V0_2_LLM_BOUNDARY_BASELINE.md`
- Failure modes: [REAL_PROVIDER_FAILURE_MODES.md](REAL_PROVIDER_FAILURE_MODES.md)
