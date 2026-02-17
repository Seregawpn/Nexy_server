# Task Brief: VoiceOver audio owner guard implementation

## Context
Реализованы кодовые правки для стабилизации audio lifecycle при конкуренции с VoiceOver без нарушения owner-архитектуры.

## Implementation
1. `GoogleSRController` получил session-bound callback context:
- добавлен `session_id` в `GoogleSRResult`;
- добавлен `session_id_getter` в конструктор;
- session id закрепляется на start/listen cycle и передается в completion/failure callbacks;
- исправлен callback contract `on_failed(error, session_id)`;
- устранен дубль запуска recognition thread в capture-loop.

2. `VoiceRecognitionIntegration`:
- пробрасывает `session_id_getter` в `GoogleSRController`;
- добавлен stale-session guard `_resolve_callback_session_id(...)`;
- `_on_sr_v2_completed/_on_sr_v2_failed` используют callback session вместо косвенного active-session;
- `voice.mic_closed` дедуплицируется по session (а не только по `(session, source)`), чтобы исключить повторные side-effects после `recording_stop`;
- snapshot terminal path теперь отменяет fallback (`_cancel_stop_terminal_fallback`) при успешной terminal публикации.

3. `SpeechPlaybackIntegration`:
- `_on_voice_mic_closed` игнорирует stale session относительно `active_output_session_id`;
- recovery reassert выполняется только при валидном playback context.

4. Добавлены тесты owner-guard логики:
- `tests/test_voice_audio_owner_guards.py`
  - дедуп `voice.mic_closed` между `recording_stop` и `v2_completed` для одной сессии;
  - stale callback session guard;
  - stale `voice.mic_closed` не триггерит playback recovery.

## Verification
- `PYTHONPATH=. pytest -q tests/test_voice_audio_owner_guards.py tests/test_interrupt_playback.py tests/test_speech_playback_session_id.py`
  - результат: `21 passed`
- `python3 scripts/verify_architecture_guards.py`
  - результат: OK
- `python3 scripts/verify_feature_flags.py`
  - результат: OK
- `python3 -m py_compile` для измененных файлов
  - результат: OK

## Информация об изменениях
- Что изменено:
  - Реализованы session-bound guards для STT callbacks, дедуп `mic_closed` и stale-session фильтрация playback recovery.
  - Добавлены тесты на новые guard-сценарии.
- Список файлов:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/modules/voice_recognition/core/google_sr_controller.py`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/integration/integrations/voice_recognition_integration.py`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/integration/integrations/speech_playback_integration.py`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/tests/test_voice_audio_owner_guards.py`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/Docs/assistant_exchange/codex/2026-02-16__task-brief__voiceover-audio-owner-guard-implementation.md`
- Причина/цель изменений:
  - Устранить race/out-of-order эффекты в audio lifecycle, совместимые с VoiceOver runtime.
- Проверка (что выполнено для валидации):
  - Целевые тесты + архитектурные/flag-гейты + компиляция измененных модулей.
