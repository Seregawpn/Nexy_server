## Что сделано
- В `SpeechPlaybackIntegration` заменен session-pinned `tts` gain на адаптивный chunk-level gain.
- Добавлены guards против клиппинга:
  - `tts_safe_max_gain` (default `2.5`)
  - `tts_headroom_peak` (default `0.90`)
  - `tts_gain_ema_alpha` (default `0.25`)
- Добавлен диагностический `clip_ratio` в лог `AUDIO_GAIN`.
- Удален старый state `self._tts_gain_by_session`, вместо него используется `self._tts_peak_ema_by_session`.

## Файлы
- `integration/integrations/speech_playback_integration.py`

## Проверка
- `python3 -m py_compile integration/integrations/speech_playback_integration.py` — OK.

## Ожидаемый эффект
- Значительно меньше систематического saturation до `0.98`.
- Меньше искажений на неравномерной динамике TTS-чанков.
