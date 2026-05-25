# Bounded Memory — Anti-Patterns

| Anti-pattern | Symptom | Prototype response |
|--------------|---------|-------------------|
| Unbounded memory growth | Store exceeds limit | Reject write |
| Mid-session memory injection | Snapshot changes mid-loop | Not allowed in API |
| Memory as crutch | Everything saved | Verification gate |
| Unverified writeback | Hallucination persisted | Discard + audit |
| Implicit context merge | Hidden token growth | Explicit `load_context` |

See `agent-os/09_antipatterns/` for curated definitions.
