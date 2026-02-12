# Analysis: quit -> relaunch после установки (first-run)

## Diagnosis
- Симптом "после Quit приложение снова запускается" в текущей архитектуре совпадает с конфликтом в `permissions_v2 restart` пути, а не только с автозапуском.
- В конфиге включен режим `require_needs_restart: false`, который делает рестарт фактически обязательным после прохождения hard-permissions.

## Root Cause
1. `permissions_v2` может инициировать рестарт даже без `needs_restart`.
   - `config/unified_config.yaml`: `permissions_v2.restart.require_needs_restart: false`.
   - `modules/permissions/v2/orchestrator.py::should_restart()` при `require_needs_restart=false` возвращает `True` при наличии hard_permissions.
2. На пути user quit нет единого cancel-гейта для V2 orchestrator restart.
   - `modules/permissions/v2/orchestrator.py::_enter_restart_sequence()` вызывает `trigger_restart()` без проверки `USER_QUIT_INTENT`.
   - `integration/integrations/first_run_permissions_integration.py::stop()` не останавливает `self._v2_integration`.
3. Дополнительный race в tray quit path.
   - `modules/tray_controller/core/tray_controller.py::_on_quit_clicked()` отправляет `quit_clicked` async и сразу делает `tray_menu.quit()`, что может не успеть выставить `USER_QUIT_INTENT` до завершения UI цикла.
4. Автозапуск как вторичный фактор.
   - В этом workspace `postinstall` LaunchAgent не ставит; `~/Library/LaunchAgents` и `/Library/LaunchAgents` не содержат `com.nexy*` plist.
   - Но legacy/внешний LaunchAgent на машине пользователя всё равно может усиливать симптом.

## Architecture Fit
- Owner рестарта при first-run V2: `PermissionOrchestrator` (`modules/permissions/v2/orchestrator.py`).
- Source of Truth для user quit: `StateKeys.USER_QUIT_INTENT` в `ApplicationStateManager`.
- Фикс должен быть в существующих владельцах (V2 orchestrator + first_run integration + tray dispatch), без новых контроллеров/флагов.

## Recommended Fix
1. Вернуть корректную политику рестарта:
   - `permissions_v2.restart.require_needs_restart: true`.
2. Добавить hard guard перед `trigger_restart()`:
   - если `USER_QUIT_INTENT=True`, abort restart sequence.
3. Обеспечить stop-пропагацию:
   - в `FirstRunPermissionsIntegration.stop()` вызвать `await self._v2_integration.stop()` при наличии.
4. Закрыть race quit dispatch:
   - в tray quit path добавить bounded wait (короткий `future.result(timeout=...)`) для подтверждения доставки `quit_clicked` перед фактическим quit.

## Verification
1. Fresh install -> first run -> Quit во время/после permission flow: нет relaunch.
2. Если есть реальный `needs_restart`, рестарт выполняется ровно один раз и не выполняется при `USER_QUIT_INTENT=True`.
3. Проверить отсутствие legacy LaunchAgents на целевой машине пользователя:
   - `~/Library/LaunchAgents/*.plist`
   - `/Library/LaunchAgents/*.plist`

