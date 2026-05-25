# Observable Failure

Failure is acceptable if **visible and bounded**.

## Requirements

1. Canonical event emitted
2. Plain-language reason
3. Terminal OUTCOME clear
4. Lineage preserved

## Anti-Fragile Outcome

Postmortem without code access — trace + audit sufficient.

## Repository Alignment

- `observability/examples/*-trace.txt`
- `integrations-real/.data/**/audit.jsonl`

## Change Test

If failure mode added but not observable — change incomplete.
