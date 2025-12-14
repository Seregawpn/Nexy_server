# Поток распознавания речи с AVFoundation

## 📋 Обзор

Документ описывает правильный поток работы распознавания речи с использованием AVFoundation аудиосистемы.

---

## 🔄 Полный поток работы

### Этап 1: Активация записи (LONG_PRESS)

```
Пользователь зажимает Control+N
    ↓
QuartzKeyboardMonitor обнаруживает LONG_PRESS (≥0.6s)
    ↓
InputProcessingIntegration._handle_long_press()
    ↓
Публикует: voice.recording_start {session_id, source: "keyboard"}
    ↓
VoiceRecognitionIntegration._on_recording_start()
```

**Что происходит в `_on_recording_start()`:**

1. ✅ **Проверка блокировок:**
   - Проверяет `_first_run_in_progress` (блокировка во время запроса разрешений)
   - Если заблокировано → возврат без действий

2. ✅ **Установка сессии:**
   - `_set_session_id(session_id, "recording_start")` — синхронизация с state_manager
   - `_recording_active = True`
   - Отмена предыдущего распознавания: `_cancel_recognition()`

3. ✅ **Запуск записи через AVFoundation:**
   ```python
   # Очистка буфера
   self._audio_buffer = []
   self._audio_buffer_sample_rate = None
   self._audio_buffer_channels = None
   
   # Callback для получения аудио данных
   async def audio_callback(data: bytes, sample_rate: int, channels: int):
       # Сохраняем параметры формата (первый чанк)
       if self._audio_buffer_sample_rate is None:
           self._audio_buffer_sample_rate = sample_rate
           self._audio_buffer_channels = channels
       
       # Накопление аудио чанков
       self._audio_buffer.append(data)
   
   # Запуск записи
   success = await self._avf_engine.start_input(callback=audio_callback)
   ```

4. ✅ **Публикация событий:**
   - `microphone.opened` {session_id}
   - `voice.recognition_started` {session_id, language}

---

### Этап 2: Запись аудио (пока клавиша зажата)

```
AVFAudioEngine.start_input()
    ↓
AVAudioEngine.inputNode() → устанавливает tap
    ↓
AVAudioEngine.start() → запускает engine
    ↓
AVFoundation вызывает audio_callback() периодически
    ↓
audio_callback(data, sample_rate, channels)
    ↓
Данные накапливаются в self._audio_buffer[]
```

**Что происходит в `audio_callback()`:**

1. ✅ **Сохранение параметров формата** (только первый чанк):
   ```python
   if self._audio_buffer_sample_rate is None:
       self._audio_buffer_sample_rate = sample_rate  # Обычно 48000
       self._audio_buffer_channels = channels        # Обычно 1 (моно)
   ```

2. ✅ **Накопление аудио чанков:**
   ```python
   self._audio_buffer.append(data)  # data: bytes (PCM int16)
   ```

3. ✅ **Логирование** (DEBUG уровень):
   ```python
   total_bytes = sum(len(chunk) for chunk in self._audio_buffer)
   logger.debug(f"🔊 [AVF] Получен аудио чанк: {len(data)} bytes, "
                f"{sample_rate}Hz, {channels}ch (всего: {total_bytes} bytes)")
   ```

**Важно:**
- Аудио данные приходят в формате **PCM int16** (2 bytes per sample)
- Sample rate обычно **48000 Hz**
- Channels обычно **1** (моно)
- Чанки приходят примерно каждые **0.8 секунды** (38400 bytes при 48000Hz, 1ch)

---

### Этап 3: Остановка записи (RELEASE)

```
Пользователь отпускает Control+N
    ↓
QuartzKeyboardMonitor обнаруживает RELEASE
    ↓
InputProcessingIntegration._handle_key_release()
    ↓
Публикует: voice.recording_stop {session_id, duration}
    ↓
VoiceRecognitionIntegration._on_recording_stop()
```

**Что происходит в `_on_recording_stop()`:**

1. ✅ **Проверка сессии:**
   - Сравнение `active_session_id` с `request_session_id`
   - Если не совпадают → игнорирование (не наша сессия)

