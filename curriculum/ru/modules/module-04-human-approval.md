# Модуль 04 — Одобрение человеком

## Цель

Понять явное одобрение человеком для действий с последствиями.

## Простое объяснение

Человек в контуре (human-in-the-loop) **явно** разрешает опасное действие. Таймаут и «молчание» — не согласие. Решение человека важнее оценки критика.

## Ключевые идеи

- approval_requested / approved / denied в trace
- Таймаут → deny (fail-closed)
- Внутренние документы тоже могут требовать одобрения
- Критик не заменяет человека

## Что прочитать

- `agent-os/doctrine/governance-before-autonomy.md`
- [../lessons/lesson-human-approval.md](../lessons/lesson-human-approval.md)
- [../../operator-playbooks/safety-guides/why-approval-is-required.md](../../operator-playbooks/safety-guides/why-approval-is-required.md)

## Что запустить

```powershell
python prototypes/fail-closed-external-action/minimal-demo.py --scenario no-approval
python prototypes/fail-closed-external-action/minimal-demo.py --scenario approved
python prototypes/integrations/telegram-review-gate/minimal-demo.py --scenario happy
```

## Упражнение

[../exercises/exercise-block-unsafe-action.md](../exercises/exercise-block-unsafe-action.md)

## Частые ошибки

- «Внутреннее — можно без человека»
- Авто-approve по таймауту
- Считать critic PASS = можно публиковать

## Контрольные вопросы

1. Когда нужен человек?
2. Что значит fail-closed при отсутствии approval?
3. Кто побеждает: критик или человек?

## Ожидаемый результат

Студент объясняет разницу no-approval / approved по trace.
