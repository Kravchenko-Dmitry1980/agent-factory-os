# Phase 3 — Freeze Policy

**Effective:** from Phase 2.8 sign-off through Phase 3.0 spec work  
**Extends:** [../FREEZE_RECOMMENDATIONS.md](../FREEZE_RECOMMENDATIONS.md) (Phase 1.4) with Phase 2/3 rules

---

## Frozen (no change without explicit user approval)

| Zone | Rule |
|------|------|
| New corpora | No new `Books/*` imports |
| Research repos | No new `experiments/*` sandboxes |
| Runtime code | No Hermes/MobileAgent/swarm stack in root |
| Platform architecture | No unified agent OS runtime |
| Digital twin factory | No implementation |
| CV factory | No implementation |
| RAG / embeddings / vector DB | Forbidden |
| MCP runtime / MCP agent server | Forbidden |
| Graph DB / ontology engine | Forbidden |
| Production deployment | No prod Telegram/FastAPI/SaaS |
| Shared framework extraction | No promote `prototypes/shared/` to `kit/runtime/` |
| Prototype **code** | No edits (Phase 2.8 boundary) |
| Integration-real **code** | No edits |
| Evaluation **scripts** | No edits |
| Observability **examples** | No edits |
| `agent-os/` concept promotion | No new canonical concepts without promotion pipeline |
| `13_gui-agents/` taxonomy | Still forbidden |

---

## Allowed without code

| Activity | Location |
|----------|----------|
| Phase 3 planning & template **specs** | `governance/phase-3-*` or future `agent-builder-kit/` (user-approved path) |
| Safety / evaluation / trace templates | MD only |
| One minimal demo template **document** | References existing `review-loop-agent` |
| Documentation updates | governance, curriculum cross-links |
| Governance reviews | `governance/phase-2-8/`, successors |
| Diagrams (Mermaid) | governance or kit docs |

---

## Requires explicit user approval

| Action |
|--------|
| Any code generator |
| Any reusable runtime package |
| Any production adapter enablement |
| Any new agent category implementation |
| CV template implementation |
| Digital twin template implementation |
| New Python dependencies |
| CI/CD workflows |
| Modifying prototype or evaluation code |

---

## Unfreeze triggers

Only user message explicitly naming:

- what to unfreeze
- why
- scope limit
- rollback plan
