# GUI Verification Loop — Governance

## A/B/C Taxonomy

| Outcome | Meaning | Agent may advance goal? |
|---------|---------|-------------------------|
| **A** | Expected transition | Yes |
| **B** | Wrong screen | No — replan |
| **C** | No meaningful change | No — retry (bounded) |

## Fail-Closed Rules

- Only **A** allows marking subgoal complete
- **B** and **C** reject premature success claims
- Unverified click → never execute in demo pipeline

## Alignment

- `agent-os/01_agent-runtime/gui-agent-loop.md`
- `agent-os/00_foundations/visual-verification.md`
