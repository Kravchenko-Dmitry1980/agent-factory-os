# Task Triage Agent — Anti-Patterns

**Date:** 2026-05-26  
**Status:** PLAN_ONLY

---

## Anti-pattern catalog

| Anti-pattern | Why Tempting | Why Dangerous | Mitigation |
|--------------|--------------|---------------|------------|
| **triage-as-execution** | "Just fix it while you're here" | Bypasses planning and approval | NO_EXECUTION policy; REJECT_UNSAFE |
| **triage-as-orchestrator** | "Smart router saves time" | Multi-agent drift, hidden automation | NO_ORCHESTRATOR policy; BLOCKED |
| **triage-as-project-manager** | "Track all tasks in one place" | PM platform scope creep | Scope lock; no queue/tickets |
| **auto-routing without approval** | "Send to Review Assistant automatically" | Orchestrator + execution | orchestrator_boundary_enforced |
| **risk laundering** | Label high-risk task as low | Unsafe work proceeds | Risk gate; ESCALATE on policy touch |
| **false readiness** | "Task is ready to implement" when info missing | Wasted impl, rework | NEEDS_CLARIFICATION |
| **hidden delegation** | "I've assigned this to the team" | Fake authority | No assign fields in contract |
| **vague task accepted as ready** | Avoid clarifying questions | Wrong work started by human | missing_info_detection required |
| **approval removal** | "Triage replaces human approval" | Governance erosion | HITL policy; approval_required |
| **frozen spec mutation** | "Quick fix to frozen template" | Breaks change lock | ESCALATE + change proposal |
| **provider-by-default** | "LLM classifies everything" | Cost, drift, injection surface | Provider policy; mock-first |
| **persistent task memory** | "Remember all past tasks" | Unbounded context, privacy | Memory policy; session-only |
| **benchmark triage accuracy** | "Score triage model 95%" | Benchmark platform drift | PASS/FAIL eval only |
| **second template = factory** | "Two agents → generate more" | Factory illusion | Explicit anti-factory in scope lock |

---

## Red flags in task text (input)

Phrases that should trigger elevated response:

- "just run", "execute now", "deploy immediately"
- "route to", "assign to", "start agent"
- "create Jira", "add to backlog", "schedule sprint"
- "skip approval", "bypass gate", "no human needed"
- "modify frozen", "change v0.3 without review"

---

## Red flags in triage output

- `suggested_next_step` contains imperative execution verb without "human should"
- `final_triage_decision` not in allowed enum
- Missing `approval_required` when risk ≥ medium
- Trace omits `orchestrator_boundary_enforced` when task requested routing

---

## Governance review trigger

Any spec or impl introducing **queue**, **router**, **delegate**, or **execute** keywords in core workflow → **stop and rollback plan**.
