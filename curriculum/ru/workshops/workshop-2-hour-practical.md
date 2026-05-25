# Воркшоп: 2 часа практики

## Аудитория

Стажёры, день 1.

## Длительность

2 часа

## Цель

Пройти безопасность L0–L2 hands-on.

## План

1. Ввод 30 мин ([workshop-30-min-intro.md](workshop-30-min-intro.md))
2. Fail-closed три сценария (20 мин)
3. Bounded memory overflow (15 мин)
4. Read trace (25 мин)
5. Урок fail-closed (10 мин)
6. Q&A по beginner assessment (20 мин)

## Какие файлы открыть

- [../modules/module-06-fail-closed-execution.md](../modules/module-06-fail-closed-execution.md)
- [../lessons/lesson-fail-closed.md](../lessons/lesson-fail-closed.md)
- [../exercises/exercise-read-trace.md](../exercises/exercise-read-trace.md)

## Какие команды запустить

```powershell
python prototypes/fail-closed-external-action/minimal-demo.py --scenario no-approval
python prototypes/bounded-memory-agent/minimal-demo.py --scenario overflow
python prototypes/queue-orchestration/minimal-demo.py --scenario max-retries
python evaluation/scripts/check_expected_text_traces.py
```

## Вопросы для обсуждения

1. Exit 0 и Published False — совместимы?
2. Когда эскалация?
3. Что записать в learning log?

## Ожидаемый результат обучения

Готовность к [../exercises/exercise-run-first-demo.md](../exercises/exercise-run-first-demo.md) и read-trace с наставником.
