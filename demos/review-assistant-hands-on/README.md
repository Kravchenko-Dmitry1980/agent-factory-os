# Review Assistant — Hands-on Demo

**Phase 3.5.1** — ручной операторский walkthrough для Review Assistant Thin v0.3.

Markdown-only. Без кода. Без изменения поведения агента.

---

## Что это за демо

Ручной hands-on walkthrough для **Review Assistant Thin v0.3** (`prototypes-derived/review-assistant-thin/minimal_demo.py`).

Оператор (Дмитрий) запустил сценарии в PowerShell и увидел реальный вывод: решения, trace, блокировки, доставку.

---

## Зачем это существует

В проекте было много фаз: governance, specs, freeze, harness. Но до ручного запуска система ощущалась как **документы**.

Этот пакет фиксирует:

- что **реально запускалось**
- что **реально работало**
- что **ещё лаборатория**, а не продукт

---

## Что было «тронуто»

| Слой | Сценарии |
|------|----------|
| Original Review Assistant | happy, missing_approval, critic_uncertain, bad_draft, unsafe_publish_attempt |
| Mock LLM | llm_valid_draft, llm_malformed_output, llm_unsafe_output |
| Real local provider (LM Studio) | real_provider_synthetic + `--real-provider` |

**Frozen baseline:** review-assistant-thin-v0.3, provider-safety-harness-v0.1, task-triage-agent-specs-v0.1.

---

## Чем это демо **не** является

- не product UI
- не production
- не полноценная agent platform
- не Operator Console
- не Task Triage implementation

**Demo Runner v0.1 (FROZEN_WITH_NOTES):** UX wrapper — [../review-assistant-runner/README.md](../review-assistant-runner/README.md) · [freeze](../review-assistant-runner/freeze/README.md)

---

## Порядок чтения

1. [DEMO_SUMMARY_FOR_DMITRY_RU.md](DEMO_SUMMARY_FOR_DMITRY_RU.md) — коротко для Дмитрия
2. [HANDS_ON_DEMO_REPORT_RU.md](HANDS_ON_DEMO_REPORT_RU.md) — основной отчёт
3. [COMMANDS_RUN.md](COMMANDS_RUN.md) — точные команды
4. [SCENARIO_RESULTS.md](SCENARIO_RESULTS.md) — таблица результатов
5. [TRACE_EXPLANATION_RU.md](TRACE_EXPLANATION_RU.md) — что значит TRACE
6. [WHAT_IS_REAL_NOW_RU.md](WHAT_IS_REAL_NOW_RU.md) — что уже настоящее
7. [WHAT_IS_STILL_MOCK_RU.md](WHAT_IS_STILL_MOCK_RU.md) — что ещё mock/lab
8. [WHY_IT_DOES_NOT_FEEL_LIKE_PRODUCT_RU.md](WHY_IT_DOES_NOT_FEEL_LIKE_PRODUCT_RU.md) — почему не продукт
9. [UX_GAPS_RU.md](UX_GAPS_RU.md) — пробелы UX
10. [NEXT_PRACTICAL_STEPS_RU.md](NEXT_PRACTICAL_STEPS_RU.md) — что делать дальше

---

## Governance

[governance/PHASE_3_5_1_HANDS_ON_DEMO_REPORT_REVIEW.md](../../governance/PHASE_3_5_1_HANDS_ON_DEMO_REPORT_REVIEW.md)

**Next:** Demo Runner v0.1 frozen — [../review-assistant-runner/freeze/README.md](../review-assistant-runner/freeze/README.md)

**Date:** 2026-05-26
