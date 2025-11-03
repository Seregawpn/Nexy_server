# SANDBOX PERMISSIONS FIX - Резюме изменений

**Дата:** 2025-11-02
**Проблема:** Бесконечные рестарты при первом запуске из-за PermissionError при создании флагов в sandbox

---

## Корневая причина (Root Cause Analysis)

### Симптомы из nexy_first_run.log

1. **PermissionError** при создании флагов:
   ```
   PermissionError: [Errno 13] Permission denied:
   '~/Library/Application Support/Nexy/permissions_first_run_completed.flag'
   ```

2. **Бесконечный цикл рестартов**:
   - Каждый рестарт → флаг не создаётся → считается "первым запуском" → запрос разрешений → рестарт
   - Цикл повторяется бесконечно

3. **Преждевременная активация голосовых модулей**:
   - VoiceRecognitionIntegration и WelcomeMessageIntegration запускаются до завершения рестарта
   - Причина: флаг `permissions_restart_pending` не сбрасывается (зависит от несуществующих файловых флагов)

### Технические причины

1. **`get_user_data_dir()` не учитывает sandbox**:
   - Пытается писать в `~/Library/Application Support/Nexy`
   - В sandbox должен использовать `~/Library/Containers/{bundle_id}/Data/...`

2. **`PermissionsRestartHandler` постоянно пытается открыть /Applications/Nexy.app**:
   - В dev режиме .app может отсутствовать или не иметь исполняемого файла
   - Каждая попытка занимает ~10 секунд (timeout), затем fallback на dev процесс

3. **Отсутствие env fallback для флагов**:
   - Когда файловые флаги не создаются, нет альтернативного механизма передачи состояния

---

## Реализованные исправления

### 1. `integration/utils/resource_path.py` - Sandbox Detection

**Изменения:**
- Добавлены 3-уровневые fallbacks для `get_user_data_dir()`, `get_user_cache_dir()`, `get_user_logs_dir()`:
  1. Стандартный путь `~/Library/Application Support/{app_name}`
  2. Sandbox container `~/Library/Containers/{bundle_id}/Data/Library/Application Support/{app_name}`
  3. Временный `/tmp/{app_name}` (последний fallback)

- Проверка возможности записи через test file touch/unlink

- Автоопределение `bundle_id` из `APP_BUNDLE_ID` env или дефолтный `com.nexy.assistant`

**Преимущества:**
- ✅ Работает в sandbox без PermissionError
- ✅ Graceful degradation (/tmp fallback)
- ✅ Явная ошибка если все пути недоступны

**Файлы:**
- `integration/utils/resource_path.py:57-188`

---

### 2. `integration/integrations/first_run_permissions_integration.py` - Robust Flag Creation

**Изменения:**
- Добавлен метод `_safe_touch_flag()` с обработкой PermissionError
- Добавлен fallback на `state_manager.set_state_data("permissions_restart_completed_fallback", True)`
- Добавлена проверка env переменной `NEXY_FIRST_RUN_RESTARTED` в `initialize()`
- При неудачном создании флага `permissions_first_run_completed`:
  - Публикуется `permissions.first_run_failed`
  - Вызывается `_handle_restart_failure()` для сброса состояния
  - Возвращается `False` чтобы координатор продолжил без рестарта

**Преимущества:**
- ✅ Не застревает в цикле при PermissionError
- ✅ Env fallback позволяет обнаружить рестарт даже без файловых флагов
- ✅ Детальное логирование для диагностики

**Файлы:**
- `integration/integrations/first_run_permissions_integration.py:77-121` (initialize)
- `integration/integrations/first_run_permissions_integration.py:168-178` (флаг first_run_completed)
- `integration/integrations/first_run_permissions_integration.py:188-193` (флаг restart_completed)
- `integration/integrations/first_run_permissions_integration.py:387-422` (_safe_touch_flag, _set_restart_flag)

---

### 3. `modules/permission_restart/macos/permissions_restart_handler.py` - Missing Bundle Detection

**Изменения:**
- Добавлен флаг `self._packaged_unavailable` для избежания повторных попыток открыть недоступный .app
- Специальная обработка `kLSNoExecutableErr` (10810) - bundle без исполняемого файла
- В `_launch_dev_process()` передача env переменной `NEXY_FIRST_RUN_RESTARTED=1` новому процессу
- Пропуск `_launch_packaged_app()` если уже знаем что bundle недоступен

