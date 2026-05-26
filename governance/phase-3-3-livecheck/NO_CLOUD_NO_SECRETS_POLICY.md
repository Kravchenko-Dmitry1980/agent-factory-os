# No Cloud / No Secrets Policy

Phase 3.3-LiveCheck safety policy for local real provider validation.

---

## Endpoint policy

| Rule | Phase 3.3-LiveCheck |
|------|---------------------|
| Local endpoint only | **Yes** — `http://127.0.0.1:1234` |
| OpenAI cloud | **No** |
| Anthropic cloud | **No** |
| Russian cloud providers (GigaChat, YandexGPT, etc.) | **No** |
| Remote hosted inference without operator control | **No** |

---

## Secrets policy

| Rule | Phase 3.3-LiveCheck |
|------|---------------------|
| API key used | **No** |
| API key in repo | **No** |
| `.env` file created | **No** |
| Secrets in prompts | **No** |
| Secrets in logs or traces | **No** |
| Env var values printed | **No** |

Optional `RA_LLM_API_KEY` exists for tools that require a dummy key locally; this phase did not set it.

---

## Data policy

| Rule | Phase 3.3-LiveCheck |
|------|---------------------|
| Synthetic data only | **Yes** — hardcoded scenario prompt |
| Real client data | **No** |
| Project / repo content in prompt | **No** |
| Private or medical data | **No** |
| Operator chat pasted into scenario | **No** |

---

## Network exposure policy

| Rule | Phase 3.3-LiveCheck |
|------|---------------------|
| Bind to localhost | Expected operator practice |
| Expose server to LAN/WAN | **Do not** without explicit intent |
| Automated outbound cloud calls from scripts | **No** — mock default |

---

## Architecture policy

| Rule | Phase 3.3-LiveCheck |
|------|---------------------|
| Provider framework | **Not created** |
| Provider router / registry | **Not created** |
| Runtime orchestration | **Not created** |
| Factory pattern | **Not created** |
| Second agent / RAG / MCP | **Not created** |

---

## Verification

Live check PASS with this policy means:

- Contract script reached localhost only when `--real-provider` set
- No-network checks still PASS without env configuration
- Documentation records compliance; no code changes in LiveCheck phase

---

## Operator reminder

Before any future live run:

1. Confirm synthetic scenario only
2. Confirm no API key in shell history committed to repo
3. Confirm LM Studio not exposed beyond local machine
4. Stop server when done
