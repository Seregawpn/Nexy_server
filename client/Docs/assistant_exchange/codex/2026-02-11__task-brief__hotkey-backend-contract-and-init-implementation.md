# Task Brief — hotkey backend contract and init implementation

## Context
Пользователь попросил обновить требования и перейти к реализации: один suppression path (`Ctrl+N`) без влияния на другие комбинации.

## Changes

1. Updated requirements spec:
- File: `Docs/HOTKEY_COMBINATION_REQUIREMENTS.md`
- Added runtime contract sections:
  - `REQ-HK-010 Allowed Libraries`
  - `REQ-HK-011 Backend Selection`
  - `REQ-HK-012 Single Suppression Owner`
- Clarified backend policy (`auto|quartz|pynput`) and owner boundaries.

2. Implemented backend-init policy in input integration:
- File: `integration/integrations/input_processing_integration.py`
- Added strict backend validation:
  - unknown backend -> warning + fallback to `auto`.
  - explicit `quartz` mode with unavailable Quartz -> no silent fallback, `ptt_available=false`, clear error log.
  - fallback path logs explicit non-expansion of suppression paths.

## Why this fits architecture
- Input owner stays centralized in `InputProcessingIntegration`.
- Quartz remains suppression-owner for strict `Ctrl+N`.
- No new owner path introduced in UI/tray layers.

## Verification
- `python3 -m py_compile integration/integrations/input_processing_integration.py modules/input_processing/keyboard/mac/quartz_monitor.py modules/input_processing/keyboard/keyboard_monitor.py config/unified_config_loader.py`
- Result: success.
