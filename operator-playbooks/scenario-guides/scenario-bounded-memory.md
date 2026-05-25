# Scenario: Bounded Memory

## What It Teaches

Memory is bounded; writeback only after verification. Frozen snapshot preserved.

## What Can Go Wrong

- Unbounded context growth
- Write without verification
- Silent truncate on overflow

## Correct Safe Behavior

- `happy` → verified write within limit
- `overflow` → reject
- `unverified-writeback` → reject

## Files to Run

```powershell
python prototypes/bounded-memory-agent/minimal-demo.py --scenario happy
python prototypes/bounded-memory-agent/minimal-demo.py --scenario overflow
python prototypes/bounded-memory-agent/minimal-demo.py --scenario unverified-writeback
python prototypes/integrations/bounded-memory-review-workflow/minimal-demo.py --scenario overflow
```

## Traces to Inspect

- Demo audit (no dedicated example trace — check audit actions)

## Evaluation Checks

- `evaluation/scenarios/bounded-memory-scenarios.md`
- Smoke: `bounded-memory overflow`

## Deep Docs

- [../safety-guides/why-memory-must-be-bounded.md](../safety-guides/why-memory-must-be-bounded.md)
- `agent-os/doctrine/bounded-memory.md`
