# LLM Verification — Governance

## Core Principle

```
LLM output ≠ truth
```

Critique/verification is a **separate step**. Model text is untrusted input until verified.

| Rule | Implementation |
|------|----------------|
| Timeout | urllib timeout |
| Malformed handling | try/parse, fail-closed |
| Uncertain | escalate, not accept |
| Deny on failure | no fallback accept |
| One model | single API call |
| Audit | all decisions logged |

## Alignment

- `Books/swarm-playbooks/anti-patterns/critic-as-fake-verification.md`
- `prototypes/review-loop-agent/`
