# Hidden Drift Analysis

Drift that hides inside **good metrics** or **green demos**.

## Case 1: Happy Path Only Testing

Demos pass `--scenario happy` only → failure gates rot.

**Fix:** CI mentally = run all `--scenario` failure flags locally.

## Case 2: Mock Always On

Real adapter never tested → production surprise.

**Fix:** Periodic `--real` smoke with credentials, still single-process.

## Case 3: Documentation Lag

Code changed, `failure-modes.md` stale → false confidence.

**Fix:** Same PR updates docs (or reject).

## Case 4: Promotion Skip

Experiment → agent-os copy without governance pipeline.

**Fix:** [governance/PROMOTION_STRATEGY.md](../../governance/PROMOTION_STRATEGY.md)

## Case 5: Observability Theater

Many events, none canonical — unreadable postmortems.

**Fix:** [observability/event-taxonomy/](../../observability/event-taxonomy/)

## Question

> Would we notice governance erosion in one week of only happy-path runs?

If no — hidden drift present.
