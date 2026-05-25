# Mobile-Agent Family — Version Map

---

## Family Tree

```mermaid
flowchart TB
    subgraph models [Foundation Models]
        QwenVL[Qwen-VL series]
        GUIOwl[GUI-Owl 7B/32B]
        GUIOwl15[GUI-Owl 1.5 family]
    end

    subgraph agents [Agent Frameworks]
        V1[Mobile-Agent-v1<br/>Single agent]
        V2[Mobile-Agent-v2<br/>Multi-prompt]
        V3[Mobile-Agent-v3<br/>Multi-class + GUI-Owl]
        V35[Mobile-Agent-v3.5<br/>E2E GUI-Owl 1.5]
        PC[PC-Agent]
        MAE[Mobile-Agent-E]
    end

    subgraph research [Research Modules]
        Critic[GUI-Critic-R1]
        UIS1[UI-S1 RL]
    end

    V1 --> V2
    V2 --> V3
    V3 --> V35
    QwenVL --> V1
    QwenVL --> V2
    QwenVL --> PC
    GUIOwl --> V3
    GUIOwl15 --> V35
    V2 --> PC
    V2 --> MAE
    V3 -.-> Critic
    V35 -.-> Critic
    GUIOwl --> UIS1
```

---

## Version Cheat Sheet

| Version | Venue | Agent structure | Primary model | Platforms |
|---------|-------|-----------------|---------------|-----------|
| v1 | ICLR 2024 WS | Single operator | GPT-4 + Qwen-VL caption | Android |
| v2 | NeurIPS 2024 | 4 prompt roles | GPT-4o + perception | Android, Harmony |
| v3 | Preprint 2025 | 4 Python agent classes | GUI-Owl + vLLM | Android, OSWorld eval |
| v3.5 | Preprint 2026 | E2E VLM (+ model roles) | GUI-Owl 1.5 | Mobile, PC, browser |
| PC-Agent | ICLR 2025 WS | 5 prompt roles | Qwen-VL | Windows/Mac desktop |
| Mobile-Agent-E | Preprint 2025 | Multi + experience | Qwen + perception | Android |
| GUI-Critic-R1 | NeurIPS 2025 | Offline critic | Qwen2.5-VL | Mobile/desktop/web datasets |
| UI-S1 | ACL 2026 | RL training | Qwen GUI + VERL | Training envs |

---

## Capability Progression

### Navigation & planning
- **v1:** Implicit in single-thread reasoning
- **v2:** Progress agent tracks `completed_content`
- **v3:** Manager maintains plan + subgoals + replan on stuck
- **v3.5:** Native long-horizon memory in model; MemGUI-Bench leader claim

### Visual grounding
- **v1/v2:** External OCR + DINO + coordinate lists in prompt
- **v3:** GUI-Owl end-to-end + optional Grounding module (OSWorld)
- **v3.5:** Native grounding benchmarks (ScreenSpot, OSWorld-G)

### Tool use / MCP
- **v1–v3:** GUI actions only in open-source loops
- **v3.5:** Native tool & MCP calling (OSWorld-MCP, Mobile-World SOTA claims)

### Self-improvement
- **Mobile-Agent-E:** Experience reflector/retriever for shortcuts and tips
- **UI-S1:** Semi-online RL for policy improvement (training, not runtime)

### Error diagnosis
- **v2+:** Post-action reflection (A/B/C)
- **GUI-Critic-R1:** Pre-action critic (not integrated in main loops)

---

## Which Version to Study for What

| Research question | Best starting point |
|-------------------|---------------------|
| GUI as environment + ADB contract | v2 `run.py` + `prompt.py` |
| Multi-agent coordination + InfoPool | v3 `mobile_agent_e.py` |
| Native VLM GUI agent | v3.5 `mobile_use/utils.py` |
| Desktop automation | PC-Agent `run.py` |
| Benchmark integration | v3 `os_world_v3/`, `android_world_v3/` |
| Action verification theory | GUI-Critic-R1 + v2 reflect prompts |
| Training GUI policies | UI-S1 |

---

## External Ecosystem

- **ToolCUA** (separate repo) — GUI vs tool path orchestration
- **OSWorld-MCP** — MCP benchmark
- **MobileWorld** — mobile tool+MCP benchmark
- **Wuying Cloud Phone/Desktop** — hosted demos without local deploy

---

## Research Workspace Note

Only `source/MobileAgent/` is cloned. Related repos (ToolCUA, OSWorld-MCP, MobileWorld) are referenced in README but **not ingested** in this experiment.
