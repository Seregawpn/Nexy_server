# Task Brief: Focus single-owner + quit/restart guard

## Goal
Устранить симптомы "Spotlight/menu исчезают" и "после Quit приложение снова запускается" без реархитектуры.

## Changes
- Centralized forced app activation to one owner path:
  - kept only startup activation in `main.py`
  - removed forced `activateIgnoringOtherApps_(True)` from:
    - `modules/tray_controller/core/tray_controller.py`
    - `modules/tray_controller/macos/menu_handler.py`
- Added explicit user quit intent state:
  - `integration/core/state_keys.py`: `USER_QUIT_INTENT`
  - `integration/core/simple_module_coordinator.py`:
    - reset to `False` at init
    - set to `True` on tray quit event
- Added restart suppression on user quit intent:
  - `integration/integrations/permission_restart_integration.py`
  - guard applied for:
    - `first_run_restart_pending`
    - transition-based scheduling
    - delayed restart execution
- Fixed autostart config ownership to existing integration section:
  - `integration/core/integration_factory.py` now reads `integrations.autostart_manager`
  - `config/unified_config.yaml` updated:
    - `integrations.autostart_manager.monitor_enabled: true`
    - `integrations.autostart_manager.auto_repair: false`
    - `integrations.autostart_manager.cleanup_legacy_launch_agent: true`

## Architecture Fit
- Source of truth preserved:
  - lifecycle quit intent: coordinator/state_manager
  - restart path: permission_restart integration
  - autostart path: autostart_manager integration
- No new side channel for mode/startup decisions introduced.

## Verification
- `python3 -m py_compile integration/core/state_keys.py integration/core/simple_module_coordinator.py integration/integrations/permission_restart_integration.py integration/core/integration_factory.py modules/tray_controller/core/tray_controller.py`
- `python3 -m py_compile modules/tray_controller/macos/menu_handler.py`
- `rg -n "activateIgnoringOtherApps_(True)" main.py modules/tray_controller -S`
  - expected remaining owner: `main.py` only
