# Demo Runner v0.1 — Transcript Policy

**Version:** demo-runner-v0.1  
**Date:** 2026-05-26  
**Status:** FROZEN

Operator-facing RU copy: [../TRANSCRIPT_POLICY_RU.md](../TRANSCRIPT_POLICY_RU.md)

---

## Default

**Transcript saving is disabled by default.**

Runner does not write files unless `--save-transcript` is passed.

---

## Enable condition

```powershell
python demos/review-assistant-runner/demo_runner.py --scenario happy --save-transcript
```

Output directory: `demos/review-assistant-runner/transcripts/`  
Filename pattern: `YYYYMMDD_HHMMSS_<scenario>.md`

---

## Allowed transcript contents

| Field | Allowed |
|-------|---------|
| Timestamp | yes |
| Scenario name / title | yes |
| Command (argv, no env) | yes |
| Raw stdout | yes |
| Parsed decision | yes |
| Parsed trace events | yes |
| Russian summary | yes |
| Safety status | yes |
| PASS/FAIL (validation items) | yes |

---

## Forbidden transcript contents

| Field | Forbidden |
|-------|-----------|
| Environment variables | yes |
| `.env` contents | yes |
| API keys / tokens | yes |
| Auth headers | yes |
| `RA_LLM_BASE_URL` value | yes (for real provider runs) |
| Private user data | yes |
| stderr with secrets | yes |

For `real_provider_synthetic`: save scenario key only; do not save provider URL or credentials.

---

## Secret safety rules

- Runner must not dump `os.environ`
- Runner must not print API keys
- Runner must not require API key for menu items 1–8, 10–15
- Transcript markdown is operator-local artifact — not committed with secrets

---

## Change rule

Any change to transcript saving requires transcript safety review + validation + explicit approval.

See [DEMO_RUNNER_V0_1_CHANGE_LOCK.md](DEMO_RUNNER_V0_1_CHANGE_LOCK.md).
