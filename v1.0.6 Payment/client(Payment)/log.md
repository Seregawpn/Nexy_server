ed=False (было True)
2025-12-02 20:27:06,518 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔄 [RESET] Деактивация комбинации: control_pressed=False, n_pressed=False
2025-12-02 20:27:06,518 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔑 Combo deactivation: короткое нажатие, генерируем SHORT_PRESS
2025-12-02 20:27:06,518 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔑 _trigger_event: type=short_press, duration=0.088s, thread=MainThread
2025-12-02 20:27:06,518 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔑 _run_callback: short_press, callback=_handle_short_press
🔑 _run_callback: short_press, callback=_handle_short_press
2025-12-02 20:27:06,518 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔑 _trigger_event: type=release, duration=0.088s, thread=MainThread
2025-12-02 20:27:06,519 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔑 Выполняем async callback в loop: short_press (loop=4700916624, running=True)
🔑 Выполняем async callback в loop: short_press (loop=4700916624, running=True)
2025-12-02 20:27:06,519 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔑 _run_callback: release, callback=_handle_key_release
🔑 _run_callback: release, callback=_handle_key_release
2025-12-02 20:27:06,520 - integration.integrations.input_processing_integration - DEBUG - 🔑 SHORT_PRESS: 0.088с
2025-12-02 20:27:06,521 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔑 Выполняем async callback в loop: release (loop=4700916624, running=True)
🔑 Выполняем async callback в loop: release (loop=4700916624, running=True)
2025-12-02 20:27:06,521 - integration.integrations.input_processing_integration - INFO - 🛑 SHORT_PRESS без записи - отменяем pending session 1764725226.4302258
2025-12-02 20:27:06,526 - integration.integrations.input_processing_integration - INFO - 🛑 SHORT_PRESS: проверка прерывания (mode=AppMode.PROCESSING, playback_active=False, grpc_session=1764725212.421291, should_interrupt=True)
2025-12-02 20:27:06,526 - integration.integrations.input_processing_integration - INFO - 🛑 SHORT_PRESS: МГНОВЕННО прерываем воспроизведение (mode=AppMode.PROCESSING, playback_active=False, grpc_session=1764725212.421291)
2025-12-02 20:27:06,527 - integration.core.event_bus - DEBUG - EventBus: dispatch 'playback.cancelled' to 3 subscriber(s)
2025-12-02 20:27:06,527 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'playback.cancelled': <bound method SpeechPlaybackIntegration._on_unified_interrupt of <integration.integrations.speech_playback_integration.SpeechPlaybackIntegration object at 0x1183c0980>>
2025-12-02 20:27:06,527 - integration.integrations.speech_playback_integration - INFO - SpeechPlayback: ЕДИНЫЙ канал прерывания, source=input_processing, reason=keyboard
2025-12-02 20:27:06,527 - integration.integrations.speech_playback_integration - DEBUG - SpeechPlayback: воспроизведение уже остановлено (state=PlaybackState.IDLE)
2025-12-02 20:27:06,527 - integration.integrations.speech_playback_integration - INFO - SpeechPlayback: прерывание обработано через ЕДИНЫЙ канал
2025-12-02 20:27:06,527 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'playback.cancelled': <bound method InputProcessingIntegration._on_playback_finished of <integration.integrations.input_processing_integration.InputProcessingIntegration object at 0x118321e80>>
2025-12-02 20:27:06,527 - integration.integrations.input_processing_integration - DEBUG - PLAYBACK: finished (event=playback.cancelled, session=1764725212.421291)
2025-12-02 20:27:06,527 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'playback.cancelled': <bound method SignalIntegration._on_playback_cancelled of <integration.integrations.signal_integration.SignalIntegration object at 0x1183c0d70>>
2025-12-02 20:27:06,527 - integration.integrations.signal_integration - DEBUG - Signals: CANCEL skipped (reason=keyboard)
2025-12-02 20:27:06,528 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: playback.cancelled
2025-12-02 20:27:06,528 - integration.integrations.input_processing_integration - INFO - 🛑 SHORT_PRESS: playback.cancelled опубликовано НАПРЯМУЮ для мгновенного прерывания
2025-12-02 20:27:06,528 - integration.core.event_bus - DEBUG - EventBus: dispatch 'interrupt.request' to 4 subscriber(s)
2025-12-02 20:27:06,528 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'interrupt.request': <bound method ListeningWorkflow._on_interrupt_request of <integration.workflows.listening_workflow.ListeningWorkflow object at 0x1183c1e80>>
2025-12-02 20:27:06,528 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'interrupt.request': <bound method ProcessingWorkflow._on_interrupt_request of <integration.workflows.processing_workflow.ProcessingWorkflow object at 0x1183c1fd0>>
2025-12-02 20:27:06,528 - integration.workflows.processing_workflow - INFO - ⚙️ ProcessingWorkflow: получен запрос ПРЕРЫВАНИЯ, reason=user_interrupt, stage=capturing, active=True
2025-12-02 20:27:06,528 - integration.workflows.processing_workflow - INFO - ⚙️ ProcessingWorkflow: отменяем gRPC запрос
2025-12-02 20:27:06,528 - integration.core.event_bus - DEBUG - EventBus: dispatch 'grpc.request_cancel' to 2 subscriber(s)
2025-12-02 20:27:06,528 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'grpc.request_cancel': <bound method SpeechPlaybackIntegration._on_grpc_cancel of <integration.integrations.speech_playback_integration.SpeechPlaybackIntegration object at 0x1183c0980>>
2025-12-02 20:27:06,528 - integration.integrations.speech_playback_integration - INFO - SpeechPlayback: получен grpc.request_cancel — очищаем буфер
2025-12-02 20:27:06,528 - modules.speech_playback.core.buffer - INFO - 🧹 Очередь очищена: 0 чанков
2025-12-02 20:27:06,528 - modules.speech_playback.core.buffer - INFO - 🧹 Буфер воспроизведения очищен: 0 фреймов
2025-12-02 20:27:06,528 - modules.speech_playback.core.buffer - INFO - 🧹 Все буферы очищены
2025-12-02 20:27:06,528 - modules.speech_playback.core.player - WARNING - ⚠️ Невозможно остановить воспроизведение в текущем состоянии
2025-12-02 20:27:06,528 - integration.core.event_bus - DEBUG - EventBus: dispatch 'playback.cancelled' to 3 subscriber(s)
2025-12-02 20:27:06,528 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'playback.cancelled': <bound method SpeechPlaybackIntegration._on_unified_interrupt of <integration.integrations.speech_playback_integration.SpeechPlaybackIntegration object at 0x1183c0980>>
2025-12-02 20:27:06,528 - integration.integrations.speech_playback_integration - INFO - SpeechPlayback: ЕДИНЫЙ канал прерывания, source=grpc_cancel, reason=interrupt
2025-12-02 20:27:06,528 - integration.integrations.speech_playback_integration - DEBUG - SpeechPlayback: воспроизведение уже остановлено (state=PlaybackState.IDLE)
2025-12-02 20:27:06,528 - integration.integrations.speech_playback_integration - INFO - SpeechPlayback: прерывание обработано через ЕДИНЫЙ канал
2025-12-02 20:27:06,528 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'playback.cancelled': <bound method InputProcessingIntegration._on_playback_finished of <integration.integrations.input_processing_integration.InputProcessingIntegration object at 0x118321e80>>
2025-12-02 20:27:06,528 - integration.integrations.input_processing_integration - DEBUG - PLAYBACK: finished (event=playback.cancelled, session=1764725212.421291)
2025-12-02 20:27:06,528 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'playback.cancelled': <bound method SignalIntegration._on_playback_cancelled of <integration.integrations.signal_integration.SignalIntegration object at 0x1183c0d70>>
2025-12-02 20:27:06,528 - integration.integrations.signal_integration - DEBUG - Signals: CANCEL skipped (reason=grpc_cancel)
2025-12-02 20:27:06,528 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: playback.cancelled
2025-12-02 20:27:06,528 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'grpc.request_cancel': <bound method GrpcClientIntegration._on_request_cancel of <integration.integrations.grpc_client_integration.GrpcClientIntegration object at 0x118323e00>>
2025-12-02 20:27:06,528 - integration.integrations.grpc_client_integration - INFO - grpc.request_cancel: no inflight request to cancel (noop)
2025-12-02 20:27:06,528 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: grpc.request_cancel
2025-12-02 20:27:06,528 - integration.workflows.processing_workflow - INFO - ⚙️ ProcessingWorkflow: останавливаем воспроизведение через ЕДИНЫЙ канал
2025-12-02 20:27:06,529 - integration.core.event_bus - DEBUG - EventBus: dispatch 'playback.cancelled' to 3 subscriber(s)
2025-12-02 20:27:06,529 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'playback.cancelled': <bound method SpeechPlaybackIntegration._on_unified_interrupt of <integration.integrations.speech_playback_integration.SpeechPlaybackIntegration object at 0x1183c0980>>
2025-12-02 20:27:06,529 - integration.integrations.speech_playback_integration - INFO - SpeechPlayback: ЕДИНЫЙ канал прерывания, source=processing_workflow, reason=user_interrupt
2025-12-02 20:27:06,529 - integration.integrations.speech_playback_integration - DEBUG - SpeechPlayback: воспроизведение уже остановлено (state=PlaybackState.IDLE)
2025-12-02 20:27:06,529 - integration.integrations.speech_playback_integration - INFO - SpeechPlayback: прерывание обработано через ЕДИНЫЙ канал
2025-12-02 20:27:06,529 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'playback.cancelled': <bound method InputProcessingIntegration._on_playback_finished of <integration.integrations.input_processing_integration.InputProcessingIntegration object at 0x118321e80>>
2025-12-02 20:27:06,529 - integration.integrations.input_processing_integration - DEBUG - PLAYBACK: finished (event=playback.cancelled, session=None)
2025-12-02 20:27:06,529 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'playback.cancelled': <bound method SignalIntegration._on_playback_cancelled of <integration.integrations.signal_integration.SignalIntegration object at 0x1183c0d70>>
2025-12-02 20:27:06,529 - integration.integrations.signal_integration - INFO - Signals: CANCEL (playback.cancelled)
2025-12-02 20:27:06,533 - integration.core.event_bus - DEBUG - EventBus: dispatch 'playback.signal' to 1 subscriber(s)
2025-12-02 20:27:06,533 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'playback.signal': <bound method SpeechPlaybackIntegration._on_playback_signal of <integration.integrations.speech_playback_integration.SpeechPlaybackIntegration object at 0x1183c0980>>
2025-12-02 20:27:06,533 - integration.integrations.speech_playback_integration - INFO - 🔔 playback.signal: pattern=cancel, bytes=11520, sr=48000, ch=1, gain=1.0, prio=0
2025-12-02 20:27:06,533 - modules.speech_playback.core.player - INFO - 🎯 [AUDIO_REFACTOR] Начало инициализации Sequential Speech Player...
2025-12-02 20:27:06,533 - modules.speech_playback.core.player - DEBUG - 🔍 [AUDIO_DEBUG] Инициализация Core Audio Manager...
2025-12-02 20:27:06,533 - modules.speech_playback.macos.core_audio - INFO - ✅ Core Audio инициализирован
2025-12-02 20:27:06,533 - modules.speech_playback.core.player - INFO - ✅ [AUDIO_SUCCESS] Core Audio Manager инициализирован
2025-12-02 20:27:06,533 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Запрашиваем системное default output устройство...
2025-12-02 20:27:06,533 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] ШАГ 1.2: Определение устройства через macOS API (приоритет 1)
2025-12-02 20:27:06,533 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Используем SwitchAudioSource: /opt/homebrew/bin/SwitchAudioSource
2025-12-02 20:27:06,533 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Запрос текущего default output устройства...
I0000 00:00:1764725226.534366 4787285 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-02 20:27:06,587 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 [TAP] KeyUp: N (keycode=45)
2025-12-02 20:27:06,669 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Команда выполнена: returncode=0, stdout_len=94, stderr_len=0
2025-12-02 20:27:06,671 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Получен JSON: {'name': 'MacBook Air Speakers', 'type': 'output', 'id': '71', 'uid': 'BuiltInSpeakerDevice'}
2025-12-02 20:27:06,672 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] macOS default OUTPUT (через SwitchAudioSource): "MacBook Air Speakers"
2025-12-02 20:27:06,672 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Успешно получено имя устройства: MacBook Air Speakers
2025-12-02 20:27:06,672 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] macOS default OUTPUT (источник истины): "MacBook Air Speakers"
2025-12-02 20:27:06,672 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Найден ID для 'MacBook Air Speakers': 4
2025-12-02 20:27:06,672 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Найдено устройство через SwitchAudioSource: name=MacBook Air Speakers, id=4
2025-12-02 20:27:06,672 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Найдено default output устройство (через SwitchAudioSource):
2025-12-02 20:27:06,672 - modules.speech_playback.core.player - INFO -    Name: MacBook Air Speakers
2025-12-02 20:27:06,672 - modules.speech_playback.core.player - INFO -    Index: 4
2025-12-02 20:27:06,672 - modules.speech_playback.core.player - INFO -    Max Output Channels: 2
2025-12-02 20:27:06,672 - modules.speech_playback.core.player - INFO -    Default Sample Rate: 48000.0 Hz
2025-12-02 20:27:06,672 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Полная информация: {'name': 'MacBook Air Speakers', 'index': 4, 'hostapi': 0, 'max_input_channels': 0, 'max_output_channels': 2, 'default_low_input_latency': 0.01, 'default_low_output_latency': 0.015166666666666667, 'default_high_input_latency': 0.1, 'default_high_output_latency': 0.0245, 'default_samplerate': 48000.0}
2025-12-02 20:27:06,672 - modules.speech_playback.core.player - INFO - 🎯 Используем системное устройство по умолчанию от macOS
2025-12-02 20:27:06,672 - modules.speech_playback.core.player - INFO - 📊 [AUDIO_STATS] Конфигурация плеера: sample_rate=48000Hz, channels=2, dtype=int16
2025-12-02 20:27:06,673 - modules.speech_playback.macos.performance - INFO - ✅ Мониторинг производительности запущен
2025-12-02 20:27:06,673 - modules.speech_playback.core.player - INFO - ✅ [AUDIO_SUCCESS] Sequential Speech Player инициализирован успешно
2025-12-02 20:27:06,673 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] _start_audio_stream вызван: sync_output=True, device_id=None
2025-12-02 20:27:06,673 - modules.speech_playback.core.player - WARNING - ⚠️ [OUTPUT] Обнаружен существующий поток при создании нового, закрываем...
2025-12-02 20:27:06,673 - modules.speech_playback.core.player - WARNING - ⚠️ [OUTPUT] Существующий поток: active=False, started=False
2025-12-02 20:27:06,673 - modules.speech_playback.core.player - DEBUG - 🔄 [OUTPUT] Закрываем неактивный поток...
2025-12-02 20:27:06,674 - modules.speech_playback.core.player - DEBUG - ✅ [OUTPUT] Старый поток полностью освобожден (active=False, ожидание: 0.000с)
2025-12-02 20:27:06,674 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Старый поток закрыт и освобожден (ожидание: 0.000с)
2025-12-02 20:27:06,779 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Текущая конфигурация: rate=48000Hz, channels=2, dtype=int16, buffer_size=512
2025-12-02 20:27:06,779 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Синхронизируем формат с устройством...
2025-12-02 20:27:06,779 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Запрашиваем системное default output устройство...
2025-12-02 20:27:06,779 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] ШАГ 1.2: Определение устройства через macOS API (приоритет 1)
2025-12-02 20:27:06,779 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Используем SwitchAudioSource: /opt/homebrew/bin/SwitchAudioSource
2025-12-02 20:27:06,779 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Запрос текущего default output устройства...
I0000 00:00:1764725226.779892 4787285 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-02 20:27:06,865 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Команда выполнена: returncode=0, stdout_len=94, stderr_len=0
2025-12-02 20:27:06,866 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Получен JSON: {'name': 'MacBook Air Speakers', 'type': 'output', 'id': '71', 'uid': 'BuiltInSpeakerDevice'}
2025-12-02 20:27:06,866 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] macOS default OUTPUT (через SwitchAudioSource): "MacBook Air Speakers"
2025-12-02 20:27:06,866 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Успешно получено имя устройства: MacBook Air Speakers
2025-12-02 20:27:06,866 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] macOS default OUTPUT (источник истины): "MacBook Air Speakers"
2025-12-02 20:27:06,866 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Найден ID для 'MacBook Air Speakers': 4
2025-12-02 20:27:06,866 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Найдено устройство через SwitchAudioSource: name=MacBook Air Speakers, id=4
2025-12-02 20:27:06,866 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Найдено default output устройство (через SwitchAudioSource):
2025-12-02 20:27:06,866 - modules.speech_playback.core.player - INFO -    Name: MacBook Air Speakers
2025-12-02 20:27:06,867 - modules.speech_playback.core.player - INFO -    Index: 4
2025-12-02 20:27:06,867 - modules.speech_playback.core.player - INFO -    Max Output Channels: 2
2025-12-02 20:27:06,867 - modules.speech_playback.core.player - INFO -    Default Sample Rate: 48000.0 Hz
2025-12-02 20:27:06,867 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Полная информация: {'name': 'MacBook Air Speakers', 'index': 4, 'hostapi': 0, 'max_input_channels': 0, 'max_output_channels': 2, 'default_low_input_latency': 0.01, 'default_low_output_latency': 0.015166666666666667, 'default_high_input_latency': 0.1, 'default_high_output_latency': 0.0245, 'default_samplerate': 48000.0}
2025-12-02 20:27:06,867 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] После синхронизации: rate=48000Hz, channels=2
2025-12-02 20:27:06,867 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] device_id не передан, получаем устройство через macOS API (SwitchAudioSource)...
2025-12-02 20:27:06,867 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Fallback на SwitchAudioSource (device_id не передан)
2025-12-02 20:27:06,867 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Запрашиваем системное default output устройство...
2025-12-02 20:27:06,867 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] ШАГ 1.2: Определение устройства через macOS API (приоритет 1)
2025-12-02 20:27:06,867 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Используем SwitchAudioSource: /opt/homebrew/bin/SwitchAudioSource
2025-12-02 20:27:06,867 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Запрос текущего default output устройства...
I0000 00:00:1764725226.868216 4787285 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-02 20:27:06,953 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Команда выполнена: returncode=0, stdout_len=94, stderr_len=0
2025-12-02 20:27:06,953 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Получен JSON: {'name': 'MacBook Air Speakers', 'type': 'output', 'id': '71', 'uid': 'BuiltInSpeakerDevice'}
2025-12-02 20:27:06,954 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] macOS default OUTPUT (через SwitchAudioSource): "MacBook Air Speakers"
2025-12-02 20:27:06,954 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Успешно получено имя устройства: MacBook Air Speakers
2025-12-02 20:27:06,954 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] macOS default OUTPUT (источник истины): "MacBook Air Speakers"
2025-12-02 20:27:06,954 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Найден ID для 'MacBook Air Speakers': 4
2025-12-02 20:27:06,954 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Найдено устройство через SwitchAudioSource: name=MacBook Air Speakers, id=4
2025-12-02 20:27:06,955 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Найдено default output устройство (через SwitchAudioSource):
2025-12-02 20:27:06,955 - modules.speech_playback.core.player - INFO -    Name: MacBook Air Speakers
2025-12-02 20:27:06,955 - modules.speech_playback.core.player - INFO -    Index: 4
2025-12-02 20:27:06,955 - modules.speech_playback.core.player - INFO -    Max Output Channels: 2
2025-12-02 20:27:06,955 - modules.speech_playback.core.player - INFO -    Default Sample Rate: 48000.0 Hz
2025-12-02 20:27:06,955 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Полная информация: {'name': 'MacBook Air Speakers', 'index': 4, 'hostapi': 0, 'max_input_channels': 0, 'max_output_channels': 2, 'default_low_input_latency': 0.01, 'default_low_output_latency': 0.015166666666666667, 'default_high_input_latency': 0.1, 'default_high_output_latency': 0.0245, 'default_samplerate': 48000.0}
2025-12-02 20:27:06,955 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] macOS API (источник истины): "MacBook Air Speakers" (ID=4)
2025-12-02 20:27:06,955 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Обычное устройство: используем ID=4
2025-12-02 20:27:06,955 - modules.audio_core.device_params_normalizer - DEBUG - ✅ [OUTPUT] Нормализовано: "MacBook Air Speakers" → 48000 Hz, 2 ch
2025-12-02 20:27:06,955 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Нормализованные параметры для "MacBook Air Speakers":
2025-12-02 20:27:06,956 - modules.speech_playback.core.player - INFO -    Sample Rate: 48000 → 48000 Hz
2025-12-02 20:27:06,956 - modules.speech_playback.core.player - INFO -    Channels: 2
2025-12-02 20:27:06,956 - modules.speech_playback.core.stream_config_resolver - DEBUG - 🔧 [OUTPUT] Обычное устройство: используем все параметры (device=4, channels=1, blocksize=512)
2025-12-02 20:27:06,956 - modules.speech_playback.core.player - DEBUG - 🔧 [OUTPUT] Обычное устройство: используем все параметры (device=4, channels=1, blocksize=512)
2025-12-02 20:27:06,956 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Конфигурация потока:
2025-12-02 20:27:06,956 - modules.speech_playback.core.player - INFO -    device: 4
2025-12-02 20:27:06,956 - modules.speech_playback.core.player - INFO -    channels: 1
2025-12-02 20:27:06,956 - modules.speech_playback.core.player - INFO -    dtype: int16
2025-12-02 20:27:06,956 - modules.speech_playback.core.player - INFO -    samplerate: 48000 Hz
2025-12-02 20:27:06,956 - modules.speech_playback.core.player - INFO -    blocksize: 512
2025-12-02 20:27:06,956 - modules.speech_playback.core.player - INFO -    latency: N/A (не задан, пусть PortAudio выберет)
2025-12-02 20:27:06,956 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Создаём поток для устройства: MacBook Air Speakers (ID=4)
2025-12-02 20:27:06,956 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Проверяем доступность устройства ID 4...
2025-12-02 20:27:06,956 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Проверка доступности устройства ID 4...
2025-12-02 20:27:06,956 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Получаем список всех устройств...
2025-12-02 20:27:06,956 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Всего устройств в системе: 5
2025-12-02 20:27:06,956 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Запрашиваем информацию об устройстве ID 4...
2025-12-02 20:27:06,956 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] sd.query_devices() завершён для ID 4
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Информация об устройстве получена: MacBook Air Speakers
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - DEBUG -    Index: 4
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - DEBUG -    Max Input Channels: 0
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - DEBUG -    Max Output Channels: 2
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - DEBUG -    Default Sample Rate: 48000.0 Hz
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - DEBUG -    Host API: 0
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Устройство ID 4 (MacBook Air Speakers) доступно:
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - INFO -    Sample Rate: 48000.0 Hz
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - INFO -    Max Output Channels: 2
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Результат проверки доступности: True
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Устройство MacBook Air Speakers (ID=4) доступно
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Начинаем создание потока (max_retries=5, base_delay=0.3s, BT=False)...
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Подтверждение: старый поток полностью закрыт (_audio_stream=None)
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Подтверждение: старый поток закрыт → создаём новый stream
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - INFO -    Устройство: MacBook Air Speakers (ID=4, BT=False)
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - INFO -    Параметры: device=4, channels=1, samplerate=48000, blocksize=512, latency=N/A
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Попытка 1/5 создания потока...
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Параметры потока: {'device': 4, 'channels': 1, 'dtype': 'int16', 'samplerate': 48000, 'blocksize': 512, 'callback': <bound method SequentialSpeechPlayer._audio_callback of <modules.speech_playback.core.player.SequentialSpeechPlayer object at 0x118389fd0>>}
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Попытка 2/5 создания потока...
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Параметры потока: {'device': 4, 'channels': 1, 'dtype': 'int16', 'samplerate': 48000, 'blocksize': 512, 'callback': <bound method SequentialSpeechPlayer._audio_callback of <modules.speech_playback.core.player.SequentialSpeechPlayer object at 0x118389fd0>>}
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Попытка 3/5 создания потока...
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Параметры потока: {'device': 4, 'channels': 1, 'dtype': 'int16', 'samplerate': 48000, 'blocksize': 512, 'callback': <bound method SequentialSpeechPlayer._audio_callback of <modules.speech_playback.core.player.SequentialSpeechPlayer object at 0x118389fd0>>}
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Попытка 4/5 создания потока...
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Параметры потока: {'device': 4, 'channels': 1, 'dtype': 'int16', 'samplerate': 48000, 'blocksize': 512, 'callback': <bound method SequentialSpeechPlayer._audio_callback of <modules.speech_playback.core.player.SequentialSpeechPlayer object at 0x118389fd0>>}
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Попытка 5/5 создания потока...
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Параметры потока: {'device': 4, 'channels': 1, 'dtype': 'int16', 'samplerate': 48000, 'blocksize': 512, 'callback': <bound method SequentialSpeechPlayer._audio_callback of <modules.speech_playback.core.player.SequentialSpeechPlayer object at 0x118389fd0>>}
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Последний host error code: 0
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Создаем новый поток через AudioStreamManager: device=4, BT=False
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Запускаем create_stream (_start_audio_stream) в отдельном thread (timeout=3.0с)...
2025-12-02 20:27:06,958 - asyncio - DEBUG - Using selector: KqueueSelector
2025-12-02 20:27:06,958 - modules.audio_core.stream_manager - INFO - 🔍 [OUTPUT] create_stream ВХОД: device=4 (MacBook Air Speakers), BT=False, max_retries=2
2025-12-02 20:27:06,958 - modules.audio_core.stream_manager - DEBUG - 🔍 [OUTPUT] create_stream: пытаемся захватить lock...
2025-12-02 20:27:06,958 - modules.audio_core.stream_manager - DEBUG - ✅ [OUTPUT] create_stream: lock захвачен (время ожидания: 0.0ms), начинаем создание потока
2025-12-02 20:27:06,958 - modules.audio_core.stream_manager - DEBUG - 🔒 [OUTPUT] Закрытие потока...
2025-12-02 20:27:06,958 - modules.audio_core.stream_manager - DEBUG - ⏳ [OUTPUT] Задержка после закрытия: 0.3с (BT=False)
2025-12-02 20:27:07,265 - modules.audio_core.stream_manager - DEBUG - ✅ [OUTPUT] Поток успешно закрыт
2025-12-02 20:27:07,266 - modules.audio_core.stream_manager - INFO - 🔄 [OUTPUT] Попытка 1/2 создания потока:
   device_id=4, device_name=MacBook Air Speakers
   samplerate=48000Hz, channels=1
   dtype=int16, blocksize=512, latency=None
   is_bluetooth=False, callback=True
