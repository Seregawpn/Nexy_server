2025-10-20 13:04:13,172 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: new_mode=AppMode.PROCESSING (type: <enum 'AppMode'>)
2025-10-20 13:04:13,172 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: mode_to_status={<AppMode.SLEEPING: 'sleeping'>: <TrayStatus.SLEEPING: 'sleeping'>, <AppMode.LISTENING: 'listening'>: <TrayStatus.LISTENING: 'listening'>, <AppMode.PROCESSING: 'processing'>: <TrayStatus.PROCESSING: 'processing'>}
2025-10-20 13:04:13,172 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: new_mode in mapping? True
2025-10-20 13:04:13,173 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: key=AppMode.SLEEPING (type: <enum 'AppMode'>), equals new_mode? False
2025-10-20 13:04:13,173 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: key=AppMode.LISTENING (type: <enum 'AppMode'>), equals new_mode? False
2025-10-20 13:04:13,173 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: key=AppMode.PROCESSING (type: <enum 'AppMode'>), equals new_mode? True
2025-10-20 13:04:13,173 - integration.integrations.tray_controller_integration - DEBUG - TrayIntegration: mapping mode -> status: AppMode.PROCESSING -> TrayStatus.PROCESSING
2025-10-20 13:04:13,173 - integration.core.event_bus - DEBUG - EventBus: dispatch 'tray.status_updated' to 0 subscriber(s)
2025-10-20 13:04:13,173 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: tray.status_updated
2025-10-20 13:04:13,173 - integration.integrations.tray_controller_integration - INFO - 🔄 Режим приложения изменен: processing → processing
2025-10-20 13:04:13,173 - integration.integrations.screenshot_capture_integration - INFO - 🔍 ScreenshotCapture: Получено событие app.mode_changed - mode=AppMode.PROCESSING (type: <enum 'AppMode'>)
2025-10-20 13:04:13,173 - integration.integrations.screenshot_capture_integration - DEBUG - ScreenshotCaptureIntegration: already captured for session
2025-10-20 13:04:13,173 - integration.workflows.processing_workflow - DEBUG - ⚙️ ProcessingWorkflow: режим изменен на processing
2025-10-20 13:04:13,173 - integration.workflows.processing_workflow - INFO - ⚙️ ProcessingWorkflow: НАЧАЛО цепочки обработки, session_id=None
2025-10-20 13:04:13,173 - integration.workflows.processing_workflow - INFO - ⚙️ ProcessingWorkflow: переход starting → capturing
2025-10-20 13:04:13,174 - integration.workflows.listening_workflow - DEBUG - 🎤 ListeningWorkflow: режим изменен на processing
🔄 Координация смены режима: processing
2025-10-20 13:04:13,174 - integration.integrations.updater_integration - INFO - Режим приложения изменен на: None
I0000 00:00:1760979853.188185 2294900 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-10-20 13:04:13,208 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: _apply_status_ui_sync ВЫЗВАН! status=TrayStatus.PROCESSING (type: <enum 'TrayStatus'>)
🎯 TRAY DEBUG: TrayIconGenerator.create_circle_icon status=TrayStatus.PROCESSING (type: <enum 'TrayStatus'>)
🎯 TRAY DEBUG: Available colors: {<TrayStatus.SLEEPING: 'sleeping'>: '#808080', <TrayStatus.LISTENING: 'listening'>: '#007AFF', <TrayStatus.PROCESSING: 'processing'>: '#FF9500'}
🎯 TRAY DEBUG: Selected color: #FF9500
🎯 TRAY DEBUG: create_icon_file вызван для status=TrayStatus.PROCESSING
🎯 TRAY DEBUG: generated color=#FF9500, PIL_available=True
2025-10-20 13:04:13,212 - integration.integrations.tray_controller_integration - INFO - ✅ Tray UI applied: listening -> processing
2025-10-20 13:04:13,360 - modules.voiceover_control.core.controller - DEBUG - VoiceOverController: Updated status - currently running: False
2025-10-20 13:04:13,360 - modules.voiceover_control.core.controller - DEBUG - VoiceOverController: VoiceOver is not currently running, skipping duck for mode processing
2025-10-20 13:04:13,360 - integration.integrations.voiceover_ducking_integration - DEBUG - VoiceOverDuckingIntegration: Applied mode processing
2025-10-20 13:04:15,498 - integration.integrations.grpc_client_integration - INFO - gRPC received text_chunk len=27 for session 1760979846.413692
2025-10-20 13:04:15,498 - integration.core.event_bus - DEBUG - EventBus: dispatch 'grpc.response.text' to 0 subscriber(s)
2025-10-20 13:04:15,498 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: grpc.response.text
2025-10-20 13:04:15,847 - integration.integrations.grpc_client_integration - INFO - gRPC received audio_chunk bytes=244800 dtype=int16 shape=[] for session 1760979846.413692
2025-10-20 13:04:15,847 - integration.core.event_bus - DEBUG - EventBus: dispatch 'grpc.response.audio' to 1 subscriber(s)
2025-10-20 13:04:15,847 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'grpc.response.audio': <bound method SpeechPlaybackIntegration._on_audio_chunk of <integration.integrations.speech_playback_integration.SpeechPlaybackIntegration object at 0x114996ba0>>
2025-10-20 13:04:15,847 - integration.integrations.speech_playback_integration - INFO - 🔊 Получен аудио чанк: 244800 bytes, dtype=int16, shape=[], sr=None, ch=None для сессии 1760979846.413692
2025-10-20 13:04:15,849 - integration.integrations.speech_playback_integration - INFO - 🔍 audio_chunk: sid=1760979846.413692, in_dtype='int16', dec_dtype=int16, shape=(122400,), min=-21259.000, max=18719.000, bytes=244800
2025-10-20 13:04:15,849 - modules.speech_playback.core.buffer - INFO - ✅ Чанк добавлен: chunk_2_1760979855849 (size: 122400, queue: 1)
2025-10-20 13:04:15,849 - modules.speech_playback.core.buffer - DEBUG - 🔍 Получен чанк: chunk_2_1760979855849
2025-10-20 13:04:15,850 - modules.speech_playback.core.buffer - INFO - ✅ Чанк добавлен в буфер: chunk_2_1760979855849 (frames: 122400, buffer: 0 → 122400, ch=1)
2025-10-20 13:04:16,152 - modules.speech_playback.core.player - INFO - ▶️ Аудио поток стартован (lazy start)
2025-10-20 13:04:16,152 - modules.speech_playback.core.player - INFO - ✅ Аудио данные добавлены: chunk_2_1760979855849 (size: 122400)
2025-10-20 13:04:16,152 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: grpc.response.audio
2025-10-20 13:04:16,153 - integration.integrations.grpc_client_integration - INFO - gRPC received text_chunk len=45 for session 1760979846.413692
2025-10-20 13:04:16,153 - integration.core.event_bus - DEBUG - EventBus: dispatch 'grpc.response.text' to 0 subscriber(s)
2025-10-20 13:04:16,153 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: grpc.response.text
2025-10-20 13:04:16,160 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 121888)
2025-10-20 13:04:16,170 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 121376)
2025-10-20 13:04:16,180 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 120864)
2025-10-20 13:04:16,181 - integration.integrations.grpc_client_integration - INFO - gRPC received audio_chunk bytes=283200 dtype=int16 shape=[] for session 1760979846.413692
2025-10-20 13:04:16,181 - integration.core.event_bus - DEBUG - EventBus: dispatch 'grpc.response.audio' to 1 subscriber(s)
2025-10-20 13:04:16,181 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'grpc.response.audio': <bound method SpeechPlaybackIntegration._on_audio_chunk of <integration.integrations.speech_playback_integration.SpeechPlaybackIntegration object at 0x114996ba0>>
2025-10-20 13:04:16,181 - integration.integrations.speech_playback_integration - INFO - 🔊 Получен аудио чанк: 283200 bytes, dtype=int16, shape=[], sr=None, ch=None для сессии 1760979846.413692
2025-10-20 13:04:16,182 - integration.integrations.speech_playback_integration - INFO - 🔍 audio_chunk: sid=1760979846.413692, in_dtype='int16', dec_dtype=int16, shape=(141600,), min=-21997.000, max=20166.000, bytes=283200
2025-10-20 13:04:16,183 - modules.speech_playback.core.buffer - INFO - ✅ Чанк добавлен: chunk_3_1760979856183 (size: 141600, queue: 1)
2025-10-20 13:04:16,183 - modules.speech_playback.core.player - INFO - ✅ Аудио данные добавлены: chunk_3_1760979856183 (size: 141600)
2025-10-20 13:04:16,183 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: grpc.response.audio
2025-10-20 13:04:16,183 - integration.integrations.grpc_client_integration - INFO - gRPC received text_chunk len=103 for session 1760979846.413692
2025-10-20 13:04:16,183 - integration.core.event_bus - DEBUG - EventBus: dispatch 'grpc.response.text' to 0 subscriber(s)
2025-10-20 13:04:16,183 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: grpc.response.text
2025-10-20 13:04:16,190 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 120352)
2025-10-20 13:04:16,200 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 119840)
2025-10-20 13:04:16,210 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 119328)
2025-10-20 13:04:16,220 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 118816)
2025-10-20 13:04:16,230 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 118304)
2025-10-20 13:04:16,240 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 117792)
2025-10-20 13:04:16,250 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 117280)
2025-10-20 13:04:16,260 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 116768)
2025-10-20 13:04:16,270 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 116256)
2025-10-20 13:04:16,280 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 115744)
2025-10-20 13:04:16,290 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 115232)
2025-10-20 13:04:16,300 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 114720)
2025-10-20 13:04:16,320 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 114208)
2025-10-20 13:04:16,330 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 113696)
2025-10-20 13:04:16,340 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 113184)
2025-10-20 13:04:16,350 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 112672)
2025-10-20 13:04:16,360 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 112160)
2025-10-20 13:04:16,370 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 111648)
2025-10-20 13:04:16,380 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 111136)
2025-10-20 13:04:16,390 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 110624)
2025-10-20 13:04:16,400 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 110112)
2025-10-20 13:04:16,410 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 109600)
2025-10-20 13:04:16,420 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 109088)
2025-10-20 13:04:16,430 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 108576)
2025-10-20 13:04:16,440 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 108064)
2025-10-20 13:04:16,450 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 107552)
2025-10-20 13:04:16,460 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 107040)
2025-10-20 13:04:16,480 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 106528)
2025-10-20 13:04:16,490 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 106016)
2025-10-20 13:04:16,500 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 105504)
2025-10-20 13:04:16,510 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 104992)
2025-10-20 13:04:16,520 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 104480)
2025-10-20 13:04:16,530 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 103968)
2025-10-20 13:04:16,540 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 103456)
2025-10-20 13:04:16,550 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 102944)
2025-10-20 13:04:16,560 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 102432)
2025-10-20 13:04:16,570 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 101920)
2025-10-20 13:04:16,580 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 101408)
2025-10-20 13:04:16,590 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 100896)
2025-10-20 13:04:16,600 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 100384)
2025-10-20 13:04:16,610 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 99872)
2025-10-20 13:04:16,620 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 99360)
2025-10-20 13:04:16,640 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 98848)
2025-10-20 13:04:16,650 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 98336)
2025-10-20 13:04:16,660 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 97824)
2025-10-20 13:04:16,670 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 97312)
2025-10-20 13:04:16,680 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 96800)
2025-10-20 13:04:16,689 - integration.integrations.grpc_client_integration - INFO - gRPC received audio_chunk bytes=682800 dtype=int16 shape=[] for session 1760979846.413692
2025-10-20 13:04:16,689 - integration.core.event_bus - DEBUG - EventBus: dispatch 'grpc.response.audio' to 1 subscriber(s)
2025-10-20 13:04:16,689 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'grpc.response.audio': <bound method SpeechPlaybackIntegration._on_audio_chunk of <integration.integrations.speech_playback_integration.SpeechPlaybackIntegration object at 0x114996ba0>>
2025-10-20 13:04:16,689 - integration.integrations.speech_playback_integration - INFO - 🔊 Получен аудио чанк: 682800 bytes, dtype=int16, shape=[], sr=None, ch=None для сессии 1760979846.413692
2025-10-20 13:04:16,690 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 96288)
2025-10-20 13:04:16,691 - integration.integrations.speech_playback_integration - INFO - 🔍 audio_chunk: sid=1760979846.413692, in_dtype='int16', dec_dtype=int16, shape=(341400,), min=-23760.000, max=24971.000, bytes=682800
2025-10-20 13:04:16,691 - modules.speech_playback.core.buffer - INFO - ✅ Чанк добавлен: chunk_4_1760979856691 (size: 341400, queue: 2)
2025-10-20 13:04:16,691 - modules.speech_playback.core.player - INFO - ✅ Аудио данные добавлены: chunk_4_1760979856691 (size: 341400)
2025-10-20 13:04:16,691 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: grpc.response.audio
2025-10-20 13:04:16,691 - integration.integrations.grpc_client_integration - INFO - gRPC received text_chunk len=85 for session 1760979846.413692
2025-10-20 13:04:16,691 - integration.core.event_bus - DEBUG - EventBus: dispatch 'grpc.response.text' to 0 subscriber(s)
2025-10-20 13:04:16,691 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: grpc.response.text
2025-10-20 13:04:16,700 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 95776)
2025-10-20 13:04:16,710 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 95264)
2025-10-20 13:04:16,720 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 94752)
2025-10-20 13:04:16,730 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 94240)
2025-10-20 13:04:16,740 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 93728)
2025-10-20 13:04:16,750 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 93216)
2025-10-20 13:04:16,760 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 92704)
2025-10-20 13:04:16,770 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 92192)
2025-10-20 13:04:16,780 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 91680)
2025-10-20 13:04:16,800 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 91168)
2025-10-20 13:04:16,810 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 90656)
2025-10-20 13:04:16,820 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 90144)
2025-10-20 13:04:16,830 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 89632)
2025-10-20 13:04:16,840 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 89120)
2025-10-20 13:04:16,850 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 88608)
2025-10-20 13:04:16,860 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 88096)
2025-10-20 13:04:16,870 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 87584)
2025-10-20 13:04:16,880 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 87072)
2025-10-20 13:04:16,890 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 86560)
2025-10-20 13:04:16,900 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 86048)
2025-10-20 13:04:16,910 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 85536)
2025-10-20 13:04:16,920 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 85024)
2025-10-20 13:04:16,930 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 84512)
2025-10-20 13:04:16,940 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 84000)
2025-10-20 13:04:16,960 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 83488)
2025-10-20 13:04:16,970 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 82976)
2025-10-20 13:04:16,980 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 82464)
2025-10-20 13:04:16,990 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 81952)
2025-10-20 13:04:17,000 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 81440)
2025-10-20 13:04:17,010 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 80928)
2025-10-20 13:04:17,020 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 80416)
2025-10-20 13:04:17,030 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 79904)
2025-10-20 13:04:17,040 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 79392)
2025-10-20 13:04:17,050 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 78880)
2025-10-20 13:04:17,060 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 78368)
2025-10-20 13:04:17,070 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 77856)
2025-10-20 13:04:17,080 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 77344)
2025-10-20 13:04:17,090 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 76832)
2025-10-20 13:04:17,100 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 76320)
2025-10-20 13:04:17,120 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 75808)
2025-10-20 13:04:17,130 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 75296)
2025-10-20 13:04:17,140 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 74784)
2025-10-20 13:04:17,150 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 74272)
2025-10-20 13:04:17,160 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 73760)
2025-10-20 13:04:17,170 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 73248)
2025-10-20 13:04:17,180 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 72736)
2025-10-20 13:04:17,190 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 72224)
2025-10-20 13:04:17,200 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 71712)
2025-10-20 13:04:17,210 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 71200)
2025-10-20 13:04:17,220 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 70688)
2025-10-20 13:04:17,230 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 70176)
2025-10-20 13:04:17,240 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 69664)
2025-10-20 13:04:17,250 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 69152)
2025-10-20 13:04:17,260 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 68640)
2025-10-20 13:04:17,280 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 68128)
2025-10-20 13:04:17,290 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 67616)
2025-10-20 13:04:17,300 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 67104)
2025-10-20 13:04:17,310 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 66592)
2025-10-20 13:04:17,320 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 66080)
2025-10-20 13:04:17,330 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 65568)
2025-10-20 13:04:17,340 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 65056)
2025-10-20 13:04:17,350 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 64544)
2025-10-20 13:04:17,356 - integration.integrations.grpc_client_integration - INFO - gRPC received audio_chunk bytes=591600 dtype=int16 shape=[] for session 1760979846.413692
2025-10-20 13:04:17,357 - integration.core.event_bus - DEBUG - EventBus: dispatch 'grpc.response.audio' to 1 subscriber(s)
2025-10-20 13:04:17,357 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'grpc.response.audio': <bound method SpeechPlaybackIntegration._on_audio_chunk of <integration.integrations.speech_playback_integration.SpeechPlaybackIntegration object at 0x114996ba0>>
2025-10-20 13:04:17,357 - integration.integrations.speech_playback_integration - INFO - 🔊 Получен аудио чанк: 591600 bytes, dtype=int16, shape=[], sr=None, ch=None для сессии 1760979846.413692
2025-10-20 13:04:17,357 - integration.integrations.speech_playback_integration - INFO - 🔍 audio_chunk: sid=1760979846.413692, in_dtype='int16', dec_dtype=int16, shape=(295800,), min=-24204.000, max=22379.000, bytes=591600
2025-10-20 13:04:17,357 - modules.speech_playback.core.buffer - INFO - ✅ Чанк добавлен: chunk_5_1760979857357 (size: 295800, queue: 3)
2025-10-20 13:04:17,357 - modules.speech_playback.core.player - INFO - ✅ Аудио данные добавлены: chunk_5_1760979857357 (size: 295800)
2025-10-20 13:04:17,357 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: grpc.response.audio
2025-10-20 13:04:17,357 - integration.integrations.grpc_client_integration - INFO - gRPC received text_chunk len=72 for session 1760979846.413692
2025-10-20 13:04:17,357 - integration.core.event_bus - DEBUG - EventBus: dispatch 'grpc.response.text' to 0 subscriber(s)
2025-10-20 13:04:17,357 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: grpc.response.text
2025-10-20 13:04:17,360 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 64032)
2025-10-20 13:04:17,370 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 63520)
2025-10-20 13:04:17,380 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 63008)
2025-10-20 13:04:17,390 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 62496)
2025-10-20 13:04:17,400 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 61984)
2025-10-20 13:04:17,410 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 61472)
2025-10-20 13:04:17,420 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 60960)
2025-10-20 13:04:17,440 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 60448)
2025-10-20 13:04:17,450 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 59936)
2025-10-20 13:04:17,460 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 59424)
2025-10-20 13:04:17,470 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 58912)
2025-10-20 13:04:17,480 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 58400)
2025-10-20 13:04:17,490 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 57888)
2025-10-20 13:04:17,500 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 57376)
2025-10-20 13:04:17,510 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 56864)
2025-10-20 13:04:17,520 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 56352)
2025-10-20 13:04:17,530 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 55840)
2025-10-20 13:04:17,540 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 55328)
2025-10-20 13:04:17,550 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 54816)
2025-10-20 13:04:17,560 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 54304)
2025-10-20 13:04:17,570 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 53792)
2025-10-20 13:04:17,580 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 53280)
2025-10-20 13:04:17,600 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 52768)
2025-10-20 13:04:17,610 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 52256)
2025-10-20 13:04:17,620 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 51744)
2025-10-20 13:04:17,630 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 51232)
2025-10-20 13:04:17,640 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 50720)
2025-10-20 13:04:17,650 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 50208)
2025-10-20 13:04:17,660 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 49696)
2025-10-20 13:04:17,670 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 49184)
2025-10-20 13:04:17,680 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 48672)
2025-10-20 13:04:17,690 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 48160)
2025-10-20 13:04:17,700 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 47648)
2025-10-20 13:04:17,710 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 47136)
2025-10-20 13:04:17,720 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 46624)
2025-10-20 13:04:17,730 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 46112)
2025-10-20 13:04:17,740 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 45600)
2025-10-20 13:04:17,760 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 45088)
2025-10-20 13:04:17,770 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 44576)
2025-10-20 13:04:17,780 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 44064)
2025-10-20 13:04:17,790 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 43552)
2025-10-20 13:04:17,800 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 43040)
2025-10-20 13:04:17,810 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 42528)
2025-10-20 13:04:17,820 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 42016)
2025-10-20 13:04:17,830 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 41504)
2025-10-20 13:04:17,840 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 40992)
2025-10-20 13:04:17,850 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 40480)
2025-10-20 13:04:17,860 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 39968)
2025-10-20 13:04:17,870 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 39456)
2025-10-20 13:04:17,880 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 38944)
2025-10-20 13:04:17,890 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 38432)
2025-10-20 13:04:17,900 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 37920)
2025-10-20 13:04:17,919 - integration.integrations.grpc_client_integration - DEBUG - gRPC stream progress: 10 chunks received
2025-10-20 13:04:17,919 - integration.integrations.grpc_client_integration - INFO - gRPC received audio_chunk bytes=579600 dtype=int16 shape=[] for session 1760979846.413692
2025-10-20 13:04:17,920 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 37408)
2025-10-20 13:04:17,920 - integration.core.event_bus - DEBUG - EventBus: dispatch 'grpc.response.audio' to 1 subscriber(s)
2025-10-20 13:04:17,920 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'grpc.response.audio': <bound method SpeechPlaybackIntegration._on_audio_chunk of <integration.integrations.speech_playback_integration.SpeechPlaybackIntegration object at 0x114996ba0>>
2025-10-20 13:04:17,920 - integration.integrations.speech_playback_integration - INFO - 🔊 Получен аудио чанк: 579600 bytes, dtype=int16, shape=[], sr=None, ch=None для сессии 1760979846.413692
2025-10-20 13:04:17,921 - integration.integrations.speech_playback_integration - INFO - 🔍 audio_chunk: sid=1760979846.413692, in_dtype='int16', dec_dtype=int16, shape=(289800,), min=-22417.000, max=18555.000, bytes=579600
2025-10-20 13:04:17,921 - modules.speech_playback.core.buffer - INFO - ✅ Чанк добавлен: chunk_6_1760979857921 (size: 289800, queue: 4)
2025-10-20 13:04:17,922 - modules.speech_playback.core.player - INFO - ✅ Аудио данные добавлены: chunk_6_1760979857921 (size: 289800)
2025-10-20 13:04:17,922 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: grpc.response.audio
2025-10-20 13:04:17,922 - integration.integrations.grpc_client_integration - INFO - gRPC received text_chunk len=200 for session 1760979846.413692
2025-10-20 13:04:17,922 - integration.core.event_bus - DEBUG - EventBus: dispatch 'grpc.response.text' to 0 subscriber(s)
2025-10-20 13:04:17,922 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: grpc.response.text
2025-10-20 13:04:17,930 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 36896)
2025-10-20 13:04:17,935 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Quartz tap вызван: event_type=10
2025-10-20 13:04:17,935 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Keycode=49, target=49
2025-10-20 13:04:17,935 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔑 Целевая клавиша обнаружена! keycode=49
2025-10-20 13:04:17,935 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔽 Quartz tap: keyDown detected for target key
2025-10-20 13:04:17,935 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔑 _trigger_event: type=press, duration=0.000s, thread=MainThread
2025-10-20 13:04:17,935 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔑 _run_callback: press, callback=_handle_press
🔑 _run_callback: press, callback=_handle_press
2025-10-20 13:04:17,935 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔑 Выполняем async callback в loop: press
🔑 Выполняем async callback в loop: press
2025-10-20 13:04:17,936 - integration.integrations.input_processing_integration - INFO - 🎤 PTT: keyDown(space) → PRESS, timestamp=1760979857.935262
2025-10-20 13:04:17,936 - integration.integrations.input_processing_integration - DEBUG - PRESS: current_session=1760979846.413692, pending_session=None, recognized=True, recording=False
🔑 PRESS EVENT: 1760979857.935262 - начинаем запись
2025-10-20 13:04:17,936 - integration.integrations.input_processing_integration - DEBUG - PRESS: сохранён session_id для отмены: 1760979846.413692
2025-10-20 13:04:17,936 - integration.integrations.input_processing_integration - DEBUG - PRESS: pending_session_id=1760979857.935262
2025-10-20 13:04:17,936 - integration.core.event_bus - DEBUG - EventBus: dispatch 'keyboard.press' to 1 subscriber(s)
2025-10-20 13:04:17,936 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'keyboard.press': <bound method VoiceOverDuckingIntegration.handle_keyboard_press of <integration.integrations.voiceover_ducking_integration.VoiceOverDuckingIntegration object at 0x1149978c0>>
I0000 00:00:1760979857.937414 2294936 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
 2025-10-20 13:04:17,954 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 36384)
