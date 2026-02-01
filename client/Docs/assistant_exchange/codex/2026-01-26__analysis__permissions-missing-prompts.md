# Permissions Missing Prompts — Analysis

## Summary
Observed: only mic + screen + input dialogs appear, остальные разрешения не запрашиваются.

## Evidence
- `log.md` содержит TCC для `kTCCServiceScreenCapture`, `kTCCServiceMicrophone`, `kTCCServiceListenEvent`, **нет** `kTCCServiceContacts`.
- В `config/unified_config.yaml` порядок V2 включает `contacts`, `accessibility`, `full_disk_access`.
- В V2 orchestrator диалоги показываются только для auto_dialog; `accessibility` и `full_disk_access` — settings-only.
- Контакты требуют наличия `pyobjc-framework-Contacts` + `NSContactsUsageDescription` в Info.plist + CNContactStore trigger.

## Likely Root Cause
1) Contacts prompt не появляется из-за runtime/packaging gap (нет `Contacts` framework в .app или отсутствует `NSContactsUsageDescription` в main Info.plist). Тогда ContactsProber silently fails and the step passes without prompt.
2) Ожидаемые “доп. запросы” для Accessibility/Full Disk — это не системные диалоги, а открытие System Settings. Если Settings не открывается (или пользователь не заметил), кажется, что запросов нет.

## Architecture Notes
- Source of Truth: `integrations.permissions_v2.order` + `modules/permissions/v2/probers/*`.
- First-run flow продолжает pipeline даже если шаг в WAITING_USER; UI диалог может не появиться, но шаг считается обработанным.

## Next Checks (cheap)
- В .app: проверить `Contents/Info.plist` на `NSContactsUsageDescription`.
- В runtime: `import Contacts` из .app окружения (pyobjc-framework-Contacts).
- В логах: наличие `[CONTACTS_PROBER] Triggered contacts permission request`.

