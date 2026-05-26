# No Runtime Policy

## Rule

Agent Builder Kit v0.1 contains **zero executable runtime**.

## Forbidden in kit

- Python, JavaScript, TypeScript source
- CLI entrypoints
- FastAPI / Telegram bots
- LangGraph / workflow engines
- MCP servers
- Docker / deploy configs for agents
- `requirements.txt` changes for kit purposes

## Allowed

- Reference paths to Phase 2 prototypes (external to kit)
- Text description of conceptual workflow
- Mermaid diagrams

## Implementation

Any code implementation requires:

1. Explicit user approval
2. Separate phase (3.1+)
3. H1–H5 gates from `governance/PHASE_3_START_CONDITIONS.md`

## Verification

Phase 3.0 review must confirm: no `.py`, `.js`, `.ts` files under `agent-builder-kit/`.
