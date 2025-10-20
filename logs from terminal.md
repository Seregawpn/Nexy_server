2025-10-19 17:59:12,970 - modules.speech_playback.core.player - INFO - ▶️ Аудио поток стартован (lazy start)
2025-10-19 17:59:12,970 - modules.speech_playback.core.player - INFO - ✅ Аудио данные добавлены: chunk_1_1760911152487 (size: 5760)
2025-10-19 17:59:12,970 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: playback.signal
2025-10-19 17:59:12,971 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: voice.mic_opened
2025-10-19 17:59:12,971 - integration.integrations.voice_recognition_integration - INFO - VOICE: microphone opened (real)
2025-10-19 17:59:12,971 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'voice.recording_start': <bound method ListeningWorkflow._on_recording_start of <integration.workflows.listening_workflow.ListeningWorkflow object at 0x11891b0e0>>
2025-10-19 17:59:12,972 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'voice.recording_start': <bound method ModeManagementIntegration._on_voice_recording_start of <integration.integrations.mode_management_integration.ModeManagementIntegration object at 0x118919550>>
2025-10-19 17:59:12,973 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: voice.recording_start
2025-10-19 17:59:12,973 - integration.integrations.input_processing_integration - DEBUG - LONG_PRESS: voice.recording_start опубликовано
2025-10-19 17:59:12,973 - integration.core.event_bus - DEBUG - EventBus: dispatch 'mode.request' to 1 subscriber(s)
2025-10-19 17:59:12,973 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'mode.request': <bound method ModeManagementIntegration._on_mode_request of <integration.integrations.mode_management_integration.ModeManagementIntegration object at 0x118919550>>
2025-10-19 17:59:12,974 - integration.core.state_manager - INFO - 🔄 Режим изменен: sleeping → listening
2025-10-19 17:59:12,974 - integration.core.state_manager - INFO - 🎯 TRAY DEBUG: set_mode() готов публиковать app.mode_changed: AppMode.LISTENING
2025-10-19 17:59:12,974 - integration.core.state_manager - INFO - 🎯 TRAY DEBUG: EventBus подключен: True
2025-10-19 17:59:12,974 - integration.core.state_manager - INFO - 🔄 StateManager: начинаем публикацию событий (EventBus подключен, eb_loop=4689698384)
2025-10-19 17:59:12,974 - integration.core.state_manager - INFO - 🔄 StateManager: публикуем через run_coroutine_threadsafe на loop EventBus (без ожидания)
2025-10-19 17:59:12,975 - integration.core.state_manager - INFO - ✅ StateManager: события опубликованы успешно
2025-10-19 17:59:12,975 - mode_management.core.mode_controller - INFO - ✅ Режим изменен: sleeping → listening
2025-10-19 17:59:12,975 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: mode.request
2025-10-19 17:59:12,975 - integration.integrations.input_processing_integration - INFO - LONG_PRESS: запрос на LISTENING отправлен
2025-10-19 17:59:12,977 - integration.core.state_manager - INFO - 🎯 TRAY DEBUG: StateManager публикует app.mode_changed: AppMode.LISTENING (type: <enum 'AppMode'>)
2025-10-19 17:59:12,978 - integration.core.state_manager - INFO - 🎯 TRAY DEBUG: StateManager event_data: {'mode': <AppMode.LISTENING: 'listening'>}
2025-10-19 17:59:12,978 - integration.core.event_bus - INFO - EventBus: 'app.mode_changed' → subscribers=9, data={'mode': <AppMode.LISTENING: 'listening'>}
2025-10-19 17:59:12,978 - integration.core.event_bus - DEBUG - EventBus: dispatch 'app.mode_changed' to 9 subscriber(s)
2025-10-19 17:59:12,978 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method TrayControllerIntegration._on_mode_changed of <integration.integrations.tray_controller_integration.TrayControllerIntegration object at 0x118918050>>
2025-10-19 17:59:12,978 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method ScreenshotCaptureIntegration._on_mode_changed of <integration.integrations.screenshot_capture_integration.ScreenshotCaptureIntegration object at 0x118919010>>
2025-10-19 17:59:12,978 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method ModeManagementIntegration._on_app_mode_changed of <integration.integrations.mode_management_integration.ModeManagementIntegration object at 0x118919550>>
2025-10-19 17:59:12,978 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method ProcessingWorkflow._on_mode_changed of <integration.workflows.processing_workflow.ProcessingWorkflow object at 0x11891af90>>
2025-10-19 17:59:12,978 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method VoiceRecognitionIntegration._on_app_mode_changed of <integration.integrations.voice_recognition_integration.VoiceRecognitionIntegration object at 0x118919400>>
2025-10-19 17:59:12,978 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method VoiceOverDuckingIntegration.handle_mode_change of <integration.integrations.voiceover_ducking_integration.VoiceOverDuckingIntegration object at 0x11891aa50>>
2025-10-19 17:59:12,978 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method ListeningWorkflow._on_mode_changed of <integration.workflows.listening_workflow.ListeningWorkflow object at 0x11891b0e0>>
2025-10-19 17:59:12,979 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method SimpleModuleCoordinator._on_mode_changed of <integration.core.simple_module_coordinator.SimpleModuleCoordinator object at 0x11787ae40>>
2025-10-19 17:59:12,979 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method UpdaterIntegration._on_mode_changed of <integration.integrations.updater_integration.UpdaterIntegration object at 0x118918440>>
2025-10-19 17:59:12,979 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: app.mode_changed
2025-10-19 17:59:12,979 - integration.core.state_manager - INFO - 🎯 TRAY DEBUG: StateManager app.mode_changed опубликовано успешно
2025-10-19 17:59:12,979 - integration.core.state_manager - INFO - 🎯 TRAY DEBUG: StateManager подписчиков на app.mode_changed: 9
2025-10-19 17:59:12,979 - integration.core.state_manager - INFO - 🔄 StateManager: -> publish app.state_changed: AppMode.SLEEPING -> AppMode.LISTENING
2025-10-19 17:59:12,979 - integration.core.event_bus - DEBUG - EventBus: dispatch 'app.state_changed' to 1 subscriber(s)
2025-10-19 17:59:12,979 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.state_changed': <bound method InterruptManagementIntegration._on_app_state_changed of <integration.integrations.interrupt_management_integration.InterruptManagementIntegration object at 0x118918ec0>>
2025-10-19 17:59:12,979 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: app.state_changed
2025-10-19 17:59:12,979 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: _on_mode_changed ВЫЗВАН!
2025-10-19 17:59:12,979 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: event type=<class 'dict'>, event={'type': 'app.mode_changed', 'data': {'mode': <AppMode.LISTENING: 'listening'>}, 'timestamp': 70859.739378666}
2025-10-19 17:59:12,979 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: data={'mode': <AppMode.LISTENING: 'listening'>}
2025-10-19 17:59:12,979 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: new_mode=AppMode.LISTENING (type: <enum 'AppMode'>)
2025-10-19 17:59:12,979 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: mode_to_status={<AppMode.SLEEPING: 'sleeping'>: <TrayStatus.SLEEPING: 'sleeping'>, <AppMode.LISTENING: 'listening'>: <TrayStatus.LISTENING: 'listening'>, <AppMode.PROCESSING: 'processing'>: <TrayStatus.PROCESSING: 'processing'>}
2025-10-19 17:59:12,979 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: new_mode in mapping? True
2025-10-19 17:59:12,979 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: key=AppMode.SLEEPING (type: <enum 'AppMode'>), equals new_mode? False
2025-10-19 17:59:12,979 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: key=AppMode.LISTENING (type: <enum 'AppMode'>), equals new_mode? True
2025-10-19 17:59:12,980 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: key=AppMode.PROCESSING (type: <enum 'AppMode'>), equals new_mode? False
2025-10-19 17:59:12,980 - integration.integrations.tray_controller_integration - DEBUG - TrayIntegration: mapping mode -> status: AppMode.LISTENING -> TrayStatus.LISTENING
2025-10-19 17:59:12,980 - integration.core.event_bus - DEBUG - EventBus: dispatch 'tray.status_updated' to 0 subscriber(s)
2025-10-19 17:59:12,980 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: tray.status_updated
2025-10-19 17:59:12,980 - integration.integrations.tray_controller_integration - INFO - 🔄 Режим приложения изменен: listening → listening
2025-10-19 17:59:12,980 - integration.integrations.screenshot_capture_integration - INFO - 🔍 ScreenshotCapture: Получено событие app.mode_changed - mode=AppMode.LISTENING (type: <enum 'AppMode'>)
2025-10-19 17:59:12,980 - integration.workflows.processing_workflow - DEBUG - ⚙️ ProcessingWorkflow: режим изменен на listening
2025-10-19 17:59:12,981 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: _apply_status_ui_sync ВЫЗВАН! status=TrayStatus.LISTENING (type: <enum 'TrayStatus'>)
🎯 TRAY DEBUG: TrayIconGenerator.create_circle_icon status=TrayStatus.LISTENING (type: <enum 'TrayStatus'>)
🎯 TRAY DEBUG: Available colors: {<TrayStatus.SLEEPING: 'sleeping'>: '#808080', <TrayStatus.LISTENING: 'listening'>: '#007AFF', <TrayStatus.PROCESSING: 'processing'>: '#FF9500'}
🎯 TRAY DEBUG: Selected color: #007AFF
🎯 TRAY DEBUG: create_icon_file вызван для status=TrayStatus.LISTENING
🎯 TRAY DEBUG: generated color=#007AFF, PIL_available=True
2025-10-19 17:59:12,981 - integration.workflows.listening_workflow - DEBUG - 🎤 ListeningWorkflow: режим изменен на listening
I0000 00:00:1760911152.984684 1647057 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
🔄 Координация смены режима: listening
2025-10-19 17:59:13,002 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 5248)
2025-10-19 17:59:13,004 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 4736)
2025-10-19 17:59:13,006 - integration.integrations.tray_controller_integration - INFO - ✅ Tray UI applied: sleeping -> listening
2025-10-19 17:59:13,010 - integration.integrations.updater_integration - INFO - Режим приложения изменен на: None
2025-10-19 17:59:13,011 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Quartz tap вызван: event_type=10
2025-10-19 17:59:13,011 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Keycode=49, target=49
2025-10-19 17:59:13,011 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔑 Целевая клавиша обнаружена! keycode=49
2025-10-19 17:59:13,011 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔽 Quartz tap: keyDown detected for target key
2025-10-19 17:59:13,011 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔒 Quartz: игнорируем авто-повтор keyDown
 2025-10-19 17:59:13,025 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 4224)
