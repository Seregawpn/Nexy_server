## Что изменено
- Переведен playback на стандартный режим без авто-усиления чанков по умолчанию.

## Измененные файлы
- `config/unified_config.yaml`
  - `speech_playback.tts_auto_gain_enabled: false`
- `config/unified_config_loader.py`
  - default `tts_auto_gain_enabled` изменен на `False`
- `integration/integrations/speech_playback_integration.py`
  - fallback/default чтения `tts_auto_gain_enabled` изменен на `False`

## Проверка
- `python3 -m py_compile integration/integrations/speech_playback_integration.py` — OK
- `python3 -m py_compile config/unified_config_loader.py` — OK

## Ожидаемый результат
- Звук воспроизводится в стандартной амплитуде потока сервера, без клиентского переусиления и без артефактов от auto-gain.
