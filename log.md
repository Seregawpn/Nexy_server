2025-12-01 12:23:26,276 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Найден ID для 'MacBook Air Speakers': 4
2025-12-01 12:23:26,276 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Найдено устройство через SwitchAudioSource: name=MacBook Air Speakers, id=4
2025-12-01 12:23:26,276 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Найдено default output устройство (через SwitchAudioSource):
2025-12-01 12:23:26,276 - modules.speech_playback.core.player - INFO -    Name: MacBook Air Speakers
2025-12-01 12:23:26,276 - modules.speech_playback.core.player - INFO -    Index: 4
2025-12-01 12:23:26,276 - modules.speech_playback.core.player - INFO -    Max Output Channels: 2
2025-12-01 12:23:26,276 - modules.speech_playback.core.player - INFO -    Default Sample Rate: 48000.0 Hz
2025-12-01 12:23:26,276 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Полная информация: {'name': 'MacBook Air Speakers', 'index': 4, 'hostapi': 0, 'max_input_channels': 0, 'max_output_channels': 2, 'default_low_input_latency': 0.01, 'default_low_output_latency': 0.015166666666666667, 'default_high_input_latency': 0.1, 'default_high_output_latency': 0.0245, 'default_samplerate': 48000.0}
2025-12-01 12:23:26,321 - modules.speech_playback.core.player - INFO - ⏸️ Аудио поток остановлен (очередь пуста, lazy stop)
2025-12-01 12:23:26,821 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Используем SwitchAudioSource: /opt/homebrew/bin/SwitchAudioSource
I0000 00:00:1764609806.822187 3473740 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-01 12:23:26,908 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] macOS default OUTPUT (через SwitchAudioSource): "MacBook Air Speakers"
2025-12-01 12:23:26,908 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Найден ID для 'MacBook Air Speakers': 4
2025-12-01 12:23:27,914 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Используем SwitchAudioSource: /opt/homebrew/bin/SwitchAudioSource
I0000 00:00:1764609807.915160 3473740 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-01 12:23:28,002 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] macOS default OUTPUT (через SwitchAudioSource): "MacBook Air Speakers"
2025-12-01 12:23:28,002 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Найден ID для 'MacBook Air Speakers': 4
2025-12-01 12:23:29,008 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Используем SwitchAudioSource: /opt/homebrew/bin/SwitchAudioSource
I0000 00:00:1764609809.009248 3473740 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-01 12:23:29,099 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] macOS default OUTPUT (через SwitchAudioSource): "MacBook Air Speakers"
2025-12-01 12:23:29,100 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Найден ID для 'MacBook Air Speakers': 4
2025-12-01 12:23:30,105 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Используем SwitchAudioSource: /opt/homebrew/bin/SwitchAudioSource
I0000 00:00:1764609810.106096 3473740 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-01 12:23:30,226 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] macOS default OUTPUT (через SwitchAudioSource): "Sergiy’s AirPods"
2025-12-01 12:23:30,226 - modules.speech_playback.core.player - DEBUG - 💡 [OUTPUT] BT устройство 'Sergiy’s AirPods' - используем device=None (не ищем ID в PortAudio)
2025-12-01 12:23:30,226 - modules.speech_playback.core.player - INFO - 🔄 [OUTPUT] Обнаружена смена устройства: "MacBook Air Speakers" (ID=4, BT=False) → "Sergiy’s AirPods" (ID=None, BT=True)
2025-12-01 12:23:30,226 - modules.speech_playback.core.player - INFO - 🔄 [OUTPUT] Начало переключения устройства: "MacBook Air Speakers" (ID=4, BT=False) → "Sergiy’s AirPods" (ID=None, BT=True)
2025-12-01 12:23:30,226 - modules.speech_playback.core.player - INFO - 🛑 [OUTPUT] Остановка старого потока для устройства "MacBook Air Speakers"...
2025-12-01 12:23:30,226 - modules.speech_playback.core.player - DEBUG - 🔄 [OUTPUT] Закрываем поток...
2025-12-01 12:23:30,229 - modules.speech_playback.core.player - DEBUG - ✅ [OUTPUT] Поток закрыт (close() вызван)
2025-12-01 12:23:30,229 - modules.speech_playback.core.player - DEBUG - ✅ [OUTPUT] Поток не был активен (active=False)
2025-12-01 12:23:30,229 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Финальная проверка: поток не активен (active=False)
2025-12-01 12:23:30,229 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Финальная проверка: поток не активен (active=False) - можно устанавливать _audio_stream=None
2025-12-01 12:23:30,229 - modules.speech_playback.core.player - INFO - 🛑 Аудио поток остановлен и закрыт (ожидание: 0.000с, active=False: True)
2025-12-01 12:23:30,229 - modules.speech_playback.core.player - DEBUG - ⏳ [OUTPUT] Задержка после close() для обычного устройства: 0.3с...
2025-12-01 12:23:30,534 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Поток полностью закрыт (общее время: 0.300с, active=False: True)
2025-12-01 12:23:30,534 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Лог подтверждения: active=False → _audio_stream=None → устройство освобождено
2025-12-01 12:23:30,534 - modules.speech_playback.core.player - INFO - ⏳ [OUTPUT] Задержка перед созданием нового потока: 2.0с (BT=True)
2025-12-01 12:23:30,534 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Подтверждение: старый поток полностью закрыт, устройство освобождено
2025-12-01 12:23:30,547 - modules.speech_playback.core.player - INFO - 🔄 Playback loop завершен
2025-12-01 12:23:30,547 - integration.integrations.speech_playback_integration - INFO - SpeechPlayback: _on_player_completed для сессии 1764609797.337923, grpc_done=False, finalized=False
2025-12-01 12:23:30,547 - integration.integrations.speech_playback_integration - DEBUG - SpeechPlayback: пропускаем завершение для сессии 1764609797.337923 (grpc_done=False, finalized=False)
2025-12-01 12:23:30,697 - modules.speech_playback.macos.performance - DEBUG - 📊 CPU: 21.0%, Memory: 80.2%
2025-12-01 12:23:32,540 - modules.speech_playback.core.buffer - INFO - 🧹 Очередь очищена: 0 чанков
2025-12-01 12:23:32,540 - modules.speech_playback.core.buffer - INFO - 🧹 Буфер воспроизведения очищен: 0 фреймов
2025-12-01 12:23:32,540 - modules.speech_playback.core.buffer - INFO - 🧹 Все буферы очищены
2025-12-01 12:23:32,540 - modules.speech_playback.core.player - DEBUG - 🔄 [OUTPUT] Буфер очищен
2025-12-01 12:23:32,541 - modules.speech_playback.core.player - DEBUG - 💡 [OUTPUT] BT устройство или device_id=None - пропускаем получение информации из PortAudio
2025-12-01 12:23:32,541 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Создаем новый поток для устройства "Sergiy’s AirPods" (device_id=None, BT=True)...
2025-12-01 12:23:32,541 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] _start_audio_stream вызван: sync_output=True, device_id=None
2025-12-01 12:23:32,541 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Текущая конфигурация: rate=48000Hz, channels=2, dtype=int16, buffer_size=512
2025-12-01 12:23:32,541 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Синхронизируем формат с устройством...
2025-12-01 12:23:32,541 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Запрашиваем системное default output устройство...
2025-12-01 12:23:32,541 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] ШАГ 1.2: Определение устройства через macOS API (приоритет 1)
2025-12-01 12:23:32,542 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Используем SwitchAudioSource: /opt/homebrew/bin/SwitchAudioSource
I0000 00:00:1764609812.542747 3473740 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-01 12:23:32,644 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] macOS default OUTPUT (через SwitchAudioSource): "Sergiy’s AirPods"
2025-12-01 12:23:32,645 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] macOS default OUTPUT (источник истины): "Sergiy’s AirPods"
2025-12-01 12:23:32,645 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Найден ID для 'Sergiy’s AirPods': 1
2025-12-01 12:23:32,645 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Найдено устройство через SwitchAudioSource: name=Sergiy’s AirPods, id=1
2025-12-01 12:23:32,645 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Найдено default output устройство (через SwitchAudioSource):
2025-12-01 12:23:32,645 - modules.speech_playback.core.player - INFO -    Name: Sergiy’s AirPods
2025-12-01 12:23:32,645 - modules.speech_playback.core.player - INFO -    Index: 1
2025-12-01 12:23:32,645 - modules.speech_playback.core.player - INFO -    Max Output Channels: 2
2025-12-01 12:23:32,645 - modules.speech_playback.core.player - INFO -    Default Sample Rate: 48000.0 Hz
2025-12-01 12:23:32,645 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Полная информация: {'name': 'Sergiy’s AirPods', 'index': 1, 'hostapi': 0, 'max_input_channels': 0, 'max_output_channels': 2, 'default_low_input_latency': 0.01, 'default_low_output_latency': 0.16133333333333333, 'default_high_input_latency': 0.1, 'default_high_output_latency': 0.17066666666666666, 'default_samplerate': 48000.0}
2025-12-01 12:23:32,645 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] После синхронизации: rate=48000Hz, channels=2
2025-12-01 12:23:32,645 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] device_id не передан, получаем устройство через macOS API (SwitchAudioSource)...
2025-12-01 12:23:32,645 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Fallback на SwitchAudioSource (device_id не передан)
2025-12-01 12:23:32,645 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Запрашиваем системное default output устройство...
2025-12-01 12:23:32,645 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] ШАГ 1.2: Определение устройства через macOS API (приоритет 1)
2025-12-01 12:23:32,646 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Используем SwitchAudioSource: /opt/homebrew/bin/SwitchAudioSource
I0000 00:00:1764609812.646295 3473740 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
2025-12-01 12:23:32,728 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] macOS default OUTPUT (через SwitchAudioSource): "Sergiy’s AirPods"
2025-12-01 12:23:32,728 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] macOS default OUTPUT (источник истины): "Sergiy’s AirPods"
2025-12-01 12:23:32,729 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Найден ID для 'Sergiy’s AirPods': 1
2025-12-01 12:23:32,729 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Найдено устройство через SwitchAudioSource: name=Sergiy’s AirPods, id=1
2025-12-01 12:23:32,729 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Найдено default output устройство (через SwitchAudioSource):
2025-12-01 12:23:32,729 - modules.speech_playback.core.player - INFO -    Name: Sergiy’s AirPods
2025-12-01 12:23:32,729 - modules.speech_playback.core.player - INFO -    Index: 1
2025-12-01 12:23:32,729 - modules.speech_playback.core.player - INFO -    Max Output Channels: 2
2025-12-01 12:23:32,729 - modules.speech_playback.core.player - INFO -    Default Sample Rate: 48000.0 Hz
2025-12-01 12:23:32,729 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Полная информация: {'name': 'Sergiy’s AirPods', 'index': 1, 'hostapi': 0, 'max_input_channels': 0, 'max_output_channels': 2, 'default_low_input_latency': 0.01, 'default_low_output_latency': 0.16133333333333333, 'default_high_input_latency': 0.1, 'default_high_output_latency': 0.17066666666666666, 'default_samplerate': 48000.0}
2025-12-01 12:23:32,729 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] macOS API (источник истины): "Sergiy’s AirPods" (ID=1)
2025-12-01 12:23:32,729 - modules.speech_playback.core.player - INFO - 🔧 [OUTPUT] BT устройство обнаружено: "Sergiy’s AirPods"
2025-12-01 12:23:32,729 - modules.speech_playback.core.player - INFO - 💡 [OUTPUT] SwitchAudioSource → device=None для BT (macOS управляет параметрами)
2025-12-01 12:23:32,729 - modules.speech_playback.core.player - DEBUG - 💡 [OUTPUT] BT устройство "Sergiy’s AirPods" - пропускаем DeviceParamsNormalizer, доверяем macOS параметрам
2025-12-01 12:23:32,729 - modules.speech_playback.core.player - INFO - 💡 [OUTPUT] SwitchAudioSource → "Sergiy’s AirPods" (BT устройство)
2025-12-01 12:23:32,729 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] BT устройство: используем device=None (НЕ используем PortAudio ID)
2025-12-01 12:23:32,729 - modules.speech_playback.core.player - INFO - 🔧 [OUTPUT] BT устройство: используем channels=2 (обязательно), НЕ задаем blocksize, latency (пусть macOS/PortAudio выберут сами)
2025-12-01 12:23:32,729 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Конфигурация потока:
2025-12-01 12:23:32,730 - modules.speech_playback.core.player - INFO -    device: None
2025-12-01 12:23:32,730 - modules.speech_playback.core.player - INFO -    channels: 2
2025-12-01 12:23:32,730 - modules.speech_playback.core.player - INFO -    dtype: int16
2025-12-01 12:23:32,730 - modules.speech_playback.core.player - INFO -    samplerate: 48000 Hz
2025-12-01 12:23:32,730 - modules.speech_playback.core.player - INFO -    blocksize: N/A (не задан, пусть PortAudio выберет)
2025-12-01 12:23:32,730 - modules.speech_playback.core.player - INFO -    latency: N/A (не задан, пусть PortAudio выберет)
2025-12-01 12:23:32,730 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Создаём поток для устройства: Sergiy’s AirPods (ID=System Default)
2025-12-01 12:23:32,730 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Пропускаем проверку доступности (device_id=None, device_id_actual=System Default)
2025-12-01 12:23:32,730 - modules.speech_playback.core.player - INFO - ⏳ [OUTPUT] Bluetooth устройство обнаружено, ожидание готовности CoreAudio pipeline (2.0с)...
2025-12-01 12:23:34,735 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Начинаем создание потока (max_retries=5, base_delay=0.3s, BT=True)...
2025-12-01 12:23:34,736 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Подтверждение: старый поток полностью закрыт (_audio_stream=None)
2025-12-01 12:23:34,736 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Попытка 1/5 создания потока...
2025-12-01 12:23:34,736 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Подтверждение: старый поток закрыт → создаём новый stream
2025-12-01 12:23:34,736 - modules.speech_playback.core.player - INFO -    Устройство: Sergiy’s AirPods (ID=System Default, BT=True)
2025-12-01 12:23:34,736 - modules.speech_playback.core.player - INFO -    Параметры: device=None, channels=2, samplerate=48000, blocksize=N/A, latency=N/A
2025-12-01 12:23:34,736 - modules.speech_playback.core.player - INFO -    SwitchAudioSource → device=None для BT (macOS управляет параметрами)
2025-12-01 12:23:34,736 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Параметры потока: {'device': None, 'channels': 2, 'dtype': 'int16', 'samplerate': 48000, 'callback': <bound method SequentialSpeechPlayer._audio_callback of <modules.speech_playback.core.player.SequentialSpeechPlayer object at 0x1182d27b0>>}
2025-12-01 12:23:34,736 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Создаем новый поток: device=None, BT=True
||PaMacCore (AUHAL)|| Warning on line 521: err=''!obj'', msg=Unknown Error
||PaMacCore (AUHAL)|| Warning on line 441: err=''!obj'', msg=Unknown Error
||PaMacCore (AUHAL)|| Error on line 1332: err='-10851', msg=Audio Unit: Invalid Property Value
2025-12-01 12:23:34,740 - modules.speech_playback.core.player - ERROR - ❌ [OUTPUT] Попытка 1/5 создания потока не удалась (время: 0.00с)
2025-12-01 12:23:34,740 - modules.speech_playback.core.player - ERROR -    Устройство: Sergiy’s AirPods (ID=System Default, BT=True)
2025-12-01 12:23:34,740 - modules.speech_playback.core.player - ERROR -    Параметры: device=None, channels=2, samplerate=48000, blocksize=N/A, latency=N/A
2025-12-01 12:23:34,740 - modules.speech_playback.core.player - ERROR -    Ошибка: PortAudioError: Error opening OutputStream: Internal PortAudio error [PaErrorCode -9986]
2025-12-01 12:23:34,740 - modules.speech_playback.core.player - ERROR -    is_error_9986=True, is_error_10851=False
2025-12-01 12:23:34,740 - modules.speech_playback.core.player - WARNING - ⚠️ [OUTPUT] Обнаружена ошибка -9986 (Internal PortAudio error) - устройство может быть занято
2025-12-01 12:23:34,741 - modules.speech_playback.core.player - INFO - 💡 [OUTPUT] Рекомендация: убедитесь, что старый поток полностью закрыт
2025-12-01 12:23:34,741 - modules.speech_playback.core.player - DEBUG -    Детали ошибки:
Traceback (most recent call last):
  File "/Users/sergiyzasorin/Development/Nexy/client(prod)/modules/speech_playback/core/player.py", line 877, in _start_audio_stream
    self._audio_stream = sd.OutputStream(**stream_config)
                         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/Users/sergiyzasorin/Development/Nexy/client(prod)/.venv/lib/python3.13/site-packages/sounddevice.py", line 1515, in __init__
    _StreamBase.__init__(self, kind='output', wrap_callback='array',
    ~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                         **_remove_self(locals()))
                         ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sergiyzasorin/Development/Nexy/client(prod)/.venv/lib/python3.13/site-packages/sounddevice.py", line 909, in __init__
    _check(_lib.Pa_OpenStream(self._ptr, iparameters, oparameters,
    ~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                              samplerate, blocksize, stream_flags,
                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                              callback_ptr, userdata),
                              ^^^^^^^^^^^^^^^^^^^^^^^^
           f'Error opening {self.__class__.__name__}')
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sergiyzasorin/Development/Nexy/client(prod)/.venv/lib/python3.13/site-packages/sounddevice.py", line 2804, in _check
    raise PortAudioError(errormsg, err)
