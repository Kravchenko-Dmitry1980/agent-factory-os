# Failure Cascades

How small failures become governance incidents.

## Cascade 1: Critic → Publish

```
verification_passed (critic)  ← wrong: treated as truth
→ task_completed (publish)
→ (later) human discovers hallucination
```

**Break:** `approval_requested` mandatory.

## Cascade 2: Retry → Storm → Cost

```
verification_failed
→ retry_triggered (unbounded)
→ (no escalation_triggered)
→ budget exhausted
```

**Break:** `retry_exhausted` + ceiling.

## Cascade 3: LLM → Silent Accept

```
llm_malformed_output
→ (missing verification_failed)
→ task_completed
```

**Break:** fail-closed parse gate.

## Cascade 4: Memory Drift

```
memory write to durable (verified)
→ snapshot stale in session
→ agent "forgets" mid-task
→ retry_triggered on wrong assumption
```

**Break:** document frozen snapshot; explicit context load events.

## Reading Cascades

Follow [event lineage](../event-taxonomy/event-lineage.md) until first missing gate event — that is the injection point.
