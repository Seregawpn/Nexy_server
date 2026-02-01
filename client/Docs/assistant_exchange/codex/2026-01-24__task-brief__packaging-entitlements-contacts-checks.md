# Packaging Entitlements + Contacts Checks

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-01-24
- ID (INS-###): INS-000 (registry missing)

## Diagnosis
Сборка могла проходить с невалидными entitlements и без pyobjc Contacts, что ломало permissions.

## Root Cause
Отсутствовали fail-fast проверки и был невалидный entitlement ключ.

## Optimal Fix
Добавлен preflight import Contacts и проверка entitlements blob; удален невалидный entitlement.

## Verification
Сборка падает при отсутствии Contacts или invalid entitlements; кодсайн без предупреждений.

## Запрос/цель
Стабилизировать packaging по permissions.

## Контекст
- Файлы: packaging/build_final.sh, packaging/entitlements.plist

## Решения/выводы
- Добавлена проверка `import Contacts` в preflight.
- Добавлена проверка invalid entitlements blob.
- Удален `com.apple.security.automation.accessibility`.

## Открытые вопросы
- Отсутствует Docs/CRM_INSTRUCTION_REGISTRY.md; нужен источник INS-###.

## Следующие шаги
- Пересобрать .app и проверить codesign entitlements.
