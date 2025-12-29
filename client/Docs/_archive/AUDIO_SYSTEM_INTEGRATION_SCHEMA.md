# Схема внедрения новой аудиосистемы

**Статус**: Нормативный документ  
**Версия**: 1.0  
**Дата**: 2025-01-XX

---

## 1. Текущая архитектура (до миграции)

### 1.1 Схема компонентов

```
┌─────────────────────────────────────────────────────────────────┐
│                    SimpleModuleCoordinator                       │
│                    (Главный координатор)                         │
└───────────────────────────┬─────────────────────────────────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
        ▼                    ▼                    ▼
┌───────────────┐   ┌──────────────────┐   ┌──────────────┐
│   Input       │   │ VoiceRecognition │   │  Speech     │
│ Processing    │──▶│   Integration    │   │ Playback    │
│ Integration   │   │                  │   │ Integration │
└───────┬───────┘   └────────┬─────────┘   └──────┬───────┘
        │                    │                    │
        │                    │                    │
        ▼                    ▼                    ▼
┌───────────────┐   ┌──────────────────┐   ┌──────────────┐
│  Keyboard     │   │ SpeechRecognizer│   │ Sequential   │
│  Monitor      │   │                  │   │ SpeechPlayer │
│               │   │ ┌──────────────┐│   │              │
│               │   │ │AudioDevice   ││   │ ┌──────────┐ │
│               │   │ │Monitor       ││   │ │sounddevice││
│               │   │ │(polling 0.5s)││   │ │OutputStream││
│               │   │ └──────────────┘│   │ └──────────┘ │
│               │   │                  │   │              │
│               │   │ ┌──────────────┐│   │              │
│               │   │ │sounddevice   ││   │              │
│               │   │ │InputStream   ││   │              │
│               │   │ └──────────────┘│   │              │
│               │   └──────────────────┘   └──────────────┘
└───────────────┘
```

### 1.2 Поток событий (текущий)

```
[Пользователь нажимает Ctrl+N]
        │
        ▼
InputProcessingIntegration
        │
        ├─▶ publish("voice.recording_start")
        │
        ▼
VoiceRecognitionIntegration
        │
        ├─▶ SpeechRecognizer.start_listening()
        │   │
        │   ├─▶ AudioDeviceMonitor (polling 0.5s)
        │   │   └─▶ sd.default.device[0] (системный default)
        │   │
        │   └─▶ sounddevice.InputStream (открывает микрофон)
        │       └─▶ Google Speech Recognition
        │
        ├─▶ publish("voice.mic_opened")
        │
        ▼
[Пользователь отпускает Ctrl+N]
        │
        ▼
InputProcessingIntegration
        │
        ├─▶ publish("voice.recording_stop")
        │
        ▼
VoiceRecognitionIntegration
        │
        ├─▶ SpeechRecognizer.stop_listening()
        │   └─▶ sounddevice.InputStream.close()
        │
        ├─▶ publish("voice.mic_closed")
        │
        ├─▶ publish("voice.recognition_completed")
        │
        ▼
GrpcClientIntegration
        │
        ├─▶ publish("grpc.audio_chunk")
        │
        ▼
SpeechPlaybackIntegration
        │
        ├─▶ SequentialSpeechPlayer.add_audio_data()
        │   └─▶ sounddevice.OutputStream (воспроизведение)
        │
        ├─▶ publish("playback.started")
        │
        └─▶ publish("playback.completed")
```

---

## 2. Новая архитектура (после миграции)

### 2.1 Схема компонентов с RouteManager

