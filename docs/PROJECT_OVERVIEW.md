# Agent Factory OS — Project Overview

## Purpose

Agent Factory OS helps teams design AI agents with **governance first**: explicit contracts, human approval, fail-closed safety, frozen baselines, and local evaluation before any optional real-provider experiment.

## Who benefits

- Engineers building **auditable** agent workflows
- Operators running **CLI demos** and reading human-readable traces
- Educators and labs teaching **safe agent patterns** (RU/EN curriculum)
- Maintainers who need **freeze records** and phase reviews, not ad-hoc prompts

## What is implemented today

- Review Assistant **template** and **thin** implementation (`prototypes-derived/review-assistant-thin/`)
- **Mock LLM** boundary and **provider safety harness** (16 synthetic cases, no network)
- **Real provider contract** checks (no-network by default; live opt-in documented)
- **Demo Runner v0.1** with scenario menu and Russian operator docs
- **Evaluation scripts** for thin, mock, smoke, and text traces
- **Governance** phase reviews and freeze artifacts
- **Task Triage Agent** template specs (v0.1, documentation-only line)

## What is planned

See [ROADMAP.md](../ROADMAP.md): free-form CLI freeze, memory triage, task triage thin implementation, optional live provider harness.

## What remains non-production

- No hosted runtime or multi-tenant SaaS
- No guarantee of model quality or benchmark scores
- Real provider paths require explicit operator setup and are not default
- Human approval and governance gates remain mandatory for delivery scenarios

## Entry points

- [README.md](../README.md)
- [START_HERE_RU.md](../START_HERE_RU.md)
- [demos/review-assistant-runner/README.md](../demos/review-assistant-runner/README.md)
