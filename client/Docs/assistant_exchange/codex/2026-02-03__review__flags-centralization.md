# Review: Feature Flags & Restart Handler Centralization

## Summary
Проверил изменения после рефакторинга флагов и удаления дубликата рестарт‑хэндлера. Файл `modules/permission_restart/macos/restart_handler.py` удалён. Реестр флагов расширен, но остались рассинхронизации.

## Findings
- **Остаточный дрейф реестра:** `NEXY_ENVIRONMENT` используется в `config/unified_config_loader.py`, но отсутствует в `Docs/FEATURE_FLAGS.md`.
- **Неиспользуемые флаги в реестре:** `NEXY_KS_PERMISSION_RESTART_V2`, `NEXY_DISABLE_TERMINAL_PERMISSIONS_BYPASS` по‑прежнему в реестре, но не используются в коде (на текущем срезе).

## Files Checked
- `Docs/FEATURE_FLAGS.md`
- `config/unified_config_loader.py`
- `modules/permission_restart/macos/` (удалён `restart_handler.py`)

## Suggested Next Steps
1. Добавить `NEXY_ENVIRONMENT` в реестр либо убрать из кода, если не нужен.
2. Решить судьбу `NEXY_KS_PERMISSION_RESTART_V2`/`NEXY_DISABLE_TERMINAL_PERMISSIONS_BYPASS`: подключить в коде или удалить из реестра.

## Verification
- Тесты не запускались.
