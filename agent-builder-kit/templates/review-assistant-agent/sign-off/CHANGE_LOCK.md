# Change Lock — Review Assistant Agent v0.1

Any future change to **frozen** Review Assistant v0.1 spec files must follow this process.

---

## Required for every change

1. **Change proposal** — fill [change-proposal.md](../change-proposal.md) (RA-CP-xxx)
2. **Impact analysis** — what breaks (scenarios, playbooks, curriculum)
3. **Evaluation check** — rerun [EVALUATION_CHECK_RESULT.md](EVALUATION_CHECK_RESULT.md) criteria
4. **Trace comparison** — before/after expected traces
5. **Rollback plan** — restore v0.1 frozen snapshot
6. **Human approval** — lead sign-off before merge

---

## Links

| Resource | Path |
|----------|------|
| Change proposals (repo) | `evolution/change-proposals/` |
| Quality gates | `evaluation/quality-gates/` |
| Trace examples | `observability/examples/` |
| Template lifecycle | [template-lifecycle.md](../../../template-governance/template-lifecycle.md) |
| Versioning | [template-versioning-policy.md](../../../template-governance/template-versioning-policy.md) |
| Freeze policy | [template-freeze-policy.md](../../../template-governance/template-freeze-policy.md) |
| Kit change spec | [change-proposal-spec.md](../../../template-specs/change-proposal-spec.md) |

---

## Unfreeze rules

To modify frozen v0.1 semantics:

1. Open change proposal with explicit «unfreeze» reason
2. Pass safety-regression checklist
3. Bump version (v0.1 → v0.2 if semantic change)
4. Re-run smoke + trace baseline scripts
5. Update sign-off folder with new FREEZE_RECORD

---

## Forbidden without full process

- Direct edit to workflow removing human approval
- Adding auto-publish
- Adding tools or memory without gates
- Copy-paste from external repos

---

## v0.1 status

**LOCKED** as of 2026-05-26. See [FREEZE_RECORD.md](FREEZE_RECORD.md).
