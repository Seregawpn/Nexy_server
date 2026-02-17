# Task Brief: Audio Session Reassert Dedup and Owner Guard (2026-02-17)

## Goal
Снизить остаточные конфликты аудио-owner при VoiceOver, убрав лишние reassert/recovery циклы на no-op playback path.

## What was changed
1. `SpeechPlaybackIntegration`:
- `_ensure_player_ready()` получил флаг `reassert_profile` (по умолчанию `False`).
- Обычная очередь аудио больше не принуждает reassert профиля на каждом вызове.
- В `_on_voice_mic_closed()` добавлен dedup-guard по сессии/времени.
- Recovery после `voice.mic_closed` теперь выполняет явный reassert ровно в owner-path (`reassert_profile=True`).

2. `AVFoundationPlayer`:
- `start_playback()` получил флаг `reassert_session`.
- Убран безусловный reassert профиля на idempotent no-op path.
- Reassert в no-op выполняется только при явном запросе (`reassert_session=True`).
- При реальном старте playback профиль как и раньше обеспечивается.

3. Тесты:
- Добавлен тест `test_playback_mic_recovery_dedup_and_reassert_once`.
- Проверяет, что повторные `voice.mic_closed` для одной сессии дедуплицируются,
  и recovery/reassert запускается только один раз.

## Architecture Gates
- Single Owner Gate: соблюден (audio transitions остаются в owner integration path).
- Zero Duplication Gate: соблюден (дублирующий reassert на no-op path убран).
- Anti-Race Gate: усилен (dedup guard + single owner recovery trigger).
- Flag Lifecycle Gate: без изменений флагов.

## Verification
- `PYTHONPATH=. pytest -q tests/test_voice_audio_owner_guards.py tests/test_interrupt_playback.py tests/test_speech_playback_session_id.py`
  - Result: `22 passed`
- `python3 scripts/verify_architecture_guards.py`
  - Result: `Architecture guards OK`
- `python3 scripts/verify_feature_flags.py`
  - Result: `Feature flags registry OK`

## Информация об изменениях
- Что изменено:
  - Убран безусловный playback profile reassert в no-op path.
  - Добавлен dedup для `voice.mic_closed` recovery.
  - Добавлен тест на dedup/reassert behavior.
- Список файлов:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/integration/integrations/speech_playback_integration.py`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/modules/speech_playback/core/avf_player.py`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/tests/test_voice_audio_owner_guards.py`
- Причина/цель изменений:
  - Уменьшить вероятность owner-конфликтов (`session=(null)`) за счет устранения лишних reassert/recovery циклов.
- Проверка (что выполнено для валидации):
  - Локальные тесты (22 passed), architecture guards OK, feature flags OK.
