# Packaging/Env Audit — Contacts

## Date
2026-01-27

## Scope
Проверка упаковочных документов, скриптов и окружения на наличие контактов и ключей разрешений.

## Findings
- `requirements.txt`: есть `pyobjc-framework-Contacts==12.1`.
- `packaging/Nexy.spec`: есть hiddenimport `Contacts` и `NSContactsUsageDescription` в `info_plist`.
- `packaging/build_final.sh`: есть preflight `import Contacts` (arm64 + x86_64).
- `packaging/entitlements.plist`: есть `com.apple.security.personal-information.addressbook`.
- `scripts/verify_pyinstaller.py`: **не проверяет** `NSContactsUsageDescription`, `NSInputMonitoringUsageDescription`, `NSFullDiskAccessUsageDescription`.

## Gaps
- В `Nexy.spec` отсутствуют `NSInputMonitoringUsageDescription` и `NSFullDiskAccessUsageDescription` в info_plist.
- Скрипт `verify_pyinstaller.py` не валидирует ключи Contacts/FDA/InputMonitoring.

## Conclusion
Packaging/Deps для Contacts в целом присутствуют, но есть пробелы в проверках и в info_plist для InputMonitoring/FDA.
