# Rollback — Demo Runner

**Phase 3.5.2** — как убрать runner без влияния на agent logic.

---

## Что можно удалить безопасно

Demo Runner — UX wrapper only. Удаление **не меняет** Review Assistant:

```powershell
cd C:\Dima\Projects\CURSOR\AGENT
Remove-Item -Recurse -Force demos\review-assistant-runner
```

Опционально удалить governance review:

```powershell
Remove-Item governance\PHASE_3_5_2_DEMO_RUNNER_IMPL_REVIEW.md
```

Откатить navigation updates в:

- `governance/README.md`
- `START_HERE_RU.md`
- `operator-playbooks/ru/README.md`
- `demos/review-assistant-hands-on/README.md`

---

## Что НЕ трогать при rollback

| Путь | Причина |
|------|---------|
| `prototypes-derived/review-assistant-thin/` | Agent logic |
| `evaluation/scripts/` | Baseline checks |
| Frozen specs | Governance |

---

## После rollback — как запускать демо

Прямые команды (как до Phase 3.5.2):

```powershell
python prototypes-derived/review-assistant-thin/minimal_demo.py --scenario happy
python evaluation/scripts/check_review_assistant_thin.py
```

Hands-on отчёт остаётся: `demos/review-assistant-hands-on/`.

---

## Признаки drift

Удалите runner если:

- операторы путают runner с production UI
- появляются запросы на plugin system / dynamic registry
- runner начинает импортировать project modules (нарушение границы)

Правильный ответ на drift — rollback + freeze plan review, не расширение runner.
