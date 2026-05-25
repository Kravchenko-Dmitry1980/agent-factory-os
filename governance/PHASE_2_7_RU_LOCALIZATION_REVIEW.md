# Phase 2.7-RU — Localization Review

**Date:** 2026-05-25  
**Scope:** `curriculum/ru/` Russian educational localization  
**English source:** `curriculum/` (unchanged except language navigation block)

---

## Completeness

| Area | EN files | RU files | Mirror OK? |
|------|----------|----------|------------|
| Root | README, course-map | README, course-map | Yes |
| modules | 14 | 14 | Yes |
| lessons | 10 | 10 | Yes |
| exercises | 10 | 10 | Yes |
| assessments | 5 | 5 | Yes |
| workshops | 5 | 5 | Yes |
| teacher-notes | 6 | 6 | Yes |
| student-guides | 5 | 5 | Yes |
| role-based-tracks | 5 | 5 | Yes |
| methodology | 6 | 6 | Yes |
| diagrams | 5 | 5 | Yes |
| governance | 5 | 5 | Yes |

**Total RU curriculum files:** 77 + this review references EN root navigation only.

---

## Required review questions

| Question | Answer |
|----------|--------|
| Is the Russian version complete? | **Yes** — structure mirrors EN `curriculum/`. |
| Is the language simple enough? | **Yes** — short sentences; terms explained on first use. |
| Are technical terms explained? | **Yes** — fail-closed, trace, drift, rollback in glossary and lessons. |
| Was the English version preserved? | **Yes** — only `curriculum/README.md` gained a Languages block; no EN file deleted/renamed/moved. |
| Did localization create new concepts? | **No** — same phases, gates, exercises, criteria. |
| Did localization weaken safety rules? | **No** — deny-first, Phase 3 gate, anti-hype retained. |
| Is it usable for Russian-speaking interns? | **Yes** — track-intern, workshops, student-start-here in RU. |

---

## Beginner friendliness

**Strengths:** Plain Russian in README and modules; glossary; learning log template; «что НЕ изучаем» upfront.

**Weakest area:** Some links still point to English operator-playbooks and agent-os doctrine (intentional — those corpora were out of scope). Students need one sentence from mentor: «команды те же, текст playbook можно читать с переводчиком».

---

## Terminology consistency

| Term | RU usage |
|------|----------|
| fail-closed | fail-closed + «безопасная остановка» |
| trace | trace + «след выполнения» |
| governance | governance + «правила управления» |
| platform drift | platform drift + «уход в платформу» |
| rollback | rollback + «откат» |
| evaluation | проверка поведения |

Commands and repo paths remain English/ASCII as required.

---

## Hype / platform drift check

- No new automation or scripts added.
- RU text does not label repo as Agent Factory or production platform.
- Phase 3 criteria unchanged (8 competencies + lead sign-off).
- Capstone remains smoke + proposal + traces, not unified runtime.

---

## English files modified?

| File | Change |
|------|--------|
| `curriculum/README.md` | Added `## Languages` navigation only |
| All other EN curriculum | Unchanged |

---

## What was NOT modified (per boundary)

- `prototypes/`, `integrations-real/`, `observability/`, `evolution/`, `evaluation/` (runtime)
- `agent-os/`, `Books/`
- No new scripts, CI, or architecture layers

---

## Strongest RU localization area

**Modules + exercises** — full section template (цель, простое объяснение, шаги, pass/fail) aligned with EN pedagogy.

## Weakest RU localization area

**External EN-only dependencies** (operator-playbooks body text, doctrine files) — RU curriculum links to them without translating those trees (by design).

---

## Sign-off recommendation

Phase 2.7-RU **accepted** for teaching use. Recommend pilot with one intern cohort; collect mentor notes on playbook language friction.
