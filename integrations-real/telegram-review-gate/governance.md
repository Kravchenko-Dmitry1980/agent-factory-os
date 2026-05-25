# Telegram Review Gate — Governance

| Principle | Implementation |
|-----------|----------------|
| Explicit approval | Human message or mock flag |
| Deny-by-default timeout | No response = deny |
| Audit log | Append-only JSONL |
| Approval fingerprint | SHA256 of action |
| Escalation | High-risk timeout → escalate record |
| Fail-closed | Never continue on uncertainty |

## Alignment

- `prototypes/fail-closed-external-action/`
- `prototypes/integrations/review-queue-workflow/`
