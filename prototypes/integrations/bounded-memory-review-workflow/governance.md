# Bounded Memory Review — Governance

| Rule | Implementation |
|------|----------------|
| Frozen snapshot | Set at session start only |
| Explicit context load | load_context() |
| Critique advisory | Does not auto-verify |
| Verification before writeback | verify step |
| Size ceiling | MAX_MEMORY_CHARS |
| Uncertainty block | fail-closed |

## Alignment

- `agent-os/08_patterns/verification-before-writeback.md`
- `prototypes/bounded-memory-agent/`
- `prototypes/review-loop-agent/`
