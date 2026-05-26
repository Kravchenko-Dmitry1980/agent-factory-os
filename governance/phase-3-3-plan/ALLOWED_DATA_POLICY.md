# Allowed Data Policy

**Phase 3.3-Plan** — what may be sent to a future real provider.

---

## Allowed by default (first live tests)

| Data type | Example | Condition |
|-----------|---------|-----------|
| Synthetic demo task | "Review this sample paragraph for clarity." | Fixed scenario text in repo |
| Non-sensitive test text | Lorem-style or public-domain snippets | No PII |
| Short draft text | ≤ N tokens; predefined in scenario | Bounded size |
| Non-private examples | Public README excerpts (explicitly listed) | Pre-approved list in eval |
| Approved prompt content | Template-bound system + user prompt | Versioned in impl |

---

## Requires explicit written approval (before send)

| Data type | Why gated |
|-----------|-----------|
| User-provided project data | IP / confidentiality |
| Business documents | Confidential |
| Meeting notes | PII / confidential |
| Medical text | Sensitive category |
| Personal data | Privacy law |
| Client data | Contractual |
| Source code (repo) | IP; may contain secrets |
| Secrets-like text | Even "test keys" teach bad habits |

---

## First real provider test rule

# No sensitive data in first real provider test.

Use only:

- Scenario-driven synthetic strings (like v0.2 mock)
- Explicitly listed public snippets
- No user paste buffer
- No workspace file reads for provider input

---

## Pre-send checklist (future impl)

1. Data class identified (public / synthetic / approved-other)
2. Prompt length within cap
3. No forbidden patterns (see [FORBIDDEN_DATA_POLICY.md](FORBIDDEN_DATA_POLICY.md))
4. Redaction applied if mixed content
5. Trace logs payload hash or length — not full sensitive text

---

## Operator rule

If unsure whether data may be sent → **do not send**. Use mock mode.
