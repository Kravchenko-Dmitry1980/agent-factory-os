# Russian Curriculum Readiness

**Source review:** [../PHASE_2_7_RU_LOCALIZATION_REVIEW.md](../PHASE_2_7_RU_LOCALIZATION_REVIEW.md)  
**Scope:** `curriculum/ru/`

---

## Summary verdict

| Question | Answer |
|----------|--------|
| Complete? | **Yes** — 78 files mirror EN structure |
| Beginner-friendly? | **Yes** — plain Russian, glossary, student-start-here |
| Safety preserved? | **Yes** — anti-hype, phase-3 gate, fail-closed pedagogy intact |
| Key terms explained? | **Yes** — glossary + lessons |
| Prepares for Phase 3? | **Yes** — module-13, phase-3-entry-criteria, assessments |
| EN dependencies problem? | **Medium** — operator-playbooks + agent-os doctrine EN; mitigated by mentor |
| Translate later? | Optional: operator first-30-min RU; not blocking v0.1 specs |

---

## Area table

| Area | Status | Risk | Recommendation |
|------|--------|------|----------------|
| README / course-map | Ready | Low | Entry point for RU interns |
| Modules 00–13 | Ready | Low | Teach L0–L2 before kit |
| Lessons (10) | Ready | Low | Use in workshops |
| Exercises (10) | Ready | Low | Mandatory hands-on |
| Assessments (5) | Ready | Medium | Mentor for sign-off |
| Workshops (5) | Ready | Low | intern-onboarding first |
| Teacher notes | Ready | Low | Train mentors in RU |
| Student guides | Ready | Low | command-list unchanged paths |
| Role tracks | Ready | Low | Match org role |
| Methodology | Ready | Low | phase-3 criteria strict |
| RU governance docs | Ready | Low | Align with phase-2-8 |
| Links to EN playbooks | Partial | **Medium** | One-line mentor note: same commands |
| Links to agent-os doctrine | Partial | Medium | Read with translator or bilingual mentor |
| One-page cheat sheet | **Missing** | Low | Optional `student-cheatsheet-ru.md` later |
| RU operator-playbooks | **Missing** | Medium | Phase 3.1+ or parallel doc project |

---

## Navigation gaps

- `curriculum/README.md` has Languages block → `ru/` ✓
- `governance/phase-2-8/` not yet linked from `curriculum/ru/README.md` — add cross-link in doc pass (optional)

## English link friction

**Affected paths:** `operator-playbooks/start-here/first-30-minutes.md`, runbooks, some doctrine files.

**Mitigation for Phase 3:**

1. RU curriculum commands identical — no translation needed for PowerShell.
2. Mentor runs first demo alongside RU text.
3. Builder Kit v0.1 specs should be **bilingual or RU-primary** when created (user choice).

---

## Phase 3 readiness (RU audience)

**CONDITIONAL GO** for RU-speaking interns **if** mentor available.

Without mentor: **NO-GO** for unsupervised Phase 3 participation (assessment integrity).

---

## Recommended additions (non-blocking)

| Item | Priority |
|------|----------|
| `curriculum/ru/student-guides/student-cheatsheet-one-page.md` | P2 |
| RU summary of `first-30-minutes.md` | P2 |
| Link phase-2-8 README from curriculum/ru/README | P3 |
