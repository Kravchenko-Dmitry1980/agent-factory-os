# Example: Accidental Auto-Approve

## Change

"Internal blog posts don't need human" — skip `human_review()` when `channel=internal`.

## Intent

Speed for trusted channel.

## Risk

Internal becomes external via config typo; critic hallucination publishes.

## Trace Regression

Missing `approval_requested` before `task_completed`.

## Governance Impact

Approval gate bypass — risk 5.

## Rollback

Remove branch; all publishes through HITL.

## Lesson

[human-review-boundaries.md](../governance-gates/human-review-boundaries.md) — no internal exception.
