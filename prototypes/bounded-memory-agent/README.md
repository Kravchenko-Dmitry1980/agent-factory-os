# Bounded Memory Agent

**Purpose:** Validate frozen snapshots, memory limits, memory-aware execution, and memory failure modes.

## Features

- Max memory size (character budget)
- Snapshot creation at session start
- No uncontrolled writeback (verification required)
- Explicit context loading
- Memory reset policy

## Run

```powershell
python prototypes/bounded-memory-agent/minimal-demo.py
python prototypes/bounded-memory-agent/minimal-demo.py --scenario overflow
python prototypes/bounded-memory-agent/minimal-demo.py --scenario unverified-writeback
```

## Doctrine Links

- `agent-os/02_memory/frozen-memory-snapshot.md`
- `agent-os/08_patterns/verification-before-writeback.md`
- `agent-os/09_antipatterns/unbounded-memory-growth.md`