```
┌─────────────────────────────────────────────────────────────────┐
│                    SimpleModuleCoordinator                       │
│                    (Главный координатор)                         │
└───────────────────────────┬─────────────────────────────────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
        ▼                    ▼                    ▼
┌───────────────┐   ┌──────────────────┐   ┌──────────────┐
│   Input       │   │ VoiceRecognition │   │  Speech     │
│ Processing    │──▶│   Integration    │   │ Playback    │
│ Integration   │   │                  │   │ Integration │
└───────┬───────┘   └────────┬─────────┘   └──────┬───────┘
        │                    │                    │
        │                    │                    │
        ▼                    ▼                    ▼
┌───────────────┐   ┌──────────────────┐   ┌──────────────┐
│  Keyboard     │   │ SpeechRecognizer │   │ Sequential   │
│  Monitor      │   │                  │   │ SpeechPlayer │
│               │   │ ┌──────────────┐│   │              │
│               │   │ │Google Input  ││   │ ┌──────────┐ │
│               │   │ │Controller    ││   │ │AVFoundation││
│               │   │ │(adapter)     ││   │ │AudioPlayback││
│               │   │ └──────────────┘│   │ │(AVAudioEngine)││
│               │   │                  │   │ └──────────┘ │
│               │   │ ┌──────────────┐│   │              │
│               │   │ │sounddevice   ││   │              │
│               │   │ │InputStream   ││   │              │
│               │   │ │(единственный ││   │              │
│               │   │ │ владелец)    ││   │              │
│               │   │ └──────────────┘│   │              │
│               │   └──────────────────┘   └──────────────┘
└───────────────┘
        │                    │                    │
        │                    │                    │
        └────────────────────┼────────────────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ AudioRoute      │
                    │ Manager         │
                    │ Integration     │
                    │ (НОВЫЙ)         │
                    └────────┬─────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
        ▼                    ▼                    ▼
┌───────────────┐   ┌──────────────────┐   ┌──────────────┐
│AVFoundation   │   │  RouteManager    │   │AVFoundation  │
│DeviceMonitor  │──▶│  (reconcile)     │──▶│AudioPlayback │
│               │   │                  │   │              │
│ ┌───────────┐│   │ ┌──────────────┐│   │ ┌──────────┐ │
│ │NSNotif    ││   │ │InputSM       ││   │ │AVAudio   │ │
│ │Center     ││   │ │OutputSM      ││   │ │Engine    │ │
│ │(0ms)      ││   │ │Mapping       ││   │ │          │ │
│ └───────────┘│   │ │Debounce      ││   │ │AVAudio   │ │
│              │   │ │Single-flight ││   │ │PlayerNode │ │
│ ┌───────────┐│   │ └──────────────┘│   │ └──────────┘ │
│ │Polling    ││   │                  │   │              │
│ │(1-2s)     ││   │                  │   │              │
│ └───────────┘│   │                  │   │              │
│              │   │ ┌──────────────┐│   │              │
│ ┌───────────┐│   │ │Device        ││   │              │
│ │AVCapture  ││   │ │Signature    ││   │              │
│ │Device     ││   │ │Mapping      ││   │              │
│ │(devices)  ││   │ │(AVF→PA)     ││   │              │
│ └───────────┘│   │ └──────────────┘│   │              │
└──────────────┘   └──────────────────┘   └──────────────┘
```

### 2.2 Поток событий (новый с RouteManager)