2025-10-19 17:59:13,025 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 3712)
2025-10-19 17:59:13,045 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 3200)
2025-10-19 17:59:13,045 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 2688)
2025-10-19 17:59:13,065 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 2176)
2025-10-19 17:59:13,065 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 1664)
2025-10-19 17:59:13,078 - modules.voice_recognition.core.speech_recognizer - WARNING - ⚠️ Попытка 1/3: Первый чанк не получен за 500ms
2025-10-19 17:59:13,085 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 1152)
2025-10-19 17:59:13,085 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 640)
2025-10-19 17:59:13,093 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Quartz tap вызван: event_type=10
2025-10-19 17:59:13,093 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Keycode=49, target=49
2025-10-19 17:59:13,093 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔑 Целевая клавиша обнаружена! keycode=49
2025-10-19 17:59:13,093 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔽 Quartz tap: keyDown detected for target key
2025-10-19 17:59:13,093 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔒 Quartz: игнорируем авто-повтор keyDown
 2025-10-19 17:59:13,105 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 128)
2025-10-19 17:59:13,105 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 128 фреймов + 384 тишины (dtype=int16, ch=1)
2025-10-19 17:59:13,125 - modules.speech_playback.core.player - INFO - ✅ Чанк chunk_1_1760911152487 полностью воспроизведен
2025-10-19 17:59:13,125 - modules.speech_playback.core.buffer - DEBUG - ✅ Чанк завершен: chunk_1_1760911152487
2025-10-19 17:59:13,126 - modules.speech_playback.core.player - INFO - ✅ Чанк обработан: chunk_1_1760911152487
2025-10-19 17:59:13,178 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Quartz tap вызван: event_type=10
2025-10-19 17:59:13,178 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Keycode=49, target=49
2025-10-19 17:59:13,178 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔑 Целевая клавиша обнаружена! keycode=49
2025-10-19 17:59:13,178 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔽 Quartz tap: keyDown detected for target key
2025-10-19 17:59:13,178 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔒 Quartz: игнорируем авто-повтор keyDown
 2025-10-19 17:59:13,260 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Quartz tap вызван: event_type=10
2025-10-19 17:59:13,260 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Keycode=49, target=49
2025-10-19 17:59:13,260 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔑 Целевая клавиша обнаружена! keycode=49
2025-10-19 17:59:13,260 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔽 Quartz tap: keyDown detected for target key
2025-10-19 17:59:13,260 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔒 Quartz: игнорируем авто-повтор keyDown
 2025-10-19 17:59:13,340 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Quartz tap вызван: event_type=10
2025-10-19 17:59:13,341 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Keycode=49, target=49
2025-10-19 17:59:13,341 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔑 Целевая клавиша обнаружена! keycode=49
2025-10-19 17:59:13,341 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔽 Quartz tap: keyDown detected for target key
2025-10-19 17:59:13,341 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔒 Quartz: игнорируем авто-повтор keyDown
 2025-10-19 17:59:13,376 - modules.speech_playback.core.player - INFO - ⏸️ Аудио поток остановлен (очередь пуста, lazy stop)
2025-10-19 17:59:13,426 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Quartz tap вызван: event_type=10
2025-10-19 17:59:13,426 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Keycode=49, target=49
2025-10-19 17:59:13,426 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔑 Целевая клавиша обнаружена! keycode=49
2025-10-19 17:59:13,426 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔽 Quartz tap: keyDown detected for target key
2025-10-19 17:59:13,426 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔒 Quartz: игнорируем авто-повтор keyDown
 2025-10-19 17:59:13,507 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Quartz tap вызван: event_type=10