2. ✅ **Остановка записи через AVFoundation:**
   ```python
   if self._use_avf and self._avf_engine is not None:
       result = await self._avf_engine.stop_input()
       # result: AudioInputResult {frames_recorded, duration_ms, ...}
   ```

3. ✅ **Обработка накопленного аудио:**
   ```python
   if self._audio_buffer:
       # Объединение всех чанков
       total_audio = b''.join(self._audio_buffer)
       sample_rate = self._audio_buffer_sample_rate or 48000
       channels = self._audio_buffer_channels or 1
       
       # Отправка на распознавание
       await self._recognize_avf_audio(
           total_audio,
           sample_rate,
           channels,
           session_id
       )
   ```

4. ✅ **Очистка буфера:**
   ```python
   self._audio_buffer = []
   self._audio_buffer_sample_rate = None
   self._audio_buffer_channels = None
   ```

5. ✅ **Публикация событий:**
   - `microphone.closed` {session_id}

---

### Этап 4: Распознавание речи

```
VoiceRecognitionIntegration._recognize_avf_audio()
    ↓
Конвертация аудио данных
    ↓
Google Speech API распознавание
    ↓
Публикация результата
```

**Что происходит в `_recognize_avf_audio()`:**

1. ✅ **Проверка зависимостей:**
   ```python
   if not importlib.util.find_spec("speech_recognition"):
       # Ошибка: speech_recognition не доступен
       await self.event_bus.publish("voice.recognition_failed", {...})
       return
   ```

2. ✅ **Конвертация аудио данных:**
   ```python
   # bytes → numpy array (int16)
   audio_array_int16 = np.frombuffer(audio_data, dtype=np.int16)
   
   # int16 → float32, нормализация [-32768, 32767] → [-1.0, 1.0]
   audio_array_float32 = audio_array_int16.astype(np.float32) / 32767.0
   
   # Если многоканальное → усреднение до моно
   if channels > 1:
       frame_count = len(audio_array_float32) // channels
       audio_array_float32 = audio_array_float32[:frame_count * channels] \
           .reshape(frame_count, channels).mean(axis=1)
   
   # float32 → int16 для speech_recognition
   audio_bytes_int16 = (np.clip(audio_array_float32, -1.0, 1.0) * 32767.0) \
       .astype(np.int16).tobytes()
   ```

3. ✅ **Создание AudioData для speech_recognition:**
   ```python
   import speech_recognition as sr
   audio_data_obj = sr.AudioData(
       audio_bytes_int16,
       sample_rate,  # 48000
       2             # sample_width=2 (int16)
   )
   ```

4. ✅ **Распознавание через библиотеку SpeechRecognition:**
   ```python
   # Используем библиотеку speech_recognition (pip install SpeechRecognition)
   # Эта библиотека под капотом использует Google Speech API через recognize_google()
   
   # Используем recognizer из SpeechRecognizer (если доступен)
   if self._recognizer is not None and hasattr(self._recognizer, 'recognizer'):
       recognizer = self._recognizer.recognizer
       language = getattr(self._recognizer.config, 'language', 'en-US')
   else:
       # Создаём новый Recognizer из библиотеки SpeechRecognition
       recognizer = sr.Recognizer()
       language = 'en-US'
   
   # Распознавание через метод recognize_google() библиотеки SpeechRecognition
   # (который использует Google Speech API под капотом)
   text = recognizer.recognize_google(audio_data_obj, language=language)
   ```

5. ✅ **Публикация результата:**
   ```python
   # Успех
   await self.event_bus.publish("voice.recognition_completed", {
       "session_id": session_id,
       "text": text,
       "confidence": None,  # Google Speech API не всегда предоставляет
       "language": language,
       "source": "avf_recognition"
   })
   
   # Ошибка: речь не распознана
   except sr.UnknownValueError:
       await self.event_bus.publish("voice.recognition_failed", {
           "session_id": session_id,
           "error": "Speech not recognized",
           "source": "avf_recognition"
       })
   
   # Ошибка: проблема с сервисом
   except sr.RequestError as e:
       await self.event_bus.publish("voice.recognition_failed", {
           "session_id": session_id,
           "error": str(e),
           "source": "avf_recognition"
       })
   ```

---

## 📊 Диаграмма потока

