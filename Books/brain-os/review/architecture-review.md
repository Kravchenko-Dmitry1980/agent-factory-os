# Architecture Review

Классификация идей Brain OS по зрелости (evidence: оба source docs).

## Production-relevant

- Control plane separation (Product vs Brain OS vs planes)
- Task lifecycle + state machine
- TaskEnvelope / RoutingDecision / TraceRecord contracts (черновик)
- Deterministic routing pseudocode
- Trace-first + event envelope
- Execution supervisor + fallback
- Human escalation for high-risk
- Memory retrieval scoring formula (structure)
- Acceptance criteria NFR (latency, trace completeness, idempotency claim)

## Strong reusable

- Policy-before-reasoning sequencing
- Evaluation-before-writeback
- Memory-aware routing
- Event catalog for observability

## Promising but incomplete

- Policy engine (strategy without versioned policy DSL)
- Evaluation engine (metrics without evaluator spec)
- ER model (entities without migration/index strategy)
- API reference (JSON examples without OpenAPI)
- Multi-agent template (roles without domain packs)

## Speculative

- adaptation-service / v0.3 learned routing
- simulation_mode distinct semantics
- System-1.5 compute plane (named, not specified)

## Branding-only

- CAIM / MirrorMind / System-1.5 / VGP2 as **product names** без inter-plane RPC contracts
- «операционная когнитивная платформа» marketing framing

## Dangerous if promoted too early

- adaptation without governance
- universal 4-agent template as canonical pattern
- digital twin reproducibility claim without replay/versioning
- idempotency NFR without implementation spec
