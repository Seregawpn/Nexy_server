# Database Schema DDL

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-01-02

## Запрос/цель
Создать базовый SQL (DDL) для PostgreSQL, соответствующий текущему коду server/modules/database.

## Контекст
- Файлы: server/Docs/DATABASE_SCHEMA.sql
- Документы: server/modules/database/providers/postgresql_provider.py
- Ограничения: структура должна соответствовать используемым таблицам/функциям

## Решения/выводы
- Добавлен DDL с таблицами users/sessions/commands/llm_answers/screenshots/performance_metrics и функциями cleanup_expired_short_term_memory/get_memory_stats.

## Открытые вопросы
- Нужно ли использовать отдельную схему (не public) или префикс таблиц.

## Следующие шаги
- Выполнить DDL в PostgreSQL и проверить наличие таблиц/функций.
