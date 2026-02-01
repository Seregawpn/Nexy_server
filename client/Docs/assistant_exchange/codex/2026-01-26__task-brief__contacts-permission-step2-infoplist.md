# Contacts Permission Step 2 — Info.plist Check

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-01-26
- ID (INS-###): INS-000 (registry missing)

## Diagnosis
Contacts prompt требует ключ `NSContactsUsageDescription` в основном Info.plist .app.

## Root Cause
Без этого ключа macOS блокирует показ диалога Contacts.

## Optimal Fix
Подтвердить наличие `NSContactsUsageDescription` в `packaging/Nexy.spec` (info_plist section).

## Verification
- В `packaging/Nexy.spec` присутствует `NSContactsUsageDescription`.

## Запрос/цель
Выполнить второй этап — проверка Info.plist.

## Контекст
- Файлы: packaging/Nexy.spec

## Решения/выводы
- Ключ `NSContactsUsageDescription` присутствует в `packaging/Nexy.spec` (info_plist).

## Открытые вопросы
- Нет.

## Следующие шаги
- Перейти к проверке зависимостей/упаковки (pyobjc Contacts).
