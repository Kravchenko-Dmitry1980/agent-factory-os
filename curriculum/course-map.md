# Course Map

Full learning route — Levels 0 through 10.

Each level maps to modules, exercises, and operator-playbook resources.

---

## Level 0 — Orientation

**Goal:** Understand what this project is and what it is not.

| Resource | Path |
|----------|------|
| Module | [modules/module-00-orientation.md](modules/module-00-orientation.md) |
| Read | `agent-os/doctrine/system-positioning.md` |
| Operator | [../operator-playbooks/README.md](../operator-playbooks/README.md) |
| Exercise | [exercises/exercise-run-first-demo.md](exercises/exercise-run-first-demo.md) |
| Time | ~30 min |

---

## Level 1 — Agent Basics

**Goal:** An agent is a workflow with tools, memory, checks, and limits — not magic.

| Resource | Path |
|----------|------|
| Module | [modules/module-01-what-is-an-ai-agent.md](modules/module-01-what-is-an-ai-agent.md) |
| Lesson | [lessons/lesson-fail-closed.md](lessons/lesson-fail-closed.md) (preview) |
| Demo | `prototypes/review-loop-agent/minimal-demo.py` |

---

## Level 2 — Safety Basics

**Goal:** Fail-closed, approval, verification, human review.

| Resource | Path |
|----------|------|
| Modules | [module-03-verification-first.md](modules/module-03-verification-first.md), [module-04-human-approval.md](modules/module-04-human-approval.md), [module-06-fail-closed-execution.md](modules/module-06-fail-closed-execution.md) |
| Lessons | critic, LLM, approval lessons in `lessons/` |
| Exercise | [exercise-block-unsafe-action.md](exercises/exercise-block-unsafe-action.md) |

---

## Level 3 — Prototypes

**Goal:** Run small systems and observe behavior.

| Resource | Path |
|----------|------|
| Module | [module-05-bounded-memory.md](modules/module-05-bounded-memory.md) |
| Runbook | [../operator-playbooks/runbooks/run-prototypes.md](../operator-playbooks/runbooks/run-prototypes.md) |
| Exercises | first demo, break review loop |

---

## Level 4 — Workflow Integration

**Goal:** Several steps connect into one safe workflow.

| Resource | Path |
|----------|------|
| Module | [module-07-workflow-orchestration.md](modules/module-07-workflow-orchestration.md) |
| Runbook | [../operator-playbooks/runbooks/run-integration-workflows.md](../operator-playbooks/runbooks/run-integration-workflows.md) |
| Exercise | [exercise-trigger-escalation.md](exercises/exercise-trigger-escalation.md) |

---

## Level 5 — Real Adapters

**Goal:** Real external boundaries (mock mode default).

| Resource | Path |
|----------|------|
| Module | [module-08-real-integrations.md](modules/module-08-real-integrations.md) |
| Runbook | [../operator-playbooks/runbooks/run-real-adapters.md](../operator-playbooks/runbooks/run-real-adapters.md) |
| Exercise | [exercise-detect-bad-llm-output.md](exercises/exercise-detect-bad-llm-output.md) |

---

## Level 6 — Observability

**Goal:** Read traces; understand failures.

| Resource | Path |
|----------|------|
| Module | [module-09-observability-and-traces.md](modules/module-09-observability-and-traces.md) |
| Lesson | [lessons/lesson-audit-lineage.md](lessons/lesson-audit-lineage.md) |
| Exercise | [exercise-read-trace.md](exercises/exercise-read-trace.md) |

---

## Level 7 — Evaluation

**Goal:** Check that behavior stayed safe.

| Resource | Path |
|----------|------|
| Module | [module-10-evaluation-and-regression.md](modules/module-10-evaluation-and-regression.md) |
| Lesson | [lessons/lesson-regression.md](lessons/lesson-regression.md) |
| Exercise | [exercise-run-evaluation.md](exercises/exercise-run-evaluation.md) |

---

## Level 8 — Safe Evolution

**Goal:** Change without breaking gates.

| Resource | Path |
|----------|------|
| Module | [module-11-safe-evolution.md](modules/module-11-safe-evolution.md) |
| Exercises | change proposal, rollback, platform drift |
| Evolution | `evolution/change-proposals/` |

---

## Level 9 — Operator Readiness

**Goal:** Operate using playbooks confidently.

| Resource | Path |
|----------|------|
| Module | [module-12-operator-practice.md](modules/module-12-operator-practice.md) |
| Operator | [../operator-playbooks/](../operator-playbooks/) |
| Assessment | [assessments/operator-assessment.md](assessments/operator-assessment.md) |

---

## Level 10 — Phase 3 Readiness

**Goal:** Know when Agent Builder Kit is safe to start.

| Resource | Path |
|----------|------|
| Module | [module-13-phase-3-readiness.md](modules/module-13-phase-3-readiness.md) |
| Methodology | [methodology/phase-3-entry-criteria.md](methodology/phase-3-entry-criteria.md) |
| Assessment | [assessments/phase-3-readiness-assessment.md](assessments/phase-3-readiness-assessment.md) |

---

## Visual Map

[diagrams/learning-ladder.md](diagrams/learning-ladder.md)

---

## By Role (Shortcut)

| Role | Track file |
|------|------------|
| Intern | [role-based-tracks/track-intern.md](role-based-tracks/track-intern.md) |
| AI developer | [role-based-tracks/track-ai-developer.md](role-based-tracks/track-ai-developer.md) |
| Cursor operator | [role-based-tracks/track-cursor-operator.md](role-based-tracks/track-cursor-operator.md) |
| Project lead | [role-based-tracks/track-project-lead.md](role-based-tracks/track-project-lead.md) |
| AI architect | [role-based-tracks/track-ai-architect.md](role-based-tracks/track-ai-architect.md) |
