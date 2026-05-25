# Карта курса

Полный маршрут обучения — уровни 0–10.

Каждый уровень связан с модулями, упражнениями и материалами operator-playbooks.

---

## Уровень 0 — Ориентация

**Цель:** понять, что это за проект и чем он не является.

| Ресурс | Путь |
|--------|------|
| Модуль | [modules/module-00-orientation.md](modules/module-00-orientation.md) |
| Читать | `agent-os/doctrine/system-positioning.md` |
| Оператор | [../../operator-playbooks/README.md](../../operator-playbooks/README.md) |
| Упражнение | [exercises/exercise-run-first-demo.md](exercises/exercise-run-first-demo.md) |
| Время | ~30 мин |

---

## Уровень 1 — Основы AI-агентов

**Цель:** агент = workflow с инструментами, памятью, проверками и лимитами.

| Ресурс | Путь |
|--------|------|
| Модуль | [modules/module-01-what-is-an-ai-agent.md](modules/module-01-what-is-an-ai-agent.md) |
| Урок | [lessons/lesson-fail-closed.md](lessons/lesson-fail-closed.md) (превью) |
| Демо | `prototypes/review-loop-agent/minimal-demo.py` |

---

## Уровень 2 — Основы безопасности

**Цель:** fail-closed, одобрение, проверка, участие человека.

| Ресурс | Путь |
|--------|------|
| Модули | [module-03-verification-first.md](modules/module-03-verification-first.md), [module-04-human-approval.md](modules/module-04-human-approval.md), [module-06-fail-closed-execution.md](modules/module-06-fail-closed-execution.md) |
| Уроки | critic, LLM, approval в `lessons/` |
| Упражнение | [exercise-block-unsafe-action.md](exercises/exercise-block-unsafe-action.md) |

---

## Уровень 3 — Прототипы

**Цель:** запускать маленькие системы и наблюдать поведение.

| Ресурс | Путь |
|--------|------|
| Модуль | [modules/module-05-bounded-memory.md](modules/module-05-bounded-memory.md) |
| Runbook | [../../operator-playbooks/runbooks/run-prototypes.md](../../operator-playbooks/runbooks/run-prototypes.md) |
| Упражнения | первое демо, break review loop |

---

## Уровень 4 — Связанные workflow

**Цель:** несколько шагов в одном безопасном процессе.

| Ресурс | Путь |
|--------|------|
| Модуль | [modules/module-07-workflow-orchestration.md](modules/module-07-workflow-orchestration.md) |
| Runbook | [../../operator-playbooks/runbooks/run-integration-workflows.md](../../operator-playbooks/runbooks/run-integration-workflows.md) |
| Упражнение | [exercise-trigger-escalation.md](exercises/exercise-trigger-escalation.md) |

---

## Уровень 5 — Реальные адаптеры

**Цель:** границы с внешним миром (по умолчанию mock).

| Ресурс | Путь |
|--------|------|
| Модуль | [modules/module-08-real-integrations.md](modules/module-08-real-integrations.md) |
| Runbook | [../../operator-playbooks/runbooks/run-real-adapters.md](../../operator-playbooks/runbooks/run-real-adapters.md) |
| Упражнение | [exercise-detect-bad-llm-output.md](exercises/exercise-detect-bad-llm-output.md) |

---

## Уровень 6 — Наблюдаемость и traces

**Цель:** читать trace; понимать сбои.

| Ресурс | Путь |
|--------|------|
| Модуль | [modules/module-09-observability-and-traces.md](modules/module-09-observability-and-traces.md) |
| Урок | [lessons/lesson-audit-lineage.md](lessons/lesson-audit-lineage.md) |
| Упражнение | [exercise-read-trace.md](exercises/exercise-read-trace.md) |

---

## Уровень 7 — Проверка поведения

**Цель:** убедиться, что поведение осталось безопасным.

| Ресурс | Путь |
|--------|------|
| Модуль | [modules/module-10-evaluation-and-regression.md](modules/module-10-evaluation-and-regression.md) |
| Урок | [lessons/lesson-regression.md](lessons/lesson-regression.md) |
| Упражнение | [exercise-run-evaluation.md](exercises/exercise-run-evaluation.md) |

---

## Уровень 8 — Безопасное развитие системы

**Цель:** менять систему, не ломая gates.

| Ресурс | Путь |
|--------|------|
| Модуль | [modules/module-11-safe-evolution.md](modules/module-11-safe-evolution.md) |
| Упражнения | change proposal, rollback, platform drift |
| Evolution | `evolution/change-proposals/` |

---

## Уровень 9 — Готовность оператора

**Цель:** уверенно работать по playbooks.

| Ресурс | Путь |
|--------|------|
| Модуль | [modules/module-12-operator-practice.md](modules/module-12-operator-practice.md) |
| Оператор | [../../operator-playbooks/](../../operator-playbooks/) |
| Оценка | [assessments/operator-assessment.md](assessments/operator-assessment.md) |

---

## Уровень 10 — Готовность к Phase 3

**Цель:** понять, когда можно начинать Agent Builder Kit.

| Ресурс | Путь |
|--------|------|
| Модуль | [modules/module-13-phase-3-readiness.md](modules/module-13-phase-3-readiness.md) |
| Методика | [methodology/phase-3-entry-criteria.md](methodology/phase-3-entry-criteria.md) |
| Оценка | [assessments/phase-3-readiness-assessment.md](assessments/phase-3-readiness-assessment.md) |

---

## Визуальная карта

[diagrams/learning-ladder.md](diagrams/learning-ladder.md)

---

## По роли (краткий путь)

| Роль | Трек |
|------|------|
| Стажёр | [role-based-tracks/track-intern.md](role-based-tracks/track-intern.md) |
| AI-разработчик | [role-based-tracks/track-ai-developer.md](role-based-tracks/track-ai-developer.md) |
| Оператор Cursor | [role-based-tracks/track-cursor-operator.md](role-based-tracks/track-cursor-operator.md) |
| Руководитель | [role-based-tracks/track-project-lead.md](role-based-tracks/track-project-lead.md) |
| AI-архитектор | [role-based-tracks/track-ai-architect.md](role-based-tracks/track-ai-architect.md) |