2025-12-02 20:27:07,267 - modules.audio_core.stream_manager - DEBUG - 🔍 [OUTPUT] Подготавливаем параметры потока...
2025-12-02 20:27:07,267 - modules.audio_core.stream_manager - DEBUG - 🔍 [OUTPUT] Параметры подготовлены: {'device': 4, 'samplerate': 48000, 'channels': 1, 'dtype': 'int16', 'callback': <bound method SequentialSpeechPlayer._audio_callback of <modules.speech_playback.core.player.SequentialSpeechPlayer object at 0x118389fd0>>, 'blocksize': 512}
2025-12-02 20:27:07,267 - modules.audio_core.stream_manager - DEBUG - 🔍 [OUTPUT] Создаем output поток через PortAudio...
2025-12-02 20:27:07,299 - modules.audio_core.stream_manager - DEBUG - ✅ [OUTPUT] Поток создан через PortAudio: <sounddevice.OutputStream object at 0x118589950>
2025-12-02 20:27:07,300 - modules.audio_core.stream_manager - INFO - ✅ [OUTPUT] Поток создан успешно на попытке 1 (время: 342.4ms)
2025-12-02 20:27:07,305 - modules.speech_playback.core.player - DEBUG - ✅ [OUTPUT] create_stream (_start_audio_stream) завершен успешно
2025-12-02 20:27:07,312 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Аудио поток создан успешно! (время создания: 0.35с)
2025-12-02 20:27:07,312 - modules.speech_playback.core.player - INFO -    Устройство: MacBook Air Speakers (ID=4, BT=False)
2025-12-02 20:27:07,313 - modules.speech_playback.core.player - INFO -    Параметры: channels=1, samplerate=48000Hz, dtype=int16, blocksize=512, latency=N/A
2025-12-02 20:27:07,313 - modules.speech_playback.core.player - INFO -    Задержки: prestart=0с, backoff=4.8с
2025-12-02 20:27:07,314 - modules.speech_playback.core.player - INFO - 💾 [OUTPUT] Сохранена безопасная конфигурация после успешного создания потока (попытка 5)
2025-12-02 20:27:07,314 - modules.speech_playback.core.player - DEBUG - 💡 Поток будет стартован при появлении первого чанка (lazy start)
2025-12-02 20:27:07,314 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Стартуем поток: stream exists=True, started=False
2025-12-02 20:27:07,352 - modules.speech_playback.core.player - INFO - ▶️ Аудио поток стартован (lazy start)
2025-12-02 20:27:07,352 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Поток стартован: active=True
2025-12-02 20:27:07,353 - modules.speech_playback.core.player - INFO - 🔄 Playback loop запущен
2025-12-02 20:27:07,353 - modules.speech_playback.core.player - INFO - 🎵 Воспроизведение запущено
2025-12-02 20:27:07,353 - integration.core.event_bus - DEBUG - EventBus: dispatch 'playback.started' to 2 subscriber(s)
2025-12-02 20:27:07,354 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'playback.started': <bound method ProcessingWorkflow._on_playback_started of <integration.workflows.processing_workflow.ProcessingWorkflow object at 0x1183c1fd0>>
2025-12-02 20:27:07,354 - integration.workflows.processing_workflow - INFO - 🔊 ProcessingWorkflow: воспроизведение началось
2025-12-02 20:27:07,354 - integration.workflows.processing_workflow - INFO - ⚙️ ProcessingWorkflow: переход capturing → playing_audio
2025-12-02 20:27:07,354 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'playback.started': <bound method InputProcessingIntegration._on_playback_started of <integration.integrations.input_processing_integration.InputProcessingIntegration object at 0x118321e80>>
2025-12-02 20:27:07,354 - integration.integrations.input_processing_integration - DEBUG - PLAYBACK: started (session=None)
2025-12-02 20:27:07,355 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: playback.started
2025-12-02 20:27:07,355 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Проверка устройства: session=None, started=True, time_since_check=1.29s
2025-12-02 20:27:07,355 - modules.speech_playback.core.player - INFO - 🔊 [OUTPUT] Начальное устройство: "Sergiy’s AirPods" (BT=True)
2025-12-02 20:27:07,356 - modules.speech_playback.core.player - DEBUG - 🔧 [CALLBACK] Конвертировано 1 каналов → 1 каналов: shape=(512, 1)
2025-12-02 20:27:07,356 - modules.speech_playback.core.player - DEBUG - 🔄 Моно аудио будет воспроизведено на 2 каналах
2025-12-02 20:27:07,358 - modules.speech_playback.core.buffer - INFO - ✅ Чанк добавлен: chunk_3_1764725227358 (size: 5760, queue: 1)
2025-12-02 20:27:07,358 - modules.speech_playback.core.player - DEBUG - ✅ [OUTPUT] Поток уже стартован
2025-12-02 20:27:07,358 - modules.speech_playback.core.player - INFO - ✅ Аудио данные добавлены: chunk_3_1764725227358 (size: 5760)
2025-12-02 20:27:07,358 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: playback.signal
2025-12-02 20:27:07,358 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: playback.cancelled
2025-12-02 20:27:07,358 - integration.workflows.processing_workflow - INFO - ⚙️ ProcessingWorkflow: возврат в SLEEPING, reason=interrupted
2025-12-02 20:27:07,359 - integration.core.event_bus - DEBUG - EventBus: dispatch 'mode.request' to 1 subscriber(s)
2025-12-02 20:27:07,360 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'mode.request': <bound method ModeManagementIntegration._on_mode_request of <integration.integrations.mode_management_integration.ModeManagementIntegration object at 0x1183238c0>>
2025-12-02 20:27:07,360 - integration.integrations.mode_management_integration - INFO - 🔄 MODE_REQUEST: target=AppMode.SLEEPING, source=ProcessingWorkflow.processing_interrupted, session_id=None, priority=90
2025-12-02 20:27:07,364 - integration.integrations.mode_management_integration - WARNING - MODE_REQUEST: target=AppMode.SLEEPING not in allowed modes, ignoring
2025-12-02 20:27:07,364 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: mode.request
2025-12-02 20:27:07,365 - integration.workflows.base_workflow - DEBUG - 🔄 ProcessingWorkflow: запрос смены режима sleeping
2025-12-02 20:27:07,365 - integration.workflows.processing_workflow - DEBUG - ⚙️ ProcessingWorkflow: состояние очищено
2025-12-02 20:27:07,365 - modules.speech_playback.core.player - DEBUG - 🔧 [CALLBACK] Конвертировано 1 каналов → 1 каналов: shape=(512, 1)
2025-12-02 20:27:07,408 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'interrupt.request': <bound method InterruptManagementIntegration._on_interrupt_request of <integration.integrations.interrupt_management_integration.InterruptManagementIntegration object at 0x118323230>>
2025-12-02 20:27:07,408 - modules.speech_playback.core.buffer - DEBUG - 🔍 Получен чанк: chunk_3_1764725227358
2025-12-02 20:27:07,409 - modules.speech_playback.core.buffer - INFO - ✅ Чанк добавлен в буфер: chunk_3_1764725227358 (frames: 5760, buffer: 0 → 5760, ch=2)
2025-12-02 20:27:07,409 - integration.integrations.interrupt_management_integration - WARNING - ⚠️ Неизвестный тип прерывания: interrupt.request, используем SESSION_CLEAR
2025-12-02 20:27:07,413 - modules.interrupt_management.core.interrupt_coordinator - INFO - 🔄 Запуск прерывания session_clear (приоритет: 2)
2025-12-02 20:27:07,413 - integration.integrations.interrupt_management_integration - INFO - Handling session clear interrupt
2025-12-02 20:27:07,413 - integration.core.event_bus - DEBUG - EventBus: dispatch 'session.clear_requested' to 0 subscriber(s)
2025-12-02 20:27:07,413 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: session.clear_requested
2025-12-02 20:27:07,413 - integration.core.event_bus - DEBUG - EventBus: dispatch 'mode.request' to 1 subscriber(s)
2025-12-02 20:27:07,413 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'mode.request': <bound method ModeManagementIntegration._on_mode_request of <integration.integrations.mode_management_integration.ModeManagementIntegration object at 0x1183238c0>>
2025-12-02 20:27:07,413 - integration.integrations.mode_management_integration - INFO - 🔄 MODE_REQUEST: target=AppMode.SLEEPING, source=interrupt_management, session_id=None, priority=None
2025-12-02 20:27:07,413 - integration.integrations.mode_management_integration - INFO - 🔄 MODE_REQUEST: current_mode=AppMode.PROCESSING, target=AppMode.SLEEPING, source=interrupt_management
2025-12-02 20:27:07,417 - integration.integrations.mode_management_integration - INFO - 🔄 MODE_REQUEST: в PROCESSING, проверяем session_id (active=1764725212.421291, request=None)
2025-12-02 20:27:07,418 - integration.integrations.mode_management_integration - INFO - 🔄 MODE_REQUEST: применяем mode → AppMode.SLEEPING
2025-12-02 20:27:07,419 - integration.core.state_manager - INFO - 🔄 Режим изменен: processing → sleeping
2025-12-02 20:27:07,419 - integration.core.state_manager - INFO - 🎯 TRAY DEBUG: set_mode() готов публиковать app.mode_changed: AppMode.SLEEPING, session_id=None
2025-12-02 20:27:07,420 - integration.core.state_manager - INFO - 🎯 TRAY DEBUG: EventBus подключен: True
2025-12-02 20:27:07,420 - integration.core.state_manager - INFO - 🔄 StateManager: начинаем публикацию событий (EventBus подключен, eb_loop=4700916624)
2025-12-02 20:27:07,420 - integration.core.state_manager - INFO - 🔄 StateManager: публикуем через run_coroutine_threadsafe на loop EventBus (без ожидания)
2025-12-02 20:27:07,421 - integration.core.state_manager - INFO - ✅ StateManager: события опубликованы успешно
2025-12-02 20:27:07,421 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 5248)
2025-12-02 20:27:07,421 - mode_management.core.mode_controller - INFO - ✅ Режим изменен: processing → sleeping
2025-12-02 20:27:07,421 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: mode.request
2025-12-02 20:27:07,422 - modules.interrupt_management.core.interrupt_coordinator - ERROR - ❌ Прерывание session_clear не выполнено
2025-12-02 20:27:07,423 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'interrupt.request': <bound method ActionExecutionIntegration._on_interrupt of <integration.integrations.action_execution_integration.ActionExecutionIntegration object at 0x1183c02f0>>
2025-12-02 20:27:07,423 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: interrupt.request
2025-12-02 20:27:07,423 - integration.integrations.input_processing_integration - INFO - 🛑 SHORT_PRESS: interrupt.request опубликовано для ProcessingWorkflow
2025-12-02 20:27:07,423 - integration.core.event_bus - DEBUG - EventBus: dispatch 'mode.request' to 1 subscriber(s)
2025-12-02 20:27:07,423 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'mode.request': <bound method ModeManagementIntegration._on_mode_request of <integration.integrations.mode_management_integration.ModeManagementIntegration object at 0x1183238c0>>
2025-12-02 20:27:07,423 - integration.integrations.mode_management_integration - INFO - 🔄 MODE_REQUEST: target=AppMode.SLEEPING, source=keyboard.short_press, session_id=None, priority=100
2025-12-02 20:27:07,423 - integration.integrations.mode_management_integration - INFO - 🔄 MODE_REQUEST: current_mode=AppMode.SLEEPING, target=AppMode.SLEEPING, source=keyboard.short_press
2025-12-02 20:27:07,423 - integration.integrations.mode_management_integration - DEBUG - Mode request ignored (same mode): AppMode.SLEEPING
2025-12-02 20:27:07,424 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: mode.request
2025-12-02 20:27:07,424 - integration.integrations.input_processing_integration - INFO - 🛑 SHORT_PRESS: дополнительный запрос на SLEEPING отправлен
2025-12-02 20:27:07,425 - integration.core.state_manager - DEBUG - 🔄 Session ID обновлен (без публикации события): 1764725212.421291 → None
2025-12-02 20:27:07,425 - integration.integrations.input_processing_integration - DEBUG - 🔄 Session ID сброшен в state_manager (reason: short_press_reset)
2025-12-02 20:27:07,425 - integration.core.event_bus - DEBUG - EventBus: dispatch 'keyboard.short_press_cancelled' to 0 subscriber(s)
2025-12-02 20:27:07,425 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: keyboard.short_press_cancelled
2025-12-02 20:27:07,425 - integration.workflows.processing_workflow - DEBUG - ⚙️ ProcessingWorkflow: мониторинг этапа capturing отменен
2025-12-02 20:27:07,425 - integration.workflows.processing_workflow - DEBUG - ⚙️ ProcessingWorkflow: общий мониторинг отменен
2025-12-02 20:27:07,425 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - ✅ Async callback short_press completed successfully
✅ Async callback short_press completed successfully
🎤🎤🎤 _handle_key_release ВЫЗВАН! duration=0.088s
2025-12-02 20:27:07,426 - integration.integrations.input_processing_integration - INFO - 🎤 _handle_key_release ВЫЗВАН! duration=0.088s
2025-12-02 20:27:07,426 - integration.integrations.input_processing_integration - INFO - 🛑 PTT: keyUp(ctrl_n) → RELEASE, duration=88ms
2025-12-02 20:27:07,426 - integration.integrations.input_processing_integration - DEBUG - RELEASE: session=None, recognized=False, recording=False
2025-12-02 20:27:07,426 - integration.integrations.input_processing_integration - DEBUG - 🔄 RELEASE: was_recording=False (_recording_started=False, mic_active=False)
2025-12-02 20:27:07,426 - integration.integrations.input_processing_integration - DEBUG - ℹ️ RELEASE пришёл без активной записи: session=None, duration=88ms, mic_active=False
2025-12-02 20:27:07,426 - integration.integrations.input_processing_integration - DEBUG - 🔄 [STATE] PENDING → IDLE (reason: release_without_recording)
2025-12-02 20:27:07,431 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 4736)
2025-12-02 20:27:07,443 - integration.integrations.input_processing_integration - DEBUG - RELEASE: session_id=None уже ожидает завершения gRPC
2025-12-02 20:27:07,454 - integration.workflows.base_workflow - DEBUG - 🔄 ProcessingWorkflow: задача отменена - ProcessingWorkflow:stage_timeout_playing_audio
2025-12-02 20:27:07,454 - integration.core.state_manager - INFO - 🎯 TRAY DEBUG: StateManager публикует app.mode_changed: AppMode.SLEEPING (type: <enum 'AppMode'>)
2025-12-02 20:27:07,454 - integration.core.state_manager - INFO - 🎯 TRAY DEBUG: StateManager event_data: {'mode': <AppMode.SLEEPING: 'sleeping'>}
2025-12-02 20:27:07,454 - integration.core.event_bus - INFO - EventBus: 'app.mode_changed' → subscribers=9, data={'mode': <AppMode.SLEEPING: 'sleeping'>}
2025-12-02 20:27:07,454 - integration.core.event_bus - DEBUG - EventBus: dispatch 'app.mode_changed' to 9 subscriber(s)
2025-12-02 20:27:07,454 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method TrayControllerIntegration._on_mode_changed of <integration.integrations.tray_controller_integration.TrayControllerIntegration object at 0x118321be0>>
2025-12-02 20:27:07,455 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method ScreenshotCaptureIntegration._on_mode_changed of <integration.integrations.screenshot_capture_integration.ScreenshotCaptureIntegration object at 0x118323380>>
2025-12-02 20:27:07,455 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method ModeManagementIntegration._on_app_mode_changed of <integration.integrations.mode_management_integration.ModeManagementIntegration object at 0x1183238c0>>
2025-12-02 20:27:07,455 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method ProcessingWorkflow._on_mode_changed of <integration.workflows.processing_workflow.ProcessingWorkflow object at 0x1183c1fd0>>
2025-12-02 20:27:07,455 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 4224)
2025-12-02 20:27:07,476 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method VoiceRecognitionIntegration._on_app_mode_changed of <integration.integrations.voice_recognition_integration.VoiceRecognitionIntegration object at 0x118323770>>
2025-12-02 20:27:07,478 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method VoiceOverDuckingIntegration.handle_mode_change of <integration.integrations.voiceover_ducking_integration.VoiceOverDuckingIntegration object at 0x1183c16a0>>
2025-12-02 20:27:07,478 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method ListeningWorkflow._on_mode_changed of <integration.workflows.listening_workflow.ListeningWorkflow object at 0x1183c1e80>>
2025-12-02 20:27:07,478 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method SimpleModuleCoordinator._on_mode_changed of <integration.core.simple_module_coordinator.SimpleModuleCoordinator object at 0x118320440>>
2025-12-02 20:27:07,482 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method UpdaterIntegration._on_mode_changed of <integration.integrations.updater_integration.UpdaterIntegration object at 0x118321fd0>>
2025-12-02 20:27:07,482 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: app.mode_changed
2025-12-02 20:27:07,482 - integration.core.state_manager - INFO - 🎯 TRAY DEBUG: StateManager app.mode_changed опубликовано успешно
2025-12-02 20:27:07,482 - integration.core.state_manager - INFO - 🎯 TRAY DEBUG: StateManager подписчиков на app.mode_changed: 9
2025-12-02 20:27:07,483 - integration.core.state_manager - INFO - 🔄 StateManager: -> publish app.state_changed: AppMode.PROCESSING -> AppMode.SLEEPING
2025-12-02 20:27:07,483 - integration.core.event_bus - DEBUG - EventBus: dispatch 'app.state_changed' to 1 subscriber(s)
2025-12-02 20:27:07,484 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.state_changed': <bound method InterruptManagementIntegration._on_app_state_changed of <integration.integrations.interrupt_management_integration.InterruptManagementIntegration object at 0x118323230>>
2025-12-02 20:27:07,485 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: app.state_changed
2025-12-02 20:27:07,489 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 3712)
2025-12-02 20:27:07,490 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - ✅ Async callback release completed successfully
✅ Async callback release completed successfully
2025-12-02 20:27:07,490 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: _on_mode_changed ВЫЗВАН!
2025-12-02 20:27:07,490 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: event type=<class 'dict'>, event={'type': 'app.mode_changed', 'data': {'mode': <AppMode.SLEEPING: 'sleeping'>}, 'timestamp': 212282.400493125}
2025-12-02 20:27:07,490 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: data={'mode': <AppMode.SLEEPING: 'sleeping'>}
2025-12-02 20:27:07,490 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: new_mode_raw=AppMode.SLEEPING (type: <enum 'AppMode'>)
2025-12-02 20:27:07,490 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: new_mode нормализован: AppMode.SLEEPING (type: <enum 'AppMode'>)
2025-12-02 20:27:07,492 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: mode_to_status={<AppMode.SLEEPING: 'sleeping'>: <TrayStatus.SLEEPING: 'sleeping'>, <AppMode.LISTENING: 'listening'>: <TrayStatus.LISTENING: 'listening'>, <AppMode.PROCESSING: 'processing'>: <TrayStatus.PROCESSING: 'processing'>}
2025-12-02 20:27:07,493 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: new_mode in mapping? True
2025-12-02 20:27:07,493 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: key=AppMode.SLEEPING (type: <enum 'AppMode'>), equals new_mode? True
2025-12-02 20:27:07,494 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: key=AppMode.LISTENING (type: <enum 'AppMode'>), equals new_mode? False
2025-12-02 20:27:07,498 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: key=AppMode.PROCESSING (type: <enum 'AppMode'>), equals new_mode? False
2025-12-02 20:27:07,498 - integration.integrations.tray_controller_integration - DEBUG - TrayIntegration: mapping mode -> status: AppMode.SLEEPING -> TrayStatus.SLEEPING
2025-12-02 20:27:07,498 - integration.core.event_bus - DEBUG - EventBus: dispatch 'tray.status_updated' to 0 subscriber(s)
2025-12-02 20:27:07,498 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: tray.status_updated
2025-12-02 20:27:07,498 - integration.integrations.tray_controller_integration - INFO - 🔄 Режим приложения изменен: sleeping → sleeping
2025-12-02 20:27:07,498 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: _apply_status_ui_sync ВЫЗВАН! status=TrayStatus.SLEEPING (type: <enum 'TrayStatus'>)
2025-12-02 20:27:07,499 - integration.integrations.tray_controller_integration - DEBUG - 🔍 [UI] Начало обновления иконки трея: status=sleeping
2025-12-02 20:27:07,499 - integration.integrations.tray_controller_integration - DEBUG - 🔍 [UI] Предыдущий статус: processing, новый статус: sleeping
2025-12-02 20:27:07,500 - integration.integrations.screenshot_capture_integration - INFO - 🔍 ScreenshotCapture: Получено событие app.mode_changed - mode=AppMode.SLEEPING (type: <enum 'AppMode'>)
2025-12-02 20:27:07,500 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 3200)
2025-12-02 20:27:07,501 - modules.tray_controller.core.tray_types - DEBUG - 🎯 TRAY DEBUG: TrayIconGenerator.create_circle_icon status=TrayStatus.SLEEPING (type: <enum 'TrayStatus'>)
2025-12-02 20:27:07,501 - integration.integrations.screenshot_capture_integration - DEBUG - ScreenshotCapture: Игнорируем режим AppMode.SLEEPING, ждем PROCESSING
2025-12-02 20:27:07,506 - modules.tray_controller.core.tray_types - DEBUG - 🎯 TRAY DEBUG: Available colors: {<TrayStatus.SLEEPING: 'sleeping'>: '#808080', <TrayStatus.LISTENING: 'listening'>: '#007AFF', <TrayStatus.PROCESSING: 'processing'>: '#FF9500'}
2025-12-02 20:27:07,507 - integration.workflows.processing_workflow - DEBUG - ⚙️ ProcessingWorkflow: режим изменен на sleeping
2025-12-02 20:27:07,507 - modules.tray_controller.core.tray_types - DEBUG - 🎯 TRAY DEBUG: Selected color: #808080
2025-12-02 20:27:07,507 - integration.workflows.listening_workflow - DEBUG - 🎤 ListeningWorkflow: режим изменен на sleeping
2025-12-02 20:27:07,507 - modules.tray_controller.macos.tray_icon - DEBUG - 🎯 TRAY DEBUG: create_icon_file вызван для status=TrayStatus.SLEEPING
2025-12-02 20:27:07,507 - modules.tray_controller.macos.tray_icon - DEBUG - 🎯 TRAY DEBUG: generated color=#808080, PIL_available=True
🔄 Координация смены режима: sleeping
2025-12-02 20:27:07,508 - integration.integrations.tray_controller_integration - DEBUG - 🔍 [UI] Иконка создана: /var/folders/ys/xlx_chms3hqcs1lfyq37395c0000gn/T/tmp203jgm7p.png, обновляем меню...
2025-12-02 20:27:07,508 - modules.tray_controller.macos.menu_handler - INFO - 🔍 ДИАГНОСТИКА update_icon: icon_path='/var/folders/ys/xlx_chms3hqcs1lfyq37395c0000gn/T/tmp203jgm7p.png'
2025-12-02 20:27:07,508 - modules.tray_controller.macos.menu_handler - INFO - 🔍 ДИАГНОСТИКА update_icon: os.path.exists(icon_path)=True
2025-12-02 20:27:07,508 - modules.tray_controller.macos.menu_handler - INFO - 🔍 ДИАГНОСТИКА update_icon: размер файла=193 bytes
2025-12-02 20:27:07,509 - modules.tray_controller.macos.menu_handler - INFO - ✅ ДИАГНОСТИКА update_icon: Иконка обновлена успешно (попытка 1)
2025-12-02 20:27:07,509 - integration.integrations.tray_controller_integration - DEBUG - 🔍 [UI] Иконка обновлена в меню
2025-12-02 20:27:07,509 - integration.integrations.tray_controller_integration - DEBUG - 🔍 [UI] Текст статуса обновлен: Sleeping
2025-12-02 20:27:07,509 - integration.integrations.tray_controller_integration - INFO - ✅ Tray UI applied: processing -> sleeping
2025-12-02 20:27:07,509 - integration.integrations.tray_controller_integration - DEBUG - 🔍 [UI] Обновление иконки трея завершено успешно
2025-12-02 20:27:07,511 - integration.integrations.updater_integration - INFO - Режим приложения изменен на: AppMode.SLEEPING
2025-12-02 20:27:07,511 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 2688)
2025-12-02 20:27:07,521 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 2176)
2025-12-02 20:27:07,531 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 1664)
2025-12-02 20:27:07,546 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 1152)
2025-12-02 20:27:07,553 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 640)
2025-12-02 20:27:07,579 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 128)
2025-12-02 20:27:07,591 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 128 фреймов + 384 тишины (dtype=int16, ch=1)
2025-12-02 20:27:07,601 - modules.speech_playback.core.player - DEBUG - 🔧 [CALLBACK] Конвертировано 1 каналов → 1 каналов: shape=(512, 1)
2025-12-02 20:27:07,602 - modules.speech_playback.core.player - INFO - ✅ Чанк chunk_3_1764725227358 полностью воспроизведен
2025-12-02 20:27:07,602 - modules.speech_playback.core.buffer - DEBUG - ✅ Чанк завершен: chunk_3_1764725227358
2025-12-02 20:27:07,602 - modules.speech_playback.core.player - INFO - ✅ Чанк обработан: chunk_3_1764725227358
2025-12-02 20:27:07,612 - modules.speech_playback.core.player - DEBUG - 🔧 [CALLBACK] Конвертировано 1 каналов → 1 каналов: shape=(512, 1)
2025-12-02 20:27:07,623 - modules.speech_playback.core.player - DEBUG - 🔧 [CALLBACK] Конвертировано 1 каналов → 1 каналов: shape=(512, 1)
2025-12-02 20:27:07,633 - modules.speech_playback.core.player - DEBUG - 🔧 [CALLBACK] Конвертировано 1 каналов → 1 каналов: shape=(512, 1)
2025-12-02 20:27:07,644 - modules.speech_playback.core.player - DEBUG - 🔧 [CALLBACK] Конвертировано 1 каналов → 1 каналов: shape=(512, 1)
2025-12-02 20:27:07,655 - modules.speech_playback.core.player - DEBUG - 🔧 [CALLBACK] Конвертировано 1 каналов → 1 каналов: shape=(512, 1)
2025-12-02 20:27:07,665 - modules.speech_playback.core.player - DEBUG - 🔧 [CALLBACK] Конвертировано 1 каналов → 1 каналов: shape=(512, 1)
2025-12-02 20:27:07,676 - modules.speech_playback.core.player - DEBUG - 🔧 [CALLBACK] Конвертировано 1 каналов → 1 каналов: shape=(512, 1)
2025-12-02 20:27:07,687 - modules.speech_playback.core.player - DEBUG - 🔧 [CALLBACK] Конвертировано 1 каналов → 1 каналов: shape=(512, 1)
2025-12-02 20:27:07,697 - modules.speech_playback.core.player - DEBUG - 🔧 [CALLBACK] Конвертировано 1 каналов → 1 каналов: shape=(512, 1)
2025-12-02 20:27:07,708 - modules.speech_playback.core.player - DEBUG - 🔧 [CALLBACK] Конвертировано 1 каналов → 1 каналов: shape=(512, 1)
2025-12-02 20:27:07,824 - modules.speech_playback.core.player - INFO - ⏸️ Аудио поток остановлен (очередь пуста, lazy stop)
I0000 00:00:1764725231.257804 4787424 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-02 20:27:11,349 - modules.audio_core.device_change_publisher - DEBUG - ✅ [INPUT] macOS default (через SwitchAudioSource): "MacBook Air Microphone"
I0000 00:00:1764725231.391569 4787424 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-02 20:27:11,464 - modules.audio_core.device_change_publisher - DEBUG - ✅ [OUTPUT] macOS default (через SwitchAudioSource): "MacBook Air Speakers"
I0000 00:00:1764725232.471273 4787424 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-02 20:27:12,559 - modules.audio_core.device_change_publisher - DEBUG - ✅ [INPUT] macOS default (через SwitchAudioSource): "MacBook Air Microphone"
I0000 00:00:1764725232.560709 4787424 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-02 20:27:12,631 - modules.audio_core.device_change_publisher - DEBUG - ✅ [OUTPUT] macOS default (через SwitchAudioSource): "MacBook Air Speakers"
I0000 00:00:1764725233.638664 4787424 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-02 20:27:13,726 - modules.audio_core.device_change_publisher - DEBUG - ✅ [INPUT] macOS default (через SwitchAudioSource): "MacBook Air Microphone"
I0000 00:00:1764725233.727494 4787424 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-02 20:27:13,799 - modules.audio_core.device_change_publisher - DEBUG - ✅ [OUTPUT] macOS default (через SwitchAudioSource): "MacBook Air Speakers"
I0000 00:00:1764725234.806279 4787424 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-02 20:27:14,892 - modules.audio_core.device_change_publisher - DEBUG - ✅ [INPUT] macOS default (через SwitchAudioSource): "MacBook Air Microphone"
I0000 00:00:1764725234.893735 4787424 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-02 20:27:14,967 - modules.audio_core.device_change_publisher - DEBUG - ✅ [OUTPUT] macOS default (через SwitchAudioSource): "MacBook Air Speakers"
I0000 00:00:1764725235.969669 4787424 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-02 20:27:16,058 - modules.audio_core.device_change_publisher - DEBUG - ✅ [INPUT] macOS default (через SwitchAudioSource): "MacBook Air Microphone"
I0000 00:00:1764725236.059935 4787424 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-02 20:27:16,131 - modules.audio_core.device_change_publisher - DEBUG - ✅ [OUTPUT] macOS default (через SwitchAudioSource): "MacBook Air Speakers"
I0000 00:00:1764725237.138016 4787424 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-02 20:27:17,228 - modules.audio_core.device_change_publisher - DEBUG - ✅ [INPUT] macOS default (через SwitchAudioSource): "MacBook Air Microphone"
I0000 00:00:1764725237.229088 4787424 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-02 20:27:17,303 - modules.audio_core.device_change_publisher - DEBUG - ✅ [OUTPUT] macOS default (через SwitchAudioSource): "MacBook Air Speakers"
2025-12-02 20:27:17,915 - modules.speech_playback.macos.performance - DEBUG - 📊 CPU: 7.7%, Memory: 76.3%
I0000 00:00:1764725238.309287 4787424 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-02 20:27:18,395 - modules.audio_core.device_change_publisher - DEBUG - ✅ [INPUT] macOS default (через SwitchAudioSource): "MacBook Air Microphone"
I0000 00:00:1764725238.396665 4787424 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-02 20:27:18,487 - modules.audio_core.device_change_publisher - DEBUG - ✅ [OUTPUT] macOS default (через SwitchAudioSource): "MacBook Air Speakers"
I0000 00:00:1764725239.491272 4787424 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-02 20:27:19,573 - modules.audio_core.device_change_publisher - DEBUG - ✅ [INPUT] macOS defau


