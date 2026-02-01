# Идеальная диаграмма системы аудио

## Дата создания
2025-01-XX

## Обзор

Эта диаграмма показывает **идеальное** состояние системы активации микрофона с учетом всех флагов, состояний и правильного взаимодействия между компонентами.

---

## Полная схема состояний и флагов

### 1. Состояния системы

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           СОСТОЯНИЯ СИСТЕМЫ                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                               │
│  AppMode (state_manager):                                                    │
│    ├─ SLEEPING    - Спящий режим, нет активных операций                     │
│    ├─ LISTENING   - Прослушивание, микрофон активен                         │
│    └─ PROCESSING  - Обработка команды, воспроизведение ответа               │
│                                                                               │
│  InputState (input_processing_integration):                                  │
│    ├─ IDLE        - Нет активных операций                                   │
│    ├─ PENDING     - PRESS получен, ожидание LONG_PRESS                      │
│    ├─ LISTENING   - LONG_PRESS получен, запись активна                       │
│    └─ PROCESSING  - RELEASE получен, обработка gRPC                         │
│                                                                               │
│  MicrophoneState (state_manager):                                           │
│    ├─ idle        - Микрофон закрыт                                          │
│    ├─ opening     - Микрофон открывается                                    │
│    ├─ active      - Микрофон активен, запись идет                            │
│    ├─ closing     - Микрофон закрывается                                    │
│    └─ error       - Ошибка, требуется восстановление                        │
│                                                                               │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2. Флаги системы

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           ФЛАГИ СИСТЕМЫ                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                               │
│  InputProcessingIntegration:                                                 │
│    ├─ _recording_started: bool          - Начата ли запись                  │
│    ├─ _playback_active: bool            - Активно ли воспроизведение        │
│    ├─ _pending_session_id: Optional     - Подготовленная сессия             │
│    ├─ _active_grpc_session_id: Optional  - Активная gRPC сессия              │
│    ├─ _long_press_in_progress: bool      - Обрабатывается LONG_PRESS         │
│    ├─ _session_recognized: bool          - Распознана ли сессия               │
│    └─ _last_playback_start_ts: float     - Время последнего playback.started │
│                                                                               │
│  VoiceRecognitionIntegration:                                                │
│    ├─ _recording_active: bool            - Активна ли запись                 │
│    ├─ _google_recording_active: bool     - Активна ли Google запись          │
│    ├─ _google_stop_listening: Optional   - Функция остановки записи           │
│    ├─ _user_initiated_recording: bool    - Активация пользователем           │
│    ├─ _first_run_in_progress: bool       - First run в процессе              │
│    └─ _last_recording_stop_time: float   - Время последней остановки         │
│                                                                               │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Идеальный поток активации микрофона

