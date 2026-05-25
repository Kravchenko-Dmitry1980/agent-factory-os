# Критерии входа в Phase 3

Когда команде можно начинать **Agent Builder Kit** (Phase 3).

Phase 3 — **инструменты сборки gated workflow** по этой методологии. Это **не** автономная фабрика и **не** фабрика цифровых двойников.

---

## Обязательные компетенции (все)

| # | Критерий | Проверка |
|---|----------|----------|
| 1 | Оператор запускает демо | Smoke PASS; runbook без угадывания |
| 2 | Оператор читает trace | exercise-read-trace pass |
| 3 | Понимает fail-closed | Оценка + пересказ bypass |
| 4 | Видит небезопасную автономию | Red flags; missing approval |
| 5 | Запускает evaluation | Три скрипта + смысл FAIL |
| 6 | Пишет change proposal | Шаблон или ревью |
| 7 | Решает rollback | exercise-decide-rollback |
| 8 | Понимает platform drift | drift exercise |

---

## Командные gates

- [ ] Минимум один наставник pass operator или developer assessment
- [ ] Project lead pass lead assessment
- [ ] phase-3-readiness assessment подписан
- [ ] Нет открытых critical smoke FAIL на main
- [ ] Зафиксировано: Phase 3 **без** production deploy и digital twin factory

Политика: [../governance/phase-3-gate-policy.md](../governance/phase-3-gate-policy.md)  
Оценка: [../assessments/phase-3-readiness-assessment.md](../assessments/phase-3-readiness-assessment.md)

---

## Явно НЕ готовы, если

- Называют прототипы «production MVP»
- Не могут объяснить critic ≠ truth
- Планируют пропустить evaluation «Phase 3 сам проверит»
- Хотят swarm до одного mastered gated workflow

---

## Что даст Phase 3 (превью — не строится в 2.7)

- Сборка workflow из известных паттернов
- Дисциплина builder с fail-closed по умолчанию
- По-прежнему local-first

Фабрика цифровых двойников — **позже**, после дисциплины Builder Kit.

---

## Почему нельзя прыгать раньше

Ранний Phase 3 закрепляет drift: общий runtime, слабые gates, hype для стейкхолдеров. Студент перестаёт видеть **какой gate** спас от ошибки.

**«Не готов» — нормальный исход.** Продолжайте L7–L10.
