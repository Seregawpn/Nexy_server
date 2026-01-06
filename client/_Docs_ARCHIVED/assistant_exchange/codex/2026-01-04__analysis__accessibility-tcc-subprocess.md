# Accessibility TCC Subprocess Isolation

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-04

## Запрос/цель
- Устранить падение из-за TCCAccessRequest для Accessibility путем изоляции проверки в subprocess.

## Контекст
- Файлы: modules/permissions/macos/accessibility_handler.py, modules/permissions/first_run/status_checker.py
- Документы: Docs/PROJECT_REQUIREMENTS.md (REQ-013), Docs/ARCHITECTURE_OVERVIEW.md
- Ограничения: не менять архитектуру, избегать дублирования логики

## Решения/выводы
- Вынесен общий subprocess-чек AX в helper внутри accessibility_handler, чтобы избежать прямого вызова AXIsProcessTrustedWithOptions в основном процессе.
- status_checker переиспользует helper, убрана дублирующая реализация.
- Поведение и маппинг статусов сохранены (ok/import_error/timeout/error).

## Открытые вопросы
- Нет.

## Следующие шаги
- Пересборка пакета и проверка first-run, логирование tccd без TCCAccessRequest ошибок.
