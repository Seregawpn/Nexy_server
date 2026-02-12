# Task Brief: Unified quit path for autostart session suspend

## Context
Пользовательский симптом: после закрытия/выхода приложение может подниматься снова.

## Diagnosis
В коде есть autostart контур через LaunchAgent (`autostart_manager`). Suspend LaunchAgent для текущей сессии делается только на user-initiated shutdown (`app.shutdown` + `user_initiated`/`USER_QUIT_INTENT`).

Проблема: системный terminate путь (`applicationShouldTerminate`) в `MacOSTrayMenu` не был связан с единым quit-flow. `set_quit_callback()` в runtime не вызывался.

## Changes
1. `modules/tray_controller/core/tray_controller.py`
- В `TrayController.start()` добавлена регистрация quit callback:
  - `self.tray_menu.set_quit_callback(lambda: self._on_quit_clicked(sender=None))`
- Этим любой системный quit (Dock/Cmd+Q/osascript quit) направляется в единый путь:
  - `quit_clicked` -> coordinator sets `USER_QUIT_INTENT=true` -> publishes `app.shutdown(user_initiated=true)` -> autostart integration can suspend LaunchAgent in current session.

2. `tests/test_tray_quit_dispatch.py`
- Добавлен регрессионный тест `test_start_registers_system_quit_callback_to_unified_quit_flow`.
- Проверяет, что callback зарегистрирован и вызывает `_on_quit_clicked(sender=None)`.

## Verification
Executed:
- `pytest -q tests/test_tray_quit_dispatch.py tests/test_user_quit_ack.py`

Result:
- `5 passed`

## Notes
- Packaging `postinstall` уже удаляет legacy LaunchAgent (`/Library/LaunchAgents/com.sergiyzasorin.nexy.voiceassistant.plist`).
- Риск повторного запуска остаётся, если на машине есть внешний/старый autostart артефакт вне текущего управления.
