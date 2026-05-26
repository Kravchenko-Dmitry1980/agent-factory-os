# Data Safety Policy — Phase 3.4

**Purpose:** Data rules for future provider safety harness and synthetic test fixtures.

---

## Allowed

| Data type | Examples |
|-----------|----------|
| Synthetic prompts | Fictional project names, dummy tasks |
| Fake examples | "Project Alpha status on track" |
| Dummy placeholders | `FAKE_CLIENT_NAME`, `SYNTHETIC_NOTE_001` |
| Local-only neutral text | Generic review/summary requests |
| Harness-generated traces | No real payloads |

---

## Forbidden

| Data type | Reason |
|-----------|--------|
| Real client data | Privacy |
| Medical records | PHI |
| Financial data | PII/sensitivity |
| Credentials | Secrets |
| Source code from private repos | IP/leakage |
| Private documents | Confidentiality |
| Production logs | May contain secrets/PII |
| `.env` files or contents | Secrets |
| Secrets of any kind | [SECRET_SAFETY_POLICY.md](SECRET_SAFETY_POLICY.md) |
| Private datasets | Uncontrolled sensitivity |
| Repository content as test input | Use synthetic shapes only |

---

## Rule

> **If data might be sensitive, do not test it.**

When in doubt → use placeholder from [SAFE_SYNTHETIC_TEST_SET.md](SAFE_SYNTHETIC_TEST_SET.md).

---

## Real provider mode (future)

Even with local LM Studio:

- Prompts must remain synthetic
- Do not paste real emails, tickets, or code reviews into harness
- Traces must not capture real user data

---

## Alignment

- [../phase-3-3-plan/ALLOWED_DATA_POLICY.md](../phase-3-3-plan/ALLOWED_DATA_POLICY.md)
- [../phase-3-3-plan/FORBIDDEN_DATA_POLICY.md](../phase-3-3-plan/FORBIDDEN_DATA_POLICY.md)
- [../phase-3-3-livecheck/NO_CLOUD_NO_SECRETS_POLICY.md](../phase-3-3-livecheck/NO_CLOUD_NO_SECRETS_POLICY.md)

---

## Violation response

Using real sensitive data in harness → **immediate NO-GO** for impl; rollback if discovered post-merge.