ed=False (было True)
2025-12-02 20:27:06,518 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔄 [RESET] Деактивация комбинации: control_pressed=False, n_pressed=False
2025-12-02 20:27:06,518 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔑 Combo deactivation: короткое нажатие, генерируем SHORT_PRESS
2025-12-02 20:27:06,518 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔑 _trigger_event: type=short_press, duration=0.088s, thread=MainThread
2025-12-02 20:27:06,518 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔑 _run_callback: short_press, callback=_handle_short_press
🔑 _run_callback: short_press, callback=_handle_short_press
2025-12-02 20:27:06,518 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔑 _trigger_event: type=release, duration=0.088s, thread=MainThread
2025-12-02 20:27:06,519 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔑 Выполняем async callback в loop: short_press (loop=4700916624, running=True)
🔑 Выполняем async callback в loop: short_press (loop=4700916624, running=True)
2025-12-02 20:27:06,519 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔑 _run_callback: release, callback=_handle_key_release
🔑 _run_callback: release, callback=_handle_key_release
2025-12-02 20:27:06,520 - integration.integrations.input_processing_integration - DEBUG - 🔑 SHORT_PRESS: 0.088с
2025-12-02 20:27:06,521 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔑 Выполняем async callback в loop: release (loop=4700916624, running=True)
🔑 Выполняем async callback в loop: release (loop=4700916624, running=True)
2025-12-02 20:27:06,521 - integration.integrations.input_processing_integration - INFO - 🛑 SHORT_PRESS без записи - отменяем pending session 1764725226.4302258
2025-12-02 20:27:06,526 - integration.integrations.input_processing_integration - INFO - 🛑 SHORT_PRESS: проверка прерывания (mode=AppMode.PROCESSING, playback_active=False, grpc_session=1764725212.421291, should_interrupt=True)
2025-12-02 20:27:06,526 - integration.integrations.input_processing_integration - INFO - 🛑 SHORT_PRESS: МГНОВЕННО прерываем воспроизведение (mode=AppMode.PROCESSING, playback_active=False, grpc_session=1764725212.421291)
2025-12-02 20:27:06,527 - integration.core.event_bus - DEBUG - EventBus: dispatch 'playback.cancelled' to 3 subscriber(s)
2025-12-02 20:27:06,527 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'playback.cancelled': <bound method SpeechPlaybackIntegration._on_unified_interrupt of <integration.integrations.speech_playback_integration.SpeechPlaybackIntegration object at 0x1183c0980>>
2025-12-02 20:27:06,527 - integration.integrations.speech_playback_integration - INFO - SpeechPlayback: ЕДИНЫЙ канал прерывания, source=input_processing, reason=keyboard
2025-12-02 20:27:06,527 - integration.integrations.speech_playback_integration - DEBUG - SpeechPlayback: воспроизведение уже остановлено (state=PlaybackState.IDLE)
2025-12-02 20:27:06,527 - integration.integrations.speech_playback_integration - INFO - SpeechPlayback: прерывание обработано через ЕДИНЫЙ канал
2025-12-02 20:27:06,527 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'playback.cancelled': <bound method InputProcessingIntegration._on_playback_finished of <integration.integrations.input_processing_integration.InputProcessingIntegration object at 0x118321e80>>
2025-12-02 20:27:06,527 - integration.integrations.input_processing_integration - DEBUG - PLAYBACK: finished (event=playback.cancelled, session=1764725212.421291)
2025-12-02 20:27:06,527 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'playback.cancelled': <bound method SignalIntegration._on_playback_cancelled of <integration.integrations.signal_integration.SignalIntegration object at 0x1183c0d70>>
2025-12-02 20:27:06,527 - integration.integrations.signal_integration - DEBUG - Signals: CANCEL skipped (reason=keyboard)
2025-12-02 20:27:06,528 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: playback.cancelled
2025-12-02 20:27:06,528 - integration.integrations.input_processing_integration - INFO - 🛑 SHORT_PRESS: playback.cancelled опубликовано НАПРЯМУЮ для мгновенного прерывания
2025-12-02 20:27:06,528 - integration.core.event_bus - DEBUG - EventBus: dispatch 'interrupt.request' to 4 subscriber(s)
2025-12-02 20:27:06,528 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'interrupt.request': <bound method ListeningWorkflow._on_interrupt_request of <integration.workflows.listening_workflow.ListeningWorkflow object at 0x1183c1e80>>
2025-12-02 20:27:06,528 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'interrupt.request': <bound method ProcessingWorkflow._on_interrupt_request of <integration.workflows.processing_workflow.ProcessingWorkflow object at 0x1183c1fd0>>
2025-12-02 20:27:06,528 - integration.workflows.processing_workflow - INFO - ⚙️ ProcessingWorkflow: получен запрос ПРЕРЫВАНИЯ, reason=user_interrupt, stage=capturing, active=True
2025-12-02 20:27:06,528 - integration.workflows.processing_workflow - INFO - ⚙️ ProcessingWorkflow: отменяем gRPC запрос
2025-12-02 20:27:06,528 - integration.core.event_bus - DEBUG - EventBus: dispatch 'grpc.request_cancel' to 2 subscriber(s)
2025-12-02 20:27:06,528 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'grpc.request_cancel': <bound method SpeechPlaybackIntegration._on_grpc_cancel of <integration.integrations.speech_playback_integration.SpeechPlaybackIntegration object at 0x1183c0980>>
2025-12-02 20:27:06,528 - integration.integrations.speech_playback_integration - INFO - SpeechPlayback: получен grpc.request_cancel — очищаем буфер
2025-12-02 20:27:06,528 - modules.speech_playback.core.buffer - INFO - 🧹 Очередь очищена: 0 чанков
2025-12-02 20:27:06,528 - modules.speech_playback.core.buffer - INFO - 🧹 Буфер воспроизведения очищен: 0 фреймов
2025-12-02 20:27:06,528 - modules.speech_playback.core.buffer - INFO - 🧹 Все буферы очищены
2025-12-02 20:27:06,528 - modules.speech_playback.core.player - WARNING - ⚠️ Невозможно остановить воспроизведение в текущем состоянии
2025-12-02 20:27:06,528 - integration.core.event_bus - DEBUG - EventBus: dispatch 'playback.cancelled' to 3 subscriber(s)
2025-12-02 20:27:06,528 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'playback.cancelled': <bound method SpeechPlaybackIntegration._on_unified_interrupt of <integration.integrations.speech_playback_integration.SpeechPlaybackIntegration object at 0x1183c0980>>
2025-12-02 20:27:06,528 - integration.integrations.speech_playback_integration - INFO - SpeechPlayback: ЕДИНЫЙ канал прерывания, source=grpc_cancel, reason=interrupt
2025-12-02 20:27:06,528 - integration.integrations.speech_playback_integration - DEBUG - SpeechPlayback: воспроизведение уже остановлено (state=PlaybackState.IDLE)
2025-12-02 20:27:06,528 - integration.integrations.speech_playback_integration - INFO - SpeechPlayback: прерывание обработано через ЕДИНЫЙ канал
2025-12-02 20:27:06,528 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'playback.cancelled': <bound method InputProcessingIntegration._on_playback_finished of <integration.integrations.input_processing_integration.InputProcessingIntegration object at 0x118321e80>>
2025-12-02 20:27:06,528 - integration.integrations.input_processing_integration - DEBUG - PLAYBACK: finished (event=playback.cancelled, session=1764725212.421291)
2025-12-02 20:27:06,528 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'playback.cancelled': <bound method SignalIntegration._on_playback_cancelled of <integration.integrations.signal_integration.SignalIntegration object at 0x1183c0d70>>
2025-12-02 20:27:06,528 - integration.integrations.signal_integration - DEBUG - Signals: CANCEL skipped (reason=grpc_cancel)
2025-12-02 20:27:06,528 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: playback.cancelled
2025-12-02 20:27:06,528 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'grpc.request_cancel': <bound method GrpcClientIntegration._on_request_cancel of <integration.integrations.grpc_client_integration.GrpcClientIntegration object at 0x118323e00>>
2025-12-02 20:27:06,528 - integration.integrations.grpc_client_integration - INFO - grpc.request_cancel: no inflight request to cancel (noop)
2025-12-02 20:27:06,528 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: grpc.request_cancel
2025-12-02 20:27:06,528 - integration.workflows.processing_workflow - INFO - ⚙️ ProcessingWorkflow: останавливаем воспроизведение через ЕДИНЫЙ канал
2025-12-02 20:27:06,529 - integration.core.event_bus - DEBUG - EventBus: dispatch 'playback.cancelled' to 3 subscriber(s)
2025-12-02 20:27:06,529 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'playback.cancelled': <bound method SpeechPlaybackIntegration._on_unified_interrupt of <integration.integrations.speech_playback_integration.SpeechPlaybackIntegration object at 0x1183c0980>>
2025-12-02 20:27:06,529 - integration.integrations.speech_playback_integration - INFO - SpeechPlayback: ЕДИНЫЙ канал прерывания, source=processing_workflow, reason=user_interrupt
2025-12-02 20:27:06,529 - integration.integrations.speech_playback_integration - DEBUG - SpeechPlayback: воспроизведение уже остановлено (state=PlaybackState.IDLE)
2025-12-02 20:27:06,529 - integration.integrations.speech_playback_integration - INFO - SpeechPlayback: прерывание обработано через ЕДИНЫЙ канал
2025-12-02 20:27:06,529 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'playback.cancelled': <bound method InputProcessingIntegration._on_playback_finished of <integration.integrations.input_processing_integration.InputProcessingIntegration object at 0x118321e80>>
2025-12-02 20:27:06,529 - integration.integrations.input_processing_integration - DEBUG - PLAYBACK: finished (event=playback.cancelled, session=None)
2025-12-02 20:27:06,529 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'playback.cancelled': <bound method SignalIntegration._on_playback_cancelled of <integration.integrations.signal_integration.SignalIntegration object at 0x1183c0d70>>
2025-12-02 20:27:06,529 - integration.integrations.signal_integration - INFO - Signals: CANCEL (playback.cancelled)
2025-12-02 20:27:06,533 - integration.core.event_bus - DEBUG - EventBus: dispatch 'playback.signal' to 1 subscriber(s)
2025-12-02 20:27:06,533 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'playback.signal': <bound method SpeechPlaybackIntegration._on_playback_signal of <integration.integrations.speech_playback_integration.SpeechPlaybackIntegration object at 0x1183c0980>>
2025-12-02 20:27:06,533 - integration.integrations.speech_playback_integration - INFO - 🔔 playback.signal: pattern=cancel, bytes=11520, sr=48000, ch=1, gain=1.0, prio=0
2025-12-02 20:27:06,533 - modules.speech_playback.core.player - INFO - 🎯 [AUDIO_REFACTOR] Начало инициализации Sequential Speech Player...
2025-12-02 20:27:06,533 - modules.speech_playback.core.player - DEBUG - 🔍 [AUDIO_DEBUG] Инициализация Core Audio Manager...
2025-12-02 20:27:06,533 - modules.speech_playback.macos.core_audio - INFO - ✅ Core Audio инициализирован
2025-12-02 20:27:06,533 - modules.speech_playback.core.player - INFO - ✅ [AUDIO_SUCCESS] Core Audio Manager инициализирован
2025-12-02 20:27:06,533 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Запрашиваем системное default output устройство...
2025-12-02 20:27:06,533 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] ШАГ 1.2: Определение устройства через macOS API (приоритет 1)
2025-12-02 20:27:06,533 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Используем SwitchAudioSource: /opt/homebrew/bin/SwitchAudioSource
2025-12-02 20:27:06,533 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Запрос текущего default output устройства...
I0000 00:00:1764725226.534366 4787285 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-02 20:27:06,587 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 [TAP] KeyUp: N (keycode=45)
2025-12-02 20:27:06,669 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Команда выполнена: returncode=0, stdout_len=94, stderr_len=0
2025-12-02 20:27:06,671 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Получен JSON: {'name': 'MacBook Air Speakers', 'type': 'output', 'id': '71', 'uid': 'BuiltInSpeakerDevice'}
2025-12-02 20:27:06,672 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] macOS default OUTPUT (через SwitchAudioSource): "MacBook Air Speakers"
2025-12-02 20:27:06,672 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Успешно получено имя устройства: MacBook Air Speakers
2025-12-02 20:27:06,672 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] macOS default OUTPUT (источник истины): "MacBook Air Speakers"
2025-12-02 20:27:06,672 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Найден ID для 'MacBook Air Speakers': 4
2025-12-02 20:27:06,672 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Найдено устройство через SwitchAudioSource: name=MacBook Air Speakers, id=4
2025-12-02 20:27:06,672 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Найдено default output устройство (через SwitchAudioSource):
2025-12-02 20:27:06,672 - modules.speech_playback.core.player - INFO -    Name: MacBook Air Speakers
2025-12-02 20:27:06,672 - modules.speech_playback.core.player - INFO -    Index: 4
2025-12-02 20:27:06,672 - modules.speech_playback.core.player - INFO -    Max Output Channels: 2
2025-12-02 20:27:06,672 - modules.speech_playback.core.player - INFO -    Default Sample Rate: 48000.0 Hz
2025-12-02 20:27:06,672 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Полная информация: {'name': 'MacBook Air Speakers', 'index': 4, 'hostapi': 0, 'max_input_channels': 0, 'max_output_channels': 2, 'default_low_input_latency': 0.01, 'default_low_output_latency': 0.015166666666666667, 'default_high_input_latency': 0.1, 'default_high_output_latency': 0.0245, 'default_samplerate': 48000.0}
2025-12-02 20:27:06,672 - modules.speech_playback.core.player - INFO - 🎯 Используем системное устройство по умолчанию от macOS
2025-12-02 20:27:06,672 - modules.speech_playback.core.player - INFO - 📊 [AUDIO_STATS] Конфигурация плеера: sample_rate=48000Hz, channels=2, dtype=int16
2025-12-02 20:27:06,673 - modules.speech_playback.macos.performance - INFO - ✅ Мониторинг производительности запущен
2025-12-02 20:27:06,673 - modules.speech_playback.core.player - INFO - ✅ [AUDIO_SUCCESS] Sequential Speech Player инициализирован успешно
2025-12-02 20:27:06,673 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] _start_audio_stream вызван: sync_output=True, device_id=None
2025-12-02 20:27:06,673 - modules.speech_playback.core.player - WARNING - ⚠️ [OUTPUT] Обнаружен существующий поток при создании нового, закрываем...
2025-12-02 20:27:06,673 - modules.speech_playback.core.player - WARNING - ⚠️ [OUTPUT] Существующий поток: active=False, started=False
2025-12-02 20:27:06,673 - modules.speech_playback.core.player - DEBUG - 🔄 [OUTPUT] Закрываем неактивный поток...
2025-12-02 20:27:06,674 - modules.speech_playback.core.player - DEBUG - ✅ [OUTPUT] Старый поток полностью освобожден (active=False, ожидание: 0.000с)
2025-12-02 20:27:06,674 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Старый поток закрыт и освобожден (ожидание: 0.000с)
2025-12-02 20:27:06,779 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Текущая конфигурация: rate=48000Hz, channels=2, dtype=int16, buffer_size=512
2025-12-02 20:27:06,779 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Синхронизируем формат с устройством...
2025-12-02 20:27:06,779 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Запрашиваем системное default output устройство...
2025-12-02 20:27:06,779 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] ШАГ 1.2: Определение устройства через macOS API (приоритет 1)
2025-12-02 20:27:06,779 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Используем SwitchAudioSource: /opt/homebrew/bin/SwitchAudioSource
2025-12-02 20:27:06,779 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Запрос текущего default output устройства...
I0000 00:00:1764725226.779892 4787285 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-02 20:27:06,865 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Команда выполнена: returncode=0, stdout_len=94, stderr_len=0
2025-12-02 20:27:06,866 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Получен JSON: {'name': 'MacBook Air Speakers', 'type': 'output', 'id': '71', 'uid': 'BuiltInSpeakerDevice'}
2025-12-02 20:27:06,866 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] macOS default OUTPUT (через SwitchAudioSource): "MacBook Air Speakers"
2025-12-02 20:27:06,866 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Успешно получено имя устройства: MacBook Air Speakers
2025-12-02 20:27:06,866 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] macOS default OUTPUT (источник истины): "MacBook Air Speakers"
2025-12-02 20:27:06,866 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Найден ID для 'MacBook Air Speakers': 4
2025-12-02 20:27:06,866 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Найдено устройство через SwitchAudioSource: name=MacBook Air Speakers, id=4
2025-12-02 20:27:06,866 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Найдено default output устройство (через SwitchAudioSource):
2025-12-02 20:27:06,866 - modules.speech_playback.core.player - INFO -    Name: MacBook Air Speakers
2025-12-02 20:27:06,867 - modules.speech_playback.core.player - INFO -    Index: 4
2025-12-02 20:27:06,867 - modules.speech_playback.core.player - INFO -    Max Output Channels: 2
2025-12-02 20:27:06,867 - modules.speech_playback.core.player - INFO -    Default Sample Rate: 48000.0 Hz
2025-12-02 20:27:06,867 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Полная информация: {'name': 'MacBook Air Speakers', 'index': 4, 'hostapi': 0, 'max_input_channels': 0, 'max_output_channels': 2, 'default_low_input_latency': 0.01, 'default_low_output_latency': 0.015166666666666667, 'default_high_input_latency': 0.1, 'default_high_output_latency': 0.0245, 'default_samplerate': 48000.0}
2025-12-02 20:27:06,867 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] После синхронизации: rate=48000Hz, channels=2
2025-12-02 20:27:06,867 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] device_id не передан, получаем устройство через macOS API (SwitchAudioSource)...
2025-12-02 20:27:06,867 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Fallback на SwitchAudioSource (device_id не передан)
2025-12-02 20:27:06,867 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Запрашиваем системное default output устройство...
2025-12-02 20:27:06,867 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] ШАГ 1.2: Определение устройства через macOS API (приоритет 1)
2025-12-02 20:27:06,867 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Используем SwitchAudioSource: /opt/homebrew/bin/SwitchAudioSource
2025-12-02 20:27:06,867 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Запрос текущего default output устройства...
I0000 00:00:1764725226.868216 4787285 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-02 20:27:06,953 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Команда выполнена: returncode=0, stdout_len=94, stderr_len=0
2025-12-02 20:27:06,953 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Получен JSON: {'name': 'MacBook Air Speakers', 'type': 'output', 'id': '71', 'uid': 'BuiltInSpeakerDevice'}
2025-12-02 20:27:06,954 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] macOS default OUTPUT (через SwitchAudioSource): "MacBook Air Speakers"
2025-12-02 20:27:06,954 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Успешно получено имя устройства: MacBook Air Speakers
2025-12-02 20:27:06,954 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] macOS default OUTPUT (источник истины): "MacBook Air Speakers"
2025-12-02 20:27:06,954 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Найден ID для 'MacBook Air Speakers': 4
2025-12-02 20:27:06,954 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Найдено устройство через SwitchAudioSource: name=MacBook Air Speakers, id=4
2025-12-02 20:27:06,955 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Найдено default output устройство (через SwitchAudioSource):
2025-12-02 20:27:06,955 - modules.speech_playback.core.player - INFO -    Name: MacBook Air Speakers
2025-12-02 20:27:06,955 - modules.speech_playback.core.player - INFO -    Index: 4
2025-12-02 20:27:06,955 - modules.speech_playback.core.player - INFO -    Max Output Channels: 2
2025-12-02 20:27:06,955 - modules.speech_playback.core.player - INFO -    Default Sample Rate: 48000.0 Hz
2025-12-02 20:27:06,955 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Полная информация: {'name': 'MacBook Air Speakers', 'index': 4, 'hostapi': 0, 'max_input_channels': 0, 'max_output_channels': 2, 'default_low_input_latency': 0.01, 'default_low_output_latency': 0.015166666666666667, 'default_high_input_latency': 0.1, 'default_high_output_latency': 0.0245, 'default_samplerate': 48000.0}
2025-12-02 20:27:06,955 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] macOS API (источник истины): "MacBook Air Speakers" (ID=4)
2025-12-02 20:27:06,955 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Обычное устройство: используем ID=4
2025-12-02 20:27:06,955 - modules.audio_core.device_params_normalizer - DEBUG - ✅ [OUTPUT] Нормализовано: "MacBook Air Speakers" → 48000 Hz, 2 ch
2025-12-02 20:27:06,955 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Нормализованные параметры для "MacBook Air Speakers":
2025-12-02 20:27:06,956 - modules.speech_playback.core.player - INFO -    Sample Rate: 48000 → 48000 Hz
2025-12-02 20:27:06,956 - modules.speech_playback.core.player - INFO -    Channels: 2
2025-12-02 20:27:06,956 - modules.speech_playback.core.stream_config_resolver - DEBUG - 🔧 [OUTPUT] Обычное устройство: используем все параметры (device=4, channels=1, blocksize=512)
2025-12-02 20:27:06,956 - modules.speech_playback.core.player - DEBUG - 🔧 [OUTPUT] Обычное устройство: используем все параметры (device=4, channels=1, blocksize=512)
2025-12-02 20:27:06,956 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Конфигурация потока:
2025-12-02 20:27:06,956 - modules.speech_playback.core.player - INFO -    device: 4
2025-12-02 20:27:06,956 - modules.speech_playback.core.player - INFO -    channels: 1
2025-12-02 20:27:06,956 - modules.speech_playback.core.player - INFO -    dtype: int16
2025-12-02 20:27:06,956 - modules.speech_playback.core.player - INFO -    samplerate: 48000 Hz
2025-12-02 20:27:06,956 - modules.speech_playback.core.player - INFO -    blocksize: 512
2025-12-02 20:27:06,956 - modules.speech_playback.core.player - INFO -    latency: N/A (не задан, пусть PortAudio выберет)
2025-12-02 20:27:06,956 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Создаём поток для устройства: MacBook Air Speakers (ID=4)
2025-12-02 20:27:06,956 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Проверяем доступность устройства ID 4...
2025-12-02 20:27:06,956 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Проверка доступности устройства ID 4...
2025-12-02 20:27:06,956 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Получаем список всех устройств...
2025-12-02 20:27:06,956 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Всего устройств в системе: 5
2025-12-02 20:27:06,956 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Запрашиваем информацию об устройстве ID 4...
2025-12-02 20:27:06,956 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] sd.query_devices() завершён для ID 4
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Информация об устройстве получена: MacBook Air Speakers
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - DEBUG -    Index: 4
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - DEBUG -    Max Input Channels: 0
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - DEBUG -    Max Output Channels: 2
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - DEBUG -    Default Sample Rate: 48000.0 Hz
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - DEBUG -    Host API: 0
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Устройство ID 4 (MacBook Air Speakers) доступно:
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - INFO -    Sample Rate: 48000.0 Hz
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - INFO -    Max Output Channels: 2
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Результат проверки доступности: True
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Устройство MacBook Air Speakers (ID=4) доступно
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Начинаем создание потока (max_retries=5, base_delay=0.3s, BT=False)...
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Подтверждение: старый поток полностью закрыт (_audio_stream=None)
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Подтверждение: старый поток закрыт → создаём новый stream
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - INFO -    Устройство: MacBook Air Speakers (ID=4, BT=False)
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - INFO -    Параметры: device=4, channels=1, samplerate=48000, blocksize=512, latency=N/A
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Попытка 1/5 создания потока...
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Параметры потока: {'device': 4, 'channels': 1, 'dtype': 'int16', 'samplerate': 48000, 'blocksize': 512, 'callback': <bound method SequentialSpeechPlayer._audio_callback of <modules.speech_playback.core.player.SequentialSpeechPlayer object at 0x118389fd0>>}
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Попытка 2/5 создания потока...
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Параметры потока: {'device': 4, 'channels': 1, 'dtype': 'int16', 'samplerate': 48000, 'blocksize': 512, 'callback': <bound method SequentialSpeechPlayer._audio_callback of <modules.speech_playback.core.player.SequentialSpeechPlayer object at 0x118389fd0>>}
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Попытка 3/5 создания потока...
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Параметры потока: {'device': 4, 'channels': 1, 'dtype': 'int16', 'samplerate': 48000, 'blocksize': 512, 'callback': <bound method SequentialSpeechPlayer._audio_callback of <modules.speech_playback.core.player.SequentialSpeechPlayer object at 0x118389fd0>>}
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Попытка 4/5 создания потока...
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Параметры потока: {'device': 4, 'channels': 1, 'dtype': 'int16', 'samplerate': 48000, 'blocksize': 512, 'callback': <bound method SequentialSpeechPlayer._audio_callback of <modules.speech_playback.core.player.SequentialSpeechPlayer object at 0x118389fd0>>}
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Попытка 5/5 создания потока...
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Параметры потока: {'device': 4, 'channels': 1, 'dtype': 'int16', 'samplerate': 48000, 'blocksize': 512, 'callback': <bound method SequentialSpeechPlayer._audio_callback of <modules.speech_playback.core.player.SequentialSpeechPlayer object at 0x118389fd0>>}
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Последний host error code: 0
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Создаем новый поток через AudioStreamManager: device=4, BT=False
2025-12-02 20:27:06,957 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Запускаем create_stream (_start_audio_stream) в отдельном thread (timeout=3.0с)...
2025-12-02 20:27:06,958 - asyncio - DEBUG - Using selector: KqueueSelector
2025-12-02 20:27:06,958 - modules.audio_core.stream_manager - INFO - 🔍 [OUTPUT] create_stream ВХОД: device=4 (MacBook Air Speakers), BT=False, max_retries=2
2025-12-02 20:27:06,958 - modules.audio_core.stream_manager - DEBUG - 🔍 [OUTPUT] create_stream: пытаемся захватить lock...
2025-12-02 20:27:06,958 - modules.audio_core.stream_manager - DEBUG - ✅ [OUTPUT] create_stream: lock захвачен (время ожидания: 0.0ms), начинаем создание потока
2025-12-02 20:27:06,958 - modules.audio_core.stream_manager - DEBUG - 🔒 [OUTPUT] Закрытие потока...
2025-12-02 20:27:06,958 - modules.audio_core.stream_manager - DEBUG - ⏳ [OUTPUT] Задержка после закрытия: 0.3с (BT=False)
2025-12-02 20:27:07,265 - modules.audio_core.stream_manager - DEBUG - ✅ [OUTPUT] Поток успешно закрыт
2025-12-02 20:27:07,266 - modules.audio_core.stream_manager - INFO - 🔄 [OUTPUT] Попытка 1/2 создания потока:
   device_id=4, device_name=MacBook Air Speakers
   samplerate=48000Hz, channels=1
   dtype=int16, blocksize=512, latency=None
   is_bluetooth=False, callback=True
