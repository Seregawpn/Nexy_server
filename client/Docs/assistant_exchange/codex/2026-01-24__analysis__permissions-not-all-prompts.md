# Missing Permission Prompts

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-24
- ID (INS-###): INS-000 (registry missing)

## Diagnosis
Пользователь видит только mic/screen/input; остальные разрешения не показывают диалоги, приложение продолжает старт.

## Root Cause
Accessibility/FDA — settings-only (нет диалогов) + возможный пропуск pipeline из-за существующего permissions_first_run_completed.flag; Contacts может быть недоступен в сборке.

## Optimal Fix
Сбросить флаги и ledger, убедиться в наличии Contacts в .app, проверить V2 step logs и Settings opening.

## Verification
Логи `permissions.v2.step_changed` и наличие/отсутствие флага.

## Запрос/цель
Объяснить причину отсутствующих диалогов и дать проверки.

## Контекст
- Файлы: integration/integrations/first_run_permissions_integration.py, modules/permissions/v2/orchestrator.py
- Логи: ~/Library/Logs/Nexy/nexy.log

## Решения/выводы
- Не все permissions вызывают диалог; settings-only шаги должны открывать Settings.
- При наличии флага pipeline пропускается.

## Открытые вопросы
- Отсутствует Docs/CRM_INSTRUCTION_REGISTRY.md; нужен источник INS-###.

## Следующие шаги
- Очистить flags/ledger и проверить шаги в логах.
