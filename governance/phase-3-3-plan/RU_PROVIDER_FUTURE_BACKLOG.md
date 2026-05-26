# RU Provider Future Backlog

**Phase 3.3-Plan** — research backlog only. **No RU integration now.**

Hermes Desktop RU fork findings are **research-only** (Phase 3.2.2).

---

## Provider table

| Provider | Why Interesting | What Must Be Verified | Risks | Status |
|----------|-----------------|----------------------|-------|--------|
| **GigaChat** | Sber ecosystem; RU language; enterprise familiarity | API availability, auth model, data policy, pricing, structured output | Cloud egress; compliance; lock-in | **Planned/claimed** in Hermes RU README — **not verified** for Agent-OS |
| **YandexGPT** | Yandex Cloud; RU market | API docs, keys, rate limits, retention policy | Same as cloud | **Planned/claimed** in Hermes RU README — **not in fork code** |
| **Bitrix VibeCode** | OpenAI-compatible `vibecode.bitrix24.tech`; BitrixGPT | API key flow, OAuth (fork: **not implemented**), terms of use | Portal scope; incomplete OAuth scaffolding | **In Hermes RU fork code** — research only |
| **NeuralDeep Hub** | RU OSS aggregator; `api.neuraldeep.ru/v1` | Hub trust, key issuance, Bitrix exchange endpoint (fork: **TBD**) | Third-party hub; endpoint not built for OAuth swap | **In Hermes RU fork code** — research only |

---

## Sequencing

1. Global single provider boundary (Phase 3.3 impl — non-RU likely first)
2. Freeze v0.3 with mock + one real provider
3. RU provider **comparison markdown** (no calls)
4. Individual RU provider approval phases — each separate

---

## No claims rule

Do not state "GigaChat supported" or "YandexGPT integrated" unless verified in our impl with passing eval.

Mark README/marketing claims as **planned/claimed** until then.

---

## Agent-OS RU UX without RU provider

- `curriculum/ru/` continues
- Future Operator Console RU mode (Phase 4+ plan)
- Provider docs in Russian when impl approved

---

## References

- [../phase-3-2-2/RU_PROVIDER_DIRECTION_REVIEW.md](../phase-3-2-2/RU_PROVIDER_DIRECTION_REVIEW.md)
- `external-repos-triage/hermes-desktop-delta/ru-product/russian-provider-backlog.md`

---

## Decision

**No RU provider integration in Phase 3.3-Plan or impl without explicit per-provider approval.**