```
[Пользователь нажимает Ctrl+N]
        │
        ▼
InputProcessingIntegration
        │
        ├─▶ publish("voice.recording_start")
        │
        ▼
AudioRouteManagerIntegration (НОВЫЙ)
        │
        ├─▶ RouteManager.reconcile_routes()
        │   │
        │   ├─▶ Snapshot состояния
        │   │   ├─▶ AVFoundationDeviceMonitor.get_devices()
        │   │   ├─▶ Проверка first_run_in_progress
        │   │   ├─▶ Проверка permission_restart_pending
        │   │   └─▶ Проверка update_in_progress
        │   │
        │   ├─▶ Определение desired route
        │   │   └─▶ System default input (от AVFoundation)
        │   │
        │   ├─▶ Маппинг AVFoundation → PortAudio
        │   │   ├─▶ DeviceSignature (нормализация имени)
        │   │   ├─▶ Confidence (HIGH/MEDIUM/LOW/NONE)
        │   │   └─▶ device_index (или None для system default)
        │   │
        │   ├─▶ Решение: restart input
        │   │   └─▶ GoogleInputController.start(device_index)
        │   │
        │   └─▶ Применение решения
        │       └─▶ SpeechRecognizer.start_listening(device_index)
        │
        ▼
VoiceRecognitionIntegration
        │
        ├─▶ SpeechRecognizer.start_listening(device_index)
        │   │
        │   ├─▶ sounddevice.InputStream(device=device_index)
        │   │   └─▶ Google Speech Recognition
        │   │
        │   └─▶ Heartbeat через audio callback
        │
        ├─▶ publish("voice.mic_opened")
        │
        ▼
[AVFoundationDeviceMonitor обнаруживает изменение устройства]
        │
        ├─▶ NSNotificationCenter callback (0ms)
        │   └─▶ asyncio.run_coroutine_threadsafe()
        │       └─▶ publish("audio.device.default_changed")
        │
        └─▶ Polling (1-2s fallback)
            └─▶ publish("audio.device.default_changed")
        │
        ▼
AudioRouteManagerIntegration
        │
        ├─▶ RouteManager.reconcile_routes()
        │   │
        │   ├─▶ Debounce (per-device)
        │   │   ├─▶ Bluetooth: 200ms → 1200ms
        │   │   ├─▶ USB: 100ms → 600ms
        │   │   └─▶ Built-in: 100ms → 200ms
        │   │
        │   ├─▶ Single-flight (pending если уже выполняется)
        │   │
        │   └─▶ Решение: restart input с новым устройством
        │       └─▶ SpeechRecognizer.stop_listening()
        │           └─▶ SpeechRecognizer.start_listening(new_device_index)
        │
        ▼
[Пользователь отпускает Ctrl+N]
        │
        ▼
InputProcessingIntegration
        │
        ├─▶ publish("voice.recording_stop")
        │
        ▼
AudioRouteManagerIntegration
        │
        ├─▶ RouteManager.reconcile_routes()
        │   └─▶ Решение: stop input
        │       └─▶ GoogleInputController.stop()
        │
        ▼
VoiceRecognitionIntegration
        │
        ├─▶ SpeechRecognizer.stop_listening()
        │   └─▶ sounddevice.InputStream.close()
        │
        ├─▶ publish("voice.mic_closed")
        │
        ├─▶ publish("voice.recognition_completed")
        │
        ▼
GrpcClientIntegration
        │
        ├─▶ publish("grpc.audio_chunk")
        │
        ▼
AudioRouteManagerIntegration
        │
        ├─▶ RouteManager.reconcile_output()
        │   │
        │   ├─▶ Проверка output устройства
        │   │   └─▶ AVFoundationDeviceMonitor.get_output_device()
        │   │
        │   └─▶ Решение: готов к воспроизведению
        │       └─▶ AVFoundationAudioPlayback.is_ready()
        │
        ▼
SpeechPlaybackIntegration
        │
        ├─▶ AVFoundationAudioPlayback.schedule_buffer()
        │   │
        │   ├─▶ Конвертация numpy → AVAudioPCMBuffer
        │   │   └─▶ AVAudioConverter (16kHz → 48kHz если нужно)
        │   │
        │   └─▶ AVAudioPlayerNode.scheduleBuffer()
        │       └─▶ AVAudioEngine (воспроизведение)
        │
        ├─▶ publish("playback.started")
        │
        └─▶ publish("playback.completed")
```

---

## 3. Детальная схема RouteManager

### 3.1 Архитектура RouteManager

