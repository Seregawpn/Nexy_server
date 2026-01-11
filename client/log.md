ion...
2026-01-11 11:19:44,376 - integration.integrations.update_notification_integration - INFO - [UPDATE_NOTIFY] Интеграция готова к приему событий обновления
2026-01-11 11:19:44,376 - modules.grpc_client.core.connection_manager - INFO - 🔌 [DEBUG] Создание канала - use_ssl=True, ssl_verify=False
2026-01-11 11:19:44,376 - integration.core.base_integration - INFO - UpdateNotification started successfully
✅ update_notification запущен
🚀 Запуск updater...
2026-01-11 11:19:44,376 - modules.grpc_client.core.connection_manager - INFO - 🔌 [DEBUG] SSL enabled, ssl_verify=False
2026-01-11 11:19:44,376 - integration.integrations.updater_integration - INFO - ⏭️ Пропускаю запуск UpdaterIntegration - отключен
✅ updater запущен
🚀 Запуск welcome_message...
2026-01-11 11:19:44,377 - modules.grpc_client.core.connection_manager - WARNING - ⚠️ SSL verification disabled for 20.63.24.187:443 - используется insecure_channel для self-signed сертификата
2026-01-11 11:19:44,377 - integration.integrations.welcome_message_integration - INFO - ✅ [WELCOME_INTEGRATION] Запущен
✅ welcome_message запущен
🚀 Запуск voiceover_ducking...
2026-01-11 11:19:44,377 - modules.grpc_client.core.connection_manager - INFO - 🔌 [DEBUG] Using insecure_channel for self-signed certificate (as per server documentation)
2026-01-11 11:19:44,377 - integration.core.base_integration - INFO - Starting voiceover_ducking...
2026-01-11 11:19:44,377 - grpc._cython.cygrpc - DEBUG - [_cygrpc] Loaded running loop: id(loop)=4586276816
2026-01-11 11:19:44,377 - integration.integrations.voiceover_ducking_integration - INFO - 🚀 VoiceOverDuckingIntegration запущен
2026-01-11 11:19:44,377 - grpc._cython.cygrpc - DEBUG - Using AsyncIOEngine.POLLER as I/O engine
2026-01-11 11:19:44,378 - integration.core.base_integration - INFO - voiceover_ducking started successfully
✅ voiceover_ducking запущен
🚀 Запуск autostart_manager...
2026-01-11 11:19:44,378 - integration.integrations.autostart_manager_integration - INFO - 🚀 Запуск AutostartManagerIntegration
2026-01-11 11:19:44,379 - grpc._cython.cygrpc - DEBUG - [_cygrpc] Loaded running loop: id(loop)=4586276816
2026-01-11 11:19:44,379 - integration.core.event_bus - DEBUG - EventBus: dispatch 'autostart.status_checked' to 0 subscriber(s)
2026-01-11 11:19:44,381 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: autostart.status_checked
2026-01-11 11:19:44,381 - integration.integrations.autostart_manager_integration - WARNING - ⚠️ LaunchAgent автозапуск не найден
2026-01-11 11:19:44,381 - integration.integrations.autostart_manager_integration - INFO - ✅ AutostartManagerIntegration запущен
✅ autostart_manager запущен
🚀 Запуск Workflows...
🚀 Запуск workflow listening...
2026-01-11 11:19:44,381 - integration.workflows.listening_workflow - INFO - 🎤 ListeningWorkflow: готов к координации прослушивания
2026-01-11 11:19:44,381 - integration.workflows.base_workflow - INFO - 🚀 ListeningWorkflow: запущен
✅ Workflow listening запущен
🚀 Запуск workflow processing...
2026-01-11 11:19:44,381 - integration.workflows.processing_workflow - INFO - ⚙️ ProcessingWorkflow: готов к координации обработки
2026-01-11 11:19:44,381 - integration.workflows.base_workflow - INFO - 🚀 ProcessingWorkflow: запущен
✅ Workflow processing запущен
2026-01-11 11:19:44,381 - integration.core.event_bus - DEBUG - EventBus: dispatch 'app.startup' to 9 subscriber(s)
2026-01-11 11:19:44,381 - integration.core.event_bus - DEBUG - EventBus: scheduled async callback on main loop for 'app.startup': <bound method HardwareIdIntegration._on_app_startup of <integration.integrations.hardware_id_integration.HardwareIdIntegration object at 0x11154acf0>>
2026-01-11 11:19:44,382 - integration.core.event_bus - DEBUG - EventBus: scheduled async callback on main loop for 'app.startup': <bound method TrayControllerIntegration._on_app_startup of <integration.integrations.tray_controller_integration.TrayControllerIntegration object at 0x11154b230>>
2026-01-11 11:19:44,382 - integration.core.event_bus - DEBUG - EventBus: scheduled async callback on main loop for 'app.startup': <bound method SimpleModuleCoordinator._on_app_startup of <integration.core.simple_module_coordinator.SimpleModuleCoordinator object at 0x111549d30>>
2026-01-11 11:19:44,382 - integration.core.event_bus - DEBUG - EventBus: scheduled async callback on main loop for 'app.startup': <bound method InstanceManagerIntegration._on_app_startup of <integration.integrations.instance_manager_integration.InstanceManagerIntegration object at 0x11154a900>>
2026-01-11 11:19:44,382 - integration.core.event_bus - DEBUG - EventBus: scheduled async callback on main loop for 'app.startup': <bound method NetworkManagerIntegration._on_app_startup of <integration.integrations.network_manager_integration.NetworkManagerIntegration object at 0x11154b620>>
2026-01-11 11:19:44,382 - integration.core.event_bus - DEBUG - EventBus: scheduled async callback on main loop for 'app.startup': <bound method UpdaterIntegration._on_app_startup of <integration.integrations.updater_integration.UpdaterIntegration object at 0x11154b8c0>>
2026-01-11 11:19:44,382 - integration.core.event_bus - DEBUG - EventBus: scheduled async callback on main loop for 'app.startup': <bound method InterruptManagementIntegration._on_app_startup of <integration.integrations.interrupt_management_integration.InterruptManagementIntegration object at 0x1115a0830>>
2026-01-11 11:19:44,382 - integration.core.event_bus - DEBUG - EventBus: scheduled async callback on main loop for 'app.startup': <bound method PermissionRestartIntegration._on_app_startup_event of <integration.integrations.permission_restart_integration.PermissionRestartIntegration object at 0x1115a0050>>
2026-01-11 11:19:44,382 - integration.core.event_bus - DEBUG - EventBus: scheduled async callback on main loop for 'app.startup': <bound method AutostartManagerIntegration._on_app_startup of <integration.integrations.autostart_manager_integration.AutostartManagerIntegration object at 0x1115a2510>>
2026-01-11 11:19:44,382 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: app.startup
✅ Все интеграции запущены
🎯 Запуск приложения с иконкой в меню-баре...
================================================================================
CRITICAL CHECKPOINT: About to activate NSApplication
================================================================================
🔧 Активация NSApplication перед запуском menu bar...
2026-01-11 11:19:44,382 - integration.core.simple_module_coordinator - INFO - 🔧 CRITICAL: Activating NSApplication before app.run()
[NEXY_INIT] Activating NSApplication for menu bar app...
[NEXY_INIT] NSApplication instance: <NSApplication: 0x9c7650000>
[NEXY_INIT] Current activation policy: 1
[NEXY_INIT] 🔍 DIAGNOSTICS: automaticTerminationSupportEnabled = False
[NEXY_INIT] 🔍 DIAGNOSTICS: System uptime = 297992.48s
[NEXY_INIT] 🔍 DIAGNOSTICS: Process ID = 60953
[NEXY_INIT] ℹ️  INFO: Automatic termination was already disabled
2026-01-11 11:19:44,383 - integration.core.event_bus - DEBUG - EventBus: dispatch 'hardware.id_obtained' to 1 subscriber(s)
[NEXY_INIT] setActivationPolicy(Accessory) returned: False
2026-01-11 11:19:44,383 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'hardware.id_obtained': <bound method GrpcClientIntegration._on_hardware_id of <integration.integrations.grpc_client_integration.GrpcClientIntegration object at 0x1115a1400>>
[NEXY_INIT] New activation policy: 1
2026-01-11 11:19:44,383 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: hardware.id_obtained
2026-01-11 11:19:44,383 - integration.integrations.tray_controller_integration - INFO - 🚀 Обработка запуска приложения в TrayControllerIntegration
2026-01-11 11:19:44,383 - integration.integrations.tray_controller_integration - INFO - 🔄 Синхронизация с режимом приложения: sleeping → sleeping
🚀 Обработка запуска приложения в координаторе
📱 Обработка события app.startup
2026-01-11 11:19:44,384 - integration.integrations.network_manager_integration - INFO - App startup - publishing network status snapshot
2026-01-11 11:19:44,384 - integration.core.event_bus - DEBUG - EventBus: dispatch 'network.status_snapshot' to 0 subscriber(s)
2026-01-11 11:19:44,384 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: network.status_snapshot
2026-01-11 11:19:44,384 - integration.core.event_bus - DEBUG - EventBus: dispatch 'tray.update_tooltip' to 0 subscriber(s)
2026-01-11 11:19:44,384 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: tray.update_tooltip
2026-01-11 11:19:44,384 - integration.integrations.updater_integration - INFO - 🚀 Обработка запуска приложения в UpdaterIntegration
2026-01-11 11:19:44,384 - integration.integrations.interrupt_management_integration - INFO - App startup - initializing interrupt management
2026-01-11 11:19:44,384 - integration.core.event_bus - DEBUG - EventBus: dispatch 'interrupt.status_snapshot' to 0 subscriber(s)
2026-01-11 11:19:44,384 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: interrupt.status_snapshot
[NEXY_INIT] Called activateIgnoringOtherApps_(True)
[NEXY_INIT] SUCCESS: NSApplication activated for menu bar app
✅ NSApplication активирован успешно
2026-01-11 11:19:44,384 - integration.core.simple_module_coordinator - INFO - ✅ CRITICAL: NSApplication activated successfully
================================================================================
🛡️ [ANTI_TAL] Вызов _hold_tal_until_tray_ready()...
================================================================================
2026-01-11 11:19:44,385 - integration.core.simple_module_coordinator - INFO - 🛡️ [ANTI_TAL] Вызов _hold_tal_until_tray_ready()
🛡️ [ANTI_TAL] _hold_tal_until_tray_ready() ВХОД (tal_hold_active=False)
2026-01-11 11:19:44,385 - integration.core.simple_module_coordinator - INFO - 🛡️ [ANTI_TAL] _hold_tal_until_tray_ready() ВХОД (tal_hold_active=False)
🛡️ [ANTI_TAL] auto_term_enabled=False
2026-01-11 11:19:44,385 - integration.core.simple_module_coordinator - INFO - 🛡️ [ANTI_TAL] auto_term_enabled=False
🛡️ [ANTI_TAL] Вызов disableAutomaticTermination_()...
2026-01-11 11:19:44,385 - integration.core.simple_module_coordinator - INFO - 🛡️ [ANTI_TAL] Вызов disableAutomaticTermination_()
2026-01-11 11:19:44,385 - integration.core.simple_module_coordinator - INFO - TAL=hold (ts=1768148384.39, auto_term_enabled=False)
🛡️ [ANTI_TAL] TAL удержание установлено (auto_term_enabled=False) - будет снято после tray.ready или через 120s
🛡️ [ANTI_TAL] Используем фоновый event loop для периодического обновления: <_UnixSelectorEventLoop running=True closed=False debug=False>
2026-01-11 11:19:44,385 - integration.core.simple_module_coordinator - INFO - 🛡️ [ANTI_TAL] Используем фоновый event loop для периодического обновления
✅ [ANTI_TAL] _hold_tal_until_tray_ready() завершён успешно
2026-01-11 11:19:44,385 - integration.core.simple_module_coordinator - INFO - ✅ [ANTI_TAL] _hold_tal_until_tray_ready() завершён успешно
================================================================================
⏳ CRITICAL: Waiting for ControlCenter to be ready...
================================================================================
2026-01-11 11:19:44,385 - integration.core.simple_module_coordinator - INFO - ⏳ CRITICAL: Ожидание готовности ControlCenter (tray имеет собственную retry-логику)
2026-01-11 11:19:44,385 - modules.network_manager.core.network_manager - INFO - Network monitoring loop started
2026-01-11 11:19:44,385 - integration.core.event_bus - DEBUG - EventBus: dispatch 'autostart.status_checked' to 0 subscriber(s)
2026-01-11 11:19:44,385 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: autostart.status_checked
2026-01-11 11:19:44,385 - integration.integrations.autostart_manager_integration - WARNING - ⚠️ LaunchAgent автозапуск не найден
2026-01-11 11:19:44,386 - modules.network_manager.core.network_manager - DEBUG - Network quality changed: excellent
2026-01-11 11:19:44,387 - integration.integrations.network_manager_integration - DEBUG - Network event received: network.quality_changed
2026-01-11 11:19:44,387 - integration.core.event_bus - DEBUG - EventBus: dispatch 'network.quality_changed' to 0 subscriber(s)
2026-01-11 11:19:44,387 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: network.quality_changed
2026-01-11 11:19:44,405 - modules.permissions.first_run.status_checker - DEBUG - 🎙️ Microphone: AVFoundation auth_status raw = 3
2026-01-11 11:19:44,405 - modules.permissions.first_run.status_checker - DEBUG - 🎙️ Microphone: GRANTED (AVFoundation)
2026-01-11 11:19:44,406 - modules.permissions.first_run.status_checker - INFO - ♿ Accessibility: AXIsProcessTrusted() → granted
2026-01-11 11:19:44,425 - modules.permissions.first_run.status_checker - DEBUG - ⌨️ Input Monitoring: IOHIDCheckAccess(ListenEvent) = 0
2026-01-11 11:19:44,425 - modules.permissions.first_run.status_checker - DEBUG - ⌨️ Input Monitoring: GRANTED
2026-01-11 11:19:44,448 - modules.permissions.macos.screen_capture_permission - INFO - ✅ Screen Capture permission granted
2026-01-11 11:19:44,449 - modules.permissions.first_run.status_checker - DEBUG - 📺 Screen Capture: GRANTED
2026-01-11 11:19:44,449 - modules.permission_restart.core.permission_change_detector - DEBUG - [PERMISSION_RESTART] Event received: type=permissions.init perm=microphone old=not_determined new=granted session=app_startup_init source=app_startup_init (critical=True)
2026-01-11 11:19:44,449 - modules.permission_restart.core.permission_change_detector - INFO - [PERMISSION_RESTART] Critical permission granted: microphone (not_determined → granted)
2026-01-11 11:19:44,449 - modules.permission_restart.core.permission_change_detector - DEBUG - [PERMISSION_RESTART] Event received: type=permissions.init perm=accessibility old=not_determined new=granted session=app_startup_init source=app_startup_init (critical=True)
2026-01-11 11:19:44,449 - modules.permission_restart.core.permission_change_detector - INFO - [PERMISSION_RESTART] Critical permission granted: accessibility (not_determined → granted)
2026-01-11 11:19:44,449 - modules.permission_restart.core.permission_change_detector - DEBUG - [PERMISSION_RESTART] Event received: type=permissions.init perm=input_monitoring old=not_determined new=granted session=app_startup_init source=app_startup_init (critical=True)
2026-01-11 11:19:44,449 - modules.permission_restart.core.permission_change_detector - INFO - [PERMISSION_RESTART] Critical permission granted: input_monitoring (not_determined → granted)
2026-01-11 11:19:44,449 - modules.permission_restart.core.permission_change_detector - DEBUG - [PERMISSION_RESTART] Event received: type=permissions.init perm=screen_capture old=not_determined new=granted session=app_startup_init source=app_startup_init (critical=True)
2026-01-11 11:19:44,449 - modules.permission_restart.core.permission_change_detector - INFO - [PERMISSION_RESTART] Critical permission granted: screen_capture (not_determined → granted)
2026-01-11 11:19:44,449 - integration.integrations.permission_restart_integration - INFO - [PERMISSION_RESTART] Initialized with current permissions: {'microphone': 'granted', 'accessibility': 'granted', 'input_monitoring': 'granted', 'screen_capture': 'granted'}
2026-01-11 11:19:44,449 - integration.core.event_bus - DEBUG - EventBus: dispatch 'system.permissions_ready' to 1 subscriber(s)
2026-01-11 11:19:44,449 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'system.permissions_ready': <bound method VoiceOverDuckingIntegration._on_permissions_ready of <integration.integrations.voiceover_ducking_integration.VoiceOverDuckingIntegration object at 0x1115a2900>>
2026-01-11 11:19:44,449 - modules.voiceover_control.core.controller - DEBUG - VoiceOverController: пропускаем AX API проверку (может вызвать TCC ошибку)
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
I0000 00:00:1768148384.450473 13748819 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2026-01-11 11:19:44,455 - integration.integrations.autostart_manager_integration - INFO - 📱 App startup - проверяем статус автозапуска
2026-01-11 11:19:44,455 - integration.core.event_bus - DEBUG - EventBus: dispatch 'autostart.status_checked' to 0 subscriber(s)
2026-01-11 11:19:44,455 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: autostart.status_checked
2026-01-11 11:19:44,456 - integration.integrations.autostart_manager_integration - WARNING - ⚠️ LaunchAgent автозапуск не найден
🛡️ [ANTI_TAL] Задача _periodically_refresh_tal_hold() создана в фоновом loop
2026-01-11 11:19:44,457 - integration.core.simple_module_coordinator - INFO - 🛡️ [ANTI_TAL] Задача _periodically_refresh_tal_hold() создана в фоновом loop
🛡️ [ANTI_TAL] Задача _release_tal_hold_after_timeout() создана в фоновом loop
2026-01-11 11:19:44,457 - integration.core.simple_module_coordinator - INFO - 🛡️ [ANTI_TAL] Задача _release_tal_hold_after_timeout() создана в фоновом loop
I0000 00:00:1768148384.641823 13748819 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
I0000 00:00:1768148384.654663 13748782 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2026-01-11 11:19:44,693 - modules.voiceover_control.core.controller - WARNING - 🔍 VoiceOver: CalledProcessError - exit_code=1, stderr='39:50: execution error: The variable speechMuted is not defined. (-2753)
'
2026-01-11 11:19:44,693 - modules.voiceover_control.core.controller - INFO - VoiceOverController: speechMuted AppleScript commands unavailable - using control key fallback
2026-01-11 11:19:44,693 - modules.voiceover_control.core.controller - INFO - VoiceOverController initialized successfully (VoiceOver was running: False)
2026-01-11 11:19:44,693 - integration.integrations.voiceover_ducking_integration - INFO - ✅ VoiceOverDuckingIntegration: controller initialized after permissions_ready
2026-01-11 11:19:44,693 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: system.permissions_ready
2026-01-11 11:19:44,693 - integration.core.event_bus - DEBUG - EventBus: dispatch 'system.ready_to_greet' to 1 subscriber(s)
2026-01-11 11:19:44,693 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'system.ready_to_greet': <bound method WelcomeMessageIntegration._on_ready_to_greet of <integration.integrations.welcome_message_integration.WelcomeMessageIntegration object at 0x1115a27b0>>
2026-01-11 11:19:44,693 - integration.integrations.welcome_message_integration - INFO - 🚀 [WELCOME_INTEGRATION] Обработка события готовности к приветствию
2026-01-11 11:19:44,700 - modules.voiceover_control.core.controller - WARNING - 🔍 VoiceOver: CalledProcessError - exit_code=1, stderr='39:50: execution error: The variable speechMuted is not defined. (-2753)
'
2026-01-11 11:19:44,700 - modules.voiceover_control.core.controller - INFO - VoiceOverController initialized successfully (VoiceOver was running: False)
2026-01-11 11:19:44,700 - integration.integrations.voiceover_ducking_integration - INFO - ✅ VoiceOverDuckingIntegration: controller initialized after first_run_completed
2026-01-11 11:19:44,995 - integration.integrations.welcome_message_integration - INFO - 🎵 [WELCOME_INTEGRATION] Начинаю воспроизведение приветствия (trigger=system_ready)
2026-01-11 11:19:44,995 - integration.integrations.welcome_message_integration - INFO - 🔄 [WELCOME_INTEGRATION] Переход в режим PROCESSING для приветствия
2026-01-11 11:19:44,995 - integration.core.event_bus - DEBUG - EventBus: dispatch 'mode.request' to 1 subscriber(s)
2026-01-11 11:19:44,995 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'mode.request': <bound method ModeManagementIntegration._on_mode_request of <integration.integrations.mode_management_integration.ModeManagementIntegration object at 0x1115a0ec0>>
2026-01-11 11:19:44,995 - integration.integrations.mode_management_integration - INFO - 🔄 MODE_REQUEST: target=PROCESSING, source=welcome_message, session_id=None, priority=None
2026-01-11 11:19:44,996 - integration.integrations.mode_management_integration - INFO - 🔄 MODE_REQUEST: current_mode=AppMode.SLEEPING, target=AppMode.PROCESSING, source=welcome_message
2026-01-11 11:19:44,996 - integration.integrations.mode_management_integration - INFO - 🔄 MODE_REQUEST: применяем mode → AppMode.PROCESSING
2026-01-11 11:19:44,996 - integration.core.state_manager - INFO - 🔄 Режим изменен: sleeping → processing
2026-01-11 11:19:44,996 - mode_management.core.mode_controller - INFO - ✅ Режим изменен: sleeping → processing
2026-01-11 11:19:44,996 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: mode.request
2026-01-11 11:19:44,996 - modules.welcome_message.core.welcome_player - INFO - 🎵 [WELCOME_PLAYER] Начинаю воспроизведение приветствия
2026-01-11 11:19:44,996 - modules.welcome_message.core.welcome_player - INFO - 🔍 [WELCOME_PLAYER] config.enabled=True, config.use_server=True
2026-01-11 11:19:44,997 - integration.integrations.welcome_message_integration - INFO - 🎵 [WELCOME_INTEGRATION] Приветствие началось
2026-01-11 11:19:44,997 - modules.welcome_message.core.welcome_player - INFO - 🔍 [WELCOME_PLAYER] Запрашиваю серверное аудио...
2026-01-11 11:19:44,997 - modules.welcome_message.core.welcome_player - INFO - 🔍 [WELCOME_PLAYER] Генерирую аудио для текста: 'Hi! Nexy is here. How can I help you?'
2026-01-11 11:19:44,997 - modules.grpc_client.core.grpc_client - INFO - 🔌 [DEBUG] _initialize_servers creating ServerConfig for 'local': ssl_verify=True
2026-01-11 11:19:44,997 - modules.grpc_client.core.grpc_client - INFO - 🔌 [DEBUG] Created ServerConfig for 'local': ssl_verify=True
2026-01-11 11:19:44,997 - modules.grpc_client.core.connection_manager - INFO - 🌐 Добавлен сервер local: 127.0.0.1:50051
2026-01-11 11:19:44,997 - modules.grpc_client.core.grpc_client - INFO - 🔌 [DEBUG] _initialize_servers creating ServerConfig for 'production': ssl_verify=False
2026-01-11 11:19:44,997 - modules.grpc_client.core.grpc_client - INFO - 🔌 [DEBUG] Created ServerConfig for 'production': ssl_verify=False
2026-01-11 11:19:44,997 - modules.grpc_client.core.connection_manager - INFO - 🌐 Добавлен сервер production: 20.63.24.187:443
2026-01-11 11:19:44,997 - modules.grpc_client.core.grpc_client - INFO - 🔌 [DEBUG] _initialize_servers creating ServerConfig for 'fallback': ssl_verify=True
2026-01-11 11:19:44,997 - modules.grpc_client.core.grpc_client - INFO - 🔌 [DEBUG] Created ServerConfig for 'fallback': ssl_verify=True
2026-01-11 11:19:44,997 - modules.grpc_client.core.connection_manager - INFO - 🌐 Добавлен сервер fallback: 127.0.0.1:50052
2026-01-11 11:19:44,997 - modules.grpc_client.core.grpc_client - INFO - 🌐 Инициализировано 3 серверов
2026-01-11 11:19:44,997 - modules.grpc_client.core.grpc_client - INFO - 🔌 [DEBUG] Config says default server: 'production'
2026-01-11 11:19:44,998 - modules.grpc_client.core.grpc_client - INFO - 🔌 [DEBUG] Available servers: ['local', 'production', 'fallback']
2026-01-11 11:19:44,998 - modules.grpc_client.core.grpc_client - INFO - 🌐 Установлен сервер по умолчанию: production
2026-01-11 11:19:44,998 - modules.grpc_client.core.connection_manager - INFO - 🔌 [DEBUG] Начало подключения к серверу: production
2026-01-11 11:19:44,998 - modules.grpc_client.core.grpc_client - INFO - 🔄 Состояние соединения: connecting
2026-01-11 11:19:44,998 - modules.grpc_client.core.connection_manager - INFO - 🔌 [DEBUG] Server config - address: 20.63.24.187:443, use_ssl: True, ssl_verify: False
2026-01-11 11:19:44,998 - modules.grpc_client.core.connection_manager - INFO - 🔌 [GRPC_LOOP] Creating channel in loop=4586276816 (running=True)
2026-01-11 11:19:44,998 - modules.grpc_client.core.connection_manager - INFO - 🔌 [DEBUG] Создание канала - use_ssl=True, ssl_verify=False
2026-01-11 11:19:44,998 - modules.grpc_client.core.connection_manager - INFO - 🔌 [DEBUG] SSL enabled, ssl_verify=False
2026-01-11 11:19:44,998 - modules.grpc_client.core.connection_manager - WARNING - ⚠️ SSL verification disabled for 20.63.24.187:443 - используется insecure_channel для self-signed сертификата
2026-01-11 11:19:44,998 - modules.grpc_client.core.connection_manager - INFO - 🔌 [DEBUG] Using insecure_channel for self-signed certificate (as per server documentation)
2026-01-11 11:19:44,998 - grpc._cython.cygrpc - DEBUG - [_cygrpc] Loaded running loop: id(loop)=4586276816
2026-01-11 11:19:44,998 - grpc._cython.cygrpc - DEBUG - [_cygrpc] Loaded running loop: id(loop)=4586276816
2026-01-11 11:19:44,999 - integration.core.event_bus - INFO - EventBus: 'app.mode_changed' → subscribers=9, data={'mode': <AppMode.PROCESSING: 'processing'>}
2026-01-11 11:19:44,999 - integration.core.event_bus - DEBUG - EventBus: dispatch 'app.mode_changed' to 9 subscriber(s)
2026-01-11 11:19:44,999 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method TrayControllerIntegration._on_mode_changed of <integration.integrations.tray_controller_integration.TrayControllerIntegration object at 0x11154b230>>
2026-01-11 11:19:44,999 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method ScreenshotCaptureIntegration._on_mode_changed of <integration.integrations.screenshot_capture_integration.ScreenshotCaptureIntegration object at 0x1115a0980>>
2026-01-11 11:19:44,999 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method ModeManagementIntegration._on_app_mode_changed of <integration.integrations.mode_management_integration.ModeManagementIntegration object at 0x1115a0ec0>>
2026-01-11 11:19:44,999 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method ProcessingWorkflow._on_mode_changed of <integration.workflows.processing_workflow.ProcessingWorkflow object at 0x1115a3380>>
2026-01-11 11:19:44,999 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method ActionExecutionIntegration._on_mode_changed of <integration.integrations.action_execution_integration.ActionExecutionIntegration object at 0x1115a17f0>>
2026-01-11 11:19:44,999 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method VoiceRecognitionIntegration._on_app_mode_changed of <integration.integrations.voice_recognition_integration.VoiceRecognitionIntegration object at 0x1115a0d70>>
2026-01-11 11:19:44,999 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method ListeningWorkflow._on_mode_changed of <integration.workflows.listening_workflow.ListeningWorkflow object at 0x1115a2f90>>
2026-01-11 11:19:44,999 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method SimpleModuleCoordinator._on_mode_changed of <integration.core.simple_module_coordinator.SimpleModuleCoordinator object at 0x111549d30>>
2026-01-11 11:19:44,999 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method UpdaterIntegration._on_mode_changed of <integration.integrations.updater_integration.UpdaterIntegration object at 0x11154b8c0>>
2026-01-11 11:19:45,000 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: app.mode_changed
2026-01-11 11:19:45,000 - integration.core.event_bus - DEBUG - EventBus: dispatch 'app.state_changed' to 1 subscriber(s)
2026-01-11 11:19:45,000 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.state_changed': <bound method InterruptManagementIntegration._on_app_state_changed of <integration.integrations.interrupt_management_integration.InterruptManagementIntegration object at 0x1115a0830>>
2026-01-11 11:19:45,000 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: app.state_changed
2026-01-11 11:19:45,000 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: _on_mode_changed ВЫЗВАН!
2026-01-11 11:19:45,000 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: event type=<class 'dict'>, event={'type': 'app.mode_changed', 'data': {'mode': <AppMode.PROCESSING: 'processing'>}, 'timestamp': 297993.095393125}
2026-01-11 11:19:45,000 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: data={'mode': <AppMode.PROCESSING: 'processing'>}
2026-01-11 11:19:45,000 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: new_mode=AppMode.PROCESSING (type: <enum 'AppMode'>)
2026-01-11 11:19:45,000 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: mode_to_status={<AppMode.SLEEPING: 'sleeping'>: <TrayStatus.SLEEPING: 'sleeping'>, <AppMode.LISTENING: 'listening'>: <TrayStatus.LISTENING: 'listening'>, <AppMode.PROCESSING: 'processing'>: <TrayStatus.PROCESSING: 'processing'>}
2026-01-11 11:19:45,000 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: new_mode in mapping? True
2026-01-11 11:19:45,000 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: key=AppMode.SLEEPING (type: <enum 'AppMode'>), equals new_mode? False
2026-01-11 11:19:45,000 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: key=AppMode.LISTENING (type: <enum 'AppMode'>), equals new_mode? False
2026-01-11 11:19:45,000 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: key=AppMode.PROCESSING (type: <enum 'AppMode'>), equals new_mode? True
2026-01-11 11:19:45,000 - integration.integrations.tray_controller_integration - DEBUG - TrayIntegration: mapping mode -> status: AppMode.PROCESSING -> TrayStatus.PROCESSING
2026-01-11 11:19:45,000 - integration.core.event_bus - DEBUG - EventBus: dispatch 'tray.status_updated' to 0 subscriber(s)
2026-01-11 11:19:45,000 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: tray.status_updated
2026-01-11 11:19:45,000 - integration.integrations.tray_controller_integration - INFO - 🔄 Режим приложения изменен: processing → processing
2026-01-11 11:19:45,001 - integration.integrations.screenshot_capture_integration - INFO - 🔍 ScreenshotCapture: Получено событие app.mode_changed - mode=AppMode.PROCESSING (type: <enum 'AppMode'>)
2026-01-11 11:19:45,001 - integration.integrations.screenshot_capture_integration - INFO - 📸 ScreenshotCaptureIntegration: app entered PROCESSING, session_id=None
2026-01-11 11:19:45,002 - integration.workflows.processing_workflow - DEBUG - ⚙️ ProcessingWorkflow: режим изменен на processing
2026-01-11 11:19:45,002 - integration.workflows.processing_workflow - INFO - ⚙️ ProcessingWorkflow: НАЧАЛО цепочки обработки, session_id=None
2026-01-11 11:19:45,002 - integration.workflows.processing_workflow - WARNING - ⚙️ ProcessingWorkflow: session_id is None, skipping total timeout monitor
2026-01-11 11:19:45,002 - integration.workflows.processing_workflow - INFO - ⚙️ ProcessingWorkflow: переход starting → capturing
2026-01-11 11:19:45,008 - integration.integrations.voice_recognition_integration - DEBUG - VOICE: mode changed to AppMode.PROCESSING, ensuring listening stopped
2026-01-11 11:19:45,008 - modules.voice_recognition.core.google_sr_controller - INFO - ❌ Listening cancelled
2026-01-11 11:19:45,008 - integration.workflows.listening_workflow - DEBUG - 🎤 ListeningWorkflow: режим изменен на processing
2026-01-11 11:19:45,008 - integration.workflows.listening_workflow - INFO - 🎤 ListeningWorkflow: вышли из LISTENING, сбрасываем состояние
🔄 Координация смены режима: processing
2026-01-11 11:19:45,010 - integration.integrations.updater_integration - INFO - Режим приложения изменен на: AppMode.PROCESSING
2026-01-11 11:19:45,188 - PIL.Image - DEBUG - Importing AvifImagePlugin
2026-01-11 11:19:45,195 - PIL.Image - DEBUG - Importing BlpImagePlugin
2026-01-11 11:19:45,199 - PIL.Image - DEBUG - Importing BmpImagePlugin
2026-01-11 11:19:45,199 - PIL.Image - DEBUG - Importing BufrStubImagePlugin
2026-01-11 11:19:45,201 - PIL.Image - DEBUG - Importing CurImagePlugin
2026-01-11 11:19:45,202 - PIL.Image - DEBUG - Importing DcxImagePlugin
2026-01-11 11:19:45,204 - PIL.Image - DEBUG - Importing DdsImagePlugin
2026-01-11 11:19:45,211 - PIL.Image - DEBUG - Importing EpsImagePlugin
2026-01-11 11:19:45,217 - PIL.Image - DEBUG - Importing FitsImagePlugin
2026-01-11 11:19:45,219 - PIL.Image - DEBUG - Importing FliImagePlugin
2026-01-11 11:19:45,221 - PIL.Image - DEBUG - Importing FpxImagePlugin
2026-01-11 11:19:45,222 - PIL.Image - DEBUG - Image: failed to import FpxImagePlugin: No module named 'olefile'
2026-01-11 11:19:45,222 - PIL.Image - DEBUG - Importing FtexImagePlugin
2026-01-11 11:19:45,223 - PIL.Image - DEBUG - Importing GbrImagePlugin
2026-01-11 11:19:45,225 - PIL.Image - DEBUG - Importing GifImagePlugin
2026-01-11 11:19:45,225 - PIL.Image - DEBUG - Importing GribStubImagePlugin
2026-01-11 11:19:45,226 - PIL.Image - DEBUG - Importing Hdf5StubImagePlugin
2026-01-11 11:19:45,226 - PIL.Image - DEBUG - Importing IcnsImagePlugin
2026-01-11 11:19:45,235 - PIL.Image - DEBUG - Importing IcoImagePlugin
2026-01-11 11:19:45,238 - PIL.Image - DEBUG - Importing ImImagePlugin
2026-01-11 11:19:45,240 - PIL.Image - DEBUG - Importing ImtImagePlugin
2026-01-11 11:19:45,242 - PIL.Image - DEBUG - Importing IptcImagePlugin
2026-01-11 11:19:45,244 - PIL.Image - DEBUG - Importing JpegImagePlugin
2026-01-11 11:19:45,244 - PIL.Image - DEBUG - Importing Jpeg2KImagePlugin
2026-01-11 11:19:45,244 - PIL.Image - DEBUG - Importing McIdasImagePlugin
2026-01-11 11:19:45,245 - PIL.Image - DEBUG - Importing MicImagePlugin
2026-01-11 11:19:45,245 - PIL.Image - DEBUG - Image: failed to import MicImagePlugin: No module named 'olefile'
2026-01-11 11:19:45,246 - PIL.Image - DEBUG - Importing MpegImagePlugin
2026-01-11 11:19:45,247 - PIL.Image - DEBUG - Importing MpoImagePlugin
2026-01-11 11:19:45,266 - PIL.Image - DEBUG - Importing MspImagePlugin
2026-01-11 11:19:45,267 - PIL.Image - DEBUG - Importing PalmImagePlugin
2026-01-11 11:19:45,270 - PIL.Image - DEBUG - Importing PcdImagePlugin
2026-01-11 11:19:45,271 - PIL.Image - DEBUG - Importing PcxImagePlugin
2026-01-11 11:19:45,271 - PIL.Image - DEBUG - Importing PdfImagePlugin
2026-01-11 11:19:45,283 - PIL.Image - DEBUG - Importing PixarImagePlugin
2026-01-11 11:19:45,283 - PIL.Image - DEBUG - Importing PngImagePlugin
2026-01-11 11:19:45,283 - PIL.Image - DEBUG - Importing PpmImagePlugin
2026-01-11 11:19:45,283 - PIL.Image - DEBUG - Importing PsdImagePlugin
2026-01-11 11:19:45,286 - PIL.Image - DEBUG - Importing QoiImagePlugin
2026-01-11 11:19:45,288 - PIL.Image - DEBUG - Importing SgiImagePlugin
2026-01-11 11:19:45,290 - PIL.Image - DEBUG - Importing SpiderImagePlugin
2026-01-11 11:19:45,292 - PIL.Image - DEBUG - Importing SunImagePlugin
2026-01-11 11:19:45,293 - PIL.Image - DEBUG - Importing TgaImagePlugin
2026-01-11 11:19:45,295 - PIL.Image - DEBUG - Importing TiffImagePlugin
2026-01-11 11:19:45,295 - PIL.Image - DEBUG - Importing WebPImagePlugin
2026-01-11 11:19:45,303 - PIL.Image - DEBUG - Importing WmfImagePlugin
2026-01-11 11:19:45,305 - PIL.Image - DEBUG - Importing XbmImagePlugin
2026-01-11 11:19:45,306 - PIL.Image - DEBUG - Importing XpmImagePlugin
2026-01-11 11:19:45,308 - PIL.Image - DEBUG - Importing XVThumbImagePlugin
================================================================================
✅ CRITICAL: Delay completed, starting app.run()...
================================================================================
2026-01-11 11:19:45,386 - integration.core.simple_module_coordinator - INFO - ✅ CRITICAL: Задержка завершена, запуск app.run()
2026-01-11 11:19:45,386 - integration.core.simple_module_coordinator - INFO - 🔍 CRITICAL DEBUG: tray_controller=<modules.tray_controller.core.tray_controller.TrayController object at 0x1115a3b60>, type=<class 'modules.tray_controller.core.tray_controller.TrayController'>
🔍 CRITICAL DEBUG: tray_controller=<modules.tray_controller.core.tray_controller.TrayController object at 0x1115a3b60>, type=<class 'modules.tray_controller.core.tray_controller.TrayController'>
2026-01-11 11:19:45,386 - integration.core.simple_module_coordinator - INFO - ✅ CRITICAL: Вызываем tray_controller.run_app()
✅ CRITICAL: Вызываем tray_controller.run_app()
2026-01-11 11:19:45,388 - modules.tray_controller.core.tray_controller - INFO - ✅ NSApplication активирован перед app.run()
2026-01-11 11:19:45,388 - modules.tray_controller.macos.menu_handler - INFO - ================================================================================
2026-01-11 11:19:45,388 - modules.tray_controller.macos.menu_handler - INFO - CRITICAL: Setting up delayed icon setting with single-flight + circuit-breaker
2026-01-11 11:19:45,388 - modules.tray_controller.macos.menu_handler - INFO - CRITICAL: Icon path: /var/folders/ys/xlx_chms3hqcs1lfyq37395c0000gn/T/tmp306gho5r.png
2026-01-11 11:19:45,388 - modules.tray_controller.macos.menu_handler - INFO - CRITICAL: Series ID: b746be95
2026-01-11 11:19:45,388 - modules.tray_controller.macos.menu_handler - INFO - ================================================================================
================================================================================
CRITICAL: Setting up delayed icon setting with single-flight + circuit-breaker
CRITICAL: Icon path: /var/folders/ys/xlx_chms3hqcs1lfyq37395c0000gn/T/tmp306gho5r.png
CRITICAL: Series ID: b746be95
================================================================================
2026-01-11 11:19:45,388 - modules.tray_controller.macos.menu_handler - INFO - [STATUS_ITEM_MANAGER] Waiting for Control Center ready...
2026-01-11 11:19:45,388 - modules.tray_controller.macos.status_item_manager - INFO - [STATUS_ITEM_MANAGER] Waiting for Control Center ready (timeout=10.0s)...
2026-01-11 11:19:45,389 - modules.tray_controller.macos.status_item_manager - INFO - CC_READY ts=297993.49
2026-01-11 11:19:45,389 - modules.tray_controller.macos.menu_handler - INFO - [STATUS_ITEM_MANAGER] ✅ Control Center is ready
2026-01-11 11:19:45,389 - modules.tray_controller.macos.menu_handler - INFO - TRAY_SERIES_ID=b746be95
TRAY_SERIES_ID=b746be95
2026-01-11 11:19:45,389 - modules.tray_controller.macos.menu_handler - INFO - ✅ [STATUS_ITEM_MANAGER] Delayed icon setting timer started (first_attempt_delay=1.0s, series_id=b746be95)
2026-01-11 11:19:45,389 - modules.tray_controller.core.tray_controller - INFO - 🚀 КРИТИЧНО: Запуск app.run()...
🚀 КРИТИЧНО: Запуск app.run()...
🔍 DEBUG: app object: <rumps.rumps.App object at 0x1115c3a10>
🔍 DEBUG: app type: <class 'rumps.rumps.App'>
🔍 DEBUG: NSApplication activation policy before app.run(): 1
🔍 DEBUG: NSApplication is active: False
2026-01-11 11:19:45,447 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: _apply_status_ui_sync ВЫЗВАН! status=TrayStatus.SLEEPING (type: <enum 'TrayStatus'>)
2026-01-11 11:19:45,448 - modules.tray_controller.core.tray_types - DEBUG - 🎯 TRAY DEBUG: TrayIconGenerator.create_circle_icon status=TrayStatus.SLEEPING (type: <enum 'TrayStatus'>)
2026-01-11 11:19:45,448 - modules.tray_controller.core.tray_types - DEBUG - 🎯 TRAY DEBUG: Available colors: {<TrayStatus.SLEEPING: 'sleeping'>: '#808080', <TrayStatus.LISTENING: 'listening'>: '#007AFF', <TrayStatus.PROCESSING: 'processing'>: '#FF9500', <TrayStatus.LOCKED: 'locked'>: '#FF3B30'}
2026-01-11 11:19:45,448 - modules.tray_controller.core.tray_types - DEBUG - 🎯 TRAY DEBUG: Selected color: #808080
2026-01-11 11:19:45,448 - modules.tray_controller.macos.tray_icon - DEBUG - 🎯 TRAY DEBUG: create_icon_file вызван для status=TrayStatus.SLEEPING
2026-01-11 11:19:45,448 - modules.tray_controller.macos.tray_icon - DEBUG - 🎯 TRAY DEBUG: generated color=#808080, PIL_available=True
2026-01-11 11:19:45,449 - modules.tray_controller.macos.menu_handler - INFO - 🔍 ДИАГНОСТИКА update_icon: icon_path='/var/folders/ys/xlx_chms3hqcs1lfyq37395c0000gn/T/tmpslmhwopp.png'
2026-01-11 11:19:45,449 - modules.tray_controller.macos.menu_handler - INFO - 🔍 ДИАГНОСТИКА update_icon: os.path.exists(icon_path)=True
2026-01-11 11:19:45,449 - modules.tray_controller.macos.menu_handler - INFO - 🔍 ДИАГНОСТИКА update_icon: размер файла=193 bytes
2026-01-11 11:19:45,450 - modules.tray_controller.macos.menu_handler - INFO - ✅ ДИАГНОСТИКА update_icon: Иконка обновлена успешно (попытка 1)
2026-01-11 11:19:45,450 - integration.integrations.tray_controller_integration - INFO - ✅ Tray UI applied: sleeping -> sleeping
2026-01-11 11:19:45,450 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: _apply_status_ui_sync ВЫЗВАН! status=TrayStatus.PROCESSING (type: <enum 'TrayStatus'>)
2026-01-11 11:19:45,450 - modules.tray_controller.core.tray_types - DEBUG - 🎯 TRAY DEBUG: TrayIconGenerator.create_circle_icon status=TrayStatus.PROCESSING (type: <enum 'TrayStatus'>)
2026-01-11 11:19:45,450 - modules.tray_controller.core.tray_types - DEBUG - 🎯 TRAY DEBUG: Available colors: {<TrayStatus.SLEEPING: 'sleeping'>: '#808080', <TrayStatus.LISTENING: 'listening'>: '#007AFF', <TrayStatus.PROCESSING: 'processing'>: '#FF9500', <TrayStatus.LOCKED: 'locked'>: '#FF3B30'}
2026-01-11 11:19:45,450 - modules.tray_controller.core.tray_types - DEBUG - 🎯 TRAY DEBUG: Selected color: #FF9500
2026-01-11 11:19:45,450 - modules.tray_controller.macos.tray_icon - DEBUG - 🎯 TRAY DEBUG: create_icon_file вызван для status=TrayStatus.PROCESSING
2026-01-11 11:19:45,450 - modules.tray_controller.macos.tray_icon - DEBUG - 🎯 TRAY DEBUG: generated color=#FF9500, PIL_available=True
2026-01-11 11:19:45,451 - modules.tray_controller.macos.menu_handler - INFO - 🔍 ДИАГНОСТИКА update_icon: icon_path='/var/folders/ys/xlx_chms3hqcs1lfyq37395c0000gn/T/tmpkzxkvw8n.png'
2026-01-11 11:19:45,451 - modules.tray_controller.macos.menu_handler - INFO - 🔍 ДИАГНОСТИКА update_icon: os.path.exists(icon_path)=True
2026-01-11 11:19:45,451 - modules.tray_controller.macos.menu_handler - INFO - 🔍 ДИАГНОСТИКА update_icon: размер файла=195 bytes
2026-01-11 11:19:45,451 - modules.tray_controller.macos.menu_handler - INFO - ✅ ДИАГНОСТИКА update_icon: Иконка обновлена успешно (попытка 1)
2026-01-11 11:19:45,451 - integration.integrations.tray_controller_integration - INFO - ✅ Tray UI applied: sleeping -> processing
2026-01-11 11:19:45,455 - integration.core.simple_module_coordinator - INFO - ✅ UI-таймер запущен через rumps callback
2026-01-11 11:19:45,455 - modules.tray_controller.macos.status_item_manager - INFO - [STATUS_ITEM_MANAGER] Starting creation attempt 1 (series_id=b746be95)
2026-01-11 11:19:45,455 - modules.tray_controller.macos.menu_handler - INFO - TRAY_ATTEMPT1 start (series_id=b746be95)
2026-01-11 11:19:45,456 - modules.tray_controller.macos.status_item_manager - INFO - [STATUS_ITEM_MANAGER] ✅ Creation succeeded (attempt=1, duration=0ms)
2026-01-11 11:19:45,456 - modules.tray_controller.macos.menu_handler - INFO - TRAY_ATTEMPT1 result=ok (series_id=b746be95, duration=0ms)
✅ CRITICAL: Icon set successfully on attempt 1
2026-01-11 11:19:45,511 - modules.screenshot_capture.macos.core_graphics_bridge - DEBUG - ✅ WebP → Base64 напрямую: 1383x900, 156292 bytes, quality=85
2026-01-11 11:19:45,512 - integration.integrations.screenshot_capture_integration - INFO - TRACE phase=screenshot.ready ts=297993608 session=None extra={format=webp, early=False}
2026-01-11 11:19:45,513 - integration.core.event_bus - DEBUG - EventBus: dispatch 'screenshot.captured' to 3 subscriber(s)
2026-01-11 11:19:45,513 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'screenshot.captured': <bound method GrpcClientIntegration._on_screenshot_captured of <integration.integrations.grpc_client_integration.GrpcClientIntegration object at 0x1115a1400>>
2026-01-11 11:19:45,513 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'screenshot.captured': <bound method ProcessingWorkflow._on_screenshot_captured of <integration.workflows.processing_workflow.ProcessingWorkflow object at 0x1115a3380>>
2026-01-11 11:19:45,513 - integration.workflows.processing_workflow - INFO - 📸 ProcessingWorkflow: скриншот захвачен, path=None
2026-01-11 11:19:45,513 - integration.workflows.processing_workflow - INFO - ⚙️ ProcessingWorkflow: переход capturing → sending_grpc
2026-01-11 11:19:45,514 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'screenshot.captured': <bound method SimpleModuleCoordinator._on_screenshot_captured of <integration.core.simple_module_coordinator.SimpleModuleCoordinator object at 0x111549d30>>
🖼️ Screenshot captured: /var/folders/ys/xlx_chms3hqcs1lfyq37395c0000gn/T/nexy_screenshots/shot_297993609.webp (1383x900, 156292 bytes), session=None
2026-01-11 11:19:45,514 - integration.core.simple_module_coordinator - INFO - Screenshot captured: path=/var/folders/ys/xlx_chms3hqcs1lfyq37395c0000gn/T/nexy_screenshots/shot_297993609.webp, size=156292, dims=1383x900, session=None
2026-01-11 11:19:45,514 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: screenshot.captured
2026-01-11 11:19:45,514 - integration.integrations.screenshot_capture_integration - INFO - Screenshot captured: /var/folders/ys/xlx_chms3hqcs1lfyq37395c0000gn/T/nexy_screenshots/shot_297993609.webp
2026-01-11 11:19:45,514 - integration.workflows.processing_workflow - DEBUG - ⚙️ ProcessingWorkflow: мониторинг этапа capturing отменен
2026-01-11 11:20:15,224 - integration.core.simple_module_coordinator - INFO - idle_cpu_pct=0.40
2026-01-11 11:20:15,226 - integration.core.simple_module_coordinator - INFO - idle_ram_mb=81.12
2026-01-11 11:20:15,227 - integration.core.simple_module_coordinator - DEBUG - 📊 [METRICS] Idle CPU: 0.40%, RAM: 81.12 MB
2026-01-11 11:20:15,515 - integration.workflows.processing_workflow - WARNING - ⏰ ProcessingWorkflow: таймаут этапа sending_grpc (30.0с)
2026-01-11 11:20:15,516 - integration.workflows.processing_workflow - ERROR - ❌ ProcessingWorkflow: обработка ошибки stage_timeout_sending_grpc на этапе sending_grpc
2026-01-11 11:20:15,516 - integration.workflows.processing_workflow - INFO - ⚙️ ProcessingWorkflow: возврат в SLEEPING, reason=error_stage_timeout_sending_grpc
2026-01-11 11:20:15,525 - integration.core.event_bus - DEBUG - EventBus: dispatch 'mode.request' to 1 subscriber(s)
2026-01-11 11:20:15,527 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'mode.request': <bound method ModeManagementIntegration._on_mode_request of <integration.integrations.mode_management_integration.ModeManagementIntegration object at 0x1115a0ec0>>
2026-01-11 11:20:15,527 - integration.integrations.mode_management_integration - INFO - 🔄 MODE_REQUEST: target=AppMode.SLEEPING, source=ProcessingWorkflow.processing_error_stage_timeout_sending_grpc, session_id=None, priority=90
2026-01-11 11:20:15,527 - integration.integrations.mode_management_integration - INFO - 🔄 MODE_REQUEST: current_mode=AppMode.PROCESSING, target=AppMode.SLEEPING, source=ProcessingWorkflow.processing_error_stage_timeout_sending_grpc
2026-01-11 11:20:15,527 - integration.integrations.mode_management_integration - INFO - 🔄 MODE_REQUEST: в PROCESSING, проверяем session_id (active=None, request=None)
2026-01-11 11:20:15,527 - integration.integrations.mode_management_integration - INFO - 🔄 MODE_REQUEST: применяем как interrupt (source=ProcessingWorkflow.processing_error_stage_timeout_sending_grpc, priority=90) → AppMode.SLEEPING
2026-01-11 11:20:15,528 - integration.core.state_manager - INFO - 🔄 Режим изменен: processing → sleeping
2026-01-11 11:20:15,528 - mode_management.core.mode_controller - INFO - ✅ Режим изменен: processing → sleeping
2026-01-11 11:20:15,528 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: mode.request
2026-01-11 11:20:15,528 - integration.workflows.base_workflow - DEBUG - 🔄 ProcessingWorkflow: запрос смены режима sleeping
2026-01-11 11:20:15,528 - integration.workflows.processing_workflow - DEBUG - ⚙️ ProcessingWorkflow: состояние очищено
2026-01-11 11:20:15,529 - integration.workflows.base_workflow - DEBUG - 🔄 ProcessingWorkflow: задача отменена - ProcessingWorkflow:stage_timeout_sending_grpc
2026-01-11 11:20:15,529 - integration.core.event_bus - INFO - EventBus: 'app.mode_changed' → subscribers=9, data={'mode': <AppMode.SLEEPING: 'sleeping'>}
2026-01-11 11:20:15,529 - integration.core.event_bus - DEBUG - EventBus: dispatch 'app.mode_changed' to 9 subscriber(s)
2026-01-11 11:20:15,529 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method TrayControllerIntegration._on_mode_changed of <integration.integrations.tray_controller_integration.TrayControllerIntegration object at 0x11154b230>>
2026-01-11 11:20:15,530 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method ScreenshotCaptureIntegration._on_mode_changed of <integration.integrations.screenshot_capture_integration.ScreenshotCaptureIntegration object at 0x1115a0980>>
2026-01-11 11:20:15,530 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method ModeManagementIntegration._on_app_mode_changed of <integration.integrations.mode_management_integration.ModeManagementIntegration object at 0x1115a0ec0>>
2026-01-11 11:20:15,530 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method ProcessingWorkflow._on_mode_changed of <integration.workflows.processing_workflow.ProcessingWorkflow object at 0x1115a3380>>
2026-01-11 11:20:15,530 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method ActionExecutionIntegration._on_mode_changed of <integration.integrations.action_execution_integration.ActionExecutionIntegration object at 0x1115a17f0>>
2026-01-11 11:20:15,530 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method VoiceRecognitionIntegration._on_app_mode_changed of <integration.integrations.voice_recognition_integration.VoiceRecognitionIntegration object at 0x1115a0d70>>
2026-01-11 11:20:15,530 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method ListeningWorkflow._on_mode_changed of <integration.workflows.listening_workflow.ListeningWorkflow object at 0x1115a2f90>>
2026-01-11 11:20:15,531 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method SimpleModuleCoordinator._on_mode_changed of <integration.core.simple_module_coordinator.SimpleModuleCoordinator object at 0x111549d30>>
2026-01-11 11:20:15,531 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method UpdaterIntegration._on_mode_changed of <integration.integrations.updater_integration.UpdaterIntegration object at 0x11154b8c0>>
2026-01-11 11:20:15,531 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: app.mode_changed
2026-01-11 11:20:15,531 - integration.core.event_bus - DEBUG - EventBus: dispatch 'app.state_changed' to 1 subscriber(s)
2026-01-11 11:20:15,534 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.state_changed': <bound method InterruptManagementIntegration._on_app_state_changed of <integration.integrations.interrupt_management_integration.InterruptManagementIntegration object at 0x1115a0830>>
2026-01-11 11:20:15,536 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: app.state_changed
2026-01-11 11:20:15,538 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: _on_mode_changed ВЫЗВАН!
2026-01-11 11:20:15,540 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: event type=<class 'dict'>, event={'type': 'app.mode_changed', 'data': {'mode': <AppMode.SLEEPING: 'sleeping'>}, 'timestamp': 298023.625751791}
2026-01-11 11:20:15,540 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: data={'mode': <AppMode.SLEEPING: 'sleeping'>}
2026-01-11 11:20:15,540 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: new_mode=AppMode.SLEEPING (type: <enum 'AppMode'>)
2026-01-11 11:20:15,540 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: mode_to_status={<AppMode.SLEEPING: 'sleeping'>: <TrayStatus.SLEEPING: 'sleeping'>, <AppMode.LISTENING: 'listening'>: <TrayStatus.LISTENING: 'listening'>, <AppMode.PROCESSING: 'processing'>: <TrayStatus.PROCESSING: 'processing'>}
2026-01-11 11:20:15,540 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: new_mode in mapping? True
2026-01-11 11:20:15,540 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: key=AppMode.SLEEPING (type: <enum 'AppMode'>), equals new_mode? True
2026-01-11 11:20:15,540 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: key=AppMode.LISTENING (type: <enum 'AppMode'>), equals new_mode? False
2026-01-11 11:20:15,540 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: key=AppMode.PROCESSING (type: <enum 'AppMode'>), equals new_mode? False
2026-01-11 11:20:15,541 - integration.integrations.tray_controller_integration - DEBUG - TrayIntegration: mapping mode -> status: AppMode.SLEEPING -> TrayStatus.SLEEPING
2026-01-11 11:20:15,541 - integration.core.event_bus - DEBUG - EventBus: dispatch 'tray.status_updated' to 0 subscriber(s)
2026-01-11 11:20:15,541 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: tray.status_updated
2026-01-11 11:20:15,541 - integration.integrations.tray_controller_integration - INFO - 🔄 Режим приложения изменен: sleeping → sleeping
2026-01-11 11:20:15,547 - integration.integrations.screenshot_capture_integration - INFO - 🔍 ScreenshotCapture: Получено событие app.mode_changed - mode=AppMode.SLEEPING (type: <enum 'AppMode'>)
2026-01-11 11:20:15,547 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: _apply_status_ui_sync ВЫЗВАН! status=TrayStatus.SLEEPING (type: <enum 'TrayStatus'>)
2026-01-11 11:20:15,547 - integration.integrations.screenshot_capture_integration - DEBUG - ScreenshotCapture: Игнорируем режим AppMode.SLEEPING, ждем PROCESSING
2026-01-11 11:20:15,549 - integration.workflows.processing_workflow - DEBUG - ⚙️ ProcessingWorkflow: режим изменен на sleeping
2026-01-11 11:20:15,549 - integration.integrations.voice_recognition_integration - DEBUG - VOICE: mode changed to AppMode.SLEEPING, ensuring listening stopped
2026-01-11 11:20:15,550 - modules.voice_recognition.core.google_sr_controller - INFO - ❌ Listening cancelled
2026-01-11 11:20:15,550 - integration.workflows.listening_workflow - DEBUG - 🎤 ListeningWorkflow: режим изменен на sleeping
🔄 Координация смены режима: sleeping
2026-01-11 11:20:15,572 - modules.tray_controller.core.tray_types - DEBUG - 🎯 TRAY DEBUG: TrayIconGenerator.create_circle_icon status=TrayStatus.SLEEPING (type: <enum 'TrayStatus'>)
2026-01-11 11:20:15,587 - modules.tray_controller.core.tray_types - DEBUG - 🎯 TRAY DEBUG: Available colors: {<TrayStatus.SLEEPING: 'sleeping'>: '#808080', <TrayStatus.LISTENING: 'listening'>: '#007AFF', <TrayStatus.PROCESSING: 'processing'>: '#FF9500', <TrayStatus.LOCKED: 'locked'>: '#FF3B30'}
2026-01-11 11:20:15,587 - integration.integrations.updater_integration - INFO - Режим приложения изменен на: AppMode.SLEEPING
2026-01-11 11:20:15,590 - modules.tray_controller.core.tray_types - DEBUG - 🎯 TRAY DEBUG: Selected color: #808080
2026-01-11 11:20:15,590 - modules.tray_controller.macos.tray_icon - DEBUG - 🎯 TRAY DEBUG: create_icon_file вызван для status=TrayStatus.SLEEPING
2026-01-11 11:20:15,590 - modules.tray_controller.macos.tray_icon - DEBUG - 🎯 TRAY DEBUG: generated color=#808080, PIL_available=True
2026-01-11 11:20:15,592 - modules.tray_controller.macos.menu_handler - INFO - 🔍 ДИАГНОСТИКА update_icon: icon_path='/var/folders/ys/xlx_chms3hqcs1lfyq37395c0000gn/T/tmp5_w33x8b.png'
2026-01-11 11:20:15,592 - modules.tray_controller.macos.menu_handler - INFO - 🔍 ДИАГНОСТИКА update_icon: os.path.exists(icon_path)=True
2026-01-11 11:20:15,592 - modules.tray_controller.macos.menu_handler - INFO - 🔍 ДИАГНОСТИКА update_icon: размер файла=193 bytes
2026-01-11 11:20:15,594 - modules.tray_controller.macos.menu_handler - INFO - ✅ ДИАГНОСТИКА update_icon: Иконка обновлена успешно (попытка 1)
2026-01-11 11:20:15,594 - integration.integrations.tray_controller_integration - INFO - ✅ Tray UI applied: processing -> sleeping
