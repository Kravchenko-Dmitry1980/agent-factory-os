# Review Loop Agent

**Purpose:** Validate critique limitations, review gates, HITL approval, verification-first publishing.

## Flow

```
task → draft → critique → human review → approve/reject → publish (or stop)
```

## Key Lessons

1. **Critic ≠ truth** — critique is a filter, not verification
2. **Human review mandatory** — no publish without explicit human approval
3. **Fail-closed on uncertainty** — ambiguous critique blocks forward progress

## Run

```powershell
python prototypes/review-loop-agent/minimal-demo.py
python prototypes/review-loop-agent/minimal-demo.py --scenario uncertain-critic
python prototypes/review-loop-agent/minimal-demo.py --scenario bypass-attempt
```

## Doctrine Links

- `Books/swarm-playbooks/patterns/critique-before-publish.md`
- `agent-os/08_patterns/verification-before-writeback.md`
- `Books/swarm-playbooks/anti-patterns/critic-as-fake-verification.md`

## Files

| File | Content |
|------|---------|
| [architecture.md](architecture.md) | Component boundaries |
| [contracts.md](contracts.md) | I/O and gates |
| [failure-modes.md](failure-modes.md) | Known failures |
| [governance.md](governance.md) | HITL and fail-closed rules |
| [sequence-diagram.md](sequence-diagram.md) | Mermaid sequence |
| [minimal-demo.py](minimal-demo.py) | Runnable demo |
