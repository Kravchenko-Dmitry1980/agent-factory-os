# Prototype Rules

Every Phase 2.0 prototype MUST satisfy these rules.

## 1. Size

- Single `minimal-demo.py` ≤ ~250 lines (excluding imports)
- Understandable in **< 30 minutes**
- No hidden modules beyond `prototypes/shared/`

## 2. Governance

Each prototype MUST demonstrate:

| Principle | Minimum artifact |
|-----------|------------------|
| Fail-closed | Deny on uncertainty in demo code |
| Verification | Explicit verification step before side effects |
| Escalation | Human or supervisor path when automation stops |
| Anti-patterns | Documented in README or `anti-patterns.md` |

## 3. Documentation

Required per prototype:

- `README.md` — purpose, run instructions
- `contracts.md` — inputs, outputs, gates
- `failure-modes.md` — hallucination, bypass, drift, etc.
- `governance.md` — how doctrine applies

Additional files per spec (architecture, memory-model, etc.).

## 4. Technology

**Allowed:** Python 3.12+, JSON, SQLite (optional), in-memory queue, Mermaid, CLI.

**Forbidden:** LangGraph, agent frameworks, vector DB, Redis cluster, K8s, MCP runtime, workflow engines.

## 5. Integration with agent-os

- Reference doctrine/patterns via relative paths or wikilinks
- Do NOT copy large blocks from `agent-os/` into prototype code
- Do NOT promote prototype code into `agent-os/` without governance review

## 6. Demo Honesty

- Mock external systems (GUI, LLM, human) with deterministic functions
- Label mocks explicitly in code comments
- Never imply production readiness in README titles
