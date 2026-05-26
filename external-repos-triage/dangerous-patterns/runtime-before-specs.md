# Dangerous Pattern: Runtime Before Specs

| Field | Value |
|-------|-------|
| **Source** | ruflo, claude-code-templates CLI |
| **Why tempting** | `npx init` instant platform |
| **Why dangerous** | Skips Builder Kit discipline |
| **Early signals** | agent-builder-kit skipped; .claude-flow added |
| **Mitigation** | PHASE_3_START_CONDITIONS |
| **Phase 3.0** | Specs only |
