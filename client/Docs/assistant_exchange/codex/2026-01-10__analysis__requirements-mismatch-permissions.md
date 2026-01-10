# Requirements Mismatch — Permissions Flow

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-10
- ID (INS-###): INS-005

## Diagnosis
Packaged .app не выполняет корректный first-run permissions flow из-за отсутствующего модуля activator; readiness не наступает.

## Root Cause
Packaging gap → `modules.permissions.first_run.types` не попал в bundle → activator падает → диалоги не показываются → разрешения остаются NOT_DETERMINED → нет `system.ready_to_greet`.

## Optimal Fix
Добавить отсутствующий модуль в PyInstaller spec и пересобрать .app.

## Verification
Проверить лог Nexy: нет `No module named 'modules.permissions.first_run.types'`, появляются events `permissions.first_run_*` и `system.ready_to_greet`.

## Запрос/цель
Сопоставить фактическое поведение с требованиями и обозначить корректный fix.

## Контекст
- Файлы: packaging/Nexy.spec, modules/permissions/first_run/activator.py
- Документы: Docs/PROJECT_REQUIREMENTS.md, Docs/ARCHITECTURE_OVERVIEW.md
- Лог: /var/folders/ys/xlx_chms3hqcs1lfyq37395c0000gn/T/nexy_debug.log

## Решения/выводы
- Нарушен REQ-010 (first-run permissions flow) из-за отсутствующего модуля в bundle.
- Нарушен REQ-011 (restart после выдачи критических разрешений) как следствие незапроса разрешений.

## Открытые вопросы
- Есть ли hiddenimports в packaging/Nexy.spec для `modules.permissions.first_run.types`?

## Следующие шаги
- Добавить hiddenimport и пересобрать .app.
- Повторить first-run и подтвердить readiness.
