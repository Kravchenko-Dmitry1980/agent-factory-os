# Prototype to Factory Gap Analysis

**Principle:** patterns migrate; **code does not** copy into a factory runtime.

| Current asset | Can become | Gap | Risk | Recommendation |
|---------------|------------|-----|------|----------------|
| review-loop-agent | Review Assistant Agent Template | Spec fields, event names | Becomes «one script platform» | MD spec + link to demo |
| fail-closed-external-action | Safety Gate Template | Policy matrix per action type | Over-generalized gate | Keep action-class table in spec |
| bounded-memory-agent | Memory Boundary Template | Per-agent limits | Unlimited context in kit | Copy limits philosophy only |
| queue-orchestration | Workflow Step Template (later) | Retry/escalation params | Retry storm | v0.2 not v0.1 |
| gui-verification-loop | GUI Verify Template (later) | Real screen capture | CV confusion | Defer |
| promotion-pipeline-simulator | Promotion Gate Template (later) | Real git hooks | Auto-promote | Advanced |
| review-queue-workflow | Multi-step Review Template | Composition docs | Framework | Second template cycle |
| escalation-workflow | Triage Template (Option B) | Priority rules | Swarm routing | After Review Assistant |
| llm-verification-adapter | LLM Verify Contract | Schema + verify step | Trust LLM JSON | Section in safety template |
| filesystem-audit-log | Audit Contract Template | Central log service | Platform | Event list in trace template |
| evaluation/scripts | Template Acceptance Checklist | Per-template smoke lines | Weak smoke | Extend checklist not scripts in 3.0 |
| observability/examples | Template Trace Standard | Generator tool | Fake traces | Copy event vocabulary |
| operator-playbooks | Builder Operator Guide | Kit-specific paths | Duplicate maintain | Cross-link, don’t fork |
| prototypes/shared/gates.py | **Should NOT become** kit runtime | Extraction pressure | **Critical drift** | Document anti-pattern |
| curriculum/ru | RU Builder Study Path | Kit docs EN-only | RU friction | Bilingual kit specs |

---

## Factory capabilities NOT in prototypes

| Capability | Gap size |
|------------|----------|
| Agent registry | Large |
| Template versioning | Medium |
| Generated project scaffold | Large (needs user approval) |
| Multi-tenant ops | Out of scope |
| Continuous production eval | Out of scope |

---

## Minimum bridge for Phase 3.0

One MD spec chain:

**Review Assistant Template** → maps 1:1 to review-loop events → validated by existing smoke lines 1–2.

No new factory code required for bridge.
