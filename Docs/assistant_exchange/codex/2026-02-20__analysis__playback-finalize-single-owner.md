# Playback Finalize Single Owner

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-20
- ID (INS-###): N/A

## Diagnosis
Речь обрывалась до завершения рендера: `playback.completed` публиковался при `queue_empty=True`, хотя `buffered_sec>0` и буфер еще не был реально consumed.
Также был дубликат publish пути `hardware.id_obtained` на старте.

## Root Cause
Разные сигналы “очередь пуста” и “рендер завершен” использовались как эквивалентные → ранний terminal event → stop в середине речи.
Дополнительно raw-сессия могла наследовать старую finalize-task без перезапуска timeout policy.

## Optimal Fix
Source of Truth финализации оставлен в `SpeechPlaybackIntegration`, но condition усилен фактом рендера из `AVFPlayer`.

План внедрения:
1. Добавить в `AVFPlayer` счетчик pending render buffers (`scheduled - consumed`).
2. В `SpeechPlaybackIntegration._finalize_on_silence` считать idle только при `queue_empty && buffered_sec<=0.05 && pending_buffers==0`.
3. Убрать преждевременный break на soft-timeout, если рендер еще активен; добавить hard-timeout safety.
4. Для raw path запускать finalize через `force_restart=True`.
5. Дедуплицировать `hardware.id_obtained` publish по UUID.

## Verification
- `python3 -m py_compile` для измененных файлов: ok.
- `pytest -q tests/test_speech_playback_pipeline_diagnostic.py tests/test_interrupt_playback.py -k "terminal or idempotent"`: `2 passed`.
- Логи должны перестать показывать `Finalize timeout ... buffered_sec>0` с немедленным `playback.completed`.

## Информация об изменениях
- Что изменено:
  - finalize condition учитывает pending render buffers;
  - raw finalize task всегда перезапускается под актуальный timeout;
  - soft-timeout не завершает сессию при активном рендере;
  - dedup `hardware.id_obtained` по UUID;
  - удален дублирующийся runtime-init фрагмент в `HardwareIdIntegration`.
- Файлы:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/integration/integrations/speech_playback_integration.py`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/modules/speech_playback/core/avf_player.py`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/integration/integrations/hardware_id_integration.py`
- Причина/цель: убрать ранний terminal и дубли publish-path без изменения архитектуры owner-центров.
- Проверка: py_compile + pytest (targeted).

## Запрос/цель
Убрать обрывы речи на середине и вычистить дубли/гонки owner-path.

## Контекст
- Файлы:
  - `client/integration/integrations/speech_playback_integration.py`
  - `client/modules/speech_playback/core/avf_player.py`
  - `client/integration/integrations/hardware_id_integration.py`
- Документы:
  - `AGENTS.md`
  - `Docs/assistant_exchange/TEMPLATE.md`
- Ограничения: без реархитектуры, только architecture-fit правки.

## Решения/выводы
- Финализация playback должна опираться на факт рендера, а не только на пустую очередь.
- Duplicate publish-path на startup убран дедуп-guard’ом.

## Открытые вопросы
- Нужно ли дополнительно публиковать telemetry `pending_buffers` в runtime snapshot для мониторинга p95 finalize latency.

## Следующие шаги
- Прогнать живой сценарий startup welcome + long grpc response и проверить отсутствие mid-speech stop.
