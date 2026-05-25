# Failure-First Thinking

Prototypes exist to make **failure visible before success feels inevitable**.

## Design Order

1. List failure modes (`failure-modes.md`)
2. Define contracts with **failure states** and **escalation points**
3. Implement fail-closed gates
4. Add one happy-path demo
5. Add one demo path that triggers each major failure

## Failure Categories (All Prototypes)

| Category | Question |
|----------|----------|
| Hallucination | What if the model invents facts? |
| Missing verification | What if we skip the check? |
| Retry loops | What if retries never escalate? |
| Memory drift | What if context grows unbounded? |
| Unsafe autonomy | What if action runs without approval? |
| Missing escalation | What if automation stalls silently? |
| Governance bypass | What if a shortcut skips a gate? |

## Fail-Closed Default

When evidence is insufficient:

```
ALLOW  ← requires explicit PASS
DENY   ← default for UNCERTAIN and FAIL
```

Never:

```
UNCERTAIN → ALLOW "to keep moving"
```

## Escalation Is Not Failure

Escalation to human is **successful governance**, not demo failure. Prototypes should print escalation clearly.

## Relation to agent-os

- [[fail-closed-agent-loop]]
- [[fail-closed-defaults]]
- [[verification-before-writeback]]

Upstream: `Books/swarm-playbooks/anti-patterns/critic-as-fake-verification.md`
