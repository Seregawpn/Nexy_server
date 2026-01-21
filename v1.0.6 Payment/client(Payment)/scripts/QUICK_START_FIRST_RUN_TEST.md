# Быстрый старт: Интеграционный тест first-run

## ⚡ Команды

```bash
# 1. Очистить флаг (обязательно перед тестом!)
rm -f ~/Library/Application\ Support/Nexy/permissions_first_run_completed.flag

# 2. Запустить тест
bash scripts/test_first_run_integration.sh
```

## 📋 Чек-лист

- [ ] Флаг `permissions_first_run_completed.flag` удалён
- [ ] Скрипт запущен: `bash scripts/test_first_run_integration.sh`
- [ ] Ожидаем 60-90 секунд для полного цикла
- [ ] Проверяем логи на события `permissions.first_run_started/completed`
- [ ] Проверяем создание флага после завершения

## 🔍 Shadow-mode логи

**Где искать:**
- Обычные логи приложения (`logs/nexy.log` или `/var/folders/.../nexy_debug.log`)
- Префикс: `[COORDINATOR] Shadow-mode ...` или `[UPDATER] Shadow-mode ...`

**Активация:**
- `config/unified_config.yaml` → `features.use_events_for_update_status.enabled: true`
- `config/unified_config.yaml` → `features.use_events_for_restart_pending.enabled: true`

## 📊 Что проверяется

1. ✅ Событие `permissions.first_run_started` публикуется
2. ✅ Событие `permissions.first_run_completed` публикуется
3. ✅ Состояние `first_run_*` обновляется через state_manager
4. ✅ Флаг `permissions_first_run_completed.flag` создаётся
5. ✅ Shadow-mode логи появляются при включённых флагах

## 🆘 Если что-то пошло не так

- Проверить, что флаг удалён: `ls -la ~/Library/Application\ Support/Nexy/permissions_first_run_completed.flag`
- Проверить логи: `tail -f logs/nexy.log` или найти `nexy_debug.log` в `/var/folders/`
- Проверить состояние: `python3 scripts/check_first_run_state.py`

## 📚 Документация

- Полная инструкция: `scripts/README_FIRST_RUN_TEST.md`
- Интеграционные pytest-тесты: `integration/tests/test_permission_restart_and_update_interplay.py`
- Shadow-mode логирование: см. `Docs/FEATURE_FLAGS.md` (флаг `use_events_for_update_status`)
