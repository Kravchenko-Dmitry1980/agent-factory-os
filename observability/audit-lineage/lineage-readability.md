# Lineage Readability

## One Event Per Line (JSONL)

```json
{"event_id":"e1","action":"task_received","actor":"workflow","parent_id":null}
{"event_id":"e2","action":"review_pass","actor":"reviewer","parent_id":"e1"}
```

Human view — convert to trace format:

```
[e1] task_received   actor=workflow
[e2] review_pass     actor=reviewer  parent=e1
```

## Rules

1. Include `actor`, `action`, timestamp
2. Use `parent_id` for forks
3. Name actions with canonical vocabulary
4. Avoid nesting detail — flat keys

## Bad

```json
{"blob": {"a": {"b": {"c": 1}}}}
```

## Good

```json
{"action":"verification_failed","reason":"malformed JSON","actor":"verifier"}
```
