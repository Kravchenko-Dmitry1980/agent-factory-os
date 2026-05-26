# Provider Mode Policy — Free-Form CLI

**Date:** 2026-05-26  
**Status:** PLAN_ONLY

Aligned with Demo Runner v0.1 and review-assistant-thin-v0.3 provider boundary.

---

## Default

**No provider call.**

Mode 1 (safe mock/default) is default. No network on startup.

---

## Allowed future modes

### Mode 1 — Safe mock/default

| Property | Value |
|----------|-------|
| Network | no |
| Default | **yes** |
| First impl | **required** |
| Risk | lowest |

### Mode 2 — Local provider explicit

| Property | Value |
|----------|-------|
| Target | LM Studio / Ollama local OpenAI-compatible |
| Network | yes, operator-chosen only |
| Requires | explicit mode selection + `yes` confirmation + `RA_LLM_BASE_URL` |
| Input | synthetic/non-sensitive only |
| Cloud | **forbidden** |

---

## Forbidden

| Item | Reason |
|------|--------|
| Cloud OpenAI | Out of lab boundary |
| GigaChat / YandexGPT | Not in this phase |
| Provider by default | Safety |
| Hidden provider call | Operator deception |
| Provider fallback chain | Framework drift |
| Provider framework / router | Out of scope |
| Auto-switch mock → provider | Hidden escalation |

---

## Mode 2 confirmation (plan)

Same spirit as Demo Runner item 9:

```text
ВНИМАНИЕ: режим вызывает локальный OpenAI-compatible endpoint.
Проверьте LM Studio/Ollama, RA_LLM_BASE_URL, synthetic data only.
Продолжить? yes/no:
```

Missing env → abort, no call.

---

## Implementation note

Free-form CLI may **reuse patterns** from thin demo provider boundary but must not modify `minimal_demo.py` without separate agent phase.

Impl may:

- Inline minimal mock path in free_form_cli.py (preferred for isolation), or
- Subprocess to thin demo only if task mapping exists (higher coupling — avoid in v1)

See [RECOMMENDED_IMPLEMENTATION_PATH.md](RECOMMENDED_IMPLEMENTATION_PATH.md).

---

## Diagram

[diagrams/provider-mode-boundary.md](diagrams/provider-mode-boundary.md)
