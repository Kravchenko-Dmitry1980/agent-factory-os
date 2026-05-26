# Local Endpoint Manual Setup

Phase 3.3-LiveCheck — how the local provider was configured.

---

## What is a local OpenAI-compatible endpoint?

A **local server running on the same machine** that accepts HTTP requests in OpenAI Chat Completions shape:

- `POST /v1/chat/completions` (or equivalent path on the local tool)
- JSON body with `model`, `messages`, optional `temperature`
- JSON response with `choices[].message.content`

Examples: LM Studio Local Server, Ollama with OpenAI shim, vLLM, llama.cpp server.

The Review Assistant Thin boundary reads:

- `RA_LLM_BASE_URL` — base URL (e.g. `http://127.0.0.1:1234`)
- `RA_LLM_MODEL` — model id string (optional but recommended)
- `RA_LLM_API_KEY` — optional; not used in this phase

Real mode activates only with `--real-provider` on the demo or contract script.

---

## What was used in this phase

| Setting | Value |
|---------|-------|
| Tool | **LM Studio** |
| URL | `http://127.0.0.1:1234` |
| Model | `qwen2.5-7b-instruct-1m` |
| API key | none |
| Cloud | no |

PowerShell environment used for live check:

```powershell
$env:RA_LLM_BASE_URL = "http://127.0.0.1:1234"
$env:RA_LLM_MODEL = "qwen2.5-7b-instruct-1m"
```

---

## What the project did NOT do

| Action | Status |
|--------|--------|
| Install LM Studio | **No** — operator responsibility |
| Download model automatically | **No** |
| Start server automatically | **No** |
| Store API key in repo | **No** |
| Call cloud provider (OpenAI, Anthropic, RU providers) | **No** |
| Send private / project / repo data | **No** |
| Create `.env` file | **No** |
| Add provider framework, runtime, or factory | **No** |
| Change implementation code in LiveCheck phase | **No** |

---

## Operator responsibilities

1. Install and open LM Studio (or alternative) manually
2. Download and load model manually
3. Enable Local Server on expected port
4. Set env vars in the shell session
5. Run contract script with `--real-provider`
6. Stop server when finished; do not expose to LAN without intent

---

## Verification

After setup, confirm endpoint responds (optional manual probe):

```powershell
# Optional — not required by project scripts
Invoke-WebRequest -Uri "http://127.0.0.1:1234/v1/models" -Method GET
```

Then run:

```powershell
python evaluation/scripts/check_review_assistant_real_provider_contract.py --real-provider
```

Expected: `Summary: PASS=3 FAIL=0`