2025-10-19 17:59:13,507 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Keycode=49, target=49
2025-10-19 17:59:13,507 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔑 Целевая клавиша обнаружена! keycode=49
2025-10-19 17:59:13,507 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔽 Quartz tap: keyDown detected for target key
2025-10-19 17:59:13,507 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔒 Quartz: игнорируем авто-повтор keyDown
2025-10-19 17:59:13,510 - modules.voiceover_control.core.controller - DEBUG - VoiceOverController: Updated status - currently running: False
2025-10-19 17:59:13,510 - modules.voiceover_control.core.controller - DEBUG - VoiceOverController: VoiceOver is not currently running, skipping duck for mode listening
2025-10-19 17:59:13,510 - integration.integrations.voiceover_ducking_integration - DEBUG - VoiceOverDuckingIntegration: Applied mode listening
 2025-10-19 17:59:13,590 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Quartz tap вызван: event_type=10
2025-10-19 17:59:13,591 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Keycode=49, target=49
2025-10-19 17:59:13,591 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔑 Целевая клавиша обнаружена! keycode=49
2025-10-19 17:59:13,591 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔽 Quartz tap: keyDown detected for target key
2025-10-19 17:59:13,591 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔒 Quartz: игнорируем авто-повтор keyDown
 2025-10-19 17:59:13,634 - modules.voice_recognition.core.speech_recognizer - DEBUG - 🔄 Попытка 2/3: поток стартовал
2025-10-19 17:59:13,674 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Quartz tap вызван: event_type=10
2025-10-19 17:59:13,674 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Keycode=49, target=49
2025-10-19 17:59:13,674 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔑 Целевая клавиша обнаружена! keycode=49
2025-10-19 17:59:13,674 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔽 Quartz tap: keyDown detected for target key
2025-10-19 17:59:13,674 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔒 Quartz: игнорируем авто-повтор keyDown
 2025-10-19 17:59:13,693 - modules.voice_recognition.core.speech_recognizer - DEBUG - 🔊 Первый чанк получен: frames=1024, dtype=float32, peak=0.0009
2025-10-19 17:59:13,696 - modules.voice_recognition.core.speech_recognizer - INFO - ✅ Аудио поток стабилен, первый чанк получен
2025-10-19 17:59:13,733 - modules.voice_recognition.core.speech_recognizer - DEBUG - ✅ Сигнал восстановлен после 1 пустых чанков
2025-10-19 17:59:13,759 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Quartz tap вызван: event_type=10
2025-10-19 17:59:13,759 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Keycode=49, target=49
2025-10-19 17:59:13,759 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔑 Целевая клавиша обнаружена! keycode=49
2025-10-19 17:59:13,759 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔽 Quartz tap: keyDown detected for target key
2025-10-19 17:59:13,759 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔒 Quartz: игнорируем авто-повтор keyDown
 2025-10-19 17:59:13,840 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Quartz tap вызван: event_type=10
2025-10-19 17:59:13,840 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Keycode=49, target=49
2025-10-19 17:59:13,840 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔑 Целевая клавиша обнаружена! keycode=49
2025-10-19 17:59:13,840 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔽 Quartz tap: keyDown detected for target key
2025-10-19 17:59:13,840 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔒 Quartz: игнорируем авто-повтор keyDown
 2025-10-19 17:59:13,924 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Quartz tap вызван: event_type=10
2025-10-19 17:59:13,924 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Keycode=49, target=49
2025-10-19 17:59:13,924 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔑 Целевая клавиша обнаружена! keycode=49
2025-10-19 17:59:13,924 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔽 Quartz tap: keyDown detected for target key
2025-10-19 17:59:13,924 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔒 Quartz: игнорируем авто-повтор keyDown
 2025-10-19 17:59:14,008 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Quartz tap вызван: event_type=10
2025-10-19 17:59:14,008 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Keycode=49, target=49
2025-10-19 17:59:14,008 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔑 Целевая клавиша обнаружена! keycode=49
2025-10-19 17:59:14,008 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔽 Quartz tap: keyDown detected for target key
2025-10-19 17:59:14,008 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔒 Quartz: игнорируем авто-повтор keyDown
 2025-10-19 17:59:14,093 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Quartz tap вызван: event_type=10
2025-10-19 17:59:14,093 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Keycode=49, target=49
2025-10-19 17:59:14,093 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔑 Целевая клавиша обнаружена! keycode=49
2025-10-19 17:59:14,093 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔽 Quartz tap: keyDown detected for target key
2025-10-19 17:59:14,093 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔒 Quartz: игнорируем авто-повтор keyDown
 2025-10-19 17:59:14,175 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Quartz tap вызван: event_type=10
2025-10-19 17:59:14,175 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Keycode=49, target=49
2025-10-19 17:59:14,175 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔑 Целевая клавиша обнаружена! keycode=49
2025-10-19 17:59:14,175 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔽 Quartz tap: keyDown detected for target key
2025-10-19 17:59:14,175 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔒 Quartz: игнорируем авто-повтор keyDown
 2025-10-19 17:59:14,258 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Quartz tap вызван: event_type=10
2025-10-19 17:59:14,258 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Keycode=49, target=49
2025-10-19 17:59:14,258 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔑 Целевая клавиша обнаружена! keycode=49
2025-10-19 17:59:14,258 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔽 Quartz tap: keyDown detected for target key
2025-10-19 17:59:14,258 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔒 Quartz: игнорируем авто-повтор keyDown
 2025-10-19 17:59:14,340 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Quartz tap вызван: event_type=10
2025-10-19 17:59:14,340 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Keycode=49, target=49
2025-10-19 17:59:14,340 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔑 Целевая клавиша обнаружена! keycode=49
2025-10-19 17:59:14,340 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔽 Quartz tap: keyDown detected for target key
2025-10-19 17:59:14,340 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔒 Quartz: игнорируем авто-повтор keyDown
 2025-10-19 17:59:14,425 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Quartz tap вызван: event_type=10
2025-10-19 17:59:14,425 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Keycode=49, target=49
2025-10-19 17:59:14,425 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔑 Целевая клавиша обнаружена! keycode=49
2025-10-19 17:59:14,425 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔽 Quartz tap: keyDown detected for target key
2025-10-19 17:59:14,425 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔒 Quartz: игнорируем авто-повтор keyDown
 2025-10-19 17:59:14,507 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Quartz tap вызван: event_type=10
2025-10-19 17:59:14,507 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Keycode=49, target=49
2025-10-19 17:59:14,507 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔑 Целевая клавиша обнаружена! keycode=49
2025-10-19 17:59:14,507 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔽 Quartz tap: keyDown detected for target key
2025-10-19 17:59:14,507 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔒 Quartz: игнорируем авто-повтор keyDown
 2025-10-19 17:59:14,592 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Quartz tap вызван: event_type=10