```
┌─────────────────────────────────────────────────────────────┐
│              AudioRouteManagerIntegration                    │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │         AudioRouteManager (reconcile loop)            │  │
│  │                                                       │  │
│  │  ┌──────────────────────────────────────────────┐   │  │
│  │  │ 1. Snapshot Provider                         │   │  │
│  │  │    ├─ AVFoundation Snapshot                  │   │  │
│  │  │    ├─ PortAudio Devices                       │   │  │
│  │  │    ├─ State (first_run, permission_restart)   │   │  │
│  │  │    └─ Active Routes                          │   │  │
│  │  └──────────────────────────────────────────────┘   │  │
│  │                                                       │  │
│  │  ┌──────────────────────────────────────────────┐   │  │
│  │  │ 2. Route Decision                            │   │  │
│  │  │    ├─ Desired Route (system default/manual)  │   │  │
│  │  │    ├─ Input Mapping (AVF → PortAudio)        │   │  │
│  │  │    ├─ Output Selection (system default)      │   │  │
│  │  │    └─ Comparison with Active Route            │   │  │
│  │  └──────────────────────────────────────────────┘   │  │
│  │                                                       │  │
│  │  ┌──────────────────────────────────────────────┐   │  │
│  │  │ 3. Decision Application                     │   │  │
│  │  │    ├─ Input: restart/stop/noop               │   │  │
│  │  │    ├─ Output: recreate/ready/noop            │   │  │
│  │  │    └─ State Machines (InputSM/OutputSM)      │   │  │
│  │  └──────────────────────────────────────────────┘   │  │
│  │                                                       │  │
│  │  ┌──────────────────────────────────────────────┐   │  │
│  │  │ 4. Event Emission                            │   │  │
│  │  │    ├─ audio.route.snapshot                   │   │  │
│  │  │    ├─ audio.input.active/failed              │   │  │
│  │  │    └─ audio.output.ready/error              │   │  │
│  │  └──────────────────────────────────────────────┘   │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │         Adapters                                      │  │
│  │                                                       │  │
│  │  ┌──────────────┐  ┌──────────────┐  ┌────────────┐ │  │
│  │  │AVFoundation  │  │Google Input  │  │AVFoundation│ │  │
│  │  │DeviceMonitor │  │Controller    │  │AudioPlayback│ │  │
│  │  │              │  │              │  │            │ │  │
│  │  │• NSNotif     │  │• is_running()│  │• is_ready()│ │  │
│  │  │• Polling     │  │• start()     │  │• recreate()│ │  │
│  │  │• Devices     │  │• stop()      │  │• schedule()│ │  │
│  │  └──────────────┘  │• heartbeat()│  └────────────┘ │  │
│  │                    └──────────────┘                 │  │
│  └──────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────┘
```

### 3.2 Reconcile алгоритм

```
reconcile_routes():
    ┌─────────────────────────────────────┐
    │ 1. Snapshot мира                     │
    │    ├─ AVFoundation devices           │
    │    ├─ PortAudio devices              │
    │    ├─ System default input/output    │
    │    ├─ Active input/output            │
    │    ├─ first_run_in_progress          │
    │    ├─ permission_restart_pending     │
    │    └─ update_in_progress             │
    └─────────────────────────────────────┘
            │
            ▼
    ┌─────────────────────────────────────┐
    │ 2. Определение desired route        │
    │    ├─ Manual selection?             │
    │    │   └─▶ Use manual device        │
    │    └─ Follow system?                │
    │        └─▶ Use system default       │
    └─────────────────────────────────────┘
            │
            ▼
    ┌─────────────────────────────────────┐
    │ 3. Маппинг input (AVF → PortAudio)  │
    │    ├─ Normalize device name          │
    │    ├─ Build DeviceSignature          │
    │    ├─ Find PortAudio match           │
    │    ├─ Calculate confidence           │
    │    └─ Get device_index               │
    └─────────────────────────────────────┘
            │
            ▼
    ┌─────────────────────────────────────┐
    │ 4. Сравнение с active route         │
    │    ├─ Input changed?                │
    │    │   └─▶ Decision: restart input  │
    │    ├─ Output changed?                │
    │    │   └─▶ Decision: recreate output│
    │    └─ No changes?                    │
    │        └─▶ Decision: noop            │
    └─────────────────────────────────────┘
            │
            ▼
    ┌─────────────────────────────────────┐
    │ 5. Применение решения               │
    │    ├─ Input:                        │
    │    │   ├─ restart → GoogleInputController.start()
    │    │   ├─ stop → GoogleInputController.stop()
    │    │   └─ noop → skip
    │    └─ Output:                       │
    │        ├─ recreate → AVFoundationAudioPlayback.recreate()
    │        └─ noop → skip
    └─────────────────────────────────────┘
            │
            ▼
    ┌─────────────────────────────────────┐
    │ 6. Эмиссия событий                  │
    │    ├─ audio.route.snapshot          │
    │    ├─ audio.input.active/failed     │
    │    └─ audio.output.ready/error      │
    └─────────────────────────────────────┘
```

