# Task Brief: Server TTS Silent Stream Guard

## Context
По логам Dev (`/Users/sergiyzasorin/Library/Logs/Nexy/nexy-dev.log`) цепочка `browser_step -> grpc.tts_request -> grpc.response.audio` доходит, но часть server TTS потока приходит нулевыми/почти нулевыми PCM-чанками. Это приводило к "молчаливому успеху" воспроизведения.

## Goal
Убрать silent-success для server TTS: фильтровать silent чанки в владельце потока (`GrpcClientIntegration`) и явно сигнализировать о silent stream.

## Changes
1. Добавлен transport-level quality gate для server TTS в `GrpcClientIntegration`:
- `_is_server_tts_chunk_silent(...)` с порогами для `int16` и `float32`.
- silent чанки не публикуются в `grpc.response.audio`.

2. Добавлен явный terminal сигнал для полностью silent server TTS:
- событие `grpc.tts_failed` с `reason=silent_stream`, если получены чанки, но ни один не прошёл quality gate.

3. Добавлены конфиг-пороги и их логирование:
- `server_tts_int16_silent_peak_threshold`
- `server_tts_float_silent_peak_threshold`

4. Добавлены тесты контрактов server TTS:
- silent stream -> `grpc.tts_failed`, без `grpc.response.audio`.
- mixed stream -> публикуются только non-silent чанки, без `grpc.tts_failed`.

## Architecture Gates
- Single Owner Gate: owner качества server TTS оставлен в `GrpcClientIntegration`.
- Zero Duplication Gate: не добавлялся второй путь в `BrowserUseIntegration`.
- Anti-Race Gate: terminal сигнал для silent stream формируется единообразно по итогам одного stream loop.
- Flag Lifecycle Gate: новые feature-флаги не добавлялись.

## Verification
- Запуск: `pytest -q tests/test_browser_install_contracts.py tests/test_interrupt_playback.py tests/test_voice_audio_owner_guards.py`
- Результат: `31 passed in 10.25s`

## Информация об изменениях
- Что изменено:
  - Добавлен quality gate silent/quiet чанков в server TTS потоке.
  - Добавлен `grpc.tts_failed` при полностью silent потоке.
  - Добавлены тесты на silent/mixed server TTS поведение.
- Список файлов:
  - `integration/integrations/grpc_client_integration.py`
  - `tests/test_browser_install_contracts.py`
- Причина/цель изменений:
  - Устранить случай, когда browser-step TTS технически выполняется, но аудио фактически не слышно.
- Проверка (что выполнено для валидации):
  - Прогнаны целевые тесты, все проходят.