2025-12-02 20:27:07,267 - modules.audio_core.stream_manager - DEBUG - 🔍 [OUTPUT] Подготавливаем параметры потока...
2025-12-02 20:27:07,267 - modules.audio_core.stream_manager - DEBUG - 🔍 [OUTPUT] Параметры подготовлены: {'device': 4, 'samplerate': 48000, 'channels': 1, 'dtype': 'int16', 'callback': <bound method SequentialSpeechPlayer._audio_callback of <modules.speech_playback.core.player.SequentialSpeechPlayer object at 0x118389fd0>>, 'blocksize': 512}
2025-12-02 20:27:07,267 - modules.audio_core.stream_manager - DEBUG - 🔍 [OUTPUT] Создаем output поток через PortAudio...
2025-12-02 20:27:07,299 - modules.audio_core.stream_manager - DEBUG - ✅ [OUTPUT] Поток создан через PortAudio: <sounddevice.OutputStream object at 0x118589950>
2025-12-02 20:27:07,300 - modules.audio_core.stream_manager - INFO - ✅ [OUTPUT] Поток создан успешно на попытке 1 (время: 342.4ms)
2025-12-02 20:27:07,305 - modules.speech_playback.core.player - DEBUG - ✅ [OUTPUT] create_stream (_start_audio_stream) завершен успешно
2025-12-02 20:27:07,312 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Аудио поток создан успешно! (время создания: 0.35с)
2025-12-02 20:27:07,312 - modules.speech_playback.core.player - INFO -    Устройство: MacBook Air Speakers (ID=4, BT=False)
2025-12-02 20:27:07,313 - modules.speech_playback.core.player - INFO -    Параметры: channels=1, samplerate=48000Hz, dtype=int16, blocksize=512, latency=N/A
2025-12-02 20:27:07,313 - modules.speech_playback.core.player - INFO -    Задержки: prestart=0с, backoff=4.8с
2025-12-02 20:27:07,314 - modules.speech_playback.core.player - INFO - 💾 [OUTPUT] Сохранена безопасная конфигурация после успешного создания потока (попытка 5)
2025-12-02 20:27:07,314 - modules.speech_playback.core.player - DEBUG - 💡 Поток будет стартован при появлении первого чанка (lazy start)
2025-12-02 20:27:07,314 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Стартуем поток: stream exists=True, started=False
2025-12-02 20:27:07,352 - modules.speech_playback.core.player - INFO - ▶️ Аудио поток стартован (lazy start)
2025-12-02 20:27:07,352 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Поток стартован: active=True
2025-12-02 20:27:07,353 - modules.speech_playback.core.player - INFO - 🔄 Playback loop запущен
2025-12-02 20:27:07,353 - modules.speech_playback.core.player - INFO - 🎵 Воспроизведение запущено
2025-12-02 20:27:07,353 - integration.core.event_bus - DEBUG - EventBus: dispatch 'playback.started' to 2 subscriber(s)
2025-12-02 20:27:07,354 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'playback.started': <bound method ProcessingWorkflow._on_playback_started of <integration.workflows.processing_workflow.ProcessingWorkflow object at 0x1183c1fd0>>
2025-12-02 20:27:07,354 - integration.workflows.processing_workflow - INFO - 🔊 ProcessingWorkflow: воспроизведение началось
2025-12-02 20:27:07,354 - integration.workflows.processing_workflow - INFO - ⚙️ ProcessingWorkflow: переход capturing → playing_audio
2025-12-02 20:27:07,354 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'playback.started': <bound method InputProcessingIntegration._on_playback_started of <integration.integrations.input_processing_integration.InputProcessingIntegration object at 0x118321e80>>
2025-12-02 20:27:07,354 - integration.integrations.input_processing_integration - DEBUG - PLAYBACK: started (session=None)
2025-12-02 20:27:07,355 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: playback.started
2025-12-02 20:27:07,355 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Проверка устройства: session=None, started=True, time_since_check=1.29s
2025-12-02 20:27:07,355 - modules.speech_playback.core.player - INFO - 🔊 [OUTPUT] Начальное устройство: "Sergiy’s AirPods" (BT=True)
2025-12-02 20:27:07,356 - modules.speech_playback.core.player - DEBUG - 🔧 [CALLBACK] Конвертировано 1 каналов → 1 каналов: shape=(512, 1)
2025-12-02 20:27:07,356 - modules.speech_playback.core.player - DEBUG - 🔄 Моно аудио будет воспроизведено на 2 каналах
2025-12-02 20:27:07,358 - modules.speech_playback.core.buffer - INFO - ✅ Чанк добавлен: chunk_3_1764725227358 (size: 5760, queue: 1)
2025-12-02 20:27:07,358 - modules.speech_playback.core.player - DEBUG - ✅ [OUTPUT] Поток уже стартован
2025-12-02 20:27:07,358 - modules.speech_playback.core.player - INFO - ✅ Аудио данные добавлены: chunk_3_1764725227358 (size: 5760)
2025-12-02 20:27:07,358 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: playback.signal
2025-12-02 20:27:07,358 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: playback.cancelled
2025-12-02 20:27:07,358 - integration.workflows.processing_workflow - INFO - ⚙️ ProcessingWorkflow: возврат в SLEEPING, reason=interrupted
2025-12-02 20:27:07,359 - integration.core.event_bus - DEBUG - EventBus: dispatch 'mode.request' to 1 subscriber(s)
2025-12-02 20:27:07,360 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'mode.request': <bound method ModeManagementIntegration._on_mode_request of <integration.integrations.mode_management_integration.ModeManagementIntegration object at 0x1183238c0>>
2025-12-02 20:27:07,360 - integration.integrations.mode_management_integration - INFO - 🔄 MODE_REQUEST: target=AppMode.SLEEPING, source=ProcessingWorkflow.processing_interrupted, session_id=None, priority=90
2025-12-02 20:27:07,364 - integration.integrations.mode_management_integration - WARNING - MODE_REQUEST: target=AppMode.SLEEPING not in allowed modes, ignoring
2025-12-02 20:27:07,364 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: mode.request
2025-12-02 20:27:07,365 - integration.workflows.base_workflow - DEBUG - 🔄 ProcessingWorkflow: запрос смены режима sleeping
2025-12-02 20:27:07,365 - integration.workflows.processing_workflow - DEBUG - ⚙️ ProcessingWorkflow: состояние очищено
2025-12-02 20:27:07,365 - modules.speech_playback.core.player - DEBUG - 🔧 [CALLBACK] Конвертировано 1 каналов → 1 каналов: shape=(512, 1)
2025-12-02 20:27:07,408 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'interrupt.request': <bound method InterruptManagementIntegration._on_interrupt_request of <integration.integrations.interrupt_management_integration.InterruptManagementIntegration object at 0x118323230>>
2025-12-02 20:27:07,408 - modules.speech_playback.core.buffer - DEBUG - 🔍 Получен чанк: chunk_3_1764725227358
2025-12-02 20:27:07,409 - modules.speech_playback.core.buffer - INFO - ✅ Чанк добавлен в буфер: chunk_3_1764725227358 (frames: 5760, buffer: 0 → 5760, ch=2)
2025-12-02 20:27:07,409 - integration.integrations.interrupt_management_integration - WARNING - ⚠️ Неизвестный тип прерывания: interrupt.request, используем SESSION_CLEAR
2025-12-02 20:27:07,413 - modules.interrupt_management.core.interrupt_coordinator - INFO - 🔄 Запуск прерывания session_clear (приоритет: 2)
2025-12-02 20:27:07,413 - integration.integrations.interrupt_management_integration - INFO - Handling session clear interrupt
2025-12-02 20:27:07,413 - integration.core.event_bus - DEBUG - EventBus: dispatch 'session.clear_requested' to 0 subscriber(s)
2025-12-02 20:27:07,413 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: session.clear_requested
2025-12-02 20:27:07,413 - integration.core.event_bus - DEBUG - EventBus: dispatch 'mode.request' to 1 subscriber(s)
2025-12-02 20:27:07,413 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'mode.request': <bound method ModeManagementIntegration._on_mode_request of <integration.integrations.mode_management_integration.ModeManagementIntegration object at 0x1183238c0>>
2025-12-02 20:27:07,413 - integration.integrations.mode_management_integration - INFO - 🔄 MODE_REQUEST: target=AppMode.SLEEPING, source=interrupt_management, session_id=None, priority=None
2025-12-02 20:27:07,413 - integration.integrations.mode_management_integration - INFO - 🔄 MODE_REQUEST: current_mode=AppMode.PROCESSING, target=AppMode.SLEEPING, source=interrupt_management
2025-12-02 20:27:07,417 - integration.integrations.mode_management_integration - INFO - 🔄 MODE_REQUEST: в PROCESSING, проверяем session_id (active=1764725212.421291, request=None)
2025-12-02 20:27:07,418 - integration.integrations.mode_management_integration - INFO - 🔄 MODE_REQUEST: применяем mode → AppMode.SLEEPING
2025-12-02 20:27:07,419 - integration.core.state_manager - INFO - 🔄 Режим изменен: processing → sleeping
2025-12-02 20:27:07,419 - integration.core.state_manager - INFO - 🎯 TRAY DEBUG: set_mode() готов публиковать app.mode_changed: AppMode.SLEEPING, session_id=None
2025-12-02 20:27:07,420 - integration.core.state_manager - INFO - 🎯 TRAY DEBUG: EventBus подключен: True
2025-12-02 20:27:07,420 - integration.core.state_manager - INFO - 🔄 StateManager: начинаем публикацию событий (EventBus подключен, eb_loop=4700916624)
2025-12-02 20:27:07,420 - integration.core.state_manager - INFO - 🔄 StateManager: публикуем через run_coroutine_threadsafe на loop EventBus (без ожидания)
2025-12-02 20:27:07,421 - integration.core.state_manager - INFO - ✅ StateManager: события опубликованы успешно
2025-12-02 20:27:07,421 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 5248)
2025-12-02 20:27:07,421 - mode_management.core.mode_controller - INFO - ✅ Режим изменен: processing → sleeping
2025-12-02 20:27:07,421 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: mode.request
2025-12-02 20:27:07,422 - modules.interrupt_management.core.interrupt_coordinator - ERROR - ❌ Прерывание session_clear не выполнено
2025-12-02 20:27:07,423 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'interrupt.request': <bound method ActionExecutionIntegration._on_interrupt of <integration.integrations.action_execution_integration.ActionExecutionIntegration object at 0x1183c02f0>>
2025-12-02 20:27:07,423 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: interrupt.request
2025-12-02 20:27:07,423 - integration.integrations.input_processing_integration - INFO - 🛑 SHORT_PRESS: interrupt.request опубликовано для ProcessingWorkflow
2025-12-02 20:27:07,423 - integration.core.event_bus - DEBUG - EventBus: dispatch 'mode.request' to 1 subscriber(s)
2025-12-02 20:27:07,423 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'mode.request': <bound method ModeManagementIntegration._on_mode_request of <integration.integrations.mode_management_integration.ModeManagementIntegration object at 0x1183238c0>>
2025-12-02 20:27:07,423 - integration.integrations.mode_management_integration - INFO - 🔄 MODE_REQUEST: target=AppMode.SLEEPING, source=keyboard.short_press, session_id=None, priority=100
2025-12-02 20:27:07,423 - integration.integrations.mode_management_integration - INFO - 🔄 MODE_REQUEST: current_mode=AppMode.SLEEPING, target=AppMode.SLEEPING, source=keyboard.short_press
2025-12-02 20:27:07,423 - integration.integrations.mode_management_integration - DEBUG - Mode request ignored (same mode): AppMode.SLEEPING
2025-12-02 20:27:07,424 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: mode.request
2025-12-02 20:27:07,424 - integration.integrations.input_processing_integration - INFO - 🛑 SHORT_PRESS: дополнительный запрос на SLEEPING отправлен
2025-12-02 20:27:07,425 - integration.core.state_manager - DEBUG - 🔄 Session ID обновлен (без публикации события): 1764725212.421291 → None
2025-12-02 20:27:07,425 - integration.integrations.input_processing_integration - DEBUG - 🔄 Session ID сброшен в state_manager (reason: short_press_reset)
2025-12-02 20:27:07,425 - integration.core.event_bus - DEBUG - EventBus: dispatch 'keyboard.short_press_cancelled' to 0 subscriber(s)
2025-12-02 20:27:07,425 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: keyboard.short_press_cancelled
2025-12-02 20:27:07,425 - integration.workflows.processing_workflow - DEBUG - ⚙️ ProcessingWorkflow: мониторинг этапа capturing отменен
2025-12-02 20:27:07,425 - integration.workflows.processing_workflow - DEBUG - ⚙️ ProcessingWorkflow: общий мониторинг отменен
2025-12-02 20:27:07,425 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - ✅ Async callback short_press completed successfully
✅ Async callback short_press completed successfully
🎤🎤🎤 _handle_key_release ВЫЗВАН! duration=0.088s
2025-12-02 20:27:07,426 - integration.integrations.input_processing_integration - INFO - 🎤 _handle_key_release ВЫЗВАН! duration=0.088s
2025-12-02 20:27:07,426 - integration.integrations.input_processing_integration - INFO - 🛑 PTT: keyUp(ctrl_n) → RELEASE, duration=88ms
2025-12-02 20:27:07,426 - integration.integrations.input_processing_integration - DEBUG - RELEASE: session=None, recognized=False, recording=False
2025-12-02 20:27:07,426 - integration.integrations.input_processing_integration - DEBUG - 🔄 RELEASE: was_recording=False (_recording_started=False, mic_active=False)
2025-12-02 20:27:07,426 - integration.integrations.input_processing_integration - DEBUG - ℹ️ RELEASE пришёл без активной записи: session=None, duration=88ms, mic_active=False
2025-12-02 20:27:07,426 - integration.integrations.input_processing_integration - DEBUG - 🔄 [STATE] PENDING → IDLE (reason: release_without_recording)
2025-12-02 20:27:07,431 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 4736)
2025-12-02 20:27:07,443 - integration.integrations.input_processing_integration - DEBUG - RELEASE: session_id=None уже ожидает завершения gRPC
2025-12-02 20:27:07,454 - integration.workflows.base_workflow - DEBUG - 🔄 ProcessingWorkflow: задача отменена - ProcessingWorkflow:stage_timeout_playing_audio
2025-12-02 20:27:07,454 - integration.core.state_manager - INFO - 🎯 TRAY DEBUG: StateManager публикует app.mode_changed: AppMode.SLEEPING (type: <enum 'AppMode'>)
2025-12-02 20:27:07,454 - integration.core.state_manager - INFO - 🎯 TRAY DEBUG: StateManager event_data: {'mode': <AppMode.SLEEPING: 'sleeping'>}
2025-12-02 20:27:07,454 - integration.core.event_bus - INFO - EventBus: 'app.mode_changed' → subscribers=9, data={'mode': <AppMode.SLEEPING: 'sleeping'>}
2025-12-02 20:27:07,454 - integration.core.event_bus - DEBUG - EventBus: dispatch 'app.mode_changed' to 9 subscriber(s)
2025-12-02 20:27:07,454 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method TrayControllerIntegration._on_mode_changed of <integration.integrations.tray_controller_integration.TrayControllerIntegration object at 0x118321be0>>
2025-12-02 20:27:07,455 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method ScreenshotCaptureIntegration._on_mode_changed of <integration.integrations.screenshot_capture_integration.ScreenshotCaptureIntegration object at 0x118323380>>
2025-12-02 20:27:07,455 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method ModeManagementIntegration._on_app_mode_changed of <integration.integrations.mode_management_integration.ModeManagementIntegration object at 0x1183238c0>>
2025-12-02 20:27:07,455 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method ProcessingWorkflow._on_mode_changed of <integration.workflows.processing_workflow.ProcessingWorkflow object at 0x1183c1fd0>>
2025-12-02 20:27:07,455 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 4224)
2025-12-02 20:27:07,476 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method VoiceRecognitionIntegration._on_app_mode_changed of <integration.integrations.voice_recognition_integration.VoiceRecognitionIntegration object at 0x118323770>>
2025-12-02 20:27:07,478 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method VoiceOverDuckingIntegration.handle_mode_change of <integration.integrations.voiceover_ducking_integration.VoiceOverDuckingIntegration object at 0x1183c16a0>>
2025-12-02 20:27:07,478 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method ListeningWorkflow._on_mode_changed of <integration.workflows.listening_workflow.ListeningWorkflow object at 0x1183c1e80>>
2025-12-02 20:27:07,478 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method SimpleModuleCoordinator._on_mode_changed of <integration.core.simple_module_coordinator.SimpleModuleCoordinator object at 0x118320440>>
2025-12-02 20:27:07,482 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method UpdaterIntegration._on_mode_changed of <integration.integrations.updater_integration.UpdaterIntegration object at 0x118321fd0>>
2025-12-02 20:27:07,482 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: app.mode_changed
2025-12-02 20:27:07,482 - integration.core.state_manager - INFO - 🎯 TRAY DEBUG: StateManager app.mode_changed опубликовано успешно
2025-12-02 20:27:07,482 - integration.core.state_manager - INFO - 🎯 TRAY DEBUG: StateManager подписчиков на app.mode_changed: 9
2025-12-02 20:27:07,483 - integration.core.state_manager - INFO - 🔄 StateManager: -> publish app.state_changed: AppMode.PROCESSING -> AppMode.SLEEPING
2025-12-02 20:27:07,483 - integration.core.event_bus - DEBUG - EventBus: dispatch 'app.state_changed' to 1 subscriber(s)
2025-12-02 20:27:07,484 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.state_changed': <bound method InterruptManagementIntegration._on_app_state_changed of <integration.integrations.interrupt_management_integration.InterruptManagementIntegration object at 0x118323230>>
2025-12-02 20:27:07,485 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: app.state_changed
2025-12-02 20:27:07,489 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 3712)
2025-12-02 20:27:07,490 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - ✅ Async callback release completed successfully
✅ Async callback release completed successfully
2025-12-02 20:27:07,490 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: _on_mode_changed ВЫЗВАН!
2025-12-02 20:27:07,490 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: event type=<class 'dict'>, event={'type': 'app.mode_changed', 'data': {'mode': <AppMode.SLEEPING: 'sleeping'>}, 'timestamp': 212282.400493125}
2025-12-02 20:27:07,490 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: data={'mode': <AppMode.SLEEPING: 'sleeping'>}
2025-12-02 20:27:07,490 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: new_mode_raw=AppMode.SLEEPING (type: <enum 'AppMode'>)
2025-12-02 20:27:07,490 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: new_mode нормализован: AppMode.SLEEPING (type: <enum 'AppMode'>)
2025-12-02 20:27:07,492 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: mode_to_status={<AppMode.SLEEPING: 'sleeping'>: <TrayStatus.SLEEPING: 'sleeping'>, <AppMode.LISTENING: 'listening'>: <TrayStatus.LISTENING: 'listening'>, <AppMode.PROCESSING: 'processing'>: <TrayStatus.PROCESSING: 'processing'>}
2025-12-02 20:27:07,493 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: new_mode in mapping? True
2025-12-02 20:27:07,493 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: key=AppMode.SLEEPING (type: <enum 'AppMode'>), equals new_mode? True
2025-12-02 20:27:07,494 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: key=AppMode.LISTENING (type: <enum 'AppMode'>), equals new_mode? False
2025-12-02 20:27:07,498 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: key=AppMode.PROCESSING (type: <enum 'AppMode'>), equals new_mode? False
2025-12-02 20:27:07,498 - integration.integrations.tray_controller_integration - DEBUG - TrayIntegration: mapping mode -> status: AppMode.SLEEPING -> TrayStatus.SLEEPING
2025-12-02 20:27:07,498 - integration.core.event_bus - DEBUG - EventBus: dispatch 'tray.status_updated' to 0 subscriber(s)
2025-12-02 20:27:07,498 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: tray.status_updated
2025-12-02 20:27:07,498 - integration.integrations.tray_controller_integration - INFO - 🔄 Режим приложения изменен: sleeping → sleeping
2025-12-02 20:27:07,498 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: _apply_status_ui_sync ВЫЗВАН! status=TrayStatus.SLEEPING (type: <enum 'TrayStatus'>)
2025-12-02 20:27:07,499 - integration.integrations.tray_controller_integration - DEBUG - 🔍 [UI] Начало обновления иконки трея: status=sleeping
2025-12-02 20:27:07,499 - integration.integrations.tray_controller_integration - DEBUG - 🔍 [UI] Предыдущий статус: processing, новый статус: sleeping
2025-12-02 20:27:07,500 - integration.integrations.screenshot_capture_integration - INFO - 🔍 ScreenshotCapture: Получено событие app.mode_changed - mode=AppMode.SLEEPING (type: <enum 'AppMode'>)
2025-12-02 20:27:07,500 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 3200)
2025-12-02 20:27:07,501 - modules.tray_controller.core.tray_types - DEBUG - 🎯 TRAY DEBUG: TrayIconGenerator.create_circle_icon status=TrayStatus.SLEEPING (type: <enum 'TrayStatus'>)
2025-12-02 20:27:07,501 - integration.integrations.screenshot_capture_integration - DEBUG - ScreenshotCapture: Игнорируем режим AppMode.SLEEPING, ждем PROCESSING
2025-12-02 20:27:07,506 - modules.tray_controller.core.tray_types - DEBUG - 🎯 TRAY DEBUG: Available colors: {<TrayStatus.SLEEPING: 'sleeping'>: '#808080', <TrayStatus.LISTENING: 'listening'>: '#007AFF', <TrayStatus.PROCESSING: 'processing'>: '#FF9500'}
2025-12-02 20:27:07,507 - integration.workflows.processing_workflow - DEBUG - ⚙️ ProcessingWorkflow: режим изменен на sleeping
2025-12-02 20:27:07,507 - modules.tray_controller.core.tray_types - DEBUG - 🎯 TRAY DEBUG: Selected color: #808080
2025-12-02 20:27:07,507 - integration.workflows.listening_workflow - DEBUG - 🎤 ListeningWorkflow: режим изменен на sleeping
2025-12-02 20:27:07,507 - modules.tray_controller.macos.tray_icon - DEBUG - 🎯 TRAY DEBUG: create_icon_file вызван для status=TrayStatus.SLEEPING
2025-12-02 20:27:07,507 - modules.tray_controller.macos.tray_icon - DEBUG - 🎯 TRAY DEBUG: generated color=#808080, PIL_available=True
🔄 Координация смены режима: sleeping
2025-12-02 20:27:07,508 - integration.integrations.tray_controller_integration - DEBUG - 🔍 [UI] Иконка создана: /var/folders/ys/xlx_chms3hqcs1lfyq37395c0000gn/T/tmp203jgm7p.png, обновляем меню...
2025-12-02 20:27:07,508 - modules.tray_controller.macos.menu_handler - INFO - 🔍 ДИАГНОСТИКА update_icon: icon_path='/var/folders/ys/xlx_chms3hqcs1lfyq37395c0000gn/T/tmp203jgm7p.png'
2025-12-02 20:27:07,508 - modules.tray_controller.macos.menu_handler - INFO - 🔍 ДИАГНОСТИКА update_icon: os.path.exists(icon_path)=True
2025-12-02 20:27:07,508 - modules.tray_controller.macos.menu_handler - INFO - 🔍 ДИАГНОСТИКА update_icon: размер файла=193 bytes
2025-12-02 20:27:07,509 - modules.tray_controller.macos.menu_handler - INFO - ✅ ДИАГНОСТИКА update_icon: Иконка обновлена успешно (попытка 1)
2025-12-02 20:27:07,509 - integration.integrations.tray_controller_integration - DEBUG - 🔍 [UI] Иконка обновлена в меню
2025-12-02 20:27:07,509 - integration.integrations.tray_controller_integration - DEBUG - 🔍 [UI] Текст статуса обновлен: Sleeping
2025-12-02 20:27:07,509 - integration.integrations.tray_controller_integration - INFO - ✅ Tray UI applied: processing -> sleeping
2025-12-02 20:27:07,509 - integration.integrations.tray_controller_integration - DEBUG - 🔍 [UI] Обновление иконки трея завершено успешно
2025-12-02 20:27:07,511 - integration.integrations.updater_integration - INFO - Режим приложения изменен на: AppMode.SLEEPING
2025-12-02 20:27:07,511 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 2688)
2025-12-02 20:27:07,521 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 2176)
2025-12-02 20:27:07,531 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 1664)
2025-12-02 20:27:07,546 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 1152)
2025-12-02 20:27:07,553 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 640)
2025-12-02 20:27:07,579 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 128)
2025-12-02 20:27:07,591 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 128 фреймов + 384 тишины (dtype=int16, ch=1)
2025-12-02 20:27:07,601 - modules.speech_playback.core.player - DEBUG - 🔧 [CALLBACK] Конвертировано 1 каналов → 1 каналов: shape=(512, 1)
2025-12-02 20:27:07,602 - modules.speech_playback.core.player - INFO - ✅ Чанк chunk_3_1764725227358 полностью воспроизведен
2025-12-02 20:27:07,602 - modules.speech_playback.core.buffer - DEBUG - ✅ Чанк завершен: chunk_3_1764725227358
2025-12-02 20:27:07,602 - modules.speech_playback.core.player - INFO - ✅ Чанк обработан: chunk_3_1764725227358
2025-12-02 20:27:07,612 - modules.speech_playback.core.player - DEBUG - 🔧 [CALLBACK] Конвертировано 1 каналов → 1 каналов: shape=(512, 1)
2025-12-02 20:27:07,623 - modules.speech_playback.core.player - DEBUG - 🔧 [CALLBACK] Конвертировано 1 каналов → 1 каналов: shape=(512, 1)
2025-12-02 20:27:07,633 - modules.speech_playback.core.player - DEBUG - 🔧 [CALLBACK] Конвертировано 1 каналов → 1 каналов: shape=(512, 1)
2025-12-02 20:27:07,644 - modules.speech_playback.core.player - DEBUG - 🔧 [CALLBACK] Конвертировано 1 каналов → 1 каналов: shape=(512, 1)
2025-12-02 20:27:07,655 - modules.speech_playback.core.player - DEBUG - 🔧 [CALLBACK] Конвертировано 1 каналов → 1 каналов: shape=(512, 1)
2025-12-02 20:27:07,665 - modules.speech_playback.core.player - DEBUG - 🔧 [CALLBACK] Конвертировано 1 каналов → 1 каналов: shape=(512, 1)
2025-12-02 20:27:07,676 - modules.speech_playback.core.player - DEBUG - 🔧 [CALLBACK] Конвертировано 1 каналов → 1 каналов: shape=(512, 1)
2025-12-02 20:27:07,687 - modules.speech_playback.core.player - DEBUG - 🔧 [CALLBACK] Конвертировано 1 каналов → 1 каналов: shape=(512, 1)
2025-12-02 20:27:07,697 - modules.speech_playback.core.player - DEBUG - 🔧 [CALLBACK] Конвертировано 1 каналов → 1 каналов: shape=(512, 1)
2025-12-02 20:27:07,708 - modules.speech_playback.core.player - DEBUG - 🔧 [CALLBACK] Конвертировано 1 каналов → 1 каналов: shape=(512, 1)
2025-12-02 20:27:07,824 - modules.speech_playback.core.player - INFO - ⏸️ Аудио поток остановлен (очередь пуста, lazy stop)
I0000 00:00:1764725231.257804 4787424 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-02 20:27:11,349 - modules.audio_core.device_change_publisher - DEBUG - ✅ [INPUT] macOS default (через SwitchAudioSource): "MacBook Air Microphone"
I0000 00:00:1764725231.391569 4787424 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-02 20:27:11,464 - modules.audio_core.device_change_publisher - DEBUG - ✅ [OUTPUT] macOS default (через SwitchAudioSource): "MacBook Air Speakers"
I0000 00:00:1764725232.471273 4787424 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-02 20:27:12,559 - modules.audio_core.device_change_publisher - DEBUG - ✅ [INPUT] macOS default (через SwitchAudioSource): "MacBook Air Microphone"
I0000 00:00:1764725232.560709 4787424 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-02 20:27:12,631 - modules.audio_core.device_change_publisher - DEBUG - ✅ [OUTPUT] macOS default (через SwitchAudioSource): "MacBook Air Speakers"
I0000 00:00:1764725233.638664 4787424 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-02 20:27:13,726 - modules.audio_core.device_change_publisher - DEBUG - ✅ [INPUT] macOS default (через SwitchAudioSource): "MacBook Air Microphone"
I0000 00:00:1764725233.727494 4787424 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-02 20:27:13,799 - modules.audio_core.device_change_publisher - DEBUG - ✅ [OUTPUT] macOS default (через SwitchAudioSource): "MacBook Air Speakers"
I0000 00:00:1764725234.806279 4787424 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-02 20:27:14,892 - modules.audio_core.device_change_publisher - DEBUG - ✅ [INPUT] macOS default (через SwitchAudioSource): "MacBook Air Microphone"
I0000 00:00:1764725234.893735 4787424 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-02 20:27:14,967 - modules.audio_core.device_change_publisher - DEBUG - ✅ [OUTPUT] macOS default (через SwitchAudioSource): "MacBook Air Speakers"
I0000 00:00:1764725235.969669 4787424 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-02 20:27:16,058 - modules.audio_core.device_change_publisher - DEBUG - ✅ [INPUT] macOS default (через SwitchAudioSource): "MacBook Air Microphone"
I0000 00:00:1764725236.059935 4787424 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-02 20:27:16,131 - modules.audio_core.device_change_publisher - DEBUG - ✅ [OUTPUT] macOS default (через SwitchAudioSource): "MacBook Air Speakers"
I0000 00:00:1764725237.138016 4787424 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-02 20:27:17,228 - modules.audio_core.device_change_publisher - DEBUG - ✅ [INPUT] macOS default (через SwitchAudioSource): "MacBook Air Microphone"
I0000 00:00:1764725237.229088 4787424 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-02 20:27:17,303 - modules.audio_core.device_change_publisher - DEBUG - ✅ [OUTPUT] macOS default (через SwitchAudioSource): "MacBook Air Speakers"
2025-12-02 20:27:17,915 - modules.speech_playback.macos.performance - DEBUG - 📊 CPU: 7.7%, Memory: 76.3%
I0000 00:00:1764725238.309287 4787424 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-02 20:27:18,395 - modules.audio_core.device_change_publisher - DEBUG - ✅ [INPUT] macOS default (через SwitchAudioSource): "MacBook Air Microphone"
I0000 00:00:1764725238.396665 4787424 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-02 20:27:18,487 - modules.audio_core.device_change_publisher - DEBUG - ✅ [OUTPUT] macOS default (через SwitchAudioSource): "MacBook Air Speakers"
I0000 00:00:1764725239.491272 4787424 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-02 20:27:19,573 - modules.audio_core.device_change_publisher - DEBUG - ✅ [INPUT] macOS defau

