# Secret Handling Policy

**Phase 3.3-Plan** — applies to future real provider implementation.

---

## API key rules

| Rule | Detail |
|------|--------|
| Never commit key | No repo, no PR, no gist |
| Never print key | stdout, stderr, trace |
| Never log key | Including debug level |
| Never paste key into prompts | Model must not receive its own key |
| Load from env only | e.g. `REVIEW_ASSISTANT_PROVIDER_API_KEY` (name TBD at impl) |
| No real `.env` in repo | Plan phase: no `.env` files created |
| `.env.example` | Placeholder only **if** impl phase approves; values like `YOUR_KEY_HERE` |

---

## Environment variable rules (future)

- One variable per approved provider
- Document name in impl README — not the value
- User sets locally; never in CI logs
- Optional: refuse to start real mode if env var missing (fail-closed)

---

## Logging rules

| Do | Don't |
|----|-------|
| Log `provider_mode=real` | Log Authorization header |
| Log `provider_error=auth_failed` | Log full request/response bodies with secrets |
| Log response length / parse status | Log env dump |
| Redact URLs with embedded tokens | Log `os.environ` |

---

## Storage rules

| Location | Allowed |
|----------|---------|
| Process env (runtime) | yes — user-provided |
| Repo markdown | **no** |
| Trace files | **no** |
| Screenshots / docs | **no** |
| Credential pools | **no** (Hermes pattern rejected) |
| OS keychain | Research for much later — not Phase 3.3 |

---

## Code review gate (future impl)

Reviewer checks:

- [ ] No string literals matching key patterns
- [ ] No `print(environ)` or debug dumps
- [ ] HTTP client does not log headers
- [ ] Error messages don't echo key

---

## Leak response

See [REAL_PROVIDER_ROLLBACK_PLAN.md](REAL_PROVIDER_ROLLBACK_PLAN.md) — rotate key, disable real mode, incident doc.

---

## Plan phase compliance

This document created **without** any API keys, `.env` files, or secret placeholders in repo.
