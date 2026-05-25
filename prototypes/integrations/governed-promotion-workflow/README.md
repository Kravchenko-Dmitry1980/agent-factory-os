# Governed Promotion Workflow

**Composes:** promotion simulator + provenance + governance + anti-pattern scan.

## Flow

```
source → review → anti-pattern scan → governance → approve/reject
```

## Run

```powershell
python prototypes/integrations/governed-promotion-workflow/minimal-demo.py
python prototypes/integrations/governed-promotion-workflow/minimal-demo.py --scenario missing-provenance
python prototypes/integrations/governed-promotion-workflow/minimal-demo.py --scenario dangerous-topology
python prototypes/integrations/governed-promotion-workflow/minimal-demo.py --scenario governance-bypass
```
