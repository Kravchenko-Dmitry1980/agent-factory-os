# No Provider Framework Policy

**Phase 3.3-Plan** — strict prohibition.

---

## Forbidden in Phase 3.3 and until explicit future governance

| Pattern | Example (reject) |
|---------|------------------|
| Provider registry | `PROVIDERS = { "openai": ..., "anthropic": ... }` with plugin registration |
| Provider router | `select_provider(task)` auto-routing |
| Fallback chain | OpenAI fails → try Anthropic |
| Model marketplace | UI list of 200 models |
| Abstract `Provider` interface + N impls | `class OpenAIProvider(Provider)` + registry |
| Provider auto-selection | "Best model for task" |
| Default cloud provider | Real call without flag |
| Provider UI / wizard | Electron settings screen |
| Provider config wizard | Multi-step install like Hermes |
| Credential pools | Multiple keys per provider |
| OAuth subscription flows | Deferred indefinitely |

---

## Why

1. v0.2 freeze: mock only — framework is scope explosion
2. Hermes Desktop triage: registry/router = drift signal
3. Phase 3.2-plan: single adapter, no plugins
4. Security: each provider needs individual approval — framework hides this
5. Evaluation: cannot freeze what switches underneath

---

## Allowed (future impl only)

| Pattern | Constraint |
|---------|------------|
| One provider boundary module | Single file or small functions |
| `mock` default | Zero network |
| `real` behind explicit flag | Opt-in per run |
| One env var for one provider | No pool |
| No automatic fallback | Fail closed |

---

## Code review red flags (future)

- New directory `providers/` with multiple adapters
- `import openai` + `import anthropic` in same module
- Factory function `create_provider(name)`
- Config file listing multiple active providers
- Auto-discovery of endpoints

---

## Counter-reference

Hermes `provider-registry.ts` — **study only**, do not copy.

---

## Extension rule

Second provider = **new phase**, new security review, new eval, new freeze — not a registry entry.

---

## Plan phase compliance

No framework code created. This document is normative for future impl review.
