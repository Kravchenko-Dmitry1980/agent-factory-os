# Provider Error Handling

**Phase 3.3-Plan** — safe responses for future real provider.

Global rules:

- **No infinite retry**
- **No silent fallback** to another provider or mock mid-run
- **No hallucinated fallback draft** on timeout/error
- **Escalation or fail-closed** on uncertainty
- **Retry** only with explicit limit (e.g. max 1 retry on 503 — optional, must be documented)

---

## Error matrix

| Error | Safe Response | Trace Event | Retry? |
|-------|---------------|-------------|--------|
| **Timeout** | Escalate; no draft from partial stream | `provider_timeout`, `escalation_triggered` | No |
| **Rate limit (429)** | Fail or escalate; bounded backoff if retry approved | `provider_rate_limited`, `provider_error` | Max 1 after delay — optional |
| **Provider unavailable (5xx)** | Fail closed or escalate | `provider_error` | Max 1 — optional |
| **Invalid API key** | Fail; do not retry | `provider_error` | No |
| **Auth failure (401/403)** | Fail; user must fix env | `provider_error` | No |
| **Malformed response** | Fail; no approval path | `provider_parse_failed`, `task_failed` | No |
| **Empty response** | Fail | `provider_parse_failed` | No |
| **Too long response** | Truncate reject → fail | `provider_parse_failed` | No |
| **Unsafe response** | Block | `provider_unsafe_output`, `unsafe_action_blocked` | No |
| **Network failure** | Escalate or fail | `provider_error` | Max 1 — optional |
| **Quota exceeded** | Fail; stop calls | `provider_error` | No |
| **Unknown provider error** | Fail closed | `provider_error`, `task_failed` | No |

---

## Mapping to decisions

| Outcome | Decision |
|---------|----------|
| Parse ok + verify ok + approval | DELIVERED |
| Missing approval | BLOCKED |
| Timeout / uncertain / some errors | ESCALATED |
| Parse fail / unsafe / auth fail | FAILED |

Same decision enum as v0.2 thin scenarios.

---

## Partial stream rule

If timeout mid-stream:

- Do **not** treat partial text as draft
- Do **not** pass to verification
- Emit `provider_timeout` → escalate

---

## Mock mode

Mock path continues v0.2 behavior (`llm_timeout`, etc.) — unchanged by this policy until impl merges event names.

---

## References

- [REAL_PROVIDER_FAILURE_MODES.md](REAL_PROVIDER_FAILURE_MODES.md)
- [PROVIDER_BOUNDARY_CONTRACT.md](PROVIDER_BOUNDARY_CONTRACT.md)