**Преимущества:**
- ✅ Не тратит 10 секунд на каждую попытку в dev режиме
- ✅ Env переменная позволяет новому процессу обнаружить успешный рестарт
- ✅ Явный лог при обнаружении kLSNoExecutableErr для CI/packaging диагностики

**Файлы:**
- `modules/permission_restart/macos/permissions_restart_handler.py:44` (_packaged_unavailable)
- `modules/permission_restart/macos/permissions_restart_handler.py:76-84` (проверка unavailable)
- `modules/permission_restart/macos/permissions_restart_handler.py:135-142` (обработка kLSNoExecutableErr)
- `modules/permission_restart/macos/permissions_restart_handler.py:165-178` (env передача)

---

### 4. `integration/core/simple_module_coordinator.py` - Restart Timing & Logging

**Изменения:**
- Добавлено измерение времени `decision_duration_ms` и `restart_duration_ms`
- Улучшенное логирование решений в canonical format:
  - `decision=abort reason=... ctx={...} source=... duration_ms=...`
  - `decision=continue reason=... ctx={...} source=... duration_ms=...`
- Логирование времени выполнения рестарта

**Преимущества:**
- ✅ Мониторинг производительности gateway решений
- ✅ Диагностика задержек при рестарте
- ✅ Canonical format для парсинга логов

**Файлы:**
- `integration/core/simple_module_coordinator.py:538-600`

---

### 5. `Docs/NEXY_FIRST_RUN_LOG_EXPECTED.md` - Updated Expected Logs

**Изменения:**
- Добавлены варианты логов для sandbox (Вариант A/B)
- Документированы PermissionError логи
- Добавлен "Вариант C: Dev fallback" для рестарта
- Добавлен "Вариант B: env fallback" для обнаружения рестарта
- Новый красный флаг "Бесконечные рестарты (PermissionError)" с диагнозом и решением

**Файлы:**
- `Docs/NEXY_FIRST_RUN_LOG_EXPECTED.md` (полностью обновлён)

---

## Архитектурные решения

### Почему env fallback вместо только state_manager?

**Проблема:** `state_manager` сохраняет данные в памяти текущего процесса. После `os._exit(0)` и запуска нового процесса эти данные теряются.

**Решение:** Env переменные передаются через `subprocess.Popen(env=...)` и доступны новому процессу через `os.environ`.

### Почему 3 уровня fallback в resource_path?

**Уровень 1 (стандартный):** Работает для большинства non-sandbox запусков
**Уровень 2 (sandbox container):** macOS App Sandbox требует запись в контейнер
**Уровень 3 (/tmp):** Последняя надежда - флаги потеряются после reboot, но приложение не зависнет

### Почему _packaged_unavailable флаг?

Без этого флага каждый рестарт пытается:
1. `open -W /Applications/Nexy.app` (10s timeout)
2. Получает kLSNoExecutableErr
3. Падает в dev fallback

С флагом:
1. Первая попытка → kLSNoExecutableErr → устанавливает `_packaged_unavailable = True`
2. Следующие попытки → сразу идёт в dev fallback (экономит 10s)

---

## Тестирование

### Ручное тестирование (рекомендуется)

```bash
# 1. Очистить флаги
rm -rf ~/Library/Application\ Support/Nexy/*.flag
rm -rf ~/Library/Containers/com.nexy.assistant/Data/Library/Application\ Support/Nexy/*.flag

# 2. Сбросить TCC разрешения
tccutil reset Microphone com.nexy.assistant
tccutil reset Accessibility com.nexy.assistant
tccutil reset ScreenCapture com.nexy.assistant

# 3. Запустить из терминала с логированием
python3 main.py 2>&1 | tee ~/nexy_first_run.log

# 4. Пройти процесс выдачи разрешений
# 5. Проверить что рестарт произошёл ОДИН РАЗ
# 6. Проверить что новый процесс не запрашивает разрешения повторно
```

### Ожидаемые результаты

**Sandbox сценарий:**
```log
⚠️ Cannot write to ~/Library/Application Support/Nexy: [Errno 13], trying sandbox path...
✅ Using sandbox data directory: ~/Library/Containers/com.nexy.assistant/Data/Library/Application Support/Nexy
✅ [FIRST_RUN_PERMISSIONS] Флаг restart_completed установлен: <sandbox_path>/restart_completed.flag
```