```
┌─────────────────────────────────────────────────────────────────┐
│                    ПОТОК РАСПОЗНАВАНИЯ РЕЧИ                      │
└─────────────────────────────────────────────────────────────────┘

1. LONG_PRESS (Control+N зажат ≥0.6s)
   │
   ├─► InputProcessingIntegration._handle_long_press()
   │   └─► Публикует: voice.recording_start {session_id}
   │
   ├─► VoiceRecognitionIntegration._on_recording_start()
   │   ├─► Проверка блокировок (first_run)
   │   ├─► _set_session_id(session_id)
   │   ├─► Очистка буфера: _audio_buffer = []
   │   ├─► AVFAudioEngine.start_input(callback=audio_callback)
   │   └─► Публикует: microphone.opened, voice.recognition_started
   │
   └─► AVFAudioEngine
       ├─► AVAudioEngine.inputNode() → устанавливает tap
       ├─► AVAudioEngine.start() → запускает engine
       └─► AVFoundation вызывает audio_callback() периодически

2. ЗАПИСЬ АУДИО (пока клавиша зажата)
   │
   └─► audio_callback(data, sample_rate, channels)
       ├─► Сохранение параметров формата (первый чанк)
       ├─► Накопление: _audio_buffer.append(data)
       └─► Логирование (DEBUG)

3. RELEASE (Control+N отпущен)
   │
   ├─► InputProcessingIntegration._handle_key_release()
   │   └─► Публикует: voice.recording_stop {session_id, duration}
   │
   ├─► VoiceRecognitionIntegration._on_recording_stop()
   │   ├─► Проверка сессии (active_session_id == request_session_id)
   │   ├─► AVFAudioEngine.stop_input()
   │   ├─► Объединение буфера: total_audio = b''.join(_audio_buffer)
   │   ├─► _recognize_avf_audio(total_audio, sample_rate, channels, session_id)
   │   ├─► Очистка буфера
   │   └─► Публикует: microphone.closed

4. РАСПОЗНАВАНИЕ
   │
   └─► _recognize_avf_audio()
       ├─► Конвертация: bytes → numpy → float32 → int16
       ├─► Создание: sr.AudioData(audio_bytes_int16, sample_rate, 2)
       ├─► Распознавание: recognizer.recognize_google(audio_data_obj, language)
       └─► Публикует: voice.recognition_completed {text} или voice.recognition_failed {error}

5. ОБРАБОТКА РЕЗУЛЬТАТА
   │
   └─► Подписчики на voice.recognition_completed:
       ├─► GrpcClientIntegration → отправка на сервер
       ├─► ProcessingWorkflow → переход в режим PROCESSING
       └─► Другие интеграции
```

---

## 🔍 Ключевые моменты

### 1. Накопление аудио

**Важно:** Аудио накапливается в буфере **во время записи**, а не после остановки.

```python
# ✅ ПРАВИЛЬНО: Накопление во время записи
async def audio_callback(data: bytes, sample_rate: int, channels: int):
    self._audio_buffer.append(data)  # Накопление

# ❌ НЕПРАВИЛЬНО: Попытка получить данные после остановки
result = await self._avf_engine.stop_input()
# result.data может быть None или пустым!
```

### 2. Формат аудио данных

- **Входной формат:** PCM int16 (2 bytes per sample)
- **Sample rate:** 48000 Hz (по умолчанию)
- **Channels:** 1 (моно)
- **Размер чанка:** ~38400 bytes (0.8 секунды при 48000Hz, 1ch)

### 3. Конвертация для распознавания

```python
# Шаг 1: bytes → numpy int16
audio_array_int16 = np.frombuffer(audio_data, dtype=np.int16)

# Шаг 2: int16 → float32, нормализация
audio_array_float32 = audio_array_int16.astype(np.float32) / 32767.0

# Шаг 3: Многоканальное → моно (если нужно)
if channels > 1:
    audio_array_float32 = ... # усреднение

# Шаг 4: float32 → int16 для speech_recognition
audio_bytes_int16 = (np.clip(audio_array_float32, -1.0, 1.0) * 32767.0) \
    .astype(np.int16).tobytes()
```

### 4. Обработка ошибок

**Три типа ошибок:**

