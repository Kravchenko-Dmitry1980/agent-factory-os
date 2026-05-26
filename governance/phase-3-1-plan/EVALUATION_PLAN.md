# Evaluation Plan — Phase 3.1 Thin Review Assistant

**When to run:** After future implementation (Phase 3.1-Impl), before acceptance.

---

## Pre-implementation baseline (must PASS before code)

```powershell
cd C:\Dima\Projects\CURSOR\AGENT
python evaluation/scripts/run_demo_smoke_checks.py
python evaluation/scripts/check_expected_text_traces.py
```

| Check | Expected | Last known (2026-05-26) |
|-------|----------|-------------------------|
| Smoke | PASS=12 FAIL=0 | PASS |
| Trace | PASS=6 FAIL=0 | PASS |

Re-run on implementation start day and after implementation.

---

## Required scenario checks (impl-specific)

Run impl entry with scenario flags matching frozen template:

| Scenario | Expected safe behavior | Source |
|----------|------------------------|--------|
| Good draft approved | Delivery only after human approve | [evaluation.md](../../agent-builder-kit/templates/review-assistant-agent/evaluation.md) §1 |
| Bad draft rejected | No delivery; `approval_denied` | §2 |
| Critic uncertain | Fail-closed; no auto-delivery | §3 |
| Missing approval blocks | No delivery without approval step | §4 |
| Unsafe publish / bypass blocked | Block with audit | §5 |

Cross-reference: `evaluation/scenarios/review-loop-scenarios.md`

---

## Structural checks (no drift)

| Check | Pass criteria |
|-------|---------------|
| No runtime folder | No `runtime/`, `factory/`, `generator/` under impl or kit |
| No external action | No network calls in impl code |
| No persistent memory | No file/db profile store |
| No new dependencies | `requirements.txt` unchanged unless approved |
| Protected folders unchanged | git diff clean on prototypes/, eval/scripts/, etc. |
| Frozen spec unchanged | No semantic diff on 12 template files |

---

## Quality gates reference

Map impl behavior to `evaluation/quality-gates/`:

| Gate file | Impl must demonstrate |
|-----------|----------------------|
| fail-closed-gate.md | uncertain / missing approval blocks |
| verification-gate.md | verification events in trace |
| approval-gate.md | human before delivery |
| escalation-gate.md | uncertain → escalate or hold |
| audit-gate.md | full trace on all scenarios |

---

## Kit checklists

After impl, complete:

- [template-acceptance-checklist.md](../../agent-builder-kit/evaluation-checklists/template-acceptance-checklist.md) — for **behavior**, not re-accepting frozen spec
- [safety-regression-checklist.md](../../agent-builder-kit/evaluation-checklists/safety-regression-checklist.md)
- [trace-review-checklist.md](../../agent-builder-kit/evaluation-checklists/trace-review-checklist.md)
- [POST_IMPLEMENTATION_CHECKLIST.md](POST_IMPLEMENTATION_CHECKLIST.md)

---

## Evaluation loop

See [diagrams/evaluation-loop.md](diagrams/evaluation-loop.md)

---

## Fail policy

Any scenario fail → **do not accept** impl → follow [ROLLBACK_PLAN.md](ROLLBACK_PLAN.md)

Do not weaken `evaluation/scripts/` to make impl pass.

---

## Evidence to record

Create `governance/PHASE_3_1_IMPLEMENTATION_REVIEW.md` (future) with:

- Command lines used
- Smoke/trace summary
- Per-scenario pass/fail
- Trace snippets vs expected-traces.md
