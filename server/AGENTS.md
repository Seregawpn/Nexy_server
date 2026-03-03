# PROJECT ASSISTANT RULES — SERVER

Этот файл дополняет корневой `AGENTS.md` и применяется только для серверной части.

## Контекст сервера
- Базовые правила проекта:
  - `../AGENTS.md` (server scope)
  - `../../AGENTS.md` (global scope)
- Обязательные источники:
  - `../../Docs/PROJECT_REQUIREMENTS.md`
  - `../../Docs/ARCHITECTURE_OVERVIEW.md`
  - `../../Docs/ASSISTANT_COORDINATION_PROTOCOL.md`
  - `../../Docs/ANTIGRAVITY_PROMPT.md`
  - `../../Docs/CODEX_PROMPT.md`
  - `../../Docs/assistant_exchange/TEMPLATE.md`
  - `Docs/ARCHITECTURE_OVERVIEW.md`
  - `Docs/SERVER_DEPLOYMENT_GUIDE.md`
  - `Docs/RELEASE_AND_UPDATE_GUIDE.md`
- API-контракт: `modules/grpc_service/streaming.proto`.

## Отчетность ассистента (обязательно)
- После каждого выполненного задания создать отчетный документ.
- Путь: `Docs/assistant_exchange/<assistant>/`.
- Формат имени: `YYYY-MM-DD__type__short-title.md`.
- Типы: `task-brief`, `analysis`, `review`, `handoff`.
- Перезапись запрещена: только новый файл.

## Фокус сервера
- Работай внутри текущих модулей и интеграций сервера.
- Не нарушай существующие границы модулей.

## CRM Task Management (Server)
- Единый алгоритм: `../../Docs/_archive/CRM_ASSISTANT_INSTRUCTIONS.md`.
- Файл задач: `../.crm/TASKS.json` (SRV-XXX).
- После изменений: `python3 ../../scripts/task_aggregator.py`.

## Git Routing Rules (обязательно)
- `Seregawpn/Nexy`:
  - Назначение: корневой workspace (общий код/документация).
  - Push: из `<repo-root>`.
- `Seregawpn/Nexy`:
  - Назначение: только серверный код для Azure deploy.
  - Push: только через subtree из `<repo-root>`.
  - Канонично: `git subtree push --prefix=server origin <branch>`.
- `Seregawpn/Nexy_production`:
  - Назначение: только клиентские release assets и update manifest.
- Запрещено:
  - Пушить root-историю напрямую в `Nexy`.
  - Публиковать DMG/PKG в `Nexy` или `Nexy`.
