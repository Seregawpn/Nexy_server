# Analysis: packaging restart/autostart nuances

## Request
Проверить упаковочную документацию и скрипты на нюансы, которые могут вызывать повторный запуск после Quit.

## Findings
1. `packaging/pkg_scripts/postinstall` очищал только legacy system LaunchAgent:
   - `/Library/LaunchAgents/com.sergiyzasorin.nexy.voiceassistant.plist`
2. В проекте исторически использовался user-level LaunchAgent:
   - `~/Library/LaunchAgents/com.nexy.assistant.plist`
   Этот путь фигурирует в `modules/autostart_manager/*`.
3. Если user LaunchAgent остаётся после старых версий, он может участвовать в автоподъёме и конфликтовать с ожидаемым Quit-поведением.
4. В `Docs/PACKAGING_FINAL_GUIDE.md` не было явного пункта о mandatory очистке user LaunchAgent.

## Implemented fix
1. `packaging/pkg_scripts/postinstall`
- Добавлена очистка user LaunchAgent для активного console user:
  - определение `CONSOLE_USER/CONSOLE_UID/CONSOLE_HOME`
  - `launchctl bootout gui/<uid>/com.nexy.assistant` (best-effort)
  - `launchctl bootout gui/<uid> <path_to_user_plist>` (best-effort)
  - `rm -f ~/Library/LaunchAgents/com.nexy.assistant.plist`
- Сохранена существующая очистка legacy system LaunchAgent.

2. `Docs/PACKAGING_FINAL_GUIDE.md`
- Добавлен явный блок политики автозапуска:
  - postinstall не включает автозапуск
  - обязательная очистка system + user LaunchAgent
  - связь с проблемой relaunch после Quit

## Validation
- `bash -n packaging/pkg_scripts/postinstall` → `OK`.

## Notes
- Это packaging-level hardening дополняет runtime guard (user quit -> suspend current session) и снижает риск повторного старта на машинах с legacy/autostart остатками.
