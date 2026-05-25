# Incremental Change

One governance dimension per change set.

## Good Sequence

1. Add observability event (docs + audit name)
2. Add demo scenario flag for new failure
3. Change gate logic in one demo
4. Update integration if needed
5. Update example trace

## Bad Sequence

Rewrite all workflows + new shared lib + real adapter in one PR.

## Size Heuristic

- One `minimal-demo.py` behavioral change OR
- Docs-only batch OR
- One new adapter directory

Never all three at once.

## Validate Each Step

Run failure scenarios before next increment.
