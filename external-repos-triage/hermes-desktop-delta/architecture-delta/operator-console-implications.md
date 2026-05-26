# Operator Console Implications

**Question:** Does Agent-OS need an Operator Console later?

**Answer:** **Yes, later** — not now, not Phase 3.3.

---

## Why markdown/tree is enough for builders

- Agent Builder Kit specs live in git
- Review Assistant Thin proves template → impl → eval → freeze
- Developers can navigate governance and traces in repo

---

## Why operators still need GUI eventually

| Need | CLI/Markdown gap |
|------|------------------|
| Non-technical reviewers | Cannot read `minimal_demo.py` traces comfortably |
| Approval queues | Human approval is abstract in stdout |
| Trace inspection | Long SSE/event logs need structured viewer |
| Provider config | Keys and endpoints are error-prone in YAML/env |
| Skill/tool review | Enable/disable needs visible boundary |
| Freeze/eval status | Governance state should be visible at a glance |

Hermes Desktop proves **demand for GUI operator layer** — but implements it as full autonomy platform, not governance-first console.

---

## Operator Console is NOT Phase 3.3

Phase 3.3 = **Real LLM Provider Boundary Plan** (single provider, gated, no framework).

---

## Preconditions before Operator Console

1. Real provider boundary safely handled (post-mock, with eval + freeze)
2. More stable evaluation harness (dashboard needs real data)
3. At least **2–3 agent templates** with frozen impls
4. Clear provider governance (secrets, timeout, failure modes)
5. Approval queue becomes painful in markdown (signal to build UI)

Estimated phase: **4+** (concept/plan earlier; implementation much later).

---

## What Hermes teaches

Build **read-mostly console** first:

- templates, implementations, eval runs, traces, approvals, freeze records

Defer **write/autonomy surfaces**:

- schedules, gateways, skill install, remote mode

---

## Agent-OS differentiation

Our console must show **governance state** Hermes hides:

- freeze version, change lock, safety gates, rollback target
- explicit "LLM output ≠ truth" warnings
- no auto-publish, no hidden tool execution
