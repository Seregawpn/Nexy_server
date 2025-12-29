# Ответы на вопросы по реализации AVFoundation архитектуры

## Анализ текущей архитектуры Nexy

### 1. Язык/платформа: **1-A** ✅
- **Python + PyObjC** для работы с AVFoundation
- Текущая система использует `sounddevice` (PortAudio), но есть готовность к PyObjC
- В `modules/permissions/first_run/status_checker.py` уже используется `AVFoundation` через PyObjC

### 2. Многопоточность: **2-A** ✅
- **threading + Lock/Event** - используется повсеместно
- Примеры:
  - `modules/voice_recognition/core/speech_recognizer.py`: `threading.Thread`, `threading.Event`, `threading.Lock`, `threading.RLock`
  - `modules/voice_recognition/core/audio_device_monitor.py`: отдельный поток для мониторинга
- Предсказуемый вариант для macOS ✅

### 3. EventBus: **3-B (адаптированный)** ⚠️
- **Есть встроенный EventBus** (`integration/core/event_bus.py`)
- Но он **async/await** с приоритетами, не простой синхронный
- **Рекомендация**: Использовать существующий EventBus, но добавить синхронные методы для AVFoundation адаптеров
- Или создать простой синхронный EventBus для AVFoundation мониторинга (threading-safe)

### 4. Google Speech Recognizer: **4-B (адаптированный)** ⚠️
- **Текущая реализация**: `start_listening()` запускает поток `_run_listening()` с `sounddevice.InputStream`
- **НЕ использует** `recognizer.listen()` напрямую
- **Рекомендация**: Адаптировать под `recognizer.listen()` в цикле с таймаутами для heartbeat
- Или оставить текущий подход с `sounddevice.InputStream`, но добавить heartbeat механизм

### 5. Этапность: **5-C** ✅
- **Поэтапно** (core → защиты)
- В текущем коде уже есть:
  - Debounce (в `speech_recognizer.py`: `_last_stop_time`, `_min_stop_start_interval`)
  - Retry (в `audio_recovery_manager.py`: пороги восстановления)
  - Rollback (в `speech_recognizer.py`: fallback на предыдущее устройство)
- **Рекомендация**: Включить debounce/retry/rollback в каркас сразу (как предложено)

---

## Итоговые ответы

```
1-A, 2-A, 3-B (адаптированный), 4-B (адаптированный), 5-C
```

### Детализация:

**1-A**: Python + PyObjC (AVFoundation) ✅
- Готово к использованию
- PyObjC уже используется для проверки разрешений

**2-A**: threading + Lock/Event ✅
- Полностью соответствует текущей архитектуре
- Используется повсеместно

**3-B**: Встроенный EventBus (но адаптированный) ⚠️
- Есть async EventBus с приоритетами
- Нужно добавить синхронные методы или создать простой синхронный для AVFoundation адаптеров
- **Рекомендация**: Использовать существующий EventBus через `asyncio.run_coroutine_threadsafe()` из AVFoundation потоков

**4-B**: Адаптированный подход ⚠️
- Текущая реализация: поток с `sounddevice.InputStream`
- Можно адаптировать под `recognizer.listen()` в цикле с таймаутами
- Или оставить текущий подход, но добавить heartbeat механизм
- **Рекомендация**: Оставить текущий подход (`sounddevice.InputStream`), но добавить heartbeat через callback

**5-C**: Поэтапно с защитами ✅
- Уже есть debounce/retry/rollback в коде
- Включить в каркас сразу (как предложено)

---

## Адаптация каркаса под Nexy

### Изменения в каркасе:

1. **EventBus**: Использовать существующий async EventBus через `asyncio.run_coroutine_threadsafe()`
   ```python
   # В AVFoundation адаптерах (threading контекст)
   loop = asyncio.get_event_loop()
   asyncio.run_coroutine_threadsafe(
       event_bus.publish("audio.route.snapshot", snap),
       loop
   )
   ```

2. **Google Input Controller**: Адаптировать под текущий `SpeechRecognizer`
   ```python
   class GoogleInputController:
       def __init__(self, recognizer: SpeechRecognizer):
           self._recognizer = recognizer
       
       def is_running(self) -> bool:
           return self._recognizer.is_listening
       
       async def start(self, device_index: Optional[int]) -> None:
           # Установить device_index в recognizer
           self._recognizer.input_device_id = device_index
           await self._recognizer.start_listening()
       
       async def stop(self) -> None:
           await self._recognizer.stop_listening()
       
       def last_heartbeat_ts(self) -> float:
           # Использовать время последнего audio callback
           return self._recognizer.listen_start_time or 0.0
   ```

3. **AVF Snapshot Provider**: Реализовать через PyObjC
   ```python
   def avf_snapshot_provider() -> dict:
       import AVFoundation
       # Получение устройств через AVFoundation
       # Возврат нормализованного словаря
   ```

4. **PortAudio Device Provider**: Использовать существующий `sounddevice`
   ```python
   def portaudio_device_provider() -> list:
       import sounddevice as sd
       devices = sd.query_devices()
       # Нормализация в нужный формат
       return [{"index": i, "name": d["name"], ...} for i, d in enumerate(devices)]
   ```

---

## Структура модулей для Nexy

```
modules/voice_recognition/
├── core/
│   ├── speech_recognizer.py          # Текущий (адаптировать)
│   ├── avfoundation/
│   │   ├── __init__.py
│   │   ├── audio_contracts.py        # Контракты данных
│   │   ├── mapping.py                # Маппинг AVF → PortAudio
│   │   ├── state_machines.py         # Input/Output SM
│   │   ├── route_manager.py          # RouteManager + reconcile
│   │   └── adapters/
│   │       ├── avf_monitor.py        # NSNotification + polling
│   │       ├── avf_output.py         # AVAudioEngine wrapper
│   │       └── google_input.py       # Google SR controller adapter
│   └── ...
```

---

## Следующие шаги

1. ✅ Ответы на вопросы готовы
2. ⏭️ Адаптировать каркас под существующий EventBus (async)
3. ⏭️ Реализовать AVFoundation адаптеры через PyObjC
4. ⏭️ Интегрировать RouteManager в существующую архитектуру
5. ⏭️ Тестирование на реальных устройствах

