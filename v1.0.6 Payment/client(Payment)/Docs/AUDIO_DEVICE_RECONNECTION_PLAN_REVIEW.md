# Обзор плана переподключения аудио-устройств

**Дата:** 2025-12-02  
**Статус:** Конструктивная обратная связь

## Общая оценка

План **хорошо структурирован** и решает ключевые проблемы, выявленные в анализе архитектуры. Однако есть несколько важных дополнений и уточнений, которые повысят надежность реализации.

---

## ✅ Сильные стороны плана

### 1. Структура (3 цикла)
- **Цикл 1** (Защита) - правильно идентифицирует проблему concurrent переключений
- **Цикл 2** (Fallback) - решает проблему ошибок PortAudio (-9986/-10851)
- **Цикл 3** (Переинициализация) - обеспечивает правильный порядок операций

### 2. Учет текущей архитектуры
- Использует существующие компоненты (AudioStreamManager, DeviceChangePublisher)
- Не требует переписывания всей системы
- Интегрируется с текущим кодом

### 3. Фокус на проблемах
- Решает проблему таймаутов 15+ секунд
- Обрабатывает ошибки PortAudio
- Предотвращает race conditions

---

## ⚠️ Что нужно дополнить

### 1. Цикл 1: Защита и последовательность

#### ✅ Что хорошо:
- Идея с `_switch_in_progress` флагом правильная
- Использование `_device_tracking_lock` (уже есть в коде)

#### 🔧 Что дополнить:

**1.1. Атомарная проверка и установка guard:**
```python
# Текущий код не имеет защиты от concurrent вызовов
# Нужно добавить:
_switch_in_progress_lock = threading.RLock()  # Отдельный lock для переключения
_switch_in_progress = False

def _switch_output_device(self, ...):
    # Атомарная проверка и установка
    with self._switch_in_progress_lock:
        if self._switch_in_progress:
            logger.warning("⚠️ [OUTPUT] Переключение уже выполняется, игнорируем")
            return
        self._switch_in_progress = True
    
    try:
        # ... логика переключения ...
    finally:
        # ВСЕГДА сбрасываем guard, даже при ошибке
        with self._switch_in_progress_lock:
            self._switch_in_progress = False
```

**1.2. Проверка изменения устройства:**
```python
# В _on_output_device_changed нужно проверять:
async def _on_output_device_changed(self, event):
    new_name = event.get("device_name")
    new_id = event.get("device_id")
    
    # Получаем текущее устройство атомарно
    with self._player._device_tracking_lock:
        current_name = self._player.output_device_name
        current_id = self._player._current_output_device_id
    
    # Сравниваем по ИМЕНИ (источник истины), а не по ID
    if new_name == current_name:
        logger.debug("ℹ️ [OUTPUT] Устройство не изменилось (имя совпадает)")
        return
    
    # Проверяем guard
    if self._player._switch_in_progress:
        logger.warning("⚠️ [OUTPUT] Переключение уже выполняется, игнорируем новое событие")
        return
    
    # Запускаем переключение
    self._player._switch_output_device(new_name, new_id, is_bluetooth)
```

**1.3. Таймаут для guard:**
```python
# Защита от "залипания" guard при ошибке
_switch_in_progress_start_time: Optional[float] = None
_switch_in_progress_timeout = 10.0  # секунд

def _switch_output_device(self, ...):
    with self._switch_in_progress_lock:
        if self._switch_in_progress:
            # Проверяем таймаут
            if self._switch_in_progress_start_time:
                elapsed = time.time() - self._switch_in_progress_start_time
                if elapsed > self._switch_in_progress_timeout:
                    logger.error(f"❌ [OUTPUT] Guard залип на {elapsed:.1f}s, принудительно сбрасываем")
                    self._switch_in_progress = False
                else:
                    logger.warning("⚠️ [OUTPUT] Переключение уже выполняется, игнорируем")
                    return
        self._switch_in_progress = True
        self._switch_in_progress_start_time = time.time()
    
    try:
        # ... логика ...
    finally:
        with self._switch_in_progress_lock:
            self._switch_in_progress = False
            self._switch_in_progress_start_time = None
```

