# Audio Control Audit

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-11
- ID (INS-###): INS-N/A

## Diagnosis
В аудио-потоке есть рассинхронизация event-контрактов и дублирующие точки публикации terminal/start событий, что повышает риск залипания playback-сессий и пропуска сигналов.

## Root Cause
Часть логики осталась в legacy-ветках (signal.play / speech.playback.request / неиспользуемая TTSIntegration), при этом новый owner-путь построен вокруг grpc.response.audio + SpeechPlaybackIntegration.

## Optimal Fix
Цель: один owner для playback lifecycle и один owner для signal routing.

- Source of Truth playback lifecycle: SpeechPlaybackIntegration (`playback.started|completed|failed|cancelled`).
- Source of Truth cancel: InterruptManagementIntegration -> grpc.request_cancel -> SpeechPlaybackIntegration.
- Source of Truth cues: SignalIntegration -> playback.signal.

План:
1. Убрать ручную публикацию `playback.started` из `GrpcClientIntegration._play_server_tts`.
2. Гарантировать terminal-событие для TTS-сессий через публикацию `grpc.request_completed` (или выделенный owner-хук в SpeechPlaybackIntegration).
3. Унифицировать update-cues: заменить `signal.play` на поддерживаемый owner-путь (`processing.terminal/app.mode_changed` или явный контракт в SignalIntegration).
4. Удалить/архивировать мертвую `TTSIntegration` и остатки `speech.playback.request` контракта.
5. Привести audio config к одному месту (убрать неиспользуемые ветки/флаги, которые не участвуют в runtime).

## Verification
- На `grpc.tts_request` всегда наблюдается полный цикл: `playback.started` -> `playback.completed|failed|cancelled`.
- `ModeManagementIntegration.active_playback_sessions` не содержит устаревших session_id после terminal события.
- Update cues воспроизводятся по каноническому событию, без `signal.play` orphan-публикаций.
- В коде нет активных publishers для legacy `speech.playback.request`.

## Запрос/цель
Проанализировать текущую логику аудио-управления на конфликты, дубли и гонки.

## Контекст
- Файлы: integration/integrations/speech_playback_integration.py, integration/integrations/grpc_client_integration.py, integration/integrations/signal_integration.py, integration/integrations/update_notification_integration.py, integration/integrations/mode_management_integration.py, integration/core/event_bus.py, integration/integrations/tts_integration.py
- Документы: Docs/PROJECT_REQUIREMENTS.md, Docs/ARCHITECTURE_OVERVIEW.md, ../Docs/ASSISTANT_COORDINATION_PROTOCOL.md, Docs/FEATURE_FLAGS.md, Docs/FLOW_INTERACTION_SPEC.md
- Ограничения: без реархитектуры, только в текущих слоях/owners.

## Решения/выводы
- Главный конфликт: нарушение single-owner lifecycle для playback и orphan event-контракты для сигналов.
- Главный риск гонки: рассинхрон terminal-событий в TTS-пути и fast-dispatch `app.mode_changed`.

## Открытые вопросы
- Нужен ли отдельный канонический event для update-cues или update должен жить только через существующие mode/terminal события?

## Следующие шаги
- Выполнить точечную централизацию publishers и удалить legacy-путь сигналов/tts без добавления новых state-axis.
