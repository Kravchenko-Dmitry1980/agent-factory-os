# GUI Agent Loop — Diagram

```mermaid
flowchart TD
    Start([User instruction]) --> Cap[Capture screenshot]
    Cap --> Per{Perception mode}
    Per -->|v1/v2| OCR[OCR + icon list]
    Per -->|v3+| VLM[Raw image to VLM]
    OCR --> Ctx[Build context]
    VLM --> Ctx
    Ctx --> Plan{Multi-agent?}
    Plan -->|v2/v3| M[Manager / Progress]
    Plan -->|v1/v3.5 E2E| Act
    M --> Act[Reason → Action]
    Act --> Parse[Parse action]
    Parse --> Exec[Execute ADB / pyautogui / Playwright]
    Exec --> Cap2[Capture after screenshot]
    Cap2 --> Ver{Verification}
    Ver -->|Reflect| ABC{A/B/C?}
    ABC -->|A| Mem[Update memory / progress]
    ABC -->|B/C| Err[Set error_flag]
    Err --> M
    Mem --> Done{Stop?}
    Done -->|No| Cap
    Done -->|Yes| End([Finished])
```

## Legend

- **A** — success, continue
- **B** — wrong page, often back
- **C** — no change, retry

## Version Notes

- v2: Plan box = Progress agent output, not Manager class
- v3.5 mobile: Plan/Reflect boxes often collapsed into single VLM
- GUI-Critic pre-check not shown (optional pre-op path)
