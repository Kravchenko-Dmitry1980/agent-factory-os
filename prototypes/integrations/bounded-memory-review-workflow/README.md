# Bounded Memory Review Workflow

**Composes:** bounded memory + review loop + verification-before-writeback.

## Flow

```
context load → execution → critique → verification → writeback/reject
```

## Run

```powershell
python prototypes/integrations/bounded-memory-review-workflow/minimal-demo.py
python prototypes/integrations/bounded-memory-review-workflow/minimal-demo.py --scenario overflow
python prototypes/integrations/bounded-memory-review-workflow/minimal-demo.py --scenario uncertain
python prototypes/integrations/bounded-memory-review-workflow/minimal-demo.py --scenario unverified
```
