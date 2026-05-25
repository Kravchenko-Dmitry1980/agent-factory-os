# Why Fail-Closed Matters

**Fail-closed** = when uncertain, **deny** — not "try anyway."

---

## Fail-open (dangerous)

- Missing approval → proceed
- GUI uncertain → click
- LLM timeout → use cache guess
- Parser error → default values

---

## Fail-closed (safe)

- Missing approval → deny
- Uncertainty → block or escalate
- Malformed input → reject
- Timeout → deny

---

## One sentence

Absence of proof of safety is treated as **unsafe**.

---

## Demo

```powershell
python prototypes/fail-closed-external-action/minimal-demo.py --scenario uncertain
```

Doctrine: `agent-os/doctrine/fail-closed-execution.md`
