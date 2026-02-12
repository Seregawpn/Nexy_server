# Task Brief: gRPC speech playback stabilization (shape handling + AVF copy path)

## Goal
Убрать причины сценария "audio_chunk приходит, но речь не слышна" без изменения архитектуры EventBus/Integration flow.

## Changes
1. `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/integration/integrations/speech_playback_integration.py`
   - Убрана зависимость воспроизведения от транспортного `shape` как источника формы PCM.
   - Добавлена безопасная проверка `shape` (только диагностика несоответствия размерности).
   - Добавлена нормализация массива к линейному виду (`arr.reshape(-1)`), чтобы исключить collapse фреймов при shape вида `[1, N]`.

2. `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/modules/speech_playback/core/avf_player.py`
   - Исправлен дефект логирования в fallback-копировании буфера (`test_val` -> `test_value/read_back`), который мог маскировать фактическую ошибку копирования и уводить чанк в silent-path.

## Validation
- `python3 -m py_compile integration/integrations/speech_playback_integration.py modules/speech_playback/core/avf_player.py` -> OK

## Result
- Устранён риск потери слышимого аудио из-за некорректной интерпретации `shape` на клиенте.
- Устранён дефект в AVF fallback-ветке, влияющий на надежность записи данных в `AVAudioPCMBuffer`.
