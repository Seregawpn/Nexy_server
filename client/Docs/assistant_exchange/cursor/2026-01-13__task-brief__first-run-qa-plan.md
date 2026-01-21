# План QA/тестирования: First-Run Permissions

## Метаданные
- Ассистент: cursor
- Тип: task-brief
- Дата: 2026-01-13
- Статус: ready for QA

## Цель QA

Подтвердить соответствие реализации канону:
- Dialog-only путь (только системные prompts)
- Единый fallback (in-app dialog после таймаута)
- Единый путь рестарта (`permissions.first_run_restart_pending`)
- Порядок разрешений из конфига (Accessibility → Microphone → Screen Capture → Input Monitoring)

## Подготовка к тестированию

### 1. Очистка окружения

```bash
# Удалить флаги first-run
rm -f ~/Library/Application\ Support/Nexy/permissions_first_run_completed.flag
rm -f ~/Library/Application\ Support/Nexy/restart_completed.flag

# Очистить логи
rm -f logs/nexy.log
rm -f /var/folders/*/T/nexy_debug.log

# Проверить, что флаги удалены
ls -la ~/Library/Application\ Support/Nexy/*.flag
```

### 2. Проверка конфигурации

```bash
# Проверить порядок разрешений в конфиге
grep -A 5 "required_permissions:" config/unified_config.yaml

# Ожидаемый результат:
# required_permissions:
#   - accessibility
#   - microphone
#   - screen_capture
#   - input_monitoring

# Проверить таймаут
grep "request_timeout_sec" config/unified_config.yaml

# Ожидаемый результат:
# request_timeout_sec: 13
```

## Автоматические тесты

### Тест 1: Интеграционный тест first-run

**Команда:**
```bash
bash scripts/test_first_run_integration.sh
```

**Что проверяет:**
- ✅ Событие `permissions.first_run_started` публикуется
- ✅ Событие `permissions.first_run_completed` публикуется
- ✅ Событие `permissions.first_run_restart_pending` публикуется (если нужен рестарт)
- ✅ Флаг `permissions_first_run_completed.flag` создаётся
- ✅ Состояние `first_run_*` обновляется через state_manager

**Ожидаемый результат:**
- Все события найдены в логах
- Флаг создан
- Состояние корректно

**Время выполнения:** ~60-90 секунд

### Тест 2: Golden logs тест

**Команда:**
```bash
python3 -m pytest tests/test_golden_first_run_logs.py -v
```

**Что проверяет:**
- ✅ Последовательность событий соответствует канону
- ✅ Нет запрещённых паттернов в старом процессе
- ✅ Порядок событий логичен (restart_pending → restart_completed → welcome_message)

**Ожидаемый результат:**
- Все тесты проходят
- Последовательность соответствует `EXPECTED_SEQUENCE`

### Тест 3: TAL после рестарта

**Команда:**
```bash
# После выполнения first-run и рестарта
python3 scripts/check_tal_after_restart.py log.md
```

**Что проверяет:**
- ✅ TAL=hold установлен после перезапуска
- ✅ TAL=refresh работает (периодическое обновление)
- ✅ TAL=released после tray.ready
- ✅ Нет assertion timeout до tray.ready
- ✅ Нет exit handler до tray.ready

**Ожидаемый результат:**
- TAL hold установлен
- Tray icon готов
- Нет assertion timeout до tray.ready

## Ручные проверки

### Сценарий 1: Все разрешения GRANTED (no-prompt)

**Шаги:**
1. Предоставить все разрешения в System Settings вручную
2. Удалить флаг: `rm -f ~/Library/Application\ Support/Nexy/permissions_first_run_completed.flag`
3. Запустить приложение: `python3 main.py`
4. Наблюдать логи

**Ожидаемое поведение:**
- ✅ Нет системных диалогов (все разрешения уже есть)
- ✅ Событие `permissions.first_run_started` публикуется
- ✅ Событие `permissions.first_run_completed` публикуется (быстро, без таймаутов)
- ✅ Флаг `permissions_first_run_completed.flag` создаётся
- ✅ Нет рестарта (все разрешения уже были)

