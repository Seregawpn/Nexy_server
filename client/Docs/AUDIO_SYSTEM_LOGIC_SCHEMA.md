# Схема работы логики аудиосистемы на AVFoundation

**Дата**: 2025-01-XX  
**Версия**: 1.0  
**Статус**: Предварительная схема для планирования реализации

---

## 📊 Общая архитектура системы

```mermaid
graph TB
    subgraph "macOS System Layer"
        CoreAudio[CoreAudio<br/>Системный менеджер аудио]
        NSNotification[NSNotificationCenter<br/>Уведомления о устройствах]
        AVAudioSession[AVAudioSession<br/>Системные маршруты]
    end
    
    subgraph "AVFoundation Layer"
        AVFMonitor[AVFoundationDeviceMonitor<br/>Мониторинг устройств]
        AVFOutput[AVFoundationAudioPlayback<br/>Воспроизведение]
        DeviceMapper[DeviceMapper<br/>AVFoundation → PortAudio]
    end
    
    subgraph "Route Manager Layer"
        RouteManager[AudioRouteManager<br/>Центральный координатор]
        ReconcileEngine[ReconcileEngine<br/>Сравнение состояний]
        DecisionEngine[DecisionEngine<br/>Принятие решений]
        DebounceManager[DebounceManager<br/>Задержки событий]
        InputSM[InputStateMachine<br/>Состояния input]
        OutputSM[OutputStateMachine<br/>Состояния output]
    end
    
    subgraph "Integration Layer"
        RouteManagerInt[AudioRouteManagerIntegration<br/>Интеграция с EventBus]
        VoiceRecInt[VoiceRecognitionIntegration<br/>Адаптированная]
        SpeechPlayInt[SpeechPlaybackIntegration<br/>Адаптированная]
    end
    
    subgraph "Module Layer"
        SpeechRecognizer[SpeechRecognizer<br/>Распознавание речи]
        GoogleInput[GoogleInputController<br/>Адаптер для GSR]
        SequentialPlayer[SequentialSpeechPlayer<br/>Адаптированный плеер]
        AudioRecovery[AudioRecoveryManager<br/>Восстановление]
    end
    
    subgraph "EventBus"
        EventBus[EventBus<br/>Центральная шина событий]
    end
    
    subgraph "State Management"
        StateManager[ApplicationStateManager<br/>Управление состоянием]
        Selectors[Selectors<br/>Проверка состояний]
        Gateways[Gateways<br/>Принятие решений]
    end
    
    %% macOS → AVFoundation
    CoreAudio --> AVFMonitor
    NSNotification --> AVFMonitor
    AVAudioSession --> AVFOutput
    
    %% AVFoundation → Route Manager
    AVFMonitor --> DeviceMapper
    DeviceMapper --> RouteManager
    AVFOutput --> RouteManager
    
    %% Route Manager внутренние связи
    RouteManager --> ReconcileEngine
    RouteManager --> DecisionEngine
    RouteManager --> DebounceManager
    RouteManager --> InputSM
    RouteManager --> OutputSM
    
    %% Route Manager → Integration
    RouteManager --> RouteManagerInt
    RouteManagerInt --> EventBus
    
    %% Integration → Modules
    RouteManagerInt --> VoiceRecInt
    RouteManagerInt --> SpeechPlayInt
    VoiceRecInt --> SpeechRecognizer
    SpeechRecognizer --> GoogleInput
    SpeechPlayInt --> SequentialPlayer
    SequentialPlayer --> AVFOutput
    SpeechRecognizer --> AudioRecovery
    
    %% EventBus связи
    EventBus --> RouteManagerInt
    EventBus --> VoiceRecInt
    EventBus --> SpeechPlayInt
    EventBus --> StateManager
    
    %% State Management связи
    StateManager --> Selectors
    Selectors --> Gateways
    Gateways --> DecisionEngine
    
    style RouteManager fill:#e1f5ff
    style RouteManagerInt fill:#fff4e1
    style EventBus fill:#ffebee
    style AVFMonitor fill:#e8f5e9
    style AVFOutput fill:#e8f5e9
```

---

## 🔄 Поток данных: Input (Микрофон)

