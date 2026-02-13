# Summary
- Выполнен разбор `~/Library/Logs/Nexy/nexy-dev.log` и сопоставление warning с исходниками.
- Определены 3 ключевые архитектурные зоны с дубликатами/гонками:
  1) Tray startup/menu init,
  2) Autostart status checks,
  3) Welcome -> mode.request(PROCESSING) без session_id.

# Key Findings
1. `update_menu: self.app is None`
- Источник: `modules/tray_controller/core/tray_controller.py` вызывает `_create_default_menu()` в `initialize()` до `create_app()`.
- Логгер: `modules/tray_controller/macos/menu_handler.py:update_menu`.
- Тип: startup ordering race + ранний вызов без готового owner (`self.app`).

2. `LaunchAgent автозапуск не найден` x3
- Источник: `integration/integrations/autostart_manager_integration.py:_check_autostart_status`.
- Проверка вызывается минимум из `start()` и `app.startup` handler; дополнительно возможен внешний `autostart.check_status`.
- Тип: дублированный путь проверки (не единый trigger owner).

3. `MODE_REQUEST rejected: target=PROCESSING requires session_id (source=welcome_message)`
- Источник запроса: `integration/integrations/welcome_message_integration.py:_play_welcome_message` (publish без `session_id`).
- Валидатор: `integration/integrations/mode_management_integration.py:_on_mode_request` (guard корректен).
- Тип: контрактный конфликт между publisher и mode owner.

4. Остальные warning
- `Health check неудачен (1/3)` — transient сеть, guard есть.
- `Quartz tap disabled, recovery #1` — recoverable, self-healing.
- `No module named 'olefile'` — debug импорт PIL-плагинов, не runtime crash.
- `SSL verification disabled` — ожидаемо для self-signed dev-конфига.

# Recommended Wiring Fixes (Architecture-safe)
1. Tray startup wiring:
- Не вызывать `update_menu` до `create_app`.
- Владелец готовности: `tray.integration_ready`/наличие `self.app`.
- Реализация: в `TrayController._create_default_menu()` добавлять guard `if not self.tray_menu or not self.tray_menu.app: cache menu and return`.

2. Autostart status wiring:
- Один владелец первой проверки: либо `start()`, либо `app.startup`, но не оба.
- Добавить single-flight lock в `_check_autostart_status`.
- Логировать отсутствие LaunchAgent один раз на boot (state-change based logging).

3. Welcome/Mode wiring:
- Публиковать `mode.request(PROCESSING)` только с `session_id` (welcome playback session id).
- Либо перенести переход в PROCESSING после получения `session_id` из `_send_audio_to_playback`.
- Guard в `ModeManagementIntegration` оставить (это правильный SoT).

# Risk
- Без правок: warning-шум скрывает реальные проблемы и усложняет triage.
- С правками: риск низкий, т.к. логика централизации уже есть (EventBus + dedup guards), нужно только выровнять контракт и trigger ownership.
