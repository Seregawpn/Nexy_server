# Task Brief: STT unknown_value callback race fix

## Context
Во время удержания `Ctrl+N` в логах появлялся `unknown_value` в непрерывном режиме, после чего при `release` Processing мгновенно завершался по `failed_recognition` без gRPC.

## Diagnosis
В `VoiceRecognitionIntegration` терминальность ошибки определялась в async-публикации, а не в момент callback от GoogleSRController. Из-за этого `unknown_value`, полученный во время удержания, мог быть обработан уже после release как terminal failure.

## Architecture Fit
- Owner: `VoiceRecognitionIntegration` (STT lifecycle/events)
- Source of truth: callback-time состояние `ptt_pressed + _recording_active`
- Централизация сохранена: `ProcessingWorkflow` не получил новый обходной путь.

## Implementation
В `integration/integrations/voice_recognition_integration.py`:
1. В `_on_sr_v2_failed` зафиксировано callback-time состояние удержания:
   - `was_listening_at_callback`.
2. В `_publish_v2_failed` добавлен параметр `was_listening_at_callback`.
3. Если ошибка возникла во время удержания (даже если coroutine исполнилась после release), событие не публикуется как terminal `voice.recognition_failed`.

## Concurrency / Race Guard
Использован существующий `_state_lock` и callback-time snapshot для устранения out-of-order эффекта между callback thread и async loop.

## Verification
- `python3 -m py_compile integration/integrations/voice_recognition_integration.py` — OK.
- Проверка diff: terminal `recognition_failed` больше не эмитится для callback, пришедшего во время hold.

## Информация об изменениях
- Что изменено:
  - Устранена race-ошибка терминализации `unknown_value` после release.
  - Ошибки, произошедшие во время удержания, остаются non-terminal.
- Список файлов:
  - `integration/integrations/voice_recognition_integration.py`
  - `Docs/assistant_exchange/codex/2026-02-17__task-brief__stt-unknown-value-callback-race-fix.md`
- Причина/цель изменений:
  - Убрать сценарий, когда пользователь говорит, но цикл обрывается в `failed_recognition` без gRPC.
- Проверка:
  - Синтаксис проверен (`py_compile`), race-path закрыт callback-time guard.
