# Repository Review: claude-code-action

## Basic Info

| Field | Value |
|-------|-------|
| **URL** | https://github.com/anthropics/claude-code-action |
| **Local path** | `external-repos-triage/source/claude-code-action/` |
| **Main purpose** | Official GitHub Action running Claude Code on PRs/issues |
| **Claimed capabilities** | Auto mode detection, code review, implementation, structured outputs, multi-cloud auth |
| **Primary audience** | Repos wanting PR automation with Claude |
| **Main language / stack** | GitHub Action (TypeScript), docs for Bedrock/Vertex/Foundry |
| **Last inspected** | 2026-05-25 |
| **Commit inspected** | `787c5a0` |

## What This Repo Is

**CI/CD automation** layer: Claude on GitHub runner with permissions to repo — complements local Claude Code, not replaces learning lab.

## What This Repo Is NOT

- Not for Phase 3.0 (evaluation explicitly no CI/CD)
- Not beginner first step
- Not governed by our fail-closed demos

## Most Useful Ideas

- Solutions guide patterns (PR review, path-specific, security review)
- Security docs: permissions, commit signing
- Migration guide v0→v1 — lifecycle discipline
- «Runs on your infrastructure» — data boundary clarity

## Dangerous Ideas

- **Unattended code changes** on PR
- **@claude** triggers without human gate culture
- MCP expansion in Action config
- Conflicts with `evaluation/governance/no-ci-cd-policy.md`

## Relevance

| Area | Relevance |
|------|-----------|
| Phase 3.0 | **NONE** |
| Future | **Phase 5+** controlled GitHub automation |
| Agent Builder Kit | **Indirect** — review checklist inspiration |

## Security / Supply Chain

- GitHub token scope
- Third-party runner secrets
- Auto-implement features

## What We Can Learn

- PR review automation **patterns** (checklist only)
- Permission minimization docs

## What We Must Not Copy

- Workflow YAML into AGENT repo now
- Auto-merge patterns

## Decision

**FREEZE** until dedicated automation phase

## Rationale

High **CI/CD agent autonomy** risk; contradicts Phase 2 evaluation policy.

## Recommended Future Action

After team masters local smoke + human approval: pilot on fork with read-only review mode first; never Phase 3.0.
