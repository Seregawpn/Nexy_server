# Unify EdgeTTS Output Format

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-01
- ID (INS-###): INS-005

## Diagnosis
EdgeTTS отдавал формат, расходящийся с единым server_audio_format, что приводило к тишине/искажению в клиенте.

## Root Cause
Несогласованные дефолты формата (24kHz vs 48kHz) → метаданные и реальные PCM байты не совпадали → клиент корректно отбрасывал/проигрывал тишину.

## Optimal Fix
Выравнивание EdgeTTSProvider на единый формат из unified_config (48kHz, int16, mono) и обновление описаний формата.

## Verification
Проверить, что metadata sample_rate/channels/dtype соответствует реальным PCM данным и клиент не логирует mismatch/silent chunks.

## Запрос/цель
Единый простой формат аудио без «личных» форматов, как у приветствия.

## Контекст
- Файлы: `server/server/modules/audio_generation/providers/edge_tts_provider.py`
- Документы: `Docs/ARCHITECTURE_OVERVIEW.md`
- Ограничения: без новой архитектуры, единый источник истины

## Решения/выводы
- Убраны несинхронизированные дефолты 24kHz в EdgeTTSProvider.

## Открытые вопросы
- Нужна ли дополнительная серверная проверка RMS/peak для ранней диагностики тишины?

## Следующие шаги
- Прогнать сценарий лимита и проверить логи на отсутствие silent chunks.
