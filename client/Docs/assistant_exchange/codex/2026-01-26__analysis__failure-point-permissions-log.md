# Failure Point — Permissions Log

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-26
- ID (INS-###): INS-000 (registry missing)

## Diagnosis
В логе видны запросы только для микрофона, screen capture и listen event (input monitoring). После этого идут попытки Accessibility без entitlement, а Contacts/FDA запросов в логах нет.

## Root Cause
First-run V2 → accessibility/fda = settings-only; contacts зависит от Contacts framework/trigger → отсутствует системный prompt и нет следов Contacts/FDA в логах.

## Optimal Fix
Проверить доступность Contacts framework и события `permissions.v2.*`; убедиться, что Settings открывается для accessibility/fda. При необходимости — исправить упаковку Contacts/Quartz.

## Verification
- Логи tccd для contacts/fda отсутствуют
- Есть tccd error для accessibility без entitlement

## Запрос/цель
Указать точку отказа по log.md.

## Контекст
- Файлы: log.md, modules/permissions/v2/probers/*, config/unified_config.yaml

## Решения/выводы
- Точка отказа: переход на accessibility → системный prompt не появляется (settings-only + tccd error) и дальше нет контактов/FDA в логах.

## Открытые вопросы
- Доступен ли Contacts framework в сборке?

## Следующие шаги
- Проверить логи приложения (`[CONTACTS_PROBER]`) и наличие Settings deep-link.
