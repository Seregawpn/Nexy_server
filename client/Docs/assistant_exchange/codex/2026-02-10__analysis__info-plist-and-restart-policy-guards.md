# Analysis: Info.plist and restart policy guards

## Request
Проверить, есть ли в Info.plist/packaging нюансы перезапуска, и не удалять полезные рестарты, а корректно ограничить нежелательный relaunch после user Quit.

## Findings
1. Основной app Info.plist формируется в `packaging/Nexy.spec` (`info_plist={...}`).
2. В этом plist нет ключей, которые сами по себе включают "автоперезапуск после Quit".
   - Есть `NSSupportsAutomaticTermination=false` и `NSSupportsSuddenTermination=false` (это про auto-terminate, не про relaunch).
3. Модульные `modules/*/info/Info.plist` не являются драйверами relaunch главного приложения.
4. Реальные источники relaunch-поведения:
   - LaunchAgent/autostart контуры (legacy/user).
   - Явный `relaunch_app()` в `UpdaterIntegration` после update.
   - Permission restart (только по permission-flow, это штатный restart).

## Implemented hardening
1. `integration/integrations/updater_integration.py`
- Добавлен guard перед `relaunch_app()`:
  - если `StateKeys.USER_QUIT_INTENT=true`, updater relaunch пропускается.
- Это не отключает update/permission restart в целом, а предотвращает конфликт "пользователь нажал Quit" vs "updater хочет relaunch".

## Validation
- Regression run:
  - `tests/test_user_quit_ack.py`
  - `tests/test_interrupt_playback.py`
  - `tests/test_signal_integration_cancel_done_suppression.py`
  - `tests/test_mode_management_mode_request_dedup.py`
  - `tests/test_speech_playback_session_id.py`
- Result: `28 passed`.

## Conclusion
- Проблема не в подписи Info.plist и не в plist-ключе "relaunch".
- Правильный путь: policy guards в runtime + корректная cleanup политика autostart в packaging (без удаления нужных restart сценариев).
