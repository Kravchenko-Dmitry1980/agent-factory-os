# Module 02 — Why AI Systems Fail

## Goal

Learn **failure modes** — especially silent failures that look like success.

## Simple Explanation

AI fails more often by **plausible wrong answers** than by crashes. Systems fail when we trust output without verification, skip approval, or let memory/context grow without bounds.

## Key Ideas

- Hallucination and confident tone
- Critic pass ≠ correct facts
- Retry storms mask bugs
- Missing audit = invisible decisions
- Platform drift erodes gates slowly

## Files to Read

- `agent-os/09_antipatterns/index.md`
- `evolution/examples/accidental-auto-approve.md`
- [../lessons/lesson-critic-is-not-truth.md](../lessons/lesson-critic-is-not-truth.md)

## Commands to Run

```powershell
python prototypes/review-loop-agent/minimal-demo.py --scenario bypass-attempt
python prototypes/integrations/review-queue-workflow/minimal-demo.py --scenario approval-denied
```

Read trace: `observability/examples/failed-review-trace.txt`

## Exercise

[../exercises/exercise-break-review-loop.md](../exercises/exercise-break-review-loop.md) *(observe only — read failure modes, do not break code)*

## Common Mistakes

- Only testing happy path
- Fixing failures by removing gates
- Blaming the model instead of fixing workflow

## Checkpoint Questions

1. Give an example of silent failure.
2. What happened in failed-review trace when critic passed?
3. Name one anti-pattern from agent-os.

## Expected Outcome

Student lists three silent failure types and one demo that demonstrates each.
