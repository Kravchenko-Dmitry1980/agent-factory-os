# Mock LLM Boundary — Review Assistant Thin

**Phase 3.2** — local mock only. **No real API.**

---

## What this is

A **mock LLM boundary** simulates model responses locally so Review Assistant can exercise parse, safety, verification, and approval gates **without** calling OpenAI or any external provider.

---

## Why LLM output is untrusted

LLM text is **unverified** until:

1. Parse succeeds (`llm_parse_passed`)
2. Safety checks pass (no unsafe/uncertain flags where blocked)
3. Verification gate passes
4. Human approval granted

**LLM output ≠ truth.** Same rule as critic advisory.

---

## Failure modes handled (mock)

| Mode | Event | Outcome |
|------|-------|---------|
| Malformed payload | `llm_parse_failed` | task_failed — no approval |
| Timeout | `llm_timeout` | escalation — no fallback draft |
| Uncertain claims | `llm_uncertain` | escalation — no auto-delivery |
| Unsafe content | `llm_unsafe_output` + `unsafe_action_blocked` | task_failed |
| Valid draft | `llm_parse_passed` | still requires verification + approval |

---

## Why no real API

- Phase 3.2 scope: **boundary safety**, not model quality
- No secrets, network, or dependencies
- Mock scenarios deterministic for evaluation

---

## Why this is not a provider framework

- No `Provider` base class, registry, or router
- Functions: `get_mock_llm_raw`, `parse_mock_llm_response`, `run_mock_llm_boundary`
- Single mock mode only

---

## Before real LLM integration

Requires separate governance approval:

- User explicit message for real provider
- Security review ([LLM_SECURITY_REVIEW.md](../../governance/phase-3-2-plan/LLM_SECURITY_REVIEW.md))
- Env-based keys (never committed)
- Extended eval + freeze

---

## Scenarios

```powershell
python minimal_demo.py --scenario llm_valid_draft
python minimal_demo.py --scenario llm_malformed_output
python minimal_demo.py --scenario llm_timeout
python minimal_demo.py --scenario llm_uncertain
python minimal_demo.py --scenario llm_unsafe_output
```

Check: `python evaluation/scripts/check_review_assistant_llm_mock.py`
