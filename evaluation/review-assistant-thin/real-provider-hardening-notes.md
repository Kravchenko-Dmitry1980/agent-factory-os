# Real Provider Hardening Notes

Phase 3.3 — scope and limits.

---

## Checked locally without provider

- `real_provider_forbidden_without_flag` — no `--real-provider` → no network
- `real_provider_missing_config` — flag set but no `RA_LLM_BASE_URL` → no network
- Default checker script never calls network

---

## Requires local endpoint

- `real_provider_synthetic` with `--real-provider` + `RA_LLM_BASE_URL`
- Optional checker flag: `--real-provider` on contract script

---

## What is NOT proven

- Model quality or benchmark scores
- Prompt injection resistance (live)
- Production readiness
- Multi-provider behavior
- RU cloud providers

---

## Data policy

- **Synthetic prompt only** — hardcoded in `minimal_demo.py`
- No user paste, repo files, `.env`, secrets, PII, client data

---

## Mock remains default

- No `--real-provider` → mock/legacy paths unchanged
- Original 5 + mock LLM 5 scenarios unchanged

---

## No provider framework

Single boundary functions only — no registry, router, or SDK.
