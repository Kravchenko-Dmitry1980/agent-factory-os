# Task Triage Agent — Provider Policy

**Date:** 2026-05-26  
**Status:** PLAN_ONLY

---

## Default (Phase 3.5 and future v0.1 template)

| Rule | Value |
|------|-------|
| Provider calls | **Forbidden by default** |
| Network | **None** |
| Cloud providers | **Forbidden** |
| RU providers (GigaChat, YandexGPT) | **Forbidden** |
| LM Studio / local OpenAI-compatible | **Forbidden until separate phase** |
| Provider framework | **Forbidden** |

Task classification uses **rules and synthetic logic** in future thin impl — not LLM by default.

---

## Phase 3.5 planning

**No provider implementation.** No env vars. No API keys. No `--provider` flag design in this plan beyond "defer."

---

## Future provider path (requires new phase + approval)

If provider-assisted classification is ever approved:

| Requirement | Detail |
|-------------|--------|
| Order | Mock/rules first → optional local provider later |
| Data | Synthetic task text only in eval |
| Opt-in | Explicit flag; disabled by default |
| Local only | OpenAI-compatible local endpoint first |
| No cloud default | Separate governance for cloud |
| No framework | Single boundary function — mirror Review Assistant v0.3 |
| Output not truth | Classification must pass safety gates independently |
| Eval | No-network contract check + optional live opt-in |
| Harness | Separate triage safety eval — not merged into provider safety harness |

Mirror: [Review Assistant provider boundary](../../prototypes-derived/review-assistant-thin/freeze/V0_3_REAL_PROVIDER_BOUNDARY_BASELINE.md) discipline.

---

## Forbidden provider patterns

- Default provider on triage startup
- Provider chooses final triage decision without gates
- Provider text bypasses orchestrator/execution policies
- Provider compares/ranks models
- Storing provider responses in persistent memory

---

## Relation to provider-safety-harness-v0.1

Provider safety harness tests **Review Assistant provider output** — not Task Triage.

Future triage provider eval is a **separate script/phase** if ever needed.

Do not modify `check_review_assistant_provider_safety.py` for triage.
