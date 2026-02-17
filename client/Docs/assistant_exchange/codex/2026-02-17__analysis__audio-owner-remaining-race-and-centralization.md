# Audio Owner: Remaining Race and Centralization (2026-02-17)

## Context
Запрос пользователя: определить точные части, где остаётся ошибка, и что нужно централизовать для полного устранения конфликта VoiceOver.

## Diagnosis
По текущему `voiceover.md` конфликт фиксируется как `Python + VoiceOver` с сигнатурой:
`Found 2 different sessions ... will use session=(null)`.

Критичный вывод: в dev-режиме конфликт owner-аудиосессии остаётся, несмотря на уже внесённые guard-фиксы.

## Root Cause (remaining)
1. Reassert playback profile на каждом `start_playback()` (включая no-op path) может повторно дергать ownership и route.
2. Recovery по `voice.mic_closed` всё ещё может приводить к лишним reassert-циклам при пограничных состояниях.
3. Не все переходы lifecycle аудио гарантированно проходят через один transition-owner guard.

## Precise code touchpoints
- `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/modules/speech_playback/core/avf_player.py`
  - `start_playback()`
  - `_ensure_playback_audio_session()`
- `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/integration/integrations/speech_playback_integration.py`
  - `_on_voice_mic_closed()`
  - `_ensure_player_ready()`
- `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/integration/integrations/voice_recognition_integration.py`
  - `_on_recording_stop()`
  - `_publish_mic_closed()`
  - `_resolve_callback_session_id()`

## What to centralize
Single owner for audio transitions:
- enter_listening
- leave_listening
- mic_closed_recovery
- playback_reassert

Все эти переходы должны идти через один guard по `session_id` (single-flight + stale-drop + idempotency).

## Verification target
- 0 строк `session=(null)` в fresh dev-run.
- Нет лишних циклов reassert после `voice.mic_closed`.
- Нет start/stop churn в пределах одного voice turn.

## Verification
- `rg -n "Found 2 different sessions|session=\(null\)" voiceover.md`
- `rg -n "def start_playback|_ensure_playback_audio_session|_on_voice_mic_closed|_on_recording_stop|_publish_mic_closed|_resolve_callback_session_id"` по указанным файлам

## Информация об изменениях
- Что изменено:
  - Добавлен analysis-отчет с точными проблемными узлами и планом централизации.
- Список файлов:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/Docs/assistant_exchange/codex/2026-02-17__analysis__audio-owner-remaining-race-and-centralization.md`
- Причина/цель изменений:
  - Зафиксировать конкретные части кода, где остаётся источник конфликта, и что централизовать.
- Проверка (что выполнено для валидации):
  - Проведён grep по логам и по функциям lifecycle/owner-path.
  - Изменения в код не вносились.