ion=1764725284.579155
2025-12-02 20:28:14,879 - integration.core.simple_module_coordinator - INFO - Screenshot captured: path=/var/folders/ys/xlx_chms3hqcs1lfyq37395c0000gn/T/nexy_screenshots/shot_212349821.jpg, size=431152, dims=1383x900, session=1764725284.579155
2025-12-02 20:28:14,879 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: screenshot.captured
2025-12-02 20:28:14,879 - integration.integrations.screenshot_capture_integration - INFO - Screenshot captured: /var/folders/ys/xlx_chms3hqcs1lfyq37395c0000gn/T/nexy_screenshots/shot_212349821.jpg
2025-12-02 20:28:14,879 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'voice.recording_stop': <bound method VoiceRecognitionIntegration._on_recording_stop of <integration.integrations.voice_recognition_integration.VoiceRecognitionIntegration object at 0x118323770>>
2025-12-02 20:28:14,879 - integration.integrations.voice_recognition_integration - INFO - 🛑 VOICE: _on_recording_stop ВХОД: event={'type': 'voice.recording_stop', 'data': {'source': 'keyboard', 'timestamp': 1764725291.2833111, 'duration': 6.704156160354614, 'session_id': 1764725284.579155}, 'timestamp': 212347.70102825}
2025-12-02 20:28:14,879 - integration.integrations.voice_recognition_integration - INFO - 🛑 VOICE: recording_stop, session=1764725284.579155 (type: <class 'float'>)
2025-12-02 20:28:14,879 - integration.integrations.voice_recognition_integration - INFO - 🛑 VOICE: active_session_id=1764725284.579155 (type: <class 'float'>), request_session_id=1764725284.579155 (type: <class 'float'>)
2025-12-02 20:28:14,880 - integration.integrations.voice_recognition_integration - INFO - 🛑 VOICE: Сравнение session_id: active='1764725284.579155' vs request='1764725284.579155'
2025-12-02 20:28:14,880 - integration.integrations.voice_recognition_integration - INFO - 🛑 VOICE: Вызов request_close: mic_state_manager=True, stream_was_active=False
2025-12-02 20:28:14,880 - modules.microphone_state.core.microphone_state_manager - DEBUG - ✅ [MIC_STATE] Микрофон уже закрыт
2025-12-02 20:28:14,880 - integration.integrations.voice_recognition_integration - INFO - ✅ VOICE: request_close завершен успешно
2025-12-02 20:28:14,880 - integration.integrations.voice_recognition_integration - INFO - 🔍 VOICE: Проверка условий для stop_listening: simulate=False, recognizer=True
2025-12-02 20:28:14,880 - integration.integrations.voice_recognition_integration - INFO - 🛑 VOICE: Условия для stop_listening выполнены, вызываем stop_listening
2025-12-02 20:28:14,880 - integration.integrations.voice_recognition_integration - WARNING - ⚠️ VOICE: Распознаватель не активен (is_listening=False, stream_active=False), пропускаем stop_listening
2025-12-02 20:28:14,880 - integration.core.event_bus - DEBUG - EventBus: dispatch 'microphone.closed' to 1 subscriber(s)
2025-12-02 20:28:14,880 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'microphone.closed': <bound method MicrophoneStateManager._on_microphone_closed of <modules.microphone_state.core.microphone_state_manager.MicrophoneStateManager object at 0x110b79940>>
2025-12-02 20:28:14,880 - modules.microphone_state.core.microphone_state_manager - DEBUG - ℹ️ [MIC_STATE] Закрытие микрофона в состоянии idle (возможно, уже закрыт)
2025-12-02 20:28:14,880 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: microphone.closed
2025-12-02 20:28:14,880 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'voice.recording_stop': <bound method ListeningWorkflow._on_recording_stop of <integration.workflows.listening_workflow.ListeningWorkflow object at 0x1183c1e80>>
2025-12-02 20:28:14,880 - integration.workflows.listening_workflow - INFO - 🎤 ListeningWorkflow: завершение записи, session_id=1764725284.579155
2025-12-02 20:28:14,880 - integration.workflows.listening_workflow - INFO - 🎤 ListeningWorkflow: запись завершена успешно, ожидаем PROCESSING
2025-12-02 20:28:14,880 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: voice.recording_stop
2025-12-02 20:28:14,880 - integration.integrations.input_processing_integration - DEBUG - SHORT_PRESS: voice.recording_stop опубликовано
2025-12-02 20:28:14,881 - integration.integrations.input_processing_integration - DEBUG - 🎤 [INPUT_PROCESSING] _wait_for_mic_closed: mic_active=False
2025-12-02 20:28:14,881 - integration.integrations.input_processing_integration - DEBUG - 🎤 [INPUT_PROCESSING] Микрофон уже закрыт, пропускаем ожидание
2025-12-02 20:28:15,073 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Запрашиваем системное default output устройство...
2025-12-02 20:28:15,073 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] ШАГ 1.2: Определение устройства через macOS API (приоритет 1)
2025-12-02 20:28:15,073 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Используем SwitchAudioSource: /opt/homebrew/bin/SwitchAudioSource
2025-12-02 20:28:15,074 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Запрос текущего default output устройства...
I0000 00:00:1764725295.074500 4787285 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-02 20:28:15,190 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Команда выполнена: returncode=0, stdout_len=94, stderr_len=0
2025-12-02 20:28:15,190 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Получен JSON: {'name': 'Sergiy’s AirPods', 'type': 'output', 'id': '85', 'uid': '1C-77-54-18-C8-A3:output'}
2025-12-02 20:28:15,190 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] macOS default OUTPUT (через SwitchAudioSource): "Sergiy’s AirPods"
2025-12-02 20:28:15,190 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Успешно получено имя устройства: Sergiy’s AirPods
2025-12-02 20:28:15,190 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] macOS default OUTPUT (источник истины): "Sergiy’s AirPods"
2025-12-02 20:28:15,191 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Найден ID для 'Sergiy’s AirPods': 1
2025-12-02 20:28:15,191 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Найдено устройство через SwitchAudioSource: name=Sergiy’s AirPods, id=1
2025-12-02 20:28:15,191 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Найдено default output устройство (через SwitchAudioSource):
2025-12-02 20:28:15,191 - modules.speech_playback.core.player - INFO -    Name: Sergiy’s AirPods
2025-12-02 20:28:15,191 - modules.speech_playback.core.player - INFO -    Index: 1
2025-12-02 20:28:15,191 - modules.speech_playback.core.player - INFO -    Max Output Channels: 2
2025-12-02 20:28:15,191 - modules.speech_playback.core.player - INFO -    Default Sample Rate: 48000.0 Hz
2025-12-02 20:28:15,191 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Полная информация: {'name': 'Sergiy’s AirPods', 'index': 1, 'hostapi': 0, 'max_input_channels': 0, 'max_output_channels': 2, 'default_low_input_latency': 0.01, 'default_low_output_latency': 0.16133333333333333, 'default_high_input_latency': 0.1, 'default_high_output_latency': 0.17066666666666666, 'default_samplerate': 48000.0}
2025-12-02 20:28:15,191 - integration.integrations.input_processing_integration - DEBUG - SHORT_PRESS: session_id=1764725284.579155 удерживаем до завершения gRPC
2025-12-02 20:28:15,191 - integration.core.event_bus - DEBUG - EventBus: dispatch 'mode.request' to 1 subscriber(s)
2025-12-02 20:28:15,191 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'mode.request': <bound method ModeManagementIntegration._on_mode_request of <integration.integrations.mode_management_integration.ModeManagementIntegration object at 0x1183238c0>>
2025-12-02 20:28:15,191 - integration.integrations.mode_management_integration - INFO - 🔄 MODE_REQUEST: target=AppMode.PROCESSING, source=input_processing, session_id=None, priority=None
2025-12-02 20:28:15,191 - integration.integrations.mode_management_integration - INFO - 🔄 MODE_REQUEST: current_mode=AppMode.LISTENING, target=AppMode.PROCESSING, source=input_processing
2025-12-02 20:28:15,192 - integration.integrations.mode_management_integration - INFO - 🔄 MODE_REQUEST: применяем mode → AppMode.PROCESSING
2025-12-02 20:28:15,192 - integration.core.state_manager - INFO - 🔄 Режим изменен: listening → processing
2025-12-02 20:28:15,192 - integration.core.state_manager - INFO - 🎯 TRAY DEBUG: set_mode() готов публиковать app.mode_changed: AppMode.PROCESSING, session_id=None
2025-12-02 20:28:15,192 - integration.core.state_manager - INFO - 🎯 TRAY DEBUG: EventBus подключен: True
2025-12-02 20:28:15,192 - integration.core.state_manager - INFO - 🔄 StateManager: начинаем публикацию событий (EventBus подключен, eb_loop=4700916624)
2025-12-02 20:28:15,192 - integration.core.state_manager - INFO - 🔄 StateManager: публикуем через run_coroutine_threadsafe на loop EventBus (без ожидания)
2025-12-02 20:28:15,192 - integration.core.state_manager - INFO - ✅ StateManager: события опубликованы успешно
2025-12-02 20:28:15,192 - mode_management.core.mode_controller - INFO - ✅ Режим изменен: listening → processing
2025-12-02 20:28:15,192 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: mode.request
2025-12-02 20:28:15,192 - integration.integrations.input_processing_integration - INFO - SHORT_PRESS: запрос на PROCESSING отправлен (после записи)
2025-12-02 20:28:15,192 - integration.integrations.input_processing_integration - DEBUG - SHORT_PRESS: проверяем публикацию voice.recognition_started для session 1764725284.579155
2025-12-02 20:28:15,192 - integration.integrations.input_processing_integration - DEBUG - SHORT_PRESS: удерживаем session_id=1764725284.579155 до завершения gRPC
2025-12-02 20:28:15,192 - integration.integrations.input_processing_integration - DEBUG - ✅ RELEASE: Микрофон закрыт
2025-12-02 20:28:15,192 - integration.integrations.input_processing_integration - DEBUG - 🔄 [STATE] LISTENING → PROCESSING (reason: release_after_recording)
2025-12-02 20:28:15,192 - integration.integrations.input_processing_integration - DEBUG - RELEASE: публикуем mode.request(PROCESSING) для session 1764725284.579155
2025-12-02 20:28:15,192 - integration.core.event_bus - DEBUG - EventBus: dispatch 'mode.request' to 1 subscriber(s)
2025-12-02 20:28:15,192 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'mode.request': <bound method ModeManagementIntegration._on_mode_request of <integration.integrations.mode_management_integration.ModeManagementIntegration object at 0x1183238c0>>
2025-12-02 20:28:15,192 - integration.integrations.mode_management_integration - INFO - 🔄 MODE_REQUEST: target=AppMode.PROCESSING, source=input_processing, session_id=1764725284.579155, priority=None
2025-12-02 20:28:15,192 - integration.integrations.mode_management_integration - INFO - 🔄 MODE_REQUEST: current_mode=AppMode.PROCESSING, target=AppMode.PROCESSING, source=input_processing
2025-12-02 20:28:15,192 - integration.integrations.mode_management_integration - INFO - 🔄 MODE_REQUEST: новый запрос на PROCESSING с другим session_id (active=1764725284.579155, request=1764725284.579155) - разрешаем
2025-12-02 20:28:15,192 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: mode.request
2025-12-02 20:28:15,192 - integration.integrations.input_processing_integration - INFO - RELEASE: запрос на PROCESSING отправлен ✓
2025-12-02 20:28:15,193 - integration.integrations.input_processing_integration - DEBUG - RELEASE: удерживаем session_id=1764725284.579155 до завершения gRPC
2025-12-02 20:28:15,193 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - ✅ Async callback short_press completed successfully
✅ Async callback short_press completed successfully
2025-12-02 20:28:15,193 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - ✅ Async callback release completed successfully
✅ Async callback release completed successfully
2025-12-02 20:28:15,193 - integration.core.state_manager - INFO - 🎯 TRAY DEBUG: StateManager публикует app.mode_changed: AppMode.PROCESSING (type: <enum 'AppMode'>)
2025-12-02 20:28:15,193 - integration.core.state_manager - INFO - 🎯 TRAY DEBUG: StateManager event_data: {'mode': <AppMode.PROCESSING: 'processing'>}
2025-12-02 20:28:15,193 - integration.core.event_bus - INFO - EventBus: 'app.mode_changed' → subscribers=9, data={'mode': <AppMode.PROCESSING: 'processing'>}
2025-12-02 20:28:15,193 - integration.core.event_bus - DEBUG - EventBus: dispatch 'app.mode_changed' to 9 subscriber(s)
2025-12-02 20:28:15,193 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method TrayControllerIntegration._on_mode_changed of <integration.integrations.tray_controller_integration.TrayControllerIntegration object at 0x118321be0>>
2025-12-02 20:28:15,193 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method ScreenshotCaptureIntegration._on_mode_changed of <integration.integrations.screenshot_capture_integration.ScreenshotCaptureIntegration object at 0x118323380>>
2025-12-02 20:28:15,193 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method ModeManagementIntegration._on_app_mode_changed of <integration.integrations.mode_management_integration.ModeManagementIntegration object at 0x1183238c0>>
2025-12-02 20:28:15,193 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method ProcessingWorkflow._on_mode_changed of <integration.workflows.processing_workflow.ProcessingWorkflow object at 0x1183c1fd0>>
2025-12-02 20:28:15,193 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method VoiceRecognitionIntegration._on_app_mode_changed of <integration.integrations.voice_recognition_integration.VoiceRecognitionIntegration object at 0x118323770>>
2025-12-02 20:28:15,193 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method VoiceOverDuckingIntegration.handle_mode_change of <integration.integrations.voiceover_ducking_integration.VoiceOverDuckingIntegration object at 0x1183c16a0>>
2025-12-02 20:28:15,193 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method ListeningWorkflow._on_mode_changed of <integration.workflows.listening_workflow.ListeningWorkflow object at 0x1183c1e80>>
2025-12-02 20:28:15,193 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method SimpleModuleCoordinator._on_mode_changed of <integration.core.simple_module_coordinator.SimpleModuleCoordinator object at 0x118320440>>
2025-12-02 20:28:15,193 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method UpdaterIntegration._on_mode_changed of <integration.integrations.updater_integration.UpdaterIntegration object at 0x118321fd0>>
2025-12-02 20:28:15,193 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: app.mode_changed
2025-12-02 20:28:15,193 - integration.core.state_manager - INFO - 🎯 TRAY DEBUG: StateManager app.mode_changed опубликовано успешно
2025-12-02 20:28:15,193 - integration.core.state_manager - INFO - 🎯 TRAY DEBUG: StateManager подписчиков на app.mode_changed: 9
2025-12-02 20:28:15,193 - integration.core.state_manager - INFO - 🔄 StateManager: -> publish app.state_changed: AppMode.LISTENING -> AppMode.PROCESSING
2025-12-02 20:28:15,193 - integration.core.event_bus - DEBUG - EventBus: dispatch 'app.state_changed' to 1 subscriber(s)
2025-12-02 20:28:15,194 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.state_changed': <bound method InterruptManagementIntegration._on_app_state_changed of <integration.integrations.interrupt_management_integration.InterruptManagementIntegration object at 0x118323230>>
2025-12-02 20:28:15,194 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: app.state_changed
2025-12-02 20:28:15,194 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: _on_mode_changed ВЫЗВАН!
2025-12-02 20:28:15,194 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: event type=<class 'dict'>, event={'type': 'app.mode_changed', 'data': {'mode': <AppMode.PROCESSING: 'processing'>}, 'timestamp': 212350.139119166}
2025-12-02 20:28:15,194 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: data={'mode': <AppMode.PROCESSING: 'processing'>}
2025-12-02 20:28:15,194 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: new_mode_raw=AppMode.PROCESSING (type: <enum 'AppMode'>)
2025-12-02 20:28:15,194 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: new_mode нормализован: AppMode.PROCESSING (type: <enum 'AppMode'>)
2025-12-02 20:28:15,194 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: mode_to_status={<AppMode.SLEEPING: 'sleeping'>: <TrayStatus.SLEEPING: 'sleeping'>, <AppMode.LISTENING: 'listening'>: <TrayStatus.LISTENING: 'listening'>, <AppMode.PROCESSING: 'processing'>: <TrayStatus.PROCESSING: 'processing'>}
2025-12-02 20:28:15,194 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: new_mode in mapping? True
2025-12-02 20:28:15,194 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: key=AppMode.SLEEPING (type: <enum 'AppMode'>), equals new_mode? False
2025-12-02 20:28:15,194 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: key=AppMode.LISTENING (type: <enum 'AppMode'>), equals new_mode? False
2025-12-02 20:28:15,194 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: key=AppMode.PROCESSING (type: <enum 'AppMode'>), equals new_mode? True
2025-12-02 20:28:15,194 - integration.integrations.tray_controller_integration - DEBUG - TrayIntegration: mapping mode -> status: AppMode.PROCESSING -> TrayStatus.PROCESSING
2025-12-02 20:28:15,194 - integration.core.event_bus - DEBUG - EventBus: dispatch 'tray.status_updated' to 0 subscriber(s)
2025-12-02 20:28:15,194 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: tray.status_updated
2025-12-02 20:28:15,194 - integration.integrations.tray_controller_integration - INFO - 🔄 Режим приложения изменен: processing → processing
2025-12-02 20:28:15,194 - integration.integrations.screenshot_capture_integration - INFO - 🔍 ScreenshotCapture: Получено событие app.mode_changed - mode=AppMode.PROCESSING (type: <enum 'AppMode'>)
2025-12-02 20:28:15,194 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: _apply_status_ui_sync ВЫЗВАН! status=TrayStatus.PROCESSING (type: <enum 'TrayStatus'>)
2025-12-02 20:28:15,194 - integration.integrations.screenshot_capture_integration - DEBUG - ScreenshotCaptureIntegration: already captured for session
2025-12-02 20:28:15,194 - integration.integrations.tray_controller_integration - DEBUG - 🔍 [UI] Начало обновления иконки трея: status=processing
2025-12-02 20:28:15,195 - integration.workflows.processing_workflow - DEBUG - ⚙️ ProcessingWorkflow: режим изменен на processing
2025-12-02 20:28:15,195 - integration.integrations.tray_controller_integration - DEBUG - 🔍 [UI] Предыдущий статус: listening, новый статус: processing
2025-12-02 20:28:15,195 - integration.workflows.processing_workflow - INFO - ⚙️ ProcessingWorkflow: НАЧАЛО цепочки обработки, session_id=None
2025-12-02 20:28:15,195 - integration.workflows.processing_workflow - INFO - ⚙️ ProcessingWorkflow: переход starting → capturing
2025-12-02 20:28:15,195 - integration.workflows.listening_workflow - DEBUG - 🎤 ListeningWorkflow: режим изменен на processing
🔄 Координация смены режима: processing
2025-12-02 20:28:15,195 - integration.integrations.updater_integration - INFO - Режим приложения изменен на: AppMode.PROCESSING
2025-12-02 20:28:15,195 - modules.tray_controller.core.tray_types - DEBUG - 🎯 TRAY DEBUG: TrayIconGenerator.create_circle_icon status=TrayStatus.PROCESSING (type: <enum 'TrayStatus'>)
2025-12-02 20:28:15,196 - modules.tray_controller.core.tray_types - DEBUG - 🎯 TRAY DEBUG: Available colors: {<TrayStatus.SLEEPING: 'sleeping'>: '#808080', <TrayStatus.LISTENING: 'listening'>: '#007AFF', <TrayStatus.PROCESSING: 'processing'>: '#FF9500'}
2025-12-02 20:28:15,196 - modules.tray_controller.core.tray_types - DEBUG - 🎯 TRAY DEBUG: Selected color: #FF9500
2025-12-02 20:28:15,196 - modules.tray_controller.macos.tray_icon - DEBUG - 🎯 TRAY DEBUG: create_icon_file вызван для status=TrayStatus.PROCESSING
2025-12-02 20:28:15,196 - modules.tray_controller.macos.tray_icon - DEBUG - 🎯 TRAY DEBUG: generated color=#FF9500, PIL_available=True
2025-12-02 20:28:15,196 - integration.integrations.tray_controller_integration - DEBUG - 🔍 [UI] Иконка создана: /var/folders/ys/xlx_chms3hqcs1lfyq37395c0000gn/T/tmpqy54a0f7.png, обновляем меню...
2025-12-02 20:28:15,196 - modules.tray_controller.macos.menu_handler - INFO - 🔍 ДИАГНОСТИКА update_icon: icon_path='/var/folders/ys/xlx_chms3hqcs1lfyq37395c0000gn/T/tmpqy54a0f7.png'
2025-12-02 20:28:15,196 - modules.tray_controller.macos.menu_handler - INFO - 🔍 ДИАГНОСТИКА update_icon: os.path.exists(icon_path)=True
2025-12-02 20:28:15,196 - modules.tray_controller.macos.menu_handler - INFO - 🔍 ДИАГНОСТИКА update_icon: размер файла=195 bytes
2025-12-02 20:28:15,197 - modules.tray_controller.macos.menu_handler - INFO - ✅ ДИАГНОСТИКА update_icon: Иконка обновлена успешно (попытка 1)
2025-12-02 20:28:15,197 - integration.integrations.tray_controller_integration - DEBUG - 🔍 [UI] Иконка обновлена в меню
2025-12-02 20:28:15,197 - integration.integrations.tray_controller_integration - DEBUG - 🔍 [UI] Текст статуса обновлен: Processing
2025-12-02 20:28:15,197 - integration.integrations.tray_controller_integration - INFO - ✅ Tray UI applied: listening -> processing
2025-12-02 20:28:15,197 - integration.integrations.tray_controller_integration - DEBUG - 🔍 [UI] Обновление иконки трея завершено успешно
2025-12-02 20:28:16,209 - modules.speech_playback.macos.performance - DEBUG - 📊 CPU: 13.7%, Memory: 76.1%
2025-12-02 20:28:17,173 - integration.integrations.grpc_client_integration - INFO - 🔍 gRPC response #1: WhichOneof('content')=text_chunk
2025-12-02 20:28:17,173 - integration.integrations.grpc_client_integration - INFO - gRPC received text_chunk len=37 for session 1764725284.579155
2025-12-02 20:28:17,173 - integration.core.event_bus - DEBUG - EventBus: dispatch 'grpc.response.text' to 0 subscriber(s)
2025-12-02 20:28:17,173 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: grpc.response.text
2025-12-02 20:28:17,350 - integration.integrations.grpc_client_integration - INFO - gRPC received audio_chunk bytes=297216 dtype=int16 shape=[] for session 1764725284.579155
2025-12-02 20:28:17,351 - integration.core.event_bus - DEBUG - EventBus: dispatch 'grpc.response.audio' to 1 subscriber(s)
2025-12-02 20:28:17,351 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'grpc.response.audio': <bound method SpeechPlaybackIntegration._on_audio_chunk of <integration.integrations.speech_playback_integration.SpeechPlaybackIntegration object at 0x1183c0980>>
2025-12-02 20:28:17,351 - integration.integrations.speech_playback_integration - DEBUG - 🔍 [AUDIT] _on_audio_chunk вызван: sid=1764725284.579155, handler_time=1764725297.351348
2025-12-02 20:28:17,351 - integration.core.state_manager - DEBUG - 🔄 Session ID обновлен (без публикации события): 1764725284.579155 → 1764725284.579155
2025-12-02 20:28:17,351 - integration.integrations.speech_playback_integration - INFO - 🔊 Получен аудио чанк: 297216 bytes, dtype=int16, shape=[], sr=None, ch=None для сессии 1764725284.579155, hash=965960905874858417
2025-12-02 20:28:17,352 - integration.integrations.speech_playback_integration - INFO - 🔍 audio_chunk: sid=1764725284.579155, in_dtype='int16', dec_dtype=int16, shape=(148608,), min=-19166.000, max=20652.000, bytes=297216
2025-12-02 20:28:17,352 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Запрашиваем системное default output устройство...
2025-12-02 20:28:17,352 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] ШАГ 1.2: Определение устройства через macOS API (приоритет 1)
2025-12-02 20:28:17,352 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Используем SwitchAudioSource: /opt/homebrew/bin/SwitchAudioSource
2025-12-02 20:28:17,352 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Запрос текущего default output устройства...
I0000 00:00:1764725297.353242 4787285 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-02 20:28:17,482 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Команда выполнена: returncode=0, stdout_len=94, stderr_len=0
2025-12-02 20:28:17,482 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Получен JSON: {'name': 'Sergiy’s AirPods', 'type': 'output', 'id': '85', 'uid': '1C-77-54-18-C8-A3:output'}
2025-12-02 20:28:17,482 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] macOS default OUTPUT (через SwitchAudioSource): "Sergiy’s AirPods"
2025-12-02 20:28:17,482 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Успешно получено имя устройства: Sergiy’s AirPods
2025-12-02 20:28:17,482 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] macOS default OUTPUT (источник истины): "Sergiy’s AirPods"
2025-12-02 20:28:17,482 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Найден ID для 'Sergiy’s AirPods': 1
2025-12-02 20:28:17,482 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Найдено устройство через SwitchAudioSource: name=Sergiy’s AirPods, id=1
2025-12-02 20:28:17,482 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Найдено default output устройство (через SwitchAudioSource):
2025-12-02 20:28:17,482 - modules.speech_playback.core.player - INFO -    Name: Sergiy’s AirPods
2025-12-02 20:28:17,482 - modules.speech_playback.core.player - INFO -    Index: 1
2025-12-02 20:28:17,483 - modules.speech_playback.core.player - INFO -    Max Output Channels: 2
2025-12-02 20:28:17,483 - modules.speech_playback.core.player - INFO -    Default Sample Rate: 48000.0 Hz
2025-12-02 20:28:17,483 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Полная информация: {'name': 'Sergiy’s AirPods', 'index': 1, 'hostapi': 0, 'max_input_channels': 0, 'max_output_channels': 2, 'default_low_input_latency': 0.01, 'default_low_output_latency': 0.16133333333333333, 'default_high_input_latency': 0.1, 'default_high_output_latency': 0.17066666666666666, 'default_samplerate': 48000.0}
2025-12-02 20:28:17,483 - modules.speech_playback.core.player - INFO - 🎯 [AUDIO_REFACTOR] Начало инициализации Sequential Speech Player...
2025-12-02 20:28:17,483 - modules.speech_playback.core.player - DEBUG - 🔍 [AUDIO_DEBUG] Инициализация Core Audio Manager...
2025-12-02 20:28:17,483 - modules.speech_playback.macos.core_audio - INFO - ✅ Core Audio инициализирован
2025-12-02 20:28:17,483 - modules.speech_playback.core.player - INFO - ✅ [AUDIO_SUCCESS] Core Audio Manager инициализирован
2025-12-02 20:28:17,483 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Запрашиваем системное default output устройство...
2025-12-02 20:28:17,483 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] ШАГ 1.2: Определение устройства через macOS API (приоритет 1)
2025-12-02 20:28:17,483 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Используем SwitchAudioSource: /opt/homebrew/bin/SwitchAudioSource
2025-12-02 20:28:17,483 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Запрос текущего default output устройства...
I0000 00:00:1764725297.483725 4787285 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-02 20:28:17,574 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Команда выполнена: returncode=0, stdout_len=94, stderr_len=0
2025-12-02 20:28:17,574 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Получен JSON: {'name': 'Sergiy’s AirPods', 'type': 'output', 'id': '85', 'uid': '1C-77-54-18-C8-A3:output'}
2025-12-02 20:28:17,574 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] macOS default OUTPUT (через SwitchAudioSource): "Sergiy’s AirPods"
2025-12-02 20:28:17,575 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Успешно получено имя устройства: Sergiy’s AirPods
2025-12-02 20:28:17,575 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] macOS default OUTPUT (источник истины): "Sergiy’s AirPods"
2025-12-02 20:28:17,575 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Найден ID для 'Sergiy’s AirPods': 1
2025-12-02 20:28:17,575 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Найдено устройство через SwitchAudioSource: name=Sergiy’s AirPods, id=1
2025-12-02 20:28:17,575 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Найдено default output устройство (через SwitchAudioSource):
2025-12-02 20:28:17,575 - modules.speech_playback.core.player - INFO -    Name: Sergiy’s AirPods
2025-12-02 20:28:17,575 - modules.speech_playback.core.player - INFO -    Index: 1
2025-12-02 20:28:17,575 - modules.speech_playback.core.player - INFO -    Max Output Channels: 2
2025-12-02 20:28:17,575 - modules.speech_playback.core.player - INFO -    Default Sample Rate: 48000.0 Hz
2025-12-02 20:28:17,575 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Полная информация: {'name': 'Sergiy’s AirPods', 'index': 1, 'hostapi': 0, 'max_input_channels': 0, 'max_output_channels': 2, 'default_low_input_latency': 0.01, 'default_low_output_latency': 0.16133333333333333, 'default_high_input_latency': 0.1, 'default_high_output_latency': 0.17066666666666666, 'default_samplerate': 48000.0}
2025-12-02 20:28:17,575 - modules.speech_playback.core.player - INFO - 🎯 Используем системное устройство по умолчанию от macOS
2025-12-02 20:28:17,575 - modules.speech_playback.core.player - INFO - 📊 [AUDIO_STATS] Конфигурация плеера: sample_rate=48000Hz, channels=2, dtype=int16
2025-12-02 20:28:17,575 - modules.speech_playback.macos.performance - WARNING - ⚠️ Мониторинг уже запущен
2025-12-02 20:28:17,575 - modules.speech_playback.core.player - INFO - ✅ [AUDIO_SUCCESS] Sequential Speech Player инициализирован успешно
2025-12-02 20:28:17,575 - modules.speech_playback.core.player - WARNING - ⚠️ Состояние ERROR, сбрасываем в IDLE для повторной попытки
2025-12-02 20:28:17,575 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] _start_audio_stream вызван: sync_output=True, device_id=None
2025-12-02 20:28:17,576 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Текущая конфигурация: rate=48000Hz, channels=2, dtype=int16, buffer_size=512
2025-12-02 20:28:17,576 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Синхронизируем формат с устройством...
2025-12-02 20:28:17,576 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Запрашиваем системное default output устройство...
2025-12-02 20:28:17,576 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] ШАГ 1.2: Определение устройства через macOS API (приоритет 1)
2025-12-02 20:28:17,576 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Используем SwitchAudioSource: /opt/homebrew/bin/SwitchAudioSource
2025-12-02 20:28:17,576 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Запрос текущего default output устройства...
I0000 00:00:1764725297.576778 4787285 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-02 20:28:17,672 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Команда выполнена: returncode=0, stdout_len=94, stderr_len=0
2025-12-02 20:28:17,672 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Получен JSON: {'name': 'Sergiy’s AirPods', 'type': 'output', 'id': '85', 'uid': '1C-77-54-18-C8-A3:output'}
2025-12-02 20:28:17,672 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] macOS default OUTPUT (через SwitchAudioSource): "Sergiy’s AirPods"
2025-12-02 20:28:17,672 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Успешно получено имя устройства: Sergiy’s AirPods
2025-12-02 20:28:17,672 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] macOS default OUTPUT (источник истины): "Sergiy’s AirPods"
2025-12-02 20:28:17,672 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Найден ID для 'Sergiy’s AirPods': 1
2025-12-02 20:28:17,672 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Найдено устройство через SwitchAudioSource: name=Sergiy’s AirPods, id=1
2025-12-02 20:28:17,672 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Найдено default output устройство (через SwitchAudioSource):
2025-12-02 20:28:17,673 - modules.speech_playback.core.player - INFO -    Name: Sergiy’s AirPods
2025-12-02 20:28:17,673 - modules.speech_playback.core.player - INFO -    Index: 1
2025-12-02 20:28:17,673 - modules.speech_playback.core.player - INFO -    Max Output Channels: 2
2025-12-02 20:28:17,673 - modules.speech_playback.core.player - INFO -    Default Sample Rate: 48000.0 Hz
2025-12-02 20:28:17,673 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Полная информация: {'name': 'Sergiy’s AirPods', 'index': 1, 'hostapi': 0, 'max_input_channels': 0, 'max_output_channels': 2, 'default_low_input_latency': 0.01, 'default_low_output_latency': 0.16133333333333333, 'default_high_input_latency': 0.1, 'default_high_output_latency': 0.17066666666666666, 'default_samplerate': 48000.0}
2025-12-02 20:28:17,673 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] После синхронизации: rate=48000Hz, channels=2
2025-12-02 20:28:17,673 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] device_id не передан, получаем устройство через macOS API (SwitchAudioSource)...
2025-12-02 20:28:17,673 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Fallback на SwitchAudioSource (device_id не передан)
2025-12-02 20:28:17,673 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Запрашиваем системное default output устройство...
2025-12-02 20:28:17,673 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] ШАГ 1.2: Определение устройства через macOS API (приоритет 1)
2025-12-02 20:28:17,673 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Используем SwitchAudioSource: /opt/homebrew/bin/SwitchAudioSource
2025-12-02 20:28:17,673 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Запрос текущего default output устройства...
I0000 00:00:1764725297.674143 4787285 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
I0000 00:00:1764725297.721380 4787424 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-02 20:28:17,822 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Команда выполнена: returncode=0, stdout_len=94, stderr_len=0
2025-12-02 20:28:17,823 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Получен JSON: {'name': 'Sergiy’s AirPods', 'type': 'output', 'id': '85', 'uid': '1C-77-54-18-C8-A3:output'}
2025-12-02 20:28:17,823 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] macOS default OUTPUT (через SwitchAudioSource): "Sergiy’s AirPods"
2025-12-02 20:28:17,823 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Успешно получено имя устройства: Sergiy’s AirPods
2025-12-02 20:28:17,823 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] macOS default OUTPUT (источник истины): "Sergiy’s AirPods"
2025-12-02 20:28:17,823 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Найден ID для 'Sergiy’s AirPods': 1
2025-12-02 20:28:17,823 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Найдено устройство через SwitchAudioSource: name=Sergiy’s AirPods, id=1
2025-12-02 20:28:17,823 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Найдено default output устройство (через SwitchAudioSource):
2025-12-02 20:28:17,823 - modules.speech_playback.core.player - INFO -    Name: Sergiy’s AirPods
2025-12-02 20:28:17,823 - modules.speech_playback.core.player - INFO -    Index: 1
2025-12-02 20:28:17,823 - modules.speech_playback.core.player - INFO -    Max Output Channels: 2
2025-12-02 20:28:17,823 - modules.speech_playback.core.player - INFO -    Default Sample Rate: 48000.0 Hz
2025-12-02 20:28:17,823 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Полная информация: {'name': 'Sergiy’s AirPods', 'index': 1, 'hostapi': 0, 'max_input_channels': 0, 'max_output_channels': 2, 'default_low_input_latency': 0.01, 'default_low_output_latency': 0.16133333333333333, 'default_high_input_latency': 0.1, 'default_high_output_latency': 0.17066666666666666, 'default_samplerate': 48000.0}
2025-12-02 20:28:17,823 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] macOS API (источник истины): "Sergiy’s AirPods" (ID=1)
2025-12-02 20:28:17,823 - modules.speech_playback.core.player - INFO - 🔧 [OUTPUT] BT устройство обнаружено: "Sergiy’s AirPods"
2025-12-02 20:28:17,823 - modules.speech_playback.core.player - INFO - 💡 [OUTPUT] SwitchAudioSource → device=None для BT (macOS управляет параметрами)
2025-12-02 20:28:17,824 - modules.speech_playback.core.player - DEBUG - 💡 [OUTPUT] BT устройство "Sergiy’s AirPods" - пропускаем DeviceParamsNormalizer, доверяем macOS параметрам
2025-12-02 20:28:17,824 - modules.speech_playback.core.player - INFO - 💡 [OUTPUT] SwitchAudioSource → "Sergiy’s AirPods" (BT устройство)
2025-12-02 20:28:17,824 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] BT устройство: используем device=None (НЕ используем PortAudio ID)
2025-12-02 20:28:17,824 - modules.speech_playback.core.stream_config_resolver - INFO - 💡 [OUTPUT] SwitchAudioSource → "Sergiy’s AirPods" (BT устройство)
2025-12-02 20:28:17,824 - modules.speech_playback.core.stream_config_resolver - INFO - ✅ [OUTPUT] BT устройство: используем device=None (НЕ используем PortAudio ID)
2025-12-02 20:28:17,824 - modules.speech_playback.core.stream_config_resolver - INFO - 🔧 [OUTPUT] BT устройство: используем channels=1 (обязательно), НЕ задаем blocksize, latency (пусть macOS/PortAudio выберут сами)
2025-12-02 20:28:17,824 - modules.speech_playback.core.player - INFO - 🔧 [OUTPUT] BT устройство: используем channels=1 (обязательно), НЕ задаем blocksize, latency (пусть macOS/PortAudio выберут сами)
2025-12-02 20:28:17,824 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Конфигурация потока:
2025-12-02 20:28:17,824 - modules.speech_playback.core.player - INFO -    device: None
2025-12-02 20:28:17,824 - modules.speech_playback.core.player - INFO -    channels: 1
2025-12-02 20:28:17,824 - modules.speech_playback.core.player - INFO -    dtype: int16
2025-12-02 20:28:17,824 - modules.speech_playback.core.player - INFO -    samplerate: 48000 Hz
2025-12-02 20:28:17,824 - modules.speech_playback.core.player - INFO -    blocksize: N/A (не задан, пусть PortAudio выберет)
2025-12-02 20:28:17,824 - modules.speech_playback.core.player - INFO -    latency: N/A (не задан, пусть PortAudio выберет)
2025-12-02 20:28:17,824 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Создаём поток для устройства: Sergiy’s AirPods (ID=System Default)
2025-12-02 20:28:17,824 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Пропускаем проверку доступности (device_id=None, device_id_actual=System Default)
2025-12-02 20:28:17,824 - modules.speech_playback.core.player - INFO - ⏳ [OUTPUT] Bluetooth устройство обнаружено, ожидание готовности CoreAudio pipeline (2.5с)...
2025-12-02 20:28:17,832 - modules.audio_core.device_change_publisher - DEBUG - ✅ [INPUT] macOS default (через SwitchAudioSource): "Sergiy’s AirPods"
I0000 00:00:1764725297.833431 4787424 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-02 20:28:17,929 - modules.audio_core.device_change_publisher - DEBUG - ✅ [OUTPUT] macOS default (через SwitchAudioSource): "Sergiy’s AirPods"
2025-12-02 20:28:18,035 - modules.voice_recognition.core.speech_recognizer - DEBUG - ⚠️ Ошибка закрытия потока через AudioStreamManager: 
2025-12-02 20:28:18,036 - modules.voice_recognition.core.speech_recognizer - DEBUG - 🧹 Аудио поток очищен (_current_stream = None)
2025-12-02 20:28:18,036 - modules.voice_recognition.core.speech_recognizer - DEBUG - 🧹 Аудио поток очищен (_current_stream = None)
2025-12-02 20:28:20,328 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Начинаем создание потока (max_retries=5, base_delay=0.3s, BT=True)...
2025-12-02 20:28:20,329 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Подтверждение: старый поток полностью закрыт (_audio_stream=None)
2025-12-02 20:28:20,329 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Подтверждение: старый поток закрыт → создаём новый stream
2025-12-02 20:28:20,329 - modules.speech_playback.core.player - INFO -    Устройство: Sergiy’s AirPods (ID=System Default, BT=True)
2025-12-02 20:28:20,329 - modules.speech_playback.core.player - INFO -    Параметры: device=None, channels=1, samplerate=48000, blocksize=N/A, latency=N/A
2025-12-02 20:28:20,329 - modules.speech_playback.core.player - INFO -    SwitchAudioSource → device=None для BT (macOS управляет параметрами)
2025-12-02 20:28:20,329 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Попытка 1/5 создания потока...
2025-12-02 20:28:20,329 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Параметры потока: {'device': None, 'channels': 1, 'dtype': 'int16', 'samplerate': 48000, 'callback': <bound method SequentialSpeechPlayer._audio_callback of <modules.speech_playback.core.player.SequentialSpeechPlayer object at 0x118389fd0>>}
2025-12-02 20:28:20,329 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Попытка 2/5 создания потока...
2025-12-02 20:28:20,329 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Параметры потока: {'device': None, 'channels': 1, 'dtype': 'int16', 'samplerate': 48000, 'callback': <bound method SequentialSpeechPlayer._audio_callback of <modules.speech_playback.core.player.SequentialSpeechPlayer object at 0x118389fd0>>}
2025-12-02 20:28:20,329 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Попытка 3/5 создания потока...
2025-12-02 20:28:20,329 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Параметры потока: {'device': None, 'channels': 1, 'dtype': 'int16', 'samplerate': 48000, 'callback': <bound method SequentialSpeechPlayer._audio_callback of <modules.speech_playback.core.player.SequentialSpeechPlayer object at 0x118389fd0>>}
2025-12-02 20:28:20,329 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Попытка 4/5 создания потока...
2025-12-02 20:28:20,329 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Параметры потока: {'device': None, 'channels': 1, 'dtype': 'int16', 'samplerate': 48000, 'callback': <bound method SequentialSpeechPlayer._audio_callback of <modules.speech_playback.core.player.SequentialSpeechPlayer object at 0x118389fd0>>}
2025-12-02 20:28:20,329 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Попытка 5/5 создания потока...
2025-12-02 20:28:20,329 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Параметры потока: {'device': None, 'channels': 1, 'dtype': 'int16', 'samplerate': 48000, 'callback': <bound method SequentialSpeechPlayer._audio_callback of <modules.speech_playback.core.player.SequentialSpeechPlayer object at 0x118389fd0>>}
2025-12-02 20:28:20,329 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Последний host error code: -10851
2025-12-02 20:28:20,329 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Создаем новый поток через AudioStreamManager: device=None, BT=True
2025-12-02 20:28:20,329 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Запускаем create_stream (_start_audio_stream) в отдельном thread (timeout=5.0с)...
2025-12-02 20:28:20,330 - asyncio - DEBUG - Using selector: KqueueSelector
2025-12-02 20:28:20,330 - modules.audio_core.stream_manager - INFO - 🔍 [OUTPUT] create_stream ВХОД: device=None (Sergiy’s AirPods), BT=True, max_retries=2
2025-12-02 20:28:20,330 - modules.audio_core.stream_manager - DEBUG - 🔍 [OUTPUT] create_stream: пытаемся захватить lock...
2025-12-02 20:28:20,330 - modules.audio_core.stream_manager - DEBUG - ✅ [OUTPUT] create_stream: lock захвачен (время ожидания: 0.0ms), начинаем создание потока
2025-12-02 20:28:20,330 - modules.audio_core.stream_manager - INFO - 🔄 [OUTPUT] Попытка 1/2 создания потока:
   device_id=None, device_name=Sergiy’s AirPods
   samplerate=48000Hz, channels=1
   dtype=int16, blocksize=None, latency=None
   is_bluetooth=True, callback=True
