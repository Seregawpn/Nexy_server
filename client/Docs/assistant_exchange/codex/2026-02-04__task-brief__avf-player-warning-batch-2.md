# Task Brief

## Context
Следующим top-файлом после приоритизации был `modules/speech_playback/core/avf_player.py` (22 warning basedpyright).

## Changes
- Централизован доступ к AVFoundation/Foundation символам на уровне модуля:
  - `AVAudioEngine`, `AVAudioFormat`, `AVAudioPCMBuffer`, `AVAudioPlayerNode`, `AVAudioSession`, `AVAudioSessionRouteChangeNotification`, `NSNotificationCenter`.
- Убраны локальные `from AVFoundation/Foundation import ...` внутри методов.
- Добавлены runtime-guards перед использованием нативных символов (fallback/early return с логом).
- Усилены null-guards для `self._engine`/`self._player_node` в:
  - `start_playback`
  - `_playback_loop`
  - `_ensure_engine_running`
- Уточнен тип очереди:
  - `self._audio_queue: queue.Queue[dict[str, Any] | None]`.
- Убраны optional-member обращения на критичных путях рестарта/планирования буфера.

## Verification
- `./.venv/bin/ruff check modules/speech_playback/core/avf_player.py` → OK
- `../server/.venv/bin/basedpyright modules/speech_playback/core/avf_player.py --outputjson` → 0 diagnostics
- `./scripts/problem_scan.sh` → `TOTAL_ISSUES=369`
- `REQUIRE_BASEDPYRIGHT_IN_SCAN=true ./scripts/problem_scan_gate.sh` → PASSED

## Impact
- В `avf_player.py`: warning reduced `22 -> 0`.
- Общий backlog reduced: `391 -> 369`.
- Логика AVFoundation интеграции стала более централизованной и безопасной для optional-state.
