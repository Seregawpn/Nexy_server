# Task
Убрать повторяющийся warning-флуд VoiceOver AppleScript после фикса `speechMuted`.

# Problem
- Даже при fallback лог продолжал шуметь `CalledProcessError` из `_run_osascript`
  при проверках/установке `speech muted`.

# Changes
- Файл: `modules/voiceover_control/core/controller.py`
- Добавлен параметр `quiet_errors` в `_run_osascript(...)`.
- Для операций `speech muted` (`get/set` + status check) включен `quiet_errors=True`.
- Добавлен guard в статус-чеке: не дергать `speechMuted`, когда `VoiceOver not running`.

# Result
- Ошибки `speech muted` обрабатываются как ожидаемая unsupported-ветка (через existing fallback),
  без warning-флуда.
- Диагностика остаётся в `DEBUG`.

# Validation
- `python3 -m py_compile modules/voiceover_control/core/controller.py` — OK.
