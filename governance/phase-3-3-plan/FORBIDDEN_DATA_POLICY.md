# Forbidden Data Policy

**Phase 3.3-Plan** — never send without explicit written approval and separate governance phase.

---

## Forbidden categories

| Category | Examples |
|----------|----------|
| API keys | Any provider or service key |
| Passwords | User, admin, service |
| Tokens | OAuth, JWT, session, bot tokens |
| Private keys | SSH, TLS, signing keys |
| Credentials | Connection strings with secrets |
| Personal identifiers | Names+contact, government IDs, emails in bulk |
| Medical records | PHI, diagnoses, prescriptions |
| Financial records | Account numbers, transactions, tax data |
| Client confidential data | Contracts, unreleased product plans |
| Internal business documents | Unless explicit approval workflow |
| Full repository content | Entire codebase to cloud |
| `.env` files | Always |
| Logs containing secrets | Stack traces with auth headers |
| Proprietary model weights | Binary blobs |
| Private datasets | Customer data exports |

---

## Prompt injection carriers

Forbidden to forward unreviewed:

- Raw user HTML/markdown with embedded instructions
- Untrusted file contents from disk
- Gateway/message payloads (N/A now — no gateways)

---

## Default rule

# If unsure, do not send.

Use mock mode. Escalate to human lead for data class decision.

---

## Trace rule

Traces must not contain forbidden data categories — even on failure. Log event names + safe metadata only.

---

## Violation response

1. Stop provider calls immediately
2. Rotate compromised credentials if any secret was sent
3. Rollback per [REAL_PROVIDER_ROLLBACK_PLAN.md](REAL_PROVIDER_ROLLBACK_PLAN.md)
4. Document incident in governance
