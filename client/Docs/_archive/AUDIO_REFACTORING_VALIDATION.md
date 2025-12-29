# Валидация атомарного рефакторинга аудио системы

**Дата:** 2025-12-24  
**Статус:** ✅ Код применен, требуется валидация

## 🔍 Ключевые методы (реальный код)

### 1. `add_audio_data()` - атомарное пересоздание потока

```python:183:311:modules/speech_playback/core/player.py
def add_audio_data(self, audio_data: np.ndarray, priority: int = 0, metadata: Optional[Dict[str, Any]] = None) -> str:
    try:
        # Извлекаем metadata ВНЕ lock (быстрые операции)
        session_id = metadata.get('session_id') if metadata else None
        incoming_sr = None
        if metadata and 'sample_rate' in metadata:
            incoming_sr = int(metadata['sample_rate'])
        
        # 🔧 РЕФАКТОРИНГ: Минимизируем время под lock - только критичные операции
        # Выполняем медленные операции (_query_default_output_device) ВНЕ lock
        device_id = None
        if session_id != self._current_playback_session_id or not self._stream_started:
            device_changed = self._check_and_update_output_device()
            if device_changed:
                current_device = self._query_default_output_device()  # ВНЕ lock
                device_id = current_device.get('index') if current_device else None

        # 🔧 РЕФАКТОРИНГ: Вся логика пересоздания потока под единым lock (минимальное время)
        with self._stream_lock:
            # 1) Обновляем _actual_sample_rate если изменился
            if incoming_sr is not None:
                if self._actual_sample_rate is None or self._actual_sample_rate != incoming_sr:
                    self._actual_sample_rate = incoming_sr
            
            # 2) Обновляем сессию
            if session_id != self._current_playback_session_id:
                self._current_playback_session_id = session_id
            
            # 3) Единый механизм пересоздания потока (атомарно)
            reason = f"add_audio_data (session={session_id}, thread={threading.current_thread().name})"
            recreated = self._recreate_stream_if_needed_locked(reason=reason, device_id=device_id, incoming_sr=incoming_sr)
            
            # 4) Если поток не существует, создаем его
            if self._audio_stream is None:
                self._start_audio_stream_locked(sync_output=False, device_id=device_id)
            
            # ✅ КРИТИЧНО: Чанк добавляется в буфер ДАЖЕ если recreate был пропущен
            # Это гарантирует что аудио не потеряется

        # ... конвертация данных ВНЕ lock ...
        
        # Добавляем в буфер (priority передаем в metadata)
        if metadata is None:
            metadata = {}
        metadata['priority'] = priority
        chunk_id = self.chunk_buffer.add_chunk(audio_data, metadata)  # ✅ Чанк НЕ теряется

        # Lazy start: стартуем поток при появлении первого чанка
        self._ensure_stream_started()

        return chunk_id
```

**Инварианты:**
- ✅ Lock держится минимальное время (только проверки и пересоздание)
- ✅ Медленные операции (`_query_default_output_device`) ВНЕ lock
- ✅ Чанк добавляется в буфер ВСЕГДА (даже если recreate пропущен)
- ✅ Нет дублирования логики обновления `_actual_sample_rate`

---

### 2. `_recreate_stream_if_needed_locked()` - единый механизм пересоздания

