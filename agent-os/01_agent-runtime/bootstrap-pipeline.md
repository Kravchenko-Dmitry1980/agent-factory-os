# Bootstrap Pipeline

## Definition

The **bootstrap pipeline** initializes a production agent CLI in under ~300ms: validate environment, establish trust, register capabilities, render UI — via phased narrowing and parallel I/O.

## Key Ideas

- Five files: `cli.tsx` → `main.tsx` → `init.ts` → `setup.ts` → `replLauncher.ts`
- Fast-path dispatch: `--version`, `--help`, MCP list exit before heavy imports.
- Module-level I/O: keychain and MDM promises fire during import evaluation.
- Trust boundary: pre-trust safe ops only; post-trust reads PATH, LD_PRELOAD, git.

## Architecture Implications

- `init()` memoized — idempotent across entry points.
- Hook config frozen into immutable snapshot at setup.
- Seven launch paths converge on same `query()` loop.

## Production Implications

- ~240ms warm start, ~60ms headroom under 300ms budget.
- Dynamic imports defer OpenTelemetry (400KB+) until needed.
- Capture argv prompt before async work to prevent dropped user input.

## Related Concepts

- [[agent-vs-cli]]
- [[stateful-systems]]
- [[query-loop]]

## Sources

- `Books/claude/ch02-bootstrap.md`

## My Notes

