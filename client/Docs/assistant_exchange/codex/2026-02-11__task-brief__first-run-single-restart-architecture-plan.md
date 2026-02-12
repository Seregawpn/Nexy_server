# Task Brief: First-run architecture with single restart

## Goal
Сформировать целевую архитектуру first-run: фиксированное ожидание 15 секунд на каждый permission step, один рестарт после завершения всего pipeline, и полный запрет повторных авто-рестартов.

## Architecture Fit
- **Owner**: `modules/permissions/v2/orchestrator.py`
- **SoT**: `permission_ledger.json` (`phase`, `restart_count`, `steps`, `current_step`)
- **Quit intent SoT**: `StateKeys.USER_QUIT_INTENT` в `ApplicationStateManager`
- **Legacy restart path**: отключается при `permissions_v2.enabled=true`

## Target Flow
1. Приложение стартует, V2 orchestrator переводит ledger в `FIRST_RUN`.
2. Каждый шаг разрешений:
   - запускается trigger/probe;
   - выполняется фиксированное ожидание `15s`;
   - по таймауту шаг завершается без блокировки pipeline (независимо от granted/denied).
3. После последнего шага:
   - если `restart_count == 0` и `USER_QUIT_INTENT == false`, выполняется **ровно один** restart;
   - сразу фиксируется `restart_count=1`, `phase=POST_RESTART_VERIFY`.
4. После перезапуска:
   - post-restart verify;
   - переход в `COMPLETED` (или `LIMITED_MODE` по продуктовой политике).
5. Любые будущие restart-ветки блокируются guard-правилом `restart_count >= 1`.

## Restart Trigger Contract
- **Разрешено**:
  - только из V2 orchestrator;
  - только после завершения всех шагов first-run;
  - только при `restart_count == 0`;
  - только при `USER_QUIT_INTENT == false`.
- **Запрещено**:
  - mid-pipeline restart;
  - restart из legacy `permission_restart` при активном V2;
  - повторный restart после первого выполненного.

## Config Policy
- `integrations.permissions_v2.enabled: true`
- `integrations.permissions_v2.advance_on_timeout: true`
- `integrations.permissions_v2.default_step_timeout_s: 15.0`
- `integrations.permissions_v2.restart.require_needs_restart: false` (по вашей целевой модели "всегда один restart после pipeline")

## Cleanup / De-dup
- Отключить/не использовать restart-решения в `permission_restart_integration.py` при V2.
- Убрать decision-роль у legacy flag-файлов (`permissions_first_run_completed.flag`) — только cache/telemetry.
- Оставить единственный writer restart-решения: V2 orchestrator.

## Implementation Steps
1. Зафиксировать timeout-only политику в `config/unified_config.yaml`.
2. Обновить V2 orchestrator:
   - single-restart gate (`restart_count` + `USER_QUIT_INTENT`);
   - единая post-pipeline restart sequence.
3. Обновить first-run integration:
   - корректный stop/cancel V2 task;
   - убрать fallback-дубли публикаций, которые могут переинициировать flow.
4. Обновить permission_restart integration:
   - hard-disable runtime restart path при `permissions_v2.enabled=true`.
5. Добавить тесты:
   - `single_restart_only`;
   - `no_restart_after_first_restart`;
   - `quit_cancels_pending_restart`.

## DoD
- Fresh install: ровно один auto-restart после завершения всех first-run шагов.
- После этого нет авто-рестартов при повторных запусках/выключениях.
- При user quit до рестарта auto-restart не происходит.
- Логи подтверждают: `restart_count` изменился ровно `0 -> 1`.

