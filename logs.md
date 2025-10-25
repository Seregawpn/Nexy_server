/.venv/bin/activate
sergiyzasorin@Sergiys-MacBook-Air client % source /Users/sergiyzasorin/Development/Nexy/client/.
venv/bin/activate
(.venv) sergiyzasorin@Sergiys-MacBook-Air client % /Users/sergiyzasorin/Development/Nexy/client/
.venv/bin/python /Users/sergiyzasorin/Development/Nexy/client/main.py
✅ AppKit символы успешно скопированы в Foundation
2025-10-25 14:14:43,015 - asyncio - DEBUG - Using selector: KqueueSelector
2025-10-25 14:14:43,286 - integration.integrations.voice_recognition_integration - DEBUG - 🔍 [AUDIO_DEBUG] SpeechRecognizer импортирован успешно

============================================================
🚀 SIMPLE MODULE COORDINATOR - ИНИЦИАЛИЗАЦИЯ
============================================================
Инициализация core компонентов и интеграций...
============================================================

🔧 Создание core компонентов...
✅ Core компоненты созданы
2025-10-25 14:14:44,431 - asyncio - DEBUG - Using selector: KqueueSelector
🧵 Фоновый asyncio loop запущен для EventBus/интеграций
🔧 Создание интеграций...
2025-10-25 14:14:44,431 - integration.core.state_manager - DEBUG - StateManager: attached EventBus with loop=4409328704 running=True
2025-10-25 14:14:44,431 - integration.core.event_bus - DEBUG - EventBus: attached loop=4646522384 running=True
2025-10-25 14:14:44,481 - modules.updater.net - INFO - HTTP клиент инициализирован: timeout=30s, retries=3
2025-10-25 14:14:44,497 - integration.integrations.network_manager_integration - INFO - NetworkManagerIntegration created
2025-10-25 14:14:44,497 - integration.integrations.interrupt_management_integration - INFO - InterruptManagementIntegration created
2025-10-25 14:14:44,516 - integration.core.simple_module_coordinator - DEBUG - Voice config: simulate=False, language=en-US
2025-10-25 14:14:44,532 - integration.integrations.autostart_manager_integration - INFO - AutostartManagerIntegration created (мониторинг LaunchAgent)
2025-10-25 14:14:44,549 - modules.welcome_message.config.welcome_config - INFO - ✅ [WELCOME_CONFIG] Конфигурация загружена: enabled=True, text='Hi! Nexy is here. How can I he...'
2025-10-25 14:14:44,566 - integration.core.base_integration - INFO - voiceover_ducking integration created
✅ Интеграции созданы: instance_manager, hardware_id, first_run_permissions, tray, mode_management, input, updater, network, interrupt, voice_recognition, screenshot_capture, grpc, speech_playback, signals, autostart_manager, welcome_message, voiceover_ducking
🔧 Создание Workflows...
✅ ListeningWorkflow создан
✅ ProcessingWorkflow создан
✅ Все Workflows созданы успешно
✅ Интеграции созданы
🔧 Инициализация интеграций...
🔧 Инициализация instance_manager...
2025-10-25 14:14:44,566 - integration.core.event_bus - INFO - 📝 Подписка на событие: app.startup (приоритет: MEDIUM)
2025-10-25 14:14:44,566 - integration.core.event_bus - INFO - 📝 Подписка на событие: app.shutdown (приоритет: MEDIUM)
2025-10-25 14:14:44,566 - integration.core.event_bus - INFO - 📝 Подписка на событие: instance.check_request (приоритет: MEDIUM)
✅ InstanceManagerIntegration инициализирован
✅ instance_manager инициализирован
🔧 Инициализация hardware_id...
2025-10-25 14:14:44,566 - integration.integrations.hardware_id_integration - INFO - Initializing HardwareIdIntegration...
2025-10-25 14:14:44,567 - modules.hardware_id.core.config - INFO - ✅ Конфигурация hardware_id загружена из файла
2025-10-25 14:14:44,567 - integration.core.event_bus - INFO - 📝 Подписка на событие: app.startup (приоритет: HIGH)
2025-10-25 14:14:44,567 - integration.core.event_bus - INFO - 📝 Подписка на событие: app.shutdown (приоритет: MEDIUM)
2025-10-25 14:14:44,567 - integration.core.event_bus - INFO - 📝 Подписка на событие: hardware.id_request (приоритет: HIGH)
2025-10-25 14:14:44,567 - integration.core.event_bus - INFO - 📝 Подписка на событие: hardware.id_refresh (приоритет: MEDIUM)
2025-10-25 14:14:44,567 - integration.integrations.hardware_id_integration - INFO - HardwareIdIntegration initialized
✅ hardware_id инициализирован
🔧 Инициализация tray...
2025-10-25 14:14:44,567 - integration.integrations.tray_controller_integration - INFO - 🔧 Инициализация TrayControllerIntegration...
2025-10-25 14:14:44,568 - modules.tray_controller.core.tray_controller - INFO - 🔧 Инициализация TrayController
2025-10-25 14:14:44,568 - modules.tray_controller.core.tray_controller - INFO - ✅ TrayController инициализирован
2025-10-25 14:14:44,568 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: Подписываемся на app.mode_changed событие
2025-10-25 14:14:44,568 - integration.core.event_bus - INFO - 📝 Подписка на событие: app.mode_changed (приоритет: HIGH)
2025-10-25 14:14:44,569 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: Подписка на app.mode_changed успешна
2025-10-25 14:14:44,569 - integration.core.event_bus - INFO - 📝 Подписка на событие: app.startup (приоритет: HIGH)
2025-10-25 14:14:44,569 - integration.core.event_bus - INFO - 📝 Подписка на событие: app.shutdown (приоритет: HIGH)
2025-10-25 14:14:44,569 - integration.core.event_bus - INFO - 📝 Подписка на событие: voice.mic_opened (приоритет: HIGH)
2025-10-25 14:14:44,569 - integration.core.event_bus - INFO - 📝 Подписка на событие: voice.mic_closed (приоритет: HIGH)
2025-10-25 14:14:44,569 - integration.integrations.tray_controller_integration - INFO - ✅ Обработчики событий TrayControllerIntegration настроены
2025-10-25 14:14:44,569 - integration.integrations.tray_controller_integration - INFO - ✅ TrayControllerIntegration инициализирован
✅ tray инициализирован
🔧 Инициализация input...
2025-10-25 14:14:44,569 - integration.integrations.input_processing_integration - INFO - 🔧 Инициализация input_processing...
2025-10-25 14:14:44,573 - integration.integrations.input_processing_integration - INFO - ✅ QuartzKeyboardMonitor создан (тестирование отложено до start())
2025-10-25 14:14:44,573 - integration.integrations.input_processing_integration - INFO - 🔑 Регистрируем Quartz callback'и:
🔑 Регистрируем Quartz callback'и:
2025-10-25 14:14:44,573 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔑 QuartzMonitor: callback зарегистрирован для press
🔑 QuartzMonitor: callback зарегистрирован для press
2025-10-25 14:14:44,573 - integration.integrations.input_processing_integration - INFO - 🔑 ✅ PRESS callback зарегистрирован
🔑 ✅ PRESS callback зарегистрирован
2025-10-25 14:14:44,573 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔑 QuartzMonitor: callback зарегистрирован для short_press
🔑 QuartzMonitor: callback зарегистрирован для short_press
2025-10-25 14:14:44,573 - integration.integrations.input_processing_integration - INFO - 🔑 ✅ SHORT_PRESS callback зарегистрирован
🔑 ✅ SHORT_PRESS callback зарегистрирован
2025-10-25 14:14:44,573 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔑 QuartzMonitor: callback зарегистрирован для long_press
🔑 QuartzMonitor: callback зарегистрирован для long_press
2025-10-25 14:14:44,573 - integration.integrations.input_processing_integration - INFO - 🔑 ✅ LONG_PRESS callback зарегистрирован
🔑 ✅ LONG_PRESS callback зарегистрирован
2025-10-25 14:14:44,573 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔑 QuartzMonitor: callback зарегистрирован для release
🔑 QuartzMonitor: callback зарегистрирован для release
2025-10-25 14:14:44,573 - integration.integrations.input_processing_integration - INFO - 🔑 ✅ RELEASE callback зарегистрирован
🔑 ✅ RELEASE callback зарегистрирован
2025-10-25 14:14:44,573 - integration.integrations.input_processing_integration - INFO - ✅ KeyboardMonitor инициализирован
2025-10-25 14:14:44,573 - integration.core.event_bus - INFO - 📝 Подписка на событие: mode.switch (приоритет: HIGH)
2025-10-25 14:14:44,573 - integration.core.event_bus - INFO - 📝 Подписка на событие: voice.recognition_completed (приоритет: HIGH)
2025-10-25 14:14:44,573 - integration.core.event_bus - INFO - 📝 Подписка на событие: voice.recognition_failed (приоритет: HIGH)
2025-10-25 14:14:44,573 - integration.core.event_bus - INFO - 📝 Подписка на событие: voice.recognition_timeout (приоритет: HIGH)
2025-10-25 14:14:44,573 - integration.core.event_bus - INFO - 📝 Подписка на событие: grpc.request_completed (приоритет: HIGH)
2025-10-25 14:14:44,573 - integration.core.event_bus - INFO - 📝 Подписка на событие: grpc.request_failed (приоритет: HIGH)
2025-10-25 14:14:44,573 - integration.core.event_bus - INFO - 📝 Подписка на событие: playback.started (приоритет: MEDIUM)
2025-10-25 14:14:44,573 - integration.core.event_bus - INFO - 📝 Подписка на событие: playback.completed (приоритет: MEDIUM)
2025-10-25 14:14:44,573 - integration.core.event_bus - INFO - 📝 Подписка на событие: playback.failed (приоритет: MEDIUM)
2025-10-25 14:14:44,573 - integration.core.event_bus - INFO - 📝 Подписка на событие: playback.cancelled (приоритет: MEDIUM)
2025-10-25 14:14:44,573 - integration.core.event_bus - INFO - 📝 Подписка на событие: voice.mic_opened (приоритет: HIGH)
2025-10-25 14:14:44,573 - integration.core.event_bus - INFO - 📝 Подписка на событие: voice.mic_closed (приоритет: HIGH)
2025-10-25 14:14:44,573 - integration.integrations.input_processing_integration - INFO - ✅ input_processing инициализирован
✅ input инициализирован
🔧 Инициализация updater...
2025-10-25 14:14:44,573 - integration.integrations.updater_integration - INFO - 🔄 Инициализация UpdaterIntegration...
2025-10-25 14:14:44,573 - integration.core.event_bus - INFO - 📝 Подписка на событие: app.startup (приоритет: MEDIUM)
2025-10-25 14:14:44,573 - integration.core.event_bus - INFO - 📝 Подписка на событие: app.shutdown (приоритет: HIGH)
2025-10-25 14:14:44,573 - integration.core.event_bus - INFO - 📝 Подписка на событие: updater.check_manual (приоритет: HIGH)
2025-10-25 14:14:44,573 - integration.core.event_bus - INFO - 📝 Подписка на событие: app.mode_changed (приоритет: LOW)
2025-10-25 14:14:44,573 - integration.integrations.updater_integration - INFO - ✅ UpdaterIntegration инициализирован
✅ updater инициализирован
🔧 Инициализация network...
2025-10-25 14:14:44,573 - integration.integrations.network_manager_integration - INFO - Initializing NetworkManagerIntegration...
2025-10-25 14:14:44,573 - modules.network_manager.core.network_manager - DEBUG - Added network callback: _on_network_event
2025-10-25 14:14:44,573 - modules.network_manager.core.network_manager - INFO - Initializing NetworkManager...
2025-10-25 14:14:59,578 - integration.integrations.network_manager_integration - DEBUG - Network event received: network.status_changed
2025-10-25 14:14:59,578 - integration.core.event_bus - DEBUG - EventBus: dispatch 'network.status_changed' to 0 subscriber(s)
2025-10-25 14:14:59,578 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: network.status_changed
2025-10-25 14:14:59,578 - integration.core.event_bus - DEBUG - EventBus: dispatch 'tray.update_tooltip' to 0 subscriber(s)
2025-10-25 14:14:59,578 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: tray.update_tooltip
2025-10-25 14:14:59,578 - integration.core.event_bus - DEBUG - EventBus: dispatch 'network.connection_lost' to 0 subscriber(s)
2025-10-25 14:14:59,578 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: network.connection_lost
2025-10-25 14:14:59,578 - modules.network_manager.core.network_manager - INFO - Network status changed: unknown -> disconnected
2025-10-25 14:14:59,578 - modules.network_manager.core.network_manager - INFO - NetworkManager initialized successfully
2025-10-25 14:14:59,578 - integration.core.event_bus - INFO - 📝 Подписка на событие: app.startup (приоритет: MEDIUM)
2025-10-25 14:14:59,578 - integration.core.event_bus - INFO - 📝 Подписка на событие: app.shutdown (приоритет: MEDIUM)
2025-10-25 14:14:59,578 - integration.integrations.network_manager_integration - INFO - NetworkManagerIntegration initialized successfully
✅ network инициализирован
🔧 Инициализация interrupt...
2025-10-25 14:14:59,578 - integration.integrations.interrupt_management_integration - INFO - Initializing InterruptManagementIntegration...
2025-10-25 14:14:59,579 - modules.interrupt_management.core.interrupt_coordinator - INFO - ✅ Координатор прерываний инициализирован
2025-10-25 14:14:59,579 - modules.interrupt_management.core.interrupt_coordinator - DEBUG - 📝 Зарегистрирован обработчик для speech_stop
2025-10-25 14:14:59,579 - modules.interrupt_management.core.interrupt_coordinator - DEBUG - 📝 Зарегистрирован обработчик для speech_pause
2025-10-25 14:14:59,579 - modules.interrupt_management.core.interrupt_coordinator - DEBUG - 📝 Зарегистрирован обработчик для recording_stop
2025-10-25 14:14:59,579 - modules.interrupt_management.core.interrupt_coordinator - DEBUG - 📝 Зарегистрирован обработчик для session_clear
2025-10-25 14:14:59,579 - integration.integrations.interrupt_management_integration - INFO - Interrupt handlers registered successfully
2025-10-25 14:14:59,579 - integration.core.event_bus - INFO - 📝 Подписка на событие: app.startup (приоритет: MEDIUM)
2025-10-25 14:14:59,579 - integration.core.event_bus - INFO - 📝 Подписка на событие: app.shutdown (приоритет: HIGH)
2025-10-25 14:14:59,579 - integration.core.event_bus - INFO - 📝 Подписка на событие: app.state_changed (приоритет: HIGH)
2025-10-25 14:14:59,579 - integration.core.event_bus - INFO - 📝 Подписка на событие: interrupt.request (приоритет: HIGH)
2025-10-25 14:14:59,579 - integration.core.event_bus - INFO - 📝 Подписка на событие: interrupt.cancel (приоритет: HIGH)
2025-10-25 14:14:59,579 - integration.integrations.interrupt_management_integration - INFO - InterruptManagementIntegration initialized successfully
✅ interrupt инициализирован
🔧 Инициализация screenshot_capture...
2025-10-25 14:14:59,585 - modules.screenshot_capture.core.screenshot_capture - INFO - ✅ Core Graphics bridge инициализирован
2025-10-25 14:14:59,585 - integration.integrations.screenshot_capture_integration - INFO - ScreenshotCaptureIntegration: capture module ready
2025-10-25 14:14:59,585 - integration.core.event_bus - INFO - 📝 Подписка на событие: app.mode_changed (приоритет: HIGH)
2025-10-25 14:14:59,585 - integration.core.event_bus - INFO - 📝 Подписка на событие: voice.recording_stop (приоритет: HIGH)
2025-10-25 14:14:59,585 - integration.integrations.screenshot_capture_integration - INFO - 🔧 ScreenshotCapture: Подписки настроены - app.mode_changed, voice.recording_stop
2025-10-25 14:14:59,585 - integration.core.event_bus - INFO - 📝 Подписка на событие: permissions.status_checked (приоритет: MEDIUM)
2025-10-25 14:14:59,585 - integration.core.event_bus - INFO - 📝 Подписка на событие: permissions.changed (приоритет: MEDIUM)
2025-10-25 14:14:59,585 - integration.core.event_bus - INFO - 📝 Подписка на событие: permissions.requested (приоритет: LOW)
2025-10-25 14:14:59,585 - integration.core.event_bus - INFO - 📝 Подписка на событие: permissions.integration_ready (приоритет: MEDIUM)
2025-10-25 14:14:59,585 - integration.integrations.screenshot_capture_integration - INFO - ScreenshotCaptureIntegration initialized
2025-10-25 14:14:59,585 - integration.integrations.screenshot_capture_integration - INFO - 📸 [SCREENSHOT_INTEGRATION] Разрешения будут запрошены через PermissionsIntegration
✅ screenshot_capture инициализирован
🔧 Инициализация voice_recognition...
2025-10-25 14:14:59,585 - integration.core.event_bus - INFO - 📝 Подписка на событие: voice.recording_start (приоритет: HIGH)
2025-10-25 14:14:59,585 - integration.core.event_bus - INFO - 📝 Подписка на событие: voice.recording_stop (приоритет: HIGH)
2025-10-25 14:14:59,585 - integration.core.event_bus - INFO - 📝 Подписка на событие: keyboard.short_press (приоритет: CRITICAL)
2025-10-25 14:14:59,585 - integration.core.event_bus - INFO - 📝 Подписка на событие: app.mode_changed (приоритет: MEDIUM)
2025-10-25 14:14:59,585 - integration.integrations.voice_recognition_integration - DEBUG - 🔍 [AUDIO_DEBUG] Условия создания SpeechRecognizer: simulate=False, _REAL_VOICE_AVAILABLE=True
2025-10-25 14:14:59,585 - modules.voice_recognition.core.audio_device_monitor - INFO - 🎤 Текущий input device: 0
2025-10-25 14:14:59,585 - modules.voice_recognition.core.audio_device_monitor - INFO - 🔧 AudioDeviceMonitor создан (интервал: 0.5с)
2025-10-25 14:14:59,585 - modules.voice_recognition.core.audio_device_monitor - DEBUG - 🔔 Callback смены устройства установлен
2025-10-25 14:14:59,585 - integration.integrations.voice_recognition_integration - WARNING - ⚠️ [AUDIO_DEBUG] SpeechRecognizer не поддерживает set_event_bus
2025-10-25 14:14:59,585 - modules.voice_recognition.core.speech_recognizer - DEBUG - 🔧 Event loop установлен в SpeechRecognizer: <_UnixSelectorEventLoop running=True closed=False debug=False>
2025-10-25 14:14:59,748 - modules.voice_recognition.core.speech_recognizer - INFO - 🔧 Настраиваем микрофон для фонового шума...
tray_controller.core.tray_controller - INFO - ℹ️ Для отображения иконки запустите app.run() в главном потоке
2025-10-25 14:15:01,734 - integration.integrations.tray_controller_integration - INFO - 🔄 Синхронизация с режимом приложения: sleeping → sleeping
2025-10-25 14:15:01,734 - integration.core.event_bus - DEBUG - EventBus: dispatch 'tray.integration_ready' to 0 subscriber(s)
2025-10-25 14:15:01,734 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: tray.integration_ready
2025-10-25 14:15:01,734 - integration.integrations.tray_controller_integration - INFO - ✅ TrayControllerIntegration запущен
✅ tray запущен
🚀 Запуск mode_management...
2025-10-25 14:15:01,734 - integration.integrations.mode_management_integration - INFO - ModeManagementIntegration started
✅ mode_management запущен
🚀 Запуск input...
🔧 DEBUG: InputProcessingIntegration.start() вызван
2025-10-25 14:15:01,734 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - QuartzMonitor: установлен event loop для async-колбэков
2025-10-25 14:15:01,734 - integration.integrations.input_processing_integration - INFO - 🔧 Тестируем QuartzKeyboardMonitor после инициализации...
2025-10-25 14:15:01,734 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔐 Проверяем разрешения для Quartz Event Tap...
🔐 Проверяем разрешения для Quartz Event Tap...
2025-10-25 14:15:01,791 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔐 Accessibility permission: True
🔐 Accessibility permission: True
2025-10-25 14:15:01,824 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - QuartzMonitor: CGEventTap включен для keycode=49
2025-10-25 14:15:01,824 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🎹 Quartz-монитор клавиатуры запущен
2025-10-25 14:15:01,824 - integration.integrations.input_processing_integration - INFO - ✅ QuartzKeyboardMonitor успешно запущен
🔧 DEBUG: KeyboardMonitor статус: {'is_monitoring': True, 'key_pressed': False, 'keyboard_available': True, 'fallback_mode': False, 'config': {'key': 'space', 'short_press_threshold': 0.1, 'long_press_threshold': 0.6}, 'callbacks_registered': 4, 'backend': 'quartz'}
🔧 DEBUG: Callbacks зарегистрированы: 4
🔧 DEBUG: Мониторинг активен: True
⌨️ DEBUG: НАЖМИТЕ ПРОБЕЛ СЕЙЧАС ДЛЯ ТЕСТИРОВАНИЯ!
2025-10-25 14:15:01,824 - integration.integrations.input_processing_integration - INFO - ✅ input_processing запущен
✅ input запущен
🚀 Запуск voice_recognition...
2025-10-25 14:15:01,824 - integration.integrations.voice_recognition_integration - DEBUG - 🔍 Microphone permission check relies on macOS defaults
2025-10-25 14:15:01,824 - integration.integrations.voice_recognition_integration - INFO - VoiceRecognitionIntegration started
✅ voice_recognition запущен
🚀 Запуск network...
2025-10-25 14:15:01,824 - integration.integrations.network_manager_integration - INFO - Starting NetworkManagerIntegration...
2025-10-25 14:15:01,824 - modules.network_manager.core.network_manager - INFO - Starting NetworkManager monitoring...
2025-10-25 14:15:01,824 - modules.network_manager.core.network_manager - INFO - NetworkManager monitoring started
2025-10-25 14:15:01,824 - integration.integrations.network_manager_integration - INFO - NetworkManagerIntegration started successfully
✅ network запущен
🚀 Запуск interrupt...
2025-10-25 14:15:01,824 - integration.integrations.interrupt_management_integration - INFO - Starting InterruptManagementIntegration...
2025-10-25 14:15:01,824 - integration.integrations.interrupt_management_integration - INFO - InterruptManagementIntegration started successfully
✅ interrupt запущен
🚀 Запуск screenshot_capture...
2025-10-25 14:15:01,824 - integration.integrations.screenshot_capture_integration - INFO - ScreenshotCaptureIntegration started
✅ screenshot_capture запущен
🚀 Запуск grpc...
2025-10-25 14:15:01,824 - integration.integrations.grpc_client_integration - INFO - GrpcClientIntegration started (lazy connect)
✅ grpc запущен
🚀 Запуск speech_playback...
✅ speech_playback запущен
🚀 Запуск updater...
2025-10-25 14:15:01,824 - integration.integrations.updater_integration - INFO - 🚀 Запуск UpdaterIntegration...
2025-10-25 14:15:01,824 - integration.integrations.updater_integration - INFO - 🔍 Проверка обновлений при запуске...
2025-10-25 14:15:01,824 - modules.updater.net - INFO - Запрос манифеста: http://20.151.51.172:8081/appcast.xml
2025-10-25 14:15:01,825 - urllib3.connectionpool - DEBUG - Starting new HTTP connection (1): 20.151.51.172:8081
2025-10-25 14:15:01,857 - urllib3.connectionpool - DEBUG - http://20.151.51.172:8081 "GET /appcast.xml HTTP/1.1" 200 0
2025-10-25 14:15:01,858 - modules.updater.net - INFO - XML манифест распарсен: версия 1.0.1, build 1001
2025-10-25 14:15:01,858 - modules.updater.net - INFO - Манифест получен: версия 1.0.1
2025-10-25 14:15:01,860 - modules.updater.updater - INFO - Найдено обновление до версии 1.0.1
2025-10-25 14:15:01,860 - modules.updater.updater - INFO - Скачивание dmg...
2025-10-25 14:15:01,860 - modules.updater.net - INFO - Скачивание файла: https://github.com/Seregawpn/Nexy_production/releases/download/Update/Nexy.dmg -> /var/folders/ys/xlx_chms3hqcs1lfyq37395c0000gn/T/tmpzdwqmy42.dmg
2025-10-25 14:15:01,860 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): github.com:443
2025-10-25 14:15:02,162 - urllib3.connectionpool - DEBUG - https://github.com:443 "GET /Seregawpn/Nexy_production/releases/download/Update/Nexy.dmg HTTP/1.1" 302 0
2025-10-25 14:15:02,164 - urllib3.util.retry - DEBUG - Incremented Retry for (url='https://github.com/Seregawpn/Nexy_production/releases/download/Update/Nexy.dmg'): Retry(total=2, connect=None, read=None, redirect=4, status=None)
2025-10-25 14:15:02,164 - urllib3.poolmanager - INFO - Redirecting https://github.com/Seregawpn/Nexy_production/releases/download/Update/Nexy.dmg -> https://release-assets.githubusercontent.com/github-production-release-asset/1082905055/8cc4485f-befe-4285-9ec9-ac09f420e989?sp=r&sv=2018-11-09&sr=b&spr=https&se=2025-10-25T19%3A05%3A24Z&rscd=attachment%3B+filename%3DNexy.dmg&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2025-10-25T18%3A05%3A18Z&ske=2025-10-25T19%3A05%3A24Z&sks=b&skv=2018-11-09&sig=AmooRPAhtWjuxS1B%2Bmv3duxoQ8YVaGCAfmChzdR23cs%3D&jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmVsZWFzZS1hc3NldHMuZ2l0aHVidXNlcmNvbnRlbnQuY29tIiwia2V5Ijoia2V5MSIsImV4cCI6MTc2MTQxNzkwMiwibmJmIjoxNzYxNDE2MTAyLCJwYXRoIjoicmVsZWFzZWFzc2V0cHJvZHVjdGlvbi5ibG9iLmNvcmUud2luZG93cy5uZXQifQ.MOO_UB-2kEhlQnZiznUhkcE4TvZEaEqDtZ4t04aFDDw&response-content-disposition=attachment%3B%20filename%3DNexy.dmg&response-content-type=application%2Foctet-stream
2025-10-25 14:15:02,166 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): release-assets.githubusercontent.com:443
2025-10-25 14:15:02,240 - urllib3.connectionpool - DEBUG - https://release-assets.githubusercontent.com:443 "GET /github-production-release-asset/1082905055/8cc4485f-befe-4285-9ec9-ac09f420e989?sp=r&sv=2018-11-09&sr=b&spr=https&se=2025-10-25T19%3A05%3A24Z&rscd=attachment%3B+filename%3DNexy.dmg&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2025-10-25T18%3A05%3A18Z&ske=2025-10-25T19%3A05%3A24Z&sks=b&skv=2018-11-09&sig=AmooRPAhtWjuxS1B%2Bmv3duxoQ8YVaGCAfmChzdR23cs%3D&jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmVsZWFzZS1hc3NldHMuZ2l0aHVidXNlcmNvbnRlbnQuY29tIiwia2V5Ijoia2V5MSIsImV4cCI6MTc2MTQxNzkwMiwibmJmIjoxNzYxNDE2MTAyLCJwYXRoIjoicmVsZWFzZWFzc2V0cHJvZHVjdGlvbi5ibG9iLmNvcmUud2luZG93cy5uZXQifQ.MOO_UB-2kEhlQnZiznUhkcE4TvZEaEqDtZ4t04aFDDw&response-content-disposition=attachment%3B%20filename%3DNexy.dmg&response-content-type=application%2Foctet-stream HTTP/1.1" 200 97357144
2025-10-25 14:15:05,723 - modules.updater.net - INFO - Скачано: 10.0 MB
2025-10-25 14:15:09,258 - modules.updater.net - INFO - Скачано: 20.0 MB
2025-10-25 14:15:12,741 - modules.updater.net - INFO - Скачано: 30.0 MB
2025-10-25 14:15:17,735 - modules.updater.net - INFO - Скачано: 40.0 MB
2025-10-25 14:15:22,152 - modules.updater.net - INFO - Скачано: 50.0 MB
BUG - EventBus: awaiting async callback inline for 'screenshot.captured': <bound method GrpcClientIntegration._on_screenshot_captured of <integration.integrations.grpc_client_integration.GrpcClientIntegration object at 0x114c17cb0>>
2025-10-25 14:15:37,851 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'screenshot.captured': <bound method ProcessingWorkflow._on_screenshot_captured of <integration.workflows.processing_workflow.ProcessingWorkflow object at 0x114f69550>>
2025-10-25 14:15:37,851 - integration.workflows.processing_workflow - INFO - 📸 ProcessingWorkflow: скриншот захвачен, path=None
2025-10-25 14:15:37,851 - integration.workflows.processing_workflow - INFO - ⚙️ ProcessingWorkflow: переход capturing → sending_grpc
2025-10-25 14:15:37,851 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'screenshot.captured': <bound method SimpleModuleCoordinator._on_screenshot_captured of <integration.core.simple_module_coordinator.SimpleModuleCoordinator object at 0x114c14c20>>
🖼️ Screenshot captured: /var/folders/ys/xlx_chms3hqcs1lfyq37395c0000gn/T/nexy_screenshots/shot_83059107.jpg (1383x900, 255270 bytes), session=None
2025-10-25 14:15:37,851 - integration.core.simple_module_coordinator - INFO - Screenshot captured: path=/var/folders/ys/xlx_chms3hqcs1lfyq37395c0000gn/T/nexy_screenshots/shot_83059107.jpg, size=255270, dims=1383x900, session=None
2025-10-25 14:15:37,851 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: screenshot.captured
2025-10-25 14:15:37,851 - integration.integrations.screenshot_capture_integration - INFO - Screenshot captured: /var/folders/ys/xlx_chms3hqcs1lfyq37395c0000gn/T/nexy_screenshots/shot_83059107.jpg
2025-10-25 14:15:37,851 - integration.workflows.processing_workflow - DEBUG - ⚙️ ProcessingWorkflow: мониторинг этапа capturing отменен
2025-10-25 14:15:38,299 - modules.welcome_message.core.welcome_player - INFO - 🔍 [WELCOME_PLAYER] audio_data is None: False
2025-10-25 14:15:38,300 - modules.welcome_message.core.welcome_player - INFO - 🔍 [WELCOME_PLAYER] audio_data.shape=(252000,), dtype=int16
2025-10-25 14:15:38,300 - modules.welcome_message.core.welcome_player - INFO - 🔍 [WELCOME_PLAYER] sample_rate=48000, channels=1, duration=5.25s
2025-10-25 14:15:38,300 - modules.welcome_message.core.welcome_player - INFO - ✅ [WELCOME_PLAYER] Серверное аудио успешно подготовлено
2025-10-25 14:15:38,300 - modules.welcome_message.core.welcome_player - INFO - 🔍 [WELCOME_PLAYER] Серверное аудио получено: success=True, error=None
2025-10-25 14:15:38,300 - modules.welcome_message.core.welcome_player - INFO - ✅ [WELCOME_PLAYER] Серверное приветствие воспроизведено успешно
2025-10-25 14:15:38,300 - modules.welcome_message.core.welcome_player - INFO - 🔍 [WELCOME_PLAYER] Вызываю _on_completed callback
2025-10-25 14:15:38,300 - integration.integrations.welcome_message_integration - INFO - 🎵 [WELCOME_INTEGRATION] Приветствие завершено: server, success=True
2025-10-25 14:15:38,300 - integration.integrations.welcome_message_integration - INFO - 🔍 [WELCOME_INTEGRATION] result.success=True, result.method=server
2025-10-25 14:15:38,300 - integration.integrations.welcome_message_integration - INFO - 🔍 [WELCOME_INTEGRATION] result.error=None
2025-10-25 14:15:38,300 - integration.integrations.welcome_message_integration - INFO - 🔍 [WELCOME_INTEGRATION] result.metadata={'sample_rate': 48000, 'channels': 1, 'samples': 252000, 'frames': 252000, 'method': 'server', 'duration_sec': 5.25}
2025-10-25 14:15:38,300 - integration.integrations.welcome_message_integration - INFO - 🔍 [WELCOME_INTEGRATION] audio_data is None: False
2025-10-25 14:15:38,300 - integration.integrations.welcome_message_integration - INFO - 🔍 [WELCOME_INTEGRATION] audio_data.shape=(252000,), dtype=int16
2025-10-25 14:15:38,300 - integration.integrations.welcome_message_integration - INFO - ✅ [WELCOME_INTEGRATION] Приветствие воспроизведено: server, 5.2s
2025-10-25 14:15:38,300 - integration.integrations.welcome_message_integration - INFO - 🎙️ [WELCOME_INTEGRATION] Приветствие завершено. Разрешения обрабатываются через PermissionsIntegration
2025-10-25 14:15:38,300 - integration.core.event_bus - DEBUG - EventBus: dispatch 'welcome.completed' to 0 subscriber(s)
2025-10-25 14:15:38,300 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: welcome.completed
2025-10-25 14:15:38,300 - integration.integrations.welcome_message_integration - INFO - 🎵 [WELCOME_INTEGRATION] Отправляю аудио в SpeechPlaybackIntegration: 252000 сэмплов
2025-10-25 14:15:38,300 - integration.integrations.welcome_message_integration - INFO - 🔍 [WELCOME_INTEGRATION] Формат данных: dtype=int16, shape=(252000,)
2025-10-25 14:15:38,302 - integration.integrations.welcome_message_integration - INFO - 🔍 [WELCOME_INTEGRATION] Диапазон: min=-25589, max=24578
2025-10-25 14:15:38,302 - integration.core.event_bus - DEBUG - EventBus: dispatch 'playback.raw_audio' to 1 subscriber(s)
2025-10-25 14:15:38,302 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'playback.raw_audio': <bound method SpeechPlaybackIntegration._on_raw_audio of <integration.integrations.speech_playback_integration.SpeechPlaybackIntegration object at 0x114f68050>>
2025-10-25 14:15:38,302 - integration.integrations.speech_playback_integration - INFO - 🔔 playback.raw_audio: pattern=welcome_message, dtype=int16, shape=(252000,), sr=48000, ch=1, prio=5
2025-10-25 14:15:38,302 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] sd.default.device = [0, 1]
2025-10-25 14:15:38,302 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] output_device ID = 1
2025-10-25 14:15:38,302 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] device_info = {'name': 'Sergiy’s AirPods', 'index': 1, 'hostapi': 0, 'max_input_channels': 0, 'max_output_channels': 2, 'default_low_input_latency': 0.01, 'default_low_output_latency': 0.16133333333333333, 'default_high_input_latency': 0.1, 'default_high_output_latency': 0.17066666666666666, 'default_samplerate': 48000.0}
2025-10-25 14:15:38,302 - modules.speech_playback.core.player - INFO - 🎛 Обновляем channels плеера: 1 → 2 (device=Sergiy’s AirPods)
2025-10-25 14:15:38,303 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] sd.default.device = [0, 1]
2025-10-25 14:15:38,303 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] output_device ID = 1
2025-10-25 14:15:38,303 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] device_info = {'name': 'Sergiy’s AirPods', 'index': 1, 'hostapi': 0, 'max_input_channels': 0, 'max_output_channels': 2, 'default_low_input_latency': 0.01, 'default_low_output_latency': 0.16133333333333333, 'default_high_input_latency': 0.1, 'default_high_output_latency': 0.17066666666666666, 'default_samplerate': 48000.0}
2025-10-25 14:15:38,303 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Создаём поток для устройства: Sergiy’s AirPods (ID=1)
2025-10-25 14:15:38,306 - modules.speech_playback.core.player - INFO - 🔧 Аудио поток создан (device: Sergiy’s AirPods, ID=1, channels: 2)
2025-10-25 14:15:38,306 - modules.speech_playback.core.player - DEBUG - 💡 Поток будет стартован при появлении первого чанка (lazy start)
2025-10-25 14:15:38,306 - modules.speech_playback.core.player - INFO - 🔄 Playback loop запущен
2025-10-25 14:15:38,306 - modules.speech_playback.core.player - INFO - 🎵 Воспроизведение запущено
2025-10-25 14:15:38,306 - integration.core.event_bus - DEBUG - EventBus: dispatch 'playback.started' to 2 subscriber(s)
2025-10-25 14:15:38,307 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'playback.started': <bound method ProcessingWorkflow._on_playback_started of <integration.workflows.processing_workflow.ProcessingWorkflow object at 0x114f69550>>
2025-10-25 14:15:38,307 - integration.workflows.processing_workflow - INFO - 🎵 ProcessingWorkflow: воспроизведение приветствия началось
2025-10-25 14:15:38,307 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'playback.started': <bound method InputProcessingIntegration._on_playback_started of <integration.integrations.input_processing_integration.InputProcessingIntegration object at 0x114c163c0>>
2025-10-25 14:15:38,307 - integration.integrations.input_processing_integration - DEBUG - PLAYBACK: started (session=raw:welcome_message:1761416138302)
2025-10-25 14:15:38,307 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: playback.started
2025-10-25 14:15:38,307 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Новая сессия или первый запуск (session=None, started=False)
2025-10-25 14:15:38,307 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Проверка смены устройства...
2025-10-25 14:15:38,307 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] sd.default.device = [0, 1]
2025-10-25 14:15:38,307 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] output_device ID = 1
2025-10-25 14:15:38,307 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] device_info = {'name': 'Sergiy’s AirPods', 'index': 1, 'hostapi': 0, 'max_input_channels': 0, 'max_output_channels': 2, 'default_low_input_latency': 0.01, 'default_low_output_latency': 0.16133333333333333, 'default_high_input_latency': 0.1, 'default_high_output_latency': 0.17066666666666666, 'default_samplerate': 48000.0}
2025-10-25 14:15:38,307 - modules.speech_playback.core.player - INFO - 🔊 [OUTPUT] Начальное устройство: "Sergiy’s AirPods"
2025-10-25 14:15:38,307 - modules.speech_playback.core.player - INFO - 🔄 [OUTPUT] Устройство изменилось - пересоздаём поток
2025-10-25 14:15:38,307 - modules.speech_playback.core.player - DEBUG - 🔄 [OUTPUT] Останавливаем старый поток
2025-10-25 14:15:38,308 - modules.speech_playback.core.player - INFO - 🛑 Аудио поток остановлен
2025-10-25 14:15:38,308 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] sd.default.device = [0, 1]
2025-10-25 14:15:38,308 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] output_device ID = 1
2025-10-25 14:15:38,308 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] device_info = {'name': 'Sergiy’s AirPods', 'index': 1, 'hostapi': 0, 'max_input_channels': 0, 'max_output_channels': 2, 'default_low_input_latency': 0.01, 'default_low_output_latency': 0.16133333333333333, 'default_high_input_latency': 0.1, 'default_high_output_latency': 0.17066666666666666, 'default_samplerate': 48000.0}
2025-10-25 14:15:38,308 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Текущее OUTPUT устройство ID: 1
2025-10-25 14:15:38,308 - modules.speech_playback.core.player - DEBUG - 🔄 [OUTPUT] Создаём новый поток для нового устройства
2025-10-25 14:15:38,308 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] sd.default.device = [0, 1]
2025-10-25 14:15:38,308 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] output_device ID = 1
2025-10-25 14:15:38,308 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] device_info = {'name': 'Sergiy’s AirPods', 'index': 1, 'hostapi': 0, 'max_input_channels': 0, 'max_output_channels': 2, 'default_low_input_latency': 0.01, 'default_low_output_latency': 0.16133333333333333, 'default_high_input_latency': 0.1, 'default_high_output_latency': 0.17066666666666666, 'default_samplerate': 48000.0}
2025-10-25 14:15:38,308 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] sd.default.device = [0, 1]
2025-10-25 14:15:38,308 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] output_device ID = 1
2025-10-25 14:15:38,308 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] device_info = {'name': 'Sergiy’s AirPods', 'index': 1, 'hostapi': 0, 'max_input_channels': 0, 'max_output_channels': 2, 'default_low_input_latency': 0.01, 'default_low_output_latency': 0.16133333333333333, 'default_high_input_latency': 0.1, 'default_high_output_latency': 0.17066666666666666, 'default_samplerate': 48000.0}
2025-10-25 14:15:38,308 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Создаём поток для устройства: Sergiy’s AirPods (ID=1)
2025-10-25 14:15:38,310 - modules.speech_playback.core.player - INFO - 🔧 Аудио поток создан (device: Sergiy’s AirPods, ID=1, channels: 2)
2025-10-25 14:15:38,310 - modules.speech_playback.core.player - DEBUG - 💡 Поток будет стартован при появлении первого чанка (lazy start)
2025-10-25 14:15:38,310 - modules.speech_playback.core.player - DEBUG - 🔄 Моно аудио будет воспроизведено на 2 каналах
2025-10-25 14:15:38,310 - modules.speech_playback.core.buffer - INFO - ✅ Чанк добавлен: chunk_0_1761416138310 (size: 252000, queue: 1)
2025-10-25 14:15:38,310 - modules.speech_playback.core.buffer - DEBUG - 🔍 Получен чанк: chunk_0_1761416138310
2025-10-25 14:15:38,310 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Стартуем поток: stream exists=True, started=False
2025-10-25 14:15:38,310 - modules.speech_playback.core.buffer - INFO - ✅ Чанк добавлен в буфер: chunk_0_1761416138310 (frames: 252000, buffer: 0 → 252000, ch=2)
2025-10-25 14:15:38,641 - modules.speech_playback.core.player - INFO - ▶️ Аудио поток стартован (lazy start)
2025-10-25 14:15:38,641 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Поток стартован: active=True
2025-10-25 14:15:38,641 - modules.speech_playback.core.player - INFO - ✅ Аудио данные добавлены: chunk_0_1761416138310 (size: 252000)
2025-10-25 14:15:38,641 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: playback.raw_audio
2025-10-25 14:15:38,641 - integration.integrations.welcome_message_integration - INFO - ✅ [WELCOME_INTEGRATION] Аудио отправлено в SpeechPlaybackIntegration
2025-10-25 14:15:38,641 - integration.integrations.welcome_message_integration - INFO - 🔄 [WELCOME_INTEGRATION] Ожидаю завершения воспроизведения...
2025-10-25 14:15:38,641 - integration.core.event_bus - INFO - 📝 Подписка на событие: playback.completed (приоритет: MEDIUM)
2025-10-25 14:15:38,641 - integration.integrations.speech_playback_integration - INFO - SpeechPlayback: запуск _finalize_on_silence для сессии raw:welcome_message:1761416138302, timeout=1.0s
2025-10-25 14:15:38,650 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 251488)
2025-10-25 14:15:38,650 - modules.speech_playback.core.player - INFO - 🎵 [CALLBACK #0] frames=512, data_shape=(512, 1), buffer_size=251488, channels=2
2025-10-25 14:15:38,660 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 250976)
2025-10-25 14:15:38,661 - modules.speech_playback.core.player - INFO - 🎵 [CALLBACK #1] frames=512, data_shape=(512, 1), buffer_size=250976, channels=2
2025-10-25 14:15:38,671 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 250464)
2025-10-25 14:15:38,671 - modules.speech_playback.core.player - INFO - 🎵 [CALLBACK #2] frames=512, data_shape=(512, 1), buffer_size=250464, channels=2
2025-10-25 14:15:38,681 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 249952)
2025-10-25 14:15:38,682 - modules.speech_playback.core.player - INFO - 🎵 [CALLBACK #3] frames=512, data_shape=(512, 1), buffer_size=249952, channels=2
2025-10-25 14:15:38,692 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 249440)
2025-10-25 14:15:38,692 - modules.speech_playback.core.player - INFO - 🎵 [CALLBACK #4] frames=512, data_shape=(512, 1), buffer_size=249440, channels=2
2025-10-25 14:15:38,703 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 248928)
2025-10-25 14:15:38,703 - modules.speech_playback.core.player - INFO - 🎵 [CALLBACK #5] frames=512, data_shape=(512, 1), buffer_size=248928, channels=2
2025-10-25 14:15:38,714 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 248416)
2025-10-25 14:15:38,714 - modules.speech_playback.core.player - INFO - 🎵 [CALLBACK #6] frames=512, data_shape=(512, 1), buffer_size=248416, channels=2
2025-10-25 14:15:38,724 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 247904)
2025-10-25 14:15:38,724 - modules.speech_playback.core.player - INFO - 🎵 [CALLBACK #7] frames=512, data_shape=(512, 1), buffer_size=247904, channels=2
2025-10-25 14:15:38,735 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 247392)
2025-10-25 14:15:38,735 - modules.speech_playback.core.player - INFO - 🎵 [CALLBACK #8] frames=512, data_shape=(512, 1), buffer_size=247392, channels=2
2025-10-25 14:15:38,746 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 246880)
2025-10-25 14:15:38,746 - modules.speech_playback.core.player - INFO - 🎵 [CALLBACK #9] frames=512, data_shape=(512, 1), buffer_size=246880, channels=2
2025-10-25 14:15:38,756 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 246368)
2025-10-25 14:15:38,757 - modules.speech_playback.core.player - INFO - 🔇 [CALLBACK] Дальнейшее логирование callback отключено (работает нормально)
2025-10-25 14:15:38,767 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 245856)
2025-10-25 14:15:38,778 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 245344)
2025-10-25 14:15:38,788 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 244832)
2025-10-25 14:15:38,799 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 244320)
2025-10-25 14:15:38,810 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 243808)
2025-10-25 14:15:38,820 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 243296)
2025-10-25 14:15:38,831 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 242784)
2025-10-25 14:15:38,842 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 242272)
2025-10-25 14:15:38,852 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 241760)
2025-10-25 14:15:38,863 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 241248)
2025-10-25 14:15:38,874 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 240736)
2025-10-25 14:15:38,884 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 240224)
2025-10-25 14:15:38,895 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 239712)
2025-10-25 14:15:38,906 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 239200)
2025-10-25 14:15:38,916 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 238688)
2025-10-25 14:15:38,927 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 238176)
2025-10-25 14:15:38,938 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 237664)
2025-10-25 14:15:38,948 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 237152)
2025-10-25 14:15:38,959 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 236640)
2025-10-25 14:15:38,970 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 236128)
2025-10-25 14:15:38,980 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 235616)
2025-10-25 14:15:38,991 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 235104)
2025-10-25 14:15:39,002 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 234592)
2025-10-25 14:15:39,012 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 234080)
2025-10-25 14:15:39,023 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 233568)
2025-10-25 14:15:39,033 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 233056)
2025-10-25 14:15:39,044 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 232544)
2025-10-25 14:15:39,055 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 232032)
2025-10-25 14:15:39,066 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 231520)
2025-10-25 14:15:39,076 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 231008)
2025-10-25 14:15:39,087 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 230496)
2025-10-25 14:15:39,097 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 229984)
2025-10-25 14:15:39,108 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 229472)
2025-10-25 14:15:39,119 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 228960)
2025-10-25 14:15:39,130 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 228448)
2025-10-25 14:15:39,140 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 227936)
2025-10-25 14:15:39,151 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 227424)
2025-10-25 14:15:39,162 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 226912)
2025-10-25 14:15:39,172 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 226400)
2025-10-25 14:15:39,183 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 225888)
2025-10-25 14:15:39,194 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 225376)
2025-10-25 14:15:39,204 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 224864)
2025-10-25 14:15:39,215 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 224352)
2025-10-25 14:15:39,226 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 223840)
2025-10-25 14:15:39,236 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 223328)
2025-10-25 14:15:39,247 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 222816)
2025-10-25 14:15:39,258 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 222304)
2025-10-25 14:15:39,268 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 221792)
2025-10-25 14:15:39,279 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 221280)
2025-10-25 14:15:39,290 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 220768)
2025-10-25 14:15:39,300 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 220256)
2025-10-25 14:15:39,311 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 219744)
2025-10-25 14:15:39,322 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 219232)
2025-10-25 14:15:39,332 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 218720)
2025-10-25 14:15:39,343 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 218208)
2025-10-25 14:15:39,353 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 217696)
2025-10-25 14:15:39,364 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 217184)
2025-10-25 14:15:39,375 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 216672)
2025-10-25 14:15:39,385 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 216160)
2025-10-25 14:15:39,396 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 215648)
2025-10-25 14:15:39,407 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 215136)
2025-10-25 14:15:39,418 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 214624)
2025-10-25 14:15:39,428 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 214112)
2025-10-25 14:15:39,439 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 213600)
2025-10-25 14:15:39,449 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 213088)
2025-10-25 14:15:39,460 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 212576)
2025-10-25 14:15:39,471 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 212064)
2025-10-25 14:15:39,481 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 211552)
2025-10-25 14:15:39,492 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 211040)
2025-10-25 14:15:39,503 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 210528)
2025-10-25 14:15:39,514 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 210016)
2025-10-25 14:15:39,524 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 209504)
2025-10-25 14:15:39,535 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 208992)
2025-10-25 14:15:39,546 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 208480)
2025-10-25 14:15:39,556 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 207968)
2025-10-25 14:15:39,567 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 207456)
2025-10-25 14:15:39,578 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 206944)
2025-10-25 14:15:39,588 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 206432)
2025-10-25 14:15:39,599 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 205920)
2025-10-25 14:15:39,610 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 205408)
2025-10-25 14:15:39,620 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 204896)
2025-10-25 14:15:39,631 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 204384)
2025-10-25 14:15:39,642 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 203872)
2025-10-25 14:15:39,642 - integration.integrations.speech_playback_integration - INFO - SpeechPlayback: _finalize_on_silence завершен для сессии raw:welcome_message:1761416138302
2025-10-25 14:15:39,642 - integration.integrations.speech_playback_integration - INFO - SpeechPlayback: _finalize_on_silence проверка для сессии raw:welcome_message:1761416138302: grpc_done=True, buf_empty=False, finalized=False
2025-10-25 14:15:39,642 - integration.integrations.speech_playback_integration - INFO - SpeechPlayback: _finalize_on_silence принудительное завершение для сессии raw:welcome_message:1761416138302 (gRPC завершен, но буфер не пуст)
2025-10-25 14:15:39,652 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 203360)
2025-10-25 14:15:39,663 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 202848)
2025-10-25 14:15:39,674 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 202336)
2025-10-25 14:15:39,684 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 201824)
2025-10-25 14:15:39,695 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 201312)
2025-10-25 14:15:39,706 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 200800)
2025-10-25 14:15:39,716 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 200288)
2025-10-25 14:15:39,727 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 199776)
2025-10-25 14:15:39,738 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 199264)
2025-10-25 14:15:39,748 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 198752)
2025-10-25 14:15:39,759 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 198240)
2025-10-25 14:15:39,769 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 197728)
2025-10-25 14:15:39,780 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 197216)
2025-10-25 14:15:39,791 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 196704)
2025-10-25 14:15:39,801 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 196192)
2025-10-25 14:15:39,812 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 195680)
2025-10-25 14:15:39,823 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 195168)
2025-10-25 14:15:39,833 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 194656)
2025-10-25 14:15:39,844 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 194144)
2025-10-25 14:15:39,855 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 193632)
2025-10-25 14:15:39,865 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 193120)
2025-10-25 14:15:39,876 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 192608)
2025-10-25 14:15:39,887 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 192096)
2025-10-25 14:15:39,898 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 191584)
2025-10-25 14:15:39,908 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 191072)
2025-10-25 14:15:39,919 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 190560)
2025-10-25 14:15:39,930 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 190048)
2025-10-25 14:15:39,940 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 189536)
2025-10-25 14:15:39,951 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 189024)
2025-10-25 14:15:39,962 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 188512)
2025-10-25 14:15:39,972 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 188000)
2025-10-25 14:15:39,983 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 187488)
2025-10-25 14:15:39,994 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 186976)
2025-10-25 14:15:40,004 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 186464)
2025-10-25 14:15:40,015 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 185952)
2025-10-25 14:15:40,026 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 185440)
2025-10-25 14:15:40,036 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 184928)
2025-10-25 14:15:40,047 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 184416)
2025-10-25 14:15:40,058 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 183904)
2025-10-25 14:15:40,068 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 183392)
2025-10-25 14:15:40,079 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 182880)
2025-10-25 14:15:40,090 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 182368)
2025-10-25 14:15:40,100 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 181856)
2025-10-25 14:15:40,111 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 181344)
2025-10-25 14:15:40,122 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 180832)
2025-10-25 14:15:40,132 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 180320)
2025-10-25 14:15:40,143 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 179808)
2025-10-25 14:15:40,143 - integration.integrations.speech_playback_integration - INFO - SpeechPlayback: ожидаем естественного завершения воспроизведения для raw:welcome_message:1761416138302
2025-10-25 14:15:40,154 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 179296)
2025-10-25 14:15:40,164 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 178784)
2025-10-25 14:15:40,175 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 178272)
2025-10-25 14:15:40,186 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 177760)
2025-10-25 14:15:40,196 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 177248)
2025-10-25 14:15:40,207 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 176736)
2025-10-25 14:15:40,218 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 176224)
2025-10-25 14:15:40,228 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 175712)
2025-10-25 14:15:40,239 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 175200)
2025-10-25 14:15:40,250 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 174688)
2025-10-25 14:15:40,260 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 174176)
2025-10-25 14:15:40,271 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 173664)
2025-10-25 14:15:40,281 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 173152)
2025-10-25 14:15:40,292 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 172640)
2025-10-25 14:15:40,303 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 172128)
2025-10-25 14:15:40,313 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 171616)
2025-10-25 14:15:40,324 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 171104)
2025-10-25 14:15:40,335 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 170592)
2025-10-25 14:15:40,346 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 170080)
2025-10-25 14:15:40,356 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 169568)
2025-10-25 14:15:40,367 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 169056)
2025-10-25 14:15:40,377 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 168544)
2025-10-25 14:15:40,388 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 168032)
2025-10-25 14:15:40,399 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 167520)
2025-10-25 14:15:40,409 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 167008)
2025-10-25 14:15:40,420 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 166496)
2025-10-25 14:15:40,431 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 165984)
2025-10-25 14:15:40,441 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 165472)
2025-10-25 14:15:40,452 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 164960)
2025-10-25 14:15:40,463 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 164448)
2025-10-25 14:15:40,474 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 163936)
2025-10-25 14:15:40,484 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 163424)
2025-10-25 14:15:40,495 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 162912)
2025-10-25 14:15:40,506 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 162400)
2025-10-25 14:15:40,516 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 161888)
2025-10-25 14:15:40,527 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 161376)
2025-10-25 14:15:40,538 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 160864)
2025-10-25 14:15:40,548 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 160352)
2025-10-25 14:15:40,559 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 159840)
2025-10-25 14:15:40,569 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 159328)
2025-10-25 14:15:40,580 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 158816)
2025-10-25 14:15:40,591 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 158304)
2025-10-25 14:15:40,601 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 157792)
2025-10-25 14:15:40,612 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 157280)
2025-10-25 14:15:40,623 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 156768)
2025-10-25 14:15:40,633 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 156256)
2025-10-25 14:15:40,644 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 155744)
2025-10-25 14:15:40,655 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 155232)
2025-10-25 14:15:40,665 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 154720)
2025-10-25 14:15:40,676 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 154208)
2025-10-25 14:15:40,687 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 153696)
2025-10-25 14:15:40,697 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 153184)
2025-10-25 14:15:40,708 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 152672)
2025-10-25 14:15:40,719 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 152160)
2025-10-25 14:15:40,730 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 151648)
2025-10-25 14:15:40,740 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 151136)
2025-10-25 14:15:40,751 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 150624)
2025-10-25 14:15:40,762 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 150112)
2025-10-25 14:15:40,772 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 149600)
2025-10-25 14:15:40,783 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 149088)
2025-10-25 14:15:40,794 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 148576)
2025-10-25 14:15:40,804 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 148064)
2025-10-25 14:15:40,815 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 147552)
2025-10-25 14:15:40,826 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 147040)
2025-10-25 14:15:40,836 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 146528)
2025-10-25 14:15:40,847 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 146016)
2025-10-25 14:15:40,858 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 145504)
2025-10-25 14:15:40,868 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 144992)
2025-10-25 14:15:40,879 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 144480)
2025-10-25 14:15:40,890 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 143968)
2025-10-25 14:15:40,900 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 143456)
2025-10-25 14:15:40,911 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 142944)
2025-10-25 14:15:40,922 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 142432)
2025-10-25 14:15:40,932 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 141920)
2025-10-25 14:15:40,943 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 141408)
2025-10-25 14:15:40,954 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 140896)
2025-10-25 14:15:40,964 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 140384)
2025-10-25 14:15:40,975 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 139872)
2025-10-25 14:15:40,985 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 139360)
2025-10-25 14:15:40,996 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 138848)
2025-10-25 14:15:41,007 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 138336)
2025-10-25 14:15:41,017 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 137824)
2025-10-25 14:15:41,028 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 137312)
2025-10-25 14:15:41,039 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 136800)
2025-10-25 14:15:41,049 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 136288)
2025-10-25 14:15:41,060 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 135776)
2025-10-25 14:15:41,071 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 135264)
2025-10-25 14:15:41,081 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 134752)
2025-10-25 14:15:41,092 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 134240)
2025-10-25 14:15:41,103 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 133728)
2025-10-25 14:15:41,114 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 133216)
2025-10-25 14:15:41,124 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 132704)
2025-10-25 14:15:41,135 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 132192)
2025-10-25 14:15:41,146 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 131680)
2025-10-25 14:15:41,156 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 131168)
2025-10-25 14:15:41,167 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 130656)
2025-10-25 14:15:41,178 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 130144)
2025-10-25 14:15:41,188 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 129632)
2025-10-25 14:15:41,199 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 129120)
2025-10-25 14:15:41,210 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 128608)
2025-10-25 14:15:41,220 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 128096)
2025-10-25 14:15:41,231 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 127584)
2025-10-25 14:15:41,242 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 127072)
2025-10-25 14:15:41,252 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 126560)
2025-10-25 14:15:41,263 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 126048)
2025-10-25 14:15:41,274 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 125536)
2025-10-25 14:15:41,284 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 125024)
2025-10-25 14:15:41,295 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 124512)
2025-10-25 14:15:41,306 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 124000)
2025-10-25 14:15:41,316 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 123488)
2025-10-25 14:15:41,327 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 122976)
2025-10-25 14:15:41,337 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 122464)
2025-10-25 14:15:41,348 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 121952)
2025-10-25 14:15:41,359 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 121440)
2025-10-25 14:15:41,369 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 120928)
2025-10-25 14:15:41,380 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 120416)
2025-10-25 14:15:41,391 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 119904)
2025-10-25 14:15:41,402 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 119392)
2025-10-25 14:15:41,412 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 118880)
2025-10-25 14:15:41,423 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 118368)
2025-10-25 14:15:41,433 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 117856)
2025-10-25 14:15:41,444 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 117344)
2025-10-25 14:15:41,455 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 116832)
2025-10-25 14:15:41,465 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 116320)
2025-10-25 14:15:41,476 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 115808)
2025-10-25 14:15:41,487 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 115296)
2025-10-25 14:15:41,498 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 114784)
2025-10-25 14:15:41,508 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 114272)
2025-10-25 14:15:41,519 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 113760)
2025-10-25 14:15:41,530 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 113248)
2025-10-25 14:15:41,540 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 112736)
2025-10-25 14:15:41,551 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 112224)
2025-10-25 14:15:41,562 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 111712)
2025-10-25 14:15:41,572 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 111200)
2025-10-25 14:15:41,583 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 110688)
2025-10-25 14:15:41,594 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 110176)
2025-10-25 14:15:41,604 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 109664)
2025-10-25 14:15:41,615 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 109152)
2025-10-25 14:15:41,626 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 108640)
2025-10-25 14:15:41,636 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 108128)
2025-10-25 14:15:41,647 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 107616)
2025-10-25 14:15:41,658 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 107104)
2025-10-25 14:15:41,668 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 106592)
2025-10-25 14:15:41,679 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 106080)
2025-10-25 14:15:41,690 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 105568)
2025-10-25 14:15:41,700 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 105056)
2025-10-25 14:15:41,711 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 104544)
2025-10-25 14:15:41,722 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 104032)
2025-10-25 14:15:41,732 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 103520)
2025-10-25 14:15:41,743 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 103008)
2025-10-25 14:15:41,754 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 102496)
2025-10-25 14:15:41,764 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 101984)
2025-10-25 14:15:41,775 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 101472)
2025-10-25 14:15:41,785 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 100960)
2025-10-25 14:15:41,796 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 100448)
2025-10-25 14:15:41,807 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 99936)
2025-10-25 14:15:41,817 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 99424)
2025-10-25 14:15:41,828 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 98912)
2025-10-25 14:15:41,839 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 98400)
2025-10-25 14:15:41,849 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 97888)
2025-10-25 14:15:41,860 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 97376)
2025-10-25 14:15:41,871 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 96864)
2025-10-25 14:15:41,881 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 96352)
2025-10-25 14:15:41,892 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 95840)
2025-10-25 14:15:41,903 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 95328)
2025-10-25 14:15:41,913 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 94816)
2025-10-25 14:15:41,924 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 94304)
2025-10-25 14:15:41,935 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 93792)
2025-10-25 14:15:41,946 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 93280)
2025-10-25 14:15:41,956 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 92768)
2025-10-25 14:15:41,967 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 92256)
2025-10-25 14:15:41,978 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 91744)
2025-10-25 14:15:41,988 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 91232)
2025-10-25 14:15:41,999 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 90720)
2025-10-25 14:15:42,010 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 90208)
2025-10-25 14:15:42,020 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 89696)
2025-10-25 14:15:42,031 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 89184)
2025-10-25 14:15:42,042 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 88672)
2025-10-25 14:15:42,052 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 88160)
2025-10-25 14:15:42,063 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 87648)
2025-10-25 14:15:42,074 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 87136)
2025-10-25 14:15:42,084 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 86624)
2025-10-25 14:15:42,095 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 86112)
2025-10-25 14:15:42,106 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 85600)
2025-10-25 14:15:42,116 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 85088)
2025-10-25 14:15:42,127 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 84576)
2025-10-25 14:15:42,137 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 84064)
2025-10-25 14:15:42,148 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 83552)
2025-10-25 14:15:42,159 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 83040)
2025-10-25 14:15:42,169 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 82528)
2025-10-25 14:15:42,180 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 82016)
2025-10-25 14:15:42,191 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 81504)
2025-10-25 14:15:42,201 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 80992)
2025-10-25 14:15:42,212 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 80480)
2025-10-25 14:15:42,223 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 79968)
2025-10-25 14:15:42,233 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 79456)
2025-10-25 14:15:42,244 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 78944)
2025-10-25 14:15:42,255 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 78432)
2025-10-25 14:15:42,265 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 77920)
2025-10-25 14:15:42,276 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 77408)
2025-10-25 14:15:42,287 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 76896)
2025-10-25 14:15:42,297 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 76384)
2025-10-25 14:15:42,308 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 75872)
2025-10-25 14:15:42,319 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 75360)
2025-10-25 14:15:42,330 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 74848)
2025-10-25 14:15:42,340 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 74336)
2025-10-25 14:15:42,351 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 73824)
2025-10-25 14:15:42,362 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 73312)
2025-10-25 14:15:42,372 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 72800)
2025-10-25 14:15:42,383 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 72288)
2025-10-25 14:15:42,394 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 71776)
2025-10-25 14:15:42,404 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 71264)
2025-10-25 14:15:42,415 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 70752)
2025-10-25 14:15:42,426 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 70240)
2025-10-25 14:15:42,436 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 69728)
2025-10-25 14:15:42,447 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 69216)
2025-10-25 14:15:42,458 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 68704)
2025-10-25 14:15:42,468 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 68192)
2025-10-25 14:15:42,479 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 67680)
2025-10-25 14:15:42,490 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 67168)
2025-10-25 14:15:42,500 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 66656)
2025-10-25 14:15:42,511 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 66144)
2025-10-25 14:15:42,522 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 65632)