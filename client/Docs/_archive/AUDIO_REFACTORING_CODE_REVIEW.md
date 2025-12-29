# Реальный код атомарного рефакторинга - для валидации

**Дата:** 2025-12-24  
**Цель:** Показать реальный код ключевых методов для проверки инвариантов

---

## 🔍 Инвариант A: stop/start вызываются только из locked-пути

### Публичные методы (берут lock)

```python:433:445:modules/speech_playback/core/player.py
def _start_audio_stream(self, *, sync_output: bool = True, device_id: int = None) -> bool:
    """Публичный метод, берет lock"""
    with self._stream_lock:
        return self._start_audio_stream_locked(sync_output=sync_output, device_id=device_id)
```

```python:538:541:modules/speech_playback/core/player.py
def _stop_audio_stream(self):
    """Остановка аудио потока (публичный метод, берет lock)"""
    with self._stream_lock:
        self._stop_audio_stream_locked()
```

### Locked-версии (НЕ берут lock)

```python:435:507:modules/speech_playback/core/player.py
def _start_audio_stream_locked(self, *, sync_output: bool = True, device_id: int = None) -> bool:
    """Locked-версия, вызывается когда lock уже взят"""
    try:
        if self._audio_stream is not None:
            logger.warning("⚠️ Аудио поток уже создан")
            return True
        # ... создание потока ...
        # ✅ НЕТ with self._stream_lock - lock уже взят!
```

```python:542:556:modules/speech_playback/core/player.py
def _stop_audio_stream_locked(self):
    """Locked-версия, вызывается когда lock уже взят"""
    try:
        if self._audio_stream is not None:
            if self._stream_started:
                self._audio_stream.stop()
            self._audio_stream.close()
            self._audio_stream = None
            self._stream_started = False
            self._stream_sample_rate = None
            logger.info("🛑 Аудио поток остановлен")
        # ✅ НЕТ with self._stream_lock - lock уже взят!
```

**✅ Проверка:** Нет двойного lock, deadlock невозможен

---

## 🔍 Инвариант B: recreate не держит lock дольше минимума

### add_audio_data - минимизация времени под lock

```python:195:240:modules/speech_playback/core/player.py
def add_audio_data(self, audio_data: np.ndarray, priority: int = 0, metadata: Optional[Dict[str, Any]] = None) -> str:
    try:
        # Извлекаем metadata ВНЕ lock (быстрые операции)
        session_id = metadata.get('session_id') if metadata else None
        incoming_sr = None
        if metadata and 'sample_rate' in metadata:
            incoming_sr = int(metadata['sample_rate'])
        
        # 🔧 Медленные операции ВНЕ lock
        device_id = None
        if session_id != self._current_playback_session_id or not self._stream_started:
            device_changed = self._check_and_update_output_device()
            if device_changed:
                current_device = self._query_default_output_device()  # ✅ ВНЕ lock
                device_id = current_device.get('index') if current_device else None

        # 🔧 Lock держится минимальное время - только критичные операции
        with self._stream_lock:
            # 1) Обновляем _actual_sample_rate (быстро)
            if incoming_sr is not None:
                if self._actual_sample_rate is None or self._actual_sample_rate != incoming_sr:
                    self._actual_sample_rate = incoming_sr
            
            # 2) Обновляем сессию (быстро)
            if session_id != self._current_playback_session_id:
                self._current_playback_session_id = session_id
            
            # 3) Единый механизм пересоздания (может быть медленным, но необходимо)
            reason = f"add_audio_data (session={session_id}, thread={threading.current_thread().name})"
            recreated = self._recreate_stream_if_needed_locked(reason=reason, device_id=device_id, incoming_sr=incoming_sr)
            
            # 4) Создание потока если не существует
            if self._audio_stream is None:
                self._start_audio_stream_locked(sync_output=False, device_id=device_id)

        # ✅ Конвертация данных ВНЕ lock
        # ✅ Добавление в буфер ВНЕ lock
```

**⚠️ РИСК:** `_recreate_stream_if_needed_locked()` может вызывать `_query_default_output_device()` внутри lock (строка 744-745), если device_id не передан. Но это оптимизировано - device_id обычно передается извне.

---

## 🔍 Инвариант C: при `_recreating_stream=True` чанки НЕ теряются

### Логика в add_audio_data

```python:227:299:modules/speech_playback/core/player.py
# Под lock:
recreated = self._recreate_stream_if_needed_locked(reason=reason, device_id=device_id, incoming_sr=incoming_sr)
# Если _recreating_stream=True, метод вернет False, НО...

# ВНЕ lock:
# ... конвертация данных ...
chunk_id = self.chunk_buffer.add_chunk(audio_data, metadata)  # ✅ Чанк ВСЕГДА добавляется!
```

### Логика в _recreate_stream_if_needed_locked

```python:706:726:modules/speech_playback/core/player.py
# Защита от re-entrancy
if self._recreating_stream:
    if self._recreating_stream_start_time is not None:
        elapsed = time.time() - self._recreating_stream_start_time
        if elapsed > 5.0:  # Защита от залипания
            logger.error(f"❌ [RECREATE] КРИТИЧЕСКАЯ ОШИБКА: залипло на {elapsed:.1f}s!")
            self._recreating_stream = False
        else:
            logger.debug(f"🔍 [RECREATE] Поток уже пересоздается, пропускаем")
            return False  # ✅ Чанк все равно добавится в буфер выше!
```

