# PROJECT ASSISTANT RULES — SERVER

Этот файл дополняет корневой `AGENTS.md` и применяется только для серверной части.

## Контекст Сервера
- **Базовые правила проекта**: `AGENTS.md` (в корне).
- **Обязательные источники**:
  - `Docs/Antigravity/PROMPT.md`
  - `Docs/Codex/PROMPT.md`
  - `Docs/ASSISTANT_COORDINATION_PROTOCOL.md`
  - `server/docs/RELEASE_AND_UPDATE_GUIDE.md` (Процесс релиза и обновлений)
- **Архитектура**: `Docs/ARCHITECTURE_OVERVIEW.md`.
- **API Контракты**: `server/modules/grpc_service/streaming.proto`.

## Фокус Области (Server Scope)
- `server/modules`: Основная логика и сервисы.
- `server/integrations`: Интеграционные слои (если применимо).
- `server/Docs`: Документация, специфичная для сервера.

## Отчетность Antigravity (обязательно)
- После каждого выполненного задания создать отчетный документ.
- Путь: `Docs/assistant_exchange/antigravity/`.
- Формат имени: `YYYY-MM-DD__type__short-title.md`.
- Типы: `task-brief`, `analysis`, `review`, `handoff`.

## Инструкции по Задачам (CRM)
- При создании задач используй префикс `SRV-` (например, `SRV-001`).
- Файл задач: `server/.crm/TASKS.json`.
- Единый алгоритм: `Docs/CRM_ASSISTANT_INSTRUCTIONS.md`.
- После изменений: `python3 scripts/task_aggregator.py`.

## Правила
1. **gRPC First**: Любые изменения API должны начинаться с `.proto` файлов и обновления стабов.
2. **Стабильность**: Сервер должен быть stateless (по возможности) и отказоустойчивым.
3. **Изоляция**: Модули сервера не должны зависеть от клиента.
