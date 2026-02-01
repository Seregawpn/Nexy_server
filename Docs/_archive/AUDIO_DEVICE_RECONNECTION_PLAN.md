# План по надёжному переключению аудио-устройств

## Цель
Создать отдельный документ с пошаговым планом реализации безопасного reconnect для OUTPUT звука, опираясь на текущую архитектуру (AudioStreamManager, SequentialSpeechPlayer, DeviceChangePublisher).

## 1. Цикл 1 — Защита и последовательность
- **Задача**: гарантировать, что `_switch_output_device` запускается только после завершения предыдущей последовательности «stop → refresh params → open».
- **Действия**:
  1. Добавить флаг `_switch_in_progress` и/или `threading.Lock` в `SequentialSpeechPlayer`.
  2. В `device.default_output_changed` сравнивать новое имя/ID с сохранённым; если изменилось и guard свободен — запускать `_switch_output_device`.
  3. Логировать вход и выход guard (статус, старое/новое устройство, причина — Core Audio vs manual).
  4. Убедиться, что `_stop_event` сбрасывается только после завершения операций (удача/ошибка).

## 2. Цикл 2 — Актуальные параметры и fallback
- **Задача**: всегда использовать свежую конфигурацию; при ошибках PortAudio переходить на fallback.
- **Действия**:
  1. Перед `AudioStreamManager.create_stream`/`switch_device` логировать параметры (`device_id`, `samplerate`, `channels`, `blocksize`, `latency`, `is_bluetooth`) и попытку.
  2. Вести cache `last_successful_config` для конкретных `device_name|BT`, чтобы повторно использовать проверенные значения.
  3. На повторный `PaErrorCode -9986/-10851` переключать `StreamConfig` на `device=None`, очищать `blocksize/latency`, чтобы macOS сама подобрала параметры.
  4. После успешного запуска обновлять `config.sample_rate`, `config.channels`, очищать guard, сбрасывать `_stop_event`, записывать `duration_ms`.

## 3. Цикл 3 — Переинициализация при новом устройстве
- **Задача**: при появлении нового девайса перезапустить поток в правильном порядке.
- **Действия**:
  1. На событии `device.default_output_changed` сохранять новое имя/ID, очищать `chunk_buffer`, выставлять `_stop_event`, затем стартовать `_switch_output_device`.
  2. Удерживать guard до ответа от `AudioStreamManager.switch_device`.
  3. При успехе обновлять `output_device_name/_id/_is_current_device_bluetooth` и снова очищать `_stop_event`.
  4. При ошибке guard обнуляется, но метки имени/ID сохраняются, чтобы избежать повторной ініциации без явной смены.

## 4. Валидация и контроль
- **Менеджмент**:
  - Протестировать поведение при смене обычного и BT устройств.
  - Проверить, что guard не остается заблокированным (`_switch_in_progress` = False) и `_stop_event` очищается после ошибок.
  - Засечь время переключения — оно должно быть коротким без таймаутов 15+ с.
  - Обратить внимание на логи PortAudio, чтобы fallback запускался при `-9986/-10851`.

## 5. Следующие шаги
- Реализовать guard + cache + fallback в коде (см. `modules/speech_playback/core/player.py`, `modules/audio_core/stream_manager.py`).
- Обновить документацию (включая текущий анализ) ссылками на этот план.
- Добавить тесты для edge cases: быстрые device change события, BT vs обычные, ошибки PortAudio.