### 2. Цикл 2: Актуальные параметры и fallback

#### ✅ Что хорошо:
- Идея кэша успешных конфигураций правильная
- Fallback на `device=None` для BT устройств

#### 🔧 Что дополнить:

**2.1. Кэш успешных конфигураций:**
```python
# Уже есть _device_error_cache для ошибок, нужно добавить для успешных:
_last_successful_config: Dict[str, StreamConfig] = {}  # device_name|BT -> StreamConfig
_successful_config_lock = threading.RLock()

def _get_safe_stream_config(self, device_name, is_bluetooth, device_id):
    cache_key = f"{device_name}|{is_bluetooth}"
    
    # Проверяем кэш успешных конфигураций
    with self._successful_config_lock:
        if cache_key in self._last_successful_config:
            cached_config = self._last_successful_config[cache_key]
            logger.info(f"✅ [OUTPUT] Используем кэшированную конфигурацию для {device_name}")
            return cached_config
    
    # Создаем новую конфигурацию
    config = self._build_stream_config_for_output_device(device_name, device_id, is_bluetooth)
    
    # Сохраняем в кэш после успешного создания потока
    return config

def _on_stream_created_successfully(self, config, device_name, is_bluetooth):
    cache_key = f"{device_name}|{is_bluetooth}"
    with self._successful_config_lock:
        self._last_successful_config[cache_key] = config
        logger.debug(f"✅ [OUTPUT] Конфигурация сохранена в кэш: {cache_key}")
```

**2.2. Улучшенный fallback:**
```python
# В AudioStreamManager.create_stream() при ошибке -9986/-10851:
if error_code in (-9986, -10851):
    # Первая попытка: используем текущую конфигурацию
    if attempt == 1:
        # Повторяем с той же конфигурацией
        await asyncio.sleep(retry_delay)
        continue
    
    # Вторая попытка: fallback на device=None, очищаем blocksize/latency
    if attempt == 2:
        logger.warning(f"⚠️ [{self.stream_type.upper()}] Fallback на device=None после ошибки {error_code}")
        fallback_config = StreamConfig(
            device_id=None,  # macOS выберет сам
            device_name=config.device_name,
            samplerate=config.samplerate,
            channels=config.channels,
            dtype=config.dtype,
            callback=config.callback,
            blocksize=None,  # Не задаем
            latency=None,    # Не задаем
            is_bluetooth=config.is_bluetooth
        )
        # Пробуем с fallback конфигурацией
        try:
            stream = self._create_stream_with_config(fallback_config)
            # Успех - сохраняем fallback конфигурацию
            return StreamOperationResult(success=True, stream=stream, ...)
        except Exception as e:
            logger.error(f"❌ [{self.stream_type.upper()}] Fallback также не удался: {e}")
            # Продолжаем с обычным retry
```

**2.3. Логирование параметров:**
```python
# Перед create_stream/switch_device логировать ВСЕ параметры:
logger.info(
    f"🔍 [{self.stream_type.upper()}] Создание потока (попытка {attempt}/{max_retries}):\n"
    f"   device_id={config.device_id}, device_name={config.device_name}\n"
    f"   samplerate={config.samplerate}Hz, channels={config.channels}\n"
    f"   dtype={config.dtype}, blocksize={config.blocksize}, latency={config.latency}\n"
    f"   is_bluetooth={config.is_bluetooth}, callback={config.callback is not None}"
)
```

### 3. Цикл 3: Переинициализация при новом устройстве

#### ✅ Что хорошо:
- Правильный порядок операций (очистка буфера → stop → switch)
- Обновление tracking полей

#### 🔧 Что дополнить:

**3.1. Обработка отмены переключения:**
```python
# Если устройство снова изменилось во время переключения:
_switch_cancelled = False

def _switch_output_device(self, new_name, new_id, is_bluetooth):
    with self._switch_in_progress_lock:
        if self._switch_in_progress:
            # Проверяем, не изменилось ли устройство снова
            if new_name != self._pending_switch_device_name:
                logger.warning(f"⚠️ [OUTPUT] Устройство изменилось во время переключения: "
                             f"{self._pending_switch_device_name} → {new_name}")
                self._switch_cancelled = True
                return
        self._pending_switch_device_name = new_name
    
    try:
        # ... логика переключения ...
        # Проверяем отмену перед финальным обновлением
        if self._switch_cancelled:
            logger.info("ℹ️ [OUTPUT] Переключение отменено, новое устройство уже обрабатывается")
            return
    finally:
        with self._switch_in_progress_lock:
            self._switch_in_progress = False
            self._switch_cancelled = False
            self._pending_switch_device_name = None
```

**3.2. Уменьшение таймаута для switch_device:**
```python
# В _switch_output_device использовать уменьшенный таймаут:
timeout_sec = 5.0 if is_bluetooth else 3.0  # Вместо 10.0/5.0

# И уменьшить количество попыток:
result = self._run_async_in_thread(
    self._stream_manager.switch_device(old_stream, stream_config, max_retries=2),  # Вместо 5
    timeout_sec,
    "switch_device"
)
```

**3.3. Гарантированная очистка _stop_event:**
```python
# В _switch_output_device ВСЕГДА очищать _stop_event в finally:
try:
    # ... логика переключения ...
    if result.success:
        self._stop_event.clear()
    else:
        self._stop_event.clear()  # Очищаем даже при ошибке
except Exception as e:
    logger.error(f"❌ [OUTPUT] Ошибка переключения: {e}")
    self._stop_event.clear()  # Очищаем в любом случае
finally:
    # Дополнительная гарантия
    if self._stop_event.is_set():
        logger.warning("⚠️ [OUTPUT] _stop_event все еще установлен, принудительно очищаем")
        self._stop_event.clear()
```

### 4. Валидация и контроль

#### ✅ Что хорошо:
- Покрытие тестовых сценариев
- Проверка guard и _stop_event

#### 🔧 Что дополнить:

**4.1. Метрики времени переключения:**
```python
# Добавить метрики для мониторинга:
_switch_device_times: List[float] = []  # История времени переключения
_max_switch_device_history = 100

def _switch_output_device(self, ...):
    start_time = time.time()
    try:
        # ... логика ...
    finally:
        duration = time.time() - start_time
        self._switch_device_times.append(duration)
        if len(self._switch_device_times) > self._max_switch_device_history:
            self._switch_device_times.pop(0)
        
        # Логируем метрики
        avg_time = sum(self._switch_device_times) / len(self._switch_device_times)
        logger.info(f"📊 [OUTPUT] Время переключения: {duration:.2f}s (среднее: {avg_time:.2f}s)")
        
        # Предупреждение при долгом переключении
        if duration > 3.0:
            logger.warning(f"⚠️ [OUTPUT] Долгое переключение: {duration:.2f}s")
```

**4.2. Тесты для edge cases:**
```python
# Добавить тесты для:
# 1. Быстрые повторные события (debounce)
# 2. Отмена переключения (устройство изменилось снова)
# 3. Ошибки PortAudio с fallback
# 4. Guard залипание (таймаут)
# 5. BT vs обычные устройства
```

**4.3. Логирование decision-логов:**
```python
# Добавить decision-логи в каноническом формате:
logger.info(
    f"decision=switch_device "
    f"ctx={{device={device_name},bt={is_bluetooth},old_stream={old_stream is not None}}} "
    f"source=output_device_change "
    f"duration_ms={duration_ms:.1f}"
)
```

---

## 🔴 Критические дополнения

### 1. Связь с проблемой INPUT (race condition)

План фокусируется на OUTPUT, но проблема "зависания при зажатии клавиши" также связана с INPUT. Нужно:

```python
# В InputProcessingIntegration._can_start_recording():
async def _can_start_recording(self) -> tuple[bool, str]:
    # ... существующие проверки ...
    
    # ✅ ДОПОЛНИТЕЛЬНО: Проверяем, не идет ли переключение OUTPUT устройства
    # (может блокировать активацию микрофона)
    if self._player and hasattr(self._player, '_switch_in_progress'):
        if self._player._switch_in_progress:
            return False, "output_device_switching"
    
    return True, "ok"
```

