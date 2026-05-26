# Real Provider Warning Policy

**Date:** 2026-05-26  
**Status:** PLAN_ONLY — **non-negotiable for Demo Runner**

Real provider scenario must **not** run by accident.

---

## Scope

Applies to menu item **3.1** `real_provider_synthetic` only.

Hands-on reference: operator used LM Studio at `http://127.0.0.1:1234`, model `qwen2.5-7b-instruct-1m`. Runner must not hardcode these — read from env.

---

## Future warning text (Russian)

```text
⚠ ВНИМАНИЕ: Real Provider Scenario

Этот сценарий вызывает локальный LM Studio / OpenAI-compatible endpoint.

Проверьте:
  □ LM Studio (или аналог) запущен локально
  □ RA_LLM_BASE_URL задан (например http://127.0.0.1:1234)
  □ RA_LLM_MODEL задан
  □ Используются только synthetic test data
  □ Нет cloud provider (OpenAI cloud и т.д.)
  □ Нет API ключей в логах

Продолжить? [y/N]:
```

---

## Rules

| Rule | Enforcement |
|------|-------------|
| Default answer | **no** (N, Enter = cancel) |
| No provider call without confirmation | Runner must not pass `--real-provider` until yes |
| No provider call if env missing | Check `RA_LLM_BASE_URL` and `RA_LLM_MODEL`; abort with Russian message |
| No private data | Scenario remains `real_provider_synthetic` only — no custom user text in runner v0.1 |
| No cloud | Runner docs warn; no cloud URL templates |
| No secrets in logs | Do not print full env in summary unless debug flag (not planned v0.1) |
| Not in default menu auto-run | Group 3 never runs as part of “run all” batch |
| Cursor / CI must not call | Eval scripts use no-network contract check only |

---

## Abort messages (future)

| Condition | Message |
|-----------|---------|
| User answered no | «Сценарий отменён. Real provider не вызывался.» |
| Env missing | «RA_LLM_BASE_URL или RA_LLM_MODEL не заданы. Задайте env и повторите.» |
| Subprocess non-zero exit | «Demo завершился с ошибкой. Проверьте, запущен ли LM Studio.» |

---

## Alignment with frozen v0.3

`minimal_demo.py` already requires `--real-provider` flag. Runner **must not** remove this — only gate it with confirmation UI.

Contract check (no-network): `check_review_assistant_real_provider_contract.py` — remains separate menu item 4.4.

---

## Forbidden

- Auto-run real provider on runner startup
- “Run all scenarios including provider” one-click
- Hidden network call
- Default to cloud endpoint

See [NO_AGENT_LOGIC_CHANGE_POLICY.md](NO_AGENT_LOGIC_CHANGE_POLICY.md).
