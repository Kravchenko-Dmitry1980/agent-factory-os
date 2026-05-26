# LLM Security Review — Phase 3.2 Plan

**Scope:** Future LLM adapter boundary — planning only

---

## Threats

| Threat | Description |
|--------|-------------|
| Prompt injection | Task text overrides system instructions |
| Secret leakage | API keys or PII in prompts/logs |
| Unsafe instructions | Model output suggests destructive actions |
| Over-trusting model | Skipping verification/approval because "LLM said so" |
| Provider errors | Misconfigured client, wrong endpoint |
| Sensitive logging | Full prompts/responses in public traces |
| Cloud data exposure | Sending private data to external model without approval |
| Command execution | Treating model output as shell/API commands |
| Hidden tool-use | Model suggests MCP/tools not in allowlist |

---

## Rules (binding for future impl)

| Rule | Requirement |
|------|-------------|
| No secrets in prompts | Load from env only in real mode; never trace secrets |
| No unrestricted tools | Adapter returns text only — no tool executor |
| No command execution from LLM output | Parse text for display; never eval/exec |
| No raw sensitive data to cloud | Default mock; real mode requires explicit approval |
| No external provider by default | `provider_mode=mock` unless flag + approval |
| Mock-first | All security scenarios testable offline |
| Redact traces | Log event names + hashes, not full private content |
| Fail-closed on injection signals | Policy stub blocks obvious injection patterns (mock testable) |

---

## Real provider gate (future)

Before any OpenAI/external call:

1. User explicit approval in writing
2. `.env` / env vars documented — not committed
3. Security review sign-off
4. Rate limit + timeout configured
5. Rollback plan active

**Phase 3.2-Plan:** no API calls, no keys, no real provider code.

---

## References

- [LLM_FAILURE_MODES.md](LLM_FAILURE_MODES.md)
- [NO_RUNTIME_NO_FACTORY_POLICY.md](NO_RUNTIME_NO_FACTORY_POLICY.md)
- `agent-builder-kit/template-specs/tool-boundary-spec.md`

---

## Review cadence

| When | Action |
|------|--------|
| Before mock impl | This document acknowledged |
| Before real provider | Separate security sign-off |
