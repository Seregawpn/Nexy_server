ANAGER] Using lock file from env NEXY_INSTANCE_LOCK_FILE=/Users/sergiyzasorin/Development/Nexy/client/.nexy_dev/nexy.lock
2025-11-04 12:46:47,777 - config.unified_config_loader - DEBUG - UnifiedConfigLoader: environment defaulted to development
2025-11-04 12:46:47,799 - config.unified_config_loader - DEBUG - UnifiedConfigLoader: environment defaulted to development
2025-11-04 12:46:47,822 - modules.updater.net - WARNING - ⚠️ SSL verification disabled - используется self-signed сертификат
2025-11-04 12:46:47,822 - modules.updater.net - INFO - HTTP клиент инициализирован: timeout=10s, retries=0, ssl_verify=False
2025-11-04 12:46:47,822 - config.unified_config_loader - DEBUG - UnifiedConfigLoader: environment defaulted to development
2025-11-04 12:46:47,822 - integration.core.base_integration - INFO - PermissionRestart integration created
2025-11-04 12:46:47,822 - config.unified_config_loader - DEBUG - UnifiedConfigLoader: environment defaulted to development
2025-11-04 12:46:47,822 - integration.core.base_integration - INFO - UpdateNotification integration created
2025-11-04 12:46:47,822 - config.unified_config_loader - DEBUG - UnifiedConfigLoader: environment defaulted to development
2025-11-04 12:46:47,844 - integration.integrations.network_manager_integration - INFO - NetworkManagerIntegration created
2025-11-04 12:46:47,844 - integration.integrations.interrupt_management_integration - INFO - InterruptManagementIntegration created
2025-11-04 12:46:47,844 - config.unified_config_loader - DEBUG - UnifiedConfigLoader: environment defaulted to development
2025-11-04 12:46:47,865 - integration.core.simple_module_coordinator - DEBUG - Voice config: simulate=False, language=en-US
2025-11-04 12:46:47,865 - config.unified_config_loader - DEBUG - UnifiedConfigLoader: environment defaulted to development
2025-11-04 12:46:47,865 - config.unified_config_loader - DEBUG - UnifiedConfigLoader: environment defaulted to development
2025-11-04 12:46:47,886 - integration.integrations.autostart_manager_integration - INFO - AutostartManagerIntegration created (мониторинг LaunchAgent)
2025-11-04 12:46:47,887 - config.unified_config_loader - DEBUG - UnifiedConfigLoader: environment defaulted to development
2025-11-04 12:46:47,908 - modules.welcome_message.config.welcome_config - INFO - ✅ [WELCOME_CONFIG] Конфигурация загружена: enabled=True, text='Hi! Nexy is here. How can I he...'
2025-11-04 12:46:47,908 - config.unified_config_loader - DEBUG - UnifiedConfigLoader: environment defaulted to development
2025-11-04 12:46:47,929 - config.unified_config_loader - INFO - 🔌 [DEBUG] Loading server 'local' from YAML: ssl_verify=True
2025-11-04 12:46:47,929 - config.unified_config_loader - INFO - 🔌 [DEBUG] Loading server 'production' from YAML: ssl_verify=False
2025-11-04 12:46:47,929 - config.unified_config_loader - INFO - 🔌 [DEBUG] Loading server 'fallback' from YAML: ssl_verify=True
2025-11-04 12:46:47,929 - integration.core.base_integration - INFO - voiceover_ducking integration created
2025-11-04 12:46:47,929 - integration.integrations.first_run_permissions_integration - INFO - [FIRST_RUN_PERMISSIONS] Configuration loaded: enabled=True, pause_seconds=1.0, activation_hold_seconds=13.0
2025-11-04 12:46:47,930 - integration.utils.resource_path - INFO - ✅ Using standard user data directory: /Users/sergiyzasorin/Library/Application Support/Nexy
✅ Интеграции созданы: instance_manager, hardware_id, first_run_permissions, permission_restart, update_notification, tray, mode_management, input, updater, network, interrupt, voice_recognition, screenshot_capture, grpc, speech_playback, signals, autostart_manager, welcome_message, voiceover_ducking
🔧 Создание Workflows...
✅ ListeningWorkflow создан
✅ ProcessingWorkflow создан
✅ Все Workflows созданы успешно
✅ Интеграции созданы
🔧 Инициализация интеграций...
🔧 Инициализация instance_manager...
2025-11-04 12:46:47,930 - integration.core.event_bus - INFO - 📝 Подписка на событие: app.startup (приоритет: MEDIUM)
2025-11-04 12:46:47,930 - integration.core.event_bus - INFO - 📝 Подписка на событие: app.shutdown (приоритет: MEDIUM)
2025-11-04 12:46:47,930 - integration.core.event_bus - INFO - 📝 Подписка на событие: instance.check_request (приоритет: MEDIUM)
✅ InstanceManagerIntegration инициализирован
✅ instance_manager инициализирован
🔧 Инициализация hardware_id...
2025-11-04 12:46:47,930 - integration.integrations.hardware_id_integration - INFO - Initializing HardwareIdIntegration...
2025-11-04 12:46:47,930 - integration.utils.resource_path - DEBUG - Using cached user data dir: /Users/sergiyzasorin/Library/Application Support/Nexy
2025-11-04 12:46:47,930 - modules.hardware_id.core.config - INFO - ✅ Конфигурация hardware_id загружена из файла
2025-11-04 12:46:47,930 - integration.core.event_bus - INFO - 📝 Подписка на событие: app.startup (приоритет: HIGH)
2025-11-04 12:46:47,930 - integration.core.event_bus - INFO - 📝 Подписка на событие: app.shutdown (приоритет: MEDIUM)
2025-11-04 12:46:47,930 - integration.core.event_bus - INFO - 📝 Подписка на событие: hardware.id_request (приоритет: HIGH)
2025-11-04 12:46:47,930 - integration.core.event_bus - INFO - 📝 Подписка на событие: hardware.id_refresh (приоритет: MEDIUM)
2025-11-04 12:46:47,930 - integration.integrations.hardware_id_integration - INFO - HardwareIdIntegration initialized
✅ hardware_id инициализирован
🔧 Инициализация tray...
2025-11-04 12:46:47,931 - integration.integrations.tray_controller_integration - INFO - 🔧 Инициализация TrayControllerIntegration...
2025-11-04 12:46:47,931 - integration.utils.resource_path - DEBUG - Using cached user data dir: /Users/sergiyzasorin/Library/Application Support/Nexy
2025-11-04 12:46:47,931 - modules.tray_controller.core.tray_controller - INFO - 🔧 Инициализация TrayController
2025-11-04 12:46:47,931 - modules.tray_controller.core.tray_controller - INFO - ✅ TrayController инициализирован
2025-11-04 12:46:47,931 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: Подписываемся на app.mode_changed событие
2025-11-04 12:46:47,931 - integration.core.event_bus - INFO - 📝 Подписка на событие: app.mode_changed (приоритет: HIGH)
2025-11-04 12:46:47,931 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: Подписка на app.mode_changed успешна
2025-11-04 12:46:47,931 - integration.core.event_bus - INFO - 📝 Подписка на событие: app.startup (приоритет: HIGH)
2025-11-04 12:46:47,931 - integration.core.event_bus - INFO - 📝 Подписка на событие: app.shutdown (приоритет: HIGH)
2025-11-04 12:46:47,931 - integration.core.event_bus - INFO - 📝 Подписка на событие: voice.mic_opened (приоритет: HIGH)
2025-11-04 12:46:47,931 - integration.core.event_bus - INFO - 📝 Подписка на событие: voice.mic_closed (приоритет: HIGH)
2025-11-04 12:46:47,931 - integration.integrations.tray_controller_integration - INFO - ✅ Обработчики событий TrayControllerIntegration настроены
2025-11-04 12:46:47,931 - integration.integrations.tray_controller_integration - INFO - ✅ TrayControllerIntegration инициализирован
✅ tray инициализирован
🔧 Инициализация input...
2025-11-04 12:46:47,931 - integration.integrations.input_processing_integration - INFO - 🔧 Инициализация input_processing...
2025-11-04 12:46:47,934 - integration.integrations.input_processing_integration - INFO - ✅ QuartzKeyboardMonitor создан (тестирование отложено до start())
2025-11-04 12:46:47,934 - integration.integrations.input_processing_integration - INFO - 🔑 Регистрируем Quartz callback'и:
🔑 Регистрируем Quartz callback'и:
2025-11-04 12:46:47,934 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔑 QuartzMonitor: callback зарегистрирован для press
🔑 QuartzMonitor: callback зарегистрирован для press
2025-11-04 12:46:47,934 - integration.integrations.input_processing_integration - INFO - 🔑 ✅ PRESS callback зарегистрирован
🔑 ✅ PRESS callback зарегистрирован
2025-11-04 12:46:47,935 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔑 QuartzMonitor: callback зарегистрирован для short_press
🔑 QuartzMonitor: callback зарегистрирован для short_press
2025-11-04 12:46:47,935 - integration.integrations.input_processing_integration - INFO - 🔑 ✅ SHORT_PRESS callback зарегистрирован
🔑 ✅ SHORT_PRESS callback зарегистрирован
2025-11-04 12:46:47,935 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔑 QuartzMonitor: callback зарегистрирован для long_press
🔑 QuartzMonitor: callback зарегистрирован для long_press
2025-11-04 12:46:47,935 - integration.integrations.input_processing_integration - INFO - 🔑 ✅ LONG_PRESS callback зарегистрирован
🔑 ✅ LONG_PRESS callback зарегистрирован
2025-11-04 12:46:47,935 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔑 QuartzMonitor: callback зарегистрирован для release
🔑 QuartzMonitor: callback зарегистрирован для release
2025-11-04 12:46:47,935 - integration.integrations.input_processing_integration - INFO - 🔑 ✅ RELEASE callback зарегистрирован
🔑 ✅ RELEASE callback зарегистрирован
2025-11-04 12:46:47,935 - integration.integrations.input_processing_integration - INFO - ✅ KeyboardMonitor инициализирован
2025-11-04 12:46:47,935 - integration.core.event_bus - INFO - 📝 Подписка на событие: mode.switch (приоритет: HIGH)
2025-11-04 12:46:47,935 - integration.core.event_bus - INFO - 📝 Подписка на событие: voice.recognition_completed (приоритет: HIGH)
2025-11-04 12:46:47,935 - integration.core.event_bus - INFO - 📝 Подписка на событие: voice.recognition_failed (приоритет: HIGH)
2025-11-04 12:46:47,935 - integration.core.event_bus - INFO - 📝 Подписка на событие: voice.recognition_timeout (приоритет: HIGH)
2025-11-04 12:46:47,935 - integration.core.event_bus - INFO - 📝 Подписка на событие: grpc.request_completed (приоритет: HIGH)
2025-11-04 12:46:47,935 - integration.core.event_bus - INFO - 📝 Подписка на событие: grpc.request_failed (приоритет: HIGH)
2025-11-04 12:46:47,935 - integration.core.event_bus - INFO - 📝 Подписка на событие: playback.started (приоритет: MEDIUM)
2025-11-04 12:46:47,935 - integration.core.event_bus - INFO - 📝 Подписка на событие: playback.completed (приоритет: MEDIUM)
2025-11-04 12:46:47,935 - integration.core.event_bus - INFO - 📝 Подписка на событие: playback.failed (приоритет: MEDIUM)
2025-11-04 12:46:47,935 - integration.core.event_bus - INFO - 📝 Подписка на событие: playback.cancelled (приоритет: MEDIUM)
2025-11-04 12:46:47,935 - integration.core.event_bus - INFO - 📝 Подписка на событие: voice.mic_opened (приоритет: HIGH)
2025-11-04 12:46:47,935 - integration.core.event_bus - INFO - 📝 Подписка на событие: voice.mic_closed (приоритет: HIGH)
2025-11-04 12:46:47,935 - integration.integrations.input_processing_integration - INFO - ✅ input_processing инициализирован
✅ input инициализирован
🔧 Инициализация updater...
2025-11-04 12:46:47,935 - integration.integrations.updater_integration - INFO - 🔄 Инициализация UpdaterIntegration...
2025-11-04 12:46:47,935 - integration.core.event_bus - INFO - 📝 Подписка на событие: app.startup (приоритет: MEDIUM)
2025-11-04 12:46:47,935 - integration.core.event_bus - INFO - 📝 Подписка на событие: app.shutdown (приоритет: HIGH)
2025-11-04 12:46:47,935 - integration.core.event_bus - INFO - 📝 Подписка на событие: updater.check_manual (приоритет: HIGH)
2025-11-04 12:46:47,935 - integration.core.event_bus - INFO - 📝 Подписка на событие: app.mode_changed (приоритет: LOW)
2025-11-04 12:46:47,936 - integration.core.event_bus - INFO - 📝 Подписка на событие: mode.changed (приоритет: LOW)
2025-11-04 12:46:47,936 - integration.core.state_manager - DEBUG - 📊 Данные состояния обновлены: update_in_progress
2025-11-04 12:46:47,957 - integration.integrations.updater_integration - DEBUG - [UPDATER] Shadow-mode sync: accessor=False == state_data=False (trigger=initialize)
2025-11-04 12:46:47,957 - integration.integrations.updater_integration - INFO - ✅ UpdaterIntegration инициализирован
✅ updater инициализирован
🔧 Инициализация permission_restart...
2025-11-04 12:46:47,957 - integration.core.base_integration - INFO - Initializing PermissionRestart...
2025-11-04 12:46:47,957 - modules.permission_restart.macos.permissions_restart_handler - INFO - [PERMISSION_RESTART] RestartHandler init: dry_run=False allow_dev_fallback=True env(NEXY_DISABLE_AUTO_RESTART)=None ks(NEXY_KS_FIRST_RUN_RESTART)=None
2025-11-04 12:46:47,957 - integration.integrations.permission_restart_integration - INFO - [PERMISSION_RESTART] Integration initialised (enabled=True, delay=5.0, attempts=3)
2025-11-04 12:46:47,957 - integration.core.base_integration - INFO - PermissionRestart initialized successfully
✅ permission_restart инициализирован
🔧 Инициализация update_notification...
2025-11-04 12:46:47,957 - integration.core.base_integration - INFO - Initializing UpdateNotification...
2025-11-04 12:46:47,957 - integration.core.event_bus - INFO - 📝 Подписка на событие: updater.update_started (приоритет: MEDIUM)
2025-11-04 12:46:47,957 - integration.core.event_bus - INFO - 📝 Подписка на событие: updater.download_progress (приоритет: MEDIUM)
2025-11-04 12:46:47,957 - integration.core.event_bus - INFO - 📝 Подписка на событие: updater.install_progress (приоритет: MEDIUM)
2025-11-04 12:46:47,957 - integration.core.event_bus - INFO - 📝 Подписка на событие: updater.update_completed (приоритет: MEDIUM)
2025-11-04 12:46:47,957 - integration.core.event_bus - INFO - 📝 Подписка на событие: updater.update_failed (приоритет: MEDIUM)
2025-11-04 12:46:47,957 - integration.integrations.update_notification_integration - INFO - [UPDATE_NOTIFY] Подписки на события обновления зарегистрированы
2025-11-04 12:46:47,957 - integration.core.base_integration - INFO - UpdateNotification initialized successfully
✅ update_notification инициализирован
🔧 Инициализация network...
2025-11-04 12:46:47,957 - integration.integrations.network_manager_integration - INFO - Initializing NetworkManagerIntegration...
2025-11-04 12:46:47,958 - modules.network_manager.core.network_manager - DEBUG - Added network callback: _on_network_event
2025-11-04 12:46:47,958 - modules.network_manager.core.network_manager - INFO - Initializing NetworkManager...
2025-11-04 12:46:47,958 - integration.core.event_bus - DEBUG - EventBus: dispatch 'updater.in_progress.changed' to 0 subscriber(s)
2025-11-04 12:46:47,958 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: updater.in_progress.changed
2025-11-04 12:46:48,011 - integration.integrations.network_manager_integration - DEBUG - Network event received: network.status_changed
2025-11-04 12:46:48,011 - integration.core.event_bus - DEBUG - EventBus: dispatch 'network.status_changed' to 0 subscriber(s)
2025-11-04 12:46:48,011 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: network.status_changed
2025-11-04 12:46:48,011 - integration.core.event_bus - DEBUG - EventBus: dispatch 'tray.update_tooltip' to 0 subscriber(s)
2025-11-04 12:46:48,011 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: tray.update_tooltip
2025-11-04 12:46:48,011 - modules.network_manager.core.network_manager - INFO - Network status changed: unknown -> connected
2025-11-04 12:46:48,011 - modules.network_manager.core.network_manager - INFO - NetworkManager initialized successfully
2025-11-04 12:46:48,011 - integration.core.event_bus - INFO - 📝 Подписка на событие: app.startup (приоритет: MEDIUM)
2025-11-04 12:46:48,011 - integration.core.event_bus - INFO - 📝 Подписка на событие: app.shutdown (приоритет: MEDIUM)
2025-11-04 12:46:48,011 - integration.integrations.network_manager_integration - INFO - NetworkManagerIntegration initialized successfully
✅ network инициализирован
🔧 Инициализация interrupt...
2025-11-04 12:46:48,011 - integration.integrations.interrupt_management_integration - INFO - Initializing InterruptManagementIntegration...
2025-11-04 12:46:48,011 - modules.interrupt_management.core.interrupt_coordinator - INFO - ✅ Координатор прерываний инициализирован
2025-11-04 12:46:48,011 - modules.interrupt_management.core.interrupt_coordinator - DEBUG - 📝 Зарегистрирован обработчик для speech_stop
2025-11-04 12:46:48,011 - modules.interrupt_management.core.interrupt_coordinator - DEBUG - 📝 Зарегистрирован обработчик для speech_pause
2025-11-04 12:46:48,011 - modules.interrupt_management.core.interrupt_coordinator - DEBUG - 📝 Зарегистрирован обработчик для recording_stop
2025-11-04 12:46:48,011 - modules.interrupt_management.core.interrupt_coordinator - DEBUG - 📝 Зарегистрирован обработчик для session_clear
2025-11-04 12:46:48,011 - integration.integrations.interrupt_management_integration - INFO - Interrupt handlers registered successfully
2025-11-04 12:46:48,011 - integration.core.event_bus - INFO - 📝 Подписка на событие: app.startup (приоритет: MEDIUM)
2025-11-04 12:46:48,011 - integration.core.event_bus - INFO - 📝 Подписка на событие: app.shutdown (приоритет: HIGH)
2025-11-04 12:46:48,011 - integration.core.event_bus - INFO - 📝 Подписка на событие: app.state_changed (приоритет: HIGH)
2025-11-04 12:46:48,011 - integration.core.event_bus - INFO - 📝 Подписка на событие: interrupt.request (приоритет: HIGH)
2025-11-04 12:46:48,011 - integration.core.event_bus - INFO - 📝 Подписка на событие: interrupt.cancel (приоритет: HIGH)
2025-11-04 12:46:48,011 - integration.integrations.interrupt_management_integration - INFO - InterruptManagementIntegration initialized successfully
✅ interrupt инициализирован
🔧 Инициализация screenshot_capture...
2025-11-04 12:46:48,016 - modules.screenshot_capture.core.screenshot_capture - INFO - ✅ Core Graphics bridge инициализирован
2025-11-04 12:46:48,016 - integration.integrations.screenshot_capture_integration - INFO - ScreenshotCaptureIntegration: capture module ready
2025-11-04 12:46:48,016 - integration.core.event_bus - INFO - 📝 Подписка на событие: app.mode_changed (приоритет: HIGH)
2025-11-04 12:46:48,016 - integration.core.event_bus - INFO - 📝 Подписка на событие: voice.recording_stop (приоритет: HIGH)
2025-11-04 12:46:48,016 - integration.integrations.screenshot_capture_integration - INFO - 🔧 ScreenshotCapture: Подписки настроены - app.mode_changed, voice.recording_stop
2025-11-04 12:46:48,016 - integration.core.event_bus - INFO - 📝 Подписка на событие: permissions.status_checked (приоритет: MEDIUM)
2025-11-04 12:46:48,016 - integration.core.event_bus - INFO - 📝 Подписка на событие: permissions.changed (приоритет: MEDIUM)
2025-11-04 12:46:48,016 - integration.core.event_bus - INFO - 📝 Подписка на событие: permissions.requested (приоритет: LOW)
2025-11-04 12:46:48,016 - integration.core.event_bus - INFO - 📝 Подписка на событие: permissions.integration_ready (приоритет: MEDIUM)
2025-11-04 12:46:48,016 - integration.integrations.screenshot_capture_integration - INFO - ScreenshotCaptureIntegration initialized
2025-11-04 12:46:48,016 - integration.integrations.screenshot_capture_integration - INFO - 📸 [SCREENSHOT_INTEGRATION] Разрешения будут запрошены через PermissionsIntegration
✅ screenshot_capture инициализирован
🔧 Инициализация voice_recognition...
2025-11-04 12:46:48,016 - integration.core.event_bus - INFO - 📝 Подписка на событие: voice.recording_start (приоритет: HIGH)
2025-11-04 12:46:48,016 - integration.core.event_bus - INFO - 📝 Подписка на событие: voice.recording_stop (приоритет: HIGH)
2025-11-04 12:46:48,017 - integration.core.event_bus - INFO - 📝 Подписка на событие: keyboard.short_press (приоритет: CRITICAL)
2025-11-04 12:46:48,017 - integration.core.event_bus - INFO - 📝 Подписка на событие: app.mode_changed (приоритет: MEDIUM)
2025-11-04 12:46:48,017 - integration.core.event_bus - INFO - 📝 Подписка на событие: permissions.first_run_started (приоритет: CRITICAL)
2025-11-04 12:46:48,017 - integration.core.event_bus - INFO - 📝 Подписка на событие: permissions.first_run_completed (приоритет: CRITICAL)
2025-11-04 12:46:48,017 - integration.core.event_bus - INFO - 📝 Подписка на событие: permissions.first_run_failed (приоритет: CRITICAL)
2025-11-04 12:46:48,017 - integration.integrations.voice_recognition_integration - DEBUG - 🔍 [AUDIO_DEBUG] Условия создания SpeechRecognizer: simulate=False, _REAL_VOICE_AVAILABLE=True
2025-11-04 12:46:48,017 - modules.voice_recognition.core.audio_device_monitor - INFO - 🎤 Текущий input device: 1
2025-11-04 12:46:48,017 - modules.voice_recognition.core.audio_device_monitor - INFO - 🔧 AudioDeviceMonitor создан (интервал: 0.5с)
2025-11-04 12:46:48,017 - modules.voice_recognition.core.audio_device_monitor - DEBUG - 🔔 Callback смены устройства установлен
2025-11-04 12:46:48,017 - integration.integrations.voice_recognition_integration - WARNING - ⚠️ [AUDIO_DEBUG] SpeechRecognizer не поддерживает set_event_bus
2025-11-04 12:46:48,017 - modules.voice_recognition.core.speech_recognizer - DEBUG - 🔧 Event loop установлен в SpeechRecognizer: <_UnixSelectorEventLoop running=True closed=False debug=False>
2025-11-04 12:46:48,131 - modules.voice_recognition.core.speech_recognizer - INFO - 🔧 Настраиваем микрофон для фонового шума...
2025-11-04 12:46:49,114 - modules.voice_recognition.core.speech_recognizer - INFO - 📊 Энергетический порог установлен: 617.370400965099
2025-11-04 12:46:49,231 - modules.voice_recognition.core.speech_recognizer - INFO - ✅ Распознаватель речи инициализирован (язык: en-US)
2025-11-04 12:46:49,231 - integration.integrations.voice_recognition_integration - DEBUG - 🔍 [AUDIO_DEBUG] Event loop установлен в SpeechRecognizer
2025-11-04 12:46:49,231 - integration.integrations.voice_recognition_integration - INFO - VoiceRecognitionIntegration: real SpeechRecognizer initialized with EventBus
2025-11-04 12:46:49,231 - integration.integrations.voice_recognition_integration - INFO - VoiceRecognitionIntegration initialized
✅ voice_recognition инициализирован
🔧 Инициализация mode_management...
2025-11-04 12:46:49,231 - integration.core.event_bus - INFO - 📝 Подписка на событие: mode.request (приоритет: CRITICAL)
2025-11-04 12:46:49,231 - integration.core.event_bus - INFO - 📝 Подписка на событие: app.mode_changed (приоритет: HIGH)
2025-11-04 12:46:49,232 - mode_management.core.mode_controller - DEBUG - 📝 Зарегистрирован переход: sleeping → listening
2025-11-04 12:46:49,232 - mode_management.core.mode_controller - DEBUG - 📝 Зарегистрирован переход: listening → processing
2025-11-04 12:46:49,232 - mode_management.core.mode_controller - DEBUG - 📝 Зарегистрирован переход: processing → sleeping
2025-11-04 12:46:49,232 - mode_management.core.mode_controller - DEBUG - 📝 Зарегистрирован переход: sleeping → processing
2025-11-04 12:46:49,232 - mode_management.core.mode_controller - DEBUG - 📝 Зарегистрирован переход: listening → sleeping
2025-11-04 12:46:49,232 - mode_management.core.mode_controller - DEBUG - 📝 Зарегистрирован callback смены режима
2025-11-04 12:46:49,232 - integration.core.event_bus - INFO - 📝 Подписка на событие: voice.recording_start (приоритет: MEDIUM)
2025-11-04 12:46:49,232 - integration.core.event_bus - INFO - 📝 Подписка на событие: playback.completed (приоритет: MEDIUM)
2025-11-04 12:46:49,232 - integration.core.event_bus - INFO - 📝 Подписка на событие: playback.failed (приоритет: MEDIUM)
2025-11-04 12:46:49,232 - integration.integrations.mode_management_integration - INFO - ModeManagementIntegration initialized
✅ mode_management инициализирован
🔧 Инициализация grpc...
2025-11-04 12:46:49,232 - integration.integrations.grpc_client_integration - INFO - Initializing GrpcClientIntegration...
2025-11-04 12:46:49,232 - config.unified_config_loader - DEBUG - UnifiedConfigLoader: environment defaulted to development
2025-11-04 12:46:49,262 - config.unified_config_loader - INFO - 🔌 [DEBUG] Loading server 'local' from YAML: ssl_verify=True
2025-11-04 12:46:49,262 - config.unified_config_loader - INFO - 🔌 [DEBUG] Loading server 'production' from YAML: ssl_verify=False
2025-11-04 12:46:49,262 - config.unified_config_loader - INFO - 🔌 [DEBUG] Loading server 'fallback' from YAML: ssl_verify=True
2025-11-04 12:46:49,262 - integration.integrations.grpc_client_integration - INFO - 🔌 [DEBUG] GrpcClientIntegration passing server 'local' to GrpcClient: ssl_verify=True
2025-11-04 12:46:49,262 - integration.integrations.grpc_client_integration - INFO - 🔌 [DEBUG] GrpcClientIntegration passing server 'production' to GrpcClient: ssl_verify=False
2025-11-04 12:46:49,262 - integration.integrations.grpc_client_integration - INFO - 🔌 [DEBUG] GrpcClientIntegration passing server 'fallback' to GrpcClient: ssl_verify=True
2025-11-04 12:46:49,262 - modules.grpc_client.core.grpc_client - INFO - 🔌 [DEBUG] _initialize_servers creating ServerConfig for 'local': ssl_verify=True
2025-11-04 12:46:49,262 - modules.grpc_client.core.grpc_client - INFO - 🔌 [DEBUG] Created ServerConfig for 'local': ssl_verify=True
2025-11-04 12:46:49,262 - modules.grpc_client.core.connection_manager - INFO - 🌐 Добавлен сервер local: 127.0.0.1:50051
2025-11-04 12:46:49,262 - modules.grpc_client.core.grpc_client - INFO - 🔌 [DEBUG] _initialize_servers creating ServerConfig for 'production': ssl_verify=False
2025-11-04 12:46:49,262 - modules.grpc_client.core.grpc_client - INFO - 🔌 [DEBUG] Created ServerConfig for 'production': ssl_verify=False
2025-11-04 12:46:49,262 - modules.grpc_client.core.connection_manager - INFO - 🌐 Добавлен сервер production: 20.151.51.172:443
2025-11-04 12:46:49,262 - modules.grpc_client.core.grpc_client - INFO - 🔌 [DEBUG] _initialize_servers creating ServerConfig for 'fallback': ssl_verify=True
2025-11-04 12:46:49,262 - modules.grpc_client.core.grpc_client - INFO - 🔌 [DEBUG] Created ServerConfig for 'fallback': ssl_verify=True
2025-11-04 12:46:49,262 - modules.grpc_client.core.connection_manager - INFO - 🌐 Добавлен сервер fallback: 127.0.0.1:50052
2025-11-04 12:46:49,262 - modules.grpc_client.core.grpc_client - INFO - 🌐 Инициализировано 3 серверов
2025-11-04 12:46:49,283 - modules.grpc_client.core.grpc_client - INFO - 🔌 [DEBUG] Config says default server: 'production'
2025-11-04 12:46:49,283 - modules.grpc_client.core.grpc_client - INFO - 🔌 [DEBUG] Available servers: ['local', 'production', 'fallback']
2025-11-04 12:46:49,283 - modules.grpc_client.core.grpc_client - INFO - 🌐 Установлен сервер по умолчанию: production
2025-11-04 12:46:49,283 - integration.core.event_bus - INFO - 📝 Подписка на событие: voice.recognition_completed (приоритет: HIGH)
2025-11-04 12:46:49,283 - integration.core.event_bus - INFO - 📝 Подписка на событие: screenshot.captured (приоритет: HIGH)
2025-11-04 12:46:49,283 - integration.core.event_bus - INFO - 📝 Подписка на событие: hardware.id_obtained (приоритет: HIGH)
2025-11-04 12:46:49,283 - integration.core.event_bus - INFO - 📝 Подписка на событие: hardware.id_response (приоритет: HIGH)
2025-11-04 12:46:49,283 - integration.core.event_bus - INFO - 📝 Подписка на событие: keyboard.short_press (приоритет: CRITICAL)
2025-11-04 12:46:49,283 - integration.core.event_bus - INFO - 📝 Подписка на событие: grpc.request_cancel (приоритет: HIGH)
2025-11-04 12:46:49,283 - integration.core.event_bus - INFO - 📝 Подписка на событие: network.status_changed (приоритет: MEDIUM)
2025-11-04 12:46:49,283 - integration.core.event_bus - INFO - 📝 Подписка на событие: app.shutdown (приоритет: HIGH)
2025-11-04 12:46:49,283 - integration.integrations.grpc_client_integration - INFO - GrpcClientIntegration initialized
✅ grpc инициализирован
🔧 Инициализация speech_playback...
2025-11-04 12:46:49,283 - modules.speech_playback.core.buffer - INFO - 🔧 ChunkBuffer инициализирован (max_memory: 50MB, channels: 1)
2025-11-04 12:46:49,284 - modules.speech_playback.macos.core_audio - INFO - 🔧 CoreAudioManager создан (macOS: True)
2025-11-04 12:46:49,284 - modules.speech_playback.macos.performance - INFO - 📊 PerformanceMonitor создан
2025-11-04 12:46:49,284 - modules.speech_playback.core.player - INFO - 🔧 SequentialSpeechPlayer инициализирован
2025-11-04 12:46:49,284 - integration.integrations.speech_playback_integration - WARNING - ⚠️ [AUDIO_DEBUG] SequentialSpeechPlayer не поддерживает set_event_bus
2025-11-04 12:46:49,284 - integration.core.event_bus - INFO - 📝 Подписка на событие: grpc.response.audio (приоритет: HIGH)
2025-11-04 12:46:49,284 - integration.core.event_bus - INFO - 📝 Подписка на событие: grpc.request_completed (приоритет: HIGH)
2025-11-04 12:46:49,284 - integration.core.event_bus - INFO - 📝 Подписка на событие: grpc.request_failed (приоритет: HIGH)
2025-11-04 12:46:49,284 - integration.core.event_bus - INFO - 📝 Подписка на событие: playback.raw_audio (приоритет: HIGH)
2025-11-04 12:46:49,284 - integration.core.event_bus - INFO - 📝 Подписка на событие: playback.signal (приоритет: HIGH)
2025-11-04 12:46:49,284 - integration.core.event_bus - INFO - 📝 Подписка на событие: grpc.request_cancel (приоритет: CRITICAL)
2025-11-04 12:46:49,284 - integration.core.event_bus - INFO - 📝 Подписка на событие: playback.cancelled (приоритет: CRITICAL)
2025-11-04 12:46:49,284 - integration.core.event_bus - INFO - 📝 Подписка на событие: voice.mic_closed (приоритет: HIGH)
2025-11-04 12:46:49,284 - integration.core.event_bus - INFO - 📝 Подписка на событие: app.shutdown (приоритет: HIGH)
2025-11-04 12:46:49,284 - integration.integrations.speech_playback_integration - INFO - SpeechPlaybackIntegration initialized
✅ speech_playback инициализирован
🔧 Инициализация signals...
2025-11-04 12:46:49,284 - integration.core.event_bus - INFO - 📝 Подписка на событие: voice.mic_opened (приоритет: MEDIUM)
2025-11-04 12:46:49,284 - integration.core.event_bus - INFO - 📝 Подписка на событие: playback.completed (приоритет: MEDIUM)
2025-11-04 12:46:49,284 - integration.core.event_bus - INFO - 📝 Подписка на событие: playback.cancelled (приоритет: MEDIUM)
2025-11-04 12:46:49,284 - integration.core.event_bus - INFO - 📝 Подписка на событие: grpc.request_failed (приоритет: MEDIUM)
2025-11-04 12:46:49,284 - integration.core.event_bus - INFO - 📝 Подписка на событие: voice.recognition_failed (приоритет: MEDIUM)
2025-11-04 12:46:49,284 - integration.integrations.signal_integration - INFO - SignalIntegration initialized
✅ signals инициализирован
🔧 Инициализация autostart_manager...
2025-11-04 12:46:49,284 - integration.integrations.autostart_manager_integration - INFO - 🔧 Инициализация AutostartManagerIntegration
2025-11-04 12:46:49,284 - integration.core.event_bus - INFO - 📝 Подписка на событие: app.startup (приоритет: LOW)
2025-11-04 12:46:49,284 - integration.core.event_bus - INFO - 📝 Подписка на событие: autostart.check_status (приоритет: MEDIUM)
2025-11-04 12:46:49,284 - integration.integrations.autostart_manager_integration - INFO - ✅ AutostartManagerIntegration инициализирован
✅ autostart_manager инициализирован
🔧 Инициализация welcome_message...
2025-11-04 12:46:49,284 - integration.integrations.welcome_message_integration - INFO - 🔧 [WELCOME_INTEGRATION] Инициализация...
2025-11-04 12:46:49,284 - integration.core.event_bus - INFO - 📝 Подписка на событие: system.ready_to_greet (приоритет: MEDIUM)
2025-11-04 12:46:49,284 - integration.core.event_bus - INFO - 📝 Подписка на событие: permissions.status_checked (приоритет: HIGH)
2025-11-04 12:46:49,284 - integration.core.event_bus - INFO - 📝 Подписка на событие: permissions.changed (приоритет: HIGH)
2025-11-04 12:46:49,284 - integration.core.event_bus - INFO - 📝 Подписка на событие: permissions.requested (приоритет: MEDIUM)
2025-11-04 12:46:49,284 - integration.core.event_bus - INFO - 📝 Подписка на событие: permissions.integration_ready (приоритет: MEDIUM)
2025-11-04 12:46:49,284 - integration.integrations.welcome_message_integration - INFO - ✅ [WELCOME_INTEGRATION] Инициализирован
✅ welcome_message инициализирован
🔧 Инициализация voiceover_ducking...
2025-11-04 12:46:49,284 - integration.core.base_integration - INFO - Initializing voiceover_ducking...
2025-11-04 12:46:49,284 - integration.integrations.voiceover_ducking_integration - INFO - 🔧 Инициализация VoiceOverDuckingIntegration...
2025-11-04 12:46:49,483 - modules.voiceover_control.core.controller - WARNING - 🔍 VoiceOver: CalledProcessError - exit_code=1, stderr='39:50: execution error: The variable speechMuted is not defined. (-2753)
'
2025-11-04 12:46:49,484 - modules.voiceover_control.core.controller - INFO - VoiceOverController: speechMuted AppleScript commands unavailable - using control key fallback
2025-11-04 12:46:49,484 - modules.voiceover_control.core.controller - INFO - VoiceOverController initialized successfully (VoiceOver was running: False)
2025-11-04 12:46:49,484 - integration.core.event_bus - INFO - 📝 Подписка на событие: app.mode_changed (приоритет: MEDIUM)
2025-11-04 12:46:49,484 - integration.core.event_bus - INFO - 📝 Подписка на событие: keyboard.press (приоритет: MEDIUM)
2025-11-04 12:46:49,484 - integration.core.event_bus - INFO - 📝 Подписка на событие: app.shutdown (приоритет: MEDIUM)
2025-11-04 12:46:49,484 - integration.integrations.voiceover_ducking_integration - INFO - ✅ VoiceOverDuckingIntegration инициализирован
2025-11-04 12:46:49,484 - integration.core.base_integration - INFO - voiceover_ducking initialized successfully
✅ voiceover_ducking инициализирован
🔧 Инициализация first_run_permissions...
2025-11-04 12:46:49,484 - integration.integrations.first_run_permissions_integration - INFO - 🔧 [FIRST_RUN_PERMISSIONS] Инициализация...
2025-11-04 12:46:49,485 - integration.core.state_manager - DEBUG - 📊 Данные состояния обновлены: permissions_restart_pending
2025-11-04 12:46:49,485 - integration.integrations.first_run_permissions_integration - INFO - ✅ [FIRST_RUN_PERMISSIONS] Перезапуск после first_run завершён успешно
2025-11-04 12:46:49,485 - integration.integrations.first_run_permissions_integration - INFO -    (обнаружено через NEXY_FIRST_RUN_RESTARTED env)
2025-11-04 12:46:49,485 - integration.core.event_bus - DEBUG - EventBus: dispatch 'permissions.first_run_completed' to 2 subscriber(s)
2025-11-04 12:46:49,485 - integration.core.event_bus - DEBUG - EventBus: scheduled async callback on main loop for 'permissions.first_run_completed': <bound method VoiceRecognitionIntegration._on_first_run_completed of <integration.integrations.voice_recognition_integration.VoiceRecognitionIntegration object at 0x116d99be0>> -> <Future at 0x116d816d0 state=pending>
2025-11-04 12:46:49,485 - integration.core.event_bus - DEBUG - EventBus: scheduled async callback on main loop for 'permissions.first_run_completed': <bound method SimpleModuleCoordinator._on_permissions_completed of <integration.core.simple_module_coordinator.SimpleModuleCoordinator object at 0x1168d2a50>> -> <Future at 0x116ed8180 state=pending>
2025-11-04 12:46:49,485 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: permissions.first_run_completed
2025-11-04 12:46:49,485 - integration.integrations.voice_recognition_integration - INFO - 🔓 [VOICE_RECOGNITION] First run завершён - разблокировка активации микрофона
✅ [PERMISSIONS] Запрос разрешений завершен (session=restarted)
2025-11-04 12:46:49,485 - integration.core.simple_module_coordinator - INFO - ✅ [PERMISSIONS] Запрос разрешений завершен (session=restarted)
2025-11-04 12:46:49,485 - integration.integrations.first_run_permissions_integration - INFO - [FIRST_RUN_PERMISSIONS] restart_completed.flag удалён: /Users/sergiyzasorin/Library/Application Support/Nexy/restart_completed.flag
2025-11-04 12:46:49,485 - integration.integrations.first_run_permissions_integration - INFO - [FIRST_RUN_PERMISSIONS] permissions_first_run_completed.flag сохранён: /Users/sergiyzasorin/Library/Application Support/Nexy/permissions_first_run_completed.flag
2025-11-04 12:46:49,485 - integration.integrations.first_run_permissions_integration - INFO - [FIRST_RUN_PERMISSIONS] ✅ Флаги обработаны: restart_completed.flag удалён, permissions_first_run_completed.flag сохранён
2025-11-04 12:46:49,485 - integration.core.state_manager - DEBUG - 📊 Данные состояния обновлены: permissions_restart_completed_fallback
2025-11-04 12:46:49,485 - integration.integrations.first_run_permissions_integration - INFO - [FIRST_RUN_PERMISSIONS] Set restart_completed_fallback=True in state_manager
2025-11-04 12:46:49,485 - integration.integrations.first_run_permissions_integration - INFO - ✅ [FIRST_RUN_PERMISSIONS] Инициализирован
✅ first_run_permissions инициализирован
🔧 Инициализация Workflows...
🔧 Инициализация workflow listening...
2025-11-04 12:46:49,485 - integration.core.event_bus - INFO - 📝 Подписка на событие: voice.recording_start (приоритет: HIGH)
2025-11-04 12:46:49,485 - integration.core.event_bus - INFO - 📝 Подписка на событие: voice.recording_stop (приоритет: HIGH)
2025-11-04 12:46:49,485 - integration.core.event_bus - INFO - 📝 Подписка на событие: keyboard.short_press (приоритет: CRITICAL)
2025-11-04 12:46:49,485 - integration.core.event_bus - INFO - 📝 Подписка на событие: interrupt.request (приоритет: CRITICAL)
2025-11-04 12:46:49,486 - integration.core.event_bus - INFO - 📝 Подписка на событие: app.mode_changed (приоритет: MEDIUM)
2025-11-04 12:46:49,486 - integration.core.event_bus - INFO - 📝 Подписка на событие: voice.activity_detected (приоритет: LOW)
2025-11-04 12:46:49,486 - integration.workflows.base_workflow - INFO - 🔄 ListeningWorkflow: инициализирован
✅ Workflow listening инициализирован
🔧 Инициализация workflow processing...
2025-11-04 12:46:49,486 - integration.core.event_bus - INFO - 📝 Подписка на событие: app.mode_changed (приоритет: HIGH)
2025-11-04 12:46:49,486 - integration.core.event_bus - INFO - 📝 Подписка на событие: screenshot.captured (приоритет: HIGH)
2025-11-04 12:46:49,486 - integration.core.event_bus - INFO - 📝 Подписка на событие: screenshot.error (приоритет: HIGH)
2025-11-04 12:46:49,486 - integration.core.event_bus - INFO - 📝 Подписка на событие: grpc.request_started (приоритет: HIGH)
2025-11-04 12:46:49,486 - integration.core.event_bus - INFO - 📝 Подписка на событие: grpc.request_completed (приоритет: HIGH)
2025-11-04 12:46:49,486 - integration.core.event_bus - INFO - 📝 Подписка на событие: grpc.request_failed (приоритет: HIGH)
2025-11-04 12:46:49,486 - integration.core.event_bus - INFO - 📝 Подписка на событие: playback.started (приоритет: HIGH)
2025-11-04 12:46:49,486 - integration.core.event_bus - INFO - 📝 Подписка на событие: playback.completed (приоритет: HIGH)
2025-11-04 12:46:49,486 - integration.core.event_bus - INFO - 📝 Подписка на событие: playback.failed (приоритет: HIGH)
2025-11-04 12:46:49,486 - integration.core.event_bus - INFO - 📝 Подписка на событие: keyboard.short_press (приоритет: CRITICAL)
2025-11-04 12:46:49,486 - integration.core.event_bus - INFO - 📝 Подписка на событие: interrupt.request (приоритет: CRITICAL)
2025-11-04 12:46:49,486 - integration.workflows.base_workflow - INFO - 🔄 ProcessingWorkflow: инициализирован
✅ Workflow processing инициализирован
✅ Интеграции инициализированы
🔧 Настройка координации...
2025-11-04 12:46:49,486 - integration.core.event_bus - INFO - 📝 Подписка на событие: app.startup (приоритет: HIGH)
2025-11-04 12:46:49,486 - integration.core.event_bus - INFO - 📝 Подписка на событие: app.shutdown (приоритет: HIGH)
2025-11-04 12:46:49,486 - integration.core.event_bus - INFO - 📝 Подписка на событие: app.mode_changed (приоритет: MEDIUM)
2025-11-04 12:46:49,486 - integration.core.event_bus - INFO - 📝 Подписка на событие: tray.quit_clicked (приоритет: HIGH)
2025-11-04 12:46:49,486 - integration.core.event_bus - INFO - 📝 Подписка на событие: screenshot.captured (приоритет: MEDIUM)
2025-11-04 12:46:49,486 - integration.core.event_bus - INFO - 📝 Подписка на событие: screenshot.error (приоритет: MEDIUM)
✅ Координация настроена
✅ Координация настроена
🔧 Настройка авто-всё связей...
🔧 [AUTO] VoiceRecognitionIntegration будет использовать audio_default
✅ Авто-всё связи настроены

