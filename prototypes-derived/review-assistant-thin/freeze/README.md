# Review Assistant Thin — Freeze Folder

Папка фиксирует **freeze history** реализации Review Assistant Thin.

---

## Freeze history

| Version | Baseline | Record |
|---------|----------|--------|
| **v0.1** | Original thin implementation (5 scenarios, no LLM) | [IMPLEMENTATION_FREEZE_RECORD.md](IMPLEMENTATION_FREEZE_RECORD.md) |
| **v0.2** | Thin + mock LLM boundary (10 scenarios) | [V0_2_FREEZE_RECORD.md](V0_2_FREEZE_RECORD.md) |
| **v0.3** | Thin + mock LLM + real local provider boundary (13 scenarios) | [V0_3_FREEZE_RECORD.md](V0_3_FREEZE_RECORD.md) |

---

## Current frozen version

**review-assistant-thin-v0.3**

Path: `prototypes-derived/review-assistant-thin/`

---

## What v0.3 adds

- Local OpenAI-compatible provider boundary (opt-in)
- Explicit `--real-provider` mode
- 3 real provider contract scenarios (`real_provider_*`)
- No-network contract check (`PASS=2` default)
- LM Studio LiveCheck result (`PASS=3` observed)
- Synthetic-only live provider run
- Provider error / disabled / config-missing checks
- Secret / data / cloud safety policy documented
- [V0_3_REAL_PROVIDER_BOUNDARY_BASELINE.md](V0_3_REAL_PROVIDER_BOUNDARY_BASELINE.md)
- [V0_3_LIVE_PROVIDER_RECORD.md](V0_3_LIVE_PROVIDER_RECORD.md)

---

## What v0.3 does NOT add

- OpenAI cloud
- Anthropic
- GigaChat / YandexGPT
- Bitrix / NeuralDeep
- Provider framework / router / registry
- Runtime / factory / generator
- Second agent / second template
- RAG / MCP
- Desktop UI / Operator Console
- Production deployment
- Persistent memory / auto-publish

---

## What v0.2 adds (historical — preserved)

- Mock LLM boundary (local payloads only)
- 5 LLM mock scenarios (`llm_*`)
- [V0_2_LLM_BOUNDARY_BASELINE.md](V0_2_LLM_BOUNDARY_BASELINE.md)

---

## Why freeze

Phase 3.1 доказал: frozen template можно реализовать локально. Phase 3.2 добавил mock LLM. Phase 3.3 добавил opt-in real local provider. LiveCheck подтвердил LM Studio. Freeze v0.3 фиксирует **рабочую baseline** до любых расширений (cloud provider, prompt injection harness, второй agent).

---

## Key documents (v0.3 — current)

| Doc | Content |
|-----|---------|
| [V0_3_FREEZE_RECORD.md](V0_3_FREEZE_RECORD.md) | Status, date, what changed |
| [V0_3_IMPLEMENTATION_MANIFEST.md](V0_3_IMPLEMENTATION_MANIFEST.md) | File inventory |
| [V0_3_REAL_PROVIDER_BOUNDARY_BASELINE.md](V0_3_REAL_PROVIDER_BOUNDARY_BASELINE.md) | Real provider boundary spec |
| [V0_3_SCENARIO_BASELINE.md](V0_3_SCENARIO_BASELINE.md) | 13 scenario baselines |
| [V0_3_VALIDATION_RECORD.md](V0_3_VALIDATION_RECORD.md) | Check script results |
| [V0_3_LIVE_PROVIDER_RECORD.md](V0_3_LIVE_PROVIDER_RECORD.md) | LM Studio live record |
| [V0_3_CHANGE_LOCK.md](V0_3_CHANGE_LOCK.md) | Change rules (**active**) |
| [V0_3_ROLLBACK_RECORD.md](V0_3_ROLLBACK_RECORD.md) | Rollback to v0.2 |

---

## Historical documents (v0.2 — preserved)

| Doc | Content |
|-----|---------|
| [V0_2_FREEZE_RECORD.md](V0_2_FREEZE_RECORD.md) | v0.2 freeze record |
| [V0_2_IMPLEMENTATION_MANIFEST.md](V0_2_IMPLEMENTATION_MANIFEST.md) | v0.2 manifest |
| [V0_2_LLM_BOUNDARY_BASELINE.md](V0_2_LLM_BOUNDARY_BASELINE.md) | Mock LLM baseline |
| [V0_2_SCENARIO_BASELINE.md](V0_2_SCENARIO_BASELINE.md) | 10 scenarios |
| [V0_2_VALIDATION_RECORD.md](V0_2_VALIDATION_RECORD.md) | v0.2 validation |
| [V0_2_CHANGE_LOCK.md](V0_2_CHANGE_LOCK.md) | v0.2 change lock (superseded) |
| [V0_2_ROLLBACK_RECORD.md](V0_2_ROLLBACK_RECORD.md) | v0.2 rollback |

---

## Historical documents (v0.1 — preserved)

| Doc | Content |
|-----|---------|
| [IMPLEMENTATION_FREEZE_RECORD.md](IMPLEMENTATION_FREEZE_RECORD.md) | v0.1 freeze record |
| [IMPLEMENTATION_MANIFEST.md](IMPLEMENTATION_MANIFEST.md) | v0.1 manifest |
| [SCENARIO_BASELINE.md](SCENARIO_BASELINE.md) | 5 original scenarios |
| [CHANGE_LOCK.md](CHANGE_LOCK.md) | v0.1 change lock |
| [ROLLBACK_RECORD.md](ROLLBACK_RECORD.md) | v0.1 rollback |

---

## Change policy

Любое изменение **поведения** frozen impl → [V0_3_CHANGE_LOCK.md](V0_3_CHANGE_LOCK.md)

---

## Governance

- Phase 3.1 review: [governance/PHASE_3_1_REVIEW_ASSISTANT_THIN_REVIEW.md](../../../governance/PHASE_3_1_REVIEW_ASSISTANT_THIN_REVIEW.md)
- Phase 3.1.1 review: [governance/PHASE_3_1_1_FREEZE_HARDEN_REVIEW.md](../../../governance/PHASE_3_1_1_FREEZE_HARDEN_REVIEW.md)
- Phase 3.2 review: [governance/PHASE_3_2_MOCK_LLM_ADAPTER_REVIEW.md](../../../governance/PHASE_3_2_MOCK_LLM_ADAPTER_REVIEW.md)
- Phase 3.2.1 review: [governance/PHASE_3_2_1_FREEZE_MOCK_LLM_V0_2_REVIEW.md](../../../governance/PHASE_3_2_1_FREEZE_MOCK_LLM_V0_2_REVIEW.md)
- Phase 3.3 review: [governance/PHASE_3_3_REAL_PROVIDER_BOUNDARY_REVIEW.md](../../../governance/PHASE_3_3_REAL_PROVIDER_BOUNDARY_REVIEW.md)
- Phase 3.3-LiveCheck: [governance/PHASE_3_3_LIVE_PROVIDER_CHECK_REVIEW.md](../../../governance/PHASE_3_3_LIVE_PROVIDER_CHECK_REVIEW.md)
- Phase 3.3.1 review: [governance/PHASE_3_3_1_FREEZE_REAL_PROVIDER_V0_3_REVIEW.md](../../../governance/PHASE_3_3_1_FREEZE_REAL_PROVIDER_V0_3_REVIEW.md)
- Frozen spec (unchanged): `agent-builder-kit/templates/review-assistant-agent/`

**Status:** FROZEN_WITH_NOTES — **v0.3** (2026-05-26)
