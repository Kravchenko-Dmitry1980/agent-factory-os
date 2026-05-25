# Expected Escalations

Escalation = automation stops; human or supervisor path required.

---

## When Escalation Is Required

| Condition | Expected escalation |
|-----------|---------------------|
| Retry ceiling reached | yes |
| Persistent verification uncertainty | yes |
| Policy ambiguity on high-risk action | yes |
| LLM uncertain + high risk downstream | yes (reject or escalate) |
| Queue worker cannot resolve task | yes |

## When Escalation Is NOT Required

| Condition | Expected |
|-----------|----------|
| Clean human deny | terminal reject, not escalation |
| Malformed LLM (hard reject) | reject, optional escalation |
| Missing provenance (promotion) | governance_rejection |
| GUI hard mismatch | deny, not always escalate |

---

## Expected Escalation Trace Pattern

```text
verification_failed (×N)
retry_triggered (×N, bounded)
retry_exhausted
escalation_triggered
unsafe_action_blocked (if auto-complete attempted)
```

Reference: `observability/examples/escalation-trace.txt`

---

## Escalation Outcome Fields

| Field | Expected |
|-------|----------|
| OUTCOME status | escalated |
| GOVERNANCE escalated | yes |
| Automated completion | no |
| Human queue / supervisor | indicated in audit |

---

## Anti-Patterns

| Anti-pattern | Expected fix |
|--------------|--------------|
| retry_exhausted → task_failed (silent) | Must include escalation_triggered |
| Escalation without audit | FAIL |
| Escalation → auto-retry unlimited | FAIL |
| Remove supervisor actor | governance regression |

---

## Post-Escalation Rules

After escalation:

- No silent auto-resume
- Human decision required for retry or override
- Audit lineage preserved (append-only)

See `evolution/examples/escalation-removal-disaster.md`.
