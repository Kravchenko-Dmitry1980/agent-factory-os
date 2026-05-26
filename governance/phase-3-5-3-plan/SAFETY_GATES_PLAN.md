# Safety Gates Plan — Free-Form CLI

**Date:** 2026-05-26  
**Status:** PLAN_ONLY

Future free-form CLI **must** include these gates in order.

---

## Gate sequence

```text
1. Input safety gate
2. Mode gate
3. Draft/generation gate
4. Verification gate
5. Approval gate
6. Unsafe output gate (may overlap verification)
7. Transcript gate
8. No-execution gate (cross-cutting)
```

---

## 1. Input safety gate

| Check | Action |
|-------|--------|
| Empty input | Reject → INPUT_REJECTED |
| Secret-like patterns | Reject/warn → INPUT_REJECTED |
| Operator safe-data confirm | Required yes |
| Max length | Enforce limit |

See [INPUT_POLICY.md](INPUT_POLICY.md).

---

## 2. Mode gate

| Check | Action |
|-------|--------|
| Default | Mode 1 mock, no network |
| Mode 2 | Only if explicitly selected + confirmed + env |

See [PROVIDER_MODE_POLICY.md](PROVIDER_MODE_POLICY.md).

---

## 3. Draft / generation gate

| Check | Action |
|-------|--------|
| Mock path | Generate advisory draft from task |
| Provider path | Parse response; malformed → FAILED |
| LLM/provider output | Treat as unverified |

---

## 4. Verification gate

| Check | Action |
|-------|--------|
| Basic safety checks | Pass required for delivery path |
| Fail | → FAILED, no delivery |

---

## 5. Approval gate

| Check | Action |
|-------|--------|
| Prompt | Approve? yes/no, default no |
| No approval | → BLOCKED |
| See [APPROVAL_MODEL_PLAN.md](APPROVAL_MODEL_PLAN.md) | |

---

## 6. Unsafe output gate

| Check | Action |
|-------|--------|
| Bypass / command / unsafe patterns | unsafe_action_blocked |
| Unsafe even if operator says yes | No delivery |

---

## 7. Transcript gate

| Check | Action |
|-------|--------|
| Default | No save |
| `--save-transcript` | Sanitized content only |
| Secrets | Never save |

See [TRANSCRIPT_POLICY.md](TRANSCRIPT_POLICY.md).

---

## 8. No-execution gate

Task text and draft must **not** cause:

- External API calls (except Mode 2 after confirmation)
- File system writes (except optional transcript with flag)
- Publish / send / deploy
- Arbitrary subprocess

Input is **review demo content only**.

---

## Visibility

All gate outcomes visible in:

- SAFETY GATES section (RU summary)
- TRACE events
- Safety status line

See [TRACE_PLAN.md](TRACE_PLAN.md), [OUTPUT_FORMAT_RU.md](OUTPUT_FORMAT_RU.md).
