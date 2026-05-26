# Старт здесь (русский)

**Agent-OS Lab** — учебная инженерная лаборатория AI-агентов.  
Это главная точка входа для русскоязычных участников (Дмитрий, стажёры, операторы).

---

## Что это за проект

### Agent-OS Lab — это

- учебная инженерная **лаборатория** AI-агентов
- база знаний (`agent-os/`)
- набор **прототипов** с видимыми проверками (gates)
- набор безопасных **workflow**
- **учебная программа** (EN + RU)
- подготовка к будущему **Agent Builder Kit** (только после условий Phase 3)

### Agent-OS Lab — это НЕ

- готовая **фабрика агентов**
- фабрика **цифровых двойников**
- **production** runtime / SaaS
- система **AGI**
- клон Hermes / конкурент Claude
- «платформа», которую можно отдать клиенту как MVP

Подробнее: `agent-os/doctrine/system-positioning.md`

---

## С чего начать (рекомендуемый маршрут)

1. Прочитайте этот файл — **START_HERE_RU.md**
2. Откройте [curriculum/ru/student-guides/student-start-here.md](curriculum/ru/student-guides/student-start-here.md)
3. Быстрый запуск: [QUICKSTART_RU.md](QUICKSTART_RU.md)
4. Запустите review-loop demo **или** Review Assistant thin (команды ниже)
5. Запустите evaluation smoke check
6. Прочитайте один пример trace: `observability/examples/successful-review-trace.txt`
7. **Hands-on отчёт (Phase 3.5.1):** [demos/review-assistant-hands-on/DEMO_SUMMARY_FOR_DMITRY_RU.md](demos/review-assistant-hands-on/DEMO_SUMMARY_FOR_DMITRY_RU.md)
8. Перед Phase 3: [PHASE_3_WARNING_RU.md](PHASE_3_WARNING_RU.md)

Полная картина Phase 2: [PHASE_2_SUMMARY_RU.md](PHASE_2_SUMMARY_RU.md)

---

## Первые команды

```powershell
cd C:\Dima\Projects\CURSOR\AGENT
python prototypes/review-loop-agent/minimal-demo.py --scenario happy
python prototypes-derived/review-assistant-thin/minimal_demo.py --scenario happy
python evaluation/scripts/run_demo_smoke_checks.py
python evaluation/scripts/check_expected_text_traces.py
```

**Review Assistant thin (Phase 3.1+):** полный hands-on walkthrough — [demos/review-assistant-hands-on/README.md](demos/review-assistant-hands-on/README.md)

**Demo Runner v0.1 (FROZEN_WITH_NOTES):** меню и русское резюме — [demos/review-assistant-runner/README.md](demos/review-assistant-runner/README.md)

Freeze: [demos/review-assistant-runner/freeze/README.md](demos/review-assistant-runner/freeze/README.md)

```powershell
python demos/review-assistant-runner/demo_runner.py
python demos/review-assistant-runner/demo_runner.py --scenario happy
```

**Planned (not built):** Phase 3.5.3+ — см. [governance/phase-3-5-2-plan/README.md](governance/phase-3-5-2-plan/README.md)

Опционально — сводка статуса:

```powershell
python evaluation/scripts/summarize_evaluation_status.py
```

---

## Что считается хорошим результатом

| Шаг | Хорошо |
|-----|--------|
| Demo `happy` | В выводе есть Human decision, **Published True**, секция Audit |
| Demo `bypass-attempt` (позже) | **Published False** — bypass заблокирован |
| Smoke checks | Строка `Summary: PASS=12 FAIL=0` (или все строки PASS) |
| Trace check | `Summary: PASS=6 FAIL=0 total=6` |

**PASS** здесь значит: «демо и примеры trace ведут себя как задумано для обучения», а не «готово к production».

---

## Что делать при ошибке

1. Не правьте код «наугад».
2. [operator-playbooks/ru/ERRORS.md](operator-playbooks/ru/ERRORS.md)
3. Отчёты evaluation: `evaluation/reports/`
4. Откат и решения: `evolution/rollback-thinking/`
5. EN troubleshooting (при необходимости): `operator-playbooks/troubleshooting/common-errors.md`

---

## Что нельзя трогать новичку

| Путь | Почему |
|------|--------|
| `prototypes/shared/` | Риск «общего runtime» — platform drift |
| `integrations-real/shared/` | То же для адаптеров |
| `agent-os/` | Канон знаний — не править без promotion |
| `governance/` policies | Решения по фазам — читать, не переписывать |
| `evaluation/scripts/` | Не ослаблять проверки |
| `Books/` | Исходные корпуса — read-only |
| `experiments/` | Исследовательский периметр |

Список «что не делать»: [operator-playbooks/ru/WHAT_NOT_TO_DO.md](operator-playbooks/ru/WHAT_NOT_TO_DO.md)

---

## Навигация

| Документ | Зачем |
|----------|-------|
| [QUICKSTART_RU.md](QUICKSTART_RU.md) | Одна страница — быстрый запуск |
| [demos/review-assistant-hands-on/README.md](demos/review-assistant-hands-on/README.md) | Hands-on demo Review Assistant (Phase 3.5.1) |
| [demos/review-assistant-runner/README.md](demos/review-assistant-runner/README.md) | Demo Runner v0.1 — FROZEN_WITH_NOTES (Phase 3.5.2) |
| [demos/review-assistant-runner/freeze/README.md](demos/review-assistant-runner/freeze/README.md) | Freeze records demo-runner-v0.1 |
| [curriculum/ru/README.md](curriculum/ru/README.md) | Учебная программа |
| [operator-playbooks/ru/README.md](operator-playbooks/ru/README.md) | Мост для оператора |
| [governance/PHASE_3_START_CONDITIONS.md](governance/PHASE_3_START_CONDITIONS.md) | Условия старта Phase 3 |
| [agent-builder-kit/RU_SUMMARY.md](agent-builder-kit/RU_SUMMARY.md) | Agent Builder Kit v0.1 (спеки, Phase 3.0) |
| [governance/PHASE_3_0_BUILDER_KIT_REVIEW.md](governance/PHASE_3_0_BUILDER_KIT_REVIEW.md) | Review Phase 3.0 |
| [governance/phase-2-8/FINAL_PHASE_2_8_REPORT.md](governance/phase-2-8/FINAL_PHASE_2_8_REPORT.md) | Аудит готовности |
| [governance/phase-2-10/FINAL_PHASE_2_10_REPORT.md](governance/phase-2-10/FINAL_PHASE_2_10_REPORT.md) | Внешние репо — только исследование |
| [external-repos-triage/README.md](external-repos-triage/README.md) | Triage внешних skills/templates |

English entry: [README.md](README.md) → [agent-os/README.md](agent-os/README.md)