sounddevice.PortAudioError: Error opening OutputStream: Internal PortAudio error [PaErrorCode -9986]
2025-12-01 12:23:34,750 - modules.speech_playback.core.player - WARNING - ⚠️ [OUTPUT] Ошибка -9986: устройство может быть занято старым потоком
2025-12-01 12:23:34,750 - modules.speech_playback.core.player - INFO - 🔄 [OUTPUT] Вызываем _stop_audio_stream() для гарантированного освобождения устройства...
2025-12-01 12:23:34,750 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Используем is_bluetooth=True из текущей попытки (устройство: "Sergiy’s AirPods")
2025-12-01 12:23:34,750 - modules.speech_playback.core.player - INFO - ⏳ [OUTPUT] Задержка для освобождения устройства после ошибки: 1.0с...
2025-12-01 12:23:35,723 - modules.input_processing.keyboard.keyboard_monitor - INFO - ✅ Control+N комбинация активирована (pynput)
🔑 SYNC PRESS: 1764609815.7234051 - ПОЛУЧЕН CALLBACK!
🔑 DEBUG: Найден loop, планирую async task
🔑 DEBUG: Task запланирован: <Future at 0x1182eb8d0 state=pending>
🎤🎤🎤 _handle_press ВЫЗВАН! event=press, timestamp=1764609815.7234051
2025-12-01 12:23:35,725 - integration.integrations.input_processing_integration - INFO - 🎤 _handle_press ВЫЗВАН! event=press, timestamp=1764609815.7234051
2025-12-01 12:23:35,725 - integration.integrations.input_processing_integration - INFO - 🎤 PTT: keyDown(ctrl_n) → PRESS, timestamp=1764609815.7234051
2025-12-01 12:23:35,725 - integration.integrations.input_processing_integration - DEBUG - PRESS: current_session=1764609797.337923, pending_session=None, recognized=False, recording=False
🔑 PRESS EVENT: 1764609815.7234051 - начинаем запись
2025-12-01 12:23:35,725 - integration.integrations.input_processing_integration - DEBUG - PRESS: сохранён session_id для отмены: 1764609797.337923
2025-12-01 12:23:35,725 - integration.integrations.input_processing_integration - DEBUG - PRESS: pending_session_id=1764609815.7234051
2025-12-01 12:23:35,726 - integration.integrations.input_processing_integration - DEBUG - 🔄 [STATE] IDLE → PENDING (reason: press_received)
2025-12-01 12:23:35,726 - integration.integrations.input_processing_integration - INFO - 🔑 [INPUT] Публикую keyboard.press событие...
2025-12-01 12:23:35,726 - integration.core.event_bus - DEBUG - EventBus: dispatch 'keyboard.press' to 1 subscriber(s)
2025-12-01 12:23:35,726 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'keyboard.press': <bound method VoiceOverDuckingIntegration.handle_keyboard_press of <integration.integrations.voiceover_ducking_integration.VoiceOverDuckingIntegration object at 0x118234980>>
2025-12-01 12:23:35,726 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: keyboard.press
2025-12-01 12:23:35,726 - integration.integrations.input_processing_integration - INFO - 🔑 [INPUT] ✅ keyboard.press событие опубликовано
2025-12-01 12:23:35,755 - modules.speech_playback.core.player - INFO - 🔄 [OUTPUT] Для BT устройства создаем stream с device=None (macOS управляет параметрами)
2025-12-01 12:23:35,755 - modules.speech_playback.core.player - INFO - 🔧 [OUTPUT] Для BT устройства: device=None, channels=2, без blocksize/latency
2025-12-01 12:23:35,755 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Устройство должно быть освобождено после ошибки -9986
2025-12-01 12:23:35,755 - modules.speech_playback.core.player - INFO - ⏳ [OUTPUT] Повторная попытка через 0.90с (экспоненциальный backoff ×1.5, попытка 1/5)...
^N^N2025-12-01 12:23:36,341 - modules.input_processing.keyboard.keyboard_monitor - INFO - 🔑 HOLD_MONITOR: LONG_PRESS triggered! duration=0.618s, threshold=0.6
🔑 HOLD_MONITOR: LONG_PRESS triggered! duration=0.618s, threshold=0.6
🔑 SYNC LONG: 0.618с
🎤🎤🎤 _handle_long_press ВЫЗВАН! duration=0.618s
2025-12-01 12:23:36,342 - integration.integrations.input_processing_integration - INFO - 🎤 _handle_long_press ВЫЗВАН! duration=0.618s
2025-12-01 12:23:36,342 - integration.integrations.input_processing_integration - INFO - 🎤 PTT: LONG_PRESS triggered → RECORDING_START, duration=0.618s
2025-12-01 12:23:36,343 - integration.integrations.input_processing_integration - INFO - 🔑 LONG_PRESS: 0.618с
🔑 LONG_PRESS: 0.618с
🔑 LONG_PRESS: event.key=ctrl_n, event.timestamp=1764609816.3419662
🔑 LONG_PRESS: _recording_started=False, active_session_id=1764609797.337923
2025-12-01 12:23:36,343 - integration.integrations.input_processing_integration - DEBUG - LONG_PRESS: запрашиваем отмену gRPC перед открытием микрофона (sid=1764609797.337923)
2025-12-01 12:23:36,343 - integration.core.event_bus - DEBUG - EventBus: dispatch 'grpc.request_cancel' to 2 subscriber(s)
2025-12-01 12:23:36,343 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'grpc.request_cancel': <bound method SpeechPlaybackIntegration._on_grpc_cancel of <integration.integrations.speech_playback_integration.SpeechPlaybackIntegration object at 0x1181ffb60>>
2025-12-01 12:23:36,343 - integration.integrations.speech_playback_integration - INFO - SpeechPlayback: получен grpc.request_cancel — очищаем буфер
2025-12-01 12:23:36,343 - modules.speech_playback.core.buffer - INFO - 🧹 Очередь очищена: 0 чанков
2025-12-01 12:23:36,343 - modules.speech_playback.core.buffer - INFO - 🧹 Буфер воспроизведения очищен: 0 фреймов
2025-12-01 12:23:36,343 - modules.speech_playback.core.buffer - INFO - 🧹 Все буферы очищены
2025-12-01 12:23:36,343 - modules.speech_playback.core.player - WARNING - ⚠️ Невозможно остановить воспроизведение в текущем состоянии
2025-12-01 12:23:36,343 - integration.core.event_bus - DEBUG - EventBus: dispatch 'playback.cancelled' to 3 subscriber(s)
2025-12-01 12:23:36,343 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'playback.cancelled': <bound method SpeechPlaybackIntegration._on_unified_interrupt of <integration.integrations.speech_playback_integration.SpeechPlaybackIntegration object at 0x1181ffb60>>
2025-12-01 12:23:36,343 - integration.integrations.speech_playback_integration - INFO - SpeechPlayback: ЕДИНЫЙ канал прерывания, source=grpc_cancel, reason=interrupt
2025-12-01 12:23:36,343 - integration.integrations.speech_playback_integration - DEBUG - SpeechPlayback: воспроизведение уже остановлено (state=PlaybackState.IDLE)
2025-12-01 12:23:36,343 - integration.integrations.speech_playback_integration - INFO - SpeechPlayback: прерывание обработано через ЕДИНЫЙ канал
2025-12-01 12:23:36,343 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'playback.cancelled': <bound method InputProcessingIntegration._on_playback_finished of <integration.integrations.input_processing_integration.InputProcessingIntegration object at 0x1181fd2b0>>
2025-12-01 12:23:36,343 - integration.integrations.input_processing_integration - DEBUG - PLAYBACK: finished (event=playback.cancelled, session=1764609797.337923)
2025-12-01 12:23:36,343 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'playback.cancelled': <bound method SignalIntegration._on_playback_cancelled of <integration.integrations.signal_integration.SignalIntegration object at 0x118234050>>
2025-12-01 12:23:36,344 - integration.integrations.signal_integration - DEBUG - Signals: CANCEL skipped (reason=grpc_cancel)
2025-12-01 12:23:36,344 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: playback.cancelled
2025-12-01 12:23:36,344 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'grpc.request_cancel': <bound method GrpcClientIntegration._on_request_cancel of <integration.integrations.grpc_client_integration.GrpcClientIntegration object at 0x1181ff0e0>>
2025-12-01 12:23:36,344 - integration.integrations.grpc_client_integration - DEBUG - grpc.request_cancel: task not found or already done for sid=1764609797.337923
2025-12-01 12:23:36,344 - integration.core.event_bus - DEBUG - 📢 Событие опубликовано: grpc.request_cancel
2025-12-01 12:23:36,344 - integration.integrations.input_processing_integration - DEBUG - PLAYBACK: grace задержка 0.300s
^N^N^N2025-12-01 12:23:36,645 - integration.integrations.input_processing_integration - DEBUG - RECORDING: prestart задержка 0.300s
2025-12-01 12:23:36,661 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Старый поток закрыт → создаём новый stream (попытка 1/5)
2025-12-01 12:23:36,661 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Попытка 2/5 создания потока...
2025-12-01 12:23:36,661 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Подтверждение: старый поток закрыт → создаём новый stream
2025-12-01 12:23:36,661 - modules.speech_playback.core.player - INFO -    Устройство: Sergiy’s AirPods (ID=System Default, BT=True)
2025-12-01 12:23:36,661 - modules.speech_playback.core.player - INFO -    Параметры: device=None, channels=2, samplerate=48000, blocksize=N/A, latency=N/A
2025-12-01 12:23:36,661 - modules.speech_playback.core.player - INFO -    SwitchAudioSource → device=None для BT (macOS управляет параметрами)
2025-12-01 12:23:36,661 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Параметры потока: {'device': None, 'channels': 2, 'dtype': 'int16', 'samplerate': 48000, 'callback': <bound method SequentialSpeechPlayer._audio_callback of <modules.speech_playback.core.player.SequentialSpeechPlayer object at 0x1182d27b0>>}
2025-12-01 12:23:36,662 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Создаем новый поток: device=None, BT=True
||PaMacCore (AUHAL)|| Warning on line 521: err=''!obj'', msg=Unknown Error
||PaMacCore (AUHAL)|| Warning on line 441: err=''!obj'', msg=Unknown Error
||PaMacCore (AUHAL)|| Error on line 1332: err='-10851', msg=Audio Unit: Invalid Property Value
2025-12-01 12:23:36,664 - modules.speech_playback.core.player - ERROR - ❌ [OUTPUT] Попытка 2/5 создания потока не удалась (время: 1.93с)
2025-12-01 12:23:36,665 - modules.speech_playback.core.player - ERROR -    Устройство: Sergiy’s AirPods (ID=System Default, BT=True)
2025-12-01 12:23:36,665 - modules.speech_playback.core.player - ERROR -    Параметры: device=None, channels=2, samplerate=48000, blocksize=N/A, latency=N/A
^N2025-12-01 12:23:36,665 - modules.speech_playback.core.player - ERROR -    Ошибка: PortAudioError: Error opening OutputStream: Internal PortAudio error [PaErrorCode -9986]
2025-12-01 12:23:36,665 - modules.speech_playback.core.player - ERROR -    is_error_9986=True, is_error_10851=False
2025-12-01 12:23:36,665 - modules.speech_playback.core.player - WARNING - ⚠️ [OUTPUT] Обнаружена ошибка -9986 (Internal PortAudio error) - устройство может быть занято
2025-12-01 12:23:36,665 - modules.speech_playback.core.player - INFO - 💡 [OUTPUT] Рекомендация: убедитесь, что старый поток полностью закрыт
2025-12-01 12:23:36,665 - modules.speech_playback.core.player - DEBUG -    Детали ошибки:
Traceback (most recent call last):
  File "/Users/sergiyzasorin/Development/Nexy/client(prod)/modules/speech_playback/core/player.py", line 877, in _start_audio_stream
    self._audio_stream = sd.OutputStream(**stream_config)
                         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/Users/sergiyzasorin/Development/Nexy/client(prod)/.venv/lib/python3.13/site-packages/sounddevice.py", line 1515, in __init__
    _StreamBase.__init__(self, kind='output', wrap_callback='array',
    ~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                         **_remove_self(locals()))
                         ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sergiyzasorin/Development/Nexy/client(prod)/.venv/lib/python3.13/site-packages/sounddevice.py", line 909, in __init__
    _check(_lib.Pa_OpenStream(self._ptr, iparameters, oparameters,
    ~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                              samplerate, blocksize, stream_flags,
                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                              callback_ptr, userdata),
                              ^^^^^^^^^^^^^^^^^^^^^^^^
           f'Error opening {self.__class__.__name__}')
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sergiyzasorin/Development/Nexy/client(prod)/.venv/lib/python3.13/site-packages/sounddevice.py", line 2804, in _check
    raise PortAudioError(errormsg, err)
