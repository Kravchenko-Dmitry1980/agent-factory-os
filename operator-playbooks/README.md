# Operator Playbooks (Phase 2.6)

**Status:** Human onboarding and runbooks — not a runtime, not automation.

---

## What This Repository Is

Use this repo to **learn and practice** governed AI workflow architecture:

| Layer | Path | What it gives you |
|-------|------|-------------------|
| Knowledge & doctrine | `agent-os/` | Principles, patterns, anti-patterns |
| Governance | `governance/` | What may enter the curated core |
| Graph navigation | `graph/` | How to find related ideas |
| Reference demos | `prototypes/` | Small Python sketches (~200 lines) |
| Composed workflows | `prototypes/integrations/` | Mock multi-step workflows |
| Real local adapters | `integrations-real/` | Optional real I/O (mock by default) |
| Observability | `observability/` | How to read traces and failures |
| Safe change | `evolution/` | How to change without breaking gates |
| Behavioral checks | `evaluation/` | Local smoke + trace comparison |
| Operator guides | `operator-playbooks/` | **You are here** |

---

## What Problem It Solves

The system is powerful but easy to get lost in. Phase 2.6 answers:

1. Where should a new person start?
2. What to read and run first?
3. What not to touch?
4. How to know behavior is still safe?
5. How to make a small change and verify it?
6. How to report problems?

---

## What the Operator Can Do

- Read doctrine and patterns in `agent-os/`
- Run prototype and adapter demos locally
- Read trace examples in `observability/examples/`
- Run evaluation smoke checks (`evaluation/scripts/`)
- Propose changes using `evolution/change-proposals/`
- Compare behavior before/after a change
- Onboard teammates using paths in `learning-paths/`

---

## What the Operator Must NOT Do

- Turn prototypes into a production platform
- Add CI/CD, dashboards, or test frameworks
- Extract a shared orchestration engine
- Auto-approve AI output or skip human gates
- Patch demos blindly when something fails
- Promote ideas into `agent-os/` without governance review
- Modify `Books/` or `experiments/` as part of operator tasks

See [start-here/what-not-to-touch.md](start-here/what-not-to-touch.md).

---

## This Project Is

- An **AI architecture learning system**
- A **governance-first knowledge system**
- A **safe workflow laboratory**
- A **collection of small reference prototypes**

---

## This Project Is NOT

- Production AI platform
- Autonomous agent system
- Claude competitor
- Hermes clone
- AGI system
- Deployment platform

Full positioning: [agent-os/doctrine/system-positioning.md](../agent-os/doctrine/system-positioning.md)

---

## How to Navigate (Don't Get Lost)

```text
New here?     → start-here/start-here.md
Need commands → runbooks/
Something broke → troubleshooting/
Making a change → change-guides/
Safety why?     → safety-guides/
Teaching someone → onboarding/
```

**Map for beginners:** [diagrams/system-map-for-beginners.md](diagrams/system-map-for-beginners.md)

---

## Recommended Entry (First 30 Minutes)

1. Read this README
2. Read [agent-os/doctrine/system-positioning.md](../agent-os/doctrine/system-positioning.md)
3. Run one prototype — [runbooks/run-prototypes.md](runbooks/run-prototypes.md)
4. Read one trace — [runbooks/run-observability-examples.md](runbooks/run-observability-examples.md)
5. Run evaluation smoke — [runbooks/run-evaluation-checks.md](runbooks/run-evaluation-checks.md)
6. Read [start-here/what-not-to-touch.md](start-here/what-not-to-touch.md)

Detail: [start-here/first-30-minutes.md](start-here/first-30-minutes.md)

---

## Relation to Other Phases

```
Phase 1.x  agent-os, graph, governance  → what we believe
Phase 2.0  prototypes                     → what we can demo
Phase 2.1  integrations                   → composed mock workflows
Phase 2.2  integrations-real            → real local I/O
Phase 2.3  observability                  → readable traces
Phase 2.4  evolution                      → safe change discipline
Phase 2.5  evaluation                     → local behavioral checks
Phase 2.6  operator-playbooks             → human usability (this)
```

Governance review: [../governance/PHASE_2_6_OPERATOR_PLAYBOOK_REVIEW.md](../governance/PHASE_2_6_OPERATOR_PLAYBOOK_REVIEW.md)
