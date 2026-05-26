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

## Phase 3.3 real provider rules

- **No real provider by default** — mock/legacy default; `--real-provider` opt-in
- **One local OpenAI-compatible endpoint** — `RA_LLM_BASE_URL` only
- **No provider framework** — no registry/router/SDK
- **Synthetic data only** — hardcoded prompt for real mode
- **No sensitive data** — see [governance/phase-3-3-plan/FORBIDDEN_DATA_POLICY.md](../../governance/phase-3-3-plan/FORBIDDEN_DATA_POLICY.md)
- **Stdlib only** — urllib, no pip deps

## Scope lock

Implements **only** frozen Review Assistant v0.1 semantics — not a platform.

References:

- `governance/phase-3-1-plan/NO_RUNTIME_DECISION.md`
- `agent-builder-kit/governance/no-factory-yet-policy.md`
- `agent-builder-kit/templates/review-assistant-agent/sign-off/CHANGE_LOCK.md`