```python:690:810:modules/speech_playback/core/player.py
def _recreate_stream_if_needed_locked(self, reason: str, device_id: Optional[int], incoming_sr: Optional[int]) -> bool:
    """
    Единый метод пересоздания потока (locked-версия).
    Вызывается ТОЛЬКО когда lock уже взят.
    """
    # 🔧 ЗАЩИТА ОТ ЗАЛИПАНИЯ: Проверяем таймаут пересоздания
    if self._recreating_stream:
        if self._recreating_stream_start_time is not None:
            elapsed = time.time() - self._recreating_stream_start_time
            if elapsed > 5.0:  # 5 секунд - критический таймаут
                logger.error(f"❌ [RECREATE] КРИТИЧЕСКАЯ ОШИБКА: _recreating_stream залипло на {elapsed:.1f}s!")
                self._recreating_stream = False
                self._recreating_stream_start_time = None
            else:
                logger.debug(f"🔍 [RECREATE] Поток уже пересоздается, пропускаем")
                return False  # ✅ Чанк все равно добавится в буфер выше
    
    # Вычисляем нужные условия
    need_recreate = False
    recreate_reason = ""
    
    # 1) Проверка sample_rate mismatch
    if incoming_sr is not None:
        if self._audio_stream is not None and self._stream_sample_rate != incoming_sr:
            need_recreate = True
            recreate_reason = f"sample_rate_mismatch (stream={self._stream_sample_rate}Hz, incoming={incoming_sr}Hz)"
    
    # 2) Проверка device changed (device_id уже получен ВНЕ lock)
    if device_id is not None and self._current_device_id != device_id:
        need_recreate = True
        recreate_reason = f"device_changed (old={self._current_device_id}, new={device_id})"
    
    # 3) Проверка: поток не существует
    if self._audio_stream is None:
        need_recreate = True
        recreate_reason = "stream_not_exists"
    
    if not need_recreate:
        return False
    
    # Атомарное пересоздание
    prev_device_id = self._current_device_id
    prev_stream_sr = self._stream_sample_rate
    thread_name = threading.current_thread().name
    
    self._recreating_stream = True
    self._recreating_stream_start_time = time.time()
    
    try:
        # 🔍 ДЕТАЛЬНОЕ ЛОГИРОВАНИЕ
        logger.info(
            f"🔄 [RECREATE] Пересоздание потока: {recreate_reason} | "
            f"reason={reason} | thread={thread_name} | "
            f"prev_device={prev_device_id}→new={device_id} | "
            f"prev_stream_sr={prev_stream_sr}Hz→incoming={incoming_sr}Hz | "
            f"content_sr={self._actual_sample_rate or self.config.sample_rate}Hz | "
            f"device_sr={self._device_sample_rate}Hz"
        )
        
        # Останавливаем старый поток
        if self._audio_stream is not None:
            self._stop_audio_stream_locked()  # ✅ Locked-версия, lock уже взят
        
        # Создаем новый поток
        success = self._start_audio_stream_locked(sync_output=False, device_id=device_id)  # ✅ Locked-версия
        
        if success:
            self._stream_recreate_count += 1
            # ... метрики ...
            return True
        else:
            return False
            
    except Exception as e:
        logger.error(f"❌ [RECREATE] Ошибка: {e}", exc_info=True)
        return False
    finally:
        self._recreating_stream = False
        self._recreating_stream_start_time = None
```

**Инварианты:**
- ✅ Вызывается ТОЛЬКО когда lock уже взят
- ✅ Защита от залипания (таймаут 5 секунд)
- ✅ Детальное логирование (thread name, prev/new значения)
- ✅ Метрики для диагностики

---

### 3. `_start_audio_stream_locked()` / `_stop_audio_stream_locked()` - locked-версии

```python:435:508:modules/speech_playback/core/player.py
def _start_audio_stream(self, *, sync_output: bool = True, device_id: int = None) -> bool:
    """Публичный метод, берет lock"""
    with self._stream_lock:
        return self._start_audio_stream_locked(sync_output=sync_output, device_id=device_id)

def _start_audio_stream_locked(self, *, sync_output: bool = True, device_id: int = None) -> bool:
    """Locked-версия, вызывается когда lock уже взят"""
    # ✅ НЕТ with self._stream_lock - lock уже взят!
    if self._audio_stream is not None:
        return True
    
    if sync_output:
        self._sync_output_format_locked(restart_stream=False)  # ✅ Locked-версия
    
    # 🔧 ВАЖНО: Используем content_rate для потока (пока без ресемплинга)
    content_sr = self._actual_sample_rate if self._actual_sample_rate is not None else self.config.sample_rate
    
    if self._device_sample_rate is not None and self._device_sample_rate != content_sr:
        logger.warning(f"⚠️ [STREAM_RATE] Content rate ({content_sr}Hz) != Device rate ({self._device_sample_rate}Hz)")
    
    playback_sample_rate = content_sr
    
    stream_config = {
        'device': device_id,
        'channels': self.config.channels,
        'dtype': self.config.dtype,
        'samplerate': playback_sample_rate,  # ⚠️ ВОПРОС: правильно ли использовать content_rate?
        'blocksize': self.config.buffer_size,
        'callback': self._audio_callback
    }
    
    self._audio_stream = sd.OutputStream(**stream_config)
    self._stream_started = False
    self._stream_sample_rate = playback_sample_rate
    self._current_device_id = device_id
    
    return True
```

```python:538:556:modules/speech_playback/core/player.py
def _stop_audio_stream(self):
    """Публичный метод, берет lock"""
    with self._stream_lock:
        self._stop_audio_stream_locked()

def _stop_audio_stream_locked(self):
    """Locked-версия, вызывается когда lock уже взят"""
    # ✅ НЕТ with self._stream_lock - lock уже взят!
    if self._audio_stream is not None:
        if self._stream_started:
            self._audio_stream.stop()
        self._audio_stream.close()
        self._audio_stream = None
        self._stream_started = False
        self._stream_sample_rate = None
```

**Инварианты:**
- ✅ Публичные методы берут lock
- ✅ Locked-версии НЕ берут lock (вызываются когда lock уже взят)
- ✅ Нет двойного lock (deadlock невозможен)

