# Demo Runner v0.1 — Real Provider Policy

**Version:** demo-runner-v0.1  
**Date:** 2026-05-26  
**Status:** FROZEN

---

## Scope

Menu item **9**: `real_provider_synthetic`

---

## Policy

| Rule | Value |
|------|-------|
| Menu position | Item 9 (Real Local Provider group) |
| Run by default | **no** |
| Requires explicit selection | **yes** (menu or `--scenario real_provider_synthetic`) |
| Requires operator confirmation | **yes** — must type `yes` |
| Requires `RA_LLM_BASE_URL` | **yes** |
| Synthetic data only | **yes** — scenario uses synthetic prompt in thin demo |
| Cloud provider | **must not** use OpenAI cloud / GigaChat / YandexGPT |
| Secrets in runner | **must not** print, log, or save |
| Transcript | must not save env values or API keys |

---

## Default behavior

**No real provider call.**

On startup, interactive menu, or `--list` — no network to LM Studio/Ollama.

Cancel path: anything except `yes` → «Real provider scenario cancelled» → no command run.

Missing `RA_LLM_BASE_URL` → runner explains how to set env → no command run.

---

## Warning text (frozen behavior)

Runner shows before confirmation:

```text
ВНИМАНИЕ: этот сценарий вызывает локальный OpenAI-compatible endpoint.

Проверьте:
- LM Studio или Ollama запущен локально
- RA_LLM_BASE_URL задан
- используется synthetic data only
- cloud provider не используется
- секреты не передаются

Продолжить? yes/no:
```

---

## Underlying command (only after confirmation + env)

```text
python prototypes-derived/review-assistant-thin/minimal_demo.py --scenario real_provider_synthetic --real-provider
```

Runner adds `--real-provider`; operator does not pass it directly to `minimal_demo.py` through runner without confirmation gate.

---

## Freeze validation exclusion

Real provider live scenario is **excluded** from automated freeze validation and baseline freeze runs.

Manual live validation remains operator responsibility (see Phase 3.3-LiveCheck docs).

---

## Change rule

Any change to real provider gating requires:

- Provider safety review
- No-agent-logic-change review (if touching wrapped command)
- Validation + rollback plan
- Explicit approval

See [DEMO_RUNNER_V0_1_CHANGE_LOCK.md](DEMO_RUNNER_V0_1_CHANGE_LOCK.md).