### Этап 1: Начальное состояние (SLEEPING)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    СОСТОЯНИЕ: SLEEPING (ИДЕАЛЬНОЕ)                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                               │
│  AppMode:                    SLEEPING                                        │
│  InputState:                  IDLE                                            │
│  MicrophoneState:             idle                                            │
│                                                                               │
│  Флаги InputProcessingIntegration:                                            │
│    _recording_started:        False                                           │
│    _playback_active:          False                                           │
│    _pending_session_id:       None                                            │
│    _active_grpc_session_id:   None                                            │
│    _long_press_in_progress:   False                                           │
│    _session_recognized:       False                                           │
│    _last_playback_start_ts:   0.0                                             │
│                                                                               │
│  Флаги VoiceRecognitionIntegration:                                           │
│    _recording_active:         False                                           │
│    _google_recording_active:  False                                           │
│    _google_stop_listening:    None                                            │
│    _user_initiated_recording: False                                           │
│    _first_run_in_progress:    False                                           │
│                                                                               │
│  ✅ ВСЕ ФЛАГИ В ПРАВИЛЬНОМ СОСТОЯНИИ                                          │
│  ✅ МИКРОФОН ГАРАНТИРОВАННО ЗАКРЫТ                                            │
│                                                                               │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Этап 2: Пользователь нажимает Ctrl+N (PRESS)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    СОБЫТИЕ: PRESS (ИДЕАЛЬНОЕ)                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                               │
│  InputProcessingIntegration._handle_press()                                   │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │ 1. Проверки блокировки:                                              │  │
│  │    ├─ _playback_active == False? ✓                                   │  │
│  │    ├─ playback grace period прошёл? ✓                                 │  │
│  │    └─ mic_active == False? ✓                                         │  │
│  │                                                                       │  │
│  │ 2. Создание сессии:                                                   │  │
│  │    ├─ _pending_session_id = event.timestamp                          │  │
│  │    ├─ _recording_started = False                                      │  │
│  │    └─ _session_recognized = False                                     │  │
│  │                                                                       │  │
│  │ 3. Переход состояния:                                                 │  │
│  │    └─ _input_state = PENDING                                          │  │
│  │                                                                       │  │
│  │ 4. Публикация события:                                                │  │
│  │    └─ keyboard.press {session_id, source="keyboard"}                 │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
│                                                                               │
│  ✅ СОСТОЯНИЕ: InputState = PENDING                                           │
│  ✅ ФЛАГИ: _pending_session_id установлен, _recording_started = False        │
│                                                                               │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Этап 3: Пользователь удерживает Ctrl+N (LONG_PRESS)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                  СОБЫТИЕ: LONG_PRESS (ИДЕАЛЬНОЕ)                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                               │
│  InputProcessingIntegration._handle_long_press()                            │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │ 1. Проверка: _can_start_recording()                                   │  │
│  │    ├─ _input_state == PENDING? ✓                                     │  │
│  │    ├─ _pending_session_id != None? ✓                                 │  │
│  │    ├─ _playback_active == False? ✓                                   │  │
│  │    └─ playback grace period прошёл? ✓                                 │  │
│  │                                                                       │  │
│  │ 2. Проверка микрофона:                                                │  │
│  │    ├─ mic_active = state_manager.is_microphone_active()               │  │
│  │    └─ Если mic_active == True:                                        │  │
│  │       ├─ Публикация: voice.recording_stop {session_id=None}          │  │
│  │       └─ Ожидание: _wait_for_mic_closed_with_timeout(1.0s)          │  │
│  │                                                                       │  │
│  │ 3. Установка флагов:                                                   │  │
│  │    ├─ _long_press_in_progress = True                                  │  │
│  │    ├─ _recording_started = True                                       │  │
│  │    └─ _recording_start_time = time.time()                             │  │
│  │                                                                       │  │
│  │ 4. Публикация событий:                                                │  │
│  │    ├─ voice.recording_start {session_id, source="keyboard"}          │  │
│  │    └─ mode.request {target=LISTENING, source="keyboard"}              │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
│                                                                               │
│  ✅ СОСТОЯНИЕ: InputState = LISTENING                                         │
│  ✅ ФЛАГИ: _recording_started = True, _long_press_in_progress = True         │
│                                                                               │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Этап 4: VoiceRecognitionIntegration получает voice.recording_start

