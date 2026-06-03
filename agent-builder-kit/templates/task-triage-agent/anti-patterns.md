# Task Triage Agent — Anti-Patterns

**Status:** SPEC_DRAFT

---

## Anti-pattern catalog

| Anti-pattern | Why Tempting | Why Dangerous | Mitigation |
|--------------|--------------|---------------|------------|
| **triage-as-execution** | "Just fix it while you're here" | Bypasses planning and approval | [no-execution-boundary.md](no-execution-boundary.md); REJECT_UNSAFE |
| **triage-as-orchestrator** | "Smart router saves time" | Multi-agent drift, hidden automation | [no-orchestrator-boundary.md](no-orchestrator-boundary.md); BLOCKED |
| **triage-as-project-manager** | "Track all tasks in one place" | PM platform scope creep | Scope lock; no queue/tickets |
| **auto-routing without approval** | "Send to Review Assistant automatically" | Orchestrator + execution | orchestrator_boundary_enforced |
| **risk laundering** | Label high-risk task as low | Unsafe work proceeds | Risk gate; ESCALATE on policy touch |
| **false readiness** | "Task is ready to implement" when info missing | Wasted impl, rework | NEEDS_CLARIFICATION |
| **hidden delegation** | "I've assigned this to the team" | Fake authority | No assign fields in contract |
| **vague task accepted as ready** | Avoid clarifying questions | Wrong work started by human | missing_info_detection required |
| **approval removal** | "Triage replaces human approval" | Governance erosion | [human-approval.md](human-approval.md) |
| **frozen spec mutation** | "Quick fix to frozen template" | Breaks change lock | ESCALATE + change proposal |
| **provider call by default** | "LLM classifies everything" | Cost, drift, injection surface | [provider-policy.md](provider-policy.md) |
| **memory creep** | "Remember all past tasks" | Unbounded context, privacy | [memory-policy.md](memory-policy.md) |

---

## Additional anti-patterns

| Anti-pattern | Why Tempting | Why Dangerous | Mitigation |
|--------------|--------------|---------------|------------|
| **benchmark triage accuracy** | "Score triage model 95%" | Benchmark platform drift | PASS/FAIL eval only |
| **second template = factory** | "Two agents → generate more" | Factory illusion | Explicit anti-factory in scope |
| **triage output as ticket** | "Auto-create Jira from triage" | PM + orchestrator drift | BLOCKED |
| **silent provider upgrade** | "Use better model silently" | Hidden network, cost | Provider policy; separate phase |

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
- Trace contains `task_executed`, `agent_started`, `task_routed`

---

## Governance review trigger

Any spec or impl introducing **queue**, **router**, **delegate**, or **execute** keywords in core workflow → **stop and rollback plan**.

See [change-proposal.md](change-proposal.md).
