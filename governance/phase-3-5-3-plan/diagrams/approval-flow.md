# Diagram — Approval Flow

**Phase 3.5.3-Plan**

```mermaid
flowchart TD
  V[verification_passed] --> AR[approval_requested]
  AR --> PROMPT["Approve result? yes/no [no]"]
  PROMPT --> ANS{Answer}
  ANS -->|yes| SAFE{Output safe?}
  ANS -->|no / Enter| DENY[approval_denied / missing]
  SAFE -->|yes| GRANT[approval_granted]
  SAFE -->|no unsafe| BLOCK[unsafe_action_blocked]
  GRANT --> DEL[DELIVERED delivered=True]
  DENY --> BLK[BLOCKED delivered=False]
  BLOCK --> FAIL[FAILED delivered=False]
  VF[verification_failed] --> FAIL2[FAILED no approval path]
```

## Rules

| State | Delivery |
|-------|----------|
| approval_granted + safe | allowed |
| approval denied / default no | BLOCKED |
| verification_failed | FAILED — no approval |
| unsafe output | FAILED — approval cannot override |

See [APPROVAL_MODEL_PLAN.md](../APPROVAL_MODEL_PLAN.md).
