# AVF engine restart owner fix

## Context
На старте приветствия аудио попадало в очередь, но не проигрывалось.
В логах: повторяющийся цикл `Engine not running, waiting before retry...`.

## Root Cause
В `modules/speech_playback/core/avf_player.py` recovery-логика перезапуска `AVAudioEngine` была структурно вынесена из `_ensure_engine_running()` после `return` в соседний блок, из-за чего фактически не исполнялась.

## Change
- Восстановлен единый владелец восстановления движка: `_ensure_engine_running()`.
- Логика restart/backoff/reconnect playerNode возвращена внутрь `_ensure_engine_running()`.
- Из `_maybe_recreate_for_render_stall()` удален ошибочно попавший дублирующий блок restart.

## Verification
- `python3 -m py_compile modules/speech_playback/core/avf_player.py` — OK.
- По коду: `_ensure_engine_running()` снова содержит restart-путь и вызывается в runtime scheduling loop.

## Architectural impact
- Source of Truth для runtime-восстановления: `AVFoundationPlayer._ensure_engine_running`.
- Дублирование и второй путь восстановления убраны.
