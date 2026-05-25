# Lesson: Audit Lineage

## What is this?

**Audit lineage** = append-only record of decisions: who, what gate, what outcome, why.

## Why does it matter?

Without lineage you cannot debug, comply, or trust post-incident review.

## What can go wrong?

- Thin logs ("error occurred")
- Deleted events after refactor
- No actor attribution

## How do we check it?

Every deny path has named gate + reason. Compare good vs bad trace docs.

`evaluation/trace-comparison/good-trace-vs-bad-trace.md`

```powershell
python integrations-real/filesystem-audit-log/minimal-demo.py --scenario happy
```

## Which demo shows it?

- All prototypes (audit dump)
- filesystem-audit-log adapter
- observability/examples/*.txt