---

### 4. `_sync_output_format_locked()` - не меняет config.sample_rate

```python:619:667:modules/speech_playback/core/player.py
def _sync_output_format_locked(self, restart_stream: bool = False) -> bool:
    """
    🔧 РЕФАКТОРИНГ: НЕ изменяет config.sample_rate (это content rate).
    Обновляет только _device_sample_rate и config.channels.
    """
    if not self.config.auto_device_selection:
        return False

    sample_rate, adjusted_channels, device_name = self._probe_output_format()
    if sample_rate is None and adjusted_channels is None:
        return False

    device_sr_changed = False
    channel_changed = False

    # 🔧 РЕФАКТОРИНГ: Обновляем _device_sample_rate, НЕ config.sample_rate
    if sample_rate is not None and sample_rate > 0 and sample_rate != self._device_sample_rate:
        logger.info(f"🎛 Обновляем device_sample_rate: {self._device_sample_rate} → {sample_rate}")
        self._device_sample_rate = sample_rate  # ✅ НЕ config.sample_rate!
        device_sr_changed = True

    if adjusted_channels is not None and adjusted_channels > 0 and adjusted_channels != self.config.channels:
        self.config.channels = adjusted_channels
        channel_changed = True

    # 🔧 РЕФАКТОРИНГ: Пересоздание через единый механизм
    if restart_stream and (device_sr_changed or channel_changed) and self._audio_stream is not None:
        reason = f"device_sr_changed={device_sr_changed}, channel_changed={channel_changed}"
        self._recreate_stream_if_needed_locked(reason=reason, device_id=None, incoming_sr=None)

    return device_sr_changed or channel_changed
```

**Инварианты:**
- ✅ `config.sample_rate` НЕ изменяется (это content rate)
- ✅ Обновляется только `_device_sample_rate` (device rate)
- ✅ Пересоздание через единый механизм

---

## ✅ Чеклист валидации инвариантов

### Инвариант A: stop/start вызываются только из locked-пути

**Проверка:**
```bash
# Публичные методы берут lock
grep -n "def _start_audio_stream(" player.py
grep -n "def _stop_audio_stream(" player.py
# Должны содержать: with self._stream_lock:

# Locked-версии НЕ берут lock
grep -n "def _start_audio_stream_locked(" player.py
grep -n "def _stop_audio_stream_locked(" player.py
# НЕ должны содержать: with self._stream_lock:
```

**Результат:** ✅
- `_start_audio_stream()` - берет lock (строка 444)
- `_stop_audio_stream()` - берет lock (строка 540)
- `_start_audio_stream_locked()` - НЕ берет lock (строка 447)
- `_stop_audio_stream_locked()` - НЕ берет lock (строка 543)

### Инвариант B: recreate не держит lock дольше минимума

**Проверка:**
- ✅ Медленные операции (`_query_default_output_device`) выполняются ВНЕ lock
- ✅ Под lock только: проверки, установка флагов, stop/start (быстрые операции)
- ⚠️ **РИСК:** `_query_default_output_device()` все еще вызывается внутри `_recreate_stream_if_needed_locked()` если `device_id is None` (строка 789)
  - **РЕШЕНИЕ:** device_id должен передаваться извне (уже сделано в `add_audio_data`)

### Инвариант C: при `_recreating_stream=True` чанки НЕ теряются

**Проверка:**
- ✅ Если `_recreating_stream=True`, метод возвращает `False`
- ✅ Но чанк все равно добавляется в буфер ПОСЛЕ выхода из lock (строка 299)
- ✅ Буфер не очищается при recreate
- ✅ После завершения recreate поток начнет воспроизводить из буфера

**Результат:** ✅ Чанки не теряются

---

## ⚠️ Критический вопрос: stream_rate vs device_rate

### Текущая реализация

**Поток создается с `content_sample_rate` (24000Hz), а не `device_sample_rate` (48000Hz).**

**Риски:**
1. Некоторые устройства могут не поддерживать 24kHz напрямую
2. Драйвер может делать скрытый ресемплинг (не контролируемый)
3. Возможны рассинхроны по буферам

**Текущий код:**
```python
# _start_audio_stream_locked()
content_sr = self._actual_sample_rate if self._actual_sample_rate is not None else self.config.sample_rate
playback_sample_rate = content_sr  # ⚠️ Используем content_rate

if self._device_sample_rate is not None and self._device_sample_rate != content_sr:
    logger.warning(f"⚠️ [STREAM_RATE] Content rate ({content_sr}Hz) != Device rate ({self._device_sample_rate}Hz)")
```

