# Task
Снизить спам warning в `AVF_PLAYER [ADD_AUDIO]` (`TOTALLY SILENT` / `very quiet`).

# Changes
- Файл: `modules/speech_playback/core/avf_player.py`
- Добавлены поля rate-limit состояния:
  - `_add_audio_warn_cooldown_sec = 5.0`
  - таймстемпы и счетчики suppressed для silent/quiet warning.
- Добавлен метод `_log_add_audio_level_warning(silent: bool, peak: float)`.
- В `add_audio_data()` прямые warning заменены на вызов rate-limit helper.
- Теперь повторяющиеся события в окне 5 секунд подавляются и агрегируются:
  - логируется одна строка + `suppressed N similar in 5.0s`.

# Validation
- `python3 -m py_compile modules/speech_playback/core/avf_player.py` — OK.

# Expected Log Impact
- Резкое уменьшение количества строк:
  - `Incoming audio is TOTALLY SILENT`
  - `Incoming audio is very quiet`
- Диагностика сохраняется, но без flood в логе.
