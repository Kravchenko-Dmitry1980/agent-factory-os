# Упражнение: Сломать review-loop (наблюдение)

## Зачем это упражнение

Увидеть режимы сбоя **без правки кода** — только чтение failure-modes и trace.

## Время

20 минут

## Шаги

1. Прочитайте `prototypes/review-loop-agent/failure-modes.md`
2. Запустите:

```powershell
python prototypes/review-loop-agent/minimal-demo.py --scenario uncertain-critic
python prototypes/review-loop-agent/minimal-demo.py --scenario human-overrides-block
python prototypes/review-loop-agent/minimal-demo.py --scenario bypass-attempt
```

3. Для каждого сценария запишите: какой gate, исход, Published

## Ожидаемый результат

Таблица из 3 строк: сценарий → gate → Published.

## Что наблюдать

Разница uncertain vs bypass vs human-overrides

## Вопросы

1. Где критик «прошёл», но публикации нет?
2. Почему нельзя «чинить» снятием human gate?

## Критерии успеха

Три сценария описаны; код не менялся.

## Критерии ошибки

Правки в коде; путаете critic PASS с publish.

Модуль: [../modules/module-02-why-ai-systems-fail.md](../modules/module-02-why-ai-systems-fail.md)