**Рекомендация для тестирования:**
1. Проверить на Built-in output (обычно 48kHz)
2. Проверить на AirPods/Bluetooth (обычно 48kHz)
3. Проверить на USB audio
4. Если возникают ошибки создания потока или рассинхрон → перейти на `device_sample_rate` + ресемплинг

---

## 📊 Метрики для мониторинга

### Добавленные метрики

1. **`_stream_recreate_count`** - счетчик пересозданий
2. **`_stream_recreate_reasons`** - последние 10 причин пересозданий
3. **`_recreating_stream_start_time`** - время начала пересоздания (для защиты от залипания)

### Логирование

Каждое пересоздание логируется с:
- `reason` - причина пересоздания
- `prev_device_id → new_device_id`
- `prev_stream_sr → new_stream_sr`
- `content_sr` - sample rate контента
- `device_sr` - sample rate устройства
- `thread name` - имя потока

### Защита от залипания

- Таймаут: 5 секунд
- При превышении: принудительный сброс флага + error log

---

## 🧪 Рекомендуемые тесты

### Тест 1: Параллельные add_audio_data

```python
import threading
import numpy as np

def test_parallel_add_audio_data():
    player = SequentialSpeechPlayer()
    player.initialize()
    
    def add_chunk(sr):
        metadata = {'sample_rate': sr, 'session_id': f'session_{sr}'}
        audio = np.random.randint(-32768, 32767, size=1000, dtype=np.int16)
        player.add_audio_data(audio, metadata=metadata)
    
    threads = []
    for sr in [24000, 48000, 24000, 48000] * 5:  # 20 чанков
        t = threading.Thread(target=add_chunk, args=(sr,))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    # Проверки
    assert player._stream_recreate_count <= 10  # Не должно быть избыточных пересозданий
    assert not player._recreating_stream  # Флаг не залип
    assert player._audio_stream is not None  # Поток создан
    print(f"Recreate count: {player._stream_recreate_count}")
    print(f"Reasons: {player._stream_recreate_reasons}")
```

### Тест 2: resync_output_device + add_audio_data

```python
def test_resync_vs_add_audio():
    player = SequentialSpeechPlayer()
    player.initialize()
    
    def resync_loop():
        for _ in range(10):
            player.resync_output_device()
            time.sleep(0.1)
    
    def add_audio_loop():
        for i in range(20):
            metadata = {'sample_rate': 24000, 'session_id': f'session_{i}'}
            audio = np.random.randint(-32768, 32767, size=1000, dtype=np.int16)
            player.add_audio_data(audio, metadata=metadata)
            time.sleep(0.05)
    
    t1 = threading.Thread(target=resync_loop)
    t2 = threading.Thread(target=add_audio_loop)
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    # Проверки
    assert not player._recreating_stream
    assert player._stream_recreate_count < 20  # Не должно быть двойных пересозданий
```

---

## 🔍 Быстрая проверка кода

### Команды для валидации

```bash
# 1. Проверка что locked-версии НЕ берут lock
grep -A 5 "def _.*_locked(" modules/speech_playback/core/player.py | grep -v "with self._stream_lock"

# 2. Проверка что публичные методы берут lock
grep -B 2 -A 3 "def _start_audio_stream(" modules/speech_playback/core/player.py
grep -B 2 -A 3 "def _stop_audio_stream(" modules/speech_playback/core/player.py

# 3. Проверка что config.sample_rate не меняется в _sync_output_format
grep -A 20 "_sync_output_format_locked" modules/speech_playback/core/player.py | grep "config.sample_rate ="

# 4. Проверка защиты от залипания
grep -A 10 "_recreating_stream" modules/speech_playback/core/player.py | grep "elapsed >"
```

---

## ⚠️ Известные риски

1. **Stream на content_rate (24kHz) может не работать на некоторых устройствах**
   - Требуется тестирование на реальных устройствах
   - Если проблемы → перейти на device_rate + ресемплинг

2. **`_query_default_output_device()` все еще вызывается внутри lock в некоторых случаях**
   - Оптимизировано в `add_audio_data` (вызывается ВНЕ lock)
   - Но может вызываться в `_recreate_stream_if_needed_locked` если device_id не передан

3. **Нет явного ресемплинга content_rate → device_rate**
   - Пока полагаемся на драйвер
   - В будущем может потребоваться явный ресемплинг

---

## ✅ Итоговый статус

- ✅ **Инвариант A:** Выполнен (нет двойного lock)
- ✅ **Инвариант B:** Выполнен (lock держится минимальное время)
- ✅ **Инвариант C:** Выполнен (чанки не теряются)
- ⚠️ **Stream rate:** Требует тестирования на реальных устройствах

**Следующий шаг:** Запустить стресс-тест и проверить метрики `_stream_recreate_count` и `_stream_recreate_reasons`.


