# Safety Regression Checklist

Use after any template change (before re-accept or re-freeze).

## Gates unchanged or improved

- [ ] Fail-closed still default
- [ ] Verification still before delivery
- [ ] Human approval still required for risky outputs
- [ ] No new bypass path introduced

## Scenarios

- [ ] Happy path still passes criteria
- [ ] Fail path still terminates cleanly
- [ ] Missing approval still blocks
- [ ] Bypass attempt still blocked
- [ ] Critic uncertain still fail-closed

## Trace

- [ ] Required events still present
- [ ] No new silent steps
- [ ] Before/after trace comparison done

## Memory & Tools

- [ ] No new unrestricted tools
- [ ] No new auto writeback
- [ ] Memory limits unchanged or tightened

## Rollback

- [ ] Rollback plan documented
- [ ] Previous version tagged or identifiable