```mermaid
sequenceDiagram
    participant User as Пользователь
    participant EventBus as EventBus
    participant RouteManagerInt as RouteManagerIntegration
    participant RouteManager as AudioRouteManager
    participant AVFMonitor as AVFoundationMonitor
    participant DeviceMapper as DeviceMapper
    participant VoiceRecInt as VoiceRecognitionIntegration
    participant SpeechRecognizer as SpeechRecognizer
    participant GoogleInput as GoogleInputController
    participant GSR as Google Speech Recognition
    
    User->>EventBus: keyboard.short_press
    EventBus->>RouteManagerInt: voice.recording_start
    
    RouteManagerInt->>RouteManager: reconcile_routes()
    
    RouteManager->>AVFMonitor: get_current_devices()
    AVFMonitor-->>RouteManager: [DeviceSignature]
    
    RouteManager->>DeviceMapper: map_to_portaudio(signature)
    DeviceMapper-->>RouteManager: MappingResult(device_index, confidence)
    
    RouteManager->>RouteManager: decide_start_listening()
    
    alt Decision: START
        RouteManager->>InputSM: transition_to(STARTING)
        RouteManager->>VoiceRecInt: device_index, signature
        VoiceRecInt->>SpeechRecognizer: start_listening(device_index)
        SpeechRecognizer->>GoogleInput: get_microphone(device_index)
        GoogleInput->>GSR: Microphone(device_index=device_index)
        GSR->>GSR: Захват аудио
        GSR-->>SpeechRecognizer: Аудио данные
        SpeechRecognizer->>InputSM: transition_to(ACTIVE)
        RouteManager->>EventBus: audio.input.started
    else Decision: ABORT
        RouteManager->>EventBus: audio.input.aborted
    else Decision: RETRY
        RouteManager->>DebounceManager: schedule_retry()
        RouteManager->>EventBus: audio.input.retry_scheduled
    end
```

---

## 🔄 Поток данных: Output (Воспроизведение)

```mermaid
sequenceDiagram
    participant gRPC as gRPC Server
    participant EventBus as EventBus
    participant SpeechPlayInt as SpeechPlaybackIntegration
    participant RouteManagerInt as RouteManagerIntegration
    participant RouteManager as AudioRouteManager
    participant AVFOutput as AVFoundationAudioPlayback
    participant AVAudioEngine as AVAudioEngine
    
    gRPC->>EventBus: grpc.response.audio
    EventBus->>SpeechPlayInt: grpc.response.audio
    
    SpeechPlayInt->>RouteManagerInt: get_output_device()
    RouteManagerInt->>RouteManager: get_active_output_device()
    
    RouteManager->>AVFOutput: is_ready()
    
    alt Output ready
        SpeechPlayInt->>AVFOutput: play_chunk(audio_data)
        AVFOutput->>AVFOutput: convert_numpy_to_pcm(audio_data)
        AVFOutput->>AVAudioEngine: scheduleBuffer(pcm_buffer)
        AVAudioEngine->>AVAudioEngine: Воспроизведение
        AVFOutput->>RouteManager: playback_completed()
        RouteManager->>EventBus: audio.output.chunk_played
    else Output not ready
        SpeechPlayInt->>SpeechPlayInt: queue_chunk(audio_data)
        SpeechPlayInt->>RouteManagerInt: request_output_recreate()
        RouteManagerInt->>RouteManager: reconcile_routes()
        RouteManager->>OutputSM: transition_to(RECREATING)
        RouteManager->>AVFOutput: recreate_engine()
        AVFOutput->>AVAudioEngine: stop() + recreate()
        AVFOutput-->>RouteManager: engine_ready()
        RouteManager->>OutputSM: transition_to(READY)
        RouteManager->>SpeechPlayInt: output_ready()
        SpeechPlayInt->>AVFOutput: play_queued_chunks()
    end
```

---

## 🔄 Reconcile Loop (Центральная логика)

