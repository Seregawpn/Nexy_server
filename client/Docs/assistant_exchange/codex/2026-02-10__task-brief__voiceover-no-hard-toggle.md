# Task Brief: VoiceOver не выключается при ducking

## Контекст
- Запрос: «Сделай так чтобы VoiceOver не выключался».
- Зона: `voiceover_ducking_integration` → `modules/voiceover_control/core/controller.py`.

## Root Cause
- В `VoiceOverController._send_duck_command_sync()` ducking всегда вызывал `Command+F5`.
- `Command+F5` переключает весь сервис VoiceOver (ON/OFF), а не только речь.
- В `release()` использовался тот же hard-toggle для «восстановления», что закрепляло поведение выключения.

## Изменения
- `release()`:
  - убран auto-вызов `Command+F5`;
  - при `mute_speech` теперь выполняется `set speechMuted to false`;
  - обновлены логи на восстановление речи, а не сервиса VoiceOver.
- `_ensure_ducked()`:
  - теперь принимает результат duck-команды как `(success, muted_by_us)`;
  - перестал помечать VoiceOver как «выключенный».
- `_send_duck_command_sync()`:
  - переписан на безопасную стратегию без выключения VoiceOver:
  - `mode=mute_speech` → `set speechMuted to true`;
  - `mode=stop` → `stop speaking` (best-effort, повторы по конфигу).
- `_stop_voiceover_speaking()`:
  - возвращает `bool` для корректной агрегации успеха.

## Проверка
- `python3 -m py_compile modules/voiceover_control/core/controller.py` — OK.
- Ручная проверка: в автоматическом duck/release пути больше нет `Command+F5`.

## Риск
- Низкий: изменение локализовано в одном владельце логики (`VoiceOverController`) без новых источников истины.
