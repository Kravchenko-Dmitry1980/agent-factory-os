# Promotion Candidates

**Только рекомендации.** Agent-OS **не изменялся**.

| Concept | Source | Target Future Location | Value | Maturity | Risk | Decision | Rationale |
|---------|--------|------------------------|-------|----------|------|----------|-----------|
| Control plane pattern | `extracted/brain-os-control-plane.md` | `agent-os/00_foundations/orchestration.md` | 4 | 3 | 2 | PROMOTE_LATER | Aligns with orchestration; needs dedup with Hermes Kanban |
| Deterministic cognitive routing | `patterns/deterministic-cognitive-routing.md` | `agent-os/08_patterns/` | 5 | 3 | 2 | PROMOTE_LATER | Complements adaptive routing antipatterns |
| Trace-first architecture | `patterns/trace-first-architecture.md` | `agent-os/03_harness-engineering/` | 5 | 4 | 1 | PROMOTE_LATER | Strong fit; extend execution-feedback |
| Task lifecycle FSM | `architecture/brain-os-state-machine.md` | `agent-os/01_agent-runtime/terminal-states.md` | 4 | 3 | 2 | PROMOTE_LATER | Parallel to query loop terminals |
| Memory retrieval scoring | `extracted/memory-retrieval-scoring.md` | `agent-os/02_memory/memory-recall.md` | 4 | 3 | 2 | PROMOTE_LATER | Extends recall with scoring weights |
| Policy-before-reasoning | `patterns/policy-before-reasoning.md` | `agent-os/00_foundations/orchestration.md` | 4 | 3 | 2 | PROMOTE_LATER | Sequencing pattern |
| Human escalation gate | `patterns/human-escalation-gate.md` | `agent-os/03_harness-engineering/permission-modes.md` | 4 | 3 | 2 | PROMOTE_LATER | High-risk domains |
| Router without rules | `anti-patterns/router-without-rules.md` | `agent-os/09_antipatterns/` | 4 | 4 | 1 | PROMOTE_LATER | Pairs with deterministic routing |
| Missing trace | `anti-patterns/missing-trace.md` | `agent-os/09_antipatterns/` | 4 | 4 | 1 | PROMOTE_LATER | Observability gap |
| Missing idempotency | `anti-patterns/missing-idempotency.md` | `agent-os/09_antipatterns/` | 4 | 3 | 2 | PROMOTE_LATER | Distributed agent ops |
| CAIM/MirrorMind/VGP2 planes | `glossary/*.md` | — | 2 | 1 | 4 | REJECT | Branding without contracts |
| adaptation-service | `extracted/adaptation-service.md` | — | 2 | 1 | 5 | REJECT | No governance |
| Universal multi-agent template | `anti-patterns/universal-multi-agent-template.md` | `agent-os/04_multi-agent/` | 3 | 2 | 3 | RESEARCH_ONLY | Domain-specific roles needed |
| Digital twin reproducibility | `glossary/digital-twin-reproducibility.md` | `agent-os/06_digital-twins/` | 3 | 1 | 4 | RESEARCH_ONLY | Needs replay model first |
| Event envelope schema | `contracts/event-envelope-contract.md` | `agent-os/10_research/` | 4 | 3 | 2 | RESEARCH_ONLY | Catalog as fourth corpus first |