2025-10-19 17:59:14,592 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Keycode=49, target=49
2025-10-19 17:59:14,592 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔑 Целевая клавиша обнаружена! keycode=49
2025-10-19 17:59:14,592 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔽 Quartz tap: keyDown detected for target key
2025-10-19 17:59:14,592 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔒 Quartz: игнорируем авто-повтор keyDown
 2025-10-19 17:59:14,676 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Quartz tap вызван: event_type=10
2025-10-19 17:59:14,676 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Keycode=49, target=49
2025-10-19 17:59:14,676 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔑 Целевая клавиша обнаружена! keycode=49
2025-10-19 17:59:14,676 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔽 Quartz tap: keyDown detected for target key
2025-10-19 17:59:14,676 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔒 Quartz: игнорируем авто-повтор keyDown
 2025-10-19 17:59:14,760 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Quartz tap вызван: event_type=10
2025-10-19 17:59:14,760 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Keycode=49, target=49
2025-10-19 17:59:14,760 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔑 Целевая клавиша обнаружена! keycode=49
2025-10-19 17:59:14,760 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔽 Quartz tap: keyDown detected for target key
2025-10-19 17:59:14,760 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔒 Quartz: игнорируем авто-повтор keyDown
 2025-10-19 17:59:14,844 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Quartz tap вызван: event_type=10
2025-10-19 17:59:14,844 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Keycode=49, target=49
2025-10-19 17:59:14,844 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔑 Целевая клавиша обнаружена! keycode=49
2025-10-19 17:59:14,844 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔽 Quartz tap: keyDown detected for target key
2025-10-19 17:59:14,844 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔒 Quartz: игнорируем авто-повтор keyDown
 2025-10-19 17:59:14,928 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Quartz tap вызван: event_type=10
2025-10-19 17:59:14,928 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Keycode=49, target=49
2025-10-19 17:59:14,928 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔑 Целевая клавиша обнаружена! keycode=49
2025-10-19 17:59:14,928 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔽 Quartz tap: keyDown detected for target key
2025-10-19 17:59:14,928 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔒 Quartz: игнорируем авто-повтор keyDown
 2025-10-19 17:59:15,012 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Quartz tap вызван: event_type=10
2025-10-19 17:59:15,012 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Keycode=49, target=49
2025-10-19 17:59:15,012 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔑 Целевая клавиша обнаружена! keycode=49
2025-10-19 17:59:15,012 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔽 Quartz tap: keyDown detected for target key
2025-10-19 17:59:15,012 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔒 Quartz: игнорируем авто-повтор keyDown
 2025-10-19 17:59:15,095 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Quartz tap вызван: event_type=10
2025-10-19 17:59:15,096 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Keycode=49, target=49
2025-10-19 17:59:15,096 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔑 Целевая клавиша обнаружена! keycode=49
2025-10-19 17:59:15,096 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔽 Quartz tap: keyDown detected for target key
2025-10-19 17:59:15,096 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔒 Quartz: игнорируем авто-повтор keyDown
 2025-10-19 17:59:15,179 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Quartz tap вызван: event_type=10
2025-10-19 17:59:15,180 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Keycode=49, target=49
2025-10-19 17:59:15,180 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔑 Целевая клавиша обнаружена! keycode=49
2025-10-19 17:59:15,180 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔽 Quartz tap: keyDown detected for target key
2025-10-19 17:59:15,180 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔒 Quartz: игнорируем авто-повтор keyDown
 2025-10-19 17:59:15,264 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Quartz tap вызван: event_type=10
2025-10-19 17:59:15,264 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Keycode=49, target=49
2025-10-19 17:59:15,264 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔑 Целевая клавиша обнаружена! keycode=49
2025-10-19 17:59:15,264 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔽 Quartz tap: keyDown detected for target key
2025-10-19 17:59:15,264 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔒 Quartz: игнорируем авто-повтор keyDown
 2025-10-19 17:59:15,347 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Quartz tap вызван: event_type=10
2025-10-19 17:59:15,347 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Keycode=49, target=49
2025-10-19 17:59:15,347 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔑 Целевая клавиша обнаружена! keycode=49
2025-10-19 17:59:15,347 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔽 Quartz tap: keyDown detected for target key
2025-10-19 17:59:15,347 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔒 Quartz: игнорируем авто-повтор keyDown
 2025-10-19 17:59:15,431 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Quartz tap вызван: event_type=10
2025-10-19 17:59:15,432 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Keycode=49, target=49
2025-10-19 17:59:15,432 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔑 Целевая клавиша обнаружена! keycode=49
2025-10-19 17:59:15,432 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔽 Quartz tap: keyDown detected for target key
2025-10-19 17:59:15,432 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔒 Quartz: игнорируем авто-повтор keyDown
 2025-10-19 17:59:15,515 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Quartz tap вызван: event_type=10
2025-10-19 17:59:15,515 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Keycode=49, target=49
2025-10-19 17:59:15,515 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔑 Целевая клавиша обнаружена! keycode=49
2025-10-19 17:59:15,515 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔽 Quartz tap: keyDown detected for target key
2025-10-19 17:59:15,515 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔒 Quartz: игнорируем авто-повтор keyDown
 2025-10-19 17:59:15,598 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Quartz tap вызван: event_type=10
2025-10-19 17:59:15,598 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Keycode=49, target=49
2025-10-19 17:59:15,598 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔑 Целевая клавиша обнаружена! keycode=49
2025-10-19 17:59:15,598 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔽 Quartz tap: keyDown detected for target key
2025-10-19 17:59:15,598 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔒 Quartz: игнорируем авто-повтор keyDown
 2025-10-19 17:59:15,679 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Quartz tap вызван: event_type=11
