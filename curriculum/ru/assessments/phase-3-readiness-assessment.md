# Оценка: готовность к Phase 3

**Цель:** gate на Agent Builder Kit — не «экзамен ради галочки».

## Таблица компетенций (все обязательны)

| # | Критерий | Как проверить |
|---|----------|----------------|
| 1 | Запуск демо | Smoke PASS; runbook без угадывания |
| 2 | Чтение trace | exercise-read-trace pass |
| 3 | Fail-closed | Оценка + пересказ bypass |
| 4 | Небезопасная автономия | Red flags; missing approval сценарий |
| 5 | Evaluation | Три скрипта + смысл FAIL |
| 6 | Change proposal | Шаблон или ревью proposal |
| 7 | Rollback | exercise-decide-rollback |
| 8 | Platform drift | exercise-identify-platform-drift |

Подробно: [../methodology/phase-3-entry-criteria.md](../methodology/phase-3-entry-criteria.md)

## Письменные вопросы (10 базовых)

Обязательны те же вопросы, что в beginner-assessment.

## Практические задания

```powershell
python evaluation/scripts/run_demo_smoke_checks.py
```

Наставник наблюдает: bypass + escalation trace narration.

## Распознавание опасных признаков

- «Phase 3 tools заменят evaluation»
- «Swarm раньше одного gated workflow»
- «Прототипы уже production»

## Объясни своими словами

Что **будет** Phase 3 и чего **не будет** (digital twin factory, cloud factory).

## Критерии pass

8/8 компетенций; lead sign-off; [../governance/phase-3-gate-policy.md](../governance/phase-3-gate-policy.md) чеклист закрыт.

## Критерии fail

Любая компетенция fail; hype-нарратив; нет подписи lead.

**«Не готов» — нормальный результат.** Продолжайте L7–L10.