2025-12-02 20:28:20,330 - modules.audio_core.stream_manager - DEBUG - 🔍 [OUTPUT] Подготавливаем параметры потока...
2025-12-02 20:28:20,330 - modules.audio_core.stream_manager - DEBUG - 🔍 [OUTPUT] Параметры подготовлены: {'device': None, 'samplerate': 48000, 'channels': 1, 'dtype': 'int16', 'callback': <bound method SequentialSpeechPlayer._audio_callback of <modules.speech_playback.core.player.SequentialSpeechPlayer object at 0x118389fd0>>}
2025-12-02 20:28:20,330 - modules.audio_core.stream_manager - DEBUG - 🔍 [OUTPUT] Создаем output поток через PortAudio...
||PaMacCore (AUHAL)|| Warning on line 521: err=''!obj'', msg=Unknown Error
||PaMacCore (AUHAL)|| Warning on line 441: err=''!obj'', msg=Unknown Error
||PaMacCore (AUHAL)|| Error on line 1332: err='-10851', msg=Audio Unit: Invalid Property Value
2025-12-02 20:28:20,332 - modules.audio_core.stream_manager - WARNING - ⚠️ [OUTPUT] Ошибка создания потока на попытке 1: Error opening OutputStream: Internal PortAudio error [PaErrorCode -9986] (код: Error opening OutputStream: Internal PortAudio error). Повтор через 1.0с
2025-12-02 20:28:21,333 - modules.audio_core.stream_manager - INFO - 🔄 [OUTPUT] Попытка 2/2 создания потока:
   device_id=None, device_name=Sergiy’s AirPods
   samplerate=48000Hz, channels=1
   dtype=int16, blocksize=None, latency=None
   is_bluetooth=True, callback=True
