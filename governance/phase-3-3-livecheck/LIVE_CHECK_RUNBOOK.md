# Live Check Runbook

Exact commands for Phase 3.3-LiveCheck validation.

**Repository root:** `C:\Dima\Projects\CURSOR\AGENT`

---

## 1. Baseline (no network required)

```powershell
cd C:\Dima\Projects\CURSOR\AGENT

python evaluation/scripts/check_review_assistant_thin.py
python evaluation/scripts/check_review_assistant_llm_mock.py
python evaluation/scripts/check_review_assistant_real_provider_contract.py
python evaluation/scripts/run_demo_smoke_checks.py
python evaluation/scripts/check_expected_text_traces.py
```

**Expected:**

| Script | Expected summary |
|--------|------------------|
| `check_review_assistant_thin.py` | PASS=5 FAIL=0 |
| `check_review_assistant_llm_mock.py` | PASS=5 FAIL=0 |
| `check_review_assistant_real_provider_contract.py` | PASS=2 FAIL=0 (live scenario SKIP) |
| `run_demo_smoke_checks.py` | PASS=12 FAIL=0 |
| `check_expected_text_traces.py` | PASS=6 FAIL=0 |

---

## 2. LM Studio environment (operator session)

Start LM Studio Local Server manually first. Then:

```powershell
$env:RA_LLM_BASE_URL = "http://127.0.0.1:1234"
$env:RA_LLM_MODEL = "qwen2.5-7b-instruct-1m"
```

---

## 3. Live provider check

Requires running local server and env vars above:

```powershell
python evaluation/scripts/check_review_assistant_real_provider_contract.py --real-provider
```

**Expected:** `Summary: PASS=3 FAIL=0`

Includes:

- `real_provider_forbidden_without_flag` (no network)
- `real_provider_missing_config` (no network)
- `real_provider_synthetic (live)` (network to localhost only)

---

## 4. Manual single scenario (optional)

```powershell
python prototypes-derived/review-assistant-thin/minimal_demo.py --scenario real_provider_synthetic --real-provider
```

Inspect stdout trace for verify + approval events. Raw provider text is not persisted by design.

---

## 5. Order of execution

1. Baseline scripts (always)
2. Start LM Studio manually
3. Set env vars
4. Live contract script
5. Optional single scenario
6. Record results in [LIVE_CHECK_RESULT.md](LIVE_CHECK_RESULT.md)

---

## 6. If LM Studio is not running

Do not start it from repo automation. Either:

- Operator starts server and reruns step 3, or
- Record prior manual run as observed PASS and mark rerun `NOT_RERUN`

This phase recorded both operator-observed PASS and Cursor-confirmed rerun PASS on 2026-05-26.
