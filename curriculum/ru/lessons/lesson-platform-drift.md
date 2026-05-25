# Урок: Platform drift

## Что это?

**Platform drift** (уход в платформу) — когда учебные демо объединяют в «общий runtime», маркетинг называет это production, а gates ослабевают.

## Почему это важно?

Drift убивает обучение: студент перестаёт видеть, **какой gate** сработал.

## Что может пойти не так?

- Один shared runtime для всех демо
- «Agent Factory уже есть» на Phase 2.7
- Снятие approval «для скорости»
- Продвижение markdown в agent-os без критериев

## Как это проверить?

Прочитайте `evolution/drift-detection/early-warning-signals.md` и `evolution/examples/unsafe-shared-runtime.md`. Пройдите упражнение drift.

## Какое демо это показывает?

Негативный урок (документы + упражнение):

- [../exercises/exercise-identify-platform-drift.md](../exercises/exercise-identify-platform-drift.md)
- [../modules/module-11-safe-evolution.md](../modules/module-11-safe-evolution.md)
