# Phase 3.5.2 — Demo Runner Master Plan

**Date:** 2026-05-26  
**Status:** PLAN_ONLY

---

## Goal

Plan a **minimal future CLI demo runner** that makes Review Assistant Thin **understandable for a human operator** without changing how the agent behaves.

---

## Why now

| Before Phase 3.5.1 | After Phase 3.5.1 |
|--------------------|-------------------|
| Many governance docs | Operator ran 9 scenarios manually |
| Abstract “agent exists” | Saw DELIVERED / BLOCKED / TRACE |
| Technical CLI only | Pain point documented: raw output, no menu |

The system **works**. The **operator UX** does not.

---

## What the runner should improve

| Improvement | Detail |
|-------------|--------|
| Reduce command memorization | Fixed menu instead of `--scenario` names |
| Explain scenario meaning | Russian title + “what it proves” |
| Explain final decision | DELIVERED / BLOCKED / ESCALATED / FAILED in plain language |
| Translate trace | Key events → Russian, not full raw dump only |
| Reduce cognitive load | Structured summary block after run |
| Prepare for demos | Show stakeholders without reading governance first |

---

## What it must not do

| Forbidden | Policy doc |
|-----------|------------|
| Change agent logic | [NO_AGENT_LOGIC_CHANGE_POLICY.md](NO_AGENT_LOGIC_CHANGE_POLICY.md) |
| Become runtime / factory | [NO_RUNTIME_NO_FACTORY_POLICY.md](NO_RUNTIME_NO_FACTORY_POLICY.md) |
| Become UI platform | Out of scope |
| Call providers by default | [REAL_PROVIDER_WARNING_POLICY.md](REAL_PROVIDER_WARNING_POLICY.md) |
| Create new agent behavior | Wrapper only |
| Hide safety trace | Raw output still available; summary is additive |
| Add new scenarios | Use existing frozen scenarios only |

---

## Planned future artifact (not created in this phase)

```text
demos/review-assistant-runner/
├── demo_runner.py          # Phase 3.5.2-Impl only — stdlib, one script
├── README.md               # Impl phase
└── transcripts/            # Optional, explicit flag only
```

**`demo_runner.py` must not exist until Phase 3.5.2-Impl with explicit user approval.**

---

## Architecture (conceptual)

```text
Operator
  → demo_runner.py (menu + summary)
    → subprocess: minimal_demo.py --scenario X
    → subprocess: evaluation/scripts/check_*.py (optional menu items)
  → parse stdout (decision, delivered, TRACE lines)
  → print Russian operator summary
  → optional: save transcript (explicit flag)
```

Agent loop unchanged inside `minimal_demo.py`.

See [diagrams/demo-runner-boundary.md](diagrams/demo-runner-boundary.md).

---

## Scope summary

**In:** menu, wrapper, parse, summarize, warn on real provider, optional transcript.

**Out:** new scenarios, logic changes, UI, dependencies, runtime, factory.

Full scope: [DEMO_RUNNER_SCOPE.md](DEMO_RUNNER_SCOPE.md).

---

## Recommended path

**Option B** — one small stdlib CLI wrapper.

Detail: [RECOMMENDED_IMPLEMENTATION_PATH.md](RECOMMENDED_IMPLEMENTATION_PATH.md).

---

## Phases

| Phase | Activity |
|-------|----------|
| **3.5.2-Plan** (now) | This document package |
| **3.5.2-Impl** | One `demo_runner.py` if GO |
| **3.5.3-Plan** (later) | Interactive CLI — separate plan |

---

## Success criteria (future impl)

See [ACCEPTANCE_CRITERIA.md](ACCEPTANCE_CRITERIA.md), [EVALUATION_PLAN.md](EVALUATION_PLAN.md).

---

## Related

- Hands-on report: [demos/review-assistant-hands-on/](../../demos/review-assistant-hands-on/)
- Thin demo: `prototypes-derived/review-assistant-thin/minimal_demo.py` (unchanged)
- GO/NO-GO: [PHASE_3_5_2_GO_NO_GO.md](PHASE_3_5_2_GO_NO_GO.md)
