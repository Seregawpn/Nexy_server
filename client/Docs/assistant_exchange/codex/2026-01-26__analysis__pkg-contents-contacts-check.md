# PKG Contents Check — Contacts

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-26
- ID (INS-###): INS-000 (registry missing)

## Diagnosis
Внутри `dist/Nexy.pkg` есть `Nexy.app` с корректным Info.plist и модулем `Contacts` в `Contents/Frameworks`.

## Root Cause
Нет проблемы в текущей упаковке: Contacts framework присутствует, usage‑description задан.

## Optimal Fix
Использовать свежий PKG/DMG; если runtime всё равно выдаёт ImportError — значит запускается не этот билд или очистить старую установку.

## Verification
- `Info.plist` содержит `NSContactsUsageDescription`.
- В `.app/Contents/Frameworks` есть `Contacts/_Contacts.cpython-313-darwin.so`.

## Запрос/цель
Проверить содержимое PKG на наличие Contacts.

## Контекст
- Файлы: dist/Nexy.pkg (распакован в /tmp/Nexy_pkg_extract)

## Решения/выводы
- Contacts присутствует в пакете.

## Открытые вопросы
- Нет.

## Следующие шаги
- Установить PKG и проверить runtime лог на отсутствие ImportError.
