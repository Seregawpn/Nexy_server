# Task Brief: Docs Sync for Audio Ownership and AVF Resolver

Date: 2026-02-11

## Scope
Синхронизация canonical-документов после внедрения:
1) single-owner cancel path в SpeechPlayback,
2) runtime route-reconcile gate в VoiceRecognition,
3) canonical AVFoundation flags resolver.

## Updated Docs
- `Docs/FLOW_INTERACTION_SPEC.md`
- `Docs/ARCHITECTURE_OVERVIEW.md`
- `Docs/STATE_CATALOG.md`
- `Docs/FEATURE_FLAGS.md`

## What Was Synchronized

### 1) Cancel Single Owner
- Зафиксировано, что cancel side effects (stop/clear/guards/session cleanup) выполняются только owner-обработчиком в `SpeechPlaybackIntegration` по событию `playback.cancelled`.
- Уточнено, что `grpc.request_cancel` в `SpeechPlaybackIntegration` служит публикацией канонического `playback.cancelled`.

### 2) Route Reconcile Runtime Owner
- В `FLOW_INTERACTION_SPEC` и `ARCHITECTURE_OVERVIEW` добавлен runtime-gate на старте записи:
  - `VoiceRecognitionIntegration` вызывает `decide_route_manager_reconcile(snapshot)` до активации записи.
  - При `abort`/`retry->abort`/`retry->retry` публикуются terminal события `voice.mic_closed` + `voice.recognition_failed`.
- В `STATE_CATALOG` добавлен явный runtime owner для route reconcile на оси `device.input`.

### 3) AVFoundation Flags Canonical Resolver
- В `ARCHITECTURE_OVERVIEW` и `FEATURE_FLAGS` закреплен единый путь чтения:
  - `UnifiedConfigLoader.get_avfoundation_flags()`
  - precedence: `env > config`
  - runtime использует `effective` flags и не смешивает env/config локально.
- В `STATE_CATALOG` добавлен artifact ownership для `avfoundation.flags`.

## Notes
- Правки документальные (без runtime-кода в этом шаге).
- Актуализированы только разделы, связанные с аудио ownership/centralization.
