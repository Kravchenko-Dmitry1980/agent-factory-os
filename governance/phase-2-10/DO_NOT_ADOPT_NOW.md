# Do Not Adopt Now

Strict list for Phase 2.10 → through Phase 3.0 specs.

| Item | Why tempting | Why dangerous | When maybe later |
|------|--------------|---------------|------------------|
| Ruflo runtime/swarm | Scale, «enterprise» | Platform drift, RAG, autopilot | Unlikely / separate product decision |
| Claude Code Action GH automation | Auto PR fix | CI autonomy, token risk | Phase 5+ with read-only pilot |
| SuperClaude personas wholesale | Structured dev | Persona over architecture | Never wholesale; maybe 5 command labels |
| Claude templates bulk import | Fast setup | MCP/hooks dump | Phase 4 controlled registry |
| Scientific skills installation | Research power | Supply chain, medical risk | Phase 4+ per-skill review |
| Agentic PM runtime (`apm init`) | Multi-agent PM | Overlaps; apm-auto unsafe | Phase 4 PM template docs only |
| MCP servers from templates | Integrations | Permission sprawl | Dedicated MCP phase |
| Hooks from templates | Automation | Bypass human gates | After hook governance spec |
| Self-learning memory | Smarter agents | Unbounded memory | Digital twin phase+ |
| Distributed swarm | Multi-machine | Federation complexity | Not planned |
| CI/CD agent automation | Velocity | no-ci-cd-policy | Phase 5+ |

## Enforcement

Any PR importing from `external-repos-triage/source/` into `agent-os/`, `prototypes/`, `curriculum/` → **reject**.

Phase 3 prompt must cite [PHASE_3_START_CONDITIONS.md](../PHASE_3_START_CONDITIONS.md).
