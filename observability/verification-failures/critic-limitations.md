# Critic Limitations

## Definition

**Critic** = advisory quality filter. **Not** verification system.

## Observable Distinction

| Signal | Critic | Verification |
|--------|--------|--------------|
| Purpose | Style, obvious errors | Evidence, schema, policy |
| False positive | Pass bad facts | Should fail closed |
| Event | advisory verdict | `verification_passed/failed` |
| Can publish? | **No** | Required but not sufficient alone |

## Failure Mode: Critic as Fake Verification

Trace shows:

```
verification_passed actor=critic verdict=pass
task_completed actor=publisher
```

Missing: `approval_requested`, independent verify.

## Source

- `Books/swarm-playbooks/anti-patterns/critic-as-fake-verification.md`
- `prototypes/review-loop-agent/governance.md`

## Observability Fix

Log critic as:

```
verification_passed actor=critic advisory=true facts_verified=false
```

Human reader immediately sees limit.
