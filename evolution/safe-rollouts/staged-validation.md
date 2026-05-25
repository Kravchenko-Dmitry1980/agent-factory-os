# Staged Validation

Stages for governed changes (manual, local).

| Stage | Validation |
|-------|------------|
| **S0** | Change proposal filled |
| **S1** | Unit demos happy path |
| **S2** | All failure `--scenario` flags |
| **S3** | Trace matches observability examples |
| **S4** | Real adapter mock-offline still works |
| **S5** | (Optional) `--real` smoke |
| **S6** | Governance gate checklist |

No stage skipping.

## Artifact

Short note in PR or commit body: `Validated: S0-S4`.

## Failure at Stage Sn

Do not advance — rollback or fix before next stage.