2025-12-02 20:28:21,333 - modules.audio_core.stream_manager - DEBUG - 🔍 [OUTPUT] Подготавливаем параметры потока...
2025-12-02 20:28:21,333 - modules.audio_core.stream_manager - DEBUG - 🔍 [OUTPUT] Параметры подготовлены: {'device': None, 'samplerate': 48000, 'channels': 1, 'dtype': 'int16', 'callback': <bound method SequentialSpeechPlayer._audio_callback of <modules.speech_playback.core.player.SequentialSpeechPlayer object at 0x118389fd0>>}
2025-12-02 20:28:21,333 - modules.audio_core.stream_manager - DEBUG - 🔍 [OUTPUT] Создаем output поток через PortAudio...
||PaMacCore (AUHAL)|| Warning on line 521: err=''!obj'', msg=Unknown Error
||PaMacCore (AUHAL)|| Warning on line 441: err=''!obj'', msg=Unknown Error
||PaMacCore (AUHAL)|| Error on line 1332: err='-10851', msg=Audio Unit: Invalid Property Value
2025-12-02 20:28:21,335 - modules.audio_core.stream_manager - ERROR - ❌ [OUTPUT] Не удалось создать поток после 2 попыток: Error opening OutputStream: Internal PortAudio error [PaErrorCode -9986] (код: Error opening OutputStream: Internal PortAudio error)
2025-12-02 20:28:21,335 - modules.speech_playback.core.player - DEBUG - ✅ [OUTPUT] create_stream (_start_audio_stream) завершен успешно
2025-12-02 20:28:21,335 - modules.speech_playback.core.player - WARNING - ⚠️ [OUTPUT] Обнаружена ошибка -10851 (Invalid Property Value) - сохраняем конфигурацию для кэша
2025-12-02 20:28:21,336 - modules.speech_playback.core.player - ERROR - ❌ [OUTPUT] Попытка 5/5 создания потока не удалась (время: 1.01с)
2025-12-02 20:28:21,336 - modules.speech_playback.core.player - ERROR -    Устройство: Sergiy’s AirPods (ID=System Default, BT=True)
2025-12-02 20:28:21,336 - modules.speech_playback.core.player - ERROR -    Параметры: device=None, channels=1, samplerate=48000, blocksize=N/A, latency=N/A
2025-12-02 20:28:21,336 - modules.speech_playback.core.player - ERROR -    Ошибка: RuntimeError: Не удалось создать поток через AudioStreamManager: Error opening OutputStream: Internal PortAudio error [PaErrorCode -9986]
2025-12-02 20:28:21,336 - modules.speech_playback.core.player - ERROR -    is_error_9986=True, is_error_10851=True
2025-12-02 20:28:21,336 - modules.speech_playback.core.player - WARNING - ⚠️ [OUTPUT] Обнаружена ошибка -10851 (Invalid Property Value) для BT устройства
2025-12-02 20:28:21,336 - modules.speech_playback.core.player - INFO - 💡 [OUTPUT] Переключаемся на системный дефолт (device=None) БЕЗ параметров буферизации
2025-12-02 20:28:21,336 - modules.speech_playback.core.player - INFO - 🔧 [OUTPUT] Для BT устройства убраны все параметры буферизации (пусть PortAudio выберет сам)
2025-12-02 20:28:21,336 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Обновлённая конфигурация для BT: {'device': None, 'channels': 1, 'dtype': 'int16', 'samplerate': 48000, 'callback': <bound method SequentialSpeechPlayer._audio_callback of <modules.speech_playback.core.player.SequentialSpeechPlayer object at 0x118389fd0>>}
2025-12-02 20:28:21,336 - modules.speech_playback.core.player - WARNING - ⚠️ [OUTPUT] Обнаружена ошибка -9986 (Internal PortAudio error) - устройство может быть занято
2025-12-02 20:28:21,336 - modules.speech_playback.core.player - INFO - 💡 [OUTPUT] Рекомендация: убедитесь, что старый поток полностью закрыт
2025-12-02 20:28:21,336 - modules.speech_playback.core.player - DEBUG -    Детали ошибки:
Traceback (most recent call last):
  File "/Users/sergiyzasorin/Development/Nexy/client(prod)/modules/speech_playback/core/player.py", line 937, in _start_audio_stream
    raise RuntimeError(f"Не удалось создать поток через AudioStreamManager: {result.error_message}")
