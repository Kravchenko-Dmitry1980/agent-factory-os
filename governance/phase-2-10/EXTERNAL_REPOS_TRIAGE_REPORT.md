# External Repos Triage Report

**Phase:** 2.10  
**Date:** 2026-05-25  
**Method:** Shallow clone (`--depth 1`), README/docs read only, **zero execution**

---

## Executive Verdict

**Research-only. No Phase 3.0 scope change. No adoption.**

External repos provide **structural inspiration** for future Builder Kit specs (skill frontmatter, template taxonomy). They must **not** be installed, copied, or promoted into Agent-OS Lab.

---

## What Was Reviewed

Six GitHub repositories — see [../../external-repos-triage/repo-reviews/](../../external-repos-triage/repo-reviews/).

Commits: scientific-agent-skills `5bd00bf`, agentic-project-management `67b954d`, ruflo `60f37f2`, SuperClaude_Framework `226c45c`, claude-code-action `787c5a0`, claude-code-templates `a8f3752`.

---

## What Is Useful

1. **SKILL.md structure** (scientific-agent-skills) — agentskills.io alignment  
2. **Component taxonomy** (claude-code-templates) — agents/commands/hooks/MCP/skills  
3. **Security disclaimer culture** (scientific-agent-skills) — install selectively, scan skills  
4. **PM externalized state** (APM) — Spec/Plan/Rules, handoff  
5. **PR review checklists** (claude-code-action) — as MD bullets only  
6. **Command lifecycle grouping** (SuperClaude) — naming, not 30 commands  

---

## What Is Dangerous

1. **ruflo** — swarm, RAG, MCP, autopilot, init mutates workspace  
2. **Bulk template/skill install** — supply chain + permission sprawl  
3. **CI Claude Action** — unattended PR changes  
4. **Persona/mode frameworks** — replaces gates  
5. **apm-auto** — autonomous subagents without human shuttle  
6. **Runtime-before-specs** — `npx init` platforms  

---

## Phase 3.0 Influence

| Allowed | Forbidden |
|---------|-----------|
| Markdown spec field names | Any install command |
| Folder taxonomy ideas | Copied templates |
| Checklist inspiration | Runtime/MCP/hooks |

See [PHASE_3_IMPACT_REVIEW.md](PHASE_3_IMPACT_REVIEW.md).

---

## Repos Ranked by Usefulness (structure)

1. scientific-agent-skills  
2. claude-code-templates  
3. agentic-project-management  
4. claude-code-action (docs only)  
5. SuperClaude_Framework  
6. ruflo (negative reference)

## Repos Ranked by Risk

1. ruflo  
2. claude-code-templates (if installed)  
3. claude-code-action (if enabled)  
4. scientific-agent-skills (if mass-installed)  
5. SuperClaude_Framework  
6. agentic-project-management  

---

## Final Decision

| Item | Status |
|------|--------|
| Adopt | **No** |
| Install/execute | **No** |
| Phase 3 scope change | **No** |
| Proceed to Phase 3.0 specs | **Yes**, with [../PHASE_3_START_CONDITIONS.md](../PHASE_3_START_CONDITIONS.md) |

---

## Related artifacts

- [REPO_PRIORITY_MATRIX.md](REPO_PRIORITY_MATRIX.md)
- [DO_NOT_ADOPT_NOW.md](DO_NOT_ADOPT_NOW.md)
- [FUTURE_BACKLOG.md](FUTURE_BACKLOG.md)
- [FINAL_PHASE_2_10_REPORT.md](FINAL_PHASE_2_10_REPORT.md)
