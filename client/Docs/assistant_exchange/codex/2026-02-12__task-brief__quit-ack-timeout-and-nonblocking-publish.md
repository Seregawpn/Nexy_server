# Quit ACK Timeout + Non-Blocking Publish

## Goal
Убрать таймаутный срыв quit-intent при выходе из tray под нагрузкой.

## Implemented

1. `TrayController` quit ACK timeout increased:
- File: `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/modules/tray_controller/core/tray_controller.py`
- Change:
  - Added `self._quit_dispatch_timeout_sec = 1.5`
  - `_dispatch_quit_clicked_with_ack()` now uses configurable timeout (`1.5s`).

2. `TrayControllerIntegration._on_tray_quit` made non-blocking:
- File: `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/integration/integrations/tray_controller_integration.py`
- Change:
  - Keeps immediate SoT update: `USER_QUIT_INTENT=True`
  - Replaced blocking `await event_bus.publish("tray.quit_clicked", ...)`
    with fire-and-forget publish task.

## Why
- Previous behavior timed out at `0.35s` during startup/playback load.
- Fast `quit()` happened before observable centralized quit chain.
- New behavior preserves architecture:
  - owner remains coordinator/event bus,
  - tray sends intent quickly and does not block on full subscriber traversal.

## Tests
- Updated: `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/tests/test_tray_quit_dispatch.py`
  - timeout assertion updated to `1.5`.
- Added: `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/tests/test_tray_quit_integration_ack.py`
  - verifies `_on_tray_quit` returns quickly while publish is slow.
- Re-ran:
  - `PYTHONPATH=. pytest -q tests/test_tray_quit_dispatch.py tests/test_tray_quit_integration_ack.py tests/test_user_quit_ack.py`
  - Result: `8 passed`.
