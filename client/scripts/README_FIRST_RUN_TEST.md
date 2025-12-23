# Инструкция по запуску интеграционного теста first-run

## Быстрый старт

```bash
# 1. Удалить флаг для симуляции первого запуска
rm -f ~/Library/Application\ Support/Nexy/permissions_first_run_completed.flag

# 2. Запустить тест
bash scripts/test_first_run_integration.sh
```

## Что делает скрипт

1. **Удаляет флаг первого запуска** — симулирует первый запуск приложения
2. **Очищает старые логи** — готовит чистое окружение для теста
3. **Запускает main.py на 90 секунд** — достаточно для полного цикла first-run
4. **Мониторинг в реальном времени** — проверяет события каждые 10 секунд:
   - `permissions.first_run_started`
   - `permissions.first_run_completed`
   - `permissions.first_run_restart_pending`
5. **Автоматическое завершение** — если оба события (`started` и `completed`) найдены
6. **Проверка флагов** — проверяет создание `permissions_first_run_completed.flag`
7. **Проверка состояния** — выводит состояние через `state_manager`

## Ожидаемый вывод

```
=== First Run Integration Test ===
1. Удаляем флаг первого запуска...
   ✅ Флаг удалён
2. Очищаем старые логи...
   ✅ Логи очищены
3. Запускаем main.py (будет работать 90 секунд для полного цикла first-run)...
   Мониторинг событий first_run (каждые 10 секунд)...
   [10s] started=1, completed=0
   [20s] started=1, completed=0
   [30s] started=1, completed=1
   ✅ Полный цикл first-run завершён!

4. Финальная проверка логов на события first_run...
   События permissions.first_run_started:
   [найдены события]
   
   События permissions.first_run_completed:
   [найдены события]
   
   Проверка флага завершения first-run:
   ✅ Флаг permissions_first_run_completed.flag создан
```

## Проверка shadow-mode логирования

Для проверки диагностического логирования `update_in_progress`:

1. Убедитесь, что флаг включён в `config/unified_config.yaml`:
   ```yaml
   features:
     use_events_for_update_status:
       enabled: true
   ```

2. Запустите приложение и инициируйте обновление

3. Проверьте логи на наличие сообщений:
   ```
   [COORDINATOR] Shadow-mode sync: snapshot.update_in_progress=True == state_data=True (session=...)
   [UPDATER] Shadow-mode sync: accessor=True == state_data=True (trigger=...)
   ```

## Примечания

- **Время выполнения**: полный цикл first-run занимает ~60-90 секунд (13 секунд на каждое разрешение + паузы)
- **Автоматическое завершение**: скрипт завершится раньше, если оба события найдены
- **Флаги**: скрипт автоматически удаляет флаг перед запуском, но можно удалить вручную для чистоты

## Связанные файлы

- `scripts/test_first_run_integration.sh` — основной скрипт теста
- `scripts/check_first_run_state.py` — проверка состояния через state_manager
- `integration/tests/test_permission_restart_and_update_interplay.py` — pytest для permission restart
- `Docs/FEATURE_FLAGS.md` (флаг `use_events_for_update_status`) — описание shadow-mode логирования
