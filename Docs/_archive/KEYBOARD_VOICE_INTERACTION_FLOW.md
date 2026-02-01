# Схема взаимодействия клавиатуры и голосового управления

## Дата создания
2025-11-30

## Полный поток взаимодействия

### Фаза 1: PRESS (Нажатие клавиши)

```
[KeyboardMonitor] 
  ↓ keyDown(ctrl_n)
[InputProcessingIntegration._handle_press]
  ├─ Создает pending_session_id = event.timestamp
  ├─ Переход: IDLE → PENDING
  └─ Публикует: keyboard.press
```

**Состояния:**
- `_pending_session_id` = timestamp
- `_recording_started` = False
- `_input_state` = PENDING
- `AppMode` = SLEEPING (или текущий)

---

### Фаза 2: LONG_PRESS (Длительное нажатие > 0.6s)

```
[KeyboardMonitor] 
  ↓ LONG_PRESS triggered (duration > 0.6s)
[InputProcessingIntegration._handle_long_press]
  ├─ Проверки:
  │   ├─ _long_press_in_progress? → игнорируем
  │   ├─ _input_state == PENDING? → проверяем
  │   ├─ keyboard_monitor.key_pressed? → проверяем
  │   ├─ state_manager.is_microphone_active()? → игнорируем если True
  │   └─ _recording_started? → игнорируем если True
  │
  ├─ Ожидания:
  │   ├─ _ensure_playback_idle() (таймаут 0.5s)
  │   └─ _wait_for_mic_closed() (таймаут 0.3s)
  │
  ├─ Сброс состояния:
  │   ├─ _reset_session("long_press_start")
  │   ├─ _set_session_id(new_session_id, "long_press_start")
  │   └─ _pending_session_id = None
  │
  └─ Публикует: voice.recording_start
      ├─ session_id = active_session_id
      └─ _recording_started = True
```

**Подписчики на `voice.recording_start`:**
1. `VoiceRecognitionIntegration._on_recording_start`
2. `ListeningWorkflow._on_recording_start`
3. `ScreenshotCaptureIntegration` (подготовка)

**Состояния после LONG_PRESS:**
- `_recording_started` = True
- `_input_state` = LISTENING
- `AppMode` = LISTENING (запрашивается через mode.request)

---

### Фаза 3: voice.recording_start → Открытие микрофона

```
[VoiceRecognitionIntegration._on_recording_start]
  ├─ _set_session_id(session_id, "recording_start")
  ├─ _recording_active = True
  │
  ├─ MicrophoneStateManager.request_open(session_id)
  │   ├─ Переход: IDLE → OPENING
  │   ├─ Публикует: microphone.open_requested
  │   └─ Ждет: microphone.opened (таймаут 5s)
  │
  └─ SpeechRecognizer.start_listening()
      ├─ Создает аудио поток
      ├─ Публикует: microphone.opened
      └─ Публикует: voice.recognition_started
```

**Подписчики на `microphone.opened`:**
1. `MicrophoneStateManager._on_microphone_opened`
   - Переход: OPENING → ACTIVE
   - Устанавливает `_opened_event.set()`
   - Публикует: `voice.mic_opened`

**Состояния после открытия микрофона:**
- `MicrophoneStateManager._state` = ACTIVE
- `state_manager.is_microphone_active()` = True
- `SpeechRecognizer.is_listening` = True
- `_current_stream.active` = True

---

### Фаза 4: Запись аудио (пока клавиша нажата)

```
[SpeechRecognizer._audio_callback]
  ├─ Получает аудио чанки
  ├─ Обрабатывает (нормализация, VAD)
  └─ Сохраняет в буфер для распознавания
```

**Состояния во время записи:**
- `AppMode` = LISTENING
- Микрофон активен
- Аудио записывается

---

### Фаза 5: RELEASE (Отпускание клавиши)

```
[KeyboardMonitor] 
  ↓ keyUp(ctrl_n)
[InputProcessingIntegration._handle_key_release]
  ├─ Проверки:
  │   ├─ was_recording = _recording_started OR state_manager.is_microphone_active()
  │   └─ active_session_id = _get_active_session_id()
  │
  ├─ Если should_stop_recording:
  │   └─ Публикует: voice.recording_stop
  │       ├─ session_id = active_session_id
  │       └─ _recording_started = False (СРАЗУ после публикации!)
  │
  └─ Если was_recording:
      └─ Публикует: mode.request(PROCESSING)
```

