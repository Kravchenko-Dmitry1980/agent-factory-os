# Promotion Pipeline Simulator

**Purpose:** Validate governance workflow, promotion gates, provenance tracking.

## Flow

```
source → review → governance → promote OR reject
```

## Run

```powershell
python prototypes/promotion-pipeline-simulator/minimal-demo.py
python prototypes/promotion-pipeline-simulator/minimal-demo.py --scenario reject
python prototypes/promotion-pipeline-simulator/minimal-demo.py --scenario later
```

## Doctrine Links

- `governance/PROMOTION_STRATEGY.md`
- `agent-os/doctrine/system-positioning.md`
