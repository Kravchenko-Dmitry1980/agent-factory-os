# Упражнение: Плохой вывод LLM

## Зачем это упражнение

Научиться отличать валидный вид от проверенного содержания.

## Время

15 минут

## Шаги

```powershell
python integrations-real/llm-verification-adapter/minimal-demo.py --scenario malformed
python integrations-real/llm-verification-adapter/minimal-demo.py --scenario happy
```

Сравните с `observability/examples/malformed-llm-trace.txt` (если есть).

## Ожидаемый результат

Malformed не проходит verify; happy проходит.

## Что наблюдать

Событие verify fail / block publish

## Вопросы

1. JSON был «красивым» в malformed?
2. Какой шаг отделён от генерации?

## Критерии успеха

Объясняете, почему структура ≠ истина.

## Критерии ошибки

«Malformed = crash» без чтения gate.

Модуль: [../modules/module-03-verification-first.md](../modules/module-03-verification-first.md)
