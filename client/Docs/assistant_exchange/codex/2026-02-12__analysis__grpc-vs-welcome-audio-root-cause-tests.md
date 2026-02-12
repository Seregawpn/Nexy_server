# Analysis: gRPC speech silence root-cause via targeted tests

## Goal
Подтвердить тестами, где корень проблемы: формат входного PCM или логика воспроизведения/усиления.

## What was tested
1. `tests/test_speech_playback_grpc_audio_format.py::test_grpc_audio_chunk_decodes_int16_to_float_range`
   - Проверяет, что `grpc.response.audio` (`dtype=int16`) корректно декодируется в `float32` диапазон перед отправкой в плеер.
   - Вывод: формат декодируется корректно (не root-cause).

2. `tests/test_speech_playback_grpc_audio_format.py::test_grpc_gain_is_not_pinned_by_near_silent_first_chunk`
   - Проверяет сценарий тихого первого чанка: ранее это могло зафиксировать gain=1.0 для всей сессии.
   - Вывод: найдена и исправлена реальная причина тихого воспроизведения — pinning gain на старте.

## Code change (root-cause fix)
- `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/integration/integrations/speech_playback_integration.py`
  - Изменена логика auto-gain:
    - если первый чанк near-silent (`peak < tts_min_peak_for_gain`), gain=1.0 не кэшируется в session map;
    - gain пересчитывается на следующем meaningful чанке.

## Validation
- `PYTHONPATH=. pytest -q tests/test_speech_playback_grpc_audio_format.py tests/test_speech_playback_session_id.py tests/test_interrupt_playback.py -q` -> PASS

## Conclusion
- Корень проблемы не в неверном формате PCM.
- Наиболее вероятный корень: логика усиления для gRPC потока (тихий lead-in фиксировал недостаточный gain).
- После фикса и объединенного playback-path поведение `grpc` и `welcome` стало архитектурно ближе и диагностируемее.
