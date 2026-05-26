# Output Format — Free-Form CLI (RU)

**Дата:** 2026-05-26  
**Статус:** PLAN_ONLY

Язык операторского резюме: **русский**. TRACE может содержать EN technical tokens (как в thin demo).

---

## Общая структура

```text
========================================
FREE-FORM REVIEW ASSISTANT
========================================

Входная задача:
{sanitized_task_preview}

Режим:
{safe mock/default | local provider explicit}

----------------------------------------
РЕЗУЛЬТАТ
----------------------------------------
Решение: {DELIVERED|BLOCKED|ESCALATED|FAILED|NEEDS_APPROVAL|INPUT_REJECTED}
Доставлено: {да|нет}

----------------------------------------
ЧТО ПРОИЗОШЛО
----------------------------------------
{2–5 предложений}

----------------------------------------
ПОЧЕМУ ТАКОЕ РЕШЕНИЕ
----------------------------------------
{краткое объяснение decision}

----------------------------------------
SAFETY GATES
----------------------------------------
- verification: passed/failed/skipped
- approval: granted/missing/denied/required
- unsafe action: blocked/not detected

----------------------------------------
TRACE
----------------------------------------
- {event}: {ru_short}
...

----------------------------------------
СТАТУС БЕЗОПАСНОСТИ
----------------------------------------
{OK|BLOCKED|ESCALATED|FAILED|WARNING}
```

---

## Форматы по decision

### DELIVERED

| Поле | Значение |
|------|----------|
| Решение | DELIVERED |
| Доставлено | да |
| ПОЧЕМУ | Verification пройдена, approval получен |
| GATES | verification passed, approval granted |

### BLOCKED

| Поле | Значение |
|------|----------|
| Решение | BLOCKED |
| Доставлено | нет |
| ПОЧЕМУ | Approval не получен или политика заблокировала |
| GATES | approval missing/denied |

### ESCALATED

| Поле | Значение |
|------|----------|
| Решение | ESCALATED |
| Доставлено | нет |
| ПОЧЕМУ | Неопределённость или риск — эскалация |
| GATES | escalation triggered |

### FAILED

| Поле | Значение |
|------|----------|
| Решение | FAILED |
| Доставлено | нет |
| ПОЧЕМУ | Verification failed или unsafe block |
| GATES | verification failed / unsafe blocked |

### NEEDS_APPROVAL

| Поле | Значение |
|------|----------|
| Решение | NEEDS_APPROVAL |
| Доставлено | нет |
| ПОЧЕМУ | Черновик готов, ждёт approval (промежуточное состояние, если impl показывает до prompt) |
| GATES | approval required |

*Note:* v1 may collapse NEEDS_APPROVAL into approval prompt step; document in impl freeze.

### INPUT_REJECTED

| Поле | Значение |
|------|----------|
| Решение | INPUT_REJECTED |
| Доставлено | нет |
| ПОЧЕМУ | Пустой ввод, секрет-like, или operator declined safe-data confirm |
| GATES | input gate failed |

---

## Запрещено в summary

- Claim «production ready»
- Скрывать BLOCKED/FAILED как success
- Печатать secrets из ввода или env
- Утверждать DELIVERED без approval_granted в trace

---

## Связь с Demo Runner

Стиль согласован с Demo Runner v0.1 и [phase-3-5-2-plan/OPERATOR_OUTPUT_FORMAT_RU.md](../phase-3-5-2-plan/OPERATOR_OUTPUT_FORMAT_RU.md), но добавляет блок **Входная задача** и **SAFETY GATES**.
