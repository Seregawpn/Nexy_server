# Documentation Reality Audit

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-15
- ID (INS-###): N/A

## Diagnosis
Корневые документы `Docs/PROJECT_REQUIREMENTS.md` и `Docs/ARCHITECTURE_OVERVIEW.md` частично не соответствуют текущей структуре и рантайму: указаны устаревшие пути, числа интеграций/модулей и старые детали first-run.

## Root Cause
Исторический сдвиг структуры в `client/` и `server/server/` + параллельное существование legacy-документов (`server/Docs`) без одного владельца канона на уровне root → документы расходятся с фактическими владельцами логики в коде.

## Optimal Fix
Goal: вернуть документацию к состоянию "исполняемый канон": все пути, владельцы и контракты соответствуют текущему коду без двусмысленности.

Architecture Fit:
- Where it belongs: документационные каноны root + client + server.
- Source of Truth:
  - Клиент: `client/Docs/ARCHITECTURE_OVERVIEW.md`, `client/Docs/FLOW_INTERACTION_SPEC.md`, `client/Docs/STATE_CATALOG.md`
  - Сервер: `server/server/Docs/ARCHITECTURE_OVERVIEW.md`, `server/server/Docs/FLOW_INTERACTION_SPEC.md`
  - Root: только индекс/маршрутизация на каноны, без дублирования деталей реализации.

Breaks architecture: no

Implementation Plan:
1. Обновить `Docs/PROJECT_REQUIREMENTS.md`: заменить пути `integration/...`, `modules/...`, `scripts/...`, `tests/...`, `Docs/...` на фактические `client/...` (и серверные при необходимости).
2. Синхронизировать REQ-006 с `client/integration/core/integration_factory.py::STARTUP_ORDER`.
3. Обновить разделы first-run: убрать ссылки на `modules/permissions/first_run/*`; указать `client/modules/permissions/v2/*` и текущие конфиги (`inter_step_pause_s: 0.0`, `pause_between_requests_sec: 15.0`).
4. Обновить/сократить `Docs/ARCHITECTURE_OVERVIEW.md`: убрать устаревший snapshot "Октябрь 2025" и оставить индекс на `client/Docs/...` и `server/server/Docs/...`.
5. Явно пометить `server/Docs` как legacy/исторический контур, чтобы исключить второй источник истины.
6. Добавить lightweight CI-проверку на существование всех путей из `Docs/PROJECT_REQUIREMENTS.md`.

Code Touchpoints:
- `Docs/PROJECT_REQUIREMENTS.md`
- `Docs/ARCHITECTURE_OVERVIEW.md`
- `client/integration/core/integration_factory.py`
- `client/config/unified_config.yaml`
- `client/modules/permissions/v2/`
- `server/server/Docs/ARCHITECTURE_OVERVIEW.md`

Concurrency Guard (if needed):
- not needed (документационные изменения)

What to remove / merge:
- Удалить дублирующие runtime-детали из root `Docs/ARCHITECTURE_OVERVIEW.md`.
- Свести root-описание к маршрутизатору на канонические документы client/server.

## Verification
- Проверка существования путей:
  - `Docs/STATE_CATALOG.md` отсутствует, при этом `client/Docs/STATE_CATALOG.md` существует.
  - `integration/core/...` отсутствует в root, фактически существует `client/integration/core/...`.
- Проверка инициализации:
  - Канон старта: `client/integration/core/integration_factory.py` строки 67-93.
- Проверка first-run:
  - Конфиг: `client/config/unified_config.yaml` строки 231-260 и 400-404.
  - Реализация: `client/integration/integrations/first_run_permissions_integration.py` (V2 only).
- Проверка количества:
  - Интеграций: `find client/integration/integrations -name "*_integration.py" | wc -l` = 25.
  - Модулей: `find client/modules ... | wc -l` = 24 (без `_module_template`, `__pycache__`).

## Запрос/цель
Проверить, насколько текущая документация проекта соответствует фактической реализации, и определить необходимые уточнения/изменения.

## Контекст
- Файлы:
  - `Docs/PROJECT_REQUIREMENTS.md`
  - `Docs/ARCHITECTURE_OVERVIEW.md`
  - `client/Docs/ARCHITECTURE_OVERVIEW.md`
  - `client/Docs/FLOW_INTERACTION_SPEC.md`
  - `client/integration/core/integration_factory.py`
  - `client/integration/integrations/first_run_permissions_integration.py`
  - `client/config/unified_config.yaml`
- Документы:
  - `Docs/ASSISTANT_COORDINATION_PROTOCOL.md`
  - `Docs/CODEX_PROMPT.md`
- Ограничения: без изменения архитектуры, только выравнивание документации с существующим кодом.

## Решения/выводы
- Корневые документы сейчас частично устарели относительно реальной структуры (`client/*`, `server/server/*`).
- Канонические клиентские документы заметно ближе к реальности, но root-дубликаты создают конфликт источников истины.
- Требуется точечная синхронизация, а не реархитектура.

## Открытые вопросы
- Нужно ли сохранять детальные runtime-описания в root `Docs/ARCHITECTURE_OVERVIEW.md` или полностью оставить root как index-only?

## Следующие шаги
1. Согласовать политику root (index-only vs full mirror).
2. Внести правки в `Docs/PROJECT_REQUIREMENTS.md` и `Docs/ARCHITECTURE_OVERVIEW.md`.
3. Добавить автоматическую проверку существования путей из требований.
