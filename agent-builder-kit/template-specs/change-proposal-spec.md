# Change Proposal Spec

Any change to an accepted agent template must follow this proposal format.

Reference: `evolution/change-proposals/`

---

## Required Questions

Every template change proposal must answer:

### 1. What changes?

Concrete diff: sections added, removed, or modified.

### 2. Why?

Problem, incident, or improvement goal. Link to trace or eval failure if applicable.

### 3. What can break?

Downstream scenarios, gates, operator playbooks, student curriculum.

### 4. Which safety gate is affected?

List gates: fail-closed, verification, approval, memory, tool-use, escalation, evaluation, rollback.

### 5. Which trace should be compared?

Before/after expected trace for at least one scenario.

### 6. Which evaluation check must run?

Map to `evaluation/scenarios/` and checklist items.

### 7. What is rollback plan?

How to revert template to previous frozen version.

### 8. Who approves?

| Change type | Approver |
|-------------|----------|
| Draft template edit | template author |
| Accepted template change | lead + governance review |
| Frozen template change | explicit unfreeze + proposal |

---

## Proposal Lifecycle

```
draft proposal
  → safety review
  → trace comparison
  → evaluation checklist rerun
  → approval
  → version bump
  → optional re-freeze
```

See [template-governance/template-lifecycle.md](../template-governance/template-lifecycle.md)

---

## Template-Specific Proposals

Each reference template includes `change-proposal.md` with pre-filled context.

Example: [templates/review-assistant-agent/change-proposal.md](../templates/review-assistant-agent/change-proposal.md)

---

## Related

- [safety-gates/rollback-gate.md](../safety-gates/rollback-gate.md)
- [template-governance/template-versioning-policy.md](../template-governance/template-versioning-policy.md)
- `evolution/change-proposals/README.md`
