# Repository Review: hermes-desktop-ru

## Basic Info

| Field | Value |
|-------|-------|
| **URL** | https://github.com/vakovalskii/hermes-desktop-ru |
| **Local path** | `external-repos-triage/source/hermes-desktop-ru/` |
| **Commit inspected** | `2bbe940` (2026-05-26) |
| **Package version** | 0.5.1 (same as upstream) |
| **Main purpose** | RU-first fork of Hermes Desktop |
| **Main stack** | Same as upstream (Electron/React/TS) |
| **License** | MIT (upstream preserved) |
| **Relation to upstream** | Fork of fathah/hermes-desktop; author vakovalskii |
| **Maturity signal** | Active; smaller community; tracks upstream closely |

---

## RU-Specific Changes (verified in source)

| Change | Status |
|--------|--------|
| Russian UI locale (`src/shared/i18n/locales/ru/`) | **Implemented** |
| RU language option in Settings (`ru: "Русский"`) | **Implemented** |
| NeuralDeep Hub default models | **Implemented** — `api.neuraldeep.ru/v1`, `NEURALDEEP_API_KEY` |
| Bitrix VibeCode default models | **Implemented** — `vibecode.bitrix24.tech/v1`, `BITRIX_VIBECODE_API_KEY` |
| Provider detect for neuraldeep/vibecode URLs | **Implemented** |
| Bitrix OAuth login scaffolding | **Not implemented** — `startBitrixLogin` throws |
| Hub Bitrix→NeuralDeep key exchange | **Not implemented** — endpoint TBD |
| GigaChat | **Planned only** — README mention, no code found |
| YandexGPT | **Planned only** — README mention, no code found |

---

## What It Is

Same Hermes Desktop operator shell with **RU localization** and **RU-market provider presets** routed through OpenAI-compatible custom endpoints.

---

## What It Is Not

- Not verified production integration with GigaChat/YandexGPT
- Not Agent-OS RU curriculum replacement
- Not approved provider for our project
- Not a fork we adopt or run

---

## RU-First Value

| Area | Lesson |
|------|--------|
| Russian language UX | Full-screen i18n per module (chat, providers, schedules, …) |
| Russian defaults | Default model list includes NeuralDeep + Bitrix VibeCode |
| Local market adaptation | OpenAI-compatible RU endpoints without waiting for upstream |
| Onboarding for RU users | Provider names/descriptions in Russian (`providers.ts`) |

Aligns with why `curriculum/ru/` exists — **learners and operators need RU entry points**.

---

## Useful Ideas for Agent-OS RU

- RU-first Operator Console mode (interface + docs links)
- Explicit labeling: **implemented vs planned** providers
- RU provider comparison as **future research doc**, not live switcher
- Bitrix OAuth as example of **enterprise portal auth complexity** (defer)

---

## Provider Strategy Implications

- RU market expects **local/alternative endpoints** (NeuralDeep, Bitrix, future GigaChat/Yandex)
- Fork uses **custom endpoint + env key** pattern — not native hermes-agent provider ids
- OAuth/portal flows (Bitrix) need separate security review
- **No integration now** — only backlog entries with honesty flags

---

## Dangerous Ideas

- Assuming README "planned" providers are ready
- Fork staleness vs upstream security fixes
- Writing API keys to `.env` from OAuth flows (scaffolding exists)
- Marketing RU fork as "compliant" without data policy review
- Skill/gateway parity with upstream — same autonomy risks

---

## What We Can Learn

- RU fork pattern: **locale + provider presets + detect URLs** — minimal delta
- Planned providers must be marked **claimed/planned**, not implemented
- Enterprise RU integrations (Bitrix) explode auth scope

---

## What We Must Not Copy

- NeuralDeep/Bitrix keys handling without our secret policy
- Unimplemented OAuth scaffolding as "done"
- Fork as dependency of Agent-OS
- RU provider UI before governance checklist exists

---

## Decision

**STUDY_LATER / RESEARCH_ONLY**

Valuable for RU product direction and provider backlog. **Do not adopt or integrate.**
