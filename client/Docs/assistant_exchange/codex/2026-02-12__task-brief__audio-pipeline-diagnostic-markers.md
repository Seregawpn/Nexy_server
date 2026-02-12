# Task Brief: Add end-to-end audio pipeline diagnostic markers

## Goal
Быстро локализовать точку потери амплитуды (до очереди playback owner или внутри AVF schedule).

## Changes
1. `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/integration/integrations/speech_playback_integration.py`
   - Добавлен маркер:
     - `AUDIO_PIPELINE phase=before_queue ...`
   - В metadata для grpc path добавлен `kind=grpc_audio`.

2. `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/modules/speech_playback/core/avf_player.py`
   - Добавлен маркер:
     - `AUDIO_PIPELINE phase=before_schedule ...`
   - Лог пишет `kind`, `chunk`, `frames`, `peak`, `rms`.

3. `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/config/unified_config.yaml`
   - Включен `speech_playback.audio_diag_verbose: true` для следующего прогона диагностики.

## Validation
- `python3 -m py_compile integration/integrations/speech_playback_integration.py modules/speech_playback/core/avf_player.py` -> OK
- `PYTHONPATH=. pytest -q tests/test_speech_playback_grpc_audio_format.py tests/test_interrupt_playback.py -q` -> PASS

## Result
- Есть две контрольные точки амплитуды в едином playback-path.
- Следующий runtime прогон даст точный ответ, где теряется слышимость.
