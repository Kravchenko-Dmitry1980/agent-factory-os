# Короткий гид: безопасное изменение (RU)

Перед любой правкой в репозитории — даже «маленькой».

---

## Порядок (обязательный)

1. **Change proposal** — заполнить шаблон (на бумаге или в MD).
2. **Impact** — какие gates и демо затронуты.
3. **Evaluation** — smoke **до** и **после**.
4. **Trace** — сравнить с примером good/bad.
5. **Решение** — rollback или оставить; записать результат.

---

## Шаблон и политики

| Ресурс | Путь |
|--------|------|
| Шаблон proposal | `evolution/change-proposals/change-template.md` |
| Quality gates | `evaluation/quality-gates/quality-gate-checklist.md` |
| Примеры trace | `observability/examples/` |
| Rollback мышление | `evolution/rollback-thinking/rollback-vs-patch.md` |
| EN runbook | [../change-guides/how-to-change-safely.md](../change-guides/how-to-change-safely.md) |

---

## Когда rollback обязателен

- Пропал `approval_requested` на publish path
- Smoke FAIL после «быстрой правки»
- Auto-approve появился в trace
- Увеличили retry без proposal и без эскалации

Упражнение: [curriculum/ru/exercises/exercise-decide-rollback.md](../../curriculum/ru/exercises/exercise-decide-rollback.md)

---

## Чего не делать

- Патч «вслепую» при FAIL
- Менять `prototypes/shared/gates.py` без mentor + smoke
- Пропускать evaluation «нет времени»
- Начинать Phase 3 код без [PHASE_3_START_CONDITIONS.md](../../governance/PHASE_3_START_CONDITIONS.md)
