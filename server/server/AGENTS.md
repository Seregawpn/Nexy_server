# PROJECT ASSISTANT RULES — SERVER

Этот файл дополняет корневой `AGENTS.md` и применяется только для серверной части.

## Контекст сервера
- Базовые правила проекта: `AGENTS.md` (в корне).
- Архитектура и текущие принципы: `server/server/Docs/ARCHITECTURE_OVERVIEW.md`.
- Feature flags: `server/server/Docs/FEATURE_FLAGS.md`.
- Серверные правила разработки: `server/server/Docs/SERVER_DEVELOPMENT_RULES.md`.
- Документационный индекс: `server/server/Docs/DOCS_INDEX.md`.

## Pre-Change Gate (обязательно до любых правок кода)
- Сначала прочитай и зафиксируй релевантные разделы:
  - `AGENTS.md` (корень)
  - `Docs/DOCS_INDEX.md` и `Docs/PRE_CHANGE_CHECKLIST.md` (корневой процесс)
  - `server/server/Docs/DOCS_INDEX.md` и `server/server/Docs/PRE_CHANGE_CHECKLIST.md` (server runtime)
  - `server/server/Docs/ARCHITECTURE_OVERVIEW.md`
  - `server/server/Docs/FEATURE_FLAGS.md`
  - `server/server/Docs/SERVER_DEVELOPMENT_RULES.md`
- Перед изменениями проверь дубликаты/параллельные пути (>=70% сходства) и зафиксируй единого владельца (Source of Truth).
- Любые изменения API начинаются с `server/server/modules/grpc_service/streaming.proto`, затем регенерация protobuf.
- Если gate не пройден, изменения не вносить.

## Правило источников
- `server/server/Docs/_archive/*` — только historical reference, не Source of Truth.
- При конфликте использовать canonical-документы из `server/server/Docs/DOCS_INDEX.md`, затем корневой `Docs/DOCS_INDEX.md`.

## Отчетность ассистента (обязательно)
- После каждого выполненного задания создать отчетный документ.
- Путь: `server/Docs/assistant_exchange/<assistant>/` или `Docs/assistant_exchange/<assistant>/` по контексту задачи.
- Формат имени: `YYYY-MM-DD__type__short-title.md`.
- Типы: `task-brief`, `analysis`, `review`, `handoff`.
- Перезапись запрещена: только новый файл.

## Фокус сервера
- Работай внутри текущих модулей и интеграций сервера.
- Не нарушай существующие границы модулей.

## CRM Task Management (Server)
- Единый алгоритм: `Docs/_archive/CRM_ASSISTANT_INSTRUCTIONS.md` (reference).
- Файл задач: `server/.crm/TASKS.json` (SRV-XXX).
- После изменений: `python3 scripts/task_aggregator.py`.
