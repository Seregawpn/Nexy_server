# Task Brief: Focus config + one-shot tray fallback

## Goal
Убрать постоянный focus steal, но сохранить стабильный запуск tray через контролируемый fallback.

## Changes
- `config/unified_config.yaml`
  - Добавлена секция:
    - `focus.force_activate_on_startup: false`
    - `focus.allow_tray_startup_fallback: true`
    - `focus.tray_fallback_timeout_sec: 6.0`

- `main.py`
  - `activate_nsapplication_for_menu_bar(force_activate: bool = False)`
  - Всегда делает `setActivationPolicy(Accessory)`.
  - `activateIgnoringOtherApps_(True)` теперь выполняется только если:
    - `force_activate=True` (явный fallback), или
    - `focus.force_activate_on_startup=true`.

- `integration/core/simple_module_coordinator.py`
  - Добавлен one-shot guard: `_focus_fallback_done`.
  - Добавлены helper-методы:
    - `_get_focus_config()`
    - `_force_focus_activation_for_tray_once(reason)`
  - В tray-gate ожидании перед `first_run_permissions`/`permission_restart`:
    - timeout берется из `focus.tray_fallback_timeout_sec`
    - при `tray not ready` и `allow_tray_startup_fallback=true` выполняется однократный forced activation
    - после fallback дается короткое retry-окно (2s) для `tray_ready`.

## Architecture Fit
- Центр управления сохранен:
  - startup focus policy в `main.py`
  - fallback policy в coordinator
- Дубли forced activation в tray modules не возвращались.

## Verification
- `python3 -m py_compile main.py integration/core/simple_module_coordinator.py`
- `rg`:
  - focus keys присутствуют в `config/unified_config.yaml`
  - conditional usage присутствует в `main.py` и coordinator.
