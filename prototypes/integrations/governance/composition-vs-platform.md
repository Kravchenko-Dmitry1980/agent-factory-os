# Composition vs Platform

## Composition (Phase 2.1 Goal)

```
step_a() → step_b() → gate() → step_c() or escalate()
```

- Steps are named functions in one file
- Gates return `(allowed, reason)`
- Audit after every transition
- Failure scenarios are explicit CLI flags

**Teaches:** where governance breaks when pipelines grow.

## Platform (Forbidden)

```
engine = WorkflowEngine(config="pipeline.yaml")
engine.register(ReviewStep)
engine.register(PublishStep)
engine.run(context)
```

- Behavior hidden in engine
- Gates become optional hooks
- Escalation is a middleware default
- Readers learn the **framework**, not the **policy**

## Decision Table

| Question | Composition | Platform |
|----------|-------------|----------|
| Where is the flow? | Same file, top to bottom | Config + engine |
| Where is fail-closed? | Visible `if not allowed: return` | Exception handler |
| Can you break governance silently? | Hard — it's explicit | Easy — skip hook |
| Educational value | High | Low |

## When Integration Graduates

Insights graduate to **markdown** in `agent-os/` or `governance/`.

Code does **not** graduate to a runtime repo.
