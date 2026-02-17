# Task Brief

## Summary
Убрана избыточная блокировка browser runtime TTS при активном playback/mode processing, если есть валидный `session_id`.

## Scope
- Изменение только policy-функции suppress в `BrowserUseIntegration`.
- Без добавления новых owners/веток воспроизведения.

## Changes
- В `_should_suppress_browser_runtime_tts`:
  - suppress оставлен только для `missing_session_id`;
  - при `playback_active` и `mode=processing` с валидным `session_id` теперь `suppress=False`;
  - маршрут: публикация сразу в `grpc.tts_request`, а сериализация остаётся в `SpeechPlaybackIntegration` (single-owner).
- Причина: устранить немой режим browser-step озвучки при выполнении браузерных действий.

## Verification
- Тесты:
  - `pytest -q tests/test_browser_install_contracts.py tests/test_voice_audio_owner_guards.py tests/test_interrupt_playback.py`
- Результат:
  - `27 passed in 9.90s`

## Информация об изменениях
- Что изменено:
  - Ослаблен suppress policy для browser runtime TTS при наличии `session_id`.
- Список файлов:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/integration/integrations/browser_use_integration.py`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/Docs/assistant_exchange/codex/2026-02-17__task-brief__browser-runtime-tts-unsuppress-with-session-owner.md`
- Причина/цель изменений:
  - Вернуть слышимую озвучку браузерных шагов без обхода централизованного playback-owner.
- Проверка (что выполнено для валидации):
  - Прогон целевых регрессионных тестов.
