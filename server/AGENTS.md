# PROJECT ASSISTANT RULES — SERVER

Этот файл дополняет корневой `AGENTS.md` и применяется только для серверной части.

## Контекст Сервера
- **Базовые правила проекта**: `AGENTS.md` (в корне).
- **Обязательные источники**:
  - `Docs/ANTIGRAVITY_PROMPT.md`
  - `Docs/CODEX_PROMPT.md`
  - `Docs/ASSISTANT_COORDINATION_PROTOCOL.md`
- **Архитектура (global)**: `Docs/ARCHITECTURE_OVERVIEW.md`.
- **Архитектура (server runtime)**: `server/server/Docs/ARCHITECTURE_OVERVIEW.md`.
- **Feature flags (server runtime)**: `server/server/Docs/FEATURE_FLAGS.md`.
- **API Контракты**: `server/server/modules/grpc_service/streaming.proto`.

## Pre-Change Gate (обязательно до любых правок кода)
- Сначала прочитай и зафиксируй релевантные разделы:
  - `AGENTS.md` (корень)
  - `Docs/DOCS_INDEX.md` и `Docs/PRE_CHANGE_CHECKLIST.md` (корневой процесс)
  - `server/server/Docs/DOCS_INDEX.md` и `server/server/Docs/PRE_CHANGE_CHECKLIST.md` (server runtime)
  - `server/server/Docs/ARCHITECTURE_OVERVIEW.md`
  - `server/server/Docs/FEATURE_FLAGS.md`
- Перед изменениями проверь дубликаты/параллельные пути (>=70% сходства) и зафиксируй единого владельца (Source of Truth).
- Для API-изменений: сначала `server/server/modules/grpc_service/streaming.proto`, затем регенерация и downstream изменения.
- Если gate не пройден, изменения не вносить.

## Правило источников
- `server/server/Docs/_archive/*` — только historical reference, не Source of Truth.
- При конфликте использовать canonical-документы из `server/server/Docs/DOCS_INDEX.md`, затем корневой `Docs/DOCS_INDEX.md`.

## Фокус Области (Server Scope)
- `server/modules`: Основная логика и сервисы.
- `server/integrations`: Интеграционные слои (если применимо).
- `server/Docs`: Документация, специфичная для сервера.

## Отчетность Antigravity (обязательно)
- После каждого выполненного задания создать отчетный документ.
- Путь: `server/Docs/assistant_exchange/antigravity/` или `Docs/assistant_exchange/antigravity/` по контексту задачи.
- Формат имени: `YYYY-MM-DD__type__short-title.md`.
- Типы: `task-brief`, `analysis`, `review`, `handoff`.

## Инструкции по Задачам (CRM)
- При создании задач используй префикс `SRV-` (например, `SRV-001`).
- Файл задач: `server/.crm/TASKS.json`.
- Единый алгоритм: `Docs/_archive/CRM_ASSISTANT_INSTRUCTIONS.md` (reference).
- После изменений: `python3 scripts/task_aggregator.py`.

## Правила
1. **gRPC First**: Любые изменения API должны начинаться с `.proto` файлов и обновления стабов.
2. **Стабильность**: Сервер должен быть stateless (по возможности) и отказоустойчивым.
3. **Изоляция**: Модули сервера не должны зависеть от клиента.
