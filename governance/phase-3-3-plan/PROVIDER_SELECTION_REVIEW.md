# Provider Selection Review

**Phase 3.3-Plan** — comparison only. **No final provider chosen in plan phase.**

---

## Options

### Option A — OpenAI-compatible local endpoint

**Examples:** LM Studio, Ollama (OpenAI-compatible), llama.cpp server, vLLM

| Aspect | Assessment |
|--------|------------|
| Pros | Local/control; privacy-friendly default; no cloud egress; useful for lab and future RU/local ops |
| Cons | Setup burden; model quality varies; endpoint must be running; still needs timeout/auth policy |
| Privacy | Strongest for first live test |
| Complexity | Medium (local ops) |

---

### Option B — OpenAI cloud

| Aspect | Assessment |
|--------|------------|
| Pros | Reliable API; strong models; well-documented structured output patterns |
| Cons | Data leaves machine; API key handling; cost; policy/compliance review |
| Privacy | Weaker — cloud egress |
| Complexity | Low API integration; high governance |

---

### Option C — Russian cloud provider

**Examples:** GigaChat, YandexGPT, Bitrix VibeCode, NeuralDeep Hub

| Aspect | Assessment |
|--------|------------|
| Pros | RU market fit; business relevance; RU-language models |
| Cons | API differences; support must be verified per provider; docs may change; lock-in; legal/security review |
| Privacy | Provider-specific — must verify data policy |
| Complexity | Medium–high; Hermes RU fork shows custom URL routing pattern (research only) |

**Honesty:** NeuralDeep/Bitrix seen in Hermes RU fork code; GigaChat/YandexGPT **planned/claimed** there — not verified for Agent-OS.

---

### Option D — No real provider yet (status quo)

| Aspect | Assessment |
|--------|------------|
| Pros | Maximum safety; no secrets; no cost; no external risk; v0.2 frozen |
| Cons | Cannot observe live LLM behavior |
| Privacy | Perfect |
| Complexity | Zero |

---

## Comparison table

| Provider Option | Value | Risk | Complexity | Privacy | Recommendation |
|-----------------|-------|------|------------|---------|----------------|
| A — Local OpenAI-compatible | Controlled live test; teaches endpoint policy | Local misconfig; open port | Medium | **High** | **Strong candidate for first real impl** after approval |
| B — OpenAI cloud | Production-like reliability | Data egress; cost; keys | Low–Med | Low | Candidate if local unsuitable; extra compliance |
| C — RU cloud | Market alignment | Unverified APIs; lock-in | Med–High | Variable | **Defer** until global boundary proven + RU research |
| D — Mock only (now) | Safe baseline | No live learning | Zero | High | **Current default** — v0.2 |

---

## Recommendation (plan phase)

1. **Plan** for one provider boundary abstraction — **not** a multi-provider framework.
2. **Do not select final provider** until implementation approval message.
3. **Preferred first-live-test direction (non-binding):** Option A (local OpenAI-compatible) for privacy and control — subject to user approval at impl time.
4. Option B acceptable if explicit cloud approval + data class sign-off.
5. Option C → [RU_PROVIDER_FUTURE_BACKLOG.md](RU_PROVIDER_FUTURE_BACKLOG.md) only.

---

## Decision deferral rule

Provider selection requires at implementation time:

- Data class approval
- Secret handling approval
- Security checklist complete
- Explicit provider name in change proposal
