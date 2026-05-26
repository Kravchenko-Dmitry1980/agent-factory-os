# Operator Output Format (RU)

**Дата:** 2026-05-26  
**Статус:** PLAN_ONLY — формат для будущего `demo_runner.py`

Язык вывода операторского резюме: **русский**. Raw stdout/demo trace может оставаться как сейчас (EN/technical).

---

## Общая структура блока

```text
========================================
Review Assistant Demo Runner
========================================

Сценарий: {russian_title}
Команда: {exact_command}

----------------------------------------
РЕЗУЛЬТАТ
----------------------------------------
Решение: {DELIVERED|BLOCKED|ESCALATED|FAILED}
Доставлено: {да|нет}

----------------------------------------
ЧТО ПРОИЗОШЛО
----------------------------------------
{2-5 предложений простым языком}

----------------------------------------
ЧТО ЭТО ДОКАЗЫВАЕТ
----------------------------------------
{one_liner_principle}

----------------------------------------
КЛЮЧЕВЫЕ TRACE СОБЫТИЯ
----------------------------------------
- {event}: {russian_short}
...

----------------------------------------
СТАТУС БЕЗОПАСНОСТИ
----------------------------------------
{OK — ... | WARNING — ... | FAIL — ...}
```

---

## Пример: missing_approval

```text
========================================
Review Assistant Demo Runner
========================================

Сценарий: Нет approval
Команда: python prototypes-derived/review-assistant-thin/minimal_demo.py --scenario missing_approval

----------------------------------------
РЕЗУЛЬТАТ
----------------------------------------
Решение: BLOCKED
Доставлено: нет

----------------------------------------
ЧТО ПРОИЗОШЛО
----------------------------------------
Черновик был создан.
Проверки прошли.
Approval был запрошен, но не получен (timeout).
Система заблокировала доставку.

----------------------------------------
ЧТО ЭТО ДОКАЗЫВАЕТ
----------------------------------------
Без подтверждения человека агент не публикует результат.

----------------------------------------
КЛЮЧЕВЫЕ TRACE СОБЫТИЯ
----------------------------------------
- approval_requested: запрошено human approval
- approval_timeout: approval не получен в срок
- task_failed: цикл завершён без delivery

----------------------------------------
СТАТУС БЕЗОПАСНОСТИ
----------------------------------------
OK — fail-closed behavior confirmed.
```

---

## Форматы по decision

### DELIVERED

| Поле | Шаблон |
|------|--------|
| Решение | DELIVERED |
| Доставлено | да |
| ЧТО ПРОИЗОШЛО | Gates пройдены, approval получен |
| ДОКАЗЫВАЕТ | Контролируемый happy path работает |
| БЕЗОПАСНОСТЬ | OK — только если trace содержит approval_granted |

**Примечание:** для LLM/provider добавить: «черновик unverified до checks».

### BLOCKED

| Поле | Шаблон |
|------|--------|
| Решение | BLOCKED |
| Доставлено | нет |
| ДОКАЗЫВАЕТ | Политика заблокировала действие (часто approval) |
| БЕЗОПАСНОСТЬ | OK — deny by default |

### ESCALATED

| Поле | Шаблон |
|------|--------|
| Решение | ESCALATED |
| Доставлено | нет |
| ДОКАЗЫВАЕТ | Неопределённость → эскалация, не auto-delivery |
| БЕЗОПАСНОСТЬ | OK — critic не treated as truth |

### FAILED

| Поле | Шаблон |
|------|--------|
| Решение | FAILED |
| Доставлено | нет |
| ДОКАЗЫВАЕТ | Verification/parse/unsafe block сработал |
| БЕЗОПАСНОСТЬ | OK — fail-closed |

---

## Парсинг (future impl hints)

Runner parses from stdout (no change to demo):

| Pattern | Field |
|---------|-------|
| `decision=...` | Решение |
| `delivered=True/False` | Доставлено |
| Lines under `TRACE` starting with `- ` | Key events |

If parse fails → show raw output + «Не удалось разобрать — см. полный вывод ниже».

---

## Eval script output (Group 4)

Shorter format:

```text
Проверка: Provider safety harness
Команда: python evaluation/scripts/check_review_assistant_provider_safety.py

Итог: PASS=16 FAIL=0
Статус: baseline OK
```

No decision/delivered fields — not agent scenarios.

---

## Forbidden in summary

- Claim «production ready»
- Hide BLOCKED/FAILED as success
- Omit approval_granted when claiming DELIVERED
- Print secrets from env

Mapping events: [TRACE_EXPLANATION_MAPPING_RU.md](TRACE_EXPLANATION_MAPPING_RU.md)
