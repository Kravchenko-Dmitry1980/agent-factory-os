# Evaluation & Regression Harness (Phase 2.5)

**Status:** Local behavioral checking — not CI/CD, not production QA, not a benchmark platform.

---

## Why Evaluation Is Needed

Governed AI workflows can **look healthy while becoming unsafe**:

- Demos still run after a gate is weakened
- Logs still print after approval is skipped
- Memory still grows after writeback rules change
- Retries still happen after the ceiling is raised

Phase 2.5 teaches **how to check behavior stayed safe** after a change — without building a test platform.

---

## Why AI Systems Can Silently Regress

| Silent regression | Why it is dangerous |
|-------------------|---------------------|
| Critic pass treated as approval | Plausible draft publishes without human check |
| Retry limit +1 | Verification bugs masked instead of fixed |
| Mock shortcut in real adapter | Fail-closed path never exercised |
| Memory write without verification | Unbounded context drift |
| GUI click without visual match | Wrong screen, real side effect |

Each change alone looks small. Together they **erase governance**.

---

## Why "It Still Runs" Is Not Enough

Running a demo proves **execution**, not **correct governance**:

```text
Demo exits 0        → process did not crash
Behavior correct    → gates ran in the right order with the right outcome
```

Evaluation compares **actual behavior** (trace, audit, outcome) against **expected behavior** (scenarios, gates, matrices).

---

## Why Behavior Must Be Checked

Every governed workflow must answer eight questions:

1. Did the workflow behave correctly?
2. Did unsafe action get blocked?
3. Did escalation happen when needed?
4. Did retries stop at the limit?
5. Did memory writeback happen only after verification?
6. Did LLM failure get rejected?
7. Did GUI mismatch block execution?
8. Did a change break old behavior?

See [scenarios/](scenarios/) and [quality-gates/](quality-gates/).

---

## Why This Is NOT CI/CD

| CI/CD | Phase 2.5 evaluation |
|-------|----------------------|
| Automated pipeline on every push | Manual or ad-hoc local checks |
| Deployment gate | Change-review gate |
| Test runner framework | Readable scenarios + simple scripts |
| Blocks merge/release | Helps human reviewer decide |

No GitHub Actions. No deployment hooks. No automation platform.

See [governance/no-ci-cd-policy.md](governance/no-ci-cd-policy.md).

---

## Why This Is NOT Production Testing

| Production QA | Phase 2.5 evaluation |
|---------------|----------------------|
| Load, soak, chaos at scale | Single-process local demos |
| Staging environments | Mock mode + optional local adapters |
| SLO dashboards | Human-readable text traces |
| Regression suite in CI | Regression matrix for reviewer |

This layer **protects governance invariants**, not throughput or uptime.

---

## Structure

| Module | Purpose |
|--------|---------|
| [scenarios/](scenarios/) | Small behavioral scenarios per demo |
| [expected-outcomes/](expected-outcomes/) | What "correct" means |
| [trace-comparison/](trace-comparison/) | Compare actual vs expected traces |
| [regression-matrix/](regression-matrix/) | Area × behavior × risk tables |
| [quality-gates/](quality-gates/) | Pre-change checklists |
| [manual-review/](manual-review/) | Human reviewer guidance |
| [failure-injection/](failure-injection/) | Intentional failure cases |
| [scripts/](scripts/) | Simple local Python helpers |
| [review-assistant-thin/](review-assistant-thin/) | **Phase 3.1.1** — thin demo scenario checks (not CI) |
| [diagrams/](diagrams/) | Mermaid evaluation flows |
| [governance/](governance/) | Boundaries and anti-drift rules |
| [reports/](reports/) | Placeholder for local evaluation notes |

---

## Quick Start (Local Only)

```powershell
# Smoke-check selected demos (no API keys required)
python evaluation/scripts/run_demo_smoke_checks.py

# Verify example traces contain required events
python evaluation/scripts/check_expected_text_traces.py

# Phase 3.1.1 — Review Assistant thin (5 scenarios)
python evaluation/scripts/check_review_assistant_thin.py

# Phase 3.2 — Review Assistant mock LLM (5 scenarios)
python evaluation/scripts/check_review_assistant_llm_mock.py

# Phase 3.3 — Review Assistant real provider contract (2 no-network scenarios)
python evaluation/scripts/check_review_assistant_real_provider_contract.py

# Phase 3.4 — Review Assistant provider safety harness (16 synthetic cases, no network)
python evaluation/scripts/check_review_assistant_provider_safety.py
# Frozen: provider-safety-harness-v0.1 — see evaluation/review-assistant-thin/provider-safety/freeze/

# Phase 3.3-LiveCheck — optional live provider (LM Studio; see live-provider-checklist.md)
# $env:RA_LLM_BASE_URL = "http://127.0.0.1:1234"
# python evaluation/scripts/check_review_assistant_real_provider_contract.py --real-provider

# Summary of scenarios, gates, and coverage
python evaluation/scripts/summarize_evaluation_status.py
```

Before accepting a change:

1. Read [quality-gates/quality-gate-checklist.md](quality-gates/quality-gate-checklist.md)
2. Re-run affected scenarios from [scenarios/](scenarios/)
3. Compare trace against [expected-outcomes/](expected-outcomes/)
4. Check [regression-matrix/regression-matrix.md](regression-matrix/regression-matrix.md)

---

## Hard Boundaries

**DO NOT** use this layer to build:

- CI/CD pipelines
- Benchmark / leaderboard platforms
- Model evaluation suites
- Universal test frameworks
- Orchestration runtimes

**DO** use it to prove small behavior stayed safe.

---

## Relation to Other Phases

```
agent-os/doctrine/     → invariants (what must never break)
governance/            → promotion & audit policy
prototypes/            → mock demos to check
integrations-real/     → real I/O demos to check
observability/         → trace format & examples
evolution/             → change discipline before merge
evaluation/            → behavioral checking (this phase)
```

Governance review: [../governance/PHASE_2_5_EVALUATION_REVIEW.md](../governance/PHASE_2_5_EVALUATION_REVIEW.md)
