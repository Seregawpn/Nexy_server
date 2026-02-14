# PROJECT ASSISTANT RULES — SERVER

Этот файл дополняет корневой `AGENTS.md` и применяется только для серверной части.

## Контекст сервера
- Базовые правила проекта:
  - `../AGENTS.md` (server scope)
  - `../../AGENTS.md` (global scope)
- Обязательные источники:
  - `../../Docs/PROJECT_REQUIREMENTS.md`
  - `../../Docs/ARCHITECTURE_OVERVIEW.md`
  - `../../Docs/_archive/ASSISTANT_COORDINATION_PROTOCOL.md`
  - `../../Docs/_archive/ANTIGRAVITY_PROMPT.md`
  - `../../Docs/_archive/CODEX_PROMPT.md`
  - `../../Docs/_archive/assistant_exchange/TEMPLATE.md`
  - `../Docs/RELEASE_AND_UPDATE_GUIDE.md`
  - `Docs/ARCHITECTURE_OVERVIEW.md`
- API-контракт: `modules/grpc_service/streaming.proto`.

## Отчетность ассистента (обязательно)
- После каждого выполненного задания создать отчетный документ.
- Путь: `../Docs/assistant_exchange/<assistant>/`.
- Формат имени: `YYYY-MM-DD__type__short-title.md`.
- Типы: `task-brief`, `analysis`, `review`, `handoff`.
- Перезапись запрещена: только новый файл.

## Фокус сервера
- Работай внутри текущих модулей и интеграций сервера.
- Не нарушай существующие границы модулей.
- GitHub routing:
  - `commit/push/tag` сервера выполняются только в `https://github.com/Seregawpn/Nexy_server`.
  - Версии сервера должны быть доступны через git-теги `vX.Y.Z.BUILD` в `Nexy_server`.
  - Публикация release-артефактов (`Nexy.dmg`/`Nexy.pkg`) выполняется только в `https://github.com/Seregawpn/Nexy_production`.
  - В `Nexy_server` GitHub Release не создаются.

## CRM Task Management (Server)
- Единый алгоритм: `../../Docs/_archive/CRM_ASSISTANT_INSTRUCTIONS.md`.
- Файл задач: `../.crm/TASKS.json` (SRV-XXX).
- После изменений: `python3 ../scripts/task_aggregator.py`.
