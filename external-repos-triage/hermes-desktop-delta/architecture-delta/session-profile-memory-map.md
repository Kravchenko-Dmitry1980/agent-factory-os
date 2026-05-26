# Session, Profile, Memory Map

Analysis of Hermes Desktop identity/memory surfaces vs Agent-OS doctrine.

---

## Sessions (Hermes)

- SQLite FTS5 in `~/.hermes/state.db`
- Full chat history, search, resume
- **Useful later:** trace/session viewer for operators
- **Risk:** conflating chat log with audit trace

**Agent-OS:** traces are **governance artifacts**, not casual chat history.

---

## Profiles / Agents (Hermes)

- Isolated directories under `~/.hermes/profiles/`
- Separate config, SOUL.md, tools per profile
- **Useful later:** separate **implementation instances** per template (not personas)
- **Risk:** profile switching without freeze awareness

**Agent-OS:** one template → one thin impl baseline; profiles ≠ multiple agents without phase approval.

---

## Memory (Hermes)

- Editable memory entries + user profile memory
- External providers: Honcho, Mem0, Supermemory, ByteRover, …
- **Useful later:** **read-only** memory boundary viewer
- **Dangerous now:** any persistent writeback

**Agent-OS:** [memory-boundary-spec](../../agent-builder-kit/template-specs/memory-boundary-spec.md) — no hidden memory.

---

## Identity / Persona (SOUL.md)

- Persona editor in Hermes Desktop
- **Dangerous:** persona-over-architecture (see Phase 2.10 dangerous patterns)
- **Digital twin direction:** SOUL + memory + gateways ≈ informal digital twin

---

## Why we must NOT implement digital twin now

| Reason | Detail |
|--------|--------|
| Governance | No CV/digital twin policy allows this |
| Scope | Phase 3 is template + thin impl + mock LLM |
| Hermes marketing | "Self-improving" + memory + persona = twin drift |
| Safety | Unbounded identity persistence bypasses approval gates |

---

## Future console stance

Show **memory boundaries and freeze status** — do not offer SOUL editor or memory provider marketplace.
