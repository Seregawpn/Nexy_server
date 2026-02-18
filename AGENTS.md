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
- **Локальный inbox инцидентов (оперативный triage)**: `monitor_inbox/` (в корне текущего workspace `server`).

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
4. **Incident Inbox First (обязательно)**:
   - Перед диагностикой/фиксом сначала проверять `monitor_inbox/` и последний `*__incident__server-monitor.md`.
   - Если есть активный инцидент-документ, triage вести по нему как по первичному источнику фактов.
   - Если `monitor_inbox/` пуст, запускать `server/scripts/publish_server_incident_local.sh` и только затем переходить к ручным проверкам.

## Architecture Gate Policy (обязательно)
- Любой PR в server обязан проходить `Server Quality Gate` (`.github/workflows/server-quality.yml`).
- Обязательные проверки в CI:
  - `python scripts/verify_docs_root_server_links.py`
  - `python server/scripts/verify_pr_single_owner_check.py`
  - `python server/scripts/verify_feature_flags.py`
  - `python server/scripts/verify_architecture_guards.py`
- PR без блока `Single Owner Check` (owner/duplicate removed/no second path/legacy removal date) невалиден.
- Запрещено добавлять новый runtime second path (legacy/workaround) без срока удаления `LEGACY_REMOVE_BY: YYYY-MM-DD`.
- Запрещено добавлять новые runtime ветки с `use_*` / `disable_*` без регистрации в `server/Docs/FEATURE_FLAGS.md`.
- Правило `one event, one owner` обязательно для критичных intent-событий; owner для `mcp.command_request` — `server/integrations/core/assistant_response_parser.py`.

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
