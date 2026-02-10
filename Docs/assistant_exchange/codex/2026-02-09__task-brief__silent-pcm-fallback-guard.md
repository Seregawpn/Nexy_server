# silent-pcm-fallback-guard

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-09
- ID (INS-###): INS-UNKNOWN

## Diagnosis
gRPC поток был «успешным» по числу audio_chunk, но фактически PCM был нулевой (`all_zeros=True`) на клиентском входе.

## Root Cause
`had_audio` считался как `audio_chunk_count > 0` без учета амплитуды → silent stream не запускал fallback.

## Optimal Fix
- В `grpc_client_integration` введен `non_silent_audio_chunk_count`.
- `had_audio` теперь считается только по non-silent чанкам.
- При `audio_chunk_count > 0 && non_silent_audio_chunk_count == 0` пишется явный лог `SILENT_AUDIO_STREAM`.
- Встроенный fallback (`had_text && !had_audio`) теперь срабатывает и при zero-PCM потоке.

## Verification
- `python3 -m py_compile client/integration/integrations/grpc_client_integration.py` — OK.

## Запрос/цель
Устранить «тишину при формально успешном playback» без изменения централизованной mode-архитектуры.

## Контекст
- Файл: `/Users/sergiyzasorin/Fix_new/client/integration/integrations/grpc_client_integration.py`
- Логи: zero PCM на стороне gRPC client + speech playback.

## Решения/выводы
- Порт/соединение не primary issue: `end_message` и поток chunk приходят.
- Primary issue: качество аудиоданных (нулевой PCM), закрыто клиентским guard.

## Открытые вопросы
- Требуется отдельная серверная проверка провайдера TTS, если fallback тоже дает zero PCM.

## Следующие шаги
- Проверить live-лог на `SILENT_AUDIO_STREAM` и последующий fallback.
