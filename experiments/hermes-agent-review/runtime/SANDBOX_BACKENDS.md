# Sandbox Backends

**Code:** `tools/environments/`, `tools/terminal_tool.py`  
**Config:** `terminal.backend` in `~/.hermes/config.yaml`

---

## Seven Terminal Backends

| Backend | Isolation | Persistence | Cost Model |
|---------|-----------|-------------|------------|
| **local** | None (host shell) | Host filesystem | Free |
| **docker** | Container | Container volumes | Local compute |
| **ssh** | Remote machine | Remote filesystem | Remote compute |
| **singularity** | HPC container | Container | Cluster allocation |
| **modal** | Serverless | Hibernates idle | Pay per use |
| **daytona** | Serverless dev env | Hibernates idle | Pay per use |
| **vercel** | Vercel Sandbox | Ephemeral | Pay per use |

---

## Backend Selection

```yaml
terminal:
  backend: docker
  docker:
    image: "ubuntu:22.04"
    # ... docker-specific config
  
  # OR
  backend: modal
  modal:
    # ... modal-specific config
```

Subagents inherit parent's backend unless overridden.

---

## Serverless Persistence Pattern

Modal and Daytona offer **hibernate-on-idle**:

```
Agent session active → sandbox running → costs compute
Agent idle → sandbox hibernates → minimal cost
New request → sandbox wakes → resumes environment
```

Enables "$5 VPS equivalent" on cloud without always-on costs.

---

## Environment Passthrough

**Code:** `tools/env_passthrough.py`, `tools/credential_files.py`

- Env vars passed to sandbox
- Credential files mounted
- Configurable per-backend

---

## Browser Backends (5)

Separate from terminal — `tools/browser_tool.py`:

| Backend | Purpose |
|---------|---------|
| Local Playwright | Direct browser control |
| Browser Use (cloud) | Cloud browser via Nous Portal |
| agent-browser | Node-based browser |
| Others | Per config |

---

## execute_code RPC

**Code:** `tools/code_execution_tool.py`

Python scripts that call Hermes tools via RPC:
- Collapse multi-step pipelines into single turn
- Zero context cost for intermediate steps
- Runs in selected sandbox backend

---

## Security Model

| Backend | Trust Model |
|---------|-------------|
| local | Full host access — user responsibility |
| docker | Container isolation |
| ssh | Remote machine trust |
| serverless | Provider isolation |

**Approval system:** `tools/approval.py` detects dangerous commands regardless of backend.

---

## Agent-OS Relevance

Pattern for harness environment modeling:
- Pluggable execution backends
- Serverless hibernate pattern
- Env/credential passthrough
- Backend inheritance in subagents
