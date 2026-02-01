# Build Validity Check

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-24
- ID (INS-###): INS-000 (registry missing)

## Diagnosis
Свежая сборка завершилась успешно, но в установленном .app и в pkg payload отсутствует Contacts и entitlements невалидны.

## Root Cause
- В pkg payload нет `Contacts*` → модуль не включен.
- `codesign -d --entitlements` показывает `invalid entitlements blob` → entitlements игнорируются.
- Ledger сохранён, поэтому Settings для Accessibility больше не открывается повторно.

## Optimal Fix
Исправить entitlements (убрать sandbox-only ключи), пересобрать, установить app из pkg/dmg; очистить ledger для повторного открытия Settings.

## Verification
Проверить entitlements в pkg payload и наличие Contacts; сбросить ledger и повторить запуск.

## Запрос/цель
Проверить корректность сборки и причины некорректного поведения.

## Контекст
- Файлы: packaging/build_final.sh, packaging/entitlements.plist
- Артефакт: dist/Nexy.pkg
- Логи: ~/Library/Logs/Nexy/nexy.log

## Решения/выводы
- Сборка завершается, но артефакт содержит невалидные entitlements и без Contacts.

## Открытые вопросы
- Отсутствует Docs/CRM_INSTRUCTION_REGISTRY.md; нужен источник INS-###.

## Следующие шаги
- Исправить entitlements и пересобрать.
- Проверить наличие Contacts в payload.
