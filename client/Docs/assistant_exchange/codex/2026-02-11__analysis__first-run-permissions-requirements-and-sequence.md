# Analysis: First-run permissions requirements and sequence (implementation baseline)

## 1. Назначение
Документ фиксирует обязательные требования для текущей реализации first-run permissions:
- когда и как работает логика;
- как работает визуальная индикация (закрашивание);
- в какой последовательности идет flow;
- когда и при каких условиях происходит restart.

Этот документ является базой для реализации и проверки регрессий.

---

## 2. Область действия
- Клиент: macOS (`client/`).
- Подсистема: first-run permissions + tray visual state + restart orchestration.
- Главный owner restart решения: `modules/permissions/v2/orchestrator.py`.

---

## 3. Функциональные требования

### R-01: Timebox на шаг
- Каждый шаг permissions в first-run имеет фиксированный таймбокс `15s`.
- По истечении таймбокса шаг считается завершенным для pipeline (не блокирует следующий шаг).

### R-02: Последовательность шагов
- Порядок шагов берется только из `integrations.permissions_v2.order`.
- Параллельный запуск шагов запрещен.

### R-03: Единый restart
- После завершения всех шагов pipeline выполняется ровно один restart.
- Условия допуска restart:
  - `restart_count == 0`
  - `USER_QUIT_INTENT == false`
  - решение принято V2 owner.

### R-04: Запрет повторного restart
- После первого restart (`restart_count >= 1`) повторный auto-restart запрещен.

### R-05: Приоритет user quit
- Если выставлен `USER_QUIT_INTENT=true`, restart не должен запускаться.

### R-06: Legacy path isolation
- При активном V2 (`permissions_v2.enabled=true`) legacy `permission_restart` path не должен инициировать restart.

---

## 4. Требования к визуальной индикации (закрашивание)

### V-01: Только 3 режима tray
- Допустимы только 3 статуса: `SLEEPING`, `LISTENING`, `PROCESSING`.
- Отдельный режим блокировки для first-run запрещен.

### V-02: Восстановление после завершения
- При `permissions.first_run_completed`/`permissions.first_run_failed` tray возвращается к статусу текущего режима приложения через sync с mode.

### V-03: Канонические цвета
- `SLEEPING` -> серый (`#808080`)
- `LISTENING` -> синий (`#007AFF`)
- `PROCESSING` -> оранжевый (`#FF9500`)

### V-04: Централизация визуальной логики
- Изменение иконки/цвета только через `TrayControllerIntegration`.
- Прямые изменения цвета из других модулей запрещены.

---

## 5. Событийный контракт (Event Contract)

### Входные события
- `permissions.first_run_started`
- `permissions.first_run_completed`
- `permissions.first_run_failed`
- `tray.quit_clicked` (для установки quit-intent)

### Выходные события (минимум)
- `permissions.v2.*` (phase/step events)
- `tray.status_updated`
- restart-trigger через `PermissionsRestartHandler.trigger_restart()` (внутри V2 owner)

### Порядок (happy path)
1. `permissions.first_run_started`
2. Pipeline steps (15s каждый)
3. End-of-pipeline decision
4. `trigger_restart()` один раз
5. New process -> `POST_RESTART_VERIFY`
6. `COMPLETED`

---

## 6. Конфигурационные требования (минимальный набор)

### Keep (обязательные)
- `integrations.permissions_v2.enabled=true`
- `integrations.permissions_v2.advance_on_timeout=true`
- `integrations.permissions_v2.default_step_timeout_s=15.0`
- `integrations.permissions_v2.order`
- `integrations.permissions_v2.steps.*`
- `integrations.permissions_v2.restart.delay_sec`
- `integrations.permissions_v2.restart.require_all_hard_pass=true`
- `integrations.permissions_v2.restart.require_needs_restart=false` (для текущей целевой модели)
- `NEXY_DISABLE_AUTO_RESTART` (dry-run)
- `NEXY_KS_FIRST_RUN_RESTART` (emergency kill-switch)

### Freeze (временно, без влияния на решение)
- `permissions.first_run.batch_*`
- `features.use_events_for_restart_pending`
- `features.ks_first_run_normalization`
- `integrations.permission_restart.enabled` (не влияет на restart decision при V2)

### Remove (после стабилизации)
- runtime-ветки legacy `permission_restart` для first-run
- `permissions.first_run_restart_pending` как owner restart-решения
- doc-only runtime-неиспользуемые флаги:
  - `NEXY_FEATURE_FIRST_RUN_V2`
  - `NEXY_FEATURE_PERMISSION_RESTART_V2`

---

## 7. Анти-конфликтные правила реализации
- Один owner restart-решения.
- Один SoT (`ledger`) для фазы и счетчика restart.
- Один SoT (`USER_QUIT_INTENT`) для отмены restart.
- Любой дубль условий restart вне owner считается дефектом.
- Любая визуальная логика вне tray owner считается дефектом.

---

## 8. Проверка (DoD)
- Fresh install:
  - lock (красный) появляется на старте first-run;
  - шаги проходят по 15s timebox;
  - после pipeline ровно один restart.
- После restart:
  - повторный auto-restart отсутствует.
- User quit до restart:
  - restart отменен.
- В логах:
  - один переход `restart_count: 0 -> 1`;
  - нет legacy restart scheduling при V2 enabled.
