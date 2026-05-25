# Audit Chain Examples

## Action Lineage (External Publish)

```
task_received
review_pass
approval (fingerprint=abc123)
failure (verification failed)
escalated
```

From `integrations-real/filesystem-audit-log/minimal-demo.py`.

## Governance Lineage (Promotion)

```
source_received
review_pass
scan complete flags=[]
governance decision=promote_now
simulated_promote
```

## FastAPI Review API

SQLite audit rows mirror HTTP transitions:

```
submitted → approved | rejected | invalid_transition
```

## Reading

Walk `parent_id` chain or chronological JSONL — same story.
