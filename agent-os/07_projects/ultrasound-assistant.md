# Ultrasound Assistant

## Definition

**Ultrasound Assistant** is a project slot for a domain-specific clinical/educational agent — image workflow guidance, protocol checklists, and reference retrieval under strict verification harness.

## Key Ideas

- High-stakes domain → plan mode + verification agent mandatory.
- Reference memories for protocol URLs and equipment docs — not diagnostic conclusions in memory.
- MCP potential: PACS integrations, structured report tools (future).

## Architecture Implications

- Separate persona with constrained tool pool and explicit disclaimer injection.
- Episodic feedback for institution-specific protocols only.
- No autonomous mutations without human-in-loop permission mode.

## Production Implications

- Regulatory and liability constraints exceed generic coding agents.
- Audit trail via git-versioned memory and session logs.
- Fail-closed defaults on all write tools.

## Related Concepts

- [[verification]]
- [[execution-verification]]
- [[memory-taxonomy]]

## Sources

- Agent-OS project registry (placeholder)

## My Notes

