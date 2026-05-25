# Common Student Misunderstandings

| Misunderstanding | Correction |
|------------------|------------|
| "Critic verified facts" | Critic checked quality/style; facts need separate verification |
| "JSON from LLM = safe" | Structure OK ≠ content true |
| "Exit 0 = safe" | Gates may be removed; read audit |
| "More agents = better" | More gates unclear = worse |
| "Prototypes = MVP to ship" | Prototypes = teaching sketches |
| "Evaluation = unit tests" | Local behavioral check + human trace |
| "Phase 2 done → factory" | Phase 3 entry criteria required |
| "Memory = full chat history" | Bounded, verified writeback |
| "Retries fix bugs" | Retries mask; fix verification |
| "Fail-closed = bad UX" | Fail-closed = safe default for high impact |

## Teaching response

Always return to **trace**: show the event that proves the gate ran.

## Red flag answers

If student says "we can skip human for internal" — assign fail-closed exercise immediately.
