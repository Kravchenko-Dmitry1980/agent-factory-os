# Следующие практические шаги

**Дата:** 2026-05-26  
**После:** Phase 3.5.1 Hands-on Demo Report

---

## Рекомендация (кратко)

**Сначала Option C (Demo Runner plan), потом Option A (Interactive CLI plan).**

Task Triage implementation (Option B) — **после** того, как Review Assistant станет «ощутимым руками» для оператора.

---

## Option A — Interactive CLI для Review Assistant

**Описание:** режим, где оператор вводит текст задачи вручную (stdin или `--task "..."`).

| | |
|--|--|
| **Benefits** | Система становится touchable; без UI; относительно просто |
| **Risks** | Может потянуть изменения behavior; нужен Phase 3.5.x-Plan + GO/NO-GO |
| **Gates** | Те же: verification, approval, no auto-publish |

**Не делать без плана:** иначе risk scope creep.

---

## Option B — Task Triage Thin Implementation Plan

**Описание:** продолжить roadmap — Phase 3.6-Plan для второго агента.

| | |
|--|--|
| **Benefits** | Второй agent line движется по плану |
| **Risks** | Всё ещё abstract для оператора; нет «руками потрогал triage» |
| **Status** | Specs v0.1 frozen, impl NOT_STARTED |

**Когда:** после UX-слоя для Review Assistant или параллельно только plan (no code).

---

## Option C — Demo Runner (рекомендуется первым)

**Описание:** один wrapper-скрипт или documented flow:

- выбор сценария из меню;
- запуск `minimal_demo.py`;
- печать **читаемого русского резюме** (decision, delivered, ключевые trace events);
- опционально сохранение transcript.

| | |
|--|--|
| **Benefits** | Лучше UX **без** изменения agent logic; низкий risk |
| **Risks** | Минимальные, если runner — только обёртка |
| **Phase** | Phase 3.5.2-Plan — plan only, then impl if GO |

---

## Рекомендуемая последовательность

```text
1. Freeze/commit текущее состояние (task-triage specs, hands-on report)
2. Phase 3.5.2-Plan — Demo Runner / operator-friendly output (plan only)
3. Phase 3.5.2-Impl — Demo Runner (if GO) — wrapper, no logic change
4. Phase 3.5.3-Plan — Interactive CLI (plan only)
5. Phase 3.6-Plan — Task Triage thin impl (plan only)
6. Phase 3.6-Impl — only after explicit GO
```

---

## Что **не** рекомендуется сейчас

| Action | Why |
|--------|-----|
| Сразу писать Task Triage code | Specs frozen, но UX gap Review Assistant важнее для «ощущения» |
| Сразу делать web UI | High scope, Operator Console backlog |
| Менять minimal_demo.py без freeze review | Protected behavior |
| Live provider в CI | Explicit manual only |

---

## Immediate next prompt (для Cursor)

**Phase 3.5.2-Plan — Demo Runner / Operator-Friendly CLI Output**

Deliverables (plan only):

- where runner lives (`demos/` vs `evaluation/scripts/`)
- no agent logic change rule
- Russian summary format spec
- scenario menu design
- rollback plan
- GO/NO-GO

**Not implementation yet.**

---

## Связанные документы

- [DEMO_SUMMARY_FOR_DMITRY_RU.md](DEMO_SUMMARY_FOR_DMITRY_RU.md)
- [UX_GAPS_RU.md](UX_GAPS_RU.md)
- [task-triage sign-off PHASE_3_6_READINESS_NOTE.md](../../agent-builder-kit/templates/task-triage-agent/sign-off/PHASE_3_6_READINESS_NOTE.md)
