# Bounded Memory Review — Workflow

1. **Context load** — frozen snapshot + explicit durable slice
2. **Execution** — produce candidate memory entry (mock)
3. **Critique** — advisory quality check
4. **Verification** — evidence gate (pass/fail/uncertain)
5. **Writeback or reject** — size ceiling + verified flag
6. **Snapshot rollback** — on reject, durable unchanged; snapshot never mid-session mutate

Uncertainty blocks writeback (fail-closed).