2025-10-19 17:59:15,679 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Keycode=49, target=49
2025-10-19 17:59:15,679 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔑 Целевая клавиша обнаружена! keycode=49
2025-10-19 17:59:15,679 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - Quartz tap: keyUp detected for target key
2025-10-19 17:59:15,679 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔑 Quartz keyUp: duration=3.841s, _long_sent=True → release
2025-10-19 17:59:15,680 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔑 _run_callback: release, callback=_handle_key_release
🔑 _run_callback: release, callback=_handle_key_release
2025-10-19 17:59:15,680 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔑 Выполняем async callback в loop: release
🔑 Выполняем async callback в loop: release
2025-10-19 17:59:15,680 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔑 QuartzMonitor: _trigger_event release, duration=3.841
🔑 QuartzMonitor: _trigger_event release, duration=3.841
2025-10-19 17:59:15,681 - integration.integrations.input_processing_integration - INFO - 🔑 RELEASE EVENT: 3.841с
2025-10-19 17:59:15,681 - integration.integrations.input_processing_integration - DEBUG - RELEASE: session=1760911151.839276, recognized=False
🔑 RELEASE EVENT: 3.841с
🔑 RELEASE: session=1760911151.839276, recognized=False
2025-10-19 17:59:15,681 - integration.integrations.input_processing_integration - DEBUG - RELEASE: публикуем voice.recording_stop
2025-10-19 17:59:15,681 - integration.core.event_bus - DEBUG - EventBus: dispatch 'voice.recording_stop' to 3 subscriber(s)
2025-10-19 17:59:15,681 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'voice.recording_stop': <bound method ScreenshotCaptureIntegration._on_voice_recording_stop of <integration.integrations.screenshot_capture_integration.ScreenshotCaptureIntegration object at 0x118919010>>
2025-10-19 17:59:15,681 - integration.integrations.screenshot_capture_integration - INFO - 🎤 ScreenshotCapture: Получено voice.recording_stop, session_id=1760911151.839276
2025-10-19 17:59:15,681 - integration.integrations.screenshot_capture_integration - INFO - 📸 ScreenshotCapture: ПРЯМОЙ ЗАХВАТ по voice.recording_stop, session_id=1760911151.839276
2025-10-19 17:59:15,863 - integration.core.event_bus - DEBUG - EventBus: dispatch 'screenshot.captured' to 3 subscriber(s)
2025-10-19 17:59:15,863 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'screenshot.captured': <bound method GrpcClientIntegration._on_screenshot_captured of <integration.integrations.grpc_client_integration.GrpcClientIntegration object at 0x118919a90>>
2025-10-19 17:59:15,863 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'screenshot.captured': <bound method ProcessingWorkflow._on_screenshot_captured of <integration.workflows.processing_workflow.ProcessingWorkflow object at 0x11891af90>>
2025-10-19 17:59:15,863 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'screenshot.captured': <bound method SimpleModuleCoordinator._on_screenshot_captured of <integration.core.simple_module_coordinator.SimpleModuleCoordinator object at 0x11787ae40>>
🖼️ Screenshot captured: /var/folders/ys/xlx_chms3hqcs1lfyq37395c0000gn/T/nexy_screenshots/shot_70862623.jpg (1383x900, 339260 bytes), session=1760911151.839276
2025-10-19 17:59:15,863 - integration.core.simple_module_coordinator - INFO - Screenshot captured: path=/var/folders/ys/xlx_chms3hqcs1lfyq37395c0000gn/T/nexy_screenshots/shot_70862623.jpg, size=339260, dims=1383x900, session=1760911151.839276
2025-10-19 17:59:15,863 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: screenshot.captured
2025-10-19 17:59:15,863 - integration.integrations.screenshot_capture_integration - INFO - Screenshot captured: /var/folders/ys/xlx_chms3hqcs1lfyq37395c0000gn/T/nexy_screenshots/shot_70862623.jpg
2025-10-19 17:59:15,864 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'voice.recording_stop': <bound method VoiceRecognitionIntegration._on_recording_stop of <integration.integrations.voice_recognition_integration.VoiceRecognitionIntegration object at 0x118919400>>
2025-10-19 17:59:15,864 - integration.integrations.voice_recognition_integration - DEBUG - VOICE: recording_stop, session=1760911151.839276
2025-10-19 17:59:15,864 - integration.core.event_bus - DEBUG - EventBus: dispatch 'voice.mic_closed' to 1 subscriber(s)
2025-10-19 17:59:15,864 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'voice.mic_closed': <bound method TrayControllerIntegration._on_voice_mic_closed of <integration.integrations.tray_controller_integration.TrayControllerIntegration object at 0x118918050>>
2025-10-19 17:59:15,864 - integration.core.event_bus - DEBUG - EventBus: dispatch 'tray.status_updated' to 0 subscriber(s)
2025-10-19 17:59:15,864 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: tray.status_updated
2025-10-19 17:59:15,864 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: voice.mic_closed
2025-10-19 17:59:15,864 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'voice.recording_stop': <bound method ListeningWorkflow._on_recording_stop of <integration.workflows.listening_workflow.ListeningWorkflow object at 0x11891b0e0>>
2025-10-19 17:59:15,864 - integration.workflows.listening_workflow - INFO - 🎤 ListeningWorkflow: завершение записи, session_id=1760911151.839276
2025-10-19 17:59:15,864 - integration.workflows.listening_workflow - INFO - 🎤 ListeningWorkflow: запись завершена успешно, ожидаем PROCESSING
2025-10-19 17:59:15,864 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: voice.recording_stop
2025-10-19 17:59:15,864 - integration.integrations.input_processing_integration - DEBUG - RELEASE: voice.recording_stop опубликовано
2025-10-19 17:59:15,864 - integration.integrations.input_processing_integration - DEBUG - RELEASE: публикуем mode.request(PROCESSING)
2025-10-19 17:59:15,864 - integration.core.event_bus - DEBUG - EventBus: dispatch 'mode.request' to 1 subscriber(s)
2025-10-19 17:59:15,864 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'mode.request': <bound method ModeManagementIntegration._on_mode_request of <integration.integrations.mode_management_integration.ModeManagementIntegration object at 0x118919550>>
2025-10-19 17:59:15,864 - integration.core.state_manager - INFO - 🔄 Режим изменен: listening → processing
2025-10-19 17:59:15,864 - integration.core.state_manager - INFO - 🎯 TRAY DEBUG: set_mode() готов публиковать app.mode_changed: AppMode.PROCESSING
2025-10-19 17:59:15,864 - integration.core.state_manager - INFO - 🎯 TRAY DEBUG: EventBus подключен: True
2025-10-19 17:59:15,864 - integration.core.state_manager - INFO - 🔄 StateManager: начинаем публикацию событий (EventBus подключен, eb_loop=4689698384)
2025-10-19 17:59:15,864 - integration.core.state_manager - INFO - 🔄 StateManager: публикуем через run_coroutine_threadsafe на loop EventBus (без ожидания)
2025-10-19 17:59:15,864 - integration.core.state_manager - INFO - ✅ StateManager: события опубликованы успешно
2025-10-19 17:59:15,864 - mode_management.core.mode_controller - INFO - ✅ Режим изменен: listening → processing
2025-10-19 17:59:15,864 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: mode.request
2025-10-19 17:59:15,864 - integration.integrations.input_processing_integration - INFO - RELEASE: запрос на PROCESSING отправлен
2025-10-19 17:59:15,864 - integration.integrations.input_processing_integration - DEBUG - RELEASE: удерживаем session_id=1760911151.839276 до завершения gRPC
2025-10-19 17:59:15,865 - modules.voice_recognition.core.audio_device_monitor - INFO - 🛑 Мониторинг аудио устройств остановлен
2025-10-19 17:59:15,865 - modules.voice_recognition.core.speech_recognizer - DEBUG - 🛑 Мониторинг устройств остановлен
2025-10-19 17:59:15,865 - modules.voice_recognition.core.speech_recognizer - DEBUG - ⏳ Ожидаем завершение потока записи...
2025-10-19 17:59:16,007 - modules.voice_recognition.core.speech_recognizer - DEBUG - 🛑 Поток записи остановлен, длительность=3.52s
2025-10-19 17:59:16,007 - modules.voice_recognition.core.speech_recognizer - DEBUG - 🎧 Завершаем запись: chunks=52, thread_alive=False
2025-10-19 17:59:16,010 - modules.voice_recognition.core.speech_recognizer - INFO - 📈 Статистика аудио: chunks=52, samples=53248, duration=2.22s, peak=0.6891, rms=0.0743, rms_db=-22.6, actual_rate=24000.0, target_rate=16000, channels=1
2025-10-19 17:59:16,010 - modules.voice_recognition.core.speech_recognizer - DEBUG - 🔄 Выполняем ресемплинг: 24000.0 → 16000
I0000 00:00:1760911156.011819 1646785 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-10-19 17:59:16,651 - modules.voice_recognition.core.speech_recognizer - INFO - ✅ Распознавание завершено: text_length=10, duration=0.64s, language=en-US
2025-10-19 17:59:16,651 - modules.voice_recognition.core.speech_recognizer - INFO - 📝 Распознано: call Kayla
2025-10-19 17:59:16,651 - integration.core.event_bus - DEBUG - EventBus: dispatch 'voice.recognition_completed' to 2 subscriber(s)
2025-10-19 17:59:16,651 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'voice.recognition_completed': <bound method InputProcessingIntegration._on_recognition_completed of <integration.integrations.input_processing_integration.InputProcessingIntegration object at 0x1189182f0>>
2025-10-19 17:59:16,651 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'voice.recognition_completed': <bound method GrpcClientIntegration._on_voice_completed of <integration.integrations.grpc_client_integration.GrpcClientIntegration object at 0x118919a90>>
2025-10-19 17:59:16,651 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: voice.recognition_completed
2025-10-19 17:59:16,652 - integration.integrations.grpc_client_integration - INFO - Using Hardware ID: E03D2455... for session 1760911151.839276
2025-10-19 17:59:16,653 - integration.core.event_bus - DEBUG - EventBus: dispatch 'grpc.request_started' to 1 subscriber(s)
2025-10-19 17:59:16,653 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'grpc.request_started': <bound method ProcessingWorkflow._on_grpc_started of <integration.workflows.processing_workflow.ProcessingWorkflow object at 0x11891af90>>
2025-10-19 17:59:16,653 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: grpc.request_started
2025-10-19 17:59:16,653 - integration.integrations.grpc_client_integration - INFO - Connecting to gRPC server: production
2025-10-19 17:59:16,653 - modules.grpc_client.core.grpc_client - INFO - 🔄 Состояние соединения: connecting
2025-10-19 17:59:16,653 - grpc._cython.cygrpc - DEBUG - [_cygrpc] Loaded running loop: id(loop)=4689698384
2025-10-19 17:59:16,653 - grpc._cython.cygrpc - DEBUG - [_cygrpc] Loaded running loop: id(loop)=4689698384
2025-10-19 17:59:16,654 - integration.core.state_manager - INFO - 🎯 TRAY DEBUG: StateManager публикует app.mode_changed: AppMode.PROCESSING (type: <enum 'AppMode'>)
2025-10-19 17:59:16,654 - integration.core.state_manager - INFO - 🎯 TRAY DEBUG: StateManager event_data: {'mode': <AppMode.PROCESSING: 'processing'>}
2025-10-19 17:59:16,654 - integration.core.event_bus - INFO - EventBus: 'app.mode_changed' → subscribers=9, data={'mode': <AppMode.PROCESSING: 'processing'>}
2025-10-19 17:59:16,654 - integration.core.event_bus - DEBUG - EventBus: dispatch 'app.mode_changed' to 9 subscriber(s)
2025-10-19 17:59:16,654 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method TrayControllerIntegration._on_mode_changed of <integration.integrations.tray_controller_integration.TrayControllerIntegration object at 0x118918050>>
2025-10-19 17:59:16,654 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method ScreenshotCaptureIntegration._on_mode_changed of <integration.integrations.screenshot_capture_integration.ScreenshotCaptureIntegration object at 0x118919010>>
2025-10-19 17:59:16,654 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method ModeManagementIntegration._on_app_mode_changed of <integration.integrations.mode_management_integration.ModeManagementIntegration object at 0x118919550>>
2025-10-19 17:59:16,654 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method ProcessingWorkflow._on_mode_changed of <integration.workflows.processing_workflow.ProcessingWorkflow object at 0x11891af90>>
2025-10-19 17:59:16,654 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method VoiceRecognitionIntegration._on_app_mode_changed of <integration.integrations.voice_recognition_integration.VoiceRecognitionIntegration object at 0x118919400>>
2025-10-19 17:59:16,654 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method VoiceOverDuckingIntegration.handle_mode_change of <integration.integrations.voiceover_ducking_integration.VoiceOverDuckingIntegration object at 0x11891aa50>>
2025-10-19 17:59:16,654 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method ListeningWorkflow._on_mode_changed of <integration.workflows.listening_workflow.ListeningWorkflow object at 0x11891b0e0>>
2025-10-19 17:59:16,654 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method SimpleModuleCoordinator._on_mode_changed of <integration.core.simple_module_coordinator.SimpleModuleCoordinator object at 0x11787ae40>>
2025-10-19 17:59:16,654 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method UpdaterIntegration._on_mode_changed of <integration.integrations.updater_integration.UpdaterIntegration object at 0x118918440>>
2025-10-19 17:59:16,654 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: app.mode_changed
2025-10-19 17:59:16,654 - integration.core.state_manager - INFO - 🎯 TRAY DEBUG: StateManager app.mode_changed опубликовано успешно
2025-10-19 17:59:16,654 - integration.core.state_manager - INFO - 🎯 TRAY DEBUG: StateManager подписчиков на app.mode_changed: 9
2025-10-19 17:59:16,654 - integration.core.state_manager - INFO - 🔄 StateManager: -> publish app.state_changed: AppMode.LISTENING -> AppMode.PROCESSING
2025-10-19 17:59:16,654 - integration.core.event_bus - DEBUG - EventBus: dispatch 'app.state_changed' to 1 subscriber(s)
2025-10-19 17:59:16,655 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.state_changed': <bound method InterruptManagementIntegration._on_app_state_changed of <integration.integrations.interrupt_management_integration.InterruptManagementIntegration object at 0x118918ec0>>
2025-10-19 17:59:16,655 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: app.state_changed
2025-10-19 17:59:16,655 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: _on_mode_changed ВЫЗВАН!
2025-10-19 17:59:16,655 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: event type=<class 'dict'>, event={'type': 'app.mode_changed', 'data': {'mode': <AppMode.PROCESSING: 'processing'>}, 'timestamp': 70863.415654166}
2025-10-19 17:59:16,655 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: data={'mode': <AppMode.PROCESSING: 'processing'>}
2025-10-19 17:59:16,655 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: new_mode=AppMode.PROCESSING (type: <enum 'AppMode'>)
2025-10-19 17:59:16,655 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: mode_to_status={<AppMode.SLEEPING: 'sleeping'>: <TrayStatus.SLEEPING: 'sleeping'>, <AppMode.LISTENING: 'listening'>: <TrayStatus.LISTENING: 'listening'>, <AppMode.PROCESSING: 'processing'>: <TrayStatus.PROCESSING: 'processing'>}
2025-10-19 17:59:16,655 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: new_mode in mapping? True
2025-10-19 17:59:16,655 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: key=AppMode.SLEEPING (type: <enum 'AppMode'>), equals new_mode? False
2025-10-19 17:59:16,655 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: key=AppMode.LISTENING (type: <enum 'AppMode'>), equals new_mode? False
2025-10-19 17:59:16,655 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: key=AppMode.PROCESSING (type: <enum 'AppMode'>), equals new_mode? True
2025-10-19 17:59:16,655 - integration.integrations.tray_controller_integration - DEBUG - TrayIntegration: mapping mode -> status: AppMode.PROCESSING -> TrayStatus.PROCESSING
2025-10-19 17:59:16,655 - integration.core.event_bus - DEBUG - EventBus: dispatch 'tray.status_updated' to 0 subscriber(s)
2025-10-19 17:59:16,655 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: tray.status_updated
2025-10-19 17:59:16,655 - integration.integrations.tray_controller_integration - INFO - 🔄 Режим приложения изменен: processing → processing
2025-10-19 17:59:16,655 - integration.integrations.screenshot_capture_integration - INFO - 🔍 ScreenshotCapture: Получено событие app.mode_changed - mode=AppMode.PROCESSING (type: <enum 'AppMode'>)
2025-10-19 17:59:16,655 - integration.integrations.screenshot_capture_integration - DEBUG - ScreenshotCaptureIntegration: already captured for session
2025-10-19 17:59:16,656 - integration.workflows.processing_workflow - DEBUG - ⚙️ ProcessingWorkflow: режим изменен на processing
2025-10-19 17:59:16,656 - integration.workflows.processing_workflow - INFO - ⚙️ ProcessingWorkflow: НАЧАЛО цепочки обработки, session_id=None
2025-10-19 17:59:16,656 - integration.workflows.processing_workflow - INFO - ⚙️ ProcessingWorkflow: переход starting → capturing
2025-10-19 17:59:16,656 - integration.workflows.listening_workflow - DEBUG - 🎤 ListeningWorkflow: режим изменен на processing
🔄 Координация смены режима: processing
2025-10-19 17:59:16,656 - integration.integrations.updater_integration - INFO - Режим приложения изменен на: None
2025-10-19 17:59:16,657 - modules.grpc_client.core.grpc_client - INFO - 🔄 Состояние соединения: connected
2025-10-19 17:59:16,657 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: _apply_status_ui_sync ВЫЗВАН! status=TrayStatus.PROCESSING (type: <enum 'TrayStatus'>)
I0000 00:00:1760911156.658042 1647057 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
🎯 TRAY DEBUG: TrayIconGenerator.create_circle_icon status=TrayStatus.PROCESSING (type: <enum 'TrayStatus'>)
2025-10-19 17:59:16,657 - modules.grpc_client.core.health_checker - INFO - 🔍 Health checker запущен
🎯 TRAY DEBUG: Available colors: {<TrayStatus.SLEEPING: 'sleeping'>: '#808080', <TrayStatus.LISTENING: 'listening'>: '#007AFF', <TrayStatus.PROCESSING: 'processing'>: '#FF9500'}
🎯 TRAY DEBUG: Selected color: #FF9500
🎯 TRAY DEBUG: create_icon_file вызван для status=TrayStatus.PROCESSING
🎯 TRAY DEBUG: generated color=#FF9500, PIL_available=True
2025-10-19 17:59:16,675 - modules.grpc_client.core.connection_manager - INFO - ✅ Подключение к 20.151.51.172:50051 установлено
2025-10-19 17:59:16,675 - integration.integrations.grpc_client_integration - INFO - ✅ gRPC connected to production
2025-10-19 17:59:16,675 - integration.integrations.grpc_client_integration - INFO - Starting gRPC stream for session 1760911151.839276 with prompt: 'call Kayla...'
2025-10-19 17:59:16,676 - modules.grpc_client.core.grpc_client - INFO - 🔍 screen_info type: <class 'dict'>
2025-10-19 17:59:16,676 - modules.grpc_client.core.grpc_client - INFO - 🔍 screen_info content: {'width': 1383, 'height': 900}
2025-10-19 17:59:16,676 - modules.grpc_client.core.grpc_client - INFO - ✅ Protobuf модули успешно импортированы из proto/
2025-10-19 17:59:16,677 - grpc._cython.cygrpc - DEBUG - [_cygrpc] Loaded running loop: id(loop)=4689698384
2025-10-19 17:59:16,679 - integration.integrations.tray_controller_integration - INFO - ✅ Tray UI applied: listening -> processing
2025-10-19 17:59:16,859 - modules.voiceover_control.core.controller - DEBUG - VoiceOverController: Updated status - currently running: False
2025-10-19 17:59:16,859 - modules.voiceover_control.core.controller - DEBUG - VoiceOverController: VoiceOver is not currently running, skipping duck for mode processing
2025-10-19 17:59:16,859 - integration.integrations.voiceover_ducking_integration - DEBUG - VoiceOverDuckingIntegration: Applied mode processing
2025-10-19 17:59:19,265 - integration.integrations.grpc_client_integration - INFO - gRPC received text_chunk len=36 for session 1760911151.839276
2025-10-19 17:59:19,266 - integration.core.event_bus - DEBUG - EventBus: dispatch 'grpc.response.text' to 0 subscriber(s)
2025-10-19 17:59:19,266 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: grpc.response.text
2025-10-19 17:59:19,761 - integration.integrations.grpc_client_integration - INFO - gRPC received audio_chunk bytes=272400 dtype=int16 shape=[] for session 1760911151.839276
2025-10-19 17:59:19,761 - integration.core.event_bus - DEBUG - EventBus: dispatch 'grpc.response.audio' to 1 subscriber(s)
2025-10-19 17:59:19,761 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'grpc.response.audio': <bound method SpeechPlaybackIntegration._on_audio_chunk of <integration.integrations.speech_playback_integration.SpeechPlaybackIntegration object at 0x118919d30>>
2025-10-19 17:59:19,761 - integration.integrations.speech_playback_integration - INFO - 🔊 Получен аудио чанк: 272400 bytes, dtype=int16, shape=[], sr=None, ch=None для сессии 1760911151.839276
2025-10-19 17:59:19,763 - integration.integrations.speech_playback_integration - INFO - 🔍 audio_chunk: sid=1760911151.839276, in_dtype='int16', dec_dtype=int16, shape=(136200,), min=-18627.000, max=15973.000, bytes=272400
2025-10-19 17:59:19,763 - modules.speech_playback.core.buffer - INFO - ✅ Чанк добавлен: chunk_2_1760911159763 (size: 136200, queue: 1)
2025-10-19 17:59:19,764 - modules.speech_playback.core.buffer - DEBUG - 🔍 Получен чанк: chunk_2_1760911159763
2025-10-19 17:59:19,764 - modules.speech_playback.core.buffer - INFO - ✅ Чанк добавлен в буфер: chunk_2_1760911159763 (frames: 136200, buffer: 0 → 136200, ch=1)
2025-10-19 17:59:20,104 - modules.speech_playback.core.player - INFO - ▶️ Аудио поток стартован (lazy start)
2025-10-19 17:59:20,104 - modules.speech_playback.core.player - INFO - ✅ Аудио данные добавлены: chunk_2_1760911159763 (size: 136200)
2025-10-19 17:59:20,104 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: grpc.response.audio
2025-10-19 17:59:20,105 - integration.integrations.grpc_client_integration - INFO - gRPC received text_chunk len=51 for session 1760911151.839276
2025-10-19 17:59:20,105 - integration.core.event_bus - DEBUG - EventBus: dispatch 'grpc.response.text' to 0 subscriber(s)
2025-10-19 17:59:20,105 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: grpc.response.text
2025-10-19 17:59:20,106 - integration.integrations.grpc_client_integration - INFO - gRPC received audio_chunk bytes=366000 dtype=int16 shape=[] for session 1760911151.839276
2025-10-19 17:59:20,106 - integration.core.event_bus - DEBUG - EventBus: dispatch 'grpc.response.audio' to 1 subscriber(s)
2025-10-19 17:59:20,106 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'grpc.response.audio': <bound method SpeechPlaybackIntegration._on_audio_chunk of <integration.integrations.speech_playback_integration.SpeechPlaybackIntegration object at 0x118919d30>>
2025-10-19 17:59:20,106 - integration.integrations.speech_playback_integration - INFO - 🔊 Получен аудио чанк: 366000 bytes, dtype=int16, shape=[], sr=None, ch=None для сессии 1760911151.839276
2025-10-19 17:59:20,106 - integration.integrations.speech_playback_integration - INFO - 🔍 audio_chunk: sid=1760911151.839276, in_dtype='int16', dec_dtype=int16, shape=(183000,), min=-20317.000, max=20445.000, bytes=366000
2025-10-19 17:59:20,106 - modules.speech_playback.core.buffer - INFO - ✅ Чанк добавлен: chunk_3_1760911160106 (size: 183000, queue: 1)
2025-10-19 17:59:20,107 - modules.speech_playback.core.player - INFO - ✅ Аудио данные добавлены: chunk_3_1760911160106 (size: 183000)
2025-10-19 17:59:20,107 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: grpc.response.audio
2025-10-19 17:59:20,107 - integration.integrations.grpc_client_integration - INFO - gRPC received audio_chunk bytes=0 dtype= shape=[] for session 1760911151.839276
2025-10-19 17:59:20,107 - integration.integrations.grpc_client_integration - INFO - gRPC received empty audio_chunk - stream completed for session 1760911151.839276
2025-10-19 17:59:20,107 - integration.core.event_bus - DEBUG - EventBus: dispatch 'grpc.request_completed' to 3 subscriber(s)
2025-10-19 17:59:20,107 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'grpc.request_completed': <bound method InputProcessingIntegration._on_grpc_completed of <integration.integrations.input_processing_integration.InputProcessingIntegration object at 0x1189182f0>>
2025-10-19 17:59:20,107 - integration.integrations.input_processing_integration - DEBUG - gRPC completed for session 1760911151.839276
2025-10-19 17:59:20,107 - integration.integrations.input_processing_integration - DEBUG - SESSION RESET (grpc_completed)
2025-10-19 17:59:20,107 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'grpc.request_completed': <bound method SpeechPlaybackIntegration._on_grpc_completed of <integration.integrations.speech_playback_integration.SpeechPlaybackIntegration object at 0x118919d30>>
2025-10-19 17:59:20,107 - integration.integrations.speech_playback_integration - INFO - SpeechPlayback: получено grpc.request_completed для сессии 1760911151.839276
2025-10-19 17:59:20,107 - integration.integrations.speech_playback_integration - INFO - SpeechPlayback: установлен флаг _grpc_done_sessions[1760911151.839276] = True
2025-10-19 17:59:20,107 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'grpc.request_completed': <bound method ProcessingWorkflow._on_grpc_completed of <integration.workflows.processing_workflow.ProcessingWorkflow object at 0x11891af90>>
2025-10-19 17:59:20,107 - integration.workflows.processing_workflow - INFO - 🌐 ProcessingWorkflow: gRPC запрос завершен успешно
2025-10-19 17:59:20,107 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: grpc.request_completed
2025-10-19 17:59:20,107 - integration.integrations.speech_playback_integration - INFO - SpeechPlayback: запуск _finalize_on_silence для сессии 1760911151.839276, timeout=3.0s
2025-10-19 17:59:20,112 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 135688)
2025-10-19 17:59:20,122 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 135176)
2025-10-19 17:59:20,132 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 134664)
2025-10-19 17:59:20,142 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 134152)
2025-10-19 17:59:20,152 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 133640)
2025-10-19 17:59:20,162 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 133128)
2025-10-19 17:59:20,172 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 132616)
2025-10-19 17:59:20,182 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 132104)
2025-10-19 17:59:20,192 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 131592)
2025-10-19 17:59:20,202 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 131080)
2025-10-19 17:59:20,212 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 130568)
2025-10-19 17:59:20,222 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 130056)
2025-10-19 17:59:20,232 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 129544)
2025-10-19 17:59:20,243 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 129032)
2025-10-19 17:59:20,252 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 128520)
2025-10-19 17:59:20,272 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 128008)
2025-10-19 17:59:20,282 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 127496)
2025-10-19 17:59:20,292 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 126984)
2025-10-19 17:59:20,302 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 126472)
2025-10-19 17:59:20,312 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 125960)
2025-10-19 17:59:20,322 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 125448)
2025-10-19 17:59:20,332 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 124936)
2025-10-19 17:59:20,342 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 124424)
2025-10-19 17:59:20,352 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 123912)
2025-10-19 17:59:20,362 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 123400)
2025-10-19 17:59:20,373 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 122888)
2025-10-19 17:59:20,382 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 122376)
2025-10-19 17:59:20,392 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 121864)
2025-10-19 17:59:20,402 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 121352)
2025-10-19 17:59:20,412 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 120840)
2025-10-19 17:59:20,432 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 120328)
2025-10-19 17:59:20,442 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 119816)
2025-10-19 17:59:20,452 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 119304)
2025-10-19 17:59:20,462 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 118792)
2025-10-19 17:59:20,472 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 118280)
2025-10-19 17:59:20,482 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 117768)
2025-10-19 17:59:20,492 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 117256)
2025-10-19 17:59:20,502 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 116744)
2025-10-19 17:59:20,512 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 116232)
2025-10-19 17:59:20,522 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 115720)
2025-10-19 17:59:20,532 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 115208)
2025-10-19 17:59:20,542 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 114696)
2025-10-19 17:59:20,552 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 114184)
2025-10-19 17:59:20,562 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 113672)
2025-10-19 17:59:20,572 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 113160)
2025-10-19 17:59:20,585 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Quartz tap вызван: event_type=10
2025-10-19 17:59:20,585 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Keycode=8, target=49
^C2025-10-19 17:59:20,592 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 112648)