# Permission Modes

## Definition

**Permission modes** are named harness policies that resolve every tool authorization decision through a single mode-based chain — replacing scattered per-tool allow checks.

## Key Ideas

| Mode | Behavior |
|------|----------|
| bypassPermissions | Allow all (internal only) |
| dontAsk | Allow all, logged, no prompts |
| auto | LLM classifier decides |
| acceptEdits | Auto-allow file edits; prompt others |
| default | Interactive prompt per mutation |
| plan | Read-only; deny writes |
| bubble | Subagent escalates to parent |

## Architecture Implications

- Resolution: hook rule → tool.checkPermissions → mode → user prompt/classifier.
- Rules: alwaysAllow, alwaysDeny, alwaysAsk with content patterns (`Bash(git *)`).
- Bubble prevents headless subagents from self-approving destructive ops.

## Production Implications

- Reason about security by active mode, not by reading every tool.
- Plan mode for exploration; default for execution; auto for semi-autonomous workflows.
- Session trust dialog separate from permission mode — environment trust boundary.

## Related Concepts

- [[adaptive-harness]]
- [[harness-mechanisms]]
- [[planning]]
- [[subagents]]

## Sources

- `Books/claude/ch01-architecture.md`
- `Books/claude/ch06-tools.md`

## My Notes

