# Task Triage Agent — Agent Card

## Agent Name

**Task Triage Agent**

## Version

**v0.1-draft**

## Status

**SPEC_DRAFT**

## Primary Role

Classify tasks and recommend safe next steps.

Task Triage Agent converts vague incoming work into a structured advisory decision. It helps humans answer: what kind of task is this, how risky is it, what is missing, and what should happen next — without performing the work.

---

## Inputs

| Input | Required |
|-------|----------|
| Task text | **yes** |
| Optional context label | no |
| Optional project area | no |
| Optional risk hints | no |

See [inputs.md](inputs.md) for full field definitions.

---

## Outputs

| Output | Description |
|--------|-------------|
| Task type | Classification from allowed enum |
| Priority class | low / medium / high / blocked |
| Risk level | low / medium / high / critical |
| Missing information | List of gaps |
| Suggested next step | Advisory string for human |
| Approval requirement | boolean + reason |
| Escalation requirement | boolean + reason |
| Final triage decision | TRIAGED / NEEDS_CLARIFICATION / ESCALATE / BLOCKED / REJECT_UNSAFE |
| Trace | Ordered human-readable events |

See [outputs.md](outputs.md) and [contract.md](contract.md).

---

## Forbidden Capabilities

| Capability | Status |
|------------|--------|
| Execution | **forbidden** |
| File modification | **forbidden** |
| Tool calls | **forbidden** |
| Provider calls (by default) | **forbidden** |
| Routing | **forbidden** |
| Delegation | **forbidden** |
| Task queue creation | **forbidden** |
| Ticket creation | **forbidden** |
| Message sending | **forbidden** |
| Memory writeback | **forbidden** |

---

## Required Safety Principles

| Principle | Detail |
|-----------|--------|
| Advisory only | Output recommends; human decides |
| Human decides next action | Triage is not authorization to execute |
| No execution | No commands, files, APIs, publish |
| No orchestration | No agent dispatch, routing, queues |
| Trace every decision | Human-readable event chain required |
| Fail closed on unsafe/unclear task | BLOCKED / REJECT_UNSAFE / NEEDS_CLARIFICATION |

---

## Safe Use Cases

- Classify a development task before planning
- Classify a research or documentation task
- Detect missing acceptance criteria
- Detect provider or security risk
- Suggest planning before implementation
- Recommend escalation for unclear ownership

---

## Unsafe Use Cases

- "Just implement this now"
- "Route to Review Assistant and start"
- "Create sprint backlog from triage"
- "Skip human approval"
- "Modify frozen spec without proposal"
- Autonomous task execution of any kind

---

## Related Policies

- [no-execution-boundary.md](no-execution-boundary.md)
- [no-orchestrator-boundary.md](no-orchestrator-boundary.md)
- [human-approval.md](human-approval.md)
- [provider-policy.md](provider-policy.md)
- [memory-policy.md](memory-policy.md)
- [safety-gates.md](safety-gates.md)
