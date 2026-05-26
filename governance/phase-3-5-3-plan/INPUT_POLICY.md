# Input Policy — Free-Form CLI

**Date:** 2026-05-26  
**Status:** PLAN_ONLY

Future implementation **must** enforce input policy before processing.

---

## Allowed input

| Category | Examples |
|----------|----------|
| Synthetic task text | «Summarize Q1 metrics for blog» |
| Demo task text | «Draft status message for customer demo» |
| Non-sensitive project-like text | Generic status updates, training examples |
| Short operator examples | 1–3 sentences |

Operator must confirm input is **demo-safe** before processing (future prompt).

---

## Forbidden input (without explicit governance approval)

| Category | Action |
|----------|--------|
| Client confidential data | Reject or block |
| Medical data | Reject |
| Financial / payment data | Reject |
| Real personal data (PII) | Reject |
| Credentials / passwords | Reject |
| API keys / tokens | Reject (pattern detect) |
| `.env` content | Reject |
| Repository secrets | Reject |
| Private source code (real prod) | Reject |
| Production logs | Reject |

---

## Input rules (future impl)

| Rule | Requirement |
|------|-------------|
| Max length | Required limit (plan: 500–2000 chars — pick in impl, document in freeze) |
| Empty input | **Rejected** → `INPUT_REJECTED` |
| Whitespace-only | **Rejected** |
| Secret-like patterns | Warn + block (e.g. `sk-`, `Bearer `, `api_key=`, `password=`) |
| Operator safe-data confirm | Required yes before proceed |
| Unicode | Allowed; normalize line endings |

---

## Secret-like detection (plan)

Heuristic patterns (not exhaustive):

- OpenAI-style keys: `sk-...`
- Bearer tokens
- `API_KEY`, `SECRET`, `PASSWORD` assignments
- Base64-like long blobs in suspicious context
- `.env` key=value lines

On match: **INPUT_REJECTED** or **WARNING + abort** — no processing.

---

## Sanitization for transcript

If transcript saved:

- Store operator task text only if confirmed demo-safe
- Redact detected secret patterns before save
- Never store env dump

See [TRANSCRIPT_POLICY.md](TRANSCRIPT_POLICY.md).

---

## No-execution rule

Input task text must **not** trigger:

- File writes
- HTTP calls (except explicit Mode 2 after confirmation)
- Subprocess of operator shell commands
- Email / publish / deploy

Task text is **content for review flow only**.
