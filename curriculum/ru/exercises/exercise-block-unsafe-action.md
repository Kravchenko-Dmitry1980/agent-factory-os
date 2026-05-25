# Упражнение: Заблокировать опасное действие

## Зачем это упражнение

Показать fail-closed на трёх сценариях одобрения.

## Время

15 минут

## Шаги

```powershell
python prototypes/fail-closed-external-action/minimal-demo.py --scenario no-approval
python prototypes/fail-closed-external-action/minimal-demo.py --scenario rejected
python prototypes/fail-closed-external-action/minimal-demo.py --scenario approved
```

## Ожидаемый результат

Только approved выполняет внешнее действие; остальные — deny.

## Что наблюдать

Human/approval поля и итог Execute/Published

## Вопросы

1. Что общего у no-approval и rejected?
2. Почему timeout ≠ approved?

## Критерии успеха

Три сценария сравнены; deny объяснён.

## Критерии ошибки

Считаете no-approval успешной отправкой.

Модули: [../modules/module-04-human-approval.md](../modules/module-04-human-approval.md), [../modules/module-06-fail-closed-execution.md](../modules/module-06-fail-closed-execution.md)
