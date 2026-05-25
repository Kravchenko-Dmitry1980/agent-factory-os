# Example: Rollback Failure

## Situation

Team patched forward 4 commits after retry change caused storms.

## Mistakes

- No revert hash recorded
- Shared constant used in 3 demos
- failure-modes not updated
- Only happy path tested

## Result

Escalation broken in one demo, silent in another — inconsistent governance.

## Recovery Cost

Manual line-by-line compare to Phase 2.1 review doc.

## Lesson

[rollback-vs-patch.md](../rollback-thinking/rollback-vs-patch.md) — should have rolled back at trigger 30min.

## Prevention

[rollback-triggers.md](../rollback-thinking/rollback-triggers.md)
