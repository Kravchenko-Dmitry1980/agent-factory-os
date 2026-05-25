---
classification: operational-guidance
source_tier: operational-playbook
promotion_status: unreviewed
canonical_status: non-canonical
origin: swarm-playbooks
---

# Corpus Positioning

## This corpus IS

| Property | Description |
|----------|-------------|
| **Operational** | Patterns for running multi-agent workflows day-to-day |
| **Instructional** | Derived from beginner/intermediate playbooks |
| **Implementation-oriented** | Queue, review UI, budget fields, HITL gates |
| **Isolated** | Lives only under `Books/swarm-playbooks/` |
| **Non-canonical** | `canonical_status: non-canonical` on all extracts |
| **Promotion-pending** | Candidates listed in `review/promotion-candidates.md` — **no auto-promote** |

## This corpus IS NOT

| Property | Why |
|----------|-----|
| **Canonical architecture** | No contracts, trace model, or control plane spec |
| **Governance layer** | Does not modify or replace `governance/` |
| **Production reference architecture** | Missing idempotency, RBAC, verification, DR |
| **Agent-OS curated layer** | Does not modify `agent-os/` |
| **Research-grade theory** | Prompt tutorials ≠ formal ontology |
| **Runtime code** | No implementation in this phase |

## Relationship to Agent-OS

```
Books/swarm-playbooks/     ──(future gated promotion)──▶  agent-os/
        │                                              governance/
        │ operational wisdom                           canonical patterns
        ▼
   source/ (immutable tutorials)
```

Agent-OS is **stronger** in:

- governance and promotion pipeline
- provenance and semantic graph
- anti-patterns with architectural rigor
- taxonomy discipline
- verification-before-writeback
- fail-closed defaults

Swarm playbooks are **stronger** in:

- step-by-step operational onboarding
- concrete HITL UX (review page, plan approval)
- beginner-accessible lifecycle narrative
- queue + critic + budget **as ops patterns**

## Contamination Policy

**Forbidden without explicit promotion review:**

- Copying patterns into `agent-os/` verbatim
- Treating «8-agent swarm» as recommended topology in governance docs
- Elevating critic to verification in canonical layer
- Using CLAUDE.md pattern as memory governance

## Reader Guidance

1. Operators building first agent system → start with lifecycle + HITL + progressive autonomy
2. Architects designing production platform → read anti-patterns + critique limitations first
3. Governance reviewers → use `review/promotion-candidates.md` only

## Phase Tag

**SWARM-EXTRACTION** — operational knowledge isolation and refinement.
