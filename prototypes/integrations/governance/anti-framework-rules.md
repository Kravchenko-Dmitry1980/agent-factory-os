# Anti-Framework Rules

Phase 2.1 exists to **prevent** the following patterns.

## Forbidden Patterns

1. **`class BaseWorkflow`** or any inherited workflow hierarchy
2. **`register_step()`** or plugin discovery
3. **`WorkflowEngine.run(pipeline)`** generic executor
4. **`Agent` ABC** with `execute()` / `verify()` hooks
5. **Event bus** (`emit`, `subscribe`) between steps
6. **Dependency injection container**
7. **Config-driven step lists** replacing readable code
8. **"Universal" retry middleware** hiding escalation logic

## Allowed Patterns

1. Plain functions: `enqueue()`, `draft()`, `critique()`, `publish()`
2. Dataclasses for **this workflow's** state only
3. Enums for statuses in **this file**
4. `AuditLog.record()` after each step
5. `if scenario == "x":` for failure demos

## Duplication Is Good

Two workflows needing similar critique logic?

**Copy the 10 lines.** Do not extract `CritiqueService`.

## Review Question

> Could this code ship as a pip package named `agent-workflows`?

If yes — you've built a framework. Delete the abstraction layer.
