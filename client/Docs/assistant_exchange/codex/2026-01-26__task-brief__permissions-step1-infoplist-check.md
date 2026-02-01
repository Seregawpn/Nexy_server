# Permissions Step1 — Info.plist Check

## Date
2026-01-26

## Scope
Проверка `Contents/Info.plist` в `/Applications/Nexy.app` на usage keys.

## Findings
- Найдены: `NSContactsUsageDescription`, `NSAccessibilityUsageDescription`, `NSMicrophoneUsageDescription`, `NSScreenCaptureUsageDescription`.
- Не обнаружены в plist (по grep): `NSInputMonitoringUsageDescription`, `NSFullDiskAccessUsageDescription`.

## Evidence
Команда:
- `plutil -p /Applications/Nexy.app/Contents/Info.plist | rg ...`

## Next Step
Проверить runtime доступность `Contacts` framework из .app (import) и лог триггера контактов.