============================================================
✅ ВСЕ КОМПОНЕНТЫ ИНИЦИАЛИЗИРОВАНЫ!
============================================================
🎯 Иконка должна появиться в меню-баре macOS
🖱️ Кликните по иконке, чтобы увидеть меню
⌨️ Нажмите ПРОБЕЛ для тестирования клавиатуры
⌨️ Нажмите Ctrl+C для выхода
============================================================

🚀 Запуск всех интеграций...
🚀 Запуск instance_manager...
🚀 InstanceManagerIntegration.start() вызван
🔍 Проверка дублирования экземпляров...
🧹 Невалидная блокировка очищена
🔍 Результат проверки дублирования: InstanceStatus.SINGLE
✅ Дублирование не обнаружено, захватываем блокировку...
✅ Блокировка захвачена успешно
✅ Nexy запущен успешно (первый экземпляр)
2025-11-04 12:46:49,487 - integration.core.event_bus - DEBUG - EventBus: dispatch 'instance.status_checked' to 0 subscriber(s)
2025-11-04 12:46:49,487 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: instance.status_checked
✅ instance_manager запущен
🚀 Запуск hardware_id...
2025-11-04 12:46:49,487 - integration.integrations.hardware_id_integration - INFO - HardwareIdIntegration started
2025-11-04 12:46:49,487 - modules.hardware_id.core.hardware_identifier - INFO - 🔍 Начинаем получение Hardware ID...
2025-11-04 12:46:49,487 - modules.hardware_id.utils.caching - INFO - ✅ Hardware UUID загружен из кэша: E03D2455-8EF1-52...
2025-11-04 12:46:49,487 - modules.hardware_id.utils.validation - DEBUG - ✅ UUID валиден: E03D2455-8EF1-5270-AA03-13B5771C7CB2
2025-11-04 12:46:49,487 - modules.hardware_id.utils.validation - DEBUG - ✅ Результат Hardware ID валиден
2025-11-04 12:46:49,487 - modules.hardware_id.core.hardware_identifier - INFO - ✅ Hardware ID загружен из кэша: E03D2455-8EF1-52...
2025-11-04 12:46:49,487 - modules.hardware_id.core.hardware_identifier - INFO - ✅ Hardware ID загружен из кэша
2025-11-04 12:46:49,487 - integration.integrations.hardware_id_integration - INFO - Hardware ID ready (cache, cached=True) — uuid=E03D2455…
2025-11-04 12:46:49,487 - integration.core.event_bus - DEBUG - EventBus: dispatch 'hardware.id_obtained' to 1 subscriber(s)
2025-11-04 12:46:49,487 - integration.core.event_bus - DEBUG - EventBus: scheduled async callback on main loop for 'hardware.id_obtained': <bound method GrpcClientIntegration._on_hardware_id of <integration.integrations.grpc_client_integration.GrpcClientIntegration object at 0x116d9a270>> -> <Future at 0x116da8cb0 state=pending>
2025-11-04 12:46:49,488 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: hardware.id_obtained
2025-11-04 12:46:49,488 - integration.integrations.hardware_id_integration - INFO - Hardware ID published on startup: E03D2455...
✅ hardware_id запущен
🚀 Запуск first_run_permissions...
2025-11-04 12:46:49,488 - integration.integrations.first_run_permissions_integration - INFO - ✅ [FIRST_RUN_PERMISSIONS] Первый запуск уже завершён - пропускаем
2025-11-04 12:46:50,010 - integration.core.gateways.decision_engine - WARNING - decision_engine_rule_miss gateway=decide_continue_integration_startup ctx=ctx={mic=granted,screen=granted,accessibility=granted,device=default_ok,network=online,firstRun=False,appMode=sleeping,restart_pending=False,update_in_progress=False} source=coordinator_gateway available_rules=2 fallback_to=START
2025-11-04 12:46:50,010 - integration.core.gateways.base - DEBUG - decision=start reason=no_rule_matched ctx={mic=granted,screen=granted,accessibility=granted,device=default_ok,network=online,firstRun=False,appMode=sleeping,restart_pending=False,update_in_progress=False} source=coordinator_gateway duration_ms=0
2025-11-04 12:46:50,010 - integration.core.simple_module_coordinator - INFO - decision=continue reason=no_restart_pending ctx={firstRun=False,restart_pending=False} source=coordinator duration_ms=522
✅ [PERMISSIONS] Первый запуск уже завершён ранее, продолжаем запуск...
✅ first_run_permissions запущен
🚀 Запуск permission_restart...
2025-11-04 12:46:50,010 - integration.core.base_integration - INFO - Starting PermissionRestart...
2025-11-04 12:46:50,010 - integration.core.event_bus - INFO - 📝 Подписка на событие: permissions.changed (приоритет: HIGH)
2025-11-04 12:46:50,010 - integration.core.event_bus - INFO - 📝 Подписка на событие: permissions.status_checked (приоритет: MEDIUM)
2025-11-04 12:46:50,010 - integration.core.event_bus - INFO - 📝 Подписка на событие: permissions.first_run_completed (приоритет: HIGH)
2025-11-04 12:46:50,010 - integration.core.event_bus - INFO - 📝 Подписка на событие: updater.update_started (приоритет: MEDIUM)
2025-11-04 12:46:50,010 - integration.core.event_bus - INFO - 📝 Подписка на событие: updater.update_completed (приоритет: HIGH)
2025-11-04 12:46:50,010 - integration.core.event_bus - INFO - 📝 Подписка на событие: updater.update_skipped (приоритет: HIGH)
2025-11-04 12:46:50,010 - integration.core.event_bus - INFO - 📝 Подписка на событие: app.startup (приоритет: MEDIUM)
2025-11-04 12:46:50,010 - integration.integrations.permission_restart_integration - INFO - [PERMISSION_RESTART] Subscribed to permission events
2025-11-04 12:46:50,010 - integration.integrations.permission_restart_integration - INFO - [PERMISSION_RESTART] First run handling: will only react to live permissions.first_run_completed events
2025-11-04 12:46:50,011 - integration.core.base_integration - INFO - PermissionRestart started successfully
✅ permission_restart запущен
🚀 Запуск tray...
2025-11-04 12:46:50,011 - integration.integrations.tray_controller_integration - INFO - 🚀 Запуск TrayControllerIntegration...
2025-11-04 12:46:50,011 - modules.tray_controller.core.tray_controller - INFO - 🚀 Запуск TrayController
🎯 TRAY DEBUG: TrayIconGenerator.create_circle_icon status=TrayStatus.SLEEPING (type: <enum 'TrayStatus'>)
🎯 TRAY DEBUG: Available colors: {<TrayStatus.SLEEPING: 'sleeping'>: '#808080', <TrayStatus.LISTENING: 'listening'>: '#007AFF', <TrayStatus.PROCESSING: 'processing'>: '#FF9500'}
🎯 TRAY DEBUG: Selected color: #808080
🎯 TRAY DEBUG: create_icon_file вызван для status=TrayStatus.SLEEPING
🎯 TRAY DEBUG: generated color=#808080, PIL_available=True
2025-11-04 12:46:50,037 - modules.tray_controller.core.tray_controller - INFO - ✅ TrayController готов к запуску
2025-11-04 12:46:50,037 - modules.tray_controller.core.tray_controller - INFO - ℹ️ Для отображения иконки запустите app.run() в главном потоке
2025-11-04 12:46:50,037 - integration.integrations.tray_controller_integration - INFO - 🔄 Синхронизация с режимом приложения: sleeping → sleeping
2025-11-04 12:46:50,037 - integration.core.event_bus - DEBUG - EventBus: dispatch 'tray.integration_ready' to 0 subscriber(s)
2025-11-04 12:46:50,037 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: tray.integration_ready
2025-11-04 12:46:50,037 - integration.integrations.tray_controller_integration - INFO - ✅ TrayControllerIntegration запущен
✅ tray запущен
🚀 Запуск mode_management...
2025-11-04 12:46:50,037 - integration.integrations.mode_management_integration - INFO - ModeManagementIntegration started
✅ mode_management запущен
🚀 Запуск input...
🔧 DEBUG: InputProcessingIntegration.start() вызван
2025-11-04 12:46:50,037 - integration.integrations.input_processing_integration - INFO - 🔧 INPUT_PROCESSING: получен loop из EventBus: 4673562704
2025-11-04 12:46:50,037 - integration.integrations.input_processing_integration - INFO - 🔧 INPUT_PROCESSING: передаём loop в keyboard_monitor (loop=4673562704, running=True)
2025-11-04 12:46:50,037 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔑 QuartzMonitor: установлен event loop для async-колбэков (loop=4673562704, running=True)
🔑 QuartzMonitor: установлен event loop (loop=4673562704, running=True)
2025-11-04 12:46:50,037 - integration.integrations.input_processing_integration - INFO - 🔧 Тестируем QuartzKeyboardMonitor после инициализации...
2025-11-04 12:46:50,037 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔐 Проверяем разрешения для Quartz Event Tap...
🔐 Проверяем разрешения для Quartz Event Tap...
2025-11-04 12:46:50,093 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔐 Accessibility permission: True
🔐 Accessibility permission: True
2025-11-04 12:46:50,124 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - QuartzMonitor: CGEventTap включен для keycode=49
2025-11-04 12:46:50,124 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🎹 Quartz-монитор клавиатуры запущен
2025-11-04 12:46:50,124 - integration.integrations.input_processing_integration - INFO - ✅ QuartzKeyboardMonitor успешно запущен
🔧 DEBUG: KeyboardMonitor статус: {'is_monitoring': True, 'key_pressed': False, 'keyboard_available': True, 'fallback_mode': False, 'config': {'key': 'space', 'short_press_threshold': 0.1, 'long_press_threshold': 0.6}, 'callbacks_registered': 4, 'backend': 'quartz'}
🔧 DEBUG: Callbacks зарегистрированы: 4
🔧 DEBUG: Мониторинг активен: True
⌨️ DEBUG: НАЖМИТЕ ПРОБЕЛ СЕЙЧАС ДЛЯ ТЕСТИРОВАНИЯ!
2025-11-04 12:46:50,124 - integration.integrations.input_processing_integration - INFO - ✅ input_processing запущен
✅ input запущен
🚀 Запуск voice_recognition...
2025-11-04 12:46:50,124 - integration.integrations.voice_recognition_integration - DEBUG - 🔍 Microphone permission check relies on macOS defaults
2025-11-04 12:46:50,124 - integration.integrations.voice_recognition_integration - INFO - VoiceRecognitionIntegration started
✅ voice_recognition запущен
🚀 Запуск network...
2025-11-04 12:46:50,124 - integration.integrations.network_manager_integration - INFO - Starting NetworkManagerIntegration...
2025-11-04 12:46:50,124 - modules.network_manager.core.network_manager - INFO - Starting NetworkManager monitoring...
2025-11-04 12:46:50,124 - modules.network_manager.core.network_manager - INFO - NetworkManager monitoring started
2025-11-04 12:46:50,124 - integration.integrations.network_manager_integration - INFO - NetworkManagerIntegration started successfully
✅ network запущен
🚀 Запуск interrupt...
2025-11-04 12:46:50,124 - integration.integrations.interrupt_management_integration - INFO - Starting InterruptManagementIntegration...
2025-11-04 12:46:50,124 - integration.integrations.interrupt_management_integration - INFO - InterruptManagementIntegration started successfully
✅ interrupt запущен
🚀 Запуск screenshot_capture...
2025-11-04 12:46:50,124 - integration.integrations.screenshot_capture_integration - INFO - ScreenshotCaptureIntegration started
✅ screenshot_capture запущен
🚀 Запуск grpc...
2025-11-04 12:46:50,124 - integration.integrations.grpc_client_integration - INFO - GrpcClientIntegration started (lazy connect)
✅ grpc запущен
🚀 Запуск speech_playback...
✅ speech_playback запущен
🚀 Запуск signals...
2025-11-04 12:46:50,124 - integration.integrations.signal_integration - INFO - SignalIntegration started
✅ signals запущен
🚀 Запуск update_notification...
2025-11-04 12:46:50,124 - integration.core.base_integration - INFO - Starting UpdateNotification...
2025-11-04 12:46:50,124 - integration.integrations.update_notification_integration - INFO - [UPDATE_NOTIFY] Интеграция готова к приему событий обновления
2025-11-04 12:46:50,124 - integration.core.base_integration - INFO - UpdateNotification started successfully
✅ update_notification запущен
🚀 Запуск updater...
2025-11-04 12:46:50,124 - integration.integrations.updater_integration - INFO - ⏭️ Пропускаю запуск UpdaterIntegration - отключен
✅ updater запущен
🚀 Запуск welcome_message...
2025-11-04 12:46:50,124 - integration.integrations.welcome_message_integration - INFO - ✅ [WELCOME_INTEGRATION] Запущен
✅ welcome_message запущен
🚀 Запуск voiceover_ducking...
2025-11-04 12:46:50,124 - integration.core.base_integration - INFO - Starting voiceover_ducking...
2025-11-04 12:46:50,124 - integration.integrations.voiceover_ducking_integration - INFO - 🚀 VoiceOverDuckingIntegration запущен
2025-11-04 12:46:50,124 - integration.core.base_integration - INFO - voiceover_ducking started successfully
✅ voiceover_ducking запущен
🚀 Запуск autostart_manager...
2025-11-04 12:46:50,124 - integration.integrations.autostart_manager_integration - INFO - 🚀 Запуск AutostartManagerIntegration
2025-11-04 12:46:50,124 - integration.core.event_bus - DEBUG - EventBus: dispatch 'autostart.status_checked' to 0 subscriber(s)
2025-11-04 12:46:50,125 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: autostart.status_checked
2025-11-04 12:46:50,125 - integration.integrations.autostart_manager_integration - WARNING - ⚠️ LaunchAgent автозапуск не найден
2025-11-04 12:46:50,125 - integration.integrations.autostart_manager_integration - INFO - ✅ AutostartManagerIntegration запущен
✅ autostart_manager запущен
🚀 Запуск Workflows...
🚀 Запуск workflow listening...
2025-11-04 12:46:50,125 - integration.workflows.listening_workflow - INFO - 🎤 ListeningWorkflow: готов к координации прослушивания
2025-11-04 12:46:50,125 - integration.workflows.base_workflow - INFO - 🚀 ListeningWorkflow: запущен
✅ Workflow listening запущен
🚀 Запуск workflow processing...
2025-11-04 12:46:50,125 - integration.workflows.processing_workflow - INFO - ⚙️ ProcessingWorkflow: готов к координации обработки
2025-11-04 12:46:50,125 - integration.workflows.base_workflow - INFO - 🚀 ProcessingWorkflow: запущен
✅ Workflow processing запущен
2025-11-04 12:46:50,125 - integration.core.event_bus - DEBUG - EventBus: dispatch 'app.startup' to 9 subscriber(s)
2025-11-04 12:46:50,125 - integration.core.event_bus - DEBUG - EventBus: scheduled async callback on main loop for 'app.startup': <bound method HardwareIdIntegration._on_app_startup of <integration.integrations.hardware_id_integration.HardwareIdIntegration object at 0x1168d3a10>> -> <Future at 0x11693fac0 state=pending>
2025-11-04 12:46:50,125 - integration.core.event_bus - DEBUG - EventBus: scheduled async callback on main loop for 'app.startup': <bound method TrayControllerIntegration._on_app_startup of <integration.integrations.tray_controller_integration.TrayControllerIntegration object at 0x116d98050>> -> <Future at 0x116ee59d0 state=pending>
2025-11-04 12:46:50,125 - integration.core.event_bus - DEBUG - EventBus: scheduled async callback on main loop for 'app.startup': <bound method SimpleModuleCoordinator._on_app_startup of <integration.core.simple_module_coordinator.SimpleModuleCoordinator object at 0x1168d2a50>> -> <Future at 0x116902f50 state=pending>
2025-11-04 12:46:50,125 - integration.core.event_bus - DEBUG - EventBus: scheduled async callback on main loop for 'app.startup': <bound method InstanceManagerIntegration._on_app_startup of <integration.integrations.instance_manager_integration.InstanceManagerIntegration object at 0x1168d3620>> -> <Future at 0x116d6a150 state=pending>
2025-11-04 12:46:50,125 - integration.core.event_bus - DEBUG - EventBus: scheduled async callback on main loop for 'app.startup': <bound method UpdaterIntegration._on_app_startup of <integration.integrations.updater_integration.UpdaterIntegration object at 0x116d98440>> -> <Future at 0x116f06990 state=pending>
2025-11-04 12:46:50,125 - integration.core.event_bus - DEBUG - EventBus: scheduled async callback on main loop for 'app.startup': <bound method NetworkManagerIntegration._on_app_startup of <integration.integrations.network_manager_integration.NetworkManagerIntegration object at 0x116d992b0>> -> <Future at 0x116f06b70 state=pending>
2025-11-04 12:46:50,125 - integration.core.event_bus - DEBUG - EventBus: scheduled async callback on main loop for 'app.startup': <bound method InterruptManagementIntegration._on_app_startup of <integration.integrations.interrupt_management_integration.InterruptManagementIntegration object at 0x116d996a0>> -> <Future at 0x116d75630 state=pending>
2025-11-04 12:46:50,125 - integration.core.event_bus - DEBUG - EventBus: scheduled async callback on main loop for 'app.startup': <bound method PermissionRestartIntegration._on_app_startup_event of <integration.integrations.permission_restart_integration.PermissionRestartIntegration object at 0x116d98c20>> -> <Future at 0x116d775b0 state=pending>
2025-11-04 12:46:50,125 - integration.core.event_bus - DEBUG - EventBus: scheduled async callback on main loop for 'app.startup': <bound method AutostartManagerIntegration._on_app_startup of <integration.integrations.autostart_manager_integration.AutostartManagerIntegration object at 0x116d9ae40>> -> <Future at 0x116f30bb0 state=pending>
2025-11-04 12:46:50,125 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: app.startup
✅ Все интеграции запущены
🎯 Запуск приложения с иконкой в меню-баре...
2025-11-04 12:46:50,127 - integration.core.event_bus - DEBUG - EventBus: dispatch 'hardware.id_obtained' to 1 subscriber(s)
2025-11-04 12:46:50,127 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'hardware.id_obtained': <bound method GrpcClientIntegration._on_hardware_id of <integration.integrations.grpc_client_integration.GrpcClientIntegration object at 0x116d9a270>>
2025-11-04 12:46:50,127 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: hardware.id_obtained
2025-11-04 12:46:50,127 - integration.integrations.tray_controller_integration - INFO - 🚀 Обработка запуска приложения в TrayControllerIntegration
2025-11-04 12:46:50,127 - integration.integrations.tray_controller_integration - INFO - 🔄 Синхронизация с режимом приложения: sleeping → sleeping
🚀 Обработка запуска приложения в координаторе
📱 Обработка события app.startup
2025-11-04 12:46:50,127 - integration.integrations.updater_integration - INFO - 🚀 Обработка запуска приложения в UpdaterIntegration
2025-11-04 12:46:50,127 - integration.integrations.network_manager_integration - INFO - App startup - publishing network status snapshot
2025-11-04 12:46:50,127 - integration.core.event_bus - DEBUG - EventBus: dispatch 'network.status_snapshot' to 0 subscriber(s)
2025-11-04 12:46:50,127 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: network.status_snapshot
2025-11-04 12:46:50,127 - integration.core.event_bus - DEBUG - EventBus: dispatch 'tray.update_tooltip' to 0 subscriber(s)
2025-11-04 12:46:50,127 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: tray.update_tooltip
2025-11-04 12:46:50,127 - integration.integrations.interrupt_management_integration - INFO - App startup - initializing interrupt management
2025-11-04 12:46:50,127 - integration.core.event_bus - DEBUG - EventBus: dispatch 'interrupt.status_snapshot' to 0 subscriber(s)
2025-11-04 12:46:50,127 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: interrupt.status_snapshot
2025-11-04 12:46:50,132 - modules.permissions.macos.accessibility_handler - WARNING - ⚠️ Quartz/AX API недоступен — считаем, что разрешение не выдано
2025-11-04 12:46:50,132 - modules.permissions.first_run.status_checker - DEBUG - ♿ Accessibility: NOT_DETERMINED or DENIED
2025-11-04 12:46:50,150 - modules.permissions.first_run.status_checker - DEBUG - ⌨️ Input Monitoring: IOHIDCheckAccess вернул False, выполняем tccutil check…
2025-11-04 12:46:50,159 - modules.permissions.first_run.status_checker - DEBUG - ⌨️ Input Monitoring: NOT_DETERMINED or DENIED
2025-11-04 12:46:50,182 - modules.permissions.macos.screen_capture_permission - INFO - ✅ Screen Capture permission granted
2025-11-04 12:46:50,182 - modules.permissions.first_run.status_checker - DEBUG - 📺 Screen Capture: GRANTED
2025-11-04 12:46:50,182 - modules.permission_restart.core.permission_change_detector - DEBUG - [PERMISSION_RESTART] Event received: type=permissions.init perm=accessibility old=not_determined new=not_determined session=app_startup_init source=app_startup_init (critical=True)
2025-11-04 12:46:50,182 - modules.permission_restart.core.permission_change_detector - DEBUG - [PERMISSION_RESTART] No restart transition for accessibility (baseline=not_determined, new=not_determined, critical=True)
2025-11-04 12:46:50,182 - modules.permission_restart.core.permission_change_detector - DEBUG - [PERMISSION_RESTART] Event received: type=permissions.init perm=input_monitoring old=not_determined new=not_determined session=app_startup_init source=app_startup_init (critical=True)
2025-11-04 12:46:50,182 - modules.permission_restart.core.permission_change_detector - DEBUG - [PERMISSION_RESTART] No restart transition for input_monitoring (baseline=not_determined, new=not_determined, critical=True)
2025-11-04 12:46:50,182 - modules.permission_restart.core.permission_change_detector - DEBUG - [PERMISSION_RESTART] Event received: type=permissions.init perm=screen_capture old=not_determined new=granted session=app_startup_init source=app_startup_init (critical=True)
2025-11-04 12:46:50,182 - modules.permission_restart.core.permission_change_detector - INFO - [PERMISSION_RESTART] Critical permission granted: screen_capture (not_determined → granted)
2025-11-04 12:46:50,182 - integration.integrations.permission_restart_integration - INFO - [PERMISSION_RESTART] Initialized with current permissions: {'accessibility': 'not_determined', 'input_monitoring': 'not_determined', 'screen_capture': 'granted'}
2025-11-04 12:46:50,186 - modules.permissions.macos.accessibility_handler - WARNING - ⚠️ Quartz/AX API недоступен — считаем, что разрешение не выдано
2025-11-04 12:46:50,187 - modules.permissions.first_run.status_checker - DEBUG - ♿ Accessibility: NOT_DETERMINED or DENIED
2025-11-04 12:46:50,206 - modules.permissions.first_run.status_checker - DEBUG - ⌨️ Input Monitoring: IOHIDCheckAccess вернул False, выполняем tccutil check…
2025-11-04 12:46:50,219 - modules.permissions.first_run.status_checker - DEBUG - ⌨️ Input Monitoring: NOT_DETERMINED or DENIED
2025-11-04 12:46:50,237 - modules.permissions.macos.screen_capture_permission - INFO - ✅ Screen Capture permission granted
2025-11-04 12:46:50,237 - modules.permissions.first_run.status_checker - DEBUG - 📺 Screen Capture: GRANTED
2025-11-04 12:46:50,237 - integration.integrations.permission_restart_integration - DEBUG - [PERMISSION_RESTART] Readiness postponed, permissions not granted (accessibility=not_determined, input_monitoring=not_determined, screen_capture=granted)
2025-11-04 12:46:50,237 - integration.integrations.autostart_manager_integration - INFO - 📱 App startup - проверяем статус автозапуска
2025-11-04 12:46:50,237 - integration.core.event_bus - DEBUG - EventBus: dispatch 'autostart.status_checked' to 0 subscriber(s)
2025-11-04 12:46:50,237 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: autostart.status_checked
2025-11-04 12:46:50,237 - integration.integrations.autostart_manager_integration - WARNING - ⚠️ LaunchAgent автозапуск не найден
2025-11-04 12:46:50,261 - integration.core.simple_module_coordinator - INFO - ✅ UI-таймер запущен через rumps callback
2025-11-04 12:46:50,271 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: _apply_status_ui_sync ВЫЗВАН! status=TrayStatus.SLEEPING (type: <enum 'TrayStatus'>)
🎯 TRAY DEBUG: TrayIconGenerator.create_circle_icon status=TrayStatus.SLEEPING (type: <enum 'TrayStatus'>)
🎯 TRAY DEBUG: Available colors: {<TrayStatus.SLEEPING: 'sleeping'>: '#808080', <TrayStatus.LISTENING: 'listening'>: '#007AFF', <TrayStatus.PROCESSING: 'processing'>: '#FF9500'}
🎯 TRAY DEBUG: Selected color: #808080
🎯 TRAY DEBUG: create_icon_file вызван для status=TrayStatus.SLEEPING
🎯 TRAY DEBUG: generated color=#808080, PIL_available=True
2025-11-04 12:46:50,273 - integration.integrations.tray_controller_integration - INFO - ✅ Tray UI applied: sleeping -> sleeping