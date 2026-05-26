# Live Provider Record — Review Assistant Thin v0.3

LM Studio live validation recorded at v0.3 freeze.

**Source:** Phase 3.3-LiveCheck (2026-05-26)  
**Status in freeze phase:** LIVE_CHECK_OBSERVED_PASS — live check not rerun during 3.3.1

---

## LiveCheck status

**LIVE_CHECK_PASS**

Governance: [governance/PHASE_3_3_LIVE_PROVIDER_CHECK_REVIEW.md](../../../governance/PHASE_3_3_LIVE_PROVIDER_CHECK_REVIEW.md)

---

## Provider

| Field | Value |
|-------|-------|
| Tool | LM Studio |
| Endpoint | `http://127.0.0.1:1234` |
| Model | `qwen2.5-7b-instruct-1m` |
| API shape | OpenAI-compatible local server |
| Cloud | no |
| API key | none |

---

## Command (observed)

```powershell
$env:RA_LLM_BASE_URL = "http://127.0.0.1:1234"
$env:RA_LLM_MODEL = "qwen2.5-7b-instruct-1m"

python evaluation/scripts/check_review_assistant_real_provider_contract.py --real-provider
```

---

## Result

```
PASS  real_provider_forbidden_without_flag  ok
PASS  real_provider_missing_config          ok
PASS  real_provider_synthetic (live)        ok

Summary: PASS=3 FAIL=0
```

Observed: human operator manual run + Cursor validation during Phase 3.3-LiveCheck.

---

## Safety confirmations

| Condition | Verified |
|-----------|----------|
| Synthetic data only | yes |
| No cloud provider | yes |
| No API key used | yes |
| No secrets printed in trace | yes |
| No secrets committed | yes |
| No provider framework | yes |
| No runtime / factory | yes |
| No second agent | yes |
| Mock default preserved | yes |

---

## Limitations (explicit)

| Limitation | Notes |
|------------|-------|
| One local model only | qwen2.5-7b-instruct-1m on LM Studio |
| No model quality benchmark | Contract PASS ≠ good answers |
| No live prompt injection suite | Single synthetic prompt |
| No production readiness | Local demo only |
| No provider comparison | LM Studio only; Ollama not tested |
| Raw provider text not stored | By design |

---

## Related docs

| Doc | Path |
|-----|------|
| LiveCheck folder | [governance/phase-3-3-livecheck/README.md](../../../governance/phase-3-3-livecheck/README.md) |
| LiveCheck result | [governance/phase-3-3-livecheck/LIVE_CHECK_RESULT.md](../../../governance/phase-3-3-livecheck/LIVE_CHECK_RESULT.md) |
| Eval checklist | [evaluation/review-assistant-thin/live-provider-checklist.md](../../../evaluation/review-assistant-thin/live-provider-checklist.md) |
| Provider baseline | [V0_3_REAL_PROVIDER_BOUNDARY_BASELINE.md](V0_3_REAL_PROVIDER_BOUNDARY_BASELINE.md) |

---

## Re-run policy

Re-run live check only when:

- Operator starts LM Studio manually
- Env vars set in session
- Validating after impl change (post-unfreeze)

Do not automate server start from repo.
