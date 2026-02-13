# Analysis — hotkey/focus/voiceover conflict architecture

## Scope
- User request: анализ текущей архитектуры и флагов без внедрения.
- Goal: найти источник конфликта (`Cmd+Space`/Spotlight/Alfred) и определить архитектурно корректный fix-path без дублирования и race.

## Current architecture ownership (SoT)
- Keyboard suppression owner:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/modules/input_processing/keyboard/mac/quartz_monitor.py`
- PTT lifecycle owner:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/integration/integrations/input_processing_integration.py`
- VoiceOver control owner:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/integration/integrations/voiceover_ducking_integration.py`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/modules/voiceover_control/core/controller.py`
- Focus activation owner:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/main.py`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/integration/core/simple_module_coordinator.py`

## Flag map (current config)
- `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/config/unified_config.yaml`
  - `accessibility.voiceover_control.engage_on_keyboard_events: false`
  - `accessibility.voiceover_control.hard_toggle_enabled: false`
  - `focus.force_activate_on_startup: false`
  - `focus.allow_tray_startup_fallback: true`
  - `integrations.keyboard.key_to_monitor: ctrl_n`
  - `integrations.keyboard.backend: auto`
  - `integrations.input_processing.enable_keyboard_monitoring: true`

## Risk points found
1. Global active tap in combo mode:
   - Quartz uses active tap (`kCGEventTapOptionDefault`) for combo path and can consume events (`return None`).
   - Это единственная реальная точка, где системный shortcut может быть сломан.

2. Strict combo policy implemented, but fragile on edge states:
   - Логика уже ограничивает suppression strict `Ctrl+N` и блокирует combo при `Command/Option/Shift`.
   - Риск остается в edge-case рассинхронизации modifier flags (`flagsChanged`) и pending-release timing.

3. Focus fallback can steal foreground, but should be startup-only:
   - One-shot `activateIgnoringOtherApps_(True)` вызывается в tray startup fallback.
   - Если fallback срабатывает вне ожидаемого окна, возможен фокусный side effect.

4. Duplicate subscription in VoiceOver integration:
   - `system.permissions_ready` подписывается дважды в `VoiceOverDuckingIntegration`.
   - Это не primary причина `Cmd+Space`, но создает дублированный event-path и повышает race/noise risk.

## Root-cause hypothesis
- Most likely: нецелевой shortcut (`Cmd+Space`) затрагивается suppression/focus side effects в runtime.
- Additional possibility for older builds: config drift (не `ctrl_n`, включенный keyboard ducking, legacy hotkey path).

## Architecture-safe direction (no implementation here)
1. Keep one suppression owner: Quartz combo path only.
2. Hard invariant: suppress only strict `Ctrl+N`; all `Command/Option/Shift` combos are pass-through.
3. Keep VoiceOver isolated from keyboard press path (`engage_on_keyboard_events=false`).
4. Keep forced focus activation startup-scoped only; never hotkey runtime-scoped.
5. Remove duplicate `system.permissions_ready` subscription in VoiceOver integration.
6. Add contract tests for pass-through (`Cmd+Space`, `Cmd+Shift+A`, `Ctrl+Cmd+N`).

## Expected result after fix
- Nexy reacts only to `Ctrl+N`.
- Spotlight/Alfred remains open and focused on `Cmd+Space`.
- No duplicated event handling in VoiceOver init path.
