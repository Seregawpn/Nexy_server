# Task Brief: signal audibility profile centralization

## Problem
Сигналы `listen_start/done/error/cancel` были слабо различимы по звуку в реальном потоке, из-за чего `done` на `processing -> sleeping` воспринимался как "не проигрался".

## Root cause
`SignalIntegration` отправлял только `pattern/kind`, без явных аудио-параметров, поэтому все cue генерировались с дефолтными значениями (`tone_hz=880`, `duration_ms=120`, `volume=0.2`).

## Change
- Добавлен централизованный профиль аудио-паттернов в `SignalIntegration`:
  - `LISTEN_START`: 880Hz / 120ms / 0.22
  - `DONE`: 1040Hz / 220ms / 0.36
  - `ERROR`: 420Hz / 260ms / 0.34
  - `CANCEL`: 560Hz / 140ms / 0.28
- Все emit-ветки переведены на единый helper `_emit_audio_pattern(...)`.

## Result
- Убран "скрытый дубликат" поведения по умолчанию.
- Сигнал `DONE` стал акустически отдельным и заметным.
- Централизация сохранена: владелец маппинга cue остается один (`SignalIntegration`).

## Validation
- `PYTHONPATH=. pytest -q tests/test_signal_integration_cancel_done_suppression.py tests/test_interrupt_playback.py tests/test_processing_workflow_session_guard.py`
- `22 passed`