sounddevice.PortAudioError: Error opening OutputStream: Internal PortAudio error [PaErrorCode -9986]
2025-12-01 12:23:36,668 - modules.speech_playback.core.player - WARNING - ⚠️ [OUTPUT] Ошибка -9986: устройство может быть занято старым потоком
2025-12-01 12:23:36,668 - modules.speech_playback.core.player - INFO - 🔄 [OUTPUT] Вызываем _stop_audio_stream() для гарантированного освобождения устройства...
2025-12-01 12:23:36,668 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Используем is_bluetooth=True из текущей попытки (устройство: "Sergiy’s AirPods")
2025-12-01 12:23:36,668 - modules.speech_playback.core.player - INFO - ⏳ [OUTPUT] Задержка для освобождения устройства после ошибки: 1.0с...
^N^N2025-12-01 12:23:36,845 - integration.integrations.input_processing_integration - WARNING - ⚠️ LONG_PRESS: таймаут ожидания остановки воспроизведения (0.5s), принудительно прерываем
2025-12-01 12:23:36,846 - integration.core.event_bus - DEBUG - EventBus: dispatch 'playback.cancelled' to 3 subscriber(s)
2025-12-01 12:23:36,846 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'playback.cancelled': <bound method SpeechPlaybackIntegration._on_unified_interrupt of <integration.integrations.speech_playback_integration.SpeechPlaybackIntegration object at 0x1181ffb60>>
2025-12-01 12:23:36,846 - integration.integrations.speech_playback_integration - INFO - SpeechPlayback: ЕДИНЫЙ канал прерывания, source=input_processing, reason=timeout
2025-12-01 12:23:36,846 - integration.integrations.speech_playback_integration - DEBUG - SpeechPlayback: воспроизведение уже остановлено (state=PlaybackState.IDLE)
2025-12-01 12:23:36,846 - integration.integrations.speech_playback_integration - INFO - SpeechPlayback: прерывание обработано через ЕДИНЫЙ канал
2025-12-01 12:23:36,846 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'playback.cancelled': <bound method InputProcessingIntegration._on_playback_finished of <integration.integrations.input_processing_integration.InputProcessingIntegration object at 0x1181fd2b0>>
2025-12-01 12:23:36,846 - integration.integrations.input_processing_integration - DEBUG - PLAYBACK: finished (event=playback.cancelled, session=1764609797.337923)
2025-12-01 12:23:36,846 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'playback.cancelled': <bound method SignalIntegration._on_playback_cancelled of <integration.integrations.signal_integration.SignalIntegration object at 0x118234050>>
2025-12-01 12:23:36,846 - integration.integrations.signal_integration - INFO - Signals: CANCEL (playback.cancelled)
2025-12-01 12:23:36,851 - integration.core.event_bus - DEBUG - EventBus: dispatch 'playback.signal' to 1 subscriber(s)
2025-12-01 12:23:36,851 - integration.core.event_bus - DEBUG - EventBus: awaiting async callback inline for 'playback.signal': <bound method SpeechPlaybackIntegration._on_playback_signal of <integration.integrations.speech_playback_integration.SpeechPlaybackIntegration object at 0x1181ffb60>>
2025-12-01 12:23:36,851 - integration.integrations.speech_playback_integration - INFO - 🔔 playback.signal: pattern=cancel, bytes=11520, sr=48000, ch=1, gain=1.0, prio=0
2025-12-01 12:23:36,852 - modules.speech_playback.core.player - INFO - 🎯 [AUDIO_REFACTOR] Начало инициализации Sequential Speech Player...
2025-12-01 12:23:36,852 - modules.speech_playback.core.player - DEBUG - 🔍 [AUDIO_DEBUG] Инициализация Core Audio Manager...
2025-12-01 12:23:36,852 - modules.speech_playback.macos.core_audio - INFO - ✅ Core Audio инициализирован
2025-12-01 12:23:36,852 - modules.speech_playback.core.player - INFO - ✅ [AUDIO_SUCCESS] Core Audio Manager инициализирован
2025-12-01 12:23:36,852 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Запрашиваем системное default output устройство...
2025-12-01 12:23:36,852 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] ШАГ 1.2: Определение устройства через macOS API (приоритет 1)
2025-12-01 12:23:36,852 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Используем SwitchAudioSource: /opt/homebrew/bin/SwitchAudioSource
I0000 00:00:1764609816.853509 3472083 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
^N2025-12-01 12:23:36,956 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] macOS default OUTPUT (через SwitchAudioSource): "Sergiy’s AirPods"
2025-12-01 12:23:36,957 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] macOS default OUTPUT (источник истины): "Sergiy’s AirPods"
2025-12-01 12:23:36,957 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Найден ID для 'Sergiy’s AirPods': 1
2025-12-01 12:23:36,957 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Найдено устройство через SwitchAudioSource: name=Sergiy’s AirPods, id=1
2025-12-01 12:23:36,957 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Найдено default output устройство (через SwitchAudioSource):
2025-12-01 12:23:36,957 - modules.speech_playback.core.player - INFO -    Name: Sergiy’s AirPods
2025-12-01 12:23:36,957 - modules.speech_playback.core.player - INFO -    Index: 1
2025-12-01 12:23:36,957 - modules.speech_playback.core.player - INFO -    Max Output Channels: 2
2025-12-01 12:23:36,957 - modules.speech_playback.core.player - INFO -    Default Sample Rate: 48000.0 Hz
2025-12-01 12:23:36,957 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Полная информация: {'name': 'Sergiy’s AirPods', 'index': 1, 'hostapi': 0, 'max_input_channels': 0, 'max_output_channels': 2, 'default_low_input_latency': 0.01, 'default_low_output_latency': 0.16133333333333333, 'default_high_input_latency': 0.1, 'default_high_output_latency': 0.17066666666666666, 'default_samplerate': 48000.0}
2025-12-01 12:23:36,957 - modules.speech_playback.core.player - INFO - 🎯 Используем системное устройство по умолчанию от macOS
2025-12-01 12:23:36,957 - modules.speech_playback.core.player - INFO - 📊 [AUDIO_STATS] Конфигурация плеера: sample_rate=48000Hz, channels=2, dtype=int16
2025-12-01 12:23:36,957 - modules.speech_playback.macos.performance - WARNING - ⚠️ Мониторинг уже запущен
2025-12-01 12:23:36,957 - modules.speech_playback.core.player - WARNING - ⚠️ [OUTPUT] Мониторинг output устройства уже запущен
2025-12-01 12:23:36,957 - modules.speech_playback.core.player - INFO - ✅ [AUDIO_SUCCESS] Sequential Speech Player инициализирован успешно
2025-12-01 12:23:36,957 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] _start_audio_stream вызван: sync_output=True, device_id=None
^N^N^N^N^N^N^N^N^N2025-12-01 12:23:37,673 - modules.speech_playback.core.player - INFO - 🔄 [OUTPUT] Для BT устройства создаем stream с device=None (macOS управляет параметрами)
2025-12-01 12:23:37,676 - modules.speech_playback.core.player - INFO - 🔧 [OUTPUT] Для BT устройства: device=None, channels=2, без blocksize/latency
2025-12-01 12:23:37,676 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Устройство должно быть освобождено после ошибки -9986
2025-12-01 12:23:37,680 - modules.speech_playback.core.player - INFO - ⏳ [OUTPUT] Повторная попытка через 1.80с (экспоненциальный backoff ×1.5, попытка 2/5)...
^N^N^N^N^N^N^N^N^N^N^N^N^N^N^N^N^N^N^N^N^N2025-12-01 12:23:39,485 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Старый поток закрыт → создаём новый stream (попытка 2/5)
2025-12-01 12:23:39,486 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Попытка 3/5 создания потока...
2025-12-01 12:23:39,486 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Подтверждение: старый поток закрыт → создаём новый stream
2025-12-01 12:23:39,486 - modules.speech_playback.core.player - INFO -    Устройство: Sergiy’s AirPods (ID=System Default, BT=True)
2025-12-01 12:23:39,486 - modules.speech_playback.core.player - INFO -    Параметры: device=None, channels=2, samplerate=48000, blocksize=N/A, latency=N/A
2025-12-01 12:23:39,486 - modules.speech_playback.core.player - INFO -    SwitchAudioSource → device=None для BT (macOS управляет параметрами)
2025-12-01 12:23:39,486 - modules.speech_playback.core.player - DEBUG - 🔍 [OUTPUT] Параметры потока: {'device': None, 'channels': 2, 'dtype': 'int16', 'samplerate': 48000, 'callback': <bound method SequentialSpeechPlayer._audio_callback of <modules.speech_playback.core.player.SequentialSpeechPlayer object at 0x1182d27b0>>}
2025-12-01 12:23:39,486 - modules.speech_playback.core.player - INFO - 🔍 [OUTPUT] Создаем новый поток: device=None, BT=True
||PaMacCore (AUHAL)|| Warning on line 521: err=''!obj'', msg=Unknown Error
||PaMacCore (AUHAL)|| Warning on line 441: err=''!obj'', msg=Unknown Error
||PaMacCore (AUHAL)|| Error on line 1332: err='-10851', msg=Audio Unit: Invalid Property Value
2025-12-01 12:23:39,489 - modules.speech_playback.core.player - ERROR - ❌ [OUTPUT] Попытка 3/5 создания потока не удалась (время: 4.75с)
2025-12-01 12:23:39,489 - modules.speech_playback.core.player - ERROR -    Устройство: Sergiy’s AirPods (ID=System Default, BT=True)
2025-12-01 12:23:39,489 - modules.speech_playback.core.player - ERROR -    Параметры: device=None, channels=2, samplerate=48000, blocksize=N/A, latency=N/A
2025-12-01 12:23:39,489 - modules.speech_playback.core.player - ERROR -    Ошибка: PortAudioError: Error opening OutputStream: Internal PortAudio error [PaErrorCode -9986]
2025-12-01 12:23:39,489 - modules.speech_playback.core.player - ERROR -    is_error_9986=True, is_error_10851=False
2025-12-01 12:23:39,489 - modules.speech_playback.core.player - WARNING - ⚠️ [OUTPUT] Обнаружена ошибка -9986 (Internal PortAudio error) - устройство может быть занято
2025-12-01 12:23:39,489 - modules.speech_playback.core.player - INFO - 💡 [OUTPUT] Рекомендация: убедитесь, что старый поток полностью закрыт
2025-12-01 12:23:39,489 - modules.speech_playback.core.player - DEBUG -    Детали ошибки:
Traceback (most recent call last):
  File "/Users/sergiyzasorin/Development/Nexy/client(prod)/modules/speech_playback/core/player.py", line 877, in _start_audio_stream
    self._audio_stream = sd.OutputStream(**stream_config)
                         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/Users/sergiyzasorin/Development/Nexy/client(prod)/.venv/lib/python3.13/site-packages/sounddevice.py", line 1515, in __init__
    _StreamBase.__init__(self, kind='output', wrap_callback='array',
    ~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                         **_remove_self(locals()))
                         ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sergiyzasorin/Development/Nexy/client(prod)/.venv/lib/python3.13/site-packages/sounddevice.py", line 909, in __init__
    _check(_lib.Pa_OpenStream(self._ptr, iparameters, oparameters,
    ~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                              samplerate, blocksize, stream_flags,
                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                              callback_ptr, userdata),
                              ^^^^^^^^^^^^^^^^^^^^^^^^
           f'Error opening {self.__class__.__name__}')
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sergiyzasorin/Development/Nexy/client(prod)/.venv/lib/python3.13/site-packages/sounddevice.py", line 2804, in _check
    raise PortAudioError(errormsg, err)
