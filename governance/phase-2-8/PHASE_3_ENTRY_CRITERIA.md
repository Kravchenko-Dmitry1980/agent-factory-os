# Phase 3 — Entry Criteria (Governance)

Consolidates `curriculum/methodology/phase-3-entry-criteria.md` and `curriculum/ru/methodology/phase-3-entry-criteria.md` with repository-level gates.

---

## Human readiness

Operator (or intern with mentor) **can**:

| Skill | Verification |
|-------|--------------|
| Run one prototype | exercise-run-first-demo |
| Read one trace | exercise-read-trace |
| Run evaluation smoke | `run_demo_smoke_checks.py` PASS |
| Explain fail-closed | beginner assessment Q1 + bypass demo |
| Explain critic ≠ truth | Q2 + failed-review trace |
| Explain LLM output ≠ truth | Q3 + malformed demo |
| Explain approval gate | Q4 + no-approval demo |
| Write simple change proposal | change-template exercise |
| Decide rollback vs patch | decide-rollback exercise |
| Identify platform drift | identify-platform-drift exercise |

---

## Repository readiness

| Asset | Present |
|-------|---------|
| Doctrine | `agent-os/doctrine/` |
| Prototypes | `prototypes/` |
| Workflows | `prototypes/integrations/` |
| Real adapters | `integrations-real/` |
| Observability | `observability/` |
| Evaluation | `evaluation/` |
| Evolution | `evolution/` |
| Operator playbooks | `operator-playbooks/` |
| RU curriculum | `curriculum/ru/` |
| Phase 2.8 audit | `governance/phase-2-8/` |

---

## Governance readiness

| Document | Purpose |
|----------|---------|
| [PHASE_3_FREEZE_POLICY.md](PHASE_3_FREEZE_POLICY.md) | Freeze |
| [PHASE_3_MINIMAL_SCOPE.md](PHASE_3_MINIMAL_SCOPE.md) | Scope limit |
| [PHASE_3_RISK_REGISTER.md](PHASE_3_RISK_REGISTER.md) | Risks |
| [PHASE_3_GO_NO_GO.md](PHASE_3_GO_NO_GO.md) | Decision |
| [PHASE_3_DO_NOT_BUILD_LIST.md](PHASE_3_DO_NOT_BUILD_LIST.md) | Forbidden |

---

## Team gates (before implementation)

- [ ] Mentor sign-off (operator or developer assessment)
- [ ] Lead sign-off (lead assessment)
- [ ] Architect co-sign phase-3-readiness
- [ ] Smoke 12/12 + trace 6/6 on audit machine
- [ ] No open critical governance regression

---

## Explicitly NOT ready

See curriculum phase-3-entry-criteria «NOT ready if» — prototypes ≠ MVP, swarm before single workflow, skip evaluation.
