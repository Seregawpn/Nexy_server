# Task brief: revert packaging restart-cleanup changes

## Request
Убрать изменения в упаковке, связанные с cleanup/restart, и оставить корректное поведение через код/политику без удаления нужных restart сценариев.

## Reverted
1. `packaging/pkg_scripts/postinstall`
- Возвращён к версии с cleanup только legacy system LaunchAgent:
  - `/Library/LaunchAgents/com.sergiyzasorin.nexy.voiceassistant.plist`
- Удалена добавленная cleanup логика для user LaunchAgent `~/Library/LaunchAgents/com.nexy.assistant.plist`.

2. `Docs/PACKAGING_FINAL_GUIDE.md`
- Удалён добавленный блок "Политика автозапуска (критично для Quit-поведения)".

## Kept (not reverted)
- Runtime guard в `UpdaterIntegration` (skip relaunch при `USER_QUIT_INTENT=true`) оставлен, т.к. это кодовая защита от нежелательного relaunch после ручного Quit, без отключения штатных restart потоков.

## Validation
- `bash -n packaging/pkg_scripts/postinstall` -> `OK`.
