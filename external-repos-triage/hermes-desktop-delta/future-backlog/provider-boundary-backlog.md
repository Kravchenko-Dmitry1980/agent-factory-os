# Provider Boundary Backlog

Aligned with review-assistant-thin-v0.2 and Phase 3.3 plan direction.

---

## Done

- [x] Mock provider boundary (v0.2 frozen)
- [x] 5 LLM mock scenarios + check script

---

## Soon (Phase 3.3)

- [ ] Real LLM Provider Boundary **Plan** (no framework)
- [ ] Provider safety checklist (from Hermes security notes)
- [ ] Secret handling policy doc
- [ ] Timeout/error/failure mode spec for real calls

---

## Later

- [ ] Single real provider impl + freeze (explicit approval)
- [ ] Provider health check (connectivity, not quality score)
- [ ] RU provider comparison research (GigaChat, YandexGPT, NeuralDeep, Bitrix)
- [ ] OpenAI-compatible local endpoint eval (Ollama/LM Studio) — optional

---

## Much later

- [ ] Second approved provider (separate phase)
- [ ] Provider config spec (markdown, not Electron)
- [ ] Operator Console provider panel

---

## Explicit rule

**No provider framework until multiple providers individually approved**, each with:

- security review
- eval + trace baselines
- freeze record
- rollback plan

Hermes `provider-registry.ts` is **anti-pattern for Phase 3** — reference only.