**Проверка логов:**
```bash
grep -i "permissions.first_run" logs/nexy.log
grep -i "already granted" logs/nexy.log
```

### Сценарий 2: Отказ по одному разрешению → таймаут → fallback

**Шаги:**
1. Отказать в одном разрешении (например, Accessibility)
2. Удалить флаг: `rm -f ~/Library/Application\ Support/Nexy/permissions_first_run_completed.flag`
3. Запустить приложение: `python3 main.py`
4. Наблюдать последовательность диалогов

**Ожидаемое поведение:**
- ✅ Порядок диалогов: Accessibility → Microphone → Screen Capture → Input Monitoring
- ✅ Для отказанного разрешения: системный диалог не показывается (после DENIED)
- ✅ После таймаута всех разрешений: in-app dialog с "Open Settings" для всех недостающих
- ✅ Событие `permissions.first_run_completed` публикуется с `all_granted=False`
- ✅ Приложение продолжает работу с ограничениями

**Проверка логов:**
```bash
grep -i "permissions.first_run" logs/nexy.log
grep -i "fallback\|missing\|Open Settings" logs/nexy.log
grep -i "timeout" logs/nexy.log
```

### Сценарий 3: Быстрый grant → ранний переход

**Шаги:**
1. Удалить флаг: `rm -f ~/Library/Application\ Support/Nexy/permissions_first_run_completed.flag`
2. Запустить приложение: `python3 main.py`
3. Быстро предоставить разрешение (например, Microphone) в системном диалоге
4. Наблюдать переход к следующему разрешению

**Ожидаемое поведение:**
- ✅ Системный диалог появляется для первого разрешения
- ✅ После предоставления разрешения → сразу переход к следующему (без ожидания 13s)
- ✅ Событие `permissions.changed` публикуется при изменении статуса
- ✅ Событие `permissions.status_checked` публикуется на каждом шаге

**Проверка логов:**
```bash
grep -i "permissions.changed\|permissions.status_checked" logs/nexy.log
grep -i "granted.*after.*ms" logs/nexy.log
```

### Сценарий 4: Рестарт после получения критичных разрешений

**Шаги:**
1. Удалить флаг: `rm -f ~/Library/Application\ Support/Nexy/permissions_first_run_completed.flag`
2. Убедиться, что Accessibility, Input Monitoring или Screen Capture не предоставлены
3. Запустить приложение: `python3 main.py`
4. Предоставить одно из критичных разрешений (например, Accessibility)
5. Наблюдать рестарт

**Ожидаемое поведение:**
- ✅ Событие `permissions.first_run_restart_pending` публикуется
- ✅ Рестарт инициируется через PermissionRestartIntegration (не напрямую)
- ✅ В новом процессе: событие `permissions.first_run_completed` публикуется
- ✅ Флаг `restart_completed.flag` создаётся в новом процессе
- ✅ Приветствие играет только после рестарта

**Проверка логов:**
```bash
grep -i "permissions.first_run_restart_pending" logs/nexy.log
grep -i "restart.*initiated\|restart.*scheduled" logs/nexy.log
grep -i "Перезапуск после first_run завершён успешно" logs/nexy.log
grep -i "Воспроизведение приветственного сообщения" logs/nexy.log
```

## Чек-лист проверки канона

### Dialog-only путь
- [ ] Нет прямых вызовов Settings из activator (проверено в коде)
- [ ] Все разрешения запрашиваются через системные prompts
- [ ] Fallback (in-app dialog) появляется только после таймаута всех разрешений

### Порядок разрешений
- [ ] Порядок: Accessibility → Microphone → Screen Capture → Input Monitoring
- [ ] Порядок берётся из конфига `integrations.permissions.required_permissions`
- [ ] Каждое разрешение запрашивается последовательно (не параллельно)

### События EventBus
- [ ] `permissions.first_run_started` публикуется в начале flow
- [ ] `permissions.status_checked` публикуется на каждом шаге
- [ ] `permissions.changed` публикуется при изменении статуса
- [ ] `permissions.first_run_restart_pending` публикуется если нужен рестарт
- [ ] `permissions.first_run_completed` публикуется по завершении
- [ ] Все события содержат `session_id`

