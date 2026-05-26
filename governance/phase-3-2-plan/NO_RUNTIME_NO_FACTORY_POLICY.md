# No Runtime / No Factory Policy — Phase 3.2

**Applies to:** LLM adapter planning and any future Phase 3.2 implementation

---

## Even with LLM adapter planned, we are NOT creating

| Artifact | Forbidden |
|----------|-----------|
| Agent runtime | General execution engine |
| Adapter registry | Catalog of providers/plugins |
| Provider abstraction framework | Multi-backend SDK layer |
| Model router | Auto-select model by task |
| Prompt marketplace | Shared prompt library product |
| Agent factory | Template → deploy pipeline |
| Template generator | Scaffold from spec |
| Production integration | Telegram, FastAPI, SaaS |

---

## What IS allowed (future, mock-first)

| Allowed | Limit |
|---------|-------|
| One mock LLM adapter module | Single folder, single purpose |
| Optional real client | One provider, explicit flag, user approval |
| Extended trace events | Text stdout |
| New eval script | Separate file; no framework |

---

## Why

Phase 3.2 strengthens **one agent boundary** — not platform maturity. LLM adapters are a common drift vector toward:

- shared `llm/` package used by N agents
- provider registry
- "just one more template"

This policy blocks that path without explicit new phase.

---

## Detection signals (stop work)

```text
adapters/registry.py
providers/__init__.py
ModelRouter class
PromptTemplateEngine
agent-builder-kit/runtime/
agent-builder-kit/factory/
```

---

## References

- [NO_RUNTIME_DECISION.md](../phase-3-1-plan/NO_RUNTIME_DECISION.md) (Phase 3.1)
- [agent-builder-kit/governance/no-factory-yet-policy.md](../../agent-builder-kit/governance/no-factory-yet-policy.md)

---

## Diagram

[diagrams/no-runtime-boundary.md](diagrams/no-runtime-boundary.md)
