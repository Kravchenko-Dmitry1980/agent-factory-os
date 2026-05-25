# Operator Readiness Review

**Scope:** `operator-playbooks/` + curriculum operator modules

---

## Can roles succeed?

| Role | Can start? | Evidence | Gap |
|------|------------|----------|-----|
| Beginner | **Yes** | start-here, first-30-min, beginner-path | EN text |
| Intern | **Yes** | onboarding-for-intern, curriculum track-intern | Mentor required |
| Project lead | **Yes** | onboarding-for-project-lead, lead path | Must not skip demos |
| Cursor operator | **Yes** | cursor-operator-path, runbooks | Evaluation discipline |
| Reviewer (unsafe behavior) | **Yes** | red-flag-checklist, safety-guides | Manual judgment |
| Recovery from failures | **Yes** | troubleshooting/*, common-errors | Experience helps |

---

## Recommended first 30 minutes

From `operator-playbooks/start-here/first-30-minutes.md` (EN) — commands match RU `student-command-list.md`:

1. `cd C:\Dima\Projects\CURSOR\AGENT`
2. `python prototypes/review-loop-agent/minimal-demo.py --scenario happy`
3. `python prototypes/review-loop-agent/minimal-demo.py --scenario bypass-attempt`
4. Read one line from Audit / compare Published
5. Skim `what-not-to-touch.md`

**RU learners:** follow `curriculum/ru/student-guides/student-start-here.md` + mentor.

---

## Recommended first 2 hours

Aligns with `curriculum/ru/workshops/workshop-2-hour-practical.md`:

- fail-closed three scenarios
- bounded-memory overflow
- read one observability example
- `run_demo_smoke_checks.py`

---

## Required before Phase 3 participation

| Requirement | Doc |
|-------------|-----|
| Pass first demo + bypass narration | exercise-run-first-demo |
| Pass read-trace | exercise-read-trace |
| Smoke PASS observed | run-evaluation-checks runbook |
| Explain fail-closed, critic, LLM (3 sentences each) | beginner assessment |
| Lead acknowledges freeze + minimal scope | PHASE_3_FREEZE_POLICY |

---

## Operator score: **8/10**

Strong runbook coverage; not a 10 only because EN-only and no centralized sign-off log in repo.
