# Possible MCP Tool Contracts

Гипотетические MCP tools, inspired by MobileAgent capabilities — **not implemented**.

For future Agent-OS / digital twin integration design.

---

## Device Observation Tools

```json
{
  "name": "gui_capture_screenshot",
  "description": "Capture current screen from connected device or emulator",
  "inputSchema": {
    "type": "object",
    "properties": {
      "device_id": {"type": "string"},
      "platform": {"enum": ["android", "desktop", "browser"]}
    }
  }
}
```

```json
{
  "name": "gui_get_accessibility_tree",
  "description": "Return structured UI tree when available (OSWorld/AndroidWorld)"
}
```

---

## Perception Tools (Legacy Pipeline)

```json
{
  "name": "gui_extract_clickable_elements",
  "description": "OCR + icon detection → list of {coordinates, label}",
  "inputSchema": {
    "properties": {
      "image_path": {"type": "string"},
      "merge_strategy": {"enum": ["default", "som"]}
    }
  }
}
```

Maps to v1/v2 perception stack as optional **tool** instead of inline code.

---

## Action Tools

```json
{
  "name": "gui_execute_action",
  "inputSchema": {
    "type": "object",
    "properties": {
      "kind": {"enum": ["tap", "swipe", "type", "back", "home", "open_app"]},
      "coordinate": {"type": "array"},
      "coord_space": {"enum": ["pixel", "normalized_1000"]},
      "text": {"type": "string"}
    },
    "required": ["kind"]
  }
}
```

Adapter layer routes to ADB / pyautogui / Playwright.

---

## Verification Tools

```json
{
  "name": "gui_verify_action_delta",
  "description": "Compare before/after screenshots, return A/B/C outcome",
  "inputSchema": {
    "properties": {
      "before_image": {"type": "string"},
      "after_image": {"type": "string"},
      "expected_change": {"type": "string"}
    }
  }
}
```

```json
{
  "name": "gui_critic_pre_check",
  "description": "Run GUI-Critic-style pre-operative diagnosis",
  "inputSchema": {
    "properties": {
      "screenshot": {"type": "string"},
      "proposed_action": {"type": "object"}
    }
  }
}
```

---

## Memory Tools

```json
{
  "name": "gui_notetaker_append",
  "description": "Store fact extracted from current screen for later steps"
}
```

```json
{
  "name": "gui_progress_update",
  "description": "Update completed subgoals for planner consumption"
}
```

---

## Hybrid Routing Tool

```json
{
  "name": "agent_route_modality",
  "description": "Decide GUI action vs external MCP tool (ToolCUA / OSWorld-MCP pattern)",
  "inputSchema": {
    "properties": {
      "task_context": {"type": "string"},
      "available_tools": {"type": "array"}
    }
  }
}
```

---

## Design Principles

1. **Separate observe / act / verify** — mirrors MobileAgent loop
2. **Coord space in schema** — avoid Qwen-vs-absolute bugs
3. **Platform adapter behind one contract** — unified harness interface (cf. Code as Agent Harness ch02)
4. **Pre + post verification tools** — GUI-Critic + Reflector

---

## Status

Speculative. Requires:
- MCP server implementation
- Permission model for destructive GUI actions
- Digital twin state sync

Remain in `experiments/mobile-agent-review/` until Agent-OS GUI track is chartered.