**Dev fallback сценарий:**
```log
[PERMISSION_RESTART] open command failed (exit_code=10810, stderr=kLSNoExecutableErr)
[PERMISSION_RESTART] Packaged app unavailable - will use dev fallback
[PERMISSION_RESTART] Setting NEXY_FIRST_RUN_RESTARTED=1 for new process
# НОВЫЙ ПРОЦЕСС:
✅ [FIRST_RUN_PERMISSIONS] Перезапуск завершён успешно (обнаружено через NEXY_FIRST_RUN_RESTARTED env)
```

### Проверки (Checklist)

- [ ] Флаги создаются в sandbox container (если sandbox)
- [ ] Рестарт происходит **ОДИН РАЗ**, не повторяется
- [ ] Новый процесс обнаруживает завершённый рестарт (через flag или env)
- [ ] VoiceRecognitionIntegration НЕ активируется до рестарта
- [ ] WelcomeMessage играет ТОЛЬКО после рестарта
- [ ] Логи содержат `decision=abort` и `decision=continue` с duration_ms
- [ ] Нет повторяющихся логов `Первый запуск обнаружен`

---

## Риски и митигация

### Риск 1: /tmp fallback → потеря флагов после reboot

**Вероятность:** Низкая (только если sandbox И контейнер недоступны)
**Митигация:**
- Логирование warning: "flags will be lost on reboot"
- Телеметрия: счётчик использования /tmp fallback
- CI проверка: убедиться что packaging правильно настроил sandbox entitlements

### Риск 2: Env переменная не передаётся (edge case)

**Вероятность:** Очень низкая
**Митигация:**
- Двойная проверка: env ИЛИ flag
- Если оба не сработали → fallback на `state_manager.get_state_data("permissions_restart_completed_fallback")`

### Риск 3: Координатор продолжает запуск при неудачном рестарте

**Вероятность:** Средняя (сознательное решение для graceful degradation)
**Поведение:**
- Логирование warning
- Флаги `_permissions_in_progress` и `_restart_pending` сбрасываются
- Приложение работает без рестарта (может быть некорректное состояние)

**Митигация:**
- Мониторинг: событие `permissions.first_run_failed`
- Kill-switch: `NEXY_KS_FIRST_RUN_RESTART=1` для полного отключения рестарта

---

## Метрики для мониторинга

### События для телеметрии

1. `resource_path.sandbox_fallback_used` - использован sandbox container путь
2. `resource_path.tmp_fallback_used` - использован /tmp (критично!)
3. `permissions.first_run_failed` - не удалось создать флаг
4. `permissions.restart_env_fallback_used` - использован NEXY_FIRST_RUN_RESTARTED env
5. `permissions.restart_kLSNoExecutableErr` - bundle без исполняемого

### Счётчики

- `first_run_restart_cycles` - количество циклов рестарта (должно быть 1)
- `restart_duration_ms` - время выполнения рестарта
- `decision_duration_ms` - время принятия gateway решения

---

## Следующие шаги

### Обязательно

1. ✅ Ручное тестирование с чистыми TCC разрешениями
2. ✅ Проверка sandbox сценария (запуск из .app)
3. ✅ Проверка dev сценария (запуск из терминала python3 main.py)
4. ⏳ Обновить `change_impact.yaml` с новой осью `permissions.restart_storage`
5. ⏳ Обновить `STATE_CATALOG.md` с описанием новой оси
6. ⏳ Rebuild .app через `packaging/build_final.sh`

### Опционально (будущие улучшения)

- [ ] Unit тесты для `_safe_touch_flag()` с мокированием PermissionError
- [ ] Интеграционный тест эмулирующий sandbox PermissionError
- [ ] CI проверка что `Contents/MacOS/Nexy` существует после build
- [ ] Добавить реальные селекторы разрешений вместо hardcoded GRANTED
- [ ] Таймаут для `permissions_restart_pending` (если >N секунд → публиковать аварийный ивент)

---

## Связанные документы

- [NEXY_FIRST_RUN_LOG_EXPECTED.md](NEXY_FIRST_RUN_LOG_EXPECTED.md) - ожидаемые логи при корректной работе
- [ADR-001-first-run-restart-hotfix.md](_archive/ADR-001-first-run-restart-hotfix.md) - оригинальный ADR
- [change_impact.yaml](../config/interaction_matrix.yaml) - матрица взаимодействий состояний
- [STATE_CATALOG.md](STATE_CATALOG.md) - каталог всех осей состояния

---

**Дата последнего обновления:** 2025-11-02
**Статус:** Готово к тестированию
