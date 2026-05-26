# Provider Management Map

Hermes Desktop provider architecture vs Agent-OS constraints.

---

## What Hermes implements

| Layer | Detail |
|-------|--------|
| Built-in providers | OpenRouter, Anthropic, OpenAI, Gemini, Groq, HF, … |
| Local/custom | OpenAI-compatible (Ollama, LM Studio, vLLM, llama.cpp) |
| Registry | `provider-registry.ts` — canonical base URLs |
| Credential pools | Multiple keys per provider |
| OAuth flows | Codex, xAI, Qwen, Gemini, MiniMax subscriptions |
| Remote mode | Desktop → remote Hermes API + key |
| RU fork extras | NeuralDeep, Bitrix VibeCode via custom URL + env keys |

Config stored in `~/.hermes/.env`, `config.yaml`.

---

## Implications for Agent-OS

| Topic | Lesson |
|-------|--------|
| Local providers | Same OpenAI-compatible pattern we may use in Phase 3.3+ |
| Cloud providers | Need secrets policy, never in repo |
| OpenAI-compatible endpoints | Good **boundary** pattern; bad as **framework** now |
| Russian providers | Custom URL routing (RU fork) — plan-only for us |
| Model selection | UI temptation — defer until single provider proven |
| Provider failures | Need timeout, escalation, no fallback hallucination (already in v0.2 mock) |
| Provider policy | One approved provider at a time initially |

---

## Non-negotiable conclusion

**Provider framework is still NOT allowed now.**

Allowed:

- Phase 3.3 **plan** for single real provider boundary
- Mock boundary (frozen v0.2)
- Security checklist derived from Hermes UX mistakes

Forbidden now:

- Multi-provider registry
- Provider switcher UI
- Credential pools
- OAuth wizard
- GigaChat/YandexGPT/NeuralDeep integration

---

## RU provider note

RU fork implements NeuralDeep + Bitrix as **custom endpoints**. GigaChat/YandexGPT are **README-planned only** — do not assume availability.

---

## Future sequence

1. Mock boundary (done — v0.2)
2. Single real provider boundary + freeze
3. Provider config **spec** (not Electron UI)
4. Second provider only after eval + security review
5. Operator Console provider panel (MUCH_LATER)
