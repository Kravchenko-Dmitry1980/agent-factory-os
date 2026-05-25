# Example: Escalation Removal Disaster

## Change

Remove `ESCALATED` status — failed tasks marked `FAILED` and dropped from queue display.

## Intent

Cleaner queue UI in hypothetical dashboard.

## Risk

Human never notified; tasks vanish; autonomy failure invisible.

## Trace Regression

`retry_exhausted` without `escalation_triggered`.

## Observability

Operators see empty queue — false healthy.

## Rollback

Restore ESCALATED + supervisor audit event.

## Lesson

Escalation is success — [escalation-intelligence](../../observability/escalation-intelligence/).

Removing it is governance regression, not UX cleanup.