### 2. Обработка быстрых повторных событий

DeviceChangePublisher имеет debounce (300ms), но нужно дополнительно защититься:

```python
# В _on_output_device_changed добавить debounce:
_last_device_change_time = 0.0
_device_change_debounce = 0.5  # секунд

async def _on_output_device_changed(self, event):
    now = time.time()
    if now - self._last_device_change_time < self._device_change_debounce:
        logger.debug(f"🔒 [OUTPUT] Debounce: игнорируем событие (прошло {now - self._last_device_change_time:.3f}s)")
        return
    
    self._last_device_change_time = now
    # ... остальная логика ...
```

### 3. Интеграция с AudioStreamManager

Нужно убедиться, что AudioStreamManager поддерживает кэш и fallback:

```python
# В AudioStreamManager добавить поддержку кэша:
def set_successful_config_cache(self, cache: Dict, lock: threading.RLock):
    """Устанавливает внешний кэш для успешных конфигураций"""
    self._external_successful_cache = cache
    self._external_cache_lock = lock

def _get_cached_config(self, config: StreamConfig) -> Optional[StreamConfig]:
    """Получает кэшированную конфигурацию"""
    if not hasattr(self, '_external_successful_cache'):
        return None
    
    cache_key = self._get_config_cache_key(config)
    with self._external_cache_lock:
        return self._external_successful_cache.get(cache_key)
```

---

## 📋 Чек-лист реализации

### Цикл 1: Защита
- [ ] Добавить `_switch_in_progress` флаг и lock
- [ ] Добавить таймаут для guard (защита от залипания)
- [ ] Проверка изменения устройства по имени (не по ID)
- [ ] Логирование guard состояния
- [ ] Гарантированная очистка `_stop_event` в finally

### Цикл 2: Fallback
- [ ] Кэш успешных конфигураций (`_last_successful_config`)
- [ ] Логирование всех параметров перед созданием потока
- [ ] Fallback на `device=None` при ошибке -9986/-10851
- [ ] Обновление кэша после успешного создания
- [ ] Интеграция кэша с AudioStreamManager

### Цикл 3: Переинициализация
- [ ] Обработка отмены переключения (быстрое изменение устройства)
- [ ] Уменьшение таймаута для switch_device (3-5s вместо 15s)
- [ ] Уменьшение количества попыток (2 вместо 5)
- [ ] Правильный порядок операций (очистка → stop → switch)
- [ ] Обновление tracking полей атомарно

### Валидация
- [ ] Метрики времени переключения
- [ ] Decision-логи в каноническом формате
- [ ] Тесты для edge cases
- [ ] Интеграция с INPUT (проверка переключения OUTPUT)

---

## 🎯 Приоритеты реализации

### Высокий приоритет (критические проблемы):
1. **Guard защита** - предотвращает concurrent переключения
2. **Уменьшение таймаута** - решает проблему "зависания" (15s → 3-5s)
3. **Fallback на device=None** - решает ошибки PortAudio

### Средний приоритет (улучшения):
4. **Кэш успешных конфигураций** - ускоряет повторные переключения
5. **Метрики времени** - для мониторинга и диагностики
6. **Обработка отмены** - для быстрых повторных событий

### Низкий приоритет (оптимизации):
7. **Decision-логи** - для анализа и отладки
8. **Интеграция с INPUT** - для координации переключений

---

## 📝 Рекомендации

1. **Начать с Цикл 1** - это решает основную проблему concurrent переключений
2. **Добавить таймаут для guard** - защита от залипания критична
3. **Уменьшить таймаут switch_device** - это сразу улучшит UX
4. **Реализовать fallback** - решает большинство ошибок PortAudio
5. **Добавить метрики** - для мониторинга эффективности изменений

---

## ✅ Заключение

План **хорошо продуман** и решает ключевые проблемы. Предложенные дополнения:
- Усиливают защиту от race conditions
- Улучшают обработку ошибок
- Добавляют мониторинг и диагностику
- Интегрируют с существующей архитектурой

Рекомендую начать реализацию с **Цикл 1** (защита), так как это решает основную проблему "зависания" при зажатии клавиши.