sounddevice.PortAudioError: Error opening OutputStream: Internal PortAudio error [PaErrorCode -9986]
2025-12-01 12:23:39,491 - modules.speech_playback.core.player - WARNING - ⚠️ [OUTPUT] Ошибка -9986: устройство может быть занято старым потоком
2025-12-01 12:23:39,491 - modules.speech_playback.core.player - INFO - 🔄 [OUTPUT] Вызываем _stop_audio_stream() для гарантированного освобождения устройства...
2025-12-01 12:23:39,492 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Используем is_bluetooth=True из текущей попытки (устройство: "Sergiy’s AirPods")
2025-12-01 12:23:39,492 - modules.speech_playback.core.player - INFO - ⏳ [OUTPUT] Задержка для освобождения устройства после ошибки: 1.0с...
^N^N^N^N^N^N^N^N^N^N^N^N2025-12-01 12:23:40,497 - modules.speech_playback.core.player - INFO - 🔄 [OUTPUT] Для BT устройства создаем stream с device=None (macOS управляет параметрами)
2025-12-01 12:23:40,497 - modules.speech_playback.core.player - INFO - 🔧 [OUTPUT] Для BT устройства: device=None, channels=2, без blocksize/latency
2025-12-01 12:23:40,497 - modules.speech_playback.core.player - INFO - ✅ [OUTPUT] Устройство должно быть освобождено после ошибки -9986
2025-12-01 12:23:40,497 - modules.speech_playback.core.player - INFO - ⏳ [OUTPUT] Повторная попытка через 3.60с (экспоненциальный backoff ×1.5, попытка 3/5)...
^N^N^N^N2025-12-01 12:23:40,763 - modules.input_processing.keyboard.keyboard_monitor - DEBUG - 🔑 Combo deactivation: LONG_PRESS уже был, генерируем RELEASE
🔑 SYNC RELEASE: 5.040с
2025-12-01 12:23:41,786 - modules.speech_playback.macos.performance - DEBUG - 📊 CPU: 9.6%, Memory: 80.5%
2025-12-01 12:23:44,102 - 