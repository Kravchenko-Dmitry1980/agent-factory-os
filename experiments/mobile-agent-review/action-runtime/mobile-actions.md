# Mobile Actions — ADB Runtime

Исполнение действий на Android/Harmony через ADB.

---

## Controller Layer

| Version | File | Transport |
|---------|------|-----------|
| v1/v2/E | `controller.py` | ADB subprocess |
| v3 | `android_controller.py`, `harmonyos_controller.py` | ADB / HDC |
| v3.5 | `AdbTools` in `mobile_use/utils.py` | ADB shell |

---

## Primitive Operations

Typical mappings (conceptual):

| Intent | ADB pattern |
|--------|-------------|
| Tap | `input tap x y` |
| Swipe | `input swipe x1 y1 x2 y2 duration` |
| Text | ADB Keyboard broadcast / `input text` |
| Back | `input keyevent KEYCODE_BACK` |
| Home | `input keyevent KEYCODE_HOME` |
| Launch app | `monkey` / `am start` with package |

---

## ADB Keyboard Requirement

All READMEs require **ADB Keyboard APK**:
- Enables reliable Unicode text input
- User must switch IME to "ADB Keyboard"

Without it: `Type` actions fail silently or produce garbled input.

---

## Device Connection

Prerequisites documented:
1. Enable USB debugging (Developer Options)
2. HyperOS: extra "USB Debugging (Security Settings)"
3. `adb devices` shows authorized device
4. Windows: `adb.exe` path; Mac/Linux: chmod +x

HarmonyOS v3 path uses **HDC** instead of ADB (`--hdc_path`).

---

## Screenshot Capture

Part of action loop — typically:
```
adb exec-out screencap -p > screen.png
```

Timing: capture **after** action sleep (implicit delays in run loops).

---

## Platform Limits (Documented)

- **Supported:** Android, Harmony OS (≤4 for v2)
- **Not supported:** iOS
- Cloud alternative: Alibaba Wuying Cloud Phone (hosted Android)

---

## Security & Ops Notes

- ADB grants broad device control — equivalent to untrusted automation
- No permission prompt layer (contrast Claude Code `CanUseTool`)
- USB debugging exposes attack surface on dev devices

---

## Files

- `Mobile-Agent-v2/MobileAgent/controller.py`
- `Mobile-Agent-v3/mobile_v3/utils/android_controller.py`
- `Mobile-Agent-v3.5/mobile_use/utils.py` → class `AdbTools`
