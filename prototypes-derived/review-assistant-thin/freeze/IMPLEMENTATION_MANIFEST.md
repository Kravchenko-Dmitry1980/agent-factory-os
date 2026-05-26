# Implementation Manifest — Review Assistant Thin v0.1

| File | Purpose | Frozen? | Notes |
|------|---------|---------|-------|
| README.md | Entry docs, run commands, scope | yes | Navigation may append |
| minimal_demo.py | **Only executable** — 5 scenarios, trace output | yes | stdlib-only; scenario-based |
| contracts.md | I/O, states, events | yes | |
| behavior.md | Flow and rules | yes | |
| trace_examples.md | Expected trace shapes | yes | |
| evaluation.md | Manual eval steps | yes | |
| failure_modes.md | Known failure guards | yes | |
| governance.md | Scope lock | yes | |
| rollback.md | Revert procedure | yes | |
| freeze/README.md | Freeze index | no | Metadata |
| freeze/IMPLEMENTATION_FREEZE_RECORD.md | Freeze record | no | Metadata |
| freeze/IMPLEMENTATION_MANIFEST.md | This file | no | Metadata |
| freeze/SCENARIO_BASELINE.md | Scenario baselines | no | Metadata |
| freeze/CHANGE_LOCK.md | Change policy | no | Metadata |
| freeze/ROLLBACK_RECORD.md | Rollback record | no | Metadata |

## Executable summary

- **One file:** `minimal_demo.py`
- **Dependencies:** none (Python stdlib)
- **Hidden state:** none
- **Network:** none
- **Memory persistence:** none

## Template link

Implements (does not replace): `agent-builder-kit/templates/review-assistant-agent/` v0.1 frozen spec.

## Reference (read-only)

`prototypes/review-loop-agent/` — patterns only; not imported at runtime from prototypes.shared.
