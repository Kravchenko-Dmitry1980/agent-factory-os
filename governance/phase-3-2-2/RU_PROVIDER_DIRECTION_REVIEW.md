# RU Provider Direction Review

**Phase:** 3.2.2  
**Date:** 2026-05-26

---

## Why Russian providers matter

- RU learners/operators may require local endpoints for latency, billing, or policy expectations
- RU fork demonstrates market demand for NeuralDeep, Bitrix, planned GigaChat/YandexGPT
- Agent-OS RU curriculum needs aligned **future** provider story — not silent English-only assumption

---

## Possible providers (research status)

| Provider | Fork status | Our status |
|----------|-------------|------------|
| **GigaChat** | README planned only | Research backlog |
| **YandexGPT** | README planned only | Research backlog |
| **Bitrix VibeCode** | Implemented (custom URL + API key) | Research backlog; OAuth **not implemented** in fork |
| **NeuralDeep Hub** | Implemented (custom URL + API key) | Research backlog |

**Honesty:** Only NeuralDeep and Bitrix VibeCode found in RU fork source. GigaChat/YandexGPT are **claimed/planned**, not verified in code.

---

## Current decision

# No provider integration now.

Includes: no GigaChat, YandexGPT, NeuralDeep, Bitrix calls; no keys; no adapter code.

Stable baseline remains **review-assistant-thin-v0.2 mock LLM**.

---

## Future requirement (any provider)

Every provider must pass:

1. Security review
2. Data policy / residency review
3. Timeout and error handling
4. Evaluation scenarios (incl. failure modes)
5. Trace baselines
6. Human approval gate alignment
7. Cost and logging review
8. Change proposal + explicit approval
9. Freeze record + rollback plan

---

## RU vs global sequencing

1. First: single **global** real provider boundary (Phase 3.3 plan)
2. Then: RU provider **comparison research** (markdown)
3. Then: optional second provider if governance allows
4. Never: multi-provider framework from Hermes registry pattern

---

## RU UX without RU provider

Supported now:

- `curriculum/ru/`
- Russian governance summaries (where exist)
- Future console RU-first mode (requirements doc only)

Not supported now:

- Live RU provider switching
- Bitrix OAuth login
- NeuralDeep default models

---

## Decision

**Defer all RU provider integration.** Document in backlog. Revisit after Phase 3.3 provider boundary plan approved.
