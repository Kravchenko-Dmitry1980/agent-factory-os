# Phase 3.2-Plan — Next Capability Decision

**Status:** Planning only — **no implementation**, **no code**, **no API calls**.

---

## What Phase 3.2-Plan is

A governance decision phase that compares two possible next steps after **Review Assistant Thin v0.1** (frozen + hardened):

| Option | Description |
|--------|-------------|
| **A** | LLM adapter boundary for Review Assistant (mock-first) |
| **B** | Second text-only agent template |

This phase **chooses** the safer next step and documents plans — it does **not** build either option.

---

## Why it exists

Review Assistant Thin v0.1 proves frozen spec implementability with simulated draft/critic. The repository must decide **one** controlled next capability without drifting into factory, runtime, or template proliferation.

---

## What options are compared

- [OPTION_A_LLM_ADAPTER_PLAN.md](OPTION_A_LLM_ADAPTER_PLAN.md) — controlled LLM boundary
- [OPTION_B_SECOND_TEMPLATE_REVIEW.md](OPTION_B_SECOND_TEMPLATE_REVIEW.md) — second agent template candidates
- [OPTION_COMPARISON_MATRIX.md](OPTION_COMPARISON_MATRIX.md) — side-by-side criteria

---

## Why no implementation is created

Phase 3.2-Plan is **decision + design docs only**. Implementation requires:

- Explicit user approval for LLM adapter (see [PRECONDITIONS_FOR_3_2_IMPLEMENTATION.md](PRECONDITIONS_FOR_3_2_IMPLEMENTATION.md))
- Separate Phase 3.2-Impl prompt
- Mock-first; no external API by default

---

## Reading order

1. [PHASE_3_2_NEXT_CAPABILITY_DECISION.md](PHASE_3_2_NEXT_CAPABILITY_DECISION.md)
2. [OPTION_COMPARISON_MATRIX.md](OPTION_COMPARISON_MATRIX.md)
3. [RECOMMENDED_NEXT_STEP.md](RECOMMENDED_NEXT_STEP.md)
4. [OPTION_A_LLM_ADAPTER_PLAN.md](OPTION_A_LLM_ADAPTER_PLAN.md)
5. [LLM_BOUNDARY_CONTRACT.md](LLM_BOUNDARY_CONTRACT.md)
6. [FINAL_PHASE_3_2_PLAN_REPORT.md](FINAL_PHASE_3_2_PLAN_REPORT.md)

Supporting: LLM failure/trace/eval/security docs, second-template risk review, diagrams.

---

## Decision this phase must produce

**Recommended:** Plan **Option A — LLM Adapter Boundary** (mock-first) before any second template.

**Verdict for next implementation planning:** [CONDITIONAL_GO_FOR_LLM_ADAPTER_PLAN](FINAL_PHASE_3_2_PLAN_REPORT.md) — not GO for code yet.

---

## Current baseline (unchanged)

| Check | Status |
|-------|--------|
| Review Assistant thin | PASS=5 FAIL=0 |
| Phase 2 smoke | PASS=12 FAIL=0 |
| Phase 2 trace | PASS=6 FAIL=0 |
| Impl | frozen v0.1 |
| Runtime / factory | none |

---

## Related docs

| Phase | Path |
|-------|------|
| 3.1.1 freeze | [PHASE_3_1_1_FREEZE_HARDEN_REVIEW.md](../PHASE_3_1_1_FREEZE_HARDEN_REVIEW.md) |
| Thin impl | [prototypes-derived/review-assistant-thin/](../../prototypes-derived/review-assistant-thin/) |
| Frozen spec | [agent-builder-kit/templates/review-assistant-agent/](../../agent-builder-kit/templates/review-assistant-agent/) |
