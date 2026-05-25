# Click, Type, Swipe Abstractions

---

## Semantic Layer (What the Model Sees)

### v2 — Coordinate-centric

```
Tap (540, 1200)
Swipe (540, 1800), (540, 600)
Type (hello world)
```

- Coordinates in **absolute pixels** matching screenshot dimensions
- Swipe: two coordinate pairs (start, end)
- Type: only when keyboard flag true

### v3 — JSON semantic actions

```json
{"action": "click", "coordinate": [540, 1200]}
{"action": "swipe", "coordinate": [[540, 1800], [540, 600]]}
{"action": "type", "text": "hello world"}
{"action": "long_press", "coordinate": [540, 1200]}
{"action": "system_button", "button": "back"}
```

Richer than v2: long_press, system_button, open_app, answer.

### v3.5 — Normalized space

- GUI-Owl 1.5 outputs coords in **0–1000** range
- Runtime scales: `x_device = x_norm / 1000 * width`

Flag in v3: `--coor_type qwen-vl` for same mapping on older Qwen-VL models.

---

## Physical Layer (What the Device Executes)

| Abstraction | Mobile (ADB) | PC (pyautogui) | Web (Playwright) |
|-------------|--------------|----------------|------------------|
| click/tap | input tap | mouse click | element.click / page.mouse |
| long_press | swipe with duration | — | — |
| type | ADB Keyboard | write/typewrite | fill / keyboard.type |
| swipe/scroll | input swipe | scroll, drag | wheel, drag |
| back/home | keyevent | hotkey | browser.back |

---

## PC-Agent Extensions

Desktop adds:
- Window management via pywinauto (Windows)
- Clipboard paste via pyperclip for long text
- Subtask-level planning before low-level clicks

---

## Web (v3.5) Extensions

- Click by SOM index or coordinate
- Navigation: goto URL, new tab
- Form fill with Playwright locators
- `--use_css_som` for DOM-aware overlays

---

## Abstraction Gaps

| Gap | Impact |
|-----|--------|
| No unified `Action` type across platforms | Each runner reimplements parse + exec |
| Scroll vs swipe conflation | Model confusion on long pages |
| Multi-touch / pinch | Not in v2 contract |
| Drag-and-drop | OSWorld only (pyautogui drag) |
| Permission dialogs | No structured handling |

---

## Design Pattern for Reuse

**Two-layer action model:**
1. **Semantic action** — platform-agnostic (CLICK_TARGET, INPUT_TEXT, SCROLL_DIR)
2. **Driver adapter** — ADB / pyautogui / Playwright

MobileAgent mostly collapses layers in single-file runners; v3 JSON is closest to clean semantic layer.
