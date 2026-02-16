# Task Brief: browser install lock timeout and progress

## Goal
Убрать сценарий "browser_use завис и ничего не происходит" при ожидании install lock.

## Changes
- `modules/browser_automation/module.py`
  - Добавлен timeout ожидания install lock (`install_lock_timeout_sec`, default 180s).
  - Добавлен heartbeat при ожидании lock (`install_wait_heartbeat_sec`, default 10s) + user notification.
  - Добавлен terminal fail при timeout ожидания lock:
    - `BROWSER_TASK_FAILED`
    - description: `Browser setup timed out while waiting for install lock`
  - `BROWSER_TASK_STARTED` теперь публикуется раньше (сразу после проверки `browser_use`), чтобы убрать silent gap до установки.

## Architecture Gates
- Single Owner: сохранен (`BrowserUseModule`).
- Zero Duplication: новый путь не добавлен, расширен существующий owner flow.
- Anti-Race: сохранен `single-flight` lock, добавлен timeout-guard на ожидание lock.
- Flag Lifecycle: новые runtime flags не добавлялись, использованы только config-ключи модуля.

## Validation
- `python3 -m py_compile modules/browser_automation/module.py integration/integrations/action_execution_integration.py` -> OK
- Smoke (CLI env без browser_use): terminal fail path корректен (`BROWSER_TASK_FAILED`).

## Expected Runtime Result
- При долгом занятом install lock browser_use больше не висит бесконечно.
- Пользователь получает либо запуск задачи, либо явный fail по timeout.
