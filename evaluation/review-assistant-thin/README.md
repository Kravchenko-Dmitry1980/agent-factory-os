# Review Assistant Thin — Local Evaluation

**Small local checks** for `prototypes-derived/review-assistant-thin/` only.

---

## What this is

- Scenario checklist
- Expected trace event substrings
- One optional stdlib script: `evaluation/scripts/check_review_assistant_thin.py`

---

## What this is NOT

- General test framework
- CI/CD or GitHub Actions
- Benchmark or model scoring platform
- Production QA
- pytest suite

---

## Quick run

```powershell
cd C:\Dima\Projects\CURSOR\AGENT
python evaluation/scripts/check_review_assistant_thin.py
```

Expected: `Summary: PASS=5 FAIL=0`

Also run Phase 2 baseline (must not regress):

```powershell
python evaluation/scripts/run_demo_smoke_checks.py
python evaluation/scripts/check_expected_text_traces.py
```

---

## Files

| File | Purpose |
|------|---------|
| [scenario-checklist.md](scenario-checklist.md) | Manual checklist |
| [expected-events.md](expected-events.md) | Required event substrings |
| [hardening-notes.md](hardening-notes.md) | Scope and limits |

---

## LLM mock eval (Phase 3.2)

```powershell
python evaluation/scripts/check_review_assistant_llm_mock.py
```

Expected: `Summary: PASS=5 FAIL=0`

| File | Purpose |
|------|---------|
| [llm-scenario-checklist.md](llm-scenario-checklist.md) | LLM manual checklist |
| [llm-expected-events.md](llm-expected-events.md) | LLM event substrings |
| [llm-hardening-notes.md](llm-hardening-notes.md) | LLM scope limits |

---

## Impl freeze

**Current:** [review-assistant-thin-v0.2](../../prototypes-derived/review-assistant-thin/freeze/V0_2_SCENARIO_BASELINE.md)

Baselines: [V0_2_SCENARIO_BASELINE.md](../../prototypes-derived/review-assistant-thin/freeze/V0_2_SCENARIO_BASELINE.md) (v0.1: [SCENARIO_BASELINE.md](../../prototypes-derived/review-assistant-thin/freeze/SCENARIO_BASELINE.md))

---

## Frozen spec (unchanged)

`agent-builder-kit/templates/review-assistant-agent/` v0.1
