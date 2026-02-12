# Task Brief: AVFoundation Flags Canonical Resolver

Date: 2026-02-11

## Context
В проекте одновременно присутствовали:
- env flags: `NEXY_FEATURE_AVFOUNDATION_*`, `NEXY_KS_AVFOUNDATION_*`
- config flags: `audio_system.avfoundation_*`, `audio_system.ks_avfoundation_*`

Единого runtime-resolver не было.

## Change
Файлы:
- `config/unified_config_loader.py`
- `integration/integrations/speech_playback_integration.py`
- `integration/integrations/voice_recognition_integration.py`
- `tests/test_unified_config_avfoundation_flags.py`

Сделано:
1. Добавлен канонический resolver `UnifiedConfigLoader.get_avfoundation_flags()`.
2. Добавлен единый bool-parser env (`_parse_env_bool`).
3. Зафиксирован приоритет: env > config.
4. Добавлены вычисленные `effective` флаги (master/input/output/route_manager) с учетом kill-switch.
5. Интеграции `SpeechPlaybackIntegration` и `VoiceRecognitionIntegration` читают AVFoundation флаги только через resolver (single path) и логируют результат.

Важно: runtime-поведение аудио пайплайна не менялось (без hard-gating), изменение направлено на централизацию и устранение дублирующих источников чтения.

## Verification
- `PYTHONPATH=. pytest -q tests/test_unified_config_avfoundation_flags.py tests/test_voice_route_manager_gate.py` → `5 passed`
- `PYTHONPATH=. pytest -q tests/test_interrupt_playback.py -k "grpc_cancel or interrupt_idempotently"` → `2 passed, 19 deselected`

## Outcome
- AVFoundation flags теперь имеют единый Source of Truth в runtime (`get_avfoundation_flags`).
- Убрана необходимость локально комбинировать env/config в интеграциях.
