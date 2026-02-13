## Что изменено
- В `AVFoundationPlayer` понижен уровень логирования для нулевых чанков после извлечения из очереди:
  - было: `ERROR`
  - стало: `DEBUG`

## Почему
- Нулевые чанки ожидаемы на silent-tail участках потокового TTS.
- `ERROR` создавал ложные тревоги и шум в диагностике.

## Файл
- `modules/speech_playback/core/avf_player.py`

## Проверка
- `python3 -m py_compile modules/speech_playback/core/avf_player.py` — OK
