# Dangerous Pattern: CI/CD Agent Autonomy

| Field | Value |
|-------|-------|
| **Source** | claude-code-action |
| **Why tempting** | Auto PR review/fix |
| **Why dangerous** | No human in loop; token scope |
| **Early signals** | workflow on every PR without approval |
| **Mitigation** | evaluation no-ci-cd-policy |
| **Phase 3.0** | **Forbidden** |
