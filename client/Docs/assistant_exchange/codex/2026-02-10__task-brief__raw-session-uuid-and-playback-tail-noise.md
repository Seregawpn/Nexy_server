# Task Brief: raw session UUID and playback tail noise

## Context
- После стабилизации quit-path в логах оставались:
  - `Session ID validation failed for 'raw:welcome_message:...'`
  - `Finalize timeout waiting idle ...` для welcome/raw playback.

## Diagnosis
- `playback.raw_audio` генерировал legacy `session_id` формата `raw:<pattern>:<ts>`, невалидный для UUID-only селекторов.
- Финализация raw playback иногда упиралась в небольшой tail buffer AVFoundation и давала warning при уже пустой очереди.

## Change
- `integration/integrations/speech_playback_integration.py`:
  - добавлен `_ensure_raw_session_id()`:
    - сохраняет валидный UUIDv4,
    - генерирует новый UUIDv4 для `None`/legacy non-UUID.
  - `_on_raw_audio` теперь всегда использует UUID session_id.
  - добавлен трекинг raw-сессий (`_raw_sessions`).
  - в `_finalize_on_silence` понижен шум:
    - для raw-сессий при `queue_empty=True` и малом tail (`buffered_sec <= 0.35`) логируется info вместо warning.
  - cleanup `_raw_sessions` добавлен в cancel/failed/finalize пути.

## Tests
- Добавлены тесты:
  - `tests/test_speech_playback_session_id.py` (3 unit tests)
- Прогон:
  - `pytest -q tests/test_speech_playback_session_id.py` -> `3 passed`
  - `pytest -q tests/test_user_quit_ack.py` -> `2 passed`
  - `pytest -q tests/verify_menu_quit_fix.py` -> `2 passed`

## Architecture fit
- Source of Truth сохранён:
  - session_id остается в едином формате, совместимом с селекторами.
- Без новых owner/state-path; только нормализация существующего playback потока.
