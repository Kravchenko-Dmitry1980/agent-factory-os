# Модуль 02 — Почему ломаются AI-системы

## Цель

Изучить **режимы сбоев**, особенно тихие — когда всё «как будто успешно».

## Простое объяснение

AI чаще ломается **правдоподобной ошибкой**, чем падением процесса. Система опасна, если доверяют выводу без проверки, пропускают одобрение или раздувают память/контекст.

## Ключевые идеи

- Галлюцинации и уверенный тон
- «Критик прошёл» ≠ факты верны
- Шторм повторов (retry storm) маскирует баги
- Нет аудита — решения невидимы
- Platform drift — gates ослабевают постепенно

## Что прочитать

- `agent-os/09_antipatterns/index.md`
- `evolution/examples/accidental-auto-approve.md`
- [../lessons/lesson-critic-is-not-truth.md](../lessons/lesson-critic-is-not-truth.md)

## Что запустить

```powershell
python prototypes/review-loop-agent/minimal-demo.py --scenario bypass-attempt
python prototypes/integrations/review-queue-workflow/minimal-demo.py --scenario approval-denied
```

Прочитать trace: `observability/examples/failed-review-trace.txt`

## Упражнение

[../exercises/exercise-break-review-loop.md](../exercises/exercise-break-review-loop.md) *(только наблюдение — не ломать код)*

## Частые ошибки

- Тестировать только happy path
- «Чинить» снятием gates
- Винить модель вместо workflow

## Контрольные вопросы

1. Пример тихого сбоя.
2. Что в failed-review trace, когда критик «прошёл»?
3. Один антипаттерн из agent-os.

## Ожидаемый результат

Три типа тихих сбоев + демо для каждого.
