# PROJECT ASSISTANT RULES — SERVER

Этот файл дополняет корневой `AGENTS.md` и применяется только для серверной части.

## Контекст Сервера
- **Базовые правила проекта**: `AGENTS.md` (в корне).
- **Обязательные источники**:
  - `../Docs/PROJECT_REQUIREMENTS.md`
  - `../Docs/ARCHITECTURE_OVERVIEW.md`
  - `../Docs/_archive/ASSISTANT_COORDINATION_PROTOCOL.md`
  - `../Docs/_archive/ANTIGRAVITY_PROMPT.md`
  - `../Docs/_archive/CODEX_PROMPT.md`
  - `../Docs/_archive/assistant_exchange/TEMPLATE.md`
  - `Docs/RELEASE_AND_UPDATE_GUIDE.md` (Процесс релиза и обновлений)
- **Архитектура (server)**: `server/Docs/ARCHITECTURE_OVERVIEW.md`.
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
- Единый алгоритм: `../Docs/_archive/CRM_ASSISTANT_INSTRUCTIONS.md`.
- После изменений: `python3 scripts/task_aggregator.py`.

## Правила
1. **gRPC First**: Любые изменения API должны начинаться с `.proto` файлов и обновления стабов.
2. **Стабильность**: Сервер должен быть stateless (по возможности) и отказоустойчивым.
3. **Изоляция**: Модули сервера не должны зависеть от клиента.
4. **GitHub Routing (обязательно)**:
   - Серверный код (`commit/push/tag`) публикуется только в `https://github.com/Seregawpn/Nexy_server`.
   - Серверные версии фиксируются git-тегами вида `vX.Y.Z.BUILD` в `Nexy_server`.
   - Release-артефакты (`Nexy.dmg`, `Nexy.pkg`) публикуются только в `https://github.com/Seregawpn/Nexy_production` (теги `Update` и `App`).
   - Запрещено делать GitHub Release в `Nexy_server`.

## Быстрая самопроверка источников
Перед задачей проверь, что обязательные пути существуют. Если путь недоступен, сначала зафиксируй это в отчете и используй ближайший валидный источник из списка выше.
