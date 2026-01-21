# Remove Permission Checks in Restart Flow

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-18
- ID (INS-###): INS-008

## Diagnosis
Permission restart flow executed status checks (IOHIDCheckAccess etc.), contradicting the requirement to avoid permission checks and only trigger dialogs.

## Root Cause
PermissionRestartIntegration subscribed to `permissions.status_checked` and polled status_checker APIs during restart readiness.

## Optimal Fix
Remove status_checker usage and treat permissions as granted for restart readiness; keep restart gated only by first-run events.

## Verification
Code updated to drop status checks, remove subscriptions, and assume GRANTED for readiness.

## Запрос/цель
Eliminate permission status checks from restart flow.

## Контекст
- Файлы: integration/integrations/permission_restart_integration.py
- Документы: Docs/first_run_flow_spec.md
- Ограничения: без изменения activator

## Решения/выводы
- Removed `permissions.status_checked` subscription.
- Removed status_checker calls; readiness now assumes GRANTED.

## Открытые вопросы
- Нужен ли тест-прогон после изменения?

## Следующие шаги
- Прогнать first-run тест.
