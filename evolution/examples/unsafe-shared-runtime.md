# Example: Unsafe Shared Runtime

## Change

Extract `CritiqueService`, `QueueEngine`, `AuditPipeline` to `integrations-real/shared/`.

## Intent

DRY across adapters.

## Risk

Platform drift; hidden coupling; Phase 2.2 boundaries violated.

## Signals

- shared/ > 2 files
- Adapters import engine not audit helpers

## Rollback

Delete engine; duplicate 10-line functions per adapter.

## Lesson

[anti-platform-evolution.md](../governance/anti-platform-evolution.md)
