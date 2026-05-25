# Модуль 06 — Fail-closed выполнение

## Цель

Поведение «при сомнении — стоп», а не «попробовать наугад».

## Простое объяснение

**Fail-closed** — при неясности, ошибке проверки или отсутствии одобрения система **не** выполняет опасное действие, а останавливается с понятным отказом в trace.

## Ключевые идеи

- Deny by default
- Неуверенность критика ≠ разрешение
- Uncertain/rejected/bypass — учебные сценарии
- Exit 0 не означает «безопасно опубликовали»

## Что прочитать

- `agent-os/doctrine/fail-closed-execution.md`
- `agent-os/08_patterns/fail-closed-defaults.md`
- [../lessons/lesson-fail-closed.md](../lessons/lesson-fail-closed.md)

## Что запустить

```powershell
python prototypes/fail-closed-external-action/minimal-demo.py --scenario uncertain
python prototypes/fail-closed-external-action/minimal-demo.py --scenario rejected
python prototypes/review-loop-agent/minimal-demo.py --scenario bypass-attempt
```

## Упражнение

[../exercises/exercise-block-unsafe-action.md](../exercises/exercise-block-unsafe-action.md)

## Частые ошибки

- Fallback «на всякий случай выполнить»
- Считать timeout одобрением
- Убирать deny, чтобы демо «проходило»

## Контрольные вопросы

1. Определите fail-closed своими словами.
2. Чем uncertain отличается от rejected?
3. Что показывает bypass-attempt?

## Ожидаемый результат

Студент приводит аналогию (банкомат/дверь) и показывает deny в trace.