```mermaid
flowchart TD
    Start([Событие триггер]) --> CheckPending{Есть<br/>pending?}
    
    CheckPending -->|Да| Wait[Ждать завершения<br/>текущего reconcile]
    Wait --> CheckPending
    
    CheckPending -->|Нет| SingleFlight[Установить<br/>single-flight флаг]
    
    SingleFlight --> Snapshot[Создать Snapshot<br/>текущего состояния]
    
    Snapshot --> CheckDebounce{Debounce<br/>активен?}
    
    CheckDebounce -->|Да| DebounceWait[Ждать debounce<br/>таймаут]
    DebounceWait --> Snapshot
    
    CheckDebounce -->|Нет| GetDesired[Определить<br/>desired route]
    
    GetDesired --> MapInput[Маппинг input<br/>AVFoundation → PortAudio]
    
    MapInput --> Compare[Сравнить desired<br/>с active route]
    
    Compare --> Decision{Решение}
    
    Decision -->|Нет изменений| NoOp[NoOp<br/>Ничего не делать]
    
    Decision -->|Input изменился| RestartInput[Restart Input<br/>Перезапуск микрофона]
    
    Decision -->|Output изменился| RecreateOutput[Recreate Output<br/>Пересоздание engine]
    
    Decision -->|Оба изменились| RestartBoth[Restart Both<br/>Оба действия]
    
    RestartInput --> Apply[Применить решение]
    RecreateOutput --> Apply
    RestartBoth --> Apply
    NoOp --> EmitEvents
    
    Apply --> EmitEvents[Эмитировать события<br/>EventBus]
    
    EmitEvents --> ClearPending[Очистить pending флаг]
    
    ClearPending --> CheckNewEvents{Новые события<br/>во время reconcile?}
    
    CheckNewEvents -->|Да| SetPending[Установить pending<br/>и запустить новый reconcile]
    CheckNewEvents -->|Нет| End([Завершение])
    
    SetPending --> Snapshot
    
    style Snapshot fill:#e1f5ff
    style Decision fill:#fff4e1
    style Apply fill:#e8f5e9
    style EmitEvents fill:#ffebee
```

---

## 🔄 State Machines: Input

```mermaid
stateDiagram-v2
    [*] --> STOPPED
    
    STOPPED --> STARTING: start_request()
    STARTING --> ACTIVE: stream_opened()
    STARTING --> FAILED: timeout(2.5s) || error
    STARTING --> STOPPED: cancel_request()
    
    ACTIVE --> STOPPING: stop_request()
    ACTIVE --> FAILED: heartbeat_lost(10s) || error
    
    STOPPING --> STOPPED: stream_closed()
    STOPPING --> FAILED: error
    
    FAILED --> STARTING: retry(backoff: 1s→2s→4s)
    FAILED --> STOPPED: max_retries_exceeded()
    
    note right of STARTING
        Timeout: 2.5s
        Retries: 3
        Backoff: 1s → 2s → 4s
    end note
    
    note right of ACTIVE
        Heartbeat: каждые 10s
        Max restarts: 6 за 10 минут
    end note
```

---

## 🔄 State Machines: Output

```mermaid
stateDiagram-v2
    [*] --> READY
    
    READY --> RECREATING: device_changed() || error
    RECREATING --> READY: engine_recreated()
    RECREATING --> ERROR: timeout(1.5s) || error
    
    ERROR --> RECREATING: retry(backoff: 250ms→750ms)
    ERROR --> READY: max_retries_exceeded()
    
    note right of RECREATING
        Timeout: 1.5s
        Retries: 2
        Backoff: 250ms → 750ms
    end note
    
    note right of READY
        Queue: max 5MB, 5s
        Sample rate: 16kHz → 48kHz
    end note
```

---

## 🔄 EventBus: События RouteManager

```mermaid
graph LR
    subgraph "Input Events"
        IE1[audio.input.device_changed]
        IE2[audio.input.started]
        IE3[audio.input.stopped]
        IE4[audio.input.failed]
        IE5[audio.input.retry_scheduled]
    end
    
    subgraph "Output Events"
        OE1[audio.output.device_changed]
        OE2[audio.output.recreating]
        OE3[audio.output.ready]
        OE4[audio.output.failed]
        OE5[audio.output.chunk_played]
    end
    
    subgraph "Route Manager Events"
        RM1[audio.route.reconcile_started]
        RM2[audio.route.reconcile_completed]
        RM3[audio.route.decision]
        RM4[audio.route.mapping_result]
    end
    
    subgraph "System Events"
        SE1[permissions.first_run_started]
        SE2[permissions.restart_pending]
        SE3[app.update_in_progress]
        SE4[app.mode_changed]
        SE5[voice.recording_start]
        SE6[voice.recording_stop]
    end
    
    SE1 --> RM1
    SE2 --> RM1
    SE3 --> RM1
    SE4 --> RM1
    SE5 --> RM1
    SE6 --> RM1
    
    RM1 --> RM2
    RM2 --> RM3
    RM3 --> RM4
    
    RM3 --> IE2
    RM3 --> IE3
    RM3 --> IE4
    RM3 --> IE5
    
    RM3 --> OE2
    RM3 --> OE3
    RM3 --> OE4
    
    style RM1 fill:#e1f5ff
    style RM2 fill:#fff4e1
    style RM3 fill:#e8f5e9
```