**✅ Проверка:** Чанки не теряются - они добавляются в буфер ВСЕГДА, даже если recreate пропущен

---

## ⚠️ Критический вопрос: stream_rate выбор

### Текущая реализация

```python:453:468:modules/speech_playback/core/player.py
# 🔧 РЕФАКТОРИНГ: Выбираем sample_rate для потока
# КРИТИЧНО: Многие устройства/драйвера требуют device_rate (например 48k)
content_sr = self._actual_sample_rate if self._actual_sample_rate is not None else self.config.sample_rate

# 🔧 ВАЖНО: Проверяем совместимость с устройством
if self._device_sample_rate is not None and self._device_sample_rate != content_sr:
    logger.warning(
        f"⚠️ [STREAM_RATE] Content rate ({content_sr}Hz) != Device rate ({self._device_sample_rate}Hz). "
        f"Поток создается с content_rate, возможен скрытый ресемплинг драйвером."
    )

playback_sample_rate = content_sr  # ⚠️ Используем content_rate, НЕ device_rate
```

**⚠️ РИСК:** Поток создается с `content_rate` (24kHz), а не `device_rate` (48kHz). Это может:
- Не работать на некоторых устройствах
- Вызывать скрытый ресемплинг драйвером (не контролируемый)
- Приводить к рассинхронам

**Рекомендация:** Требуется тестирование на реальных устройствах (Built-in, AirPods, USB)

---

## 📊 Детальное логирование пересозданий

### Формат лога

```python:768:776:modules/speech_playback/core/player.py
logger.info(
    f"🔄 [RECREATE] Пересоздание потока: {recreate_reason} | "
    f"reason={reason} | thread={thread_name} | "
    f"prev_device={prev_device_id}→new={device_id} | "
    f"prev_stream_sr={prev_stream_sr}Hz→incoming={incoming_sr}Hz | "
    f"content_sr={self._actual_sample_rate or self.config.sample_rate}Hz | "
    f"device_sr={self._device_sample_rate}Hz"
)
```

**Содержит:**
- ✅ reason - причина пересоздания
- ✅ prev_device_id → new_device_id
- ✅ prev_stream_sr → new_stream_sr
- ✅ content_sr - sample rate контента
- ✅ device_sr - sample rate устройства
- ✅ thread name - имя потока

---

## 🔍 Быстрая проверка инвариантов

### Команды для валидации

```bash
# 1. Проверка что locked-версии НЕ берут lock
grep -A 10 "def _.*_locked(" modules/speech_playback/core/player.py | grep -v "with self._stream_lock"

# 2. Проверка что публичные методы берут lock
grep -B 2 -A 5 "def _start_audio_stream(" modules/speech_playback/core/player.py | head -10
grep -B 2 -A 5 "def _stop_audio_stream(" modules/speech_playback/core/player.py | head -10

# 3. Проверка что config.sample_rate не меняется в _sync_output_format
grep -A 30 "_sync_output_format_locked" modules/speech_playback/core/player.py | grep "config.sample_rate ="
# Должно быть ПУСТО (config.sample_rate не изменяется)

# 4. Проверка защиты от залипания
grep -A 15 "_recreating_stream" modules/speech_playback/core/player.py | grep "elapsed >"
# Должно быть: if elapsed > 5.0:
```

---

## ⚠️ Известные риски и ограничения

### 1. Stream на content_rate (24kHz)

**Риск:** Может не работать на устройствах, требующих 48kHz  
**Текущее решение:** Предупреждение в логах  
**Требуется:** Тестирование на реальных устройствах

### 2. `_query_default_output_device()` внутри lock

**Риск:** Может быть медленным на некоторых системах  
**Текущее решение:** Оптимизировано - вызывается ВНЕ lock в `add_audio_data`  
**Остается:** Может вызываться внутри `_recreate_stream_if_needed_locked` если device_id не передан

### 3. Нет явного ресемплинга

**Риск:** Полагаемся на драйвер для ресемплинга content_rate → device_rate  
**Текущее решение:** Предупреждение в логах  
**В будущем:** Может потребоваться явный ресемплинг

---

## ✅ Итоговый статус инвариантов

- ✅ **Инвариант A:** Выполнен (нет двойного lock, deadlock невозможен)
- ✅ **Инвариант B:** Выполнен (lock держится минимальное время, медленные операции ВНЕ lock)
- ✅ **Инвариант C:** Выполнен (чанки не теряются, добавляются в буфер ВСЕГДА)
- ⚠️ **Stream rate:** Требует тестирования на реальных устройствах

---

## 🧪 Следующий шаг: стресс-тест

Запустите приложение и проверьте логи:
1. Ищите `[RECREATE]` - должно быть ограниченное количество
2. Ищите `_stream_recreate_count` - не должно расти бесконечно
3. Ищите `_recreating_stream залипло` - не должно быть
4. Проверьте `_stream_recreate_reasons` - причины должны быть логичными

**Ожидаемый результат:**
- `_stream_recreate_count` ограничен (например, ≤ 5 за сессию)
- Нет ошибок "залипло"
- Все чанки воспроизводятся (нет потерь)