```
┌─────────────────────────────────────────────────────────────────────────────┐
│            VoiceRecognitionIntegration._on_recording_start()                 │
│                          (ИДЕАЛЬНОЕ)                                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                               │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │ 1. Проверки блокировки:                                              │  │
│  │    ├─ PROCESSING + source != "keyboard" → блокировка ❌               │  │
│  │    ├─ _first_run_in_progress → блокировка ❌                          │  │
│  │    └─ cooldown не прошёл → блокировка ❌                               │  │
│  │                                                                       │  │
│  │ 2. Установка флагов:                                                   │  │
│  │    ├─ _recording_active = True                                        │  │
│  │    ├─ _set_session_id(session_id)                                     │  │
│  │    └─ _user_initiated_recording = (source == "keyboard")              │  │
│  │                                                                       │  │
│  │ 3. AVF диагностика (если _use_avf == True):                          │  │
│  │    ├─ AVFAudioEngine.start_input()                                    │  │
│  │    ├─ await asyncio.sleep(1.0)  # Запись диагностики                  │  │
│  │    ├─ AVFAudioEngine.stop_input()  # ✅ ДЕАКТИВАЦИЯ                  │  │
│  │    ├─ await asyncio.sleep(0.2)  # Пауза для деактивации              │  │
│  │    └─ Проверка: AVF полностью деактивирован (5 попыток)                │  │
│  │                                                                       │  │
│  │ 4. Проверка разрешений:                                               │  │
│  │    ├─ PermissionChecker.check_microphone_permission()                │  │
│  │    └─ Если != "granted" → RuntimeError                                │  │
│  │                                                                       │  │
│  │ 5. Google Speech Recognition активация:                               │  │
│  │    ├─ Создание recognizer и microphone                                │  │
│  │    ├─ adjust_for_ambient_noise()                                      │  │
│  │    ├─ _google_recording_active = True  # ✅ ПЕРЕД listen_in_background│  │
│  │    ├─ _google_stop_listening = listen_in_background(microphone, callback)│
│  │    └─ Проверка: _google_stop_listening != None                        │  │
│  │                                                                       │  │
│  │ 6. Обновление состояния:                                               │  │
│  │    ├─ state_manager.set_microphone_state("active", session_id)        │  │
│  │    └─ Публикация: microphone.opened {session_id}                      │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
│                                                                               │
│  ✅ СОСТОЯНИЕ: MicrophoneState = active                                       │
│  ✅ ФЛАГИ: _google_recording_active = True, _recording_active = True          │
│  ✅ AVF ГАРАНТИРОВАННО ДЕАКТИВИРОВАН                                          │
│                                                                               │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Этап 5: Callback от listen_in_background получает аудио

```
┌─────────────────────────────────────────────────────────────────────────────┐
│              Callback от listen_in_background (ИДЕАЛЬНОЕ)                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                               │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │ 1. Проверки:                                                         │  │
│  │    ├─ _google_recording_active == True? ✓                           │  │
│  │    ├─ _google_stop_listening != None? ✓                             │  │
│  │    └─ state_manager.is_microphone_active() == True? ✓               │  │
│  │                                                                       │  │
│  │ 2. Проверка воспроизведения:                                          │  │
│  │    ├─ playback_active = state_manager._playback_active             │  │
│  │    ├─ user_initiated = _user_initiated_recording                     │  │
│  │    └─ Если playback_active && !user_initiated:                        │  │
│  │       └─ Игнорировать callback (автоматическая активация)            │  │
│  │                                                                       │  │
│  │ 3. Обработка аудио:                                                   │  │
│  │    ├─ Накопление чанков в _google_audio_chunks                       │  │
│  │    └─ Установка: _google_chunk_event.set()                           │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
│                                                                               │
│  ✅ АУДИО ОБРАБАТЫВАЕТСЯ КОРРЕКТНО                                            │
│  ✅ CALLBACK НЕ ИГНОРИРУЕТСЯ БЕЗ ПРИЧИНЫ                                      │
│                                                                               │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Этап 6: Пользователь отпускает Ctrl+N (RELEASE)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    СОБЫТИЕ: RELEASE (ИДЕАЛЬНОЕ)                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                               │
│  InputProcessingIntegration._handle_key_release()                            │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │ 1. Проверка состояния:                                               │  │
│  │    ├─ was_recording = _recording_started || mic_active                │  │
│  │    └─ active_session_id = _get_active_session_id()                    │  │
│  │                                                                       │  │
│  │ 2. Публикация событий:                                                │  │
│  │    ├─ voice.recording_stop {session_id, source="keyboard"}           │  │
│  │    └─ mode.request {target=PROCESSING, source="keyboard"}             │  │
│  │                                                                       │  │
│  │ 3. Сброс флагов:                                                      │  │
│  │    ├─ _long_press_in_progress = False                                 │  │
│  │    └─ _recording_started = False                                      │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
│                                                                               │
│  ✅ СОСТОЯНИЕ: InputState = PROCESSING                                        │
│  ✅ ФЛАГИ: _recording_started = False, _long_press_in_progress = False      │
│                                                                               │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Этап 7: VoiceRecognitionIntegration получает voice.recording_stop

