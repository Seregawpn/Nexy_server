# Task Brief: disable limited_mode and enforce always-full-access policy

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-16
- ID (INS-###): N/A

## Diagnosis
First-run lifecycle застревал в `limited_mode/first_run_in_progress`, из-за чего часть модулей могла блокироваться на старте и поведение отличалось от policy "всегда полный доступ".

## Root Cause
V2 permission owner сохранял/переиспользовал фазу `limited_mode` и публиковал legacy `permissions.first_run_failed`, а координатор не сбрасывал first-run state на этом событии.

## Optimal Fix
- Source of Truth: `modules/permissions/v2/orchestrator.py` + `modules/permissions/v2/integration.py`.
- Изменения:
  - `limited_mode` отключён как terminal-путь: оркестратор всегда завершает в `completed/full_mode`.
  - Старый ledger с `phase=limited_mode` автоматически нормализуется в `phase=completed`.
  - Legacy mapping для terminal-состояния публикует `permissions.first_run_completed` (не `failed`), с `all_granted=true`.
  - Startup-gate `are_all_granted` в coordinator удалён: модули стартуют, capability-check остаётся в owner-модулях по месту использования.

## Verification
- `python3 -m py_compile modules/permissions/v2/orchestrator.py` -> OK
- `python3 -m py_compile modules/permissions/v2/integration.py` -> OK
- `python3 -m py_compile integration/core/simple_module_coordinator.py` -> OK

## Информация об изменениях
- Что изменено:
  - Отключён limited_mode в V2 orchestrator (нормализация в completed).
  - Переключён legacy terminal event на `permissions.first_run_completed`.
  - Убран startup-блок по `are_all_granted` в coordinator.
- Файлы:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/modules/permissions/v2/orchestrator.py`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/modules/permissions/v2/integration.py`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/integration/core/simple_module_coordinator.py`
- Причина/цель:
  - Привести first-run lifecycle к policy: без limited_mode, без блокировки общего старта.
- Проверка:
  - Синтаксическая валидация Python модулей.

