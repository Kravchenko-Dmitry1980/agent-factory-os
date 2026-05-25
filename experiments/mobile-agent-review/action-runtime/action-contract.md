# Action Contract

Формальный и фактический контракт между **reasoning layer** и **execution layer** в MobileAgent.

---

## v2 Natural Language Contract

Six atomic actions in `get_action_prompt()`:

| Action | Syntax | Preconditions |
|--------|--------|---------------|
| Open app | `Open app (name)` | Desktop visible |
| Tap | `Tap (x, y)` | Valid pixel coords |
| Swipe | `Swipe (x1,y1), (x2,y2)` | — |
| Type | `Type (text)` | Keyboard activated |
| Home | `Home` | — |
| Stop | `Stop` | Task complete |

**Output format (required):**
```
### Thought ###
### Action ###
### Operation ###
```

Parser in `run.py` extracts `Action` line → dispatches to `controller.py`.

---

## v3 JSON Contract (Mobile)

Executor returns structured dict (parsed in `mobile_agent_e.py`):

| Field | Types |
|-------|-------|
| `action` | click, long_press, type, swipe, system_button, open_app, answer, terminate, … |
| `coordinate` | [x, y] or two points for swipe |
| `text` | for type/answer |
| `button` | back, home, enter (system_button) |
| `app_name` | for open_app |

Validated then mapped to ADB/HDC commands in `android_controller.py`.

---

## v3 OSWorld pyautogui Contract

Executor emits Python-like calls:
- `click`, `type`, `hotkey`, `scroll`, `drag`, …

Compiled and `exec()`'d in VM context — different surface from mobile JSON.

---

## v3.5 GUI-Owl 1.5

Model output parsed in `utils.py` wrappers — typically function-call or JSON-like action strings.

Coordinates: **0–1000 normalized** by default → scaled to device resolution in `AdbTools`.

---

## Cross-Cutting Rules

1. **One action per step** — v2 explicitly "perform just one action"
2. **Gated typing** — keyboard must be active (v2) or implicit in JSON type (v3)
3. **Explicit termination** — Stop / terminate / answer for Q&A tasks
4. **Hints channel** — `add_info` / `additional_knowledge_*` injected per role

---

## Contract Stability Issues

- v2: free-form Action line → regex parsing fragility
- v3: JSON in LLM text → needs robust `parse_response`
- Coordinate system varies by model (--coor_type flag)
- No unified action schema across mobile/PC/web in one module

---

## Agent-OS Mapping (Future)

Potential canonical action envelope:

```yaml
action_id: uuid
kind: tap | type | swipe | navigate | answer | stop
target: {x, y} | element_ref | app_id
payload: {text, direction, keys}
coord_space: pixel | normalized_1000
preconditions: [keyboard_active]
```

MobileAgent provides **reference implementations**, not a shared schema file.