```
┌─────────────────────────────────────────────────────────────────────────────┐
│            VoiceRecognitionIntegration._on_recording_stop()                  │
│                          (ИДЕАЛЬНОЕ)                                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                               │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │ 1. Проверка session_id:                                               │  │
│  │    ├─ active_session_id = _get_active_session_id()                   │  │
│  │    └─ Если active_session_id != request_session_id:                   │  │
│  │       └─ Игнорировать (не наша сессия)                                │  │
│  │                                                                       │  │
│  │ 2. Остановка Google записи:                                           │  │
│  │    ├─ Ожидание чанков: await asyncio.sleep(chunk_wait = 1.0s)         │  │
│  │    ├─ _google_recording_active = False  # ✅ ПЕРЕД остановкой         │  │
│  │    ├─ await asyncio.sleep(0.1)  # Завершение callback'ов              │  │
│  │    ├─ _google_stop_listening(wait_for_stop=False)                     │  │
│  │    └─ await asyncio.sleep(callback_wait = 0.5s)                       │  │
│  │                                                                       │  │
│  │ 3. Объединение чанков:                                                │  │
│  │    ├─ Объединение всех чанков из _google_audio_chunks                │  │
│  │    └─ Создание AudioData из объединённых данных                       │  │
│  │                                                                       │  │
│  │ 4. Распознавание:                                                     │  │
│  │    └─ _recognize_google_audio(audio_data, session_id)                  │  │
│  │                                                                       │  │
│  │ 5. Публикация результата:                                             │  │
│  │    ├─ voice.recognition_completed {session_id, text}                  │  │
│  │    └─ ИЛИ voice.recognition_failed {session_id, error}                 │  │
│  │                                                                       │  │
│  │ 6. Очистка состояния:                                                 │  │
│  │    ├─ _google_recording_active = False                                 │  │
│  │    ├─ _google_stop_listening = None                                    │  │
│  │    ├─ _google_audio_chunks = []                                        │  │
│  │    ├─ _recording_active = False                                        │  │
│  │    ├─ _user_initiated_recording = False                                │  │
│  │    ├─ state_manager.set_microphone_state("idle", session_id=None)      │  │
│  │    └─ Публикация: microphone.closed {session_id}                      │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
│                                                                               │
│  ✅ СОСТОЯНИЕ: MicrophoneState = idle                                         │
│  ✅ ФЛАГИ: Все флаги сброшены, микрофон гарантированно закрыт                │
│                                                                               │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Этап 8: Воспроизведение ответа (PROCESSING)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    СОСТОЯНИЕ: PROCESSING (ИДЕАЛЬНОЕ)                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                               │
│  AppMode:                    PROCESSING                                       │
│  InputState:                  PROCESSING                                      │
│  MicrophoneState:             idle                                            │
│                                                                               │
│  Флаги InputProcessingIntegration:                                            │
│    _recording_started:        False                                           │
│    _playback_active:          True                                            │
│    _pending_session_id:       None                                            │
│    _active_grpc_session_id:   session_id                                      │
│    _long_press_in_progress:   False                                           │
│    _session_recognized:       True                                             │
│    _last_playback_start_ts:   time.monotonic()                                │
│                                                                               │
│  Флаги VoiceRecognitionIntegration:                                           │
│    _recording_active:         False                                           │
│    _google_recording_active:  False                                           │
│    _google_stop_listening:    None                                            │
│    _user_initiated_recording: False                                           │
│                                                                               │
│  ✅ МИКРОФОН ГАРАНТИРОВАННО ЗАКРЫТ                                            │
│  ✅ ВОСПРОИЗВЕДЕНИЕ АКТИВНО                                                    │
│                                                                               │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Этап 9: Завершение воспроизведения (playback.completed)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│            InputProcessingIntegration._on_playback_finished()                │
│                          (ИДЕАЛЬНОЕ)                                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                               │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │ 1. Проверка микрофона:                                                │  │
│  │    ├─ mic_active = state_manager.is_microphone_active()               │  │
│  │    └─ Если mic_active == True:                                        │  │
│  │       ├─ ⚠️ КРИТИЧНО: Микрофон должен быть закрыт!                    │  │
│  │       ├─ Публикация: voice.recording_stop {session_id=None}          │  │
│  │       └─ Ожидание: _wait_for_mic_closed_with_timeout(1.0s)            │  │
│  │                                                                       │  │
│  │ 2. Проверка новой записи:                                             │  │
│  │    ├─ Если mic_active && _recording_started:                          │  │
│  │       └─ НЕ сбрасывать сессию (новая запись началась)                 │  │
│  │                                                                       │  │
│  │ 3. Сброс сессии:                                                      │  │
│  │    ├─ _reset_session("playback_completed")                            │  │
│  │    │   ├─ _recording_started = False                                   │  │
│  │    │   ├─ _pending_session_id = None                                   │  │
│  │    │   ├─ _active_grpc_session_id = None                               │  │
│  │    │   └─ _input_state = IDLE                                          │  │
│  │    └─ _notify_playback_idle()                                          │  │
│  │                                                                       │  │
│  │ 4. Сброс флагов воспроизведения:                                       │  │
│  │    ├─ _playback_active = False                                         │  │
│  │    └─ _last_playback_start_ts = 0.0  # Только для системных            │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
│                                                                               │
│  ✅ МИКРОФОН ГАРАНТИРОВАННО ЗАКРЫТ                                            │
│  ✅ ВСЕ ФЛАГИ СБРОШЕНЫ                                                         │
│                                                                               │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Этап 10: Возврат в SLEEPING

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    СОСТОЯНИЕ: SLEEPING (ИДЕАЛЬНОЕ)                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                               │
│  AppMode:                    SLEEPING                                        │
│  InputState:                  IDLE                                            │
│  MicrophoneState:             idle                                            │
│                                                                               │
│  Флаги InputProcessingIntegration:                                            │
│    _recording_started:        False                                           │
│    _playback_active:          False                                           │
│    _pending_session_id:       None                                            │
│    _active_grpc_session_id:   None                                            │
│    _long_press_in_progress:   False                                           │
│    _session_recognized:       False                                           │
│    _last_playback_start_ts:   0.0                                             │
│                                                                               │
│  Флаги VoiceRecognitionIntegration:                                           │
│    _recording_active:         False                                           │
│    _google_recording_active:  False                                           │
│    _google_stop_listening:    None                                            │
│    _user_initiated_recording: False                                           │
│                                                                               │
│  ✅ ВСЕ ФЛАГИ В ПРАВИЛЬНОМ СОСТОЯНИИ                                          │
│  ✅ МИКРОФОН ГАРАНТИРОВАННО ЗАКРЫТ                                            │
│  ✅ СИСТЕМА ГОТОВА К НОВОЙ АКТИВАЦИИ                                          │
│                                                                               │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Идеальная диаграмма полного цикла

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         ИДЕАЛЬНЫЙ ПОЛНЫЙ ЦИКЛ                                │
└─────────────────────────────────────────────────────────────────────────────┘

    [SLEEPING]
    ├─ AppMode: SLEEPING
    ├─ InputState: IDLE
    ├─ MicrophoneState: idle
    ├─ _recording_started: False
    ├─ _playback_active: False
    └─ _google_recording_active: False
         │
         │ Пользователь нажимает Ctrl+N (PRESS)
         ▼
    [PRESS]
    ├─ InputState: PENDING
    ├─ _pending_session_id: установлен
    └─ _recording_started: False
         │
         │ Пользователь удерживает Ctrl+N (LONG_PRESS)
         ▼
    [LONG_PRESS]
    ├─ Проверка: _can_start_recording() ✓
    ├─ Проверка микрофона: mic_active == False ✓
    ├─ _recording_started: True
    ├─ Публикация: voice.recording_start
    └─ Публикация: mode.request(LISTENING)
         │
         ▼
    [VoiceRecognitionIntegration._on_recording_start]
    ├─ Проверки блокировки: все пройдены ✓
    ├─ AVF диагностика: активирован → деактивирован ✓
    ├─ Проверка разрешений: granted ✓
    ├─ _google_recording_active: True (ПЕРЕД listen_in_background)
    ├─ listen_in_background() запущен
    ├─ state_manager.set_microphone_state("active")
    └─ Публикация: microphone.opened
         │
         ▼
    [LISTENING]
    ├─ AppMode: LISTENING
    ├─ InputState: LISTENING
    ├─ MicrophoneState: active
    ├─ _recording_started: True
    ├─ _google_recording_active: True
    └─ Callback получает аудио ✓
         │
         │ Пользователь отпускает Ctrl+N (RELEASE)
         ▼
    [RELEASE]
    ├─ Публикация: voice.recording_stop
    ├─ Публикация: mode.request(PROCESSING)
    └─ _recording_started: False
         │
         ▼
    [VoiceRecognitionIntegration._on_recording_stop]
    ├─ _google_recording_active: False (ПЕРЕД остановкой)
    ├─ _google_stop_listening() вызван
    ├─ Объединение чанков
    ├─ Распознавание: _recognize_google_audio()
    ├─ Публикация: voice.recognition_completed
    ├─ state_manager.set_microphone_state("idle")
    └─ Публикация: microphone.closed
         │
         ▼
    [PROCESSING]
    ├─ AppMode: PROCESSING
    ├─ InputState: PROCESSING
    ├─ MicrophoneState: idle
    ├─ _playback_active: True
    └─ Воспроизведение ответа
         │
         │ playback.completed
         ▼
    [playback.completed]
    ├─ Проверка: mic_active == True? → принудительное закрытие ✓
    ├─ _reset_session("playback_completed")
    ├─ _playback_active: False
    └─ Публикация: mode.request(SLEEPING)
         │
         ▼
    [SLEEPING]
    ├─ AppMode: SLEEPING
    ├─ InputState: IDLE
    ├─ MicrophoneState: idle
    ├─ _recording_started: False
    ├─ _playback_active: False
    └─ _google_recording_active: False
```

