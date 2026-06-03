# Справочник сценариев Demo Runner (RU)

**Phase 3.5.2** — все 15 пунктов фиксированного меню.

---

## Группа 1 — Базовые сценарии Review Assistant

| № | Ключ | Название | Команда | Real provider |
|---|------|----------|---------|---------------|
| 1 | `happy` | Нормальный сценарий | `minimal_demo.py --scenario happy` | нет |
| 2 | `missing_approval` | Нет approval | `minimal_demo.py --scenario missing_approval` | нет |
| 3 | `critic_uncertain` | Критик не уверен | `minimal_demo.py --scenario critic_uncertain` | нет |
| 4 | `bad_draft` | Плохой черновик | `minimal_demo.py --scenario bad_draft` | нет |
| 5 | `unsafe_publish_attempt` | Опасная попытка публикации | `minimal_demo.py --scenario unsafe_publish_attempt` | нет |

### Что доказывает группа 1

| Ключ | Ожидаемое решение | Что доказывает |
|------|-------------------|----------------|
| happy | DELIVERED | Happy path с approval работает |
| missing_approval | BLOCKED | Без approval — нет delivery |
| critic_uncertain | ESCALATED | Неопределённость → эскалация |
| bad_draft | FAILED | Verification блокирует плохой черновик |
| unsafe_publish_attempt | FAILED | Bypass блокируется |

---

## Группа 2 — Mock LLM

| № | Ключ | Название | Команда | Real provider |
|---|------|----------|---------|---------------|
| 6 | `llm_valid_draft` | Mock LLM — хороший ответ | `minimal_demo.py --scenario llm_valid_draft` | нет |
| 7 | `llm_malformed_output` | Mock LLM — сломанный ответ | `minimal_demo.py --scenario llm_malformed_output` | нет |
| 8 | `llm_unsafe_output` | Mock LLM — опасный ответ | `minimal_demo.py --scenario llm_unsafe_output` | нет |

### Что доказывает группа 2

| Ключ | Ожидаемое решение | Что доказывает |
|------|-------------------|----------------|
| llm_valid_draft | DELIVERED | LLM output проходит gates |
| llm_malformed_output | FAILED | Malformed parse rejected |
| llm_unsafe_output | FAILED | Unsafe LLM blocked |

---

## Группа 3 — Real Local Provider

| № | Ключ | Название | Команда | Real provider |
|---|------|----------|---------|---------------|
| 9 | `real_provider_synthetic` | Real provider — LM Studio (synthetic) | `minimal_demo.py --scenario real_provider_synthetic --real-provider` | **да** ⚠ |

**Требует:** подтверждение оператора + `RA_LLM_BASE_URL` + локальный LM Studio/Ollama.

---

## Группа 4 — Проверки baseline

| № | Ключ | Название | Скрипт | Сеть |
|---|------|----------|--------|------|
| 10 | `provider_safety_harness` | Provider safety harness (16 cases) | `check_review_assistant_provider_safety.py` | нет |
| 11 | `thin_baseline` | Thin baseline (5 cases) | `check_review_assistant_thin.py` | нет |
| 12 | `mock_llm_baseline` | Mock LLM baseline (5 cases) | `check_review_assistant_llm_mock.py` | нет |
| 13 | `real_provider_contract_no_network` | Real provider contract (no-network) | `check_review_assistant_real_provider_contract.py` | нет |
| 14 | `smoke_checks` | Smoke checks (12 cases) | `run_demo_smoke_checks.py` | нет |
| 15 | `text_trace_checks` | Text trace examples (6 cases) | `check_expected_text_traces.py` | нет |

### Ожидаемые PASS/FAIL

| Ключ | Ожидание |
|------|----------|
| provider_safety_harness | PASS=16 FAIL=0 |
| thin_baseline | PASS=5 FAIL=0 |
| mock_llm_baseline | PASS=5 FAIL=0 |
| real_provider_contract_no_network | PASS=2 FAIL=0 |
| smoke_checks | PASS=12 FAIL=0 |
| text_trace_checks | PASS=6 FAIL=0 |

---

## Правила меню

- Фиксированный список — без dynamic registry
- Без новых сценариев — только frozen names из thin v0.3
- Real provider — последний в группе 3, с предупреждением
- Группа 4 — явно «проверки baseline», не agent demo
