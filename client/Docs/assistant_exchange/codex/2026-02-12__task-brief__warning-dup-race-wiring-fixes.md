# Task
Снизить warning-шум и убрать дубли/гонки в startup wiring:
- tray menu update до готовности app,
- повторные autostart checks на bootstrap,
- mode.request(PROCESSING) из welcome без session_id.

# Changes
1. Tray menu startup guard
- Файл: `modules/tray_controller/macos/menu_handler.py`
- Добавлен `self._pending_menu`.
- `update_menu()` теперь откладывает обновление при `app is None` (debug вместо warning).
- После `create_app()` отложенное меню применяется автоматически.

2. Autostart single-flight + dedup startup check
- Файл: `integration/integrations/autostart_manager_integration.py`
- Добавлены:
  - `self._status_check_lock`,
  - `self._startup_check_done`,
  - `self._last_launch_agent_exists`.
- Проверка в `start()` помечает bootstrap check как выполненный.
- `app.startup` handler пропускает дублирующую проверку.
- `_check_autostart_status(trigger=...)` выполняется под lock и логирует отсутствие LaunchAgent только при смене состояния или manual trigger.

3. Welcome -> PROCESSING contract fix
- Файл: `integration/integrations/welcome_message_integration.py`
- `mode.request(PROCESSING)` теперь публикуется с `session_id`.
- `_send_audio_to_playback()` принимает optional `session_id` и использует тот же id, что и mode.request.

# Validation
- Выполнен синтаксический чек:
  - `python3 -m py_compile modules/tray_controller/macos/menu_handler.py integration/integrations/autostart_manager_integration.py integration/integrations/welcome_message_integration.py`
- Ошибок компиляции нет.

# Expected Log Impact
- Должен исчезнуть warning `update_menu: self.app is None` на старте.
- `LaunchAgent автозапуск не найден` не должен повторяться несколько раз в одном bootstrap.
- Должен исчезнуть warning `MODE_REQUEST rejected: target=PROCESSING requires session_id (source=welcome_message)`.
