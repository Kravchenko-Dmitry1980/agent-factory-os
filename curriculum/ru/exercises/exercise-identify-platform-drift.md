# Упражнение: Распознать platform drift

## Зачем это упражнение

Не повторять drift на capstone-проекте обучения.

## Время

25 минут

## Шаги

1. Прочитайте `evolution/examples/unsafe-shared-runtime.md`
2. Прочитайте `evolution/drift-detection/early-warning-signals.md`
3. Классифицируйте утверждения (SAFE / DRIFT):
   - a) Один демо = один gate виден в trace
   - b) Объединить все prototypes в shared/gates.py «для удобства»
   - c) Снять human approval на internal docs
   - d) Smoke после каждого изменения
   - e) Назвать учебные демо «production MVP»
4. Обсудите с наставником

## Ожидаемый результат

b, c, e = DRIFT; a, d = SAFE.

## Что наблюдать

Формулировки hype vs trace-first

## Вопросы

1. Почему shared runtime опасен на обучении?
2. Три ранних сигнала drift?

## Критерии успеха

5/5 классификация с объяснением.

## Критерии ошибки

Считаете e безопасным; предлагаете b как capstone.

Модуль: [../modules/module-11-safe-evolution.md](../modules/module-11-safe-evolution.md)