1. **`sr.UnknownValueError`** — речь не распознана (тишина, шум)
   - Публикуется: `voice.recognition_failed` {error: "Speech not recognized"}

2. **`sr.RequestError`** — проблема с сервисом распознавания через SpeechRecognition (сеть, квота Google Speech API)
   - Публикуется: `voice.recognition_failed` {error: str(e)}

3. **`Exception`** — другие ошибки (конвертация, формат)
   - Публикуется: `voice.recognition_failed` {error: str(e)}

---

## ✅ Чек-лист правильной работы

### При LONG_PRESS:
- [ ] `voice.recording_start` опубликовано с правильным `session_id`
- [ ] `_audio_buffer` очищен
- [ ] `AVFAudioEngine.start_input()` вызван с `audio_callback`
- [ ] `microphone.opened` опубликовано
- [ ] `voice.recognition_started` опубликовано

### Во время записи:
- [ ] `audio_callback()` вызывается периодически
- [ ] Аудио чанки накапливаются в `_audio_buffer`
- [ ] Параметры формата сохранены (`_audio_buffer_sample_rate`, `_audio_buffer_channels`)
- [ ] Логи показывают: `🔊 [AVF] Получен аудио чанк: ...`

### При RELEASE:
- [ ] `voice.recording_stop` опубликовано с правильным `session_id`
- [ ] `AVFAudioEngine.stop_input()` вызван
- [ ] `_audio_buffer` не пустой
- [ ] `_recognize_avf_audio()` вызван с правильными параметрами
- [ ] `microphone.closed` опубликовано

### При распознавании:
- [ ] Аудио данные конвертированы правильно
- [ ] `sr.AudioData` создан с правильными параметрами
- [ ] `recognize_google()` вызван
- [ ] Результат опубликован: `voice.recognition_completed` или `voice.recognition_failed`

---

## 🐛 Типичные проблемы

### Проблема 1: Буфер пустой при остановке

**Причина:** `audio_callback` не вызывается или данные не накапливаются.

**Решение:**
- Проверить, что `AVFAudioEngine.start_input()` успешно вызван
- Проверить логи на наличие `🔊 [AVF] Получен аудио чанк`
- Проверить разрешения микрофона

### Проблема 2: Распознавание не работает

**Причина:** Ошибка в конвертации или Google Speech API недоступен.

**Решение:**
- Проверить логи на наличие ошибок в `_recognize_avf_audio()`
- Проверить доступность библиотеки `speech_recognition` (pip install SpeechRecognition)
- Проверить интернет-соединение (SpeechRecognition использует Google Speech API, который требует сеть)

### Проблема 3: Неправильный формат аудио

**Причина:** Неправильная конвертация или параметры формата.

**Решение:**
- Проверить `_audio_buffer_sample_rate` и `_audio_buffer_channels`
- Проверить конвертацию: int16 → float32 → int16
- Проверить создание `sr.AudioData` с правильным `sample_width=2`

---

## 📝 Логи для диагностики

### Успешный поток:

```
✅ [AVF] Микрофон открыт через AVFAudioEngine для session 123.456
🔊 [AVF] Получен аудио чанк: 38400 bytes, 48000Hz, 1ch (всего: 38400 bytes)
🔊 [AVF] Получен аудио чанк: 38400 bytes, 48000Hz, 1ch (всего: 76800 bytes)
...
✅ [AVF] Запись остановлена через AVFAudioEngine: 422400 frames, 2437.2ms
🔊 [AVF] Накоплено 844800 bytes аудио для распознавания
📤 [AVF] Отправляем на распознавание: 844800 bytes, 48000Hz, 1ch
🎤 [AVF] Начинаем распознавание: 844800 bytes, 48000Hz
✅ [AVF] Распознавание успешно: 'Hello, how are you?' (session=123.456)
# Используется библиотека SpeechRecognition (recognize_google → Google Speech API)
```

### Ошибка распознавания:

```
⚠️ [AVF] SpeechRecognition не распознал аудио (session=123.456)
# или
❌ [AVF] Ошибка сервиса распознавания (session=123.456): [детали ошибки]
# (SpeechRecognition → Google Speech API)
```

---

**Последнее обновление:** 2025-12-09
**Версия:** 1.0



