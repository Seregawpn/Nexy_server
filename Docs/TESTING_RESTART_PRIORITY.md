# Инструкция по тестированию порядка приоритетов перезапуска

## ✅ Статус: Unit-тесты пройдены

Все 7 unit-тестов успешно прошли:
- ✅ `test_priority_1_packaged_app_first` - PRIORITY 1 вызывается первым
- ✅ `test_priority_2_execve_fallback` - PRIORITY 2 используется как fallback
- ✅ `test_priority_3_dev_fallback` - PRIORITY 3 для dev-режима
- ✅ `test_packaged_app_unavailable_marks_flag` - флаг устанавливается
- ✅ `test_all_methods_fail_aborts_restart` - прерывание при неудаче
- ✅ `test_log_messages_reflect_priority` - логи отражают приоритет
- ✅ `test_execve_fallback_logged_when_packaged_unavailable` - логирование fallback

## 🧪 Ручное тестирование

### Быстрый старт

Используйте скрипт для автоматизированного тестирования:

```bash
./scripts/test_restart_priority.sh
```

Скрипт предлагает 4 варианта:
1. **PRIORITY 1**: Packaged .app доступен (open -n -a)
2. **PRIORITY 2**: Packaged .app недоступен (os.execve fallback)
3. **PRIORITY 3**: Dev fallback (python main.py)
4. Все сценарии последовательно

### Сценарий 1: PRIORITY 1 (open -n -a)

**Цель**: Проверить что `open -n -a` используется как основной метод

**Шаги**:
1. Очистить флаги:
   ```bash
   rm ~/Library/Application\ Support/Nexy/*.flag
   rm ~/Library/Caches/Nexy/*.flag
   ```

2. Сбросить TCC разрешения:
   ```bash
   tccutil reset Microphone com.nexy.assistant
   tccutil reset Accessibility com.nexy.assistant
   tccutil reset ScreenCapture com.nexy.assistant
   tccutil reset InputMonitoring com.nexy.assistant
   ```

3. Запустить приложение:
   ```bash
   /Applications/Nexy.app/Contents/MacOS/Nexy > ~/nexy_test_priority1.log 2>&1 &
   tail -f ~/nexy_test_priority1.log
   ```

4. Выдать все разрешения (Microphone, Accessibility, Input, Screen)

5. Проверить логи:
   - ✅ Должен быть: `[PERMISSION_RESTART] Scheduled delayed packaged relaunch`
   - ✅ Должен быть: `[PERMISSION_RESTART] ✅ Atomic restart flag written`
   - ✅ Должен быть: `[PERMISSION_RESTART] Packaged app launch verified (full restart)`
   - ✅ Должен быть: `[PERMISSION_RESTART] Exiting current process`
   - ❌ НЕ должно быть: `[PERMISSION_RESTART] Restarting current bundle via execve`

6. Проверить результат:
   - ✅ Иконка появилась в menu bar
   - ✅ Лог: `✅ [FIRST_RUN_PERMISSIONS] Перезапуск после first_run завершён успешно`
   - ✅ Лог: `✅ [PERMISSIONS] Запрос разрешений завершен (session=restarted)`

### Сценарий 2: PRIORITY 2 (os.execve fallback)

**Цель**: Проверить что `os.execve()` используется как fallback

**Шаги**:
1. Временно переименовать `.app` bundle:
   ```bash
   mv /Applications/Nexy.app /Applications/Nexy.app.backup
   ```

2. Очистить флаги и TCC (как в Сценарии 1)

3. Запустить приложение из PyInstaller bundle (если доступен)

4. Выдать все разрешения

5. Проверить логи:
   - ✅ Должен быть: `[PERMISSION_RESTART] Packaged app unavailable - will use execve fallback`
   - ✅ Должен быть: `[PERMISSION_RESTART] Restarting current bundle via execve`
   - ✅ Должен быть: `[PERMISSION_RESTART] Setting NEXY_FIRST_RUN_RESTARTED=1`
   - ❌ НЕ должно быть: `[PERMISSION_RESTART] Scheduled delayed packaged relaunch`

6. Восстановить `.app` bundle:
   ```bash
   mv /Applications/Nexy.app.backup /Applications/Nexy.app
   ```

### Сценарий 3: PRIORITY 3 (dev fallback)

**Цель**: Проверить что dev fallback работает для разработки

**Шаги**:
1. Очистить флаги и TCC

2. Запустить приложение в dev-режиме:
   ```bash
   cd /Users/sergiyzasorin/Development/Nexy/client
   python3 main.py > ~/nexy_test_priority3.log 2>&1 &
   tail -f ~/nexy_test_priority3.log
   ```

3. Выдать все разрешения

4. Проверить логи:
   - ✅ Должен быть: `[PERMISSION_RESTART] Dev restart path active`
   - ✅ Должен быть: `[PERMISSION_RESTART] Launching dev process`
   - ✅ Должен быть: `[PERMISSION_RESTART] Setting NEXY_FIRST_RUN_RESTARTED=1`

## 📋 Чек-лист проверки

### Критерии успеха для PRIORITY 1:
- [ ] Лог содержит "full restart" или "Packaged app launch verified (full restart)"
- [ ] НЕТ логов о "execve fallback" или "Restarting current bundle via execve"
- [ ] Иконка появляется корректно в menu bar после перезапуска
- [ ] Новый процесс обнаружен через `pgrep`
- [ ] `permissions.first_run_completed` опубликовано в новом процессе

### Критерии успеха для PRIORITY 2:
- [ ] Лог содержит "will use execve fallback"
- [ ] Лог содержит "Restarting current bundle via execve"
- [ ] Процесс заменяется (PID сохраняется)
- [ ] `permissions.first_run_completed` опубликовано

### Критерии успеха для PRIORITY 3:
- [ ] Лог содержит "Dev restart path active"
- [ ] Лог содержит "Launching dev process"
- [ ] Новый Python процесс запущен
- [ ] `permissions.first_run_completed` опубликовано

## 🔍 Проверка логов

Для детальной проверки логов используйте:

```bash
# Поиск ключевых логов
grep -E "(PRIORITY|full restart|execve fallback|Dev restart)" ~/nexy_test_*.log

# Проверка последовательности
grep -E "\[PERMISSION_RESTART\]" ~/nexy_test_*.log | tail -20
```

## ⚠️ Известные проблемы

Если тесты не проходят:
1. Убедитесь что флаги очищены полностью
2. Проверьте что TCC разрешения сброшены
3. Убедитесь что приложение собрано корректно
4. Проверьте логи на наличие ошибок

## 📝 Отчет о тестировании

После выполнения тестов заполните:

- [ ] Сценарий 1 (PRIORITY 1) - результат: ✅/❌
- [ ] Сценарий 2 (PRIORITY 2) - результат: ✅/❌
- [ ] Сценарий 3 (PRIORITY 3) - результат: ✅/❌
- [ ] Иконка появляется корректно: ✅/❌
- [ ] Логи соответствуют спецификации: ✅/❌

