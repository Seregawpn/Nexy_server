# Task Brief: PR1 timebox single-restart + quit-guard

## Scope
- Реализован первый безопасный батч по плану (PR-1, in-scope only):
  - timeout-driven first-run (15s),
  - единичный restart после pipeline,
  - отмена restart при user quit,
  - 3-режимный tray (без LOCKED).

## Code changes
1. `modules/permissions/v2/orchestrator.py`
   - Добавлен `should_abort_restart` callback.
   - В `advance_on_timeout` режим:
     - по окончании pipeline запускается единичный restart sequence (вместо мгновенного complete).
   - Добавлены quit-guards перед и во время restart sequence.
   - В timeout-режиме `_mark_timeout` переводит шаг в `PASS_` (`TIMEBOX_RECEIVED`), не в `SKIPPED`.
   - В timeout-режиме `POST_RESTART_VERIFY` завершает flow без повторных failure-веток.

2. `modules/permissions/v2/integration.py`
   - Проброшен `should_abort_restart` в orchestrator.

3. `integration/integrations/first_run_permissions_integration.py`
   - Подключен `StateKeys.USER_QUIT_INTENT` callback (`_is_user_quit_intent`).
   - `stop()` теперь корректно останавливает V2 integration task.

4. `config/unified_config.yaml`
   - `integrations.permissions_v2.advance_on_timeout: true`
   - `integrations.permissions_v2.default_step_timeout_s: 15.0`
   - `grace_s` для шагов permissions_v2 приведен к `15.0`.

5. Tests
   - Добавлен `tests/test_first_run_orchestrator_single_restart.py`:
     - `test_advance_on_timeout_triggers_single_restart_once`
     - `test_quit_intent_cancels_restart_in_timeout_mode`
     - `test_post_restart_verify_does_not_restart_again_in_timeout_mode`

## Validation
- `python3 -m py_compile` (измененные файлы) — OK.
- `PYTHONPATH=. pytest -q tests/test_first_run_orchestrator_single_restart.py` — `3 passed`.
- `PYTHONPATH=. pytest -q tests/test_user_quit_ack.py` — `2 passed`.
- `PYTHONPATH=. pytest -q tests/verify_menu_quit_fix.py` — `2 passed`.

## Notes
- Изменения ограничены In-Scope из governance-плана.
- Legacy cleanup (freeze/remove) остается для следующего батча (PR-2/PR-3).