---

## 🔄 Интеграция с существующими модулями

```mermaid
graph TB
    subgraph "Existing Integrations"
        InputProc[InputProcessingIntegration]
        ModeMgmt[ModeManagementIntegration]
        TrayCtrl[TrayControllerIntegration]
        InterruptMgmt[InterruptManagementIntegration]
        PermissionRestart[PermissionRestartIntegration]
        FirstRun[FirstRunPermissionsIntegration]
        Updater[UpdaterIntegration]
    end
    
    subgraph "New Audio System"
        RouteManagerInt[AudioRouteManagerIntegration]
        VoiceRecInt[VoiceRecognitionIntegration<br/>Адаптированная]
        SpeechPlayInt[SpeechPlaybackIntegration<br/>Адаптированная]
    end
    
    subgraph "EventBus"
        EB[EventBus]
    end
    
    subgraph "Blocking Conditions"
        BC1[first_run: true]
        BC2[restart_pending: true]
        BC3[update_in_progress: true]
    end
    
    %% Blocking conditions
    FirstRun --> BC1
    PermissionRestart --> BC2
    Updater --> BC3
    
    BC1 --> RouteManagerInt
    BC2 --> RouteManagerInt
    BC3 --> RouteManagerInt
    
    %% Event flows
    InputProc --> EB
    ModeMgmt --> EB
    TrayCtrl --> EB
    InterruptMgmt --> EB
    
    EB --> RouteManagerInt
    EB --> VoiceRecInt
    EB --> SpeechPlayInt
    
    RouteManagerInt --> VoiceRecInt
    RouteManagerInt --> SpeechPlayInt
    
    VoiceRecInt --> EB
    SpeechPlayInt --> EB
    
    style RouteManagerInt fill:#e1f5ff
    style BC1 fill:#ffebee
    style BC2 fill:#ffebee
    style BC3 fill:#ffebee
```

---

## 🔄 Device Monitoring: Двойной механизм

```mermaid
sequenceDiagram
    participant System as macOS System
    participant NSNotification as NSNotificationCenter
    participant AVFMonitor as AVFoundationMonitor
    participant PollingThread as Polling Thread
    participant RouteManager as RouteManager
    participant EventBus as EventBus
    
    Note over System,NSNotification: Instant Detection (Event-driven)
    System->>NSNotification: Device connected/disconnected
    NSNotification->>AVFMonitor: AVAudioSessionRouteChangeNotification
    AVFMonitor->>AVFMonitor: process_notification()
    AVFMonitor->>RouteManager: device_changed(signature)
    RouteManager->>EventBus: audio.input.device_changed
    
    Note over PollingThread,EventBus: Fallback Detection (Polling)
    loop Каждые 1-2 секунды
        PollingThread->>AVFMonitor: check_devices()
        AVFMonitor->>System: query_devices()
        System-->>AVFMonitor: [devices]
        AVFMonitor->>AVFMonitor: compare_with_cache()
        alt Изменение обнаружено
            AVFMonitor->>RouteManager: device_changed(signature)
            RouteManager->>EventBus: audio.input.device_changed
        end
    end
```

---

## 🔄 Device Mapping: AVFoundation → PortAudio

```mermaid
flowchart TD
    Start([AVFoundation Device]) --> Normalize[Нормализация имени<br/>удаление суффиксов]
    
    Normalize --> BuildSig[Построение<br/>DeviceSignature]
    
    BuildSig --> CheckCache{Кэш<br/>есть?}
    
    CheckCache -->|Да| CacheHit[Использовать<br/>кэшированный результат]
    CheckCache -->|Нет| SearchPA[Поиск в PortAudio<br/>по имени и channels]
    
    SearchPA --> Match{Совпадение<br/>найдено?}
    
    Match -->|Да| CalcConfidence[Вычислить<br/>Confidence]
    
    CalcConfidence --> Confidence{Confidence<br/>уровень?}
    
    Confidence -->|HIGH| UseIndex[Использовать<br/>device_index]
    Confidence -->|MEDIUM| UseIndex
    Confidence -->|LOW| UseDefault[Использовать<br/>system default]
    Confidence -->|NONE| UseDefault
    
    Match -->|Нет| UseDefault
    
    UseIndex --> CacheResult[Кэшировать<br/>результат]
    UseDefault --> CacheResult
    
    CacheHit --> Return[Вернуть<br/>MappingResult]
    CacheResult --> Return
    
    Return --> End([Конец])
    
    style BuildSig fill:#e1f5ff
    style CalcConfidence fill:#fff4e1
    style UseIndex fill:#e8f5e9
    style UseDefault fill:#ffebee
```

