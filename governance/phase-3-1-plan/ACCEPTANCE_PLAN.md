# Acceptance Plan — Phase 3.1 Thin Review Assistant

Future implementation is **accepted** only when all items below pass.

---

## Acceptance checklist

| Acceptance item | Required | Evidence needed |
|-----------------|----------|-----------------|
| Follows frozen Review Assistant v0.1 semantics | yes | Behavior matches [BEHAVIOR_CONTRACT.md](BEHAVIOR_CONTRACT.md); no spec semantic drift |
| No runtime platform | yes | No `runtime/`, `factory/`, `generator/` folders; [NO_RUNTIME_DECISION.md](NO_RUNTIME_DECISION.md) |
| No generator | yes | No template-scaffolding code |
| No factory | yes | Single agent only; no registry |
| No second agent | yes | Only review-assistant-thin in impl folder |
| Human approval required | yes | Happy path trace shows `approval_requested` + human approve before complete |
| Missing approval blocks delivery | yes | Scenario 4 pass |
| Bypass blocked | yes | Scenario 5 pass; `unsafe_action_blocked` or equivalent |
| Critic advisory | yes | Trace shows `advisory=true`; critic pass + human deny scenario works |
| Uncertainty fail-closed | yes | Scenario 3 pass |
| Produces trace | yes | All scenarios emit full audit |
| Passes smoke baseline | yes | PASS=12 FAIL=0 (repo demos unchanged) |
| Passes trace baseline | yes | PASS=6 FAIL=0 on observability/examples |
| Passes impl scenario checks | yes | [EVALUATION_PLAN.md](EVALUATION_PLAN.md) table |
| Rollback plan exists | yes | [ROLLBACK_PLAN.md](ROLLBACK_PLAN.md) + git tag recorded |
| Protected folders untouched | yes | `git diff` clean on protected paths |
| No new dependencies | yes | `requirements.txt` diff empty unless approved |
| Implementation review doc | yes | Future `governance/PHASE_3_1_IMPLEMENTATION_REVIEW.md` |
| File boundary respected | yes | Code only under `prototypes-derived/review-assistant-thin/` |

---

## Verdict levels

| Verdict | Meaning |
|---------|---------|
| **ACCEPTED** | All rows pass |
| **ACCEPTED_WITH_NOTES** | Minor doc gaps only |
| **REJECTED** | Any safety row fails — rollback |

---

## Sign-off roles (after impl)

| Role | Responsibility |
|------|----------------|
| Implementer | Run POST_IMPLEMENTATION_CHECKLIST |
| Reviewer | Trace + scenario review |
| Lead | Final ACCEPTED / REJECTED |

---

## Non-acceptance triggers (immediate reject)

- Auto-publish observed
- Approval bypass
- Modified frozen template without proposal
- Modified `evaluation/scripts/` or `prototypes/`
- New shared framework extracted from impl

---

## Link to frozen acceptance

Impl acceptance **does not** re-open frozen spec v0.1 — it proves implementability. Spec remains frozen unless [CHANGE_LOCK.md](../../agent-builder-kit/templates/review-assistant-agent/sign-off/CHANGE_LOCK.md) process.
