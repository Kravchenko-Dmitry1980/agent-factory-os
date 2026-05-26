# Live Provider Checklist — Phase 3.3-LiveCheck

Evaluation checklist for manual local endpoint validation.

**Repo:** `C:\Dima\Projects\CURSOR\AGENT`

---

## Prerequisites (operator)

- [x] LM Studio running locally
- [x] Model loaded: `qwen2.5-7b-instruct-1m`
- [x] Local Server at `http://127.0.0.1:1234`
- [x] Cloud provider not used
- [x] API key not used
- [x] Synthetic data only

---

## Step checklist

| Step | Command | Expected | Result (2026-05-26) |
|------|---------|----------|---------------------|
| 1. Thin baseline | `python evaluation/scripts/check_review_assistant_thin.py` | PASS=5 FAIL=0 | **PASS** |
| 2. Mock LLM | `python evaluation/scripts/check_review_assistant_llm_mock.py` | PASS=5 FAIL=0 | **PASS** |
| 3. No-network contract | `python evaluation/scripts/check_review_assistant_real_provider_contract.py` | PASS=2 FAIL=0 | **PASS** |
| 4. Smoke | `python evaluation/scripts/run_demo_smoke_checks.py` | PASS=12 FAIL=0 | **PASS** |
| 5. Trace | `python evaluation/scripts/check_expected_text_traces.py` | PASS=6 FAIL=0 | **PASS** |
| 6. Set env | `$env:RA_LLM_BASE_URL = "http://127.0.0.1:1234"`; `$env:RA_LLM_MODEL = "qwen2.5-7b-instruct-1m"` | vars set | **done** |
| 7. Live contract | `python evaluation/scripts/check_review_assistant_real_provider_contract.py --real-provider` | PASS=3 FAIL=0 | **PASS** |

---

## Observed live configuration

| Field | Value |
|-------|-------|
| Provider | LM Studio |
| Endpoint | `http://127.0.0.1:1234` |
| Model | `qwen2.5-7b-instruct-1m` |
| Data | synthetic only |
| Cloud | no |
| Secrets | no |

---

## Optional manual scenario

| Step | Command | Expected |
|------|---------|----------|
| Single live demo | `python prototypes-derived/review-assistant-thin/minimal_demo.py --scenario real_provider_synthetic --real-provider` | verify → approval → DELIVERED or fail-closed |

Not required for LiveCheck PASS; contract script is authoritative.

---

## Policy confirmation

| Check | Status |
|-------|--------|
| Provider framework created | no |
| Runtime / factory added | no |
| Code changed in LiveCheck | no |
| `.env` committed | no |

---

## Governance cross-links

- [../../governance/phase-3-3-livecheck/README.md](../../governance/phase-3-3-livecheck/README.md)
- [../../governance/phase-3-3-livecheck/LIVE_CHECK_RESULT.md](../../governance/phase-3-3-livecheck/LIVE_CHECK_RESULT.md)
- [real-provider-scenario-checklist.md](real-provider-scenario-checklist.md)

---

## Verdict

**Live provider check PASS=3 FAIL=0** — ready for Phase 3.3.1-Freeze v0.3.
