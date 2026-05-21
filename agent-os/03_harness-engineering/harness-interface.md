# Harness Interface

## Definition

The **harness interface** is the contract between the LLM and the runtime: tools, permissions, hooks, messages, and termination — everything the model can observe and invoke, bounded by harness policy.

## Key Ideas

- Model sees: system prompt, tools (schemas), message history, tool results.
- Model does not control: permission modes, hook decisions, compaction, circuit breakers.
- Tool schema is the model's instruction manual — dynamic schema omits unusable fields.
- Attachments carry volatile content outside cached tool definitions.

## Architecture Implications

- Self-describing tools declare concurrency, permissions, rendering locally.
- `canUseTool` function injected into loop params — permission layer seam.
- Feature-gated schema fields removed at compile/runtime so model cannot misuse them.

## Production Implications

- ~10.2% fleet cache_creation from dynamic tool descriptions — move lists to attachments.
- MCP tools indistinguishable from built-ins after wrapping — uniform harness surface.
- SDK vs REPL differ in UI callbacks, not core harness contract.

## Related Concepts

- [[harness]]
- [[harness-mechanisms]]
- [[self-describing-tools]]
- [[permission-modes]]

## Sources

- `Books/claude/ch01-architecture.md`
- `Books/claude/ch06-tools.md`
- `Books/claude/ch08-sub-agents.md`

## My Notes