### Рестарт
- [ ] Рестарт инициируется только через `permissions.first_run_restart_pending`
- [ ] `permissions.first_run_completed` не планирует рестарт (no-op)
- [ ] Рестарт происходит через PermissionRestartIntegration

### Fallback
- [ ] Fallback вызывается только через `_show_missing_permissions_dialog`
- [ ] Fallback вызывается только после таймаута всех разрешений
- [ ] Fallback не вызывается для каждого разрешения отдельно
- [ ] Settings открывается только из in-app dialog

## Проверка логов

### Ожидаемые паттерны в логах

**Начало flow:**
```
[PERMISSIONS] session=... INITIAL statuses: mic=..., accessibility=..., screen=..., input=...
[PERMISSIONS] session=... Requesting missing permissions...
permissions.first_run_started
```

**Для каждого разрешения:**
```
[PERMISSIONS] session=... Requesting accessibility...
[PERMISSIONS] session=... accessibility=granted (confirmed) after ...ms
permissions.status_checked
permissions.changed
```

**Завершение flow:**
```
[PERMISSIONS] session=... Results: all_granted=..., needs_restart=...
permissions.first_run_restart_pending  # если нужен рестарт
permissions.first_run_completed
```

### Запрещённые паттерны

**В старом процессе (до рестарта):**
- ❌ `permissions.first_run_completed` (должно быть только в новом процессе)
- ❌ `Воспроизведение приветственного сообщения` (должно быть только после рестарта)
- ❌ `SessionCore_macOS_Legacy.*setPlayState Started.*Input` (нет записи микрофона до рестарта)

## Инструменты для проверки

### 1. Проверка состояния

**ВАЖНО:** `ApplicationStateManager` хранит состояние в памяти. Новый экземпляр не отражает runtime-состояние интеграций.

**Offline режим (по умолчанию):**
```bash
python3 scripts/check_first_run_state.py
```
Проверяет только флаг и логи (единственный источник истины без приложения).

**Runtime режим (требует работающее приложение):**
```bash
python3 scripts/check_first_run_state.py --runtime
```
⚠️ **ВАЖНО:** State валиден только при активном приложении с инициализированными интеграциями.
Скрипт создаёт новый экземпляр ApplicationStateManager, который не отражает runtime-состояние без работающего приложения.
Для проверки фактического состояния используйте offline режим (флаг + логи).

### 2. Проверка событий в логах
```bash
grep -i "permissions.first_run" logs/nexy.log
grep -i "permissions.status_checked\|permissions.changed" logs/nexy.log
```

### 3. Проверка флагов
```bash
ls -la ~/Library/Application\ Support/Nexy/*.flag
```

### 4. Проверка TAL после рестарта
```bash
python3 scripts/check_tal_after_restart.py log.md
```

## Критерии успеха

### Автоматические тесты
- ✅ `test_first_run_integration.sh` проходит успешно
- ✅ `test_golden_first_run_logs.py` проходит успешно
- ✅ `check_tal_after_restart.py` подтверждает TAL hold

### Ручные проверки
- ✅ Все сценарии работают как ожидается
- ✅ Логи соответствуют канону
- ✅ Нет запрещённых паттернов

### Соответствие канону
- ✅ Dialog-only путь соблюдён
- ✅ Порядок разрешений из конфига
- ✅ Единый путь fallback и рестарта
- ✅ Все события EventBus соответствуют канону

## Следующие шаги

1. **Запустить автоматические тесты:**
   ```bash
   bash scripts/test_first_run_integration.sh
   python3 -m pytest tests/test_golden_first_run_logs.py -v
   ```

2. **Выполнить ручные проверки:**
   - Сценарий 1: Все разрешения GRANTED
   - Сценарий 2: Отказ по одному разрешению
   - Сценарий 3: Быстрый grant
   - Сценарий 4: Рестарт после критичных разрешений

3. **Проверить логи:**
   - Соответствие ожидаемым паттернам
   - Отсутствие запрещённых паттернов
   - Правильная последовательность событий

4. **Зафиксировать результаты:**
   - Создать отчёт о результатах QA
   - Задокументировать найденные проблемы (если есть)
   - Подтвердить соответствие канону
