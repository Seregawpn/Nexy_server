# Task Brief: VoiceOver/Nexy audio session conflict fix plan

## Context
Подготовлен внедренческий план фикса конфликта аудиосессий VoiceOver + Nexy с соблюдением owner-архитектуры.

## Plan
1. Убрать дублирующий completion callback в `GoogleSRController`.
2. Усилить session-guard/idempotency в terminal STT публикациях `VoiceRecognitionIntegration`.
3. Зафиксировать единый owner `voice.mic_closed` semantics (один terminal-cycle, без повторных side-effects).
4. Ограничить recovery reassert в `SpeechPlaybackIntegration` только валидным playback context.
5. Подтвердить owner-finalization в `ModeManagementIntegration` (SLEEPING только после terminal chain).
6. Добавить race-тесты: stop+late callback, cancel during playback, stale session callback.
7. Прогнать архитектурные/feature-flag гейты и runtime smoke с VoiceOver.

## Verification
- Unit/integration tests:
  - `tests/test_interrupt_playback.py`
  - новые тесты для `voice_recognition_integration` terminal dedup и late callbacks
- Gates:
  - `python3 scripts/verify_architecture_guards.py`
  - `python3 scripts/verify_feature_flags.py`
- Runtime:
  - сценарий VoiceOver ON + PTT циклы; проверка отсутствия `session=(null)` и start/stop flapping.

## Информация об изменениях
- Что изменено:
  - Добавлен task-brief с поэтапным планом внедрения.
- Список файлов:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/Docs/assistant_exchange/codex/2026-02-16__task-brief__voiceover-audio-session-conflict-fix-plan.md`
- Причина/цель изменений:
  - Зафиксировать архитектурно-совместимый план реализации перед coding phase.
- Проверка (что выполнено для валидации):
  - Согласование шагов с owner-цепочкой и обязательными архитектурными гейтами проекта.
