# Урок: Регрессия

## Что это?

**Регрессия** — безопасное поведение, которое работало, **перестало** работать после изменения (код, промпт, лимиты).

## Почему это важно?

Без regression checks изменения «тихо» снимают gates — особенно при platform drift.

## Что может пойти не так?

- Smoke не запускали после правки
- Ослабили ожидаемые строки в trace-check
- «Зелёный» только happy path

## Как это проверить?

Smoke + check_expected_text_traces; смотрите regression examples.

`evaluation/trace-comparison/trace-regression-examples.md`

```powershell
python evaluation/scripts/run_demo_smoke_checks.py
```

## Какое демо это показывает?

- evaluation scripts
- [../exercises/exercise-run-evaluation.md](../exercises/exercise-run-evaluation.md)
