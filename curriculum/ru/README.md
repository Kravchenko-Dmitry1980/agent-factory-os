# Учебная программа Agent-OS (Phase 2.7-RU)

**Статус:** методика обучения — не код, не «фабрика агентов», не production-платформа.

**Быстрый вход:** [../../START_HERE_RU.md](../../START_HERE_RU.md) · [CHEATSHEET.md](CHEATSHEET.md) · [../../PHASE_3_WARNING_RU.md](../../PHASE_3_WARNING_RU.md)

---

## Что это

Учебная программа по **безопасным AI-workflow**: проверка перед доверием, одобрение человеком, ограниченная память, fail-closed (безопасная остановка при сомнении), читаемые trace (следы выполнения), локальная проверка поведения и безопасные изменения. Репозиторий — учебник и лаборатория.

---

## Для кого

| Аудитория | Трек |
|-----------|------|
| Стажёр / новичок | [role-based-tracks/track-intern.md](role-based-tracks/track-intern.md) |
| AI-разработчик | [role-based-tracks/track-ai-developer.md](role-based-tracks/track-ai-developer.md) |
| Оператор Cursor | [role-based-tracks/track-cursor-operator.md](role-based-tracks/track-cursor-operator.md) |
| Руководитель проекта | [role-based-tracks/track-project-lead.md](role-based-tracks/track-project-lead.md) |
| Изучающий AI-архитектуру | [role-based-tracks/track-ai-architect.md](role-based-tracks/track-ai-architect.md) |

---

## Что вы изучите

- Что такое AI-агент **на практике** (workflow + инструменты + проверки — не «магия»)
- Почему AI-системы ломаются тихо
- Как проверять вывод до доверия
- Как правильно использовать одобрение человеком
- Как читать trace и замечать плохое поведение
- Как запускать локальные проверки (evaluation)
- Как менять систему, не ломая защитные правила
- Как не уйти в platform drift (переусложнение «платформой»)
- Когда команда готова к Phase 3 (Agent Builder Kit)

---

## Чего вы пока НЕ изучите

- Обучение или fine-tuning моделей
- Рой агентов без проверок и одобрения
- Production-развёртывание в масштабе
- RAG / векторные пайплайны
- AGI и сценарии «заменить человека»
- Фабрика цифровых двойников (позже Phase 3+)
- Реализация Agent Factory (Phase 3 — только после критериев)

---

## Почему начинаем с маленьких систем

Большие платформы прячут ошибки. Маленькие демо (~200 строк) показывают **какой именно gate сработал**. Governance учат, видя его в trace, а не по рекламным формулировам.

---

## Почему нельзя верить AI без проверки

**Критик ≠ истина.** Критик оценивает форму или стиль, а не факты.

**Вывод LLM ≠ истина.** Красивый JSON не гарантирует правильность.

**«Запустилось» ≠ безопасно.** Exit code 0 не значит, что опасное действие разрешено.

Типичная поломка — правдоподобный неправильный ответ, а не падение процесса.

---

## Почему не строим «фабрику агентов» слишком рано

Пока не освоены один workflow с gates, общий runtime и «много агентов» ослабляют проверки. Phase 3 (Agent Builder Kit) — **сборка известных безопасных паттернов**, а не автономная фабрика. Подробнее: [methodology/phase-3-entry-criteria.md](methodology/phase-3-entry-criteria.md).

---

## Как проходить курс

1. Прочитайте [course-map.md](course-map.md) — уровни 0–10.
2. Начните с [student-guides/student-start-here.md](student-guides/student-start-here.md).
3. Пройдите [modules/module-00-orientation.md](modules/module-00-orientation.md).
4. Выберите трек по роли.
5. После каждого модуля — упражнение и контрольные вопросы.
6. Фиксируйте наблюдения в [student-guides/student-learning-log-template.md](student-guides/student-learning-log-template.md).

Практика: [../operator-playbooks/start-here/first-30-minutes.md](../../operator-playbooks/start-here/first-30-minutes.md) (англ., команды те же).

---

## Это НЕ курс про

- AGI
- Автономные рои без человека
- Замену людей
- Production-платформы «из коробки»
- Обучение моделей

---

## Это курс про

- Безопасный дизайн AI-workflow
- Основы архитектуры агентов
- Проверку (verification) перед доверием
- Governance (правила управления системой)
- Безопасную эволюцию системы

---

## Навигация

| С чего начать | Дальше |
|-------------|--------|
| [course-map.md](course-map.md) | Полная лестница уровней 0–10 |
| [student-guides/student-start-here.md](student-guides/student-start-here.md) | Вход для студента |
| [modules/module-00-orientation.md](modules/module-00-orientation.md) | Первый модуль |

Английская версия (без изменений): [../README.md](../README.md)

Обзор локализации: [../../governance/PHASE_2_7_RU_LOCALIZATION_REVIEW.md](../../governance/PHASE_2_7_RU_LOCALIZATION_REVIEW.md)

Условия Phase 3: [../../governance/PHASE_3_START_CONDITIONS.md](../../governance/PHASE_3_START_CONDITIONS.md)  
Оператор (RU мост): [../../operator-playbooks/ru/README.md](../../operator-playbooks/ru/README.md)

---

## Связь с фазами

```
Phase 2.6  operator-playbooks  → ежедневная работа оператора
Phase 2.7  curriculum          → системное обучение
Phase 3    Agent Builder Kit   → только после phase-3-entry-criteria
```

Критерии входа: [methodology/phase-3-entry-criteria.md](methodology/phase-3-entry-criteria.md)
