# Модуль 09 — Наблюдаемость и traces

## Цель

Читать trace как историю решений, а не как «лог ошибок».

## Простое объяснение

**Trace** (след выполнения) — упорядоченные события: кто, какой gate, какой исход, почему. Без trace нельзя отладить governance и доказать, что deny был правильным.

## Ключевые идеи

- Канонические события (canonical events)
- Блоки OUTCOME / GOVERNANCE
- Хороший vs плохой trace (сравнение)
- Примеры в `observability/examples/`

## Что прочитать

- `observability/README.md`
- `observability/event-taxonomy/canonical-events.md`
- `evaluation/trace-comparison/good-trace-vs-bad-trace.md`
- [../lessons/lesson-audit-lineage.md](../lessons/lesson-audit-lineage.md)

## Что запустить

Прочитайте 6 файлов в `observability/examples/`. Затем:

```powershell
python prototypes/integrations/review-queue-workflow/minimal-demo.py --scenario approval-denied
```

## Упражнение

[../exercises/exercise-read-trace.md](../exercises/exercise-read-trace.md)

## Частые ошибки

- Искать только ERROR
- Тонкий лог без gate/reason
- Удалять события при рефакторинге

## Контрольные вопросы

1. Что такое trace?
2. Какие поля обязательны при deny?
3. Чем хороший trace отличается от плохого?

## Ожидаемый результат

Студент устно проходит approval-denied trace по шагам.
