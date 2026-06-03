# Agent Factory OS

**Agent Factory OS** is a governance-first open-source system for designing, validating, and safely evolving AI agents.

It combines documentation-first agent engineering, frozen baselines, local evaluation harnesses, and operator-friendly CLI demos so teams can build auditable, human-supervised agents without treating model output as truth.

---

## What it is

- Methodology and tooling for **safe agent development**
- **Agent templates** with contracts, safety gates, and expected traces
- **Freeze / sign-off workflows** and phase reviews
- **Provider boundary patterns** (mock by default, real provider opt-in only)
- **Local prototypes** and thin implementations
- **Evaluation harnesses** (no-network baselines)
- **Operator-friendly CLI demos** (Review Assistant Demo Runner)

---

## What it is not

- Not a production SaaS or hosted agent platform
- Not an autonomous agent swarm or orchestrator framework
- Not a model provider SDK or benchmark leaderboard
- Not a red-team or penetration platform
- Not a replacement for human review and approval
- Not affiliated with OpenAI, Anthropic, Hermes, Claude, or other vendor projects

---

## Current working demo

**Review Assistant Demo Runner** (mock / no network by default):

```powershell
cd C:\Dima\Projects\CURSOR\AGENT
python demos/review-assistant-runner/demo_runner.py --list
python demos/review-assistant-runner/demo_runner.py --scenario happy
python demos/review-assistant-runner/demo_runner.py --scenario missing_approval
```

See [demos/review-assistant-runner/README.md](demos/review-assistant-runner/README.md).

---

## Core ideas

- Provider output is **not** truth
- LLM output is **not** truth
- Human approval is **explicit**
- Unsafe actions **fail closed**
- Traces are **human-readable**
- Changes require **governance**
- Memory / writeback must be **bounded and approved**

---

## Repository map

| Path | Purpose |
|------|---------|
| [agent-builder-kit/](agent-builder-kit/) | Agent template specifications and safety gates |
| [governance/](governance/) | Phase reviews, freeze records, risk and change control |
| [prototypes/](prototypes/) | Educational prototype demos |
| [prototypes-derived/](prototypes-derived/) | Derived thin implementations |
| [evaluation/](evaluation/) | Local safety checks and evaluation harnesses |
| [demos/](demos/) | Operator-facing CLI demos |
| [operator-playbooks/](operator-playbooks/) | Human runbooks and onboarding |
| [curriculum/](curriculum/) | Learning materials |
| [observability/](observability/) | Human-readable diagnostics and trace concepts |
| [evolution/](evolution/) | Safe change and rollback discipline |
| [integrations-real/](integrations-real/) | Local adapter boundary experiments |

Additional knowledge and research layers (e.g. `agent-os/`, `Books/`) support the lab curriculum; start with the table above for the agent factory line.

---

## Quickstart

| Audience | Entry |
|----------|-------|
| Russian (recommended) | [START_HERE_RU.md](START_HERE_RU.md) → [QUICKSTART_RU.md](QUICKSTART_RU.md) |
| Project overview | [docs/PROJECT_OVERVIEW.md](docs/PROJECT_OVERVIEW.md) |
| Architecture (RU) | [docs/ARCHITECTURE_RU.md](docs/ARCHITECTURE_RU.md) |
| Demo runner | [demos/review-assistant-runner/README.md](demos/review-assistant-runner/README.md) |

---

## Status

- **Early-stage OSS** — active development
- **Local-first** — baselines run without network by default
- **Governance-first** — freezes and reviews before expansion
- **Not production-ready** — no security certification or SLA claims

---

## License

[MIT License](LICENSE) — Copyright (c) 2026 Dmitry Kravchenko

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## Security

See [SECURITY.md](SECURITY.md). Do not commit secrets or real client data.

---

## Roadmap

Near-term plans: [ROADMAP.md](ROADMAP.md)