---

## Критические правила идеальной системы

### 1. Правило закрытия микрофона

```
✅ ВСЕГДА закрывать микрофон после:
   - voice.recording_stop
   - playback.completed (если mic_active == True)
   - Ошибки активации
   - Прерывания записи

✅ ГАРАНТИРОВАТЬ:
   - state_manager.set_microphone_state("idle", session_id=None)
   - Публикация: microphone.closed {session_id}
   - _google_recording_active = False
   - _google_stop_listening = None
```

### 2. Правило активации микрофона

```
✅ ВСЕГДА активировать микрофон ТОЛЬКО через:
   - voice.recording_start {source="keyboard"} (от пользователя)
   - НЕ автоматически после playback.completed

✅ ГАРАНТИРОВАТЬ:
   - Проверка разрешений перед активацией
   - AVF полностью деактивирован перед Google
   - _google_recording_active = True ПЕРЕД listen_in_background
   - state_manager.set_microphone_state("active", session_id)
```

### 3. Правило обработки callback

```
✅ ВСЕГДА проверять в callback:
   - _google_recording_active == True
   - _google_stop_listening != None
   - state_manager.is_microphone_active() == True
   - playback_active && !user_initiated → игнорировать

✅ ГАРАНТИРОВАТЬ:
   - Callback не обрабатывается после остановки записи
   - Callback не обрабатывается при автоматической активации во время воспроизведения
```

