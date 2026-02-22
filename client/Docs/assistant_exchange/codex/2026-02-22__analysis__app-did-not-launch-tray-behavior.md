# Analysis: Nexy app did not "launch"

## Context
User reported that app did not start after packaging/notarization.

## Findings
- Build and notarization completed successfully (DMG/PKG accepted, stapled, validated).
- Final packaging script intentionally removes artifacts from `client/dist` and leaves release files in `server/release_inbox`.
- App starts as a tray/background app (no main window expected).
- Runtime process confirmed: `/Applications/Nexy.app/Contents/MacOS/Nexy`.
- Gatekeeper/signature checks are valid for installed app.
- No crash reports found for Nexy in DiagnosticReports.

## Evidence
- Build log: `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/build_logs/build_20260221_214640.log`
- App logs: `/Users/sergiyzasorin/Library/Logs/Nexy/nexy.log`, `/Users/sergiyzasorin/Library/Logs/Nexy/nexy-dev.log`
- Release artifacts: `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/server/release_inbox/Nexy.dmg`, `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/server/release_inbox/Nexy.pkg`

## Verification
- `codesign --verify --deep --strict /Applications/Nexy.app` -> OK
- `spctl -a -vv /Applications/Nexy.app` -> accepted (Notarized Developer ID)
- Process visible in `ps/pgrep` after launch.

## Информация об изменениях
- Изменения не вносились.
- Список файлов: отсутствует.
- Причина/цель изменений: анализ инцидента запуска без правок кода.
- Проверка: выполнены команды валидации подписи/нотарификации и проверка runtime-процесса/логов.
