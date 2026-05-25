# Architecture Over Hype

Phase 2.0 prototypes defend **boring architecture** against **exciting misuse**.

## Hype Patterns We Reject

| Hype | Reality |
|------|---------|
| "Multi-agent swarm" | Coordination cost + governance holes |
| "Autonomous memory" | Unverified writeback pollution |
| "Self-improving agent" | Recursive drift without evaluation |
| "Critic = verification" | Opinion ≠ evidence |
| "One more abstraction" | Hides gates from readers |

## What Good Looks Like

```
explicit state → explicit gate → explicit outcome → audit record
```

Not:

```
AgentOrchestrator.dispatch(PlanGraph.from_yaml(...))
```

## Educational Bar

A senior engineer should read a prototype and say:

> "I see exactly where it would fail in production, and exactly which gate catches it."

If they say:

> "Nice framework, where's the docs?"

— scope has drifted.

## Doctrine Alignment

Worldview lives in `agent-os/doctrine/`:

- Governance before autonomy
- Verification before writeback
- Bounded memory
- Trace-first thinking (audit logs in prototypes)

Prototypes **demonstrate** doctrine; they do not **replace** it.

## When to Stop Adding Code

Stop when:

- The governance lesson is visible in one screen of code
- Additional features require "real" infrastructure
- You need a README section titled "Architecture Overview" longer than the code

Prefer a new small prototype over a larger one.
