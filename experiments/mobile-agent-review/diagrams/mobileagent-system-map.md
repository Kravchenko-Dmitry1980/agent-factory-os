# MobileAgent System Map — Diagram

```mermaid
flowchart TB
    subgraph user [User Layer]
        U[Natural language instruction]
        H[add_info hints]
    end

    subgraph orch [Orchestration Layer]
        MA3M[Manager v3]
        MA3E[Executor v3]
        MA3R[Reflector v3]
        MA3N[Notetaker v3]
        V2P[v2 Prompt Roles]
        OWL[GUI-Owl 1.5 E2E]
    end

    subgraph model [Model Layer]
        GPT[GPT-4 / Qwen-VL API]
        GO7[GUI-Owl 7B/32B]
        GO15[GUI-Owl 1.5 family]
        CRIT[GUI-Critic-R1]
    end

    subgraph perceive [Perception Layer]
        OCR[ModelScope OCR]
        DINO[GroundingDINO]
        SOM[SOM overlays]
        A11Y[Accessibility tree]
    end

    subgraph act [Action Layer]
        ADB[ADB / HDC]
        PY[pyautogui]
        PW[Playwright]
    end

    subgraph env [Environment]
        PH[Physical Android]
        PC[Desktop OS]
        BR[Browser]
        EMU[Emulators OSWorld/AndroidWorld]
    end

    U --> orch
    H --> orch
    orch --> model
    model --> orch
    perceive --> orch
    orch --> act
    act --> env
    env --> perceive
    CRIT -.->|pre-op offline| orch

    GO7 --> GO15
    GPT --> GO7
```

## Subproject Mapping

| Box | Repo path |
|-----|-----------|
| v2 Prompt Roles | `Mobile-Agent-v2/` |
| MA3 classes | `Mobile-Agent-v3/mobile_v3/` |
| GUI-Owl 1.5 | `Mobile-Agent-v3.5/` |
| OCR/DINO | v1/v2/E/PC |
| Benchmarks | `os_world_v3/`, `android_world_v3*`, `web_benchmark/` |
| GUI-Critic | `GUI-Critic-R1/` |
| UI-S1 training | `UI-S1/` (dashed — not runtime) |
