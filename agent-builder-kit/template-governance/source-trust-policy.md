# Source Trust Policy

## Trusted Sources (in-repo)

| Source | Trust level | Use |
|--------|-------------|-----|
| `prototypes/` | high | Reference behavior, not copy-paste code |
| `evaluation/scenarios/` | high | Scenario definitions |
| `observability/event-taxonomy/` | high | Canonical events |
| `agent-os/doctrine/` | high | Principles |
| `governance/phase-2-8/` | high | Phase 3 scope |
| `operator-playbooks/` | medium | Operational patterns |

## Untrusted for Direct Import

- External GitHub templates
- Upstream agent frameworks
- Phase 2.10 triaged repos (research notes only)

## Provenance Rule

Every template must list **Related Prototypes** and governance refs. Copied structure without attribution → reject.

## Code

Kit must not embed or copy prototype `.py` files. Reference paths only.
