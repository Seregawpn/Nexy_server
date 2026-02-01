# Permissions Build Files Review

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-24
- ID (INS-###): INS-000 (registry missing)

## Diagnosis
Основной Info.plist и entitlements содержат нужные описания, но есть потенциальные конфликты в модульных Info.plist и отсутствие Contacts модуля в bundle.

## Root Cause
Модульные Info.plist содержат заглушки "does not need" и могут конфликтовать с основным app plist; Contacts.framework не попадает в runtime.

## Optimal Fix
Проверить, используются ли модульные plist в сборке; если да — синхронизировать описания с основным app. Убедиться, что pyobjc-framework-Contacts установлен и попадает в bundle.

## Verification
Проверить содержимое .app и лог `No module named 'Contacts'`.

## Запрос/цель
Анализ корректности файлов разрешений, участвующих в сборке.

## Контекст
- Файлы: packaging/Nexy.spec, packaging/entitlements.plist, modules/*/macos/info/Info.plist
- Логи: ~/Library/Logs/Nexy/nexy.log

## Решения/выводы
- Основной Info.plist содержит NSMicrophone/NSScreenCapture/NSAccessibility/NSContacts.
- Entitlements включают addressbook и screen-capture.
- Модульные plist содержат противоречивые описания ("does not need").
- Contacts модуль отсутствует в runtime.

## Открытые вопросы
- Отсутствует Docs/CRM_INSTRUCTION_REGISTRY.md; нужен источник INS-###.

## Следующие шаги
- Определить, используются ли модульные plist в финальной .app.
- Исправить/удалить противоречивые описания, если они применяются.
