# Оценка: оператор

## Письменные вопросы

Те же 10 базовых вопросов, что в [beginner-assessment.md](beginner-assessment.md), плюс:

11. Какой runbook для prototypes?
12. Что делать при smoke FAIL?
13. Где troubleshooting common-errors?

## Практические задания

1. `python evaluation/scripts/run_demo_smoke_checks.py` — интерпретировать результат
2. Пройти run-prototypes runbook (с наставником)
3. Сценарий: после изменения smoke FAIL — опишите шаги по playbook

## Распознавание опасных признаков

- Пропуск evaluation «нет времени»
- `--real` без policy на стажировке
- Исправление FAIL ослаблением ожиданий trace

## Объясни своими словами

Чем оператор отличается от «человека, который пишет промпты»?

## Критерии pass

10 базовых + runbook navigation; smoke запущен; план при FAIL разумен.

## Критерии fail

Не находит runbooks; игнорирует FAIL; не может объяснить escalation timing.

Модуль: [../modules/module-12-operator-practice.md](../modules/module-12-operator-practice.md)
