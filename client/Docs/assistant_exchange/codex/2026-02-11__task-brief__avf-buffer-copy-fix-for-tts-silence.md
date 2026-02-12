# AVF Buffer Copy Fix For TTS Silence

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-11
- ID (INS-###): n/a

## Diagnosis
Приходят `grpc.response.audio` и стартует `AVAudioEngine`, но часть сессий не слышна: копирование сэмплов в `AVAudioPCMBuffer` было нестабильным и могло оставлять буфер пустым (тишина).

## Root Cause
Нестабильный/дублирующийся путь записи в `floatChannelData` (экспериментальный код + незащищенные fallback) → периодический сбой записи PCM в buffer → `playback.started` есть, слышимого звука нет.

## Optimal Fix
Цель: сделать один детерминированный owner-путь копирования PCM в AVFoundation buffer, без дублирующей логики.

- Architecture Fit: внутри существующего owner модуля `modules/speech_playback/core/avf_player.py`.
- Source of Truth: `AVFoundationPlayer._playback_loop` как единственный владелец конверсии и копирования в `AVAudioPCMBuffer`.
- Breaks architecture: no.

План:
1. Удалить экспериментальные ветки копирования и оставить канонический путь `memmove` по `__pyobjc_object__`.
2. Оставить один fallback: indexed copy в `ptr[i]` при недоступности pointer-copy.
3. При провале обоих путей не планировать буфер (`continue`), чтобы не публиковать «ложное» воспроизведение.
4. Упростить диагностику `peak` без лишнего расхода (`len(list(range))`).

## Verification
- `python3 -m py_compile modules/speech_playback/core/avf_player.py integration/integrations/speech_playback_integration.py`
- Runtime DoD:
  - нет `AUDIO WILL BE SILENT - unable to write to AVAudioPCMBuffer`
  - есть `TRACE phase=playback.start ... session=<sid>`
  - есть `TRACE phase=playback.end ... finalized=true`
  - есть `playback.completed` для сессии

## Pre-Change Gate Evidence (обязательно)
- Прочитанные документы:
  - `/Users/sergiyzasorin/Fix_new/client/Docs/DOCS_INDEX.md`
  - `/Users/sergiyzasorin/Fix_new/client/Docs/PRE_CHANGE_CHECKLIST.md`
  - `/Users/sergiyzasorin/Fix_new/client/Docs/PROJECT_REQUIREMENTS.md`
  - `/Users/sergiyzasorin/Fix_new/client/Docs/ARCHITECTURE_OVERVIEW.md`
  - `/Users/sergiyzasorin/Fix_new/client/Docs/FEATURE_FLAGS.md`
  - `/Users/sergiyzasorin/Fix_new/Docs/ASSISTANT_COORDINATION_PROTOCOL.md`
  - `/Users/sergiyzasorin/Fix_new/Docs/CODEX_PROMPT.md`
  - `/Users/sergiyzasorin/Fix_new/Docs/ANTIGRAVITY_PROMPT.md`
  - `/Users/sergiyzasorin/Fix_new/Docs/PRE_CHANGE_CHECKLIST.md`
  - `/Users/sergiyzasorin/Fix_new/Docs/assistant_exchange/TEMPLATE.md`
- Source of Truth: `AVFoundationPlayer._playback_loop`.
- Дублирование: удален дублирующий/экспериментальный путь копирования; владелец один.
- Feature Flags check: новых флагов нет, конфликтов нет.
- Race check: локальных новых shared-state не добавлено; сериализация осталась через существующий playback thread + `_playback_op_lock` в integration.

## Запрос/цель
Восстановить слышимое воспроизведение ответов ассистента при наличии `grpc.response.audio`.

## Контекст
- Файлы: `modules/speech_playback/core/avf_player.py`, `integration/integrations/speech_playback_integration.py`
- Ограничения: без изменения EventBus контрактов и без новых feature flags.

## Решения/выводы
- Первичный дефект был в низкоуровневой записи samples в AVAudio buffer, не в gRPC pipeline.
- Исправление локализовано в owner-модуле playback.

## Открытые вопросы
- Если после фикса всё ещё есть «тихо», проверить route/volume на уровне macOS output profile (AirPods/HFP vs A2DP) в момент воспроизведения.

## Следующие шаги
1. Прогнать голосовой сценарий 3-5 раз подряд.
2. Сверить наличие terminal-событий `playback.completed` в каждой сессии.
3. При повторе проблемы включить `audio_diag_verbose=true` и снять короткий лог фрагмент вокруг `_playback_loop`.