---

## 4. Интеграция с EventBus

### 4.1 Подписки RouteManager

```
AudioRouteManagerIntegration
    │
    ├─▶ subscribe("audio.device.connected")
    ├─▶ subscribe("audio.device.disconnected")
    ├─▶ subscribe("audio.device.default_changed")
    ├─▶ subscribe("voice.recording_start")
    ├─▶ subscribe("voice.recording_stop")
    ├─▶ subscribe("app.mode_changed")
    ├─▶ subscribe("permissions.first_run_started")
    ├─▶ subscribe("permissions.first_run_completed")
    ├─▶ subscribe("permission_restart.scheduled")
    ├─▶ subscribe("permission_restart.executing")
    └─▶ subscribe("updater.in_progress.changed")
        │
        └─▶ Все события триггерят reconcile_routes()
```

### 4.2 Публикации RouteManager

```
AudioRouteManagerIntegration
    │
    ├─▶ publish("audio.route.snapshot", {
    │       "timestamp": float,
    │       "source": "event" | "polling" | "manual",
    │       "system_default_input": {...},
    │       "active_input_signature": {...},
    │       "mapping_result": {...}
    │   })
    │
    ├─▶ publish("audio.input.active", {
    │       "uid": str,
    │       "signature": DeviceSignature,
    │       "mapping": MappingResult
    │   })
    │
    ├─▶ publish("audio.input.failed", {
    │       "uid": str,
    │       "error": str,
    │       "mapping": MappingResult
    │   })
    │
    ├─▶ publish("audio.output.ready", {
    │       "signature": DeviceSignature
    │   })
    │
    └─▶ publish("audio.output.error", {
            "error": str
        })
```

**Важно**: RouteManager НЕ публикует существующие события (`voice.recording_start/stop`, `voice.mic_opened/closed`, `playback.*`). Он только читает их и управляет маршрутизацией.

---

## 5. Порядок инициализации

### 5.1 Текущий порядок

```
1. instance_manager
2. tray
3. hardware_id
4. first_run_permissions
5. permission_restart
6. mode_management
7. input
8. voice_recognition      ← Создается здесь
9. network
10. interrupt
11. screenshot_capture
12. grpc
13. speech_playback       ← Создается здесь
14. signals
15. updater
16. welcome_message
17. voiceover_ducking
18. autostart_manager
```

### 5.2 Новый порядок (с RouteManager)

```
1. instance_manager
2. tray
3. hardware_id
4. first_run_permissions
5. permission_restart
6. mode_management
7. input
8. voice_recognition      ← Создается здесь
8.5. audio_route_manager  ← НОВЫЙ (создается после voice_recognition)
9. network
10. interrupt
11. screenshot_capture
12. grpc
13. speech_playback       ← Создается здесь (может использовать RouteManager)
14. signals
15. updater
16. welcome_message
17. voiceover_ducking
18. autostart_manager
```

**Зависимости**:
- RouteManager создается после `voice_recognition` и `speech_playback` (нужны ссылки)
- Инициализируется перед использованием аудио (перед активацией `input`)
- Условная инициализация (только если `NEXY_FEATURE_AVFOUNDATION_ROUTE_MANAGER_V2 = true`)

---

## 6. Feature Flags и условная логика

### 6.1 Проверка флагов в коде

