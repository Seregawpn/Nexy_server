# Task
Исправить runtime-ошибку VoiceOver AppleScript:
`execution error: The variable speechMuted is not defined. (-2753)`.

# Root Cause
- В AppleScript командах использовалось свойство `speechMuted`.
- На целевой системе VoiceOver-словарь ожидает форму `speech muted`.

# Changes
- Файл: `modules/voiceover_control/core/controller.py`
- Обновлены команды:
  - `return speechMuted` -> `return speech muted`
  - `set speechMuted to ...` -> `set speech muted to ...`
  - Аналогично в статус-проверке `_check_voiceover_status`.

# Validation
- `python3 -m py_compile modules/voiceover_control/core/controller.py` — OK.

# Expected Log Impact
- Должна исчезнуть ошибка:
  - `VoiceOver: CalledProcessError ... variable speechMuted is not defined`.
- При недоступности команды будет работать существующий fallback-путь.
