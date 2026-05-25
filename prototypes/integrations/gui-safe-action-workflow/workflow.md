# GUI Safe Action — Workflow

1. **Observe** — read mock screen state
2. **Propose** — plan click with expected next screen
3. **Visual verify** — A/B/C outcome on simulated post-state
4. **Approval gate** — high-risk clicks require human approval
5. **Execute or reject** — only A + approved executes

Deny-by-default on B, C, uncertain, or missing approval.
