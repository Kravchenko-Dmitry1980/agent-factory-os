# Task Triage Agent — Scope

**Date:** 2026-05-26  
**Status:** PLAN_ONLY

---

## In scope

| Item | Detail |
|------|--------|
| Text task classification | Type from allowed enum |
| Risk classification | low / medium / high / critical |
| Missing information detection | Explicit gaps before work |
| Next-step recommendation | Advisory only |
| Human approval recommendation | When medium+ risk or policy touch |
| Escalation recommendation | Security, frozen spec, provider, data |
| Defer recommendation | Blocked until clarification |
| Trace output | Human-readable event list |
| Synthetic evaluation (future) | Fixed cases, PASS/FAIL — no benchmark |

---

## Out of scope

| Item | Reason |
|------|--------|
| Execution | [NO_EXECUTION_POLICY](TASK_TRIAGE_AGENT_NO_EXECUTION_POLICY.md) |
| Orchestration / delegation | [NO_ORCHESTRATOR_POLICY](TASK_TRIAGE_AGENT_NO_ORCHESTRATOR_POLICY.md) |
| Scheduling | PM platform drift |
| Task queue | Runtime drift |
| Writing code | Implementation agent domain |
| Modifying files | Execution boundary |
| Sending messages | External action |
| Creating tickets | PM platform |
| Assigning people | Orchestrator drift |
| Provider calls by default | [PROVIDER_POLICY](TASK_TRIAGE_AGENT_PROVIDER_POLICY.md) |
| Persistent memory | [MEMORY_POLICY](TASK_TRIAGE_AGENT_MEMORY_POLICY.md) |
| Project management platform | Explicit anti-pattern |
| Multi-agent routing | Orchestrator |
| RAG / knowledge retrieval | Separate phase |
| MCP / tools | Separate phase with approval |
| Cloud / RU providers | Out of Phase 3 scope |
| Operator Console | Backlog |

---

## Scope boundary diagram

```text
┌──────────────────────────────────────┐
│         IN SCOPE (v0.1 plan)           │
│  classify · risk · missing info ·    │
│  advise next step · trace · HITL     │
└──────────────────────────────────────┘
              │
              │ human decides
              ▼
┌──────────────────────────────────────┐
│              OUT OF SCOPE              │
│  execute · route · queue · assign ·  │
│  tools · provider · memory · PM      │
└──────────────────────────────────────┘
```

---

## Comparison to Review Assistant scope

| Dimension | Review Assistant | Task Triage |
|-----------|------------------|-------------|
| Primary input | Review/draft task | Any incoming work task |
| Primary output | Draft + delivery decision | Triage classification |
| Content generation | Yes (draft) | No — classification only |
| Human approval | Before delivery | Before treating triage as action |
| Provider | Optional (v0.3) | Not by default |
| Execution | Blocked | Blocked (stronger emphasis) |

---

## Future scope expansion (requires new phase)

- Optional mock classifier (local rules, not LLM)
- Optional provider-assisted classification (mock-first, synthetic only)
- Thin implementation in `prototypes-derived/` (separate impl phase)
- Triage safety harness (separate eval phase)

Each expansion requires change proposal + governance review.
