# Объяснение TRACE — Review Assistant Hands-on

**Язык:** простой русский  
**Контекст:** вывод `minimal_demo.py` в терминале

---

## Что такое TRACE

**TRACE** — видимая история того, что произошло внутри агента.

Это не лог сервера и не телеметрия облака. Это **человекочитаемый аудит** для оператора и разработчика: какие шаги прошли, где остановились, почему не доставили.

Если в trace нет `approval_granted`, финальная доставка (`delivered=True`) **не должна** считаться легитимной.

---

## Базовые события (original loop)

| Событие | Простое значение |
|---------|------------------|
| `task_started` | Задача принята, цикл начался |
| `draft_created` | Черновик создан (источник может быть rule-based или позже llm/provider) |
| `critique_completed` | Критик отработал (результат **advisory**, не истина) |
| `verification_passed` | Проверки черновика пройдены |
| `verification_failed` | Черновик не прошёл проверку → обычно FAILED |
| `approval_requested` | Запрошено human approval |
| `approval_granted` | Approval получен (в demo — симуляция сценария) |
| `approval_timeout` | Approval не получен в срок → deny by default |
| `approval_denied` | Approval явно отклонён |
| `unsafe_action_blocked` | Опасное действие заблокировано |
| `escalation_triggered` | Неопределённость/риск → эскалация |
| `task_completed` | Успешное завершение (часто после delivery) |
| `task_failed` | Fail-closed: цикл остановлен без delivery |

---

## LLM events (mock LLM v0.2)

| Событие | Простое значение |
|---------|------------------|
| `llm_request_started` | Запрос к mock LLM начат |
| `llm_response_received` | Ответ получен |
| `llm_parse_passed` | Ответ разобран в ожидаемую форму |
| `llm_parse_failed` | Ответ malformed → FAILED |
| `llm_unsafe_output` | Ответ содержит unsafe content → block |

**Важно:** `llm_parse_passed` ≠ «модель права». Это только «ответ можно разобрать». Дальше — verification и approval.

Черновик помечается `source=llm_unverified`.

---

## Provider events (real provider v0.3)

| Событие | Простое значение |
|---------|------------------|
| `provider_request_prepared` | Запрос к локальному provider подготовлен |
| `provider_request_started` | HTTP-запрос отправлен (LM Studio) |
| `provider_response_received` | Ответ получен |
| `provider_parse_passed` | Ответ разобран в форму черновика |

**Важно:** `provider_parse_passed` ≠ «provider прав». Это только parse. Черновик — `source=provider_unverified`. Дальше critique (advisory), verification, approval.

Real provider включается **только** с `--real-provider` и env (`RA_LLM_BASE_URL`, `RA_LLM_MODEL`).

---

## Ключевые правила интерпретации

### 1. Нет approval_granted → нет легитимной delivery

Сценарий `missing_approval`: есть `approval_requested`, потом `approval_timeout`, `decision=BLOCKED`.

### 2. unsafe_action_blocked = система защитилась

Сценарии `unsafe_publish_attempt`, `llm_unsafe_output`: агент **не** «попробовал доставить несмотря ни на что».

### 3. provider_parse_passed ≠ доверие

Live run оператора: provider ответил, parse прошёл, но trace явно ведёт через verification и approval. **Provider/LLM output ≠ truth.**

### 4. critique_completed с UNCERTAIN → escalation, не delivery

`critic_uncertain`: критик не даёт уверенного «ок» → эскалация, не автопубликация.

### 5. verification_failed → FAILED

`bad_draft`: даже с approval-симуляцией плохой черновик не проходит gate.

---

## Мини-пример чтения trace (happy path)

```text
TRACE
- task_started
- draft_created
- critique_completed
- verification_passed
- approval_requested
- approval_granted
- task_completed

decision=DELIVERED
delivered=True
```

**Читаем:** все gates пройдены, human approval (симулированный) есть, доставка разрешена.

---

## Сравнение с observability examples

Frozen trace examples: `observability/examples/successful-review-trace.txt`, `failed-review-trace.txt`.

Hands-on demo подтверждает, что **thin demo печатает похожую дисциплину** — события узнаваемы, fail-closed работает.
