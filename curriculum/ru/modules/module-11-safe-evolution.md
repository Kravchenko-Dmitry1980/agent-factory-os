# Модуль 11 — Безопасная эволюция

## Цель

Менять систему через proposal, проверку и rollback — без ослабления gates.

## Простое объяснение

Изменение начинается с **change proposal** (шаблон), затем smoke до/после, затем решение: оставить или **rollback** (откат). Platform drift — когда «объединяем демо» и теряем проверки.

## Ключевые идеи

- `evolution/change-proposals/change-template.md`
- Rollback runbook
- Early warning signals drift
- Примеры accidental-auto-approve

## Что прочитать

- `evolution/README.md`
- `evolution/drift-detection/early-warning-signals.md`
- [../../operator-playbooks/change-guides/how-to-change-safely.md](../../operator-playbooks/change-guides/how-to-change-safely.md)

## Что запустить

Smoke до и после учебного изменения (с наставником):

```powershell
python evaluation/scripts/run_demo_smoke_checks.py
```

## Упражнение

[../exercises/exercise-write-change-proposal.md](../exercises/exercise-write-change-proposal.md)  
[../exercises/exercise-decide-rollback.md](../exercises/exercise-decide-rollback.md)  
[../exercises/exercise-identify-platform-drift.md](../exercises/exercise-identify-platform-drift.md)

## Частые ошибки

- Правка gates «втихую»
- Общий runtime для всех демо на обучении
- Нет proposal при изменении MAX_RETRIES

## Контрольные вопросы

1. Что такое rollback?
2. Три сигнала platform drift?
3. Зачем proposal до кода?

## Ожидаемый результат

Студент заполняет шаблон proposal (на бумаге) и классифицирует drift-примеры.
