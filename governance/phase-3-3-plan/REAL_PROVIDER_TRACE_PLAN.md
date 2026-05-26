# Real Provider Trace Plan

**Phase 3.3-Plan** — future trace events for real provider path.

Human-readable stdout traces (same style as v0.2). **No secrets. No telemetry backend.**

---

## Required future trace events

| Event | When |
|-------|------|
| `provider_request_prepared` | Data policy check passed; prompt ready |
| `provider_request_started` | Request sent (real: network begins) |
| `provider_response_received` | Raw response available |
| `provider_parse_passed` | Parse ok |
| `provider_parse_failed` | Parse failed |
| `provider_timeout` | Deadline exceeded |
| `provider_error` | API/provider error |
| `provider_rate_limited` | 429 or equivalent |
| `provider_unsafe_output` | Safety block |
| `provider_uncertain_output` | Uncertainty escalation path |
| `verification_passed` | Verification gate ok |
| `verification_failed` | Verification gate fail |
| `approval_requested` | Human approval needed |
| `approval_granted` | Human approved |
| `approval_denied` | Human denied (if scenario) |
| `approval_timeout` | Timeout deny (if scenario) |
| `task_completed` | Successful terminal |
| `task_failed` | Failed terminal |
| `escalation_triggered` | Escalation path |
| `unsafe_action_blocked` | Bypass blocked |

---

## Mock mode compatibility

When `--provider-mode mock`, emit existing `llm_*` events OR alias to `provider_*` — impl must document mapping. Eval scripts must accept chosen baseline.

---

## Trace rules

| Rule | Detail |
|------|--------|
| Human-readable | Line-oriented stdout |
| No secrets | No keys, Authorization, env values |
| No raw auth headers | Ever |
| No full sensitive payloads | Log length/hash optional |
| No telemetry backend | No PostHog/analytics (Hermes rejected) |
| Decision line | `decision=DELIVERED|FAILED|ESCALATED|BLOCKED` |
| Delivery flag | `delivered=True|False` |

---

## Forbidden in trace

- API key substrings
- Full provider JSON with embedded secrets
- User PII in first tests (use synthetic)

---

## Example shape (illustrative — not live output)

```text
provider_request_prepared
provider_request_started
provider_response_received
provider_parse_passed
verification_passed
approval_requested
approval_granted
task_completed
decision=DELIVERED
delivered=True
```

---

## Observability alignment

Map to canonical events where possible: `observability/event-taxonomy/canonical-events.md`

Phase 2 trace examples remain valid for review-loop demos — unchanged in plan phase.

---

## References

- Phase 3.2: [../phase-3-2-plan/LLM_TRACE_PLAN.md](../phase-3-2-plan/LLM_TRACE_PLAN.md)
- v0.2 LLM events: `evaluation/review-assistant-thin/llm-expected-events.md`
