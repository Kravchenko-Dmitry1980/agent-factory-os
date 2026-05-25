# Local Evaluation Policy

---

## Policy Statement

All Phase 2.5 evaluation runs **on the developer machine** using existing demos and text traces. No external service is required for default checks.

---

## Default Mode

| Component | Default |
|-----------|---------|
| LLM adapter | mock |
| Telegram gate | mock |
| Queue worker | local SQLite in `.data/` |
| Scripts | stdlib + subprocess only |
| Credentials | optional, never required for smoke |

---

## When Real Mode Is Allowed

Human may run `--real` with credentials for **manual** adapter exploration. Results are not committed as automated baselines.

---

## Data Handling

- Traces may be saved locally in `evaluation/reports/` (gitignored optional)
- Do not commit API keys or live Telegram content
- `integrations-real/.data/` remains gitignored

---

## Review Frequency

| Change type | Minimum evaluation |
|-------------|-------------------|
| Docs only in evaluation/ | self-review |
| Demo behavior change | scenarios + smoke + trace compare |
| Shared gates/audit | full smoke + all quality gates |
| New adapter | adapter scenarios + prototype equivalent |

---

## Escalation

If local check FAILs and cause unclear → rollback first (`evolution/rollback-thinking/`), then investigate.
