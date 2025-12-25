# Критические исправления для MVP-12

**Дата**: 2025-12-23  
**Статус**: Критичные патчи для стабильности Exit Gate

---

## Проблема 1: `startAndReturnError_` вызывается неправильно

**Файл**: `mvp6_output_playback/test_output_playback.py`, `mvp12_full_input_output/test_full_input_output.py`

**Проблема**: В PyObjC `NSError**` нужно принимать как output-аргумент.

**Решение**: Добавить helper метод `_engine_start()` в `OutputPlaybackPrototype`.

---

## Проблема 2: `AVAudioSession` на macOS

**Файл**: `mvp6_output_playback/test_output_playback.py`, `mvp12_full_input_output/test_full_input_output.py`

**Проблема**: `AVAudioSession` может быть нестабилен на macOS.

**Решение**: Убрать/загейтить `AVAudioSession`, использовать только `AVAudioEngine`.

---

## Проблема 3: Device switching работает только если ОС поменяла default

**Файл**: `mvp12_full_input_output/test_full_input_output.py`

**Проблема**: Сравнение только по `uid`, который может быть `portaudio_{index}` и меняться при storm.

**Решение**: Сравнивать `uid+name+sample_rate+channels`, добавить debounce.

---

## Проблема 4: Конфликт владения микрофоном

**Файл**: `mvp12_full_input_output/test_full_input_output.py`

**Проблема**: `self.current_recognizer` используется из worker thread, не thread-safe.

**Решение**: Создавать `Recognizer()` локально в `_recognize_and_play_worker`.

---

## Проблема 5: Гонки вокруг engine + player node

**Файл**: `mvp6_output_playback/test_output_playback.py`

**Проблема**: `OutputPlaybackPrototype` не полностью потокобезопасен.

**Решение**: Сделать все публичные методы потокобезопасными с внутренним lock.

---

## Проблема 6: PTT логика edge-case

**Файл**: `mvp12_full_input_output/test_full_input_output.py`

**Проблема**: `on_release` не проверяет `is_recording` перед `_stop_recording()`.

**Решение**: Добавить проверку `if self.key_pressed and self.is_recording:`.

---

## Проблема 7: Ресемплинг без антиалиасинга

**Файл**: `mvp12_full_input_output/test_full_input_output.py`

**Проблема**: Линейный ресемплинг может ухудшать распознавание.

**Решение**: Добавить простейший low-pass фильтр перед downsample.

---

## Проблема 8: Exit Gate "переключение output устройств работает"

**Файл**: `mvp12_full_input_output/test_full_input_output.py`

**Проблема**: `_switch_output_device()` не переключает output, только реагирует на смену.

**Решение**: Обновить документацию, честно указать ограничение.

---

## Проблема 9: Decision-логи отсутствуют

**Файл**: `mvp12_full_input_output/test_full_input_output.py`

**Проблема**: Нет канонических decision-логов для gateway решений.

**Решение**: Добавить decision-логи в каноническом формате.

