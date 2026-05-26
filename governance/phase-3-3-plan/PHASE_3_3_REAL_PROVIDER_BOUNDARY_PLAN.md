# Phase 3.3 — Real LLM Provider Boundary Plan

**Type:** plan only  
**Baseline:** review-assistant-thin-v0.2 (mock LLM frozen)

---

## Goal

Prepare **safe future integration** of **one** real LLM provider into Review Assistant Thin — without building it in this phase.

---

## Why real provider matters (beyond mock)

Mock v0.2 validates parse → safety → verification → approval **deterministically**. Real provider adds:

| Risk class | Mock coverage | Real gap |
|------------|---------------|----------|
| Network failures | none | connection reset, DNS, TLS |
| Timeouts | simulated | live latency variance |
| Rate limits | none | 429, backoff policy |
| Malformed live JSON/text | simulated shapes | provider-specific quirks |
| Hallucination | controlled | unbounded content |
| Prompt injection | unsafe flag scenario | live adversarial input |
| Secret handling | N/A | keys in env, log leakage |
| Cost | zero | quota, billing surprises |
| Privacy | local only | data leaves machine (cloud) |
| Provider errors | limited | auth, model not found, policy refusals |

---

## Target flow (future implementation)

```text
user task
  → provider request boundary (prepare, redact, bound size/timeout)
  → provider request (network — only if explicit real mode flag)
  → provider response (untrusted raw)
  → parse
  → safety check
  → verification gate
  → human approval gate
  → delivery OR block/escalate/fail
  → trace (no secrets)
```

Aligns with frozen mock chain in v0.2; event names may gain `provider_*` prefix alongside legacy `llm_*` for compatibility.

---

## What this plan allows (future, after approval)

- Single-provider boundary module in `minimal_demo.py` (future phase only)
- Explicit `--provider-mode mock|real` (mock default)
- One approved provider config (env-based secret)
- Extended eval scenarios for live provider (synthetic data only in first test)
- v0.3 freeze record after passing eval

---

## What this plan forbids

| Forbidden | Notes |
|-----------|-------|
| Provider framework / registry / router | [NO_PROVIDER_FRAMEWORK_POLICY.md](NO_PROVIDER_FRAMEWORK_POLICY.md) |
| Multi-provider switching | One mode at a time |
| RAG / MCP | Out of scope |
| Desktop UI / Operator Console | Phase 4+ |
| Production deployment | Lab/demo only |
| Auto-publish | Always blocked without approval |
| Hidden memory writeback | Template doctrine |
| External actions from model output | No tool execution from provider text |
| Default real provider call | Mock must remain default |
| Sensitive data in first live test | [ALLOWED_DATA_POLICY.md](ALLOWED_DATA_POLICY.md) |

---

## Document map

| Topic | Doc |
|-------|-----|
| Provider choice analysis | [PROVIDER_SELECTION_REVIEW.md](PROVIDER_SELECTION_REVIEW.md) |
| One provider rule | [SINGLE_PROVIDER_DECISION.md](SINGLE_PROVIDER_DECISION.md) |
| I/O contract | [PROVIDER_BOUNDARY_CONTRACT.md](PROVIDER_BOUNDARY_CONTRACT.md) |
| Data | [ALLOWED_DATA_POLICY.md](ALLOWED_DATA_POLICY.md), [FORBIDDEN_DATA_POLICY.md](FORBIDDEN_DATA_POLICY.md) |
| Secrets | [SECRET_HANDLING_POLICY.md](SECRET_HANDLING_POLICY.md) |
| Errors | [PROVIDER_ERROR_HANDLING.md](PROVIDER_ERROR_HANDLING.md) |
| Failures | [REAL_PROVIDER_FAILURE_MODES.md](REAL_PROVIDER_FAILURE_MODES.md) |
| Security | [REAL_PROVIDER_SECURITY_REVIEW.md](REAL_PROVIDER_SECURITY_REVIEW.md) |
| Eval / trace / rollback | REAL_PROVIDER_*_PLAN.md |
| RU providers | [RU_PROVIDER_FUTURE_BACKLOG.md](RU_PROVIDER_FUTURE_BACKLOG.md) |
| Gates | [PRECONDITIONS_FOR_REAL_PROVIDER_IMPLEMENTATION.md](PRECONDITIONS_FOR_REAL_PROVIDER_IMPLEMENTATION.md) |
| Decision | [PHASE_3_3_GO_NO_GO.md](PHASE_3_3_GO_NO_GO.md) |

---

## Phase boundary

**Phase 3.3-Plan:** markdown only (this folder).  
**Phase 3.3-Impl (future):** code + eval + freeze v0.3 — requires separate approval.
