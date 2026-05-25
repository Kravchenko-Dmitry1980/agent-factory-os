# Модуль 07 — Оркестрация workflow

## Цель

Несколько шагов в одном процессе: очередь, лимит повторов, эскалация.

## Простое объяснение

Оркестрация — не «магический диспетчер», а **очередь задач** с правилами: сколько раз повторять, когда отдать человеку, как восстановиться после сбоя.

## Ключевые идеи

- Queue-backed execution
- Bounded retries (ограниченные повторы)
- Escalation при исчерпании попыток
- Recovery без снятия gates

## Что прочитать

- `prototypes/queue-orchestration/README.md`
- `integrations/escalation-workflow/README.md`
- [../lessons/lesson-retry-and-escalation.md](../lessons/lesson-retry-and-escalation.md)

## Что запустить

```powershell
python prototypes/queue-orchestration/minimal-demo.py --scenario happy
python prototypes/queue-orchestration/minimal-demo.py --scenario max-retries
python prototypes/integrations/escalation-workflow/minimal-demo.py --scenario retry-storm
```

## Упражнение

[../exercises/exercise-trigger-escalation.md](../exercises/exercise-trigger-escalation.md)

## Частые ошибки

- Бесконечные retry
- Эскалация без события в trace
- Один гигантский агент вместо шагов с gates

## Контрольные вопросы

1. Когда эскалация к человеку?
2. Что такое max-retries?
3. Где в trace виден retry-storm?

## Ожидаемый результат

Студент пересказывает путь задачи: enqueue → retry → escalate.
