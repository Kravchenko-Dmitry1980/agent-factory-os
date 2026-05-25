# Before Promoting Idea

Promoting into `agent-os/` curated layer — not "saving a note."

- [ ] Read `governance/PROMOTION_STRATEGY.md`
- [ ] Provenance documented (source path, origin)
- [ ] Pattern paired with anti-pattern where applicable
- [ ] Not a tutorial/swarm template without gates
- [ ] Run promotion simulator if concept is architectural:

```powershell
python prototypes/promotion-pipeline-simulator/minimal-demo.py --scenario promote
python prototypes/integrations/governed-promotion-workflow/minimal-demo.py --scenario missing-provenance
```

- [ ] Human governance review — no auto-promote

Simulation ≠ real promotion.
