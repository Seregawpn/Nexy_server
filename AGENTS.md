# PROJECT ASSISTANT RULES — SERVER

Этот файл дополняет корневой `AGENTS.md` и применяется только для серверной части.

## Контекст Сервера
- **Базовые правила проекта**: `AGENTS.md` (в корне).
- **Обязательные источники**:
  - `../AGENTS.md`
  - `../Docs/PROJECT_REQUIREMENTS.md`
  - `../Docs/ARCHITECTURE_OVERVIEW.md`
  - `../Docs/ASSISTANT_COORDINATION_PROTOCOL.md`
  - `../Docs/ANTIGRAVITY_PROMPT.md`
  - `../Docs/CODEX_PROMPT.md`
  - `../Docs/assistant_exchange/TEMPLATE.md`
  - `server/Docs/ARCHITECTURE_OVERVIEW.md`
  - `server/Docs/SERVER_DEPLOYMENT_GUIDE.md`
  - `server/Docs/RELEASE_AND_UPDATE_GUIDE.md`
- **Архитектура**: `server/Docs/ARCHITECTURE_OVERVIEW.md`.
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
- Файл задач: `.crm/TASKS.json`.
- Единый алгоритм: `../Docs/_archive/CRM_ASSISTANT_INSTRUCTIONS.md`.
- После изменений: `python3 ../scripts/task_aggregator.py`.

## Правила
1. **gRPC First**: Любые изменения API должны начинаться с `.proto` файлов и обновления стабов.
2. **Стабильность**: Сервер должен быть stateless (по возможности) и отказоустойчивым.
3. **Изоляция**: Модули сервера не должны зависеть от клиента.

## Git Routing Rules (обязательно)
- `Seregawpn/Nexy` получает push только из корня текущего workspace (`<repo-root>`).
- `Seregawpn/Nexy_server` получает только `server`-срез из `<repo-root>`.
- `Seregawpn/Nexy_production` используется только для release assets (`Nexy.dmg`, `Nexy.pkg`) и update manifest.
- Запрещено пушить root-историю напрямую в `Nexy_server`.
- Запрещено смешивать code-pipeline и asset-pipeline.
- Каноничная команда для `Nexy_server`:
  - `git subtree push --prefix=server server_repo <branch>`
- Для уже существующей ветки в `Nexy_server` допускается выравнивание:
  - `git subtree split --prefix=server -b <tmp-branch>`
  - `git push --force server_repo <tmp-branch>:<branch>`
