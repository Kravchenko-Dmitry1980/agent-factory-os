# Phase 2.7 — Curriculum Review

**Date:** 2026-05-25  
**Scope:** `curriculum/`  
**Status:** Phase 2.7 complete — teachable methodology, no new code or automation

---

## Executive Summary

Phase 2.7 adds structured training: course map (Levels 0–10), 14 modules, 10 lessons, 10 exercises, 5 assessments, 5 workshops, 6 teacher-note guides, 5 student guides, 5 role tracks, 6 methodology docs, 5 Mermaid diagrams, 5 governance docs. Reuses operator-playbooks, evaluation scripts, prototypes — does not duplicate runtime. No code, scripts, CI, or Agent Factory created.

---

## Required Review Questions

### Can a beginner follow the route?

**Yes.** `student-start-here.md` → `course-map.md` Level 0 → module-00 → exercise-run-first-demo. Role tracks shorten path without skipping L0–L2 safety.

### Does the curriculum explain hard terms simply?

**Yes.** `student-glossary.md`, 10 plain-language lessons, teacher notes for agents/governance/fail-closed. Modules repeat checkpoint questions.

### Are exercises practical?

**Yes.** All tied to real demo commands and trace files. exercise-break-review-loop explicitly observe-only (no code break). Pass/fail criteria per exercise.

### Are assessments useful?

**Yes.** Five role-aligned assessments with written + practical + red flags + explain-in-your-own-words. Phase-3 readiness ties to entry criteria.

### Does it avoid hype?

**Yes.** `anti-hype-learning-policy.md`, teacher note on hype, README explicit NOT list (AGI, swarms, replace humans, model training).

### Does it prevent early platform thinking?

**Yes.** `practice-before-platform.md`, drift exercise, no-platform-drift-in-training, phase-3 gate excludes factory until competencies met.

### Are Phase 3 entry criteria clear?

**Yes.** `methodology/phase-3-entry-criteria.md` lists 8 competencies + team gates; diagram; assessment; gate policy. Digital twin factory explicitly deferred.

---

## Curriculum Clarity

| Area | Rating |
|------|--------|
| course-map | High |
| modules | High — consistent template |
| lessons | High — simple Q&A format |
| exercises | High — observable demos |
| role tracks | High |

---

## Beginner Friendliness

Strong entry funnel; glossary; command list; small-steps method. Risk: file count (~75) — mitigated by course-map and tracks.

---

## Practical Usefulness

Direct links to PowerShell commands matching repo demos. Workshops reuse operator-playbook agendas. Teachers have misunderstanding catalog.

---

## Role Coverage

Intern, developer, cursor operator, lead, architect — each with modules, exercises, checkpoint.

---

## Over-Documentation Risk

**Medium.** Overlap with operator-playbooks intentional: curriculum = teach systematically; playbooks = operate daily. Cross-links reduce duplication drift.

---

## Teaching Hype Risk

**Low** with policies; teacher must enforce anti-hype exercises live.

---

## Phase 3 Readiness Status

**Criteria defined; implementation not started.** Team must pass assessments before Builder Kit — documented in gate policy. Curriculum does not claim team is ready by default.

---

## Gaps Before Agent Builder Kit

| Gap | Mitigation in 2.7 |
|-----|-------------------|
| No Builder Kit content yet | Explicit deferral + entry criteria |
| Assessment is manual | By design — no LMS |
| Cheat sheet for experts | Could add later optional 1-pager — not required now |
| Russian localization | English curriculum; user rules allow RU responses in chat |

---

## New Automation?

**No.** No new scripts. References existing evaluation scripts only.

---

## Platform Drift?

**No.** Methodology forbids framework-as-capstone; phase-3 gate blocks premature factory.

---

## Strongest Curriculum Area

**Module + exercise + demo triangle** — every module lists commands; exercises verify with pass criteria; lessons explain why.

---

## Weakest Curriculum Area

**Potential overlap fatigue** between curriculum, operator-playbooks, and agent-os — student must trust course-map as spine.

---

## What Was NOT Modified

- `agent-os/`, `Books/`, `experiments/` — untouched
- `prototypes/`, `integrations-real/` code — untouched
- `evaluation/scripts/` — untouched
- `operator-playbooks/` — untouched (linked only)
- No git hooks, CI, dashboards, web UI

---

## Modules Created Summary

| Folder | Count |
|--------|-------|
| README + course-map | 2 |
| modules | 14 |
| lessons | 10 |
| exercises | 10 |
| assessments | 5 |
| workshops | 5 |
| teacher-notes | 6 |
| student-guides | 5 |
| role-based-tracks | 5 |
| methodology | 6 |
| diagrams | 5 |
| governance | 5 |
| PHASE_2_7 review | 1 |

**Total:** ~79 new files under curriculum + 1 governance review.

---

## Validation Checklist

| Rule | Status |
|------|--------|
| Simple language | pass |
| No new automation | pass |
| No platform drift | pass |
| Teaching quality (goal/read/run/checkpoint) | pass |

---

## Recommended Next Step

New student: [curriculum/student-guides/student-start-here.md](../curriculum/student-guides/student-start-here.md)  
Facilitator: [curriculum/workshops/workshop-30-min-intro.md](../curriculum/workshops/workshop-30-min-intro.md)

Phase 3: only after [phase-3-entry-criteria.md](../curriculum/methodology/phase-3-entry-criteria.md) sign-off.
