# Модуль 10 — Проверка поведения и регрессии

## Цель

Локально проверять, что безопасное поведение не сломалось после изменений.

## Простое объяснение

**Evaluation** здесь — не «оценка модели», а **проверка поведения** демо: smoke, ожидаемый текст в trace, сводка статуса. Smoke PASS — минимум, не полное доказательство production.

## Ключевые идеи

- `run_demo_smoke_checks.py`
- Ожидаемые строки в trace
- Regression matrix — что перепроверять
- FAIL — сигнал учиться, не «обойти»

## Что прочитать

- `evaluation/README.md`
- `evaluation/regression-matrix/regression-matrix.md`
- [../lessons/lesson-regression.md](../lessons/lesson-regression.md)

## Что запустить

```powershell
python evaluation/scripts/run_demo_smoke_checks.py
python evaluation/scripts/check_expected_text_traces.py
python evaluation/scripts/summarize_evaluation_status.py
```

## Упражнение

[../exercises/exercise-run-evaluation.md](../exercises/exercise-run-evaluation.md)

## Частые ошибки

- «Зелёный smoke = можно в прод»
- Пропуск evaluation перед Phase 3
- Чинить тесты, ослабляя ожидания

## Контрольные вопросы

1. Чем smoke отличается от полной регрессии?
2. Что делать при FAIL?
3. Что такое regression в этом репо?

## Ожидаемый результат

Студент запускает три скрипта и объясняет вывод summarize.
