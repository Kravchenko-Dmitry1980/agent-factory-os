# Как преподавать эту систему

## Принципы

1. **Демо до лекции** — сначала trace, потом доктрина.
2. **Обязательны fail-path** — только happy path вреден.
3. **Один gate за раз** — не смешивать fail-closed и drift в одном слоте.
4. **Claim → event** — любое утверждение студента должно указать на событие в trace.

## Структура занятия (60–90 мин)

1. Hook: запуск одного deny сценария
2. Имя понятия (простое определение)
3. Trace разбор
4. Упражнение
5. Checkpoint questions

## Порядок материалов

README → module-00 → first demo → L2 safety (03,04,06) → traces → evaluation → evolution → Phase 3.

## Оценка

Open book допустим; важно **показать** демо и пересказать deny. Fail = план доработки, не «плохой студент».

## Типичные ошибки преподавания

- Начинать с Books/ или agent-os без демо
- Обещать Agent Factory на первой неделе
- Пропускать bypass «чтобы успели»

Связь: [../methodology/agent-os-learning-method.md](../methodology/agent-os-learning-method.md)
