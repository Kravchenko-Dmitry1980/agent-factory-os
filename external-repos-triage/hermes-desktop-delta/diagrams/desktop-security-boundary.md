# Desktop Security Boundary

```mermaid
flowchart TB
  subgraph Untrusted["Untrusted"]
    Renderer[React Renderer]
    Markdown[User Markdown / Chat]
    WebView[Webviews]
  end

  subgraph Bridge["IPC Bridge"]
    Preload[Sandboxed Preload]
  end

  subgraph Trusted["Trusted — High Risk"]
    Main[Electron Main]
    FS[Filesystem ~/.hermes]
    Spawn[Spawn Hermes CLI]
    Secrets[API Keys / OAuth]
    Installer[Install Script]
  end

  Renderer --> Preload
  Markdown --> Renderer
  WebView --> Renderer
  Preload -->|"IPC allowlist"| Main
  Main --> FS
  Main --> Spawn
  Main --> Secrets
  Main --> Installer
```

**Hermes mitigations (observed):** contextIsolation, sandbox, navigation allowlists.

**Agent-OS stance:** defer Electron until checklist satisfied; prefer read-only console MVP.