2025-10-20 13:04:17,965 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 35872)
2025-10-20 13:04:17,975 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 35360)
2025-10-20 13:04:17,985 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 34848)
2025-10-20 13:04:17,987 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Quartz tap вызван: event_type=11
2025-10-20 13:04:17,987 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Keycode=49, target=49
2025-10-20 13:04:17,987 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔑 Целевая клавиша обнаружена! keycode=49
2025-10-20 13:04:17,987 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - Quartz tap: keyUp detected for target key
2025-10-20 13:04:17,987 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔑 PTT: keyUp → short_press, duration=0.052s, _long_sent=False, thread=MainThread
2025-10-20 13:04:17,987 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - Quartz keyUp: duration=0.052s, _long_sent=False → short_press
2025-10-20 13:04:17,987 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔑 _trigger_event: type=short_press, duration=0.052s, thread=MainThread
2025-10-20 13:04:17,988 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔑 _run_callback: short_press, callback=_handle_short_press
🔑 _run_callback: short_press, callback=_handle_short_press
2025-10-20 13:04:17,988 - modules.input_processing.keyboard.mac.quartz_monitor - INFO - 🔑 Выполняем async callback в loop: short_press
🔑 Выполняем async callback в loop: short_press
2025-10-20 13:04:17,988 - integration.integrations.input_processing_integration - DEBUG - 🔑 SHORT_PRESS: 0.052с
2025-10-20 13:04:17,988 - integration.integrations.input_processing_integration - DEBUG - SHORT_PRESS: запрашиваем отмену активного gRPC стрима (отмена)
2025-10-20 13:04:17,988 - integration.core.event_bus - DEBUG - EventBus: dispatch 'grpc.request_cancel' to 2 subscriber(s)
2025-10-20 13:04:17,989 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'grpc.request_cancel': <bound method SpeechPlaybackIntegration._on_grpc_cancel of <integration.integrations.speech_playback_integration.SpeechPlaybackIntegration object at 0x114996ba0>>
2025-10-20 13:04:17,989 - integration.integrations.speech_playback_integration - INFO - SpeechPlayback: получен grpc.request_cancel — очищаем буфер
2025-10-20 13:04:17,989 - modules.speech_playback.core.buffer - INFO - 🧹 Очередь очищена: 4 чанков
2025-10-20 13:04:17,989 - modules.speech_playback.core.buffer - INFO - 🧹 Буфер воспроизведения очищен: 34848 фреймов
2025-10-20 13:04:17,989 - modules.speech_playback.core.buffer - INFO - 🧹 Все буферы очищены
2025-10-20 13:04:17,989 - modules.speech_playback.core.buffer - INFO - 🧹 Очередь очищена: 0 чанков
2025-10-20 13:04:17,989 - modules.speech_playback.core.buffer - INFO - 🧹 Буфер воспроизведения очищен: 0 фреймов
2025-10-20 13:04:17,989 - modules.speech_playback.core.buffer - INFO - 🧹 Все буферы очищены
2025-10-20 13:04:17,989 - modules.speech_playback.core.player - INFO - ⏹️ Прерывание чанка chunk_2_1760979855849 по stop_event
2025-10-20 13:04:17,989 - modules.speech_playback.core.buffer - DEBUG - ✅ Чанк завершен: chunk_2_1760979855849
2025-10-20 13:04:17,989 - modules.speech_playback.core.player - INFO - ✅ Чанк обработан: chunk_2_1760979855849
2025-10-20 13:04:17,989 - modules.speech_playback.core.player - INFO - 🔄 Playback loop завершен
2025-10-20 13:04:17,989 - integration.integrations.speech_playback_integration - INFO - SpeechPlayback: _on_player_completed для сессии 1760979846.413692, grpc_done=False, finalized=False
2025-10-20 13:04:17,989 - integration.integrations.speech_playback_integration - DEBUG - SpeechPlayback: пропускаем завершение для сессии 1760979846.413692 (grpc_done=False, finalized=False)
2025-10-20 13:04:18,123 - modules.speech_playback.core.player - INFO - 🛑 Аудио поток остановлен
2025-10-20 13:04:18,123 - modules.speech_playback.core.player - INFO - 🛑 Воспроизведение остановлено
2025-10-20 13:04:18,123 - integration.core.event_bus - DEBUG - EventBus: dispatch 'playback.cancelled' to 3 subscriber(s)
2025-10-20 13:04:18,123 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'playback.cancelled': <bound method SpeechPlaybackIntegration._on_unified_interrupt of <integration.integrations.speech_playback_integration.SpeechPlaybackIntegration object at 0x114996ba0>>
2025-10-20 13:04:18,123 - integration.integrations.speech_playback_integration - INFO - SpeechPlayback: ЕДИНЫЙ канал прерывания, source=grpc_cancel, reason=interrupt
2025-10-20 13:04:18,123 - integration.integrations.speech_playback_integration - INFO - SpeechPlayback: прерывание обработано через ЕДИНЫЙ канал
2025-10-20 13:04:18,123 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'playback.cancelled': <bound method InputProcessingIntegration._on_playback_finished of <integration.integrations.input_processing_integration.InputProcessingIntegration object at 0x114995160>>
2025-10-20 13:04:18,123 - integration.integrations.input_processing_integration - DEBUG - PLAYBACK: finished (event=playback.cancelled, session=1760979846.413692)
2025-10-20 13:04:18,123 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'playback.cancelled': <bound method SignalIntegration._on_playback_cancelled of <integration.integrations.signal_integration.SignalIntegration object at 0x114996e40>>
2025-10-20 13:04:18,123 - integration.integrations.signal_integration - DEBUG - Signals: CANCEL skipped (reason=grpc_cancel)
2025-10-20 13:04:18,123 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: playback.cancelled
2025-10-20 13:04:18,123 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'grpc.request_cancel': <bound method GrpcClientIntegration._on_request_cancel of <integration.integrations.grpc_client_integration.GrpcClientIntegration object at 0x114996900>>
2025-10-20 13:04:18,123 - integration.core.event_bus - DEBUG - EventBus: dispatch 'grpc.request_failed' to 4 subscriber(s)
2025-10-20 13:04:18,123 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'grpc.request_failed': <bound method InputProcessingIntegration._on_grpc_failed of <integration.integrations.input_processing_integration.InputProcessingIntegration object at 0x114995160>>
2025-10-20 13:04:18,123 - integration.integrations.input_processing_integration - DEBUG - gRPC failed for session 1760979846.413692
2025-10-20 13:04:18,123 - integration.integrations.input_processing_integration - DEBUG - SESSION RESET (grpc_failed)
2025-10-20 13:04:18,123 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'grpc.request_failed': <bound method SpeechPlaybackIntegration._on_grpc_failed of <integration.integrations.speech_playback_integration.SpeechPlaybackIntegration object at 0x114996ba0>>
2025-10-20 13:04:18,123 - modules.speech_playback.core.player - WARNING - ⚠️ Невозможно остановить воспроизведение в текущем состоянии
2025-10-20 13:04:18,123 - integration.core.event_bus - DEBUG - EventBus: dispatch 'playback.failed' to 3 subscriber(s)
2025-10-20 13:04:18,123 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'playback.failed': <bound method ProcessingWorkflow._on_playback_failed of <integration.workflows.processing_workflow.ProcessingWorkflow object at 0x11498c050>>
2025-10-20 13:04:18,123 - integration.workflows.processing_workflow - ERROR - 🔊 ProcessingWorkflow: ошибка воспроизведения - cancelled
2025-10-20 13:04:18,123 - integration.workflows.processing_workflow - ERROR - ❌ ProcessingWorkflow: обработка ошибки playback_error_cancelled на этапе capturing
2025-10-20 13:04:18,123 - integration.workflows.processing_workflow - INFO - ⚙️ ProcessingWorkflow: возврат в SLEEPING, reason=error_playback_error_cancelled
2025-10-20 13:04:18,123 - integration.core.event_bus - DEBUG - EventBus: dispatch 'mode.request' to 1 subscriber(s)
2025-10-20 13:04:18,123 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'mode.request': <bound method ModeManagementIntegration._on_mode_request of <integration.integrations.mode_management_integration.ModeManagementIntegration object at 0x1149963c0>>
2025-10-20 13:04:18,123 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: mode.request
2025-10-20 13:04:18,123 - integration.workflows.base_workflow - DEBUG - 🔄 ProcessingWorkflow: запрос смены режима sleeping
2025-10-20 13:04:18,123 - integration.workflows.processing_workflow - DEBUG - ⚙️ ProcessingWorkflow: состояние очищено
2025-10-20 13:04:18,123 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'playback.failed': <bound method InputProcessingIntegration._on_playback_finished of <integration.integrations.input_processing_integration.InputProcessingIntegration object at 0x114995160>>
2025-10-20 13:04:18,123 - integration.integrations.input_processing_integration - DEBUG - PLAYBACK: finished (event=playback.failed, session=1760979846.413692)
2025-10-20 13:04:18,123 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'playback.failed': <bound method ModeManagementIntegration._bridge_playback_done of <integration.integrations.mode_management_integration.ModeManagementIntegration object at 0x1149963c0>>
2025-10-20 13:04:18,124 - integration.core.event_bus - DEBUG - EventBus: dispatch 'mode.request' to 1 subscriber(s)
2025-10-20 13:04:18,124 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'mode.request': <bound method ModeManagementIntegration._on_mode_request of <integration.integrations.mode_management_integration.ModeManagementIntegration object at 0x1149963c0>>
2025-10-20 13:04:18,124 - integration.core.state_manager - INFO - 🔄 Режим изменен: processing → sleeping
2025-10-20 13:04:18,124 - integration.core.state_manager - INFO - 🎯 TRAY DEBUG: set_mode() готов публиковать app.mode_changed: AppMode.SLEEPING
2025-10-20 13:04:18,124 - integration.core.state_manager - INFO - 🎯 TRAY DEBUG: EventBus подключен: True
2025-10-20 13:04:18,124 - integration.core.state_manager - INFO - 🔄 StateManager: начинаем публикацию событий (EventBus подключен, eb_loop=4635880784)
2025-10-20 13:04:18,124 - integration.core.state_manager - INFO - 🔄 StateManager: публикуем через run_coroutine_threadsafe на loop EventBus (без ожидания)
2025-10-20 13:04:18,124 - integration.core.state_manager - INFO - ✅ StateManager: события опубликованы успешно
2025-10-20 13:04:18,124 - mode_management.core.mode_controller - INFO - ✅ Режим изменен: processing → sleeping
2025-10-20 13:04:18,124 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: mode.request
2025-10-20 13:04:18,124 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: playback.failed
2025-10-20 13:04:18,124 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'grpc.request_failed': <bound method ProcessingWorkflow._on_grpc_failed of <integration.workflows.processing_workflow.ProcessingWorkflow object at 0x11498c050>>
2025-10-20 13:04:18,124 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'grpc.request_failed': <bound method SignalIntegration._on_error_like of <integration.integrations.signal_integration.SignalIntegration object at 0x114996e40>>
2025-10-20 13:04:18,124 - integration.integrations.signal_integration - INFO - Signals: ERROR (failure event)
2025-10-20 13:04:18,126 - integration.core.event_bus - DEBUG - EventBus: dispatch 'playback.signal' to 1 subscriber(s)
2025-10-20 13:04:18,126 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'playback.signal': <bound method SpeechPlaybackIntegration._on_playback_signal of <integration.integrations.speech_playback_integration.SpeechPlaybackIntegration object at 0x114996ba0>>
2025-10-20 13:04:18,126 - integration.integrations.speech_playback_integration - INFO - 🔔 playback.signal: pattern=error, bytes=11520, sr=48000, ch=1, gain=1.0, prio=0
2025-10-20 13:04:18,126 - modules.speech_playback.core.player - INFO - 🎯 [AUDIO_REFACTOR] Начало инициализации Sequential Speech Player...
2025-10-20 13:04:18,126 - modules.speech_playback.core.player - DEBUG - 🔍 [AUDIO_DEBUG] Инициализация Core Audio Manager...
2025-10-20 13:04:18,126 - modules.speech_playback.macos.core_audio - INFO - ✅ Core Audio инициализирован
2025-10-20 13:04:18,127 - modules.speech_playback.core.player - INFO - ✅ [AUDIO_SUCCESS] Core Audio Manager инициализирован
2025-10-20 13:04:18,127 - modules.speech_playback.core.player - INFO - 🎯 Используем системное устройство по умолчанию от macOS
2025-10-20 13:04:18,127 - modules.speech_playback.core.player - INFO - 📊 [AUDIO_STATS] Конфигурация плеера: sample_rate=48000Hz, channels=1, dtype=int16
2025-10-20 13:04:18,127 - modules.speech_playback.macos.performance - INFO - ✅ Мониторинг производительности запущен
2025-10-20 13:04:18,127 - modules.speech_playback.core.player - INFO - ✅ [AUDIO_SUCCESS] Sequential Speech Player инициализирован успешно
2025-10-20 13:04:18,129 - modules.speech_playback.core.player - INFO - 🔧 Аудио поток создан (device: системный дефолт, channels: 1)
2025-10-20 13:04:18,129 - modules.speech_playback.core.player - DEBUG - 💡 Поток будет стартован при появлении первого чанка (lazy start)
2025-10-20 13:04:18,129 - modules.speech_playback.core.player - INFO - 🔄 Playback loop запущен
2025-10-20 13:04:18,129 - modules.speech_playback.core.player - INFO - 🎵 Воспроизведение запущено
2025-10-20 13:04:18,129 - integration.core.event_bus - DEBUG - EventBus: dispatch 'playback.started' to 2 subscriber(s)
2025-10-20 13:04:18,129 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'playback.started': <bound method ProcessingWorkflow._on_playback_started of <integration.workflows.processing_workflow.ProcessingWorkflow object at 0x11498c050>>
2025-10-20 13:04:18,129 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'playback.started': <bound method InputProcessingIntegration._on_playback_started of <integration.integrations.input_processing_integration.InputProcessingIntegration object at 0x114995160>>
2025-10-20 13:04:18,130 - integration.integrations.input_processing_integration - DEBUG - PLAYBACK: started (session=None)
2025-10-20 13:04:18,130 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: playback.started
2025-10-20 13:04:18,130 - modules.speech_playback.core.buffer - INFO - ✅ Чанк добавлен: chunk_7_1760979858130 (size: 5760, queue: 1)
2025-10-20 13:04:18,130 - modules.speech_playback.core.buffer - DEBUG - 🔍 Получен чанк: chunk_7_1760979858130
2025-10-20 13:04:18,130 - modules.speech_playback.core.buffer - INFO - ✅ Чанк добавлен в буфер: chunk_7_1760979858130 (frames: 5760, buffer: 0 → 5760, ch=1)
2025-10-20 13:04:18,629 - modules.speech_playback.core.player - INFO - ▶️ Аудио поток стартован (lazy start)
2025-10-20 13:04:18,629 - modules.speech_playback.core.player - INFO - ✅ Аудио данные добавлены: chunk_7_1760979858130 (size: 5760)
2025-10-20 13:04:18,629 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: playback.signal
2025-10-20 13:04:18,629 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: grpc.request_failed
2025-10-20 13:04:18,629 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: grpc.request_cancel
2025-10-20 13:04:18,632 - integration.core.event_bus - DEBUG - EventBus: dispatch 'grpc.request_failed' to 4 subscriber(s)
2025-10-20 13:04:18,632 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'grpc.request_failed': <bound method InputProcessingIntegration._on_grpc_failed of <integration.integrations.input_processing_integration.InputProcessingIntegration object at 0x114995160>>
2025-10-20 13:04:18,632 - integration.integrations.input_processing_integration - DEBUG - gRPC failed for session 1760979846.413692, ignored (current=None, active=None)
2025-10-20 13:04:18,632 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'grpc.request_failed': <bound method SpeechPlaybackIntegration._on_grpc_failed of <integration.integrations.speech_playback_integration.SpeechPlaybackIntegration object at 0x114996ba0>>
2025-10-20 13:04:18,632 - modules.speech_playback.core.buffer - INFO - 🧹 Очередь очищена: 0 чанков
2025-10-20 13:04:18,632 - modules.speech_playback.core.buffer - INFO - 🧹 Буфер воспроизведения очищен: 5760 фреймов
2025-10-20 13:04:18,632 - modules.speech_playback.core.buffer - INFO - 🧹 Все буферы очищены
2025-10-20 13:04:18,640 - modules.speech_playback.core.player - INFO - ⏹️ Прерывание чанка chunk_7_1760979858130 по stop_event
2025-10-20 13:04:18,640 - modules.speech_playback.core.buffer - DEBUG - ✅ Чанк завершен: chunk_7_1760979858130
2025-10-20 13:04:18,640 - modules.speech_playback.core.player - INFO - ✅ Чанк обработан: chunk_7_1760979858130
2025-10-20 13:04:18,640 - modules.speech_playback.core.player - INFO - 🔄 Playback loop завершен
2025-10-20 13:04:18,640 - integration.integrations.speech_playback_integration - INFO - SpeechPlayback: _on_player_completed для сессии 1760979846.413692, grpc_done=True, finalized=True
2025-10-20 13:04:18,640 - integration.integrations.speech_playback_integration - DEBUG - SpeechPlayback: пропускаем завершение для сессии 1760979846.413692 (grpc_done=True, finalized=True)
2025-10-20 13:04:18,768 - modules.speech_playback.core.player - INFO - 🛑 Аудио поток остановлен
2025-10-20 13:04:18,768 - modules.speech_playback.core.player - INFO - 🛑 Воспроизведение остановлено
2025-10-20 13:04:18,768 - integration.core.event_bus - DEBUG - EventBus: dispatch 'playback.failed' to 3 subscriber(s)
2025-10-20 13:04:18,768 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'playback.failed': <bound method ProcessingWorkflow._on_playback_failed of <integration.workflows.processing_workflow.ProcessingWorkflow object at 0x11498c050>>
2025-10-20 13:04:18,768 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'playback.failed': <bound method InputProcessingIntegration._on_playback_finished of <integration.integrations.input_processing_integration.InputProcessingIntegration object at 0x114995160>>
2025-10-20 13:04:18,768 - integration.integrations.input_processing_integration - DEBUG - PLAYBACK: finished (event=playback.failed, session=1760979846.413692)
2025-10-20 13:04:18,768 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'playback.failed': <bound method ModeManagementIntegration._bridge_playback_done of <integration.integrations.mode_management_integration.ModeManagementIntegration object at 0x1149963c0>>
2025-10-20 13:04:18,768 - integration.core.event_bus - DEBUG - EventBus: dispatch 'mode.request' to 1 subscriber(s)
2025-10-20 13:04:18,768 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'mode.request': <bound method ModeManagementIntegration._on_mode_request of <integration.integrations.mode_management_integration.ModeManagementIntegration object at 0x1149963c0>>
2025-10-20 13:04:18,768 - integration.integrations.mode_management_integration - DEBUG - Mode request ignored (same mode): AppMode.SLEEPING
2025-10-20 13:04:18,768 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: mode.request
2025-10-20 13:04:18,768 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: playback.failed
2025-10-20 13:04:18,768 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'grpc.request_failed': <bound method ProcessingWorkflow._on_grpc_failed of <integration.workflows.processing_workflow.ProcessingWorkflow object at 0x11498c050>>
2025-10-20 13:04:18,768 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'grpc.request_failed': <bound method SignalIntegration._on_error_like of <integration.integrations.signal_integration.SignalIntegration object at 0x114996e40>>
2025-10-20 13:04:18,768 - integration.integrations.signal_integration - INFO - Signals: ERROR (failure event)
2025-10-20 13:04:18,771 - integration.core.event_bus - DEBUG - EventBus: dispatch 'playback.signal' to 1 subscriber(s)
2025-10-20 13:04:18,771 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'playback.signal': <bound method SpeechPlaybackIntegration._on_playback_signal of <integration.integrations.speech_playback_integration.SpeechPlaybackIntegration object at 0x114996ba0>>
2025-10-20 13:04:18,771 - integration.integrations.speech_playback_integration - INFO - 🔔 playback.signal: pattern=error, bytes=11520, sr=48000, ch=1, gain=1.0, prio=0
2025-10-20 13:04:18,771 - modules.speech_playback.core.player - INFO - 🎯 [AUDIO_REFACTOR] Начало инициализации Sequential Speech Player...
2025-10-20 13:04:18,771 - modules.speech_playback.core.player - DEBUG - 🔍 [AUDIO_DEBUG] Инициализация Core Audio Manager...
2025-10-20 13:04:18,771 - modules.speech_playback.macos.core_audio - INFO - ✅ Core Audio инициализирован
2025-10-20 13:04:18,771 - modules.speech_playback.core.player - INFO - ✅ [AUDIO_SUCCESS] Core Audio Manager инициализирован
2025-10-20 13:04:18,771 - modules.speech_playback.core.player - INFO - 🎯 Используем системное устройство по умолчанию от macOS
2025-10-20 13:04:18,771 - modules.speech_playback.core.player - INFO - 📊 [AUDIO_STATS] Конфигурация плеера: sample_rate=48000Hz, channels=1, dtype=int16
2025-10-20 13:04:18,771 - modules.speech_playback.macos.performance - WARNING - ⚠️ Мониторинг уже запущен
2025-10-20 13:04:18,771 - modules.speech_playback.core.player - INFO - ✅ [AUDIO_SUCCESS] Sequential Speech Player инициализирован успешно
2025-10-20 13:04:18,774 - modules.speech_playback.core.player - INFO - 🔧 Аудио поток создан (device: системный дефолт, channels: 1)
2025-10-20 13:04:18,774 - modules.speech_playback.core.player - DEBUG - 💡 Поток будет стартован при появлении первого чанка (lazy start)
2025-10-20 13:04:18,774 - modules.speech_playback.core.player - INFO - 🔄 Playback loop запущен
2025-10-20 13:04:18,774 - modules.speech_playback.core.player - INFO - 🎵 Воспроизведение запущено
2025-10-20 13:04:18,774 - integration.core.event_bus - DEBUG - EventBus: dispatch 'playback.started' to 2 subscriber(s)
2025-10-20 13:04:18,774 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'playback.started': <bound method ProcessingWorkflow._on_playback_started of <integration.workflows.processing_workflow.ProcessingWorkflow object at 0x11498c050>>
2025-10-20 13:04:18,774 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'playback.started': <bound method InputProcessingIntegration._on_playback_started of <integration.integrations.input_processing_integration.InputProcessingIntegration object at 0x114995160>>
2025-10-20 13:04:18,774 - integration.integrations.input_processing_integration - DEBUG - PLAYBACK: started (session=None)
2025-10-20 13:04:18,774 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: playback.started
2025-10-20 13:04:18,774 - modules.speech_playback.core.buffer - INFO - ✅ Чанк добавлен: chunk_8_1760979858774 (size: 5760, queue: 1)
2025-10-20 13:04:18,774 - modules.speech_playback.core.buffer - DEBUG - 🔍 Получен чанк: chunk_8_1760979858774
2025-10-20 13:04:18,774 - modules.speech_playback.core.buffer - INFO - ✅ Чанк добавлен в буфер: chunk_8_1760979858774 (frames: 5760, buffer: 0 → 5760, ch=1)
2025-10-20 13:04:19,204 - modules.speech_playback.core.player - INFO - ▶️ Аудио поток стартован (lazy start)
2025-10-20 13:04:19,204 - modules.speech_playback.core.player - INFO - ✅ Аудио данные добавлены: chunk_8_1760979858774 (size: 5760)
2025-10-20 13:04:19,204 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: playback.signal
2025-10-20 13:04:19,204 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: grpc.request_failed
2025-10-20 13:04:19,204 - integration.workflows.processing_workflow - DEBUG - ⚙️ ProcessingWorkflow: мониторинг этапа capturing отменен
2025-10-20 13:04:19,204 - integration.workflows.processing_workflow - DEBUG - ⚙️ ProcessingWorkflow: общий мониторинг отменен
2025-10-20 13:04:19,205 - modules.voiceover_control.core.controller - DEBUG - VoiceOverController: Updated status - currently running: False
2025-10-20 13:04:19,205 - modules.voiceover_control.core.controller - DEBUG - VoiceOverController: VoiceOver is not currently running, skipping duck (reason=keyboard.press)
2025-10-20 13:04:19,205 - integration.integrations.voiceover_ducking_integration - DEBUG - VoiceOverDuckingIntegration: Ducking on keyboard press
2025-10-20 13:04:19,205 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: keyboard.press
2025-10-20 13:04:19,205 - integration.core.event_bus - DEBUG - EventBus: dispatch 'mode.request' to 1 subscriber(s)
2025-10-20 13:04:19,205 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'mode.request': <bound method ModeManagementIntegration._on_mode_request of <integration.integrations.mode_management_integration.ModeManagementIntegration object at 0x1149963c0>>
2025-10-20 13:04:19,205 - integration.integrations.mode_management_integration - DEBUG - Mode request ignored (same mode): AppMode.SLEEPING
2025-10-20 13:04:19,205 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: mode.request
2025-10-20 13:04:19,205 - integration.integrations.input_processing_integration - INFO - SHORT_PRESS: запрос на SLEEPING отправлен (отмена без записи)
2025-10-20 13:04:19,205 - integration.core.state_manager - INFO - 🎯 TRAY DEBUG: StateManager публикует app.mode_changed: AppMode.SLEEPING (type: <enum 'AppMode'>)
2025-10-20 13:04:19,205 - integration.core.state_manager - INFO - 🎯 TRAY DEBUG: StateManager event_data: {'mode': <AppMode.SLEEPING: 'sleeping'>}
2025-10-20 13:04:19,205 - integration.core.event_bus - INFO - EventBus: 'app.mode_changed' → subscribers=9, data={'mode': <AppMode.SLEEPING: 'sleeping'>}
2025-10-20 13:04:19,205 - integration.core.event_bus - DEBUG - EventBus: dispatch 'app.mode_changed' to 9 subscriber(s)
2025-10-20 13:04:19,205 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method TrayControllerIntegration._on_mode_changed of <integration.integrations.tray_controller_integration.TrayControllerIntegration object at 0x114994ec0>>
2025-10-20 13:04:19,205 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method ScreenshotCaptureIntegration._on_mode_changed of <integration.integrations.screenshot_capture_integration.ScreenshotCaptureIntegration object at 0x114995e80>>
2025-10-20 13:04:19,205 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method ModeManagementIntegration._on_app_mode_changed of <integration.integrations.mode_management_integration.ModeManagementIntegration object at 0x1149963c0>>
2025-10-20 13:04:19,205 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method ProcessingWorkflow._on_mode_changed of <integration.workflows.processing_workflow.ProcessingWorkflow object at 0x11498c050>>
2025-10-20 13:04:19,205 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method VoiceRecognitionIntegration._on_app_mode_changed of <integration.integrations.voice_recognition_integration.VoiceRecognitionIntegration object at 0x114996270>>
2025-10-20 13:04:19,205 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method VoiceOverDuckingIntegration.handle_mode_change of <integration.integrations.voiceover_ducking_integration.VoiceOverDuckingIntegration object at 0x1149978c0>>
2025-10-20 13:04:19,205 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method ListeningWorkflow._on_mode_changed of <integration.workflows.listening_workflow.ListeningWorkflow object at 0x114997e00>>
2025-10-20 13:04:19,205 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method SimpleModuleCoordinator._on_mode_changed of <integration.core.simple_module_coordinator.SimpleModuleCoordinator object at 0x1144cfa10>>
2025-10-20 13:04:19,205 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.mode_changed': <bound method UpdaterIntegration._on_mode_changed of <integration.integrations.updater_integration.UpdaterIntegration object at 0x1149952b0>>
2025-10-20 13:04:19,205 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: app.mode_changed
2025-10-20 13:04:19,205 - integration.core.state_manager - INFO - 🎯 TRAY DEBUG: StateManager app.mode_changed опубликовано успешно
2025-10-20 13:04:19,205 - integration.core.state_manager - INFO - 🎯 TRAY DEBUG: StateManager подписчиков на app.mode_changed: 9
2025-10-20 13:04:19,205 - integration.core.state_manager - INFO - 🔄 StateManager: -> publish app.state_changed: AppMode.PROCESSING -> AppMode.SLEEPING
2025-10-20 13:04:19,205 - integration.core.event_bus - DEBUG - EventBus: dispatch 'app.state_changed' to 1 subscriber(s)
2025-10-20 13:04:19,205 - integration.core.event_bus - DEBUG - EventBus: create_task (fast) for 'app.state_changed': <bound method InterruptManagementIntegration._on_app_state_changed of <integration.integrations.interrupt_management_integration.InterruptManagementIntegration object at 0x114995d30>>
2025-10-20 13:04:19,205 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: app.state_changed
2025-10-20 13:04:19,205 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: _on_mode_changed ВЫЗВАН!
2025-10-20 13:04:19,205 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: event type=<class 'dict'>, event={'type': 'app.mode_changed', 'data': {'mode': <AppMode.SLEEPING: 'sleeping'>}, 'timestamp': 95610.279498208}
2025-10-20 13:04:19,205 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: data={'mode': <AppMode.SLEEPING: 'sleeping'>}
2025-10-20 13:04:19,205 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: new_mode=AppMode.SLEEPING (type: <enum 'AppMode'>)
2025-10-20 13:04:19,206 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: mode_to_status={<AppMode.SLEEPING: 'sleeping'>: <TrayStatus.SLEEPING: 'sleeping'>, <AppMode.LISTENING: 'listening'>: <TrayStatus.LISTENING: 'listening'>, <AppMode.PROCESSING: 'processing'>: <TrayStatus.PROCESSING: 'processing'>}
2025-10-20 13:04:19,206 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: new_mode in mapping? True
2025-10-20 13:04:19,206 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: key=AppMode.SLEEPING (type: <enum 'AppMode'>), equals new_mode? True
2025-10-20 13:04:19,206 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: key=AppMode.LISTENING (type: <enum 'AppMode'>), equals new_mode? False
2025-10-20 13:04:19,206 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: key=AppMode.PROCESSING (type: <enum 'AppMode'>), equals new_mode? False
2025-10-20 13:04:19,206 - integration.integrations.tray_controller_integration - DEBUG - TrayIntegration: mapping mode -> status: AppMode.SLEEPING -> TrayStatus.SLEEPING
2025-10-20 13:04:19,206 - integration.core.event_bus - DEBUG - EventBus: dispatch 'tray.status_updated' to 0 subscriber(s)
2025-10-20 13:04:19,206 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: tray.status_updated
2025-10-20 13:04:19,206 - integration.integrations.tray_controller_integration - INFO - 🔄 Режим приложения изменен: sleeping → sleeping
2025-10-20 13:04:19,206 - integration.integrations.screenshot_capture_integration - INFO - 🔍 ScreenshotCapture: Получено событие app.mode_changed - mode=AppMode.SLEEPING (type: <enum 'AppMode'>)
2025-10-20 13:04:19,206 - integration.integrations.screenshot_capture_integration - DEBUG - ScreenshotCapture: Игнорируем режим AppMode.SLEEPING, ждем PROCESSING
2025-10-20 13:04:19,206 - integration.workflows.processing_workflow - DEBUG - ⚙️ ProcessingWorkflow: режим изменен на sleeping
2025-10-20 13:04:19,206 - integration.workflows.listening_workflow - DEBUG - 🎤 ListeningWorkflow: режим изменен на sleeping
🔄 Координация смены режима: sleeping
2025-10-20 13:04:19,206 - integration.integrations.updater_integration - INFO - Режим приложения изменен на: None
I0000 00:00:1760979859.207564 2294900 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-10-20 13:04:19,218 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 5248)
2025-10-20 13:04:19,219 - integration.integrations.tray_controller_integration - INFO - 🎯 TRAY DEBUG: _apply_status_ui_sync ВЫЗВАН! status=TrayStatus.SLEEPING (type: <enum 'TrayStatus'>)
🎯 TRAY DEBUG: TrayIconGenerator.create_circle_icon status=TrayStatus.SLEEPING (type: <enum 'TrayStatus'>)
🎯 TRAY DEBUG: Available colors: {<TrayStatus.SLEEPING: 'sleeping'>: '#808080', <TrayStatus.LISTENING: 'listening'>: '#007AFF', <TrayStatus.PROCESSING: 'processing'>: '#FF9500'}
🎯 TRAY DEBUG: Selected color: #808080
🎯 TRAY DEBUG: create_icon_file вызван для status=TrayStatus.SLEEPING
🎯 TRAY DEBUG: generated color=#808080, PIL_available=True
2025-10-20 13:04:19,223 - integration.integrations.tray_controller_integration - INFO - ✅ Tray UI applied: processing -> sleeping
2025-10-20 13:04:19,224 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 4736)
2025-10-20 13:04:19,234 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 4224)
2025-10-20 13:04:19,245 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 3712)
2025-10-20 13:04:19,256 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 3200)
2025-10-20 13:04:19,266 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 2688)
2025-10-20 13:04:19,277 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 2176)
2025-10-20 13:04:19,288 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 1664)
2025-10-20 13:04:19,298 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 1152)
2025-10-20 13:04:19,309 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 640)
2025-10-20 13:04:19,320 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 512 фреймов (осталось: 128)
2025-10-20 13:04:19,331 - modules.speech_playback.core.buffer - DEBUG - 🎵 Воспроизведено: 128 фреймов + 384 тишины (dtype=int16, ch=1)
2025-10-20 13:04:19,334 - modules.speech_playback.core.player - INFO - ✅ Чанк chunk_8_1760979858774 полностью воспроизведен
2025-10-20 13:04:19,334 - modules.speech_playback.core.buffer - DEBUG - ✅ Чанк завершен: chunk_8_1760979858774
2025-10-20 13:04:19,334 - modules.speech_playback.core.player - INFO - ✅ Чанк обработан: chunk_8_1760979858774
2025-10-20 13:04:19,379 - modules.voiceover_control.core.controller - DEBUG - VoiceOverController: Updated status - currently running: False
2025-10-20 13:04:19,379 - modules.voiceover_control.core.controller - DEBUG - VoiceOverController: VoiceOver was not running initially, skipping release for mode sleeping
2025-10-20 13:04:19,379 - integration.integrations.voiceover_ducking_integration - DEBUG - VoiceOverDuckingIntegration: Applied mode sleeping
2025-10-20 13:04:19,567 - modules.speech_playback.core.player - INFO - ⏸️ Аудио поток остановлен (очередь пуста, lazy stop)
2025-10-20 13:04:21,224 - modules.input_processing.keyboard.mac.quartz_monitor - DEBUG - 🔍 Quartz tap вызван: event_type=10
2025-10-20 13:04:21,224 - modules.input_processing.keyboard.mac.q