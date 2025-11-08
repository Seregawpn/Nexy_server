# Анализ проблемы залипания микрофона при нажатии Shift для написания с большой буквы

## Проблема

При зажатии Shift для написания с большой буквы микрофон активируется и продолжает оставаться активным даже после отпускания Shift. Это происходит не всегда, но иногда.

## Анализ кода

### 1. Пороги нажатия клавиши

**Конфигурация** (`config/unified_config.yaml`):
- `short_press_threshold: 0.1` (100ms)
- `long_press_threshold: 0.6` (600ms)
- `hold_check_interval: 0.05` (50ms)

**Проблема**: Если пользователь зажимает Shift для написания с большой буквы, это может занять > 600ms, что активирует LONG_PRESS и микрофон.

### 2. Механизм генерации LONG_PRESS

В `QuartzKeyboardMonitor` LONG_PRESS может быть сгенерирован **ДВАЖДЫ**:

**Вариант A: Из hold_monitor (строка 418)**
```python
# modules/input_processing/keyboard/mac/quartz_monitor.py:395-418
def _run_hold_monitor(self):
    while not self.stop_event.is_set():
        with self.state_lock:
            if self.key_pressed and self.press_start_time:
                duration = time.time() - self.press_start_time
                if not self._long_sent and duration >= self.long_press_threshold:
                    # Генерирует LONG_PRESS
                    self._trigger_event(KeyEventType.LONG_PRESS, duration, ev)
                    self._long_sent = True
```

**Вариант B: При keyUp (строка 197-198)**
```python
# modules/input_processing/keyboard/mac/quartz_monitor.py:196-211
if duration >= self.long_press_threshold:
    event_type_out = KeyEventType.LONG_PRESS
else:
    event_type_out = KeyEventType.SHORT_PRESS

# Отправляем событие (SHORT_PRESS или LONG_PRESS)
self._trigger_event(event_type_out, duration, ev)

# RELEASE всегда отправляется после SHORT_PRESS или LONG_PRESS
self._trigger_event(KeyEventType.RELEASE, duration, ev_release)
```

### 3. Проблема: Двойная генерация LONG_PRESS

**Сценарий залипания**:

1. **Пользователь зажимает Shift** для написания с большой буквы
2. **Hold_monitor обнаруживает удержание >= 0.6 сек** → генерирует LONG_PRESS (строка 418)
3. **Микрофон активируется** через `_handle_long_press()` → `voice.recording_start`
4. **Пользователь отпускает Shift** (через 0.7-1.0 сек)
5. **При keyUp генерируется еще один LONG_PRESS** (если duration >= 0.6, строка 198)
6. **RELEASE генерируется** (строка 220)
7. **RELEASE обрабатывается** → `voice.recording_stop` публикуется
8. **НО**: Если первый LONG_PRESS уже активировал микрофон, второй LONG_PRESS может **перезаписать состояние** или **создать race condition**

### 4. Проблема: Race condition между LONG_PRESS и RELEASE

**Критическая проблема**: В `QuartzKeyboardMonitor` при keyUp генерируется **СНАЧАЛА** LONG_PRESS (если duration >= 0.6), **ЗАТЕМ** RELEASE (строка 220).

**Последовательность событий**:
1. Hold_monitor: LONG_PRESS (t=0.6s) → микрофон активируется
2. KeyUp: LONG_PRESS (t=0.7s) → **может перезаписать состояние**
3. KeyUp: RELEASE (t=0.7s) → останавливает запись

**Проблема**: Если второй LONG_PRESS приходит **ПОСЛЕ** того, как микрофон уже активирован, он может:
- Перезаписать `_current_session_id`
- Создать новую сессию записи
- RELEASE может остановить **неправильную сессию**

### 5. Проблема: Отсутствие проверки состояния при LONG_PRESS

**Код проблемы**:
```python
# integration/integrations/input_processing_integration.py:776-842
async def _handle_long_press(self, event: KeyEvent):
    # ...
    if not self._recording_started:
        # Запоминаем время начала записи
        self._recording_started = True
        await self.event_bus.publish("voice.recording_start", {...})
```

**Проблема**: Если LONG_PRESS приходит **второй раз** (при keyUp), проверка `if not self._recording_started` может быть **False**, но микрофон может быть **уже активен** из первого LONG_PRESS.

### 6. Проблема: RELEASE может не остановить микрофон

**Код RELEASE**:
```python
# integration/integrations/input_processing_integration.py:874-903
async def _handle_key_release(self, event: KeyEvent):
    # ...
    if self._recording_started and self._current_session_id is not None:
        await self.event_bus.publish("voice.recording_stop", {...})
        await self._wait_for_mic_closed()
```

**Проблема**: Если второй LONG_PRESS **перезаписал** `_current_session_id`, RELEASE может остановить **неправильную сессию**, и микрофон останется активным.

## Выявленные проблемы

### Проблема 1: Двойная генерация LONG_PRESS

**Корень проблемы**: LONG_PRESS генерируется **ДВАЖДЫ**:
1. Из `hold_monitor` (когда удержание >= 0.6 сек)
2. При `keyUp` (если duration >= 0.6 сек)

**Последствие**: Второй LONG_PRESS может перезаписать состояние и создать race condition.

### Проблема 2: Отсутствие защиты от повторных LONG_PRESS

**Корень проблемы**: В `_handle_long_press()` нет проверки, что микрофон **уже активен** из предыдущего LONG_PRESS.

**Код проблемы**:
```python
# integration/integrations/input_processing_integration.py:831-842
if not self._recording_started:
    # Активируем микрофон
    self._recording_started = True
    await self.event_bus.publish("voice.recording_start", {...})
```

**Проблема**: Если LONG_PRESS приходит второй раз, `_recording_started` может быть **True**, но микрофон может быть **уже активен** из первого LONG_PRESS.

### Проблема 3: Race condition между LONG_PRESS и RELEASE

**Корень проблемы**: При keyUp генерируется **СНАЧАЛА** LONG_PRESS, **ЗАТЕМ** RELEASE. Если LONG_PRESS приходит **ПОСЛЕ** активации микрофона, он может перезаписать `_current_session_id`, и RELEASE остановит **неправильную сессию**.

### Проблема 4: Отсутствие проверки состояния микрофона

**Корень проблемы**: В `_handle_long_press()` нет проверки реального состояния микрофона (`_mic_active`). Если микрофон **уже активен**, новый LONG_PRESS не должен активировать его повторно.

## Рекомендации для исправления

### Приоритет 1: Критично

1. **Предотвратить двойную генерацию LONG_PRESS**:
   - В `QuartzKeyboardMonitor` при keyUp **НЕ генерировать** LONG_PRESS, если `_long_sent == True`
   - Генерировать только SHORT_PRESS или RELEASE при keyUp

2. **Добавить защиту от повторных LONG_PRESS**:
   - В `_handle_long_press()` проверять, что микрофон **НЕ активен** (`_mic_active == False`)
   - Если микрофон уже активен, игнорировать LONG_PRESS

3. **Улучшить обработку RELEASE**:
   - Гарантировать, что RELEASE **всегда** останавливает микрофон, даже если `_recording_started == False`
   - Добавить принудительную остановку микрофона при RELEASE

### Приоритет 2: Важно

4. **Улучшить логирование**:
   - Добавить детальное логирование состояния микрофона при каждом LONG_PRESS/RELEASE
   - Логировать race conditions для диагностики

5. **Добавить таймауты**:
   - Если микрофон активен > 30 секунд без RELEASE, принудительно остановить его
   - Добавить watchdog для обнаружения залипания

### Приоритет 3: Желательно

6. **Улучшить пороги**:
   - Увеличить `long_press_threshold` до 1.0-1.5 секунды, чтобы избежать случайной активации при написании с большой буквы
   - Добавить конфигурируемый порог для различения "написание с большой буквы" vs "активация микрофона"

## Выводы

### Основная причина залипания

**Наиболее вероятная причина**: Двойная генерация LONG_PRESS (из hold_monitor и при keyUp) создает race condition, при которой второй LONG_PRESS перезаписывает состояние, и RELEASE останавливает неправильную сессию.

**Сценарий залипания**:
1. Пользователь зажимает Shift для написания с большой буквы (> 0.6 сек)
2. Hold_monitor генерирует LONG_PRESS → микрофон активируется
3. Пользователь отпускает Shift
4. При keyUp генерируется второй LONG_PRESS (если duration >= 0.6)
5. Второй LONG_PRESS перезаписывает `_current_session_id`
6. RELEASE останавливает неправильную сессию
7. Микрофон остается активным

### Дополнительные факторы

1. **Низкий порог LONG_PRESS**: 0.6 секунды слишком мало для различения "написание с большой буквы" vs "активация микрофона"
2. **Отсутствие защиты от повторных LONG_PRESS**: Нет проверки, что микрофон уже активен
3. **Race condition**: LONG_PRESS и RELEASE могут обрабатываться в неправильном порядке

