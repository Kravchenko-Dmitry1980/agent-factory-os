# No Runtime Decision — Phase 3.1

**Decision:** Phase 3.1 **must not** create a runtime, framework, factory, or reusable agent engine.

**Status:** Binding for Phase 3.1 thin implementation planning and future impl.

---

## Phase 3.1 must NOT create

| Artifact | Forbidden |
|----------|-----------|
| Runtime | General agent execution loop as product |
| Framework | Pluggable steps, base classes for "any agent" |
| Generator | Template → code scaffolding |
| Factory | Registry, catalog, multi-template deploy |
| Plugin system | Dynamic tool/agent loading |
| Registry | Central agent metadata store |
| Reusable agent engine | Shared orchestration across agents |
| Orchestration engine | LangGraph, workflow engine, job queue platform |

---

## Why

Phase 3.1 exists to prove **one frozen template** (Review Assistant v0.1) can be implemented **safely** and **locally** — not to bootstrap Agent Factory or Agent OS runtime.

Evidence from Phase 2.8: **CONDITIONAL GO** — kit first, factory later with explicit gates.

Creating runtime early would:

- Blur `agent-builder-kit/` spec vs execution boundaries  
- Invite second-agent and platform drift  
- Bypass evaluation and governance harness maturity  
- Duplicate `prototypes/shared/` anti-pattern (platform drift)

---

## What Phase 3.1 MAY create (future impl only)

| Allowed | Limit |
|---------|-------|
| One folder | `prototypes-derived/review-assistant-thin/` |
| One entry script | Scenario flags, stdout trace |
| Local helpers | Same folder only, not importable "SDK" |

---

## Detection signals (stop work if seen)

```text
prototypes-derived/shared/
prototypes-derived/runtime/
agent-builder-kit/runtime/
agent-builder-kit/factory/
BaseAgent class used by future agents
template_loader.py
registry.json
```

---

## Alternative deferred to later phases

| Need | Deferred to |
|------|-------------|
| Multi-template support | Phase 3.2+ with governance |
| Real LLM adapter | Separate approval |
| Production HITL | integrations-real lifecycle |
| Builder Kit runtime under kit/ | Explicit architecture review |

---

## Diagram

[diagrams/no-runtime-boundary.md](diagrams/no-runtime-boundary.md)

---

## References

- [agent-builder-kit/governance/no-runtime-policy.md](../../agent-builder-kit/governance/no-runtime-policy.md)
- [agent-builder-kit/governance/no-factory-yet-policy.md](../../agent-builder-kit/governance/no-factory-yet-policy.md)
- [PHASE_3_1_PRECONDITIONS.md](../PHASE_3_1_PRECONDITIONS.md)

---

## Confirmation

Phase 3.1-Plan **accepts** this decision. Implementation phase must re-confirm in POST_IMPLEMENTATION_CHECKLIST.
