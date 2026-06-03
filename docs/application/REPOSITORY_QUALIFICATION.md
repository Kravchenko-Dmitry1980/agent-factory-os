# Repository Qualification

## Open-source intent

This repository is maintained as a public **Agent Factory OS** project with MIT license, contribution guidelines, security policy, and reproducible no-network baselines.

## Substantive content

| Area | Evidence |
|------|----------|
| Agent engineering | `agent-builder-kit/`, templates, safety gates |
| Implementations | `prototypes-derived/review-assistant-thin/` |
| Safety evaluation | `evaluation/scripts/`, provider safety harness |
| Operator tooling | `demos/review-assistant-runner/demo_runner.py` |
| Governance | `governance/` phase and freeze records |
| Education | `curriculum/`, `operator-playbooks/`, RU quickstart |

## Reproducibility

Documented commands run without API keys or network (see PUBLIC_RELEASE_VALIDATION.md).

## Safety hygiene

- `.gitignore` excludes `.env`, `.venv`, `.data`, transcripts, external clones
- No secrets committed in release preparation scan (documentation placeholders only)
- Real provider documented as opt-in only

## Not qualified as

- Production SaaS
- Official vendor partner project
- Benchmark or red-team platform

## Application short text

Agent Factory OS is an early-stage open-source project for governance-first AI agent engineering. It includes agent templates, safety gates, freeze/sign-off workflows, local provider boundaries, evaluation harnesses, and operator-friendly CLI demos for building auditable, maintainable, human-supervised AI agents.
