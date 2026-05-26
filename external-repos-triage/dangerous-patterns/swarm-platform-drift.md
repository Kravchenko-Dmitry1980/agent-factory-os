# Dangerous Pattern: Swarm Platform Drift

| Field | Value |
|-------|-------|
| **Source** | ruflo (primary), SuperClaude, APM apm-auto |
| **Why tempting** | «100 agents», faster delivery |
| **Why dangerous** | Hides gates; scales errors; conflicts with Learning Lab |
| **Early signals** | shared runtime, swarm_init, autopilot |
| **Mitigation** | phase-2-8 DO_NOT_BUILD; one demo one gate |
| **Phase 3.0** | **Forbidden** |
