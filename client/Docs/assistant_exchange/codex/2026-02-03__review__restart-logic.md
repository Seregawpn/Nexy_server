# Review: Restart Logic Fixes (V2 Permissions)

## Summary
Проверил фактические изменения в V2 оркестраторе и интеграции. В `modules/permissions/v2/orchestrator.py` исправление вызова не применено (все еще `_enter_restart_pending`). В `modules/permissions/v2/integration.py` добавлен анблок по `RESTART_SCHEDULED` — это корректно снимает блокировку старта, но нужно добавить idempotency-guard, чтобы не было двойного completion после финального `COMPLETED`.

## Findings
- **Блокер:** `_decide_after_first_run()` по‑прежнему вызывает несуществующий `_enter_restart_pending` → риск `AttributeError` и срыва рестарт‑пути.
- **Риск дубля:** `RESTART_SCHEDULED` уже сигналит completion в `_emit_event`; после пост‑рестарт `COMPLETED` тоже триггерит completion. Нужен guard, иначе возможны двойные completion‑события/сигналы.

## Files
- `modules/permissions/v2/orchestrator.py`
- `modules/permissions/v2/integration.py`

## Recommended Fix
1. В `modules/permissions/v2/orchestrator.py` заменить `_enter_restart_pending()` на `_enter_restart_sequence()`.
2. В `modules/permissions/v2/integration.py` добавить `self._legacy_completed_emitted` (или аналог), чтобы `RESTART_SCHEDULED` не дублировал completion после `COMPLETED`.

## Verification
- Запуск first‑run V2, убедиться что нет `AttributeError`, рестарт один, и completion‑сигнал ровно один.

