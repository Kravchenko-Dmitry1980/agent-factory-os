# Agent Builder Kit v0.1

**Specification kit for designing safe AI agent templates.**

---

## What this is

Agent Builder Kit v0.1 is a **Markdown-only specification layer** for designing future AI agent templates. It defines:

- what every agent template must contain
- required safety gates
- workflow patterns
- memory boundaries
- human approval rules
- evaluation checklists
- trace templates
- anti-pattern guards
- one reference template: **Review Assistant Agent**

This kit helps teams describe agents **before** any runtime or code exists.

---

## What this is NOT

| Not this | Why |
|----------|-----|
| Runtime | No executable agent loop |
| Generator | No auto-scaffolding of files |
| Factory | No registry, ops, or production deploy |
| Production platform | Lab is Learning Lab, not SaaS |
| Digital twin builder | Out of Phase 3.0 scope |
| CV builder | Out of Phase 3.0 scope |
| RAG platform | Frozen in Phase 3 |
| MCP runtime | Frozen in Phase 3 |
| Autonomous agent system | Governance-before-autonomy |

See [governance/no-runtime-policy.md](governance/no-runtime-policy.md) and [PHASE_3_WARNING_RU.md](../PHASE_3_WARNING_RU.md).

---

## Why it exists

Phase 2 delivered prototypes, observability, evaluation, and governance. Phase 3.0 adds the **design kit** so future agents are:

- verification-first
- fail-closed by default
- human-in-the-loop for risky outputs
- evaluable before implementation
- traceable and auditable

---

## First supported template

**[Review Assistant Agent](templates/review-assistant-agent/README.md)** — drafts content and prepares it for human review. Does **not** auto-publish.

**Freeze (2026-05-26):** v0.1 **FROZEN_WITH_NOTES** — [sign-off bundle](templates/review-assistant-agent/sign-off/README.md) · [governance review](../governance/PHASE_3_0_FREEZE_REVIEW_ASSISTANT.md)

**Phase 3.1 plan (no code yet):** [governance/phase-3-1-plan/](../governance/phase-3-1-plan/README.md)

**Phase 3.1 implementation:** [prototypes-derived/review-assistant-thin/](../prototypes-derived/review-assistant-thin/README.md) · [review](../governance/PHASE_3_1_REVIEW_ASSISTANT_THIN_REVIEW.md) · **frozen v0.1** · [3.1.1 harden](../governance/PHASE_3_1_1_FREEZE_HARDEN_REVIEW.md)

---

## How to use

1. Read [RU_SUMMARY.md](RU_SUMMARY.md) (Russian) or this README (English).
2. Open [template-specs/agent-template-spec.md](template-specs/agent-template-spec.md).
3. Review [safety-gates/](safety-gates/README.md).
4. Study [templates/review-assistant-agent/](templates/review-assistant-agent/README.md).
5. Check [evaluation-checklists/](evaluation-checklists/README.md).
6. Review [diagrams/builder-kit-map.md](diagrams/builder-kit-map.md).
7. **Do not implement code** without explicit user approval.

---

## Structure

```
agent-builder-kit/
├── template-specs/       # What every template must define
├── safety-gates/         # Gate definitions
├── evaluation-checklists/
├── trace-templates/
├── template-governance/
├── templates/            # Reference agent templates
├── diagrams/
└── governance/           # Kit boundary policies
```

---

## Related repository docs

| Area | Path |
|------|------|
| Prototypes | `prototypes/review-loop-agent/` |
| Evaluation | `evaluation/scenarios/`, `evaluation/quality-gates/` |
| Observability | `observability/event-taxonomy/` |
| Evolution | `evolution/change-proposals/` |
| Phase 3 gate | `governance/PHASE_3_START_CONDITIONS.md` |
| External repos (research only) | `governance/phase-2-10/` |

---

## Version

**v0.1** — specs, templates, checklists only. No runtime. No factory.
