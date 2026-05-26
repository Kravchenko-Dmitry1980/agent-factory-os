# Governance — Review Assistant Thin

## Allowed (this folder only)

- One entry script: `minimal_demo.py`
- Stdlib Python 3.12+
- Local stdout trace
- Scenario flags via argparse
- Markdown docs in this folder

## Forbidden

- Runtime / framework / factory / generator / registry / plugins
- Second agent template or folder
- CV / digital twin / RAG / MCP / LangGraph
- External API, Telegram, FastAPI, network
- Database, persistent memory, file writeback
- New pip dependencies
- Edit `prototypes/`, `integrations-real/`, `observability/examples/` (existing eval scripts: add new file only)
- Edit frozen Review Assistant v0.1 spec body
- Import external repo templates

## Phase 3.2 LLM mock rules

- **No real API** — mock dict payloads only
- **No provider framework** — no registry, router, base adapter hierarchy
- **No model router / RAG / MCP**
- **Explicit approval required** for future real provider ([PRECONDITIONS_FOR_3_2_IMPLEMENTATION.md](../../governance/phase-3-2-plan/PRECONDITIONS_FOR_3_2_IMPLEMENTATION.md))

## Scope lock

Implements **only** frozen Review Assistant v0.1 semantics — not a platform.

References:

- `governance/phase-3-1-plan/NO_RUNTIME_DECISION.md`
- `agent-builder-kit/governance/no-factory-yet-policy.md`
- `agent-builder-kit/templates/review-assistant-agent/sign-off/CHANGE_LOCK.md`
