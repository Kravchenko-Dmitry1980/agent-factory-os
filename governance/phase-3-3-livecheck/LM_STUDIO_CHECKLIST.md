# LM Studio Checklist — Phase 3.3-LiveCheck

Manual operator checklist for live provider validation.

---

## Manual setup checklist

- [x] LM Studio opened by operator (not by repo scripts)
- [x] Model `qwen2.5-7b-instruct-1m` downloaded manually
- [x] Model loaded manually in LM Studio
- [x] Local Server enabled manually
- [x] Endpoint reachable at `http://127.0.0.1:1234`
- [x] Cloud provider not used
- [x] API key not used
- [x] Synthetic data only (hardcoded scenario prompt)

---

## PowerShell environment

```powershell
$env:RA_LLM_BASE_URL = "http://127.0.0.1:1234"
$env:RA_LLM_MODEL = "qwen2.5-7b-instruct-1m"
```

Do **not** set `RA_LLM_API_KEY` unless your local tool requires it. This phase used no key.

---

## Live check command

```powershell
cd C:\Dima\Projects\CURSOR\AGENT
python evaluation/scripts/check_review_assistant_real_provider_contract.py --real-provider
```

**Observed result:** `Summary: PASS=3 FAIL=0`

---

## Optional manual scenario

```powershell
python prototypes-derived/review-assistant-thin/minimal_demo.py --scenario real_provider_synthetic --real-provider
```

---

## What NOT to do

| Do not | Reason |
|--------|--------|
| Expose Local Server to network / `0.0.0.0` without intent | Local-only boundary assumption |
| Use real project, client, or medical data | Synthetic-only policy |
| Paste secrets into chat, traces, or commits | No secrets policy |
| Commit `.env` or key files | Repo must stay key-free |
| Switch to cloud provider in this phase | Out of scope; changes risk profile |
| Patch repo code when setup fails | Fix LM Studio setup first |

---

## Baseline before live (must pass)

```powershell
python evaluation/scripts/check_review_assistant_thin.py          # PASS=5
python evaluation/scripts/check_review_assistant_llm_mock.py      # PASS=5
python evaluation/scripts/check_review_assistant_real_provider_contract.py  # PASS=2
python evaluation/scripts/run_demo_smoke_checks.py                # PASS=12
python evaluation/scripts/check_expected_text_traces.py           # PASS=6
```
