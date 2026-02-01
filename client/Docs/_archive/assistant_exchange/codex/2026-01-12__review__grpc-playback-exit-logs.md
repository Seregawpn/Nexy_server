# gRPC/Playback Exit Logs Review

## Метаданные
- Ассистент: codex
- Тип: review
- Дата: 2026-01-12
- ID (INS-###): INS-008

## Diagnosis
Проверка добавленных логов exit-reason/summary выявила два риска искажения диагностических данных.

## Root Cause
1) audio_chunk_count инкрементится до проверки пустого чанка → had_audio может стать True без реального аудио.
2) _had_audio_for_session очищается до логирования cancelled → summary всегда показывает had_audio=false.

## Optimal Fix
Перенести инкремент audio_chunk_count после проверки len(data)>0 и логировать cancel до очистки had_audio.

## Verification
Сценарии с пустыми чанками/отменой должны показывать корректный had_audio.

## Запрос/цель
Оценить корректность новых логов exit-reason и summary.

## Контекст
- Файлы: integration/integrations/grpc_client_integration.py, integration/integrations/speech_playback_integration.py
- Документы: /Users/sergiyzasorin/Fix_new/Docs/ARCHITECTURE_OVERVIEW.md

## Решения/выводы
- Логи добавлены корректно, но два случая дают неверный summary.

## Найденные проблемы (если review)
- **Средняя**: `audio_chunk_count` инкрементится до `len(data)==0` → `had_audio=true` при пустых чанках. Файл: integration/integrations/grpc_client_integration.py
- **Средняя**: при cancel `_had_audio_for_session` очищается до лога → `had_audio` всегда false. Файл: integration/integrations/speech_playback_integration.py

## Открытые вопросы
- Нужно ли логировать длительность ожидания в no_audio? Сейчас фиксировано `duration=0`.

## Следующие шаги
- Перенести инкремент и логировать cancel до очистки.

## Итоговый статус
**ЧАСТИЧНОЕ**
