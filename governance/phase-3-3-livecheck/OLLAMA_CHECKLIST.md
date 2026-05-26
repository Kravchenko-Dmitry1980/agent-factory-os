# Ollama Checklist — Future Alternative Only

**Phase 3.3-LiveCheck did NOT use Ollama.**

---

## Status in this phase

| Item | Status |
|------|--------|
| Ollama used in live check | **No** |
| LM Studio used | **Yes** |
| Ollama documented for later | **Yes** |

Ollama remains a **future alternative** local OpenAI-compatible endpoint. Operators may use it in a later live check following the same policies (local only, synthetic data, explicit `--real-provider`, no cloud, no secrets in repo).

---

## Future Ollama setup (reference only — not executed)

1. Install Ollama manually (operator)
2. Pull model manually, e.g. `ollama pull qwen2.5:7b`
3. Ensure OpenAI-compatible API is available (default often `http://127.0.0.1:11434`)
4. Set environment:

```powershell
$env:RA_LLM_BASE_URL = "http://127.0.0.1:11434"
$env:RA_LLM_MODEL = "qwen2.5:7b"
```

5. Run same contract script:

```powershell
python evaluation/scripts/check_review_assistant_real_provider_contract.py --real-provider
```

---

## Same constraints apply

- Synthetic prompt only
- No cloud
- No API key in repo
- No provider framework
- Mock remains default without `--real-provider`
- Do not expose server to public network without intent

---

## When to use Ollama instead of LM Studio

Operator preference only. The project does not recommend one tool over another. Record endpoint URL, model id, and check results in a new live check report if Ollama is used in a future phase.