---

## 🔄 Decision Engine: Правила из interaction_matrix.yaml

```mermaid
flowchart TD
    Start([Snapshot состояния]) --> CheckFirstRun{first_run<br/>== true?}
    
    CheckFirstRun -->|Да| HardStop1[ABORT<br/>hard_stop]
    
    CheckFirstRun -->|Нет| CheckRestart{restart_pending<br/>== true?}
    
    CheckRestart -->|Да| HardStop2[ABORT<br/>hard_stop]
    
    CheckRestart -->|Нет| CheckUpdate{update_in_progress<br/>== true?}
    
    CheckUpdate -->|Да| HardStop3[ABORT<br/>hard_stop]
    
    CheckUpdate -->|Нет| CheckDeviceBusy{device.busy<br/>== true?}
    
    CheckDeviceBusy -->|Да| Retry[RETRY<br/>graceful + backoff]
    
    CheckDeviceBusy -->|Нет| CheckNetwork{network<br/>== offline?}
    
    CheckNetwork -->|Да| Degrade[DEGRADE<br/>graceful]
    
    CheckNetwork -->|Нет| CheckPermissions{permissions.mic<br/>== granted?}
    
    CheckPermissions -->|Нет| Abort[ABORT<br/>hard_stop]
    
    CheckPermissions -->|Да| CheckMode{appMode<br/>== LISTENING?}
    
    CheckMode -->|Нет| NoOp[NOOP<br/>не требуется действие]
    
    CheckMode -->|Да| Start[START<br/>начать listening]
    
    HardStop1 --> End([Решение])
    HardStop2 --> End
    HardStop3 --> End
    Retry --> End
    Degrade --> End
    Abort --> End
    NoOp --> End
    Start --> End
    
    style HardStop1 fill:#ffebee
    style HardStop2 fill:#ffebee
    style HardStop3 fill:#ffebee
    style Retry fill:#fff4e1
    style Degrade fill:#fff4e1
    style Start fill:#e8f5e9
```

---

## 🔄 Полный цикл: От события до действия

```mermaid
sequenceDiagram
    participant User as Пользователь/Система
    participant EventBus as EventBus
    participant RouteManagerInt as RouteManagerIntegration
    participant RouteManager as AudioRouteManager
    participant ReconcileEngine as ReconcileEngine
    participant DecisionEngine as DecisionEngine
    participant DebounceManager as DebounceManager
    participant DeviceMapper as DeviceMapper
    participant AVFMonitor as AVFoundationMonitor
    participant VoiceRecInt as VoiceRecognitionIntegration
    participant SpeechRecognizer as SpeechRecognizer
    
    User->>EventBus: Событие (device_changed / mode_changed / etc.)
    
    EventBus->>RouteManagerInt: audio.route.reconcile_requested
    
    RouteManagerInt->>RouteManager: reconcile_routes()
    
    RouteManager->>ReconcileEngine: create_snapshot()
    ReconcileEngine->>AVFMonitor: get_current_devices()
    AVFMonitor-->>ReconcileEngine: [DeviceSignature]
    ReconcileEngine-->>RouteManager: Snapshot
    
    RouteManager->>DebounceManager: should_debounce(device)
    DebounceManager-->>RouteManager: debounce_delay_ms
    
    alt Debounce активен
        RouteManager->>RouteManager: schedule_reconcile(delay)
        RouteManager-->>RouteManagerInt: reconcile_pending
    else Debounce неактивен
        RouteManager->>ReconcileEngine: determine_desired_route()
        ReconcileEngine->>DeviceMapper: map_to_portaudio(signature)
        DeviceMapper-->>ReconcileEngine: MappingResult
        ReconcileEngine-->>RouteManager: DesiredRoute
        
        RouteManager->>ReconcileEngine: compare_routes(desired, active)
        ReconcileEngine-->>RouteManager: RouteDiff
        
        RouteManager->>DecisionEngine: decide_action(snapshot, diff)
        DecisionEngine->>DecisionEngine: apply_rules(interaction_matrix)
        DecisionEngine-->>RouteManager: Decision(START/ABORT/RETRY/DEGRADE)
        
        RouteManager->>RouteManager: apply_decision(decision)
        
        alt Decision: START
            RouteManager->>VoiceRecInt: start_listening(device_index)
            VoiceRecInt->>SpeechRecognizer: start_listening(device_index)
            SpeechRecognizer-->>VoiceRecInt: listening_started
            VoiceRecInt-->>RouteManager: input_started
            RouteManager->>EventBus: audio.input.started
        else Decision: ABORT
            RouteManager->>EventBus: audio.input.aborted
        else Decision: RETRY
            RouteManager->>DebounceManager: schedule_retry(backoff)
            RouteManager->>EventBus: audio.input.retry_scheduled
        end
        
        RouteManager->>EventBus: audio.route.reconcile_completed
        RouteManager->>EventBus: audio.route.decision (с каноническим логом)
    end
```

