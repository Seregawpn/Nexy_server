# Task Brief: focus steal + pyobjc dlsym noise + TCC camera policy fix

## Request
Fix root causes from runtime logs: focus stealing on startup, PyObjC Foundation symbol noise, and repeated camera TCC policy errors.

## Implemented

1. Focus owner-path fix (startup)
- Updated `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/packaging/runtime_hook_pyobjc_fix.py`.
- Removed unconditional `app.activateIgnoringOtherApps_(True)` from runtime hook.
- Startup hook now only prepares `NSApplication` policy; foreground activation remains centralized in `main.py` via focus config.

2. PyObjC dlsym noise fix
- Updated:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/main.py`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/integration/utils/macos_pyobjc_fix.py`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/packaging/runtime_hook_pyobjc_fix.py`
- Replaced `hasattr(Foundation, symbol)` checks with direct AppKit symbol assignment (`getattr(AppKit, symbol, None)` -> `setattr(Foundation, ...)`).
- This avoids triggering Foundation `dlsym` lookups that spam logs with missing NSMake* symbols.

3. TCC camera policy alignment
- Updated `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/packaging/entitlements.plist`:
  - added `com.apple.security.device.camera=true`
- Updated `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/packaging/Nexy.spec`:
  - added `NSCameraUsageDescription`

## Validation
- `python3 -m py_compile main.py integration/utils/macos_pyobjc_fix.py packaging/runtime_hook_pyobjc_fix.py` -> OK
- grep checks confirm:
  - runtime hook no longer force-activates app
  - camera entitlement + usage description present

## Outcome
Single-owner startup focus policy is restored, PyObjC symbol noise path is reduced, and camera TCC policy is aligned with hardened runtime packaging.
