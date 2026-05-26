# Demo Runner v0.1 — Command Baseline

**Version:** demo-runner-v0.1  
**Date:** 2026-05-26  
**Status:** FROZEN

All commands run from repository root: `C:\Dima\Projects\CURSOR\AGENT`

---

## Core commands

### Interactive menu

```powershell
python demos/review-assistant-runner/demo_runner.py
```

### List all scenarios

```powershell
python demos/review-assistant-runner/demo_runner.py --list
```

---

## Direct scenario run (demo)

```powershell
python demos/review-assistant-runner/demo_runner.py --scenario happy
python demos/review-assistant-runner/demo_runner.py --scenario missing_approval
python demos/review-assistant-runner/demo_runner.py --scenario unsafe_publish_attempt
```

All demo keys: see [DEMO_RUNNER_V0_1_MENU_BASELINE.md](DEMO_RUNNER_V0_1_MENU_BASELINE.md).

---

## Validation via runner (Group 4)

```powershell
python demos/review-assistant-runner/demo_runner.py --scenario provider_safety_harness
python demos/review-assistant-runner/demo_runner.py --scenario thin_baseline
python demos/review-assistant-runner/demo_runner.py --scenario mock_llm_baseline
python demos/review-assistant-runner/demo_runner.py --scenario real_provider_contract_no_network
python demos/review-assistant-runner/demo_runner.py --scenario smoke_checks
python demos/review-assistant-runner/demo_runner.py --scenario text_trace_checks
```

---

## Transcript (explicit flag only)

```powershell
python demos/review-assistant-runner/demo_runner.py --scenario happy --save-transcript
```

Default: **no transcript saved**.

---

## Debug

```powershell
python demos/review-assistant-runner/demo_runner.py --scenario happy --debug
```

---

## Real provider (manual only)

**Not part of default validation. Requires confirmation. Not run during freeze.**

```powershell
$env:RA_LLM_BASE_URL = "http://127.0.0.1:1234"
$env:RA_LLM_MODEL = "qwen2.5-7b-instruct-1m"
python demos/review-assistant-runner/demo_runner.py --scenario real_provider_synthetic
```

Runner will:

1. Show warning
2. Ask `Продолжить? yes/no`
3. Check `RA_LLM_BASE_URL`
4. Only then invoke `minimal_demo.py --scenario real_provider_synthetic --real-provider`

---

## Underlying commands (invoked by runner, not edited)

Demo scenarios:

```text
python prototypes-derived/review-assistant-thin/minimal_demo.py --scenario <name>
python prototypes-derived/review-assistant-thin/minimal_demo.py --scenario real_provider_synthetic --real-provider
```

Evaluation scripts:

```text
python evaluation/scripts/check_review_assistant_provider_safety.py
python evaluation/scripts/check_review_assistant_thin.py
python evaluation/scripts/check_review_assistant_llm_mock.py
python evaluation/scripts/check_review_assistant_real_provider_contract.py
python evaluation/scripts/run_demo_smoke_checks.py
python evaluation/scripts/check_expected_text_traces.py
```
