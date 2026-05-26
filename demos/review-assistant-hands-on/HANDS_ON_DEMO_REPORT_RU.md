# Hands-on Demo Report — Review Assistant Thin

**Дата:** 2026-05-26  
**Оператор:** Дмитрий (ручной запуск в PowerShell)  
**Демо:** `prototypes-derived/review-assistant-thin/minimal_demo.py`  
**Baseline:** review-assistant-thin-v0.3 (frozen)

---

## Короткий вывод

Система **уже не только документы**.

- Есть **рабочий CLI-прототип** Review Assistant Thin.
- Агент **реально запускается** — видны `decision`, `delivered`, секция `TRACE`.
- **Mock LLM** и **real local provider (LM Studio)** проходят через те же gates: parse → verification → approval.
- LM Studio **реально ответил** на сценарий `real_provider_synthetic` (ручной запуск оператора).
- Но это **ещё лаборатория**, не продукт: нет UI, нет свободного ввода задачи, approval симулируется сценарием.

**Главный смысл:** проект демонстрирует **контролируемый agent loop** с видимой историей решений — не просто набор markdown-спек.

---

## Что было запущено руками

### 5 original scenarios

| # | Сценарий | Результат |
|---|----------|-----------|
| 1 | `happy` | DELIVERED |
| 2 | `missing_approval` | BLOCKED |
| 3 | `critic_uncertain` | ESCALATED |
| 4 | `bad_draft` | FAILED |
| 5 | `unsafe_publish_attempt` | FAILED |

### 3 mock LLM scenarios

| # | Сценарий | Результат |
|---|----------|-----------|
| 6 | `llm_valid_draft` | DELIVERED |
| 7 | `llm_malformed_output` | FAILED |
| 8 | `llm_unsafe_output` | FAILED |

### 1 real provider scenario

| # | Сценарий | Результат |
|---|----------|-----------|
| 9 | `real_provider_synthetic --real-provider` | DELIVERED (LM Studio, qwen2.5-7b-instruct-1m) |

Подробности: [COMMANDS_RUN.md](COMMANDS_RUN.md), [SCENARIO_RESULTS.md](SCENARIO_RESULTS.md).

---

## Что доказано

| Принцип | Как видно в демо |
|---------|------------------|
| **Approval обязателен** | `missing_approval` → BLOCKED, `approval_timeout`, `delivered=False` |
| **Плохой черновик блокируется** | `bad_draft` → `verification_failed`, FAILED |
| **Критик не истина** | `critic_uncertain` → UNCERTAIN → escalation, не delivery |
| **Unsafe action блокируется** | `unsafe_publish_attempt`, `llm_unsafe_output` → `unsafe_action_blocked` |
| **LLM output ≠ truth** | `llm_valid_draft`: `draft_created source=llm_unverified`, нужны verification + approval |
| **Real provider output ≠ truth** | `real_provider_synthetic`: `source=provider_unverified`, те же gates |
| **Provider: parse → verification → approval** | Trace: provider_parse_passed → verification_passed → approval_granted → task_completed |
| **Mock default сохранён** | Original + mock LLM работают без `--real-provider` |
| **Real provider только explicit** | Нужны env + флаг `--real-provider` |

---

## Что ещё **не** доказано

| Область | Почему |
|---------|--------|
| Удобный UI | Только терминал |
| Interactive input | Задача зашита в сценарий |
| «Введи свою задачу» | Нет режима free-form |
| Production readiness | Lab prototype |
| Качество модели | Один synthetic live run, не benchmark |
| Live prompt injection | Harness — synthetic local, не live red-team |
| Task Triage | Только specs v0.1, нет impl |
| Operator Console | Backlog |

---

## Главный смысл для проекта

До hands-on: много governance, freeze, harness — **абстрактно**.

После hands-on: оператор **увидел** agent loop:

```text
task → draft → critique → verification → approval → delivery (или block/fail)
```

Trace — это **аудит**, а не декорация. Решение `DELIVERED` без `approval_granted` в trace быть не должно.

---

## Связанные документы

- [TRACE_EXPLANATION_RU.md](TRACE_EXPLANATION_RU.md)
- [WHAT_IS_REAL_NOW_RU.md](WHAT_IS_REAL_NOW_RU.md)
- [WHY_IT_DOES_NOT_FEEL_LIKE_PRODUCT_RU.md](WHY_IT_DOES_NOT_FEEL_LIKE_PRODUCT_RU.md)
- [NEXT_PRACTICAL_STEPS_RU.md](NEXT_PRACTICAL_STEPS_RU.md)