```python
# В VoiceRecognitionIntegration
async def _on_recording_start(self, event):
    if self._first_run_in_progress:
        return
    
    # Проверка feature flag
    route_manager_enabled = self._config.get("audio_system", {}).get(
        "avfoundation_route_manager_enabled", False
    )
    
    if route_manager_enabled:
        # RouteManager управляет запуском
        await self.event_bus.publish("audio.input.request_start", {
            "session_id": event.get("session_id")
        })
    else:
        # Старая логика (fallback)
        if not self.config.simulate and self._recognizer:
            await self._recognizer.start_listening()

# В SpeechPlaybackIntegration
async def _on_audio_chunk(self, event):
    # Проверка feature flag
    avfoundation_output_enabled = self._config.get("audio_system", {}).get(
        "avfoundation_output_enabled", False
    )
    
    if avfoundation_output_enabled:
        # AVFoundation output
        audio_buffer = self._convert_to_avf_buffer(audio_data)
        self._avf_playback.schedule_buffer(audio_buffer)
    else:
        # Старая логика (fallback)
        self._player.add_audio_data(audio_data, ...)
```

### 6.2 Kill-switches

```python
# В AudioRouteManagerIntegration.initialize()
kill_switch = self._config.get("audio_system", {}).get(
    "ks_avfoundation_route_manager", False
)

if kill_switch:
    logger.warning("⚠️ Kill-switch active, RouteManager disabled")
    return False  # Не инициализируем RouteManager
```

---

## 7. Схема взаимодействия компонентов

### 7.1 Полная схема взаимодействий

```
┌─────────────────────────────────────────────────────────────────┐
│                         EventBus                                 │
│                  (Центральная шина событий)                      │
└───────────────────────────┬─────────────────────────────────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
        ▼                    ▼                    ▼
┌───────────────┐   ┌──────────────────┐   ┌──────────────┐
│   Input       │   │ VoiceRecognition │   │  Speech     │
│ Processing    │   │   Integration    │   │ Playback    │
│               │   │                  │   │ Integration │
│ Публикует:    │   │ Публикует:       │   │ Публикует:  │
│ • recording_  │   │ • mic_opened     │   │ • playback. │
│   start/stop  │   │ • mic_closed     │   │   started   │
│               │   │ • recognition_*  │   │ • playback. │
│               │   │                  │   │   completed │
└───────┬───────┘   └────────┬─────────┘   └──────┬───────┘
        │                    │                    │
        │                    │                    │
        └────────────────────┼────────────────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ AudioRoute      │
                    │ Manager         │
                    │ Integration     │
                    │                 │
                    │ Читает:         │
                    │ • recording_    │
                    │   start/stop    │
                    │ • mic_opened/   │
                    │   closed        │
                    │ • playback.*    │
                    │ • app.mode_     │
                    │   changed       │
                    │                 │
                    │ Публикует:      │
                    │ • audio.route.  │
                    │   snapshot      │
                    │ • audio.input.  │
                    │   active/failed │
                    │ • audio.output. │
                    │   ready/error   │
                    └─────────────────┘
```

### 7.2 Принцип взаимодействия

**RouteManager**:
- ✅ **Читает** существующие события (не изменяет их)
- ✅ **Публикует** только новые диагностические события
- ✅ **Управляет** маршрутизацией через адаптеры
- ❌ **НЕ дублирует** функциональность других интеграций
- ❌ **НЕ публикует** существующие события

**Другие интеграции**:
- ✅ **Продолжают** публиковать существующие события
- ✅ **Продолжают** читать существующие события
- ✅ **Работают** независимо от RouteManager (с fallback)

---

## 8. Заключение

**Ключевые принципы внедрения**:

1. ✅ **Минимальные изменения** - существующие интеграции изменяются минимально
2. ✅ **Обратная совместимость** - все существующие события сохраняются
3. ✅ **Нет дублирования** - RouteManager не публикует существующие события
4. ✅ **Нет конфликтов** - RouteManager только читает события и управляет маршрутизацией
5. ✅ **Feature flags** - постепенный роллаут с возможностью отката
6. ✅ **Fallback** - старая система работает параллельно до полного роллаута

**Схема внедрения готова к реализации.**