RuntimeError: Не удалось создать поток через AudioStreamManager: Error opening OutputStream: Internal PortAudio error [PaErrorCode -9986]
2025-12-02 20:28:21,337 - modules.speech_playback.core.player - WARNING - ⚠️ [OUTPUT] Ошибка -9986: устройство может быть занято старым потоком
2025-12-02 20:28:21,337 - modules.speech_playback.core.player - INFO - 🔄 [OUTPUT] Вызываем _stop_audio_stream() для гарантированного освобождения устройства...
2025-12-02 20:28:21,337 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Используем is_bluetooth=True из текущей попытки (устройство: "Sergiy’s AirPods")
2025-12-02 20:28:21,337 - modules.speech_playback.core.player - INFO - ⏳ [OUTPUT] Задержка для освобождения устройства после ошибки: 1.0с...
2025-12-02 20:28:22,342 - modules.speech_playback.core.player - INFO - 🔄 [OUTPUT] Для BT устройства создаем stream с device=None (macOS управляет параметрами)
2025-12-02 20:28:22,343 - modules.speech_playback.core.player - INFO - 🔧 [OUTPUT] Для BT устройства: device=None, channels=1, без blocksize/latency
2025-12-02 20:28:22,343 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Устройство должно быть освобождено после ошибки -9986
2025-12-02 20:28:22,343 - modules.speech_playback.core.player - INFO - 💾 [OUTPUT] Сохранена безопасная конфигурация для "Sergiy’s AirPods" после ошибки -10851
2025-12-02 20:28:22,343 - modules.speech_playback.core.player - ERROR - ❌ [OUTPUT] Все 5 попытки создания потока не удались
2025-12-02 20:28:22,343 - modules.speech_playback.core.player - ERROR - ❌ Ошибка создания аудио потока: Не удалось создать поток через AudioStreamManager: Error opening OutputStream: Internal PortAudio error [PaErrorCode -9986]
2025-12-02 20:28:22,343 - integration.core.error_handler - ERROR - ❌ UNKNOWN: start_failed
2025-12-02 20:28:22,343 - integration.core.event_bus - DEBUG - EventBus: dispatch 'error.occurred' to 0 subscriber(s)
2025-12-02 20:28:22,343 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: error.occurred
2025-12-02 20:28:22,343 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: grpc.response.audio
2025-12-02 20:28:22,344 - integration.integrations.grpc_client_integration - INFO - gRPC received text_chunk len=25 for session 1764725284.579155
2025-12-02 20:28:22,344 - integration.core.event_bus - DEBUG - EventBus: dispatch 'grpc.response.text' to 0 subscriber(s)
2025-12-02 20:28:22,344 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: grpc.response.text
2025-12-02 20:28:22,344 - integration.integrations.grpc_client_integration - INFO - gRPC received audio_chunk bytes=211968 dtype=int16 shape=[] for session 1764725284.579155
2025-12-02 20:28:22,344 - integration.core.event_bus - DEBUG - EventBus: dispatch 'grpc.response.audio' to 1 subscriber(s)
2025-12-02 20:28:22,344 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'grpc.response.audio': <bound method SpeechPlaybackIntegration._on_audio_chunk of <integration.integrations.speech_playback_integration.SpeechPlaybackIntegration object at 0x1183c0980>>
2025-12-02 20:28:22,344 - integration.integrations.speech_playback_integration - DEBUG - 🔍 [AUDIT] _on_audio_chunk вызван: sid=1764725284.579155, handler_time=1764725302.344938
2025-12-02 20:28:22,345 - integration.integrations.speech_playback_integration - INFO - 🔊 Получен аудио чанк: 211968 bytes, dtype=int16, shape=[], sr=None, ch=None для сессии 1764725284.579155, hash=965960905874858417
2025-12-02 20:28:22,345 - integration.integrations.speech_playback_integration - INFO - 🔍 audio_chunk: sid=1764725284.579155, in_dtype='int16', dec_dtype=int16, shape=(105984,), min=-19506.000, max=20238.000, bytes=211968
2025-12-02 20:28:22,345 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Запрашиваем системное default output устройство...
2025-12-02 20:28:22,345 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] ШАГ 1.2: Определение устройства через macOS API (приоритет 1)
2025-12-02 20:28:22,345 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Используем SwitchAudioSource: /opt/homebrew/bin/SwitchAudioSource
2025-12-02 20:28:22,345 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Запрос текущего default output устройства...
I0000 00:00:1764725302.346248 4787285 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-02 20:28:22,481 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Команда выполнена: returncode=0, stdout_len=94, stderr_len=0
2025-12-02 20:28:22,482 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Получен JSON: {'name': 'Sergiy’s AirPods', 'type': 'output', 'id': '85', 'uid': '1C-77-54-18-C8-A3:output'}
2025-12-02 20:28:22,482 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] macOS default OUTPUT (через SwitchAudioSource): "Sergiy’s AirPods"
2025-12-02 20:28:22,482 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Успешно получено имя устройства: Sergiy’s AirPods
2025-12-02 20:28:22,482 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] macOS default OUTPUT (источник истины): "Sergiy’s AirPods"
2025-12-02 20:28:22,482 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Найден ID для 'Sergiy’s AirPods': 1
2025-12-02 20:28:22,482 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Найдено устройство через SwitchAudioSource: name=Sergiy’s AirPods, id=1
2025-12-02 20:28:22,482 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Найдено default output устройство (через SwitchAudioSource):
2025-12-02 20:28:22,482 - modules.speech_playback.core.player - INFO -    Name: Sergiy’s AirPods
2025-12-02 20:28:22,482 - modules.speech_playback.core.player - INFO -    Index: 1
2025-12-02 20:28:22,482 - modules.speech_playback.core.player - INFO -    Max Output Channels: 2
2025-12-02 20:28:22,482 - modules.speech_playback.core.player - INFO -    Default Sample Rate: 48000.0 Hz
2025-12-02 20:28:22,482 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Полная информация: {'name': 'Sergiy’s AirPods', 'index': 1, 'hostapi': 0, 'max_input_channels': 0, 'max_output_channels': 2, 'default_low_input_latency': 0.01, 'default_low_output_latency': 0.16133333333333333, 'default_high_input_latency': 0.1, 'default_high_output_latency': 0.17066666666666666, 'default_samplerate': 48000.0}
2025-12-02 20:28:22,482 - modules.speech_playback.core.player - INFO - 🎯 [AUDIO_REFACTOR] Начало инициализации Sequential Speech Player...
2025-12-02 20:28:22,482 - modules.speech_playback.core.player - DEBUG - 🔍 [AUDIO_DEBUG] Инициализация Core Audio Manager...
2025-12-02 20:28:22,482 - modules.speech_playback.macos.core_audio - INFO - ✅ Core Audio инициализирован
2025-12-02 20:28:22,483 - modules.speech_playback.core.player - INFO - ✅ [AUDIO_SUCCESS] Core Audio Manager инициализирован
2025-12-02 20:28:22,483 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Запрашиваем системное default output устройство...
2025-12-02 20:28:22,483 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] ШАГ 1.2: Определение устройства через macOS API (приоритет 1)
2025-12-02 20:28:22,483 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Используем SwitchAudioSource: /opt/homebrew/bin/SwitchAudioSource
2025-12-02 20:28:22,483 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Запрос текущего default output устройства...
I0000 00:00:1764725302.483524 4787285 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-02 20:28:22,577 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Команда выполнена: returncode=0, stdout_len=94, stderr_len=0
2025-12-02 20:28:22,578 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Получен JSON: {'name': 'Sergiy’s AirPods', 'type': 'output', 'id': '85', 'uid': '1C-77-54-18-C8-A3:output'}
2025-12-02 20:28:22,578 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] macOS default OUTPUT (через SwitchAudioSource): "Sergiy’s AirPods"
2025-12-02 20:28:22,578 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Успешно получено имя устройства: Sergiy’s AirPods
2025-12-02 20:28:22,578 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] macOS default OUTPUT (источник истины): "Sergiy’s AirPods"
2025-12-02 20:28:22,578 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Найден ID для 'Sergiy’s AirPods': 1
2025-12-02 20:28:22,578 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Найдено устройство через SwitchAudioSource: name=Sergiy’s AirPods, id=1
2025-12-02 20:28:22,578 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Найдено default output устройство (через SwitchAudioSource):
2025-12-02 20:28:22,578 - modules.speech_playback.core.player - INFO -    Name: Sergiy’s AirPods
2025-12-02 20:28:22,578 - modules.speech_playback.core.player - INFO -    Index: 1
2025-12-02 20:28:22,579 - modules.speech_playback.core.player - INFO -    Max Output Channels: 2
2025-12-02 20:28:22,579 - modules.speech_playback.core.player - INFO -    Default Sample Rate: 48000.0 Hz
2025-12-02 20:28:22,579 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Полная информация: {'name': 'Sergiy’s AirPods', 'index': 1, 'hostapi': 0, 'max_input_channels': 0, 'max_output_channels': 2, 'default_low_input_latency': 0.01, 'default_low_output_latency': 0.16133333333333333, 'default_high_input_latency': 0.1, 'default_high_output_latency': 0.17066666666666666, 'default_samplerate': 48000.0}
2025-12-02 20:28:22,579 - modules.speech_playback.core.player - INFO - 🎯 Используем системное устройство по умолчанию от macOS
2025-12-02 20:28:22,579 - modules.speech_playback.core.player - INFO - 📊 [AUDIO_STATS] Конфигурация плеера: sample_rate=48000Hz, channels=2, dtype=int16
2025-12-02 20:28:22,579 - modules.speech_playback.macos.performance - WARNING - ⚠️ Мониторинг уже запущен
2025-12-02 20:28:22,579 - modules.speech_playback.core.player - INFO - ✅ [AUDIO_SUCCESS] Sequential Speech Player инициализирован успешно
2025-12-02 20:28:22,579 - modules.speech_playback.core.player - WARNING - ⚠️ Состояние ERROR, сбрасываем в IDLE для повторной попытки
2025-12-02 20:28:22,579 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] _start_audio_stream вызван: sync_output=True, device_id=None
2025-12-02 20:28:22,579 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Текущая конфигурация: rate=48000Hz, channels=2, dtype=int16, buffer_size=512
2025-12-02 20:28:22,579 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Синхронизируем формат с устройством...
2025-12-02 20:28:22,579 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Запрашиваем системное default output устройство...
2025-12-02 20:28:22,579 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] ШАГ 1.2: Определение устройства через macOS API (приоритет 1)
2025-12-02 20:28:22,580 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Используем SwitchAudioSource: /opt/homebrew/bin/SwitchAudioSource
2025-12-02 20:28:22,580 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Запрос текущего default output устройства...
I0000 00:00:1764725302.580469 4787285 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-02 20:28:22,676 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Команда выполнена: returncode=0, stdout_len=94, stderr_len=0
2025-12-02 20:28:22,677 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Получен JSON: {'name': 'Sergiy’s AirPods', 'type': 'output', 'id': '85', 'uid': '1C-77-54-18-C8-A3:output'}
2025-12-02 20:28:22,677 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] macOS default OUTPUT (через SwitchAudioSource): "Sergiy’s AirPods"
2025-12-02 20:28:22,677 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Успешно получено имя устройства: Sergiy’s AirPods
2025-12-02 20:28:22,677 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] macOS default OUTPUT (источник истины): "Sergiy’s AirPods"
2025-12-02 20:28:22,677 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Найден ID для 'Sergiy’s AirPods': 1
2025-12-02 20:28:22,677 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Найдено устройство через SwitchAudioSource: name=Sergiy’s AirPods, id=1
2025-12-02 20:28:22,677 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Найдено default output устройство (через SwitchAudioSource):
2025-12-02 20:28:22,677 - modules.speech_playback.core.player - INFO -    Name: Sergiy’s AirPods
2025-12-02 20:28:22,678 - modules.speech_playback.core.player - INFO -    Index: 1
2025-12-02 20:28:22,678 - modules.speech_playback.core.player - INFO -    Max Output Channels: 2
2025-12-02 20:28:22,678 - modules.speech_playback.core.player - INFO -    Default Sample Rate: 48000.0 Hz
2025-12-02 20:28:22,678 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Полная информация: {'name': 'Sergiy’s AirPods', 'index': 1, 'hostapi': 0, 'max_input_channels': 0, 'max_output_channels': 2, 'default_low_input_latency': 0.01, 'default_low_output_latency': 0.16133333333333333, 'default_high_input_latency': 0.1, 'default_high_output_latency': 0.17066666666666666, 'default_samplerate': 48000.0}
2025-12-02 20:28:22,678 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] После синхронизации: rate=48000Hz, channels=2
2025-12-02 20:28:22,678 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] device_id не передан, получаем устройство через macOS API (SwitchAudioSource)...
2025-12-02 20:28:22,678 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Fallback на SwitchAudioSource (device_id не передан)
2025-12-02 20:28:22,678 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Запрашиваем системное default output устройство...
2025-12-02 20:28:22,678 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] ШАГ 1.2: Определение устройства через macOS API (приоритет 1)
2025-12-02 20:28:22,678 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Используем SwitchAudioSource: /opt/homebrew/bin/SwitchAudioSource
2025-12-02 20:28:22,678 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Запрос текущего default output устройства...
I0000 00:00:1764725302.679227 4787285 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-02 20:28:22,777 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Команда выполнена: returncode=0, stdout_len=94, stderr_len=0
2025-12-02 20:28:22,777 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Получен JSON: {'name': 'Sergiy’s AirPods', 'type': 'output', 'id': '85', 'uid': '1C-77-54-18-C8-A3:output'}
2025-12-02 20:28:22,777 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] macOS default OUTPUT (через SwitchAudioSource): "Sergiy’s AirPods"
2025-12-02 20:28:22,777 - modules.speech_playback.core.player - DEBUG - 🔍 [SwitchAudioSource] Успешно получено имя устройства: Sergiy’s AirPods
2025-12-02 20:28:22,778 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] macOS default OUTPUT (источник истины): "Sergiy’s AirPods"
2025-12-02 20:28:22,778 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Найден ID для 'Sergiy’s AirPods': 1
2025-12-02 20:28:22,778 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Найдено устройство через SwitchAudioSource: name=Sergiy’s AirPods, id=1
2025-12-02 20:28:22,778 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Найдено default output устройство (через SwitchAudioSource):
2025-12-02 20:28:22,778 - modules.speech_playback.core.player - INFO -    Name: Sergiy’s AirPods
2025-12-02 20:28:22,778 - modules.speech_playback.core.player - INFO -    Index: 1
2025-12-02 20:28:22,778 - modules.speech_playback.core.player - INFO -    Max Output Channels: 2
2025-12-02 20:28:22,778 - modules.speech_playback.core.player - INFO -    Default Sample Rate: 48000.0 Hz
2025-12-02 20:28:22,778 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Полная информация: {'name': 'Sergiy’s AirPods', 'index': 1, 'hostapi': 0, 'max_input_channels': 0, 'max_output_channels': 2, 'default_low_input_latency': 0.01, 'default_low_output_latency': 0.16133333333333333, 'default_high_input_latency': 0.1, 'default_high_output_latency': 0.17066666666666666, 'default_samplerate': 48000.0}
2025-12-02 20:28:22,778 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] macOS API (источник истины): "Sergiy’s AirPods" (ID=1)
2025-12-02 20:28:22,778 - modules.speech_playback.core.player - INFO - 🔧 [OUTPUT] BT устройство обнаружено: "Sergiy’s AirPods"
2025-12-02 20:28:22,778 - modules.speech_playback.core.player - INFO - 💡 [OUTPUT] SwitchAudioSource → device=None для BT (macOS управляет параметрами)
2025-12-02 20:28:22,778 - modules.speech_playback.core.player - DEBUG - 💡 [OUTPUT] BT устройство "Sergiy’s AirPods" - пропускаем DeviceParamsNormalizer, доверяем macOS параметрам
2025-12-02 20:28:22,778 - modules.speech_playback.core.player - INFO - 💡 [OUTPUT] SwitchAudioSource → "Sergiy’s AirPods" (BT устройство)
2025-12-02 20:28:22,778 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] BT устройство: используем device=None (НЕ используем PortAudio ID)
2025-12-02 20:28:22,778 - modules.speech_playback.core.stream_config_resolver - INFO - 💡 [OUTPUT] SwitchAudioSource → "Sergiy’s AirPods" (BT устройство)
2025-12-02 20:28:22,778 - modules.speech_playback.core.stream_config_resolver - INFO - ✅ [OUTPUT] BT устройство: используем device=None (НЕ используем PortAudio ID)
2025-12-02 20:28:22,778 - modules.speech_playback.core.stream_config_resolver - INFO - 🔧 [OUTPUT] BT устройство: используем channels=1 (обязательно), НЕ задаем blocksize, latency (пусть macOS/PortAudio выберут сами)
2025-12-02 20:28:22,779 - modules.speech_playback.core.player - INFO - 🔧 [OUTPUT] BT устройство: используем channels=1 (обязательно), НЕ задаем blocksize, latency (пусть macOS/PortAudio выберут сами)
2025-12-02 20:28:22,779 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Конфигурация потока:
2025-12-02 20:28:22,779 - modules.speech_playback.core.player - INFO -    device: None
2025-12-02 20:28:22,779 - modules.speech_playback.core.player - INFO -    channels: 1
2025-12-02 20:28:22,779 - modules.speech_playback.core.player - INFO -    dtype: int16
2025-12-02 20:28:22,779 - modules.speech_playback.core.player - INFO -    samplerate: 48000 Hz
2025-12-02 20:28:22,779 - modules.speech_playback.core.player - INFO -    blocksize: N/A (не задан, пусть PortAudio выберет)
2025-12-02 20:28:22,779 - modules.speech_playback.core.player - INFO -    latency: N/A (не задан, пусть PortAudio выберет)
2025-12-02 20:28:22,779 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Создаём поток для устройства: Sergiy’s AirPods (ID=System Default)
2025-12-02 20:28:22,779 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Пропускаем проверку доступности (device_id=None, device_id_actual=System Default)
2025-12-02 20:28:22,779 - modules.speech_playback.core.player - INFO - ⏳ [OUTPUT] Bluetooth устройство обнаружено, ожидание готовности CoreAudio pipeline (2.5с)...
I0000 00:00:1764725302.931380 4787424 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-02 20:28:23,026 - modules.audio_core.device_change_publisher - DEBUG - ✅ [INPUT] macOS default (через SwitchAudioSource): "Sergiy’s AirPods"
I0000 00:00:1764725303.027185 4787424 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-02 20:28:23,126 - modules.audio_core.device_change_publisher - DEBUG - ✅ [OUTPUT] macOS default (через SwitchAudioSource): "Sergiy’s AirPods"
2025-12-02 20:28:25,284 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Начинаем создание потока (max_retries=5, base_delay=0.3s, BT=True)...
2025-12-02 20:28:25,284 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Подтверждение: старый поток полностью закрыт (_audio_stream=None)
2025-12-02 20:28:25,285 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Подтверждение: старый поток закрыт → создаём новый stream
2025-12-02 20:28:25,285 - modules.speech_playback.core.player - INFO -    Устройство: Sergiy’s AirPods (ID=System Default, BT=True)
2025-12-02 20:28:25,285 - modules.speech_playback.core.player - INFO -    Параметры: device=None, channels=1, samplerate=48000, blocksize=N/A, latency=N/A
2025-12-02 20:28:25,285 - modules.speech_playback.core.player - INFO -    SwitchAudioSource → device=None для BT (macOS управляет параметрами)
2025-12-02 20:28:25,285 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Попытка 1/5 создания потока...
2025-12-02 20:28:25,285 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Параметры потока: {'device': None, 'channels': 1, 'dtype': 'int16', 'samplerate': 48000, 'callback': <bound method SequentialSpeechPlayer._audio_callback of <modules.speech_playback.core.player.SequentialSpeechPlayer object at 0x118389fd0>>}
2025-12-02 20:28:25,285 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Попытка 2/5 создания потока...
2025-12-02 20:28:25,285 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Параметры потока: {'device': None, 'channels': 1, 'dtype': 'int16', 'samplerate': 48000, 'callback': <bound method SequentialSpeechPlayer._audio_callback of <modules.speech_playback.core.player.SequentialSpeechPlayer ob