### 4. Правило сброса флагов

```
✅ ВСЕГДА сбрасывать флаги после:
   - playback.completed
   - voice.recording_stop
   - Ошибки активации
   - Прерывания записи

✅ ГАРАНТИРОВАТЬ:
   - _recording_started = False
   - _playback_active = False
   - _google_recording_active = False
   - _pending_session_id = None
   - _active_grpc_session_id = None
```

---

## Матрица состояний и флагов (идеальная)

| Этап | AppMode | InputState | MicrophoneState | _recording_started | _playback_active | _google_recording_active | mic_active |
|------|---------|------------|-----------------|-------------------|------------------|-------------------------|------------|
| SLEEPING | SLEEPING | IDLE | idle | False | False | False | False |
| PRESS | SLEEPING | PENDING | idle | False | False | False | False |
| LONG_PRESS | SLEEPING | LISTENING | idle | True | False | False | False |
| recording_start | LISTENING | LISTENING | active | True | False | True | True |
| RELEASE | LISTENING | PROCESSING | active | False | False | True | True |
| recording_stop | PROCESSING | PROCESSING | idle | False | False | False | False |
| playback.started | PROCESSING | PROCESSING | idle | False | True | False | False |
| playback.completed | PROCESSING | PROCESSING | idle | False | False | False | False |
| SLEEPING (final) | SLEEPING | IDLE | idle | False | False | False | False |

---

## Чек-лист идеального состояния

### После каждого этапа проверять:

- [ ] **AppMode** соответствует ожидаемому состоянию
- [ ] **InputState** соответствует ожидаемому состоянию
- [ ] **MicrophoneState** соответствует ожидаемому состоянию
- [ ] **Все флаги** в правильном состоянии
- [ ] **Микрофон** закрыт, когда должен быть закрыт
- [ ] **Микрофон** активен, когда должен быть активен
- [ ] **Нет конфликтов** между состояниями
- [ ] **Нет залипания** флагов

### После playback.completed:

- [ ] **mic_active == False** (микрофон гарантированно закрыт)
- [ ] **_recording_started == False**
- [ ] **_playback_active == False**
- [ ] **_google_recording_active == False**
- [ ] **_pending_session_id == None**
- [ ] **_active_grpc_session_id == None**
- [ ] **AppMode == SLEEPING**
- [ ] **InputState == IDLE**
- [ ] **MicrophoneState == idle**

---

## Связанные документы

- `Docs/MICROPHONE_ACTIVATION_ANALYSIS.md` — анализ проблем
- `Docs/MICROPHONE_ACTIVATION_FLOW_DIAGRAM.md` — схема потока
- `Docs/CORRECT_MICROPHONE_LOGIC.md` — правильная логика активации

