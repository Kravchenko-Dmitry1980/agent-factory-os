# GUI as Environment

Паттерн: графический интерфейс моделируется как **среда** с observations и actions, аналогично RL env.

---

## Formal View

```
Env = (S, A, T, O)
  S — UI states (screen configurations)
  A — {tap, type, swipe, navigate, ...}
  T — transition via device driver
  O — observation (screenshot ± structured UI list)
```

MobileAgent implements this implicitly, not via gym API (except benchmark forks).

---

## Observation Space

| Version | Observation |
|---------|-------------|
| v1/v2 | Image + derived element list + keyboard flag |
| v3+ | Image (+ optional a11y tree in OSWorld) |
| Benchmarks | Env-provided state + reward |

---

## Action Space

Discrete semantic actions mapped to low-level motor commands.

UI-S1 defines explicit action spaces in `x/data/agent/space/`:
- `android_world.py`
- `computer_thought.py`
- `std_space.py`

Training-oriented formalization of the same idea.

---

## Reward Signal

- **Training (UI-S1):** RL reward from semi-online rollouts
- **Inline agent:** Reflection A/B/C as dense shaping signal
- **Benchmark:** Sparse task success at episode end

---

## Why It Matters for Agent-OS

Code-centric agents treat **filesystem + shell** as environment.

GUI agents add **pixel observation space** — different:
- Non-markovian without memory (same screen, different internal state)
- Partial observability (modals, overlays)
- Stochastic transitions (network loading)

Agent-OS `06_digital-twins/` could model GUI env as twin surface.

---

## Source References

- Mobile-Agent v1 paper: "Autonomous Multi-Modal Mobile Device Agent"
- UI-S1 action space modules
- AndroidWorld env integration in v3 eval trees
