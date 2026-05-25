# Phase 3 Entry Criteria

When the team may safely start **Agent Builder Kit** (Phase 3).

Phase 3 is **composable agent construction tooling** guided by this methodology — **not** autonomous factory, **not** digital twin factory yet.

---

## Required competencies (all must pass)

| # | Criterion | Verification |
|---|-----------|--------------|
| 1 | Operator can run demos | Smoke PASS; runbook without guessing |
| 2 | Operator can read trace | exercise-read-trace pass |
| 3 | Operator can explain fail-closed | Assessment + bypass demo narration |
| 4 | Operator can detect unsafe autonomy | Red flag exercises; missing approval scenario |
| 5 | Operator can run evaluation | Three evaluation scripts + interpret FAIL |
| 6 | Operator can write change proposal | Template exercise or reviewed proposal |
| 7 | Operator can decide rollback | decide-rollback exercise; rollback runbook |
| 8 | Operator understands platform drift | drift exercise; can reject shared runtime |

---

## Team-level gates

- [ ] At least one mentor passed operator or developer assessment
- [ ] Project lead passed lead assessment
- [ ] phase-3-readiness assessment signed
- [ ] No open critical smoke failures on main branch
- [ ] Documented agreement: Phase 3 scope excludes production deploy + digital twins factory

Policy: [../governance/phase-3-gate-policy.md](../governance/phase-3-gate-policy.md)

Assessment: [../assessments/phase-3-readiness-assessment.md](../assessments/phase-3-readiness-assessment.md)

---

## Explicitly NOT ready if

- Team calls prototypes "production MVP"
- Cannot explain critic != truth
- Plans to skip evaluation "because Phase 3 tools will test"
- Wants agent swarm before single gated workflow mastery

---

## Phase 3 will teach (preview only — not built in 2.7)

- Composing gated workflows from known patterns
- Builder discipline inheriting fail-closed defaults
- Still local-first; still not cloud factory

Digital twin factory = later phase after Builder Kit discipline proven.
