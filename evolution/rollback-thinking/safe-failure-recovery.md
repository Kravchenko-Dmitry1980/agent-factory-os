# Safe Failure Recovery

Recovery **after** governed failure — not bypass.

## Order

1. Confirm fail-closed worked (harm prevented)
2. Read trace / audit lineage
3. Decide: rollback vs bounded patch
4. Re-run failure scenario demos
5. Update observability example if needed

## Good Recovery

Escalation fired → human resolved → small doc clarifying gate.

## Bad Recovery

Verification failed → remove verification "temporarily".

## Preserve Lineage

Recovery events link to failure event via `parent_id` — see [observability/audit-lineage/](../../observability/audit-lineage/).

## Fail Closed During Recovery

While unstable, default to mock/deny modes in adapters.
