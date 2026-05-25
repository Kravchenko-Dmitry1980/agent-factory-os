# Упражнение: Вызвать эскалацию

## Зачем это упражнение

Связать retry ceiling с событием escalation в trace.

## Время

20 минут

## Шаги

1. Прочитайте `observability/examples/escalation-trace.txt`
2. Запустите:

```powershell
python prototypes/integrations/escalation-workflow/minimal-demo.py --scenario retry-storm
python prototypes/queue-orchestration/minimal-demo.py --scenario max-retries
```

3. Найдите в выводе: retry count, escalation, human handoff (если есть)

## Ожидаемый результат

Видна цепочка: повторы → лимит → эскалация.

## Что наблюдать

Имена событий, не только exit code

## Вопросы

1. Сколько retry допустимо в демо?
2. Когда должен подключиться человек?

## Критерии успеха

Пересказ escalation-trace своими словами.

## Критерии ошибки

«Просто упало» без gate/reason.

Модуль: [../modules/module-07-workflow-orchestration.md](../modules/module-07-workflow-orchestration.md)
