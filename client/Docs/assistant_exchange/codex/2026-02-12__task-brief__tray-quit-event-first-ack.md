# Tray Quit Event-First ACK Fix

## Goal
Убрать гонку между `quit_clicked` и фактическим `quit()` при выходе из tray.

## Changes
- Updated `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/modules/tray_controller/core/tray_controller.py`:
  - Added `_dispatch_quit_clicked_with_ack()`.
  - `TrayController._on_quit_clicked()` now:
    1) synchronously dispatches `quit_clicked` to owner loop with timeout `0.35s`,
    2) only then calls `tray_menu.quit()`.
  - Timeout/error paths are non-fatal and still proceed to quit.

## Why this fits architecture
- Source of truth remains centralized in coordinator/event bus.
- Tray layer now acts as initiator and no longer races ahead of event dispatch.
- No new ownership paths and no duplicate shutdown owners were introduced.

## Tests
- Added `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/tests/test_tray_quit_dispatch.py`:
  - `test_quit_click_waits_for_dispatch_ack_before_quit`
  - `test_quit_click_continues_when_dispatch_timeout`
- Existing guard tests kept green:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/tests/test_user_quit_ack.py`

## Validation Result
- Command:
  - `PYTHONPATH=. pytest -q tests/test_tray_quit_dispatch.py tests/test_user_quit_ack.py`
- Result:
  - `7 passed`

## Expected runtime log improvement
In latest session window after quit:
- should now appear `tray.quit_clicked` dispatch/publish before process exit,
- then coordinator quit ack path (`[QUIT_ACK]`) becomes observable more consistently.
