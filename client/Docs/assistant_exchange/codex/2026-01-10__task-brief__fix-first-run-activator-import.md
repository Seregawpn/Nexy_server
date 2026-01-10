# Fix First-Run Activator Import

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-01-10
- ID (INS-###): INS-005

## Diagnosis
В packaged .app activator падал из-за импорта несуществующего модуля `modules.permissions.first_run.types`.

## Root Cause
Ошибка в импорте → `No module named ...` → не запускается first-run activator → permissions не запрашиваются.

## Optimal Fix
Перевести импорт PermissionStatus на `modules.permissions.first_run.status_checker` и убрать несуществующий hiddenimport.

## Verification
- В логе Nexy нет `No module named 'modules.permissions.first_run.types'`.
- Диалоги permissions появляются при first-run.

## Запрос/цель
Устранить import-ошибку activator в packaged .app.

## Контекст
- Файлы: `modules/permissions/first_run/activator.py`, `packaging/Nexy.spec`
- Документы: `Docs/PROJECT_REQUIREMENTS.md`, `Docs/ARCHITECTURE_OVERVIEW.md`

## Решения/выводы
- Используем существующий `PermissionStatus` из `status_checker`.

## Открытые вопросы
- Нет.

## Следующие шаги
- Пересобрать .app.
- Проверить лог `/var/folders/.../T/nexy_debug.log`.
