# Упражнение: Прочитать trace

## Зачем это упражнение

Читать trace как рассказ решений, не как список ошибок.

## Время

25 минут

## Шаги

1. Откройте `observability/examples/` — выберите успешный и неуспешный файл
2. Для каждого выпишите: actor, gate, outcome, reason
3. Опционально запустите:

```powershell
python prototypes/integrations/review-queue-workflow/minimal-demo.py --scenario approval-denied
```

4. Сопоставьте живой вывод с примером failed-review

## Ожидаемый результат

Два устных пересказа по 5–7 шагов.

## Что наблюдать

GOVERNANCE / OUTCOME блоки; deny с именем gate

## Вопросы

1. Где в плохом trace не хватает данных?
2. Что произошло после critic pass?

## Критерии успеха

Оба trace объяснены; deny имеет reason.

## Критерии ошибки

Искали только ERROR; пропустили human step.

Модуль: [../modules/module-09-observability-and-traces.md](../modules/module-09-observability-and-traces.md)
