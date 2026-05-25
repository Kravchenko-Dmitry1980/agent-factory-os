# Module 01 — What Is an AI Agent?

## Goal

Understand an agent as a **bounded workflow** — not magic, not a person, not AGI.

## Simple Explanation

An **agent** here means: receive a task → use tools → maybe use memory → pass checks → maybe ask a human → produce an outcome. It is software with **rules**, not autonomous intelligence.

## Key Ideas

- Query loop: think → act → observe → repeat (with limits)
- Tools extend capability; gates limit harm
- Memory must be bounded and verified
- Subagents are delegated work units — not a swarm by default

## Files to Read

- `agent-os/01_agent-runtime/query-loop.md`
- `agent-os/01_agent-runtime/index.md`
- `prototypes/review-loop-agent/README.md`

## Commands to Run

```powershell
python prototypes/review-loop-agent/minimal-demo.py --scenario happy
python prototypes/review-loop-agent/minimal-demo.py --scenario uncertain-critic
```

## Exercise

[../exercises/exercise-run-first-demo.md](../exercises/exercise-run-first-demo.md)

## Common Mistakes

- Calling any LLM chat an "agent"
- Assuming more agents = better
- Removing limits to make demos "smarter"

## Checkpoint Questions

1. List four parts of a safe agent workflow.
2. What does the review-loop demo add beyond "call LLM once"?
3. Why are limits intentional?

## Expected Outcome

Student draws a simple box diagram: task → draft → critic → human → publish.
