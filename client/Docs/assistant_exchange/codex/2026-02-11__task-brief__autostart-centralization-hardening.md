# Autostart Centralization Hardening

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-11

## Diagnosis
В `autostart_manager` оставались конфликтные формулировки (PKG-owner) и latent race при параллельных status-check/repair.

## Root Cause
Исторический сдвиг политики packaging (postinstall cleanup-only) не был полностью синхронизирован с интеграцией; проверки автозапуска не были single-flight.

## Changes
- Добавлен `asyncio.Lock` (`_status_check_lock`) в `AutostartManagerIntegration` для single-flight проверки/repair.
- Обновлены комментарии и docstring интеграции под runtime-config модель.
- Обновлен `status_data.managed_by` на `autostart_manager_integration`.
- Синхронизирован архитектурный документ по подпискам/публикациям `autostart_manager_integration`.

## Files
- `integration/integrations/autostart_manager_integration.py`
- `Docs/ARCHITECTURE_OVERVIEW.md`

## Verification
- `python3 -m py_compile integration/integrations/autostart_manager_integration.py` — ok.
- Поиск по коду: не осталось старых ссылок на `managed_by="PKG installer"` и `autostart.status_check`.
