# Interaction Flow — Free-Form CLI (RU)

**Дата:** 2026-05-26  
**Статус:** PLAN_ONLY

---

## Общий поток (будущая impl)

```text
start
  → показать предупреждение (lab demo, не production)
  → запросить текст задачи
  → validate input
  → выбор режима:
       1. Safe mock/default (default)
       2. Local provider — только явно
  → создать/получить черновик
  → verification
  → approval (simulated prompt, default no)
  → напечатать результат
  → объяснить TRACE
  → опционально save transcript (--save-transcript)
  → exit
```

**Один запуск — одна задача.** Без chat loop. Без памяти. Без изменения файлов.

---

## Минимальная первая версия (v1)

| Rule | Value |
|------|-------|
| Tasks per run | 1 |
| Chat loop | no |
| Memory | no |
| File changes | no |
| Default mode | mock/default |
| Provider | off unless Mode 2 + yes + env |

---

## Пример взаимодействия

```text
========================================
FREE-FORM REVIEW ASSISTANT (lab demo)
========================================

⚠ Это учебный demo. Не вводите секреты и персональные данные.

Введите задачу:
> Сделай короткое сообщение заказчику о том, что демо готово.

Подтвердите: данные synthetic/demo-safe? yes/no: yes

Режим:
  1. Safe mock/default
  2. Local provider (LM Studio, explicit only)

Выберите режим [1]: 1

... TRACE ...

Approve result? yes/no [no]: no

========================================
РЕЗУЛЬТАТ
========================================

Решение: BLOCKED
Доставлено: нет

Что произошло:
Черновик создан и прошёл verification, но approval не получен.

Почему такое решение:
Без явного approval система не доставляет результат (deny by default).

SAFETY GATES
- verification: passed
- approval: missing
- unsafe action: not detected

Статус безопасности: BLOCKED
```

---

## Альтернативный исход (approval yes, safe draft)

```text
Approve result? yes/no [no]: yes

Решение: DELIVERED
Доставлено: да
...
Статус безопасности: OK
```

---

## Отклонение ввода

```text
Введите задачу:
> 

Ошибка: пустой ввод. Завершение.

---

Введите задачу:
> sk-abc123secretapikey...

Предупреждение: ввод похож на секрет. Задача отклонена (INPUT_REJECTED).
```

---

## Provider mode (Mode 2) — дополнительные шаги

Только если оператор выбрал `2`:

1. Предупреждение (как в Demo Runner v0.1)
2. `Продолжить? yes/no` — default no
3. Проверка `RA_LLM_BASE_URL`
4. Только synthetic/non-sensitive input

См. [PROVIDER_MODE_POLICY.md](PROVIDER_MODE_POLICY.md).

---

## Диаграммы

- [diagrams/operator-input-flow.md](diagrams/operator-input-flow.md)
- [diagrams/approval-flow.md](diagrams/approval-flow.md)
