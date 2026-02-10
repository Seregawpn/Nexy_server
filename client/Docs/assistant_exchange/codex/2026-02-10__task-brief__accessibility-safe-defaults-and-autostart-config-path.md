# Task Brief: Accessibility safe defaults and autostart config-path hardening

## Goal
Снизить риск blind-UX сбоев без изменения архитектуры:
- убрать влияние VoiceOver ducking на keyboard press path по умолчанию;
- гарантировать, что cleanup legacy autostart использует единый конфиг-источник.

## Changes
- `config/unified_config.yaml`
  - `accessibility.voiceover_control.engage_on_keyboard_events: false`
  - оставлено `enabled: true`, то есть VoiceOver control работает только по mode path.
- `integration/integrations/autostart_manager_integration.py`
  - заменен hardcoded legacy path на `self.config.legacy_launch_agent_path` в `_check_autostart_status()`.

## Architecture Fit
- VoiceOver поведение регулируется только существующим конфигом (`voiceover_control`).
- Autostart cleanup остается в owner-модуле `AutostartManagerIntegration`.
- Новый источник истины не добавлен.

## Verification
- `python3 -m py_compile integration/integrations/autostart_manager_integration.py`
- `rg` проверка:
  - `config/unified_config.yaml` содержит `engage_on_keyboard_events: false`
  - `autostart_manager_integration.py` использует `self.config.legacy_launch_agent_path`
