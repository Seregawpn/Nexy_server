# Task Brief: First-run ledger-only owner path (remove cache flag writes)

## Context
Запрос: сократить количество first-run флагов и оставить более чистую owner-логику.

## Diagnosis
`FirstRunPermissionsIntegration` всё ещё создавал `permissions_first_run_completed.flag`, хотя решение first-run уже централизовано в V2 ledger.

## Root Cause
Исторический cache-флаг остался в runtime write-path и расширял поверхность состояния без owner-необходимости.

## Implementation
1. Удалён write-path `permissions_first_run_completed.flag` из `FirstRunPermissionsIntegration`.
2. Удалены вызовы `_mark_first_run_completed()` в обычном и timeout completion пути.
3. Обновлён тест `test_first_run_status_policy.py` (убран assert по удалённому helper).
4. Обновлён комментарий в coordinator (ledger owner-path вместо legacy flag).
5. Обновлены спецификации/требования:
   - `Docs/first_run_flow_spec.md`
   - `Docs/PROJECT_REQUIREMENTS.md`
   - `Docs/STATE_CATALOG.md`
6. Обновлён `scripts/clear_first_run_flags.py`:
   - V2 SoT: `permission_ledger.json`
   - restart signal: `restart_completed.flag`
   - legacy флаги очищаются как cleanup-only.

## Architecture Gates
- Single Owner Gate: соблюден (`permission_ledger.json` как SoT для first-run decision).
- Zero Duplication Gate: выполнен (удален лишний cache write-path).
- Anti-Race Gate: не ухудшен (owner-path рестарта/ledger не менялся).
- Flag Lifecycle Gate: улучшен (убран runtime producer для лишнего first-run cache flag).

## Verification
- `python3 -m py_compile` для измененных файлов — OK.
- `PYTHONPATH=. pytest -q tests/test_first_run_status_policy.py` — `3 passed`.
- `rg` подтверждает отсутствие runtime-использования `permissions_first_run_completed.flag` в интеграциях (остались только cleanup/legacy scripts).

## Информация об изменениях
- Что изменено:
  - Удалена генерация `permissions_first_run_completed.flag` из runtime owner-path first-run.
  - Обновлены связанные тест/скрипт и канонические документы.
- Список файлов:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/integration/integrations/first_run_permissions_integration.py`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/tests/test_first_run_status_policy.py`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/scripts/clear_first_run_flags.py`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/integration/core/simple_module_coordinator.py`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/Docs/first_run_flow_spec.md`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/Docs/PROJECT_REQUIREMENTS.md`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/Docs/STATE_CATALOG.md`
- Причина/цель изменений:
  - Сократить количество first-run флагов и убрать лишний runtime-state.
- Проверка:
  - py_compile + pytest + grep-проверка owner-контракта.
