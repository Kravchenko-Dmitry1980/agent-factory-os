# Shared Prototype Utilities

Minimal helpers reused across Phase 2.0 prototypes. **Not a framework.**

## Modules

| File | Purpose |
|------|---------|
| `types.py` | Common enums: `Outcome`, `GateResult`, `AuditEvent` |
| `audit.py` | Append-only in-memory audit log |
| `gates.py` | Fail-closed gate helpers |

## Usage

```python
from prototypes.shared.audit import AuditLog
from prototypes.shared.gates import fail_closed, require_approval
```

Each prototype may import these or stay fully self-contained for readability.
