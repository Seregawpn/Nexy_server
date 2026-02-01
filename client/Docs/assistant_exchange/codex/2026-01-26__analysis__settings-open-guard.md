# Settings Open Guard

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-26
- ID (INS-###): INS-000 (registry missing)

## Diagnosis
OPEN_SETTINGS шаги помечали settings_opened_at независимо от результата открытия, из-за чего повторная попытка не выполнялась и пользователь видел "тишину".

## Root Cause
`PermissionOrchestrator._run_pipeline` → `settings_nav.open(...)` без проверки успеха → `settings_opened_at` фиксируется даже при неуспехе → дальнейшие попытки не происходят.

## Optimal Fix
Учитывать результат `settings_nav.open(...)` и фиксировать `settings_opened_at` только при успехе, иначе логировать предупреждение.

## Verification
- При неуспехе открытия Settings повторный запуск должен снова пытаться открыть.
- В логах видно предупреждение `[ORCHESTRATOR] Failed to open Settings...`.

## Запрос/цель
Гарантировать открытие Settings для accessibility/fda или явный сигнал о неуспехе.

## Контекст
- Файлы: modules/permissions/v2/orchestrator.py, modules/permissions/v2/settings_nav.py

## Решения/выводы
- Добавлена проверка успеха открытия Settings перед фиксацией состояния.

## Открытые вопросы
- Нужно ли добавить fallback `open -a "System Settings"`?

## Следующие шаги
- Проверить поведение на проблемной машине.
