# Docs Actuality Client Server Sync

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-11
- ID (INS-###): N/A

## Diagnosis
Часть ключевой документации client/server ссылалась на несуществующие файлы и старые пути, что давало ложные Source of Truth перед изменениями.

## Root Cause
Реорганизация структуры (`server/server`, архивы, перенос canonical docs) не была полностью синхронизирована в README/AGENTS/rules-файлах.

## Optimal Fix
Обновлены пути и ссылки в `client/Docs/README.md`, `client/Docs/DOCUMENTATION_MAP.md`, `server/server/Docs/SERVER_DEVELOPMENT_RULES.md`, `server/AGENTS.md`, `server/server/AGENTS.md`; удалены/заменены битые ссылки на существующие canonical или archive-reference документы.

## Verification
Проведена проверка ссылок в целевых файлах; удалены ссылки на `Docs/UPDATE_SYSTEM_FIXES.md`, `Docs/RAMP_PLAN.md`, `Docs/MCP_INTEGRATION_SUMMARY.md`, `Docs/CURRENT_STATUS_REPORT.md`, `Docs/CRM_ASSISTANT_INSTRUCTIONS.md`, старый proto путь и устаревший `integration/core/gateways.py`.

## Pre-Change Gate Evidence (обязательно)
- Прочитанные документы: `Docs/DOCS_INDEX.md`, `Docs/PRE_CHANGE_CHECKLIST.md`, `client/Docs/DOCS_INDEX.md`, `server/server/Docs/DOCS_INDEX.md`
- Source of Truth: root/docs indexes + workspace AGENTS
- Дублирование: объединены и синхронизированы process-ссылки
- Feature Flags check: server/client ссылочные пути оставлены на существующие `FEATURE_FLAGS.md`
- Race check: N/A (документационные правки)

## Запрос/цель
Проверить актуальность документации относительно реального кода и синхронизировать устаревшие ссылки.

## Контекст
- Файлы: `client/Docs/README.md`, `client/Docs/DOCUMENTATION_MAP.md`, `server/server/Docs/SERVER_DEVELOPMENT_RULES.md`, `server/AGENTS.md`, `server/server/AGENTS.md`

## Решения/выводы
- Актуализированы ключевые рабочие документы для ассистентов.
- Для отсутствующих канонических CRM/Canary/Beta материалов выставлены archive-reference ссылки.

## Открытые вопросы
- Нужна ли дополнительная чистка второстепенных исторических документов за пределами ключевых process-файлов.

## Следующие шаги
- При изменениях документации запускать такой же ссылочный аудит как обязательный pre-merge шаг.