---

## 📋 Ключевые принципы работы

### 1. Единственная точка решений
- **RouteManager** - единственный компонент, принимающий решения о маршрутизации
- Все события только триггерят `reconcile_routes()`
- Никакой логики на событиях напрямую

### 2. Single-flight механизм
- Одновременно выполняется только один reconcile
- Новые события → `pending = True`
- После завершения → reconcile с актуальным snapshot

### 3. Debounce per-device
- Bluetooth: 200ms → 1200ms (max)
- USB: 100ms → 600ms (max)
- Built-in: 100ms → 200ms (max)

### 4. Fallback стратегии
- Если AVFoundation недоступен → старая система (sounddevice)
- Если mapping LOW/NONE → system default
- Если устройство исчезло → последнее рабочее устройство

### 5. Блокировки
- `first_run: true` → hard_stop (блокирует RouteManager)
- `restart_pending: true` → hard_stop
- `update_in_progress: true` → hard_stop

### 6. Канонический формат логов
```
decision=<start|abort|retry|degrade> ctx={mic=...,screen=...,device=...,network=...,firstRun=...,appMode=...} source=route_manager duration_ms=<int>
```

---

## 🎯 Итоговая схема взаимодействия

```mermaid
graph TB
    subgraph "Trigger Layer"
        T1[Device Change]
        T2[Mode Change]
        T3[Permission Change]
        T4[Network Change]
    end
    
    subgraph "Route Manager Core"
        RM[AudioRouteManager]
        RE[ReconcileEngine]
        DE[DecisionEngine]
        DM[DebounceManager]
        MAP[DeviceMapper]
    end
    
    subgraph "State Machines"
        ISM[InputStateMachine]
        OSM[OutputStateMachine]
    end
    
    subgraph "Adapters"
        AVFM[AVFoundationMonitor]
        AVFO[AVFoundationOutput]
        GIN[GoogleInputController]
    end
    
    subgraph "Modules"
        SR[SpeechRecognizer]
        SP[SequentialPlayer]
    end
    
    T1 --> RM
    T2 --> RM
    T3 --> RM
    T4 --> RM
    
    RM --> RE
    RE --> MAP
    MAP --> AVFM
    RE --> DE
    DE --> DM
    
    DE --> ISM
    DE --> OSM
    
    ISM --> GIN
    GIN --> SR
    
    OSM --> AVFO
    AVFO --> SP
    
    style RM fill:#e1f5ff
    style RE fill:#fff4e1
    style DE fill:#e8f5e9
```

---

## ✅ Выводы

1. **Централизованное управление**: RouteManager - единственная точка решений
2. **Event-driven архитектура**: Все через EventBus
3. **Reconcile loop**: Постоянное сравнение desired vs active
4. **Fallback стратегии**: На каждом уровне
5. **Блокировки**: Критические состояния блокируют RouteManager
6. **Debounce**: Per-device задержки для стабильности
7. **State machines**: Четкие переходы состояний
8. **Канонические логи**: Единый формат для всех решений

---

**Эта схема служит основой для реализации всех компонентов.**

