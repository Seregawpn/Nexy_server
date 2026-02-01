# Permission Retry — Open Settings / Trigger Repeat

## Date
2026-01-27

## Change Summary
Разрешил повторное открытие Settings и повторный trigger для шагов, которые не достигли PASS/SKIPPED. Это предотвращает «залипание» после первого запуска.

## Files
- `modules/permissions/v2/orchestrator.py`

## Details
- `OPEN_SETTINGS`: теперь открывается повторно, если разрешение не PASS/SKIPPED.
- `trigger()`: повторно вызывается, если разрешение не PASS/SKIPPED.

## Rationale
Для settings-only разрешений (Accessibility/FDA) нужно повторное открытие до выдачи доступа.

## Verification Plan
- Очистить `permission_ledger.json` и `permissions_first_run_completed.flag`.
- Запустить .app, закрыть Settings без выдачи.
- Перезапустить .app — Settings должен открыться снова.
