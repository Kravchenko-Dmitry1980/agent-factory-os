# UX Gaps — Review Assistant Hands-on

**Дата:** 2026-05-26

Пробелы UX после ручного demo. **Не баги** — осознанные gaps текущей lab-фазы.

---

## Таблица gaps

| Gap | Why It Matters | Possible Future Fix |
|-----|----------------|---------------------|
| **No free-form user input** | Оператор не может проверить «свою» задачу | Interactive CLI mode (Phase 3.5.x+) |
| **No interactive approval** | Approval симулируется — не чувствуется HITL | Prompt Y/N или timeout в CLI |
| **No readable final report** | Trace полезен dev'у, не оператору | Demo Runner: русское резюме после run |
| **No scenario selector menu** | Нужно помнить имена `--scenario` | Demo Runner с меню 1–9 |
| **No saved demo transcript** | Нельзя показать команде «вот что было» | Export trace → .txt / .md автоматически |
| **No simple Russian explanation after run** | После команды — только EN/technical | Post-run summary block на русском |
| **No UI** | Не onboarding-friendly для non-dev | Minimal web/terminal UI — отдельная фаза |
| **No operator dashboard** | Нет статуса «что frozen, что PASS» | Operator Console — backlog |
| **No Task Triage demo** | Второй агент только specs | Phase 3.6+ thin impl |
| **No comparison view** | Сложно сравнить happy vs blocked side-by-side | Runner: `--compare` или batch report |
| **No «what to run first» in terminal** | Новый человек теряется | `--help` с learning path + link на demos/ |
| **START_HERE vs thin demo drift** | START_HERE ещё указывает на старый review-loop | Navigation sync (частично в Phase 3.5.1) |

---

## Приоритеты (практические)

| Priority | Gap | Effort | Risk |
|----------|-----|--------|------|
| **P1** | Readable Russian summary after run | Low | Low — no agent logic change |
| **P1** | Scenario menu / Demo Runner | Low–Medium | Low if read-only wrapper |
| **P2** | Interactive CLI input | Medium | Medium — needs plan, gates unchanged |
| **P2** | Saved transcript | Low | Low |
| **P3** | UI / dashboard | High | High — scope creep |
| **P3** | Task Triage demo | High | Medium — separate agent line |

---

## Gaps, которые **не** надо закрывать сейчас

| Gap | Почему подождать |
|-----|------------------|
| Production UI | Нет production scope |
| Cloud provider UX | Out of Phase 3 |
| Multi-agent orchestrator | Explicit anti-pattern |
| Real ticket integration | Execution boundary |

---

## Связь с governance

UX improvements должны идти через **plan → GO/NO-GO**, не ломая frozen thin v0.3 behavior без change proposal.

Рекомендация: [NEXT_PRACTICAL_STEPS_RU.md](NEXT_PRACTICAL_STEPS_RU.md).
