# Task Brief: VoiceOver hard-toggle через конфиг

## Запрос
Не удалять hard-toggle поведения VoiceOver, а оставить возможность включать/выключать через конфигурацию.

## Что сделано
- В `VoiceOverControlSettings` добавлен флаг `hard_toggle_enabled: bool = False`.
- В `VoiceOverController` добавлен state-флаг `_hard_toggled_by_us` для корректного release только если выключали через hard-toggle.
- В duck-пути:
  - при `hard_toggle_enabled=true` используется `Command+F5`;
  - при `hard_toggle_enabled=false` используется speech-only стратегия (mute/stop speaking).
- В release-пути:
  - если был hard-toggle — обратный `Command+F5`;
  - иначе восстановление речи через `speechMuted=false`.
- В `config/unified_config.yaml` добавлен ключ:
  - `accessibility.voiceover_control.hard_toggle_enabled: false` (по умолчанию безопасно, VoiceOver не выключается).

## Проверка
- `python3 -m py_compile modules/voiceover_control/core/controller.py` — OK.
- По коду: hard-toggle не удален, а управляется только конфигом.
