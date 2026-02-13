# Quit Dispatch Loop Preserve Fix

## Problem
Даже после увеличения timeout до `1.5s` в runtime оставался:
- `quit_clicked dispatch timed out ... proceeding with quit`.

## Root Cause
`TrayControllerIntegration` заранее ставил owner loop через `set_dispatch_loop(event_bus_loop)`,  
но `TrayController.initialize()` перезаписывал его на текущий loop и ломал маршрутизацию quit dispatch.

## Fix
- File: `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/modules/tray_controller/core/tray_controller.py`
  - `initialize()` now sets fallback loop **only if** `_dispatch_loop is None`.

## Tests
- Updated: `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/tests/test_tray_quit_dispatch.py`
  - added `test_initialize_does_not_override_preconfigured_dispatch_loop`.
- Existing quit tests kept:
  - `tests/test_tray_quit_integration_ack.py`
  - `tests/test_user_quit_ack.py`
- Command:
  - `PYTHONPATH=. pytest -q tests/test_tray_quit_dispatch.py tests/test_tray_quit_integration_ack.py tests/test_user_quit_ack.py`
- Result:
  - `9 passed`.