**Подписчики на `voice.recording_stop`:**
1. `VoiceRecognitionIntegration._on_recording_stop` ⚠️ **КРИТИЧНО**
2. `ScreenshotCaptureIntegration._on_voice_recording_stop`
3. `ListeningWorkflow._on_recording_stop`

**Состояния после RELEASE:**
- `_recording_started` = False
- `AppMode` = PROCESSING (запрашивается)
- Микрофон еще активен (пока не закрыт)

---

### Фаза 6: voice.recording_stop → Закрытие микрофона и распознавание

```
[VoiceRecognitionIntegration._on_recording_stop]
  ├─ Проверка session_id:
  │   ├─ active_session_id = _get_active_session_id()
  │   └─ Сравнение: active_session_id == request_session_id
  │
  ├─ Проверка физического состояния потока:
  │   ├─ Если _current_stream.active == True:
  │   │   ├─ _current_stream.stop() ⚠️ **КРИТИЧНО: ОСТАНОВКА ПОТОКА**
  │   │   └─ Публикует: microphone.closed ⚠️ **РАЗРЫВ DEADLOCK**
  │   │
  ├─ MicrophoneStateManager.request_close(session_id)
  │   ├─ Переход: ACTIVE → CLOSING
  │   ├─ Создает: _closed_event = asyncio.Event()
  │   ├─ Публикует: microphone.close_requested
  │   └─ Ждет: microphone.closed (таймаут 0.5s если поток уже остановлен)
  │       └─ Если получил microphone.closed → _closed_event.set()
  │
  ├─ SpeechRecognizer.stop_listening()
  │   ├─ Останавливает поток (если еще не остановлен)
  │   ├─ Запускает распознавание (Vosk/Whisper)
  │   └─ Возвращает: RecognitionResult
  │
  └─ Публикует результат:
      ├─ Если result.text:
      │   └─ voice.recognition_completed
      │       ├─ session_id
      │       ├─ text
      │       └─ confidence
      └─ Если result.error или нет text:
          └─ voice.recognition_failed
              ├─ session_id
              └─ error
```

**Подписчики на `voice.recognition_completed`:**
1. `InputProcessingIntegration._on_recognition_completed`
2. `GrpcClientIntegration` (отправка на сервер)
3. `ProcessingWorkflow` (координация)

**Подписчики на `voice.recognition_failed`:**
1. `InputProcessingIntegration._on_recognition_failed`
   - Публикует: `mode.request(SLEEPING)`

---

### Фаза 7: voice.recognition_completed → Обработка

```
[GrpcClientIntegration]
  ├─ Получает: voice.recognition_completed
  ├─ Отправляет на сервер: text + screenshot
  └─ Публикует: grpc.request_completed
      └─ audio_data (ответ сервера)

[SpeechPlaybackIntegration]
  ├─ Получает: playback.raw_audio
  ├─ Воспроизводит аудио
  └─ Публикует: playback.completed

[ModeManagementIntegration]
  ├─ Получает: playback.completed
  └─ Публикует: mode.request(SLEEPING)
```

---

## Узкие места и проблемы

### 🔴 Проблема 1: Deadlock в request_close

**Описание:**
- `request_close()` ждет `microphone.closed` через `_closed_event.wait()`
- `microphone.closed` публикуется только ПОСЛЕ `stop_listening()`
- Но `stop_listening()` вызывается только ПОСЛЕ `request_close()` завершится

**Решение:**
- ✅ Публикуем `microphone.closed` СРАЗУ после остановки потока (до `request_close`)
- ✅ Добавлен таймаут для `request_close` (0.5s если поток уже остановлен)

**Статус:** Исправлено

---

### 🔴 Проблема 2: Рассинхронизация состояний микрофона

**Описание:**
- `_recording_started` в `InputProcessingIntegration` - локальный флаг
- `_recording_active` в `VoiceRecognitionIntegration` - локальный флаг
- `state_manager.is_microphone_active()` - централизованное состояние
- `_current_stream.active` - физическое состояние потока

Эти 4 источника истины могут быть рассинхронизированы.

**Пример проблемы:**
- `_recording_started` = False (сброшен в RELEASE)
- `state_manager.is_microphone_active()` = False (не обновлен)
- Но `_current_stream.active` = True (поток физически активен)

**Решение:**
- ✅ Проверка физического состояния потока перед `request_close`
- ✅ Принудительная остановка потока при обнаружении активности

**Статус:** Частично исправлено (нужна полная синхронизация)

---

### 🔴 Проблема 3: `_recording_started` сбрасывается слишком рано

