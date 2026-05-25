# GUI Safe Action — Governance

| Rule | Implementation |
|------|----------------|
| Mock only | SCREENS dict, no real automation |
| A/B/C verify | Before execute |
| Deny-by-default | B, C, uncertain → reject |
| Approval gate | High-risk actions |
| Audit | Every observe/verify/gate/execute |

## Alignment

- `prototypes/gui-verification-loop/`
- `prototypes/fail-closed-external-action/`
