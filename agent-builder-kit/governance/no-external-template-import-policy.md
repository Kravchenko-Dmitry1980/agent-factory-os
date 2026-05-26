# No External Template Import Policy

## Rule

External repositories are **research-only**. Do not import their templates into agent-builder-kit.

## Source

`governance/phase-2-10/FINAL_PHASE_2_10_REPORT.md` — no adoption verdict.

## Allowed

- Structural inspiration documented in governance notes
- Links to external repos as bibliography
- Comparison tables in phase-2-10 triage docs

## Forbidden

- Copy upstream template folders
- Embed LangGraph/AutoGen/Crew configs
- Promote external README into kit templates without full governance review

## If import ever needed

Follow [external-template-policy.md](../template-governance/external-template-policy.md) — still no runtime in kit.

## Phase 3.0 compliance

Review Assistant is derived from **in-repo prototypes only**:

- `prototypes/review-loop-agent/`
- `prototypes/integrations/review-queue-workflow/`

No upstream code copied.
