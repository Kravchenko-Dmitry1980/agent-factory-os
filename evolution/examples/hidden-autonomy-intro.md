# Example: Hidden Autonomy Introduction

## Change

Add `auto_execute_low_risk=True` default in external-action adapter.

## Intent

Reduce Telegram noise.

## Risk

Risk classifier wrong → payment emails auto-sent.

## Symptom

Traces show `task_completed` without `approval_requested` for high-risk types.

## Drift Type

Autonomy drift.

## Rollback

Default `False`; deny-by-default restored.

## Lesson

[drift-patterns.md](../drift-detection/drift-patterns.md) — autonomy drift.
