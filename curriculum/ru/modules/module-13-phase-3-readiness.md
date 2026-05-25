# Модуль 13 — Готовность к Phase 3

## Цель

Понять, когда безопасно начинать **Agent Builder Kit** — и когда рано.

## Простое объяснение

Phase 3 — **инструменты сборки gated workflow из известных паттернов**, не автономная фабрика и не фабрика цифровых двойников. Переход — по критериям и подписи lead, не по желанию «ускориться».

## Ключевые идеи

- 8 компетенций (см. methodology)
- phase-3-readiness assessment
- phase-3-gate-policy
- «Не готов» — нормальный исход

## Что прочитать

- [../methodology/phase-3-entry-criteria.md](../methodology/phase-3-entry-criteria.md)
- [../governance/phase-3-gate-policy.md](../governance/phase-3-gate-policy.md)
- [../assessments/phase-3-readiness-assessment.md](../assessments/phase-3-readiness-assessment.md)

## Что запустить

Под наблюдением наставника:

```powershell
python evaluation/scripts/run_demo_smoke_checks.py
python prototypes/review-loop-agent/minimal-demo.py --scenario bypass-attempt
python prototypes/integrations/escalation-workflow/minimal-demo.py --scenario retry-storm
```

## Упражнение

[../assessments/phase-3-readiness-assessment.md](../assessments/phase-3-readiness-assessment.md)

## Частые ошибки

- «Прототипы = MVP в прод»
- Планировать swarm до одного gated workflow
- Пропустить evaluation «потому что Phase 3 сам проверит»

## Контрольные вопросы

1. Что такое Agent Builder Kit в одном предложении?
2. Назовите 3 критерия «явно не готов».
3. Кто подписывает gate?

## Ожидаемый результат

Студент честно оценивает команду по таблице 8 компетенций без маркетинговых формулировок.
