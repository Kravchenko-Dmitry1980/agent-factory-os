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

## Real provider eval (Phase 3.3)

```powershell
python evaluation/scripts/check_review_assistant_real_provider_contract.py
```

Expected: `Summary: PASS=2 FAIL=0` (no network)

| File | Purpose |
|------|---------|
| [real-provider-scenario-checklist.md](real-provider-scenario-checklist.md) | Real provider checklist |
| [real-provider-expected-events.md](real-provider-expected-events.md) | Event substrings |
| [real-provider-hardening-notes.md](real-provider-hardening-notes.md) | Scope limits |
| [live-provider-checklist.md](live-provider-checklist.md) | **Phase 3.3-LiveCheck** — LM Studio live validation checklist |

---

## Provider safety eval (Phase 3.4)

```powershell
python evaluation/scripts/check_review_assistant_provider_safety.py
```

Expected: `Summary: PASS=16 FAIL=0` (no network, no provider calls)

| File | Purpose |
|------|---------|
| [provider-safety/README.md](provider-safety/README.md) | Harness overview |
| [provider-safety/provider-safety-cases.md](provider-safety/provider-safety-cases.md) | 16 synthetic cases (groups A–G) |
| [provider-safety/harness-limitations.md](provider-safety/harness-limitations.md) | Scope limits |
| [provider-safety/freeze/README.md](provider-safety/freeze/README.md) | **Frozen v0.1** — provider-safety-harness-v0.1 |

---

## Impl freeze

**Current:** [review-assistant-thin-v0.3](../../prototypes-derived/review-assistant-thin/freeze/V0_3_SCENARIO_BASELINE.md)

Baselines:

- v0.3: [V0_3_SCENARIO_BASELINE.md](../../prototypes-derived/review-assistant-thin/freeze/V0_3_SCENARIO_BASELINE.md)
- v0.2: [V0_2_SCENARIO_BASELINE.md](../../prototypes-derived/review-assistant-thin/freeze/V0_2_SCENARIO_BASELINE.md)
- v0.1: [SCENARIO_BASELINE.md](../../prototypes-derived/review-assistant-thin/freeze/SCENARIO_BASELINE.md)

---

## Frozen spec (unchanged)

`agent-builder-kit/templates/review-assistant-agent/` v0.1
