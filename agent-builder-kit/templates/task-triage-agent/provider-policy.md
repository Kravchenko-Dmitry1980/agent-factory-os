# Task Triage Agent — Provider Policy

**Status:** SPEC_DRAFT

---

## Default

**No provider calls.**

Task Triage Agent specs do **not** require an LLM provider. Classification in a future thin implementation may use deterministic rules first — same discipline as Review Assistant mock-first path.

---

## Why no provider by default

| Reason | Detail |
|--------|--------|
| Scope control | Provider adds cost, drift, injection surface |
| Specs-first | Template defines behavior before any model |
| Fail-closed | Rules-based classification is auditable |
| Baseline safety | Review Assistant chain: mock → local → harness |

---

## If provider is considered later

Requires **separate governance phase** with:

| Requirement | Detail |
|-------------|--------|
| Explicit phase approval | Not part of v0.1 specs |
| Mock first | Deterministic classifier before any LLM |
| Local provider first | LM Studio / OpenAI-compatible local only |
| Synthetic data only | No client PII, no secrets in eval |
| Provider output not truth | Classification must pass safety gates |
| No provider framework | Thin boundary only — mirror Review Assistant |
| Provider safety harness | Separate eval phase after thin impl |

---

## Forbidden in this template

| Forbidden | Reason |
|-----------|--------|
| OpenAI cloud by default | Out of Phase 3 scope |
| GigaChat / YandexGPT integration | Out of Phase 3 scope |
| Provider router | Orchestrator/factory drift |
| Model selection UI | Out of scope |
| Provider fallback chains | Hidden complexity |
| Hidden network call | Policy violation |
| Provider output as authoritative decision | Fail-closed violation |

---

## Task input triggers

| Pattern | Response |
|---------|----------|
| "call OpenAI API" | REJECT_UNSAFE + provider policy |
| "enable LM Studio by default" | ESCALATE + approval_required |
| "use cloud model for triage" | ESCALATE, missing provider policy |
| "provider classifies everything" | Anti-pattern — see [anti-patterns.md](anti-patterns.md) |

---

## Trace rules

Default path: **no provider trace events**.

If future provider phase approved, optional event: `provider_request_prepared` — never `provider_called` in v0.1 spec.

See [expected-traces.md](expected-traces.md).

---

## Relation to Review Assistant provider chain

Review Assistant: mock LLM v0.2 → real local provider v0.3 → provider safety harness v0.1.

Task Triage: **no provider in specs**. Future provider path must not break Review Assistant baselines.
