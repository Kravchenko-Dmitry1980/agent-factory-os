# Agent Factory OS — One Pager

**Tagline:** Governance-first open source for designing, validating, and safely evolving AI agents.

## Problem

Agent prototypes often ship fast but lack approval gates, frozen baselines, and operator-readable traces—making production handoff risky.

## Solution

Agent Factory OS bundles templates, safety harnesses, governance reviews, and CLI demos so every delivery path can fail closed without human approval.

## Proof today

- Review Assistant Demo Runner (`--scenario happy`, `missing_approval`)
- Provider safety harness: 16/16 PASS (no network)
- Frozen artifacts: thin v0.3, harness v0.1, demo runner v0.1

## Differentiators

| Topic | Agent Factory OS |
|-------|------------------|
| Truth model | Provider/LLM output is advisory only |
| Default mode | Mock / local / no network |
| Change control | Freeze + governance phases |
| Audience | Engineers, operators, educators |

## Status

Early-stage OSS, local-first, active development, not production-ready.

## Links

- Repo root [README.md](../../README.md)
- Quickstart [QUICKSTART_RU.md](../../QUICKSTART_RU.md)
- Validation [PUBLIC_RELEASE_VALIDATION.md](PUBLIC_RELEASE_VALIDATION.md)
