# Task Brief: Runtime smoke checklist (focus + tray + quit)

## Scope
Проверка нового режима:
- без постоянного forced focus на старте;
- с one-shot fallback при задержке tray;
- с защитой от restart после user quit.

## Preconditions
- Сборка/запуск клиента с актуальным `config/unified_config.yaml`.
- В конфиге:
  - `focus.force_activate_on_startup: false`
  - `focus.allow_tray_startup_fallback: true`
  - `focus.tray_fallback_timeout_sec: 6.0`

## Smoke Steps
1. Cold start приложения.
2. Сразу после старта нажать `Cmd+Space` 5-10 раз.
3. Проверить tray icon и открыть меню Nexy.
4. Подождать 10-15 секунд, убедиться что меню не исчезает самопроизвольно.
5. Выполнить `Quit` через tray menu.
6. Наблюдать 60 секунд: приложение не должно самозапуститься.
7. Повторить запуск и проверить обычный PTT сценарий (press/hold/release).

## Expected Behavior
- Spotlight не схлопывается из-за Nexy.
- Tray появляется стабильно.
- Если tray задерживается, fallback активация срабатывает не более одного раза.
- После `Quit` нет самоперезапуска.
- PTT flow работает как раньше.

## Log Markers (grep)
- Нормальный путь:
  - `Skipped activateIgnoringOtherApps_(True) by focus config`
- Fallback путь (редко, при задержке):
  - `[FOCUS] Triggering one-shot tray startup fallback`
  - `[FOCUS] One-shot fallback activation executed`
- Quit path:
  - `Quit requested via tray menu`
  - `user quit intent active - skip`

## Fail Conditions
- Spotlight закрывается/теряет фокус после старта.
- Повторные fallback-активации в одном запуске.
- После `Quit` новый `NEXY APPLICATION START` без действия пользователя.
