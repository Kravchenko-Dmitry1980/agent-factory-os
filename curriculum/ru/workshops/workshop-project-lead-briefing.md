# Воркшоп: брифинг для руководителя

## Аудитория

Project lead, EM.

## Длительность

45 минут

## Цель

Positioning, evaluation status, Phase 3 gate — без hype.

## План

| Мин | Тема |
|-----|------|
| 0–10 | system-positioning + curriculum README (что НЕ) |
| 10–20 | Демо happy + bypass (наблюдение) |
| 20–30 | summarize_evaluation_status |
| 30–45 | phase-3-entry-criteria + gate policy |

## Какие файлы открыть

- `agent-os/doctrine/system-positioning.md`
- [../methodology/phase-3-entry-criteria.md](../methodology/phase-3-entry-criteria.md)
- [../governance/phase-3-gate-policy.md](../governance/phase-3-gate-policy.md)

## Какие команды запустить

```powershell
python prototypes/review-loop-agent/minimal-demo.py --scenario bypass-attempt
python evaluation/scripts/summarize_evaluation_status.py
```

## Вопросы для обсуждения

1. Где риск назвать демо production?
2. Кто подписывает Phase 3?
3. Какие метрики **не** substitute для trace?

## Ожидаемый результат обучения

Lead может объяснить задержку Phase 3 одним абзацом с критериями.
