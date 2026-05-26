# Real Provider Scenario Checklist

Phase 3.3 — contract scenarios for local OpenAI-compatible boundary.

---

## Scenarios

| Scenario | Command | Expected Behavior | Network? | Pass Criteria |
|----------|---------|-------------------|----------|---------------|
| `real_provider_forbidden_without_flag` | `python minimal_demo.py --scenario real_provider_forbidden_without_flag` | Real provider disabled without flag | **No** | `provider_disabled`, FAILED, exit 0 |
| `real_provider_missing_config` | `python minimal_demo.py --scenario real_provider_missing_config --real-provider` (no `RA_LLM_BASE_URL`) | Missing base URL blocks | **No** | `provider_config_missing`, FAILED |
| `real_provider_synthetic` | `python minimal_demo.py --scenario real_provider_synthetic --real-provider` | Live call if configured | **Yes** (opt-in) | parse → verify → approval → DELIVERED or fail-closed |

---

## Automated check (default no-network)

```powershell
python evaluation/scripts/check_review_assistant_real_provider_contract.py
```

Expected: `PASS=2 FAIL=0`

---

## Optional live check

Requires local endpoint (LM Studio, Ollama, vLLM, etc.):

```powershell
$env:RA_LLM_BASE_URL = "http://127.0.0.1:1234"
# optional: $env:RA_LLM_API_KEY = "..."
# optional: $env:RA_LLM_MODEL = "local-model"
python evaluation/scripts/check_review_assistant_real_provider_contract.py --real-provider
```

---

## Regression (must still pass)

```powershell
python evaluation/scripts/check_review_assistant_thin.py
python evaluation/scripts/check_review_assistant_llm_mock.py
```
