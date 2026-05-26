# Real Provider Security Review

**Phase 3.3-Plan** — security gates before any implementation.

---

## Topics

### Data privacy

- Cloud providers: task text leaves machine → data class approval required
- Local endpoints: lower egress risk; still log discipline
- Provider retention/training policy must be reviewed per vendor

### Secret leakage

- Env-only keys; no trace/logging (see [SECRET_HANDLING_POLICY.md](SECRET_HANDLING_POLICY.md))
- Hermes lesson: plaintext `.env` on disk — minimize exposure window

### Prompt injection

- User/task text may contain adversarial instructions
- Provider output may contain injection
- Gates must be **code-enforced**, not prompt-only

### Provider trust

- Provider is untrusted transport + untrusted generator
- No "official model said safe" shortcut

### Provider logs

- Vendor may log prompts — assume yes for cloud unless DPA says otherwise
- Our traces: no secrets, minimal payload

### Compliance / legal

- Separate review for cloud (OpenAI) vs RU providers
- Not completed in plan phase — required at impl approval

### Cost exposure

- Rate limits + quota caps
- Fail on quota exceeded; no retry storm
- Optional: max calls per demo session

### Retry abuse

- Bounded retries only
- No loop on 401/403

### Output used as command

- Forbidden: executing provider text
- Forbidden: passing to subprocess without approval gate

### Hidden external action

- No webhooks, gateways, MCP from provider path in Phase 3.3

### Cloud vs local tradeoff

| | Local OpenAI-compatible | Cloud API |
|---|---------------------------|-----------|
| Privacy | Better for lab | Weaker |
| Setup | Operator burden | Lower |
| First test | Preferred direction | Needs explicit cloud approval |

### RU provider considerations

- Data residency expectations
- API stability; fork vs official docs
- See [RU_PROVIDER_FUTURE_BACKLOG.md](RU_PROVIDER_FUTURE_BACKLOG.md)
- Hermes RU findings **research-only**

---

## Security gate checklist (before real provider impl)

| Item | Approved at plan? | Required at impl |
|------|-------------------|------------------|
| Provider selected | **No** — deferred | yes |
| Data class approved | plan defines policy | yes |
| Key handling approved | plan defines policy | yes |
| Timeout policy approved | yes (in error doc) | yes |
| Logging policy approved | yes (secret doc) | yes |
| Trace policy approved | yes (trace plan) | yes |
| Rollback plan approved | yes | yes |
| Evaluation scenarios selected | outlined | yes |
| Mock remains default | yes | yes |
| No provider framework | yes | yes |
| No sensitive first test | yes | yes |
| Baseline checks PASS | N/A (no impl) | yes |

---

## Verdict (plan phase)

Security **planning complete**. Implementation **not authorized** until checklist signed at impl gate.

---

## References

- [../phase-3-2-plan/LLM_SECURITY_REVIEW.md](../phase-3-2-plan/LLM_SECURITY_REVIEW.md)
- [../phase-3-2-2/SECURITY_AND_PROVIDER_RISK_REGISTER.md](../phase-3-2-2/SECURITY_AND_PROVIDER_RISK_REGISTER.md)
