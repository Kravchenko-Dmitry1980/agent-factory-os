# Reference Architecture Prototypes (Phase 2.0)

**Status:** Educational reference implementations — not production systems.

---

## Why These Prototypes Exist

The repository stabilizes architecture through **doctrine**, **governance**, and **curated knowledge** (`agent-os/`). Phase 2.0 adds **bounded executable sketches** that make abstract principles **testable in under 30 minutes**.

Each prototype answers one question:

> Can we implement this governance principle in ~200 lines without building a platform?

If yes — the principle is teachable. If no — the doctrine may be underspecified or over-scoped.

---

## Why They Are Intentionally Small

| Property | Rationale |
|----------|-----------|
| **Tiny** | Readable in one sitting; no hidden framework magic |
| **Bounded** | Fixed inputs, fixed state, no distributed assumptions |
| **Failure-aware** | `failure-modes.md` is mandatory, not optional |
| **Governance-aware** | Fail-closed, verification, escalation are first-class |
| **No platform drift** | Forbidden: orchestration runtimes, agent swarms, vector infra |

Production complexity is **forbidden** here because it obscures the lesson. A LangGraph monster teaches framework APIs, not governance.

---

## What They Validate

| Prototype | Validates |
|-----------|-----------|
| [review-loop-agent](review-loop-agent/) | Critique limitations, review gates, HITL, verification-first |
| [bounded-memory-agent](bounded-memory-agent/) | Frozen snapshots, memory limits, no uncontrolled writeback |
| [queue-orchestration](queue-orchestration/) | Durable tasks, lifecycle, retry boundaries, escalation |
| [fail-closed-external-action](fail-closed-external-action/) | Approval-before-action, deny-by-default, audit |
| [gui-verification-loop](gui-verification-loop/) | Visual verification, A/B/C taxonomy, unverified-click prevention |
| [promotion-pipeline-simulator](promotion-pipeline-simulator/) | Promotion gates, provenance, governance workflow |

Shared rules: [governance/](governance/)  
Diagrams: [diagrams/](diagrams/)

---

## Connection to Doctrine Layer

```
agent-os/doctrine/     → worldview (what we believe)
agent-os/08_patterns/  → curated patterns (what we teach)
governance/            → promotion & audit policy (what we allow)
prototypes/            → executable sketches (what we can demonstrate)
```

Prototypes **do not** extend `agent-os/` taxonomy. They **reference** it:

- [[verification-before-writeback]] → `bounded-memory-agent`, `review-loop-agent`
- [[fail-closed-defaults]] → all prototypes
- [[frozen-memory-snapshot]] → `bounded-memory-agent`
- [[visual-verification]] → `gui-verification-loop`
- `governance/PROMOTION_STRATEGY.md` → `promotion-pipeline-simulator`

Run any demo:

```powershell
python prototypes/review-loop-agent/minimal-demo.py
python prototypes/bounded-memory-agent/minimal-demo.py
python prototypes/queue-orchestration/minimal-demo.py
python prototypes/fail-closed-external-action/minimal-demo.py
python prototypes/gui-verification-loop/minimal-demo.py
python prototypes/promotion-pipeline-simulator/minimal-demo.py
```

---

## Hard Boundaries (Non-Negotiable)

**DO NOT** evolve prototypes into:

- Production platforms
- Orchestration frameworks
- Agent swarms
- RAG / vector infrastructure
- MCP runtimes
- Cloud deployments

See [governance/prototype-boundaries.md](governance/prototype-boundaries.md).

---

## Navigation

1. Read [governance/prototype-rules.md](governance/prototype-rules.md)
2. Pick one prototype README
3. Run `minimal-demo.py`
4. Read `failure-modes.md` and `contracts.md`
5. Compare with matching diagram in `diagrams/`
