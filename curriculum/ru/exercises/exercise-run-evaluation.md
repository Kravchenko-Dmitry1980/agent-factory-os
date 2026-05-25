# Упражнение: Запустить evaluation

## Зачем это упражнение

Освоить три локальных скрипта проверки поведения.

## Время

15 минут

## Шаги

```powershell
cd C:\Dima\Projects\CURSOR\AGENT
python evaluation/scripts/run_demo_smoke_checks.py
python evaluation/scripts/check_expected_text_traces.py
python evaluation/scripts/summarize_evaluation_status.py
```

Запишите: PASS/FAIL по каждому скрипту.

## Ожидаемый результат

Понимание, что smoke — минимальная планка, не прод-доказательство.

## Что наблюдать

Какие демо упали; текст FAIL, не только код возврата

## Вопросы

1. Что делать при FAIL до Phase 3?
2. Чем smoke отличается от trace text check?

## Критерии успеха

Три команды запущены; статус интерпретирован.

## Критерии ошибки

Игнор FAIL; не могут повторить команды.

Модуль: [../modules/module-10-evaluation-and-regression.md](../modules/module-10-evaluation-and-regression.md)