**Описание:**
- В `RELEASE` (строка 1419): `_recording_started = False` устанавливается СРАЗУ после публикации `voice.recording_stop`
- Но микрофон еще активен и запись еще идет
- Это может привести к race condition при быстром повторном нажатии

**Решение:**
- ⚠️ Нужно сбрасывать `_recording_started` только после подтверждения закрытия микрофона

**Статус:** Требует исправления

---

### 🔴 Проблема 4: `stop_listening()` не вызывается при deadlock

**Описание:**
- Если `request_close()` застревает (deadlock), код не доходит до `stop_listening()`
- Распознавание не запускается
- Речь не отправляется на сервер

**Решение:**
- ✅ Добавлен таймаут для `request_close`
- ✅ Публикация `microphone.closed` до `request_close` разрывает deadlock

**Статус:** Исправлено

---

### 🟡 Проблема 5: Множественные проверки состояния

**Описание:**
- В `LONG_PRESS` много проверок состояния (строки 1156-1196)
- В `RELEASE` проверки `was_recording` через несколько источников
- Это может привести к race conditions

**Решение:**
- ⚠️ Нужна единая точка проверки состояния микрофона

**Статус:** Требует рефакторинга

---

### 🟡 Проблема 6: Session ID рассинхронизация

**Описание:**
- `session_id` хранится в нескольких местах:
  - `InputProcessingIntegration._pending_session_id`
  - `InputProcessingIntegration._active_grpc_session_id`
  - `VoiceRecognitionIntegration._active_session_id`
  - `state_manager.get_current_session_id()`
- Конвертация между float и str может привести к mismatch

**Решение:**
- ✅ Используется `state_manager` как единый источник истины
- ✅ Конвертация в строки для сравнения

**Статус:** Частично исправлено

---

## План исправлений

**📋 Детальный план исправлений:** См. `Docs/VOICE_INTERACTION_FIX_PLAN.md`

---

## Рекомендации по исправлению

### Приоритет 1: Критические исправления

1. **Синхронизация `_recording_started`**
   - Сбрасывать `_recording_started` только после подтверждения закрытия микрофона
   - Использовать `microphone.closed` как триггер для сброса

2. **Единая точка проверки состояния микрофона**
   - Создать функцию `is_microphone_actually_active()` которая проверяет:
     - `state_manager.is_microphone_active()`
     - `_current_stream.active` (физическое состояние)
   - Использовать эту функцию везде вместо множественных проверок

### Приоритет 2: Улучшения

3. **Упрощение логики LONG_PRESS**
   - Убрать дублирующие проверки
   - Использовать единую функцию проверки состояния

4. **Улучшение обработки ошибок**
   - Добавить fallback для всех критических операций
   - Логировать все изменения состояния

### Приоритет 3: Рефакторинг

5. **Единый источник истины для session_id**
   - Удалить локальные переменные `_pending_session_id`, `_active_grpc_session_id`
   - Использовать только `state_manager.get_current_session_id()`

6. **Упрощение состояния микрофона**
   - Удалить `_recording_started` и `_recording_active`
   - Использовать только `state_manager.is_microphone_active()`

---

## Схема потока (упрощенная)

```
PRESS
  ↓
PENDING (pending_session_id создан)
  ↓
LONG_PRESS (> 0.6s)
  ↓
voice.recording_start
  ↓
MicrophoneStateManager.request_open
  ↓
SpeechRecognizer.start_listening
  ↓
microphone.opened
  ↓
LISTENING (запись идет)
  ↓
RELEASE
  ↓
voice.recording_stop
  ↓
[ПРОБЛЕМА: request_close ждет microphone.closed]
  ↓
stop_listening() ← НЕ ВЫЗЫВАЕТСЯ ПРИ DEADLOCK
  ↓
voice.recognition_completed/failed
  ↓
PROCESSING
  ↓
SLEEPING
```

---

## Исправленная схема потока

```
PRESS
  ↓
PENDING
  ↓
LONG_PRESS
  ↓
voice.recording_start
  ↓
LISTENING (запись идет)
  ↓
RELEASE
  ↓
voice.recording_stop
  ↓
[ИСПРАВЛЕНО: Проверка физического состояния потока]
  ├─ Если поток активен:
  │   ├─ _current_stream.stop()
  │   └─ microphone.closed (публикуется СРАЗУ)
  ↓
request_close (таймаут 0.5s)
  ├─ Получает microphone.closed → завершается быстро
  ↓
stop_listening() ← ВЫЗЫВАЕТСЯ
  ↓
voice.recognition_completed/failed
  ↓
PROCESSING
  ↓
SLEEPING
```

