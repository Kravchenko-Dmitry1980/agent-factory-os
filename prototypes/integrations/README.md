# Workflow Integration Sandbox (Phase 2.1)

**Status:** Composed governed workflows — not a framework.

---

## Why Integrations Exist

Phase 2.0 proved individual governance principles in isolation. Phase 2.1 asks:

> What happens when two or three principles meet in one linear workflow?

Integrations teach **workflow understanding**: where gates chain, where uncertainty propagates, where escalation must fire.

---

## Why Workflows Are Intentionally Tiny

| Property | Rationale |
|----------|-----------|
| One workflow = one lesson | No universal orchestrator |
| Linear scripts | No plugin registry |
| Per-workflow `minimal-demo.py` | No shared base class |
| Copy-paste over abstraction | Readability beats reuse |

Each workflow should be understood in **< 45 minutes**.

---

## Reusable Runtime Is Forbidden

Phase 2.1 is the **highest drift risk** in the prototype program.

If you see:

- `BaseWorkflow`, `WorkflowEngine`, `AgentRegistry`
- Plugin loading or event bus
- Growing `integrations/shared/` beyond path helpers

**STOP.** That is accidental platform creation.

Use `prototypes/shared/` (audit + gates) only. Do not grow it.

---

## Why Orchestration Complexity Is Dangerous

Real orchestration platforms hide governance gates inside framework magic. Here, every step must be **visible in one file**.

Complexity inflation symptoms:

- Generic step interfaces
- YAML-driven workflows
- "Universal" retry/escalation middleware

These teach framework APIs, not governance.

---

## Workflows

| Workflow | Composes |
|----------|----------|
| [review-queue-workflow](review-queue-workflow/) | queue + review loop + escalation + approval |
| [gui-safe-action-workflow](gui-safe-action-workflow/) | GUI verify + fail-closed + approval |
| [governed-promotion-workflow](governed-promotion-workflow/) | promotion + provenance + anti-pattern scan |
| [bounded-memory-review-workflow](bounded-memory-review-workflow/) | memory limits + critique + verified writeback |
| [escalation-workflow](escalation-workflow/) | uncertainty + retry ceiling + human escalation |

Governance: [governance/](governance/)  
Diagrams: [diagrams/](diagrams/)

---

## Run

```powershell
python prototypes/integrations/review-queue-workflow/minimal-demo.py
python prototypes/integrations/gui-safe-action-workflow/minimal-demo.py
python prototypes/integrations/governed-promotion-workflow/minimal-demo.py
python prototypes/integrations/bounded-memory-review-workflow/minimal-demo.py
python prototypes/integrations/escalation-workflow/minimal-demo.py
```

Scenarios: `--scenario <name>` on each demo.

---

## Relation to Phase 2.0

```
Phase 2.0 prototypes  →  atomic governance lessons
Phase 2.1 integrations →  composed linear workflows
Phase 2.2+ (future)    →  NOT framework extraction
```

Do not import Phase 2.0 `minimal-demo.py` modules. Workflows reimplement composition inline.
