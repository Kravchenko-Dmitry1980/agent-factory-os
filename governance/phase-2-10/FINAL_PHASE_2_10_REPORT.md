# Final Phase 2.10 Report

**Date:** 2026-05-25

---

## Repos reviewed

6 — all shallow-cloned to `external-repos-triage/source/`

## Local clones created?

**Yes** — `--depth 1` only. No install, no run.

## Files created

- `external-repos-triage/` — README, 6 repo-reviews, comparison, 6 useful-patterns, 8 dangerous-patterns, security-notes, future-backlog pointer, 5 diagrams  
- `governance/phase-2-10/` — 10 governance docs + 2 diagrams  

## Top useful patterns

1. Skill file structure (YAML frontmatter + when-NOT)  
2. Template taxonomy (agent/command/hook/MCP/skill)  
3. Security disclaimer + selective install policy  
4. Externalized PM Spec/Plan/Rules  
5. PR review checklist patterns (MD only)  

## Top dangerous patterns

1. Swarm platform drift (ruflo)  
2. Template/skill dumping (`npx --yes`)  
3. CI/CD agent autonomy (claude-code-action)  
4. Self-learning/RAG memory hype  
5. Runtime-before-specs (`npx init`)  

## Highest-value repo

**scientific-agent-skills** — for future skill-template-spec (structure + security culture)

## Highest-risk repo

**ruflo** — swarm, MCP, RAG, autopilot, massive install surface

## Phase 3.0 scope changed?

**No**

## Anything adopted?

**No**

## Anything installed/executed?

**No** — no npm/pip/uv/docker/scripts from upstream

## Research-only decisions

All six repos — see [RESEARCH_ONLY_DECISIONS.md](RESEARCH_ONLY_DECISIONS.md)

## Future backlog

[FUTURE_BACKLOG.md](FUTURE_BACKLOG.md)

## What was NOT modified

agent-os, Books, experiments, prototypes, integrations-real, observability, evolution, evaluation, curriculum, operator-playbooks — **no changes**

agent-builder-kit/ — **not created**

## Recommendation before Phase 3.0

1. User confirms [../PHASE_3_START_CONDITIONS.md](../PHASE_3_START_CONDITIONS.md) C1–C8  
2. Read [../../PHASE_3_WARNING_RU.md](../../PHASE_3_WARNING_RU.md)  
3. Start Phase 3 prompt: **internal** Review Assistant spec only — cite phase-2-8 + phase-2-10 DO_NOT_ADOPT  
4. Do **not** import external templates in same PR  

## Optional housekeeping

Add `external-repos-triage/source/` to `.gitignore` if clones should not be committed (large size).
