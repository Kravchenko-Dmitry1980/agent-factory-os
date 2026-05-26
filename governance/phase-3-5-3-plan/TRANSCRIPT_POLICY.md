# Transcript Policy — Free-Form CLI

**Date:** 2026-05-26  
**Status:** PLAN_ONLY

Aligned with Demo Runner v0.1 [TRANSCRIPT_POLICY](../../demos/review-assistant-runner/freeze/DEMO_RUNNER_V0_1_TRANSCRIPT_POLICY.md).

---

## Default

**No transcript saved.**

---

## Enable condition

Explicit flag only (plan):

```powershell
python demos/review-assistant-freeform/free_form_cli.py --save-transcript
```

Output: `demos/review-assistant-freeform/transcripts/YYYYMMDD_HHMMSS_freeform.md`

---

## Allowed contents

| Field | Allowed |
|-------|---------|
| Timestamp | yes |
| Sanitized input preview | yes (redact secrets) |
| Mode | yes |
| Final decision | yes |
| Trace events | yes |
| Russian summary | yes |
| Safety status | yes |
| Command argv | yes (no env) |

---

## Forbidden contents

| Field | Forbidden |
|-------|-----------|
| Secrets / API keys | yes |
| `.env` | yes |
| Auth headers | yes |
| Full provider config / RA_LLM_BASE_URL value | yes |
| Environment dump | yes |
| Private data not confirmed demo-safe | yes |

---

## Real provider mode

If Mode 2 used: save mode name and decision only; **do not** save endpoint URL or tokens.

---

## Change rule

Transcript behavior change requires transcript safety review + freeze update (future v0.1 freeform freeze).
