# Analysis: Quit/Restart Conflict — Architecture Gates

Дата: 2026-02-12
Ассистент: Codex
Тип: analysis

## 1. Контекст и цель

Цель: перед любыми изменениями зафиксировать текущий архитектурный контракт для `first-run / restart / user quit`, чтобы не сломать рабочий V2 flow и не создать второй источник истины.

## 2. Использованные источники

- `Docs/PROJECT_REQUIREMENTS.md`
- `Docs/ARCHITECTURE_OVERVIEW.md`
- `Docs/first_run_flow_spec.md`
- Runtime код:
  - `modules/permissions/v2/orchestrator.py`
  - `modules/permissions/v2/integration.py`
  - `integration/integrations/first_run_permissions_integration.py`
  - `integration/integrations/permission_restart_integration.py`
  - `integration/core/simple_module_coordinator.py`
  - `modules/permission_restart/macos/permissions_restart_handler.py`

Примечание: `Docs/ASSISTANT_COORDINATION_PROTOCOL.md` и `Docs/CODEX_PROMPT.md` отсутствуют в текущем `Docs/`.

## 3. As-Is архитектурный контракт (подтверждено)

### 3.1 Source of Truth

- First-run lifecycle: `permission_ledger.json` (`phase`, `restart_count`) — основной SoT.
- Runtime quit-state: `StateKeys.USER_QUIT_INTENT`.

### 3.2 Owner-модули

- Решение о рестарте first-run: `modules/permissions/v2/orchestrator.py`.
- Транспорт рестарта (single-flight/lock/atomic flag): `modules/permission_restart/macos/permissions_restart_handler.py`.
- Гейтинг старта интеграций по first-run/restart state: `integration/core/simple_module_coordinator.py`.
- Legacy restart runtime path: `integration/integrations/permission_restart_integration.py` (заморожен при V2, но код и подписки частично остаются).

### 3.3 Канонический поток (рабочий)

1. `FIRST_RUN` (каждый шаг = `grace 15s`)
2. `RESTART_PENDING`
3. `RESTART_STARTED`
4. новый процесс
5. `POST_RESTART_VERIFY`
6. `COMPLETED`

## 4. Обнаруженные архитектурные риски (без правок)

### R1. Остаточный legacy-contract в coordinator

- `SimpleModuleCoordinator` подписан на `permissions.first_run_restart_pending`.
- При V2 owner рестарта — orchestrator, а не legacy event path.
- Риск: дублирующий путь семантики restart pending (контрактовый шум, потенциальная рассинхронизация по state flags).

### R2. Legacy restart integration содержит множество fallback веток

- `PermissionRestartIntegration` в V2 режиме в основном frozen, но код веток resume/pending/gateway scheduling остается.
- Риск: при конфигурационном дрейфе может частично реактивироваться не-owner путь.

### R3. Quit vs Restart race в узком окне

- `USER_QUIT_INTENT` guard уже есть.
- Но при узком timing окне между постановкой quit intent и уже запланированным restart task возможен конфликтный сценарий (редкий).

## 5. Допустимые изменения (architecture-safe only)

### 5.1 Что можно менять

- Только owner-точки:
  - `orchestrator` (решение)
  - `restart_handler` (исполнение)
  - `coordinator` (state gating и event wiring)
- Только guards/idempotency/удаление legacy-ветвей.

### 5.2 Что нельзя менять

- Нельзя добавлять новый SoT-флаг вместо ledger/state manager.
- Нельзя вводить альтернативный restart owner вне V2 orchestrator.
- Нельзя переносить restart decision в интеграции, которые не являются owner.

## 6. Минимальный безопасный план (до код-изменений)

1. Зафиксировать owner-матрицу в задаче (V2 orchestrator = единственный restart owner).
2. Подтвердить, что `permissions.first_run_restart_pending` не является каноническим входом для V2 режима.
3. Подтвердить приоритет `USER_QUIT_INTENT` над любым restart scheduling.
4. Только после этого делать точечную очистку legacy-подписок/ветвей.

## 7. Проверка после будущих изменений (DoD)

1. Ручной `Quit` из tray:
   - нет нового `NEXY APPLICATION START` после quit.
   - нет `Restart requested` после `USER_QUIT_INTENT=True`.
2. First-run:
   - ровно один auto-restart.
   - после рестарта `POST_RESTART_VERIFY -> COMPLETED`.
3. Нет дублирующих источников решения о restart/completion.

## 8. Итог

Текущая архитектура уже близка к целевой: V2 централизует first-run/restart.
Проблема — остаточные legacy-contract точки, которые нужно чистить только через owner-first подход, без добавления новых состояний и без реархитектуры.
