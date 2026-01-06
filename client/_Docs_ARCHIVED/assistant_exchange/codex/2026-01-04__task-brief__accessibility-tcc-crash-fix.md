# Accessibility TCC Crash Fix

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-01-04

## Запрос/цель
- Зафиксировать и описать исправление crash из-за TCCAccessRequest (Accessibility) через subprocess-изоляцию.

## Контекст
- Файлы: modules/permissions/macos/accessibility_handler.py, modules/permissions/first_run/status_checker.py
- Документы: Docs/PROJECT_REQUIREMENTS.md (REQ-013)
- Ограничения: без изменения архитектуры, без новых источников истины

## Решения/выводы
- Проверка Accessibility выполняется в /usr/bin/python3 subprocess, основной процесс больше не вызывает AX напрямую.
- Дублирующая логика в status_checker использует общий helper.

## Открытые вопросы
- Нет.

## Следующие шаги
- Прогнать first-run по инструкции и проверить TCC логи на отсутствие TCCAccessRequest ошибок.
