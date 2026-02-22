# PTT pre-release chunk activation

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-21
- ID (INS-###): N/A

## Diagnosis
Pre-release collect path in gRPC integration sends interim chunks before key release, creating early server-side activation risk and violating canonical PTT flow.

## Root Cause
`voice.recognition_completed(interim=true)` triggers `REQUEST_PHASE_COLLECT` send before `voice.recording_stop`; this bypasses release-gated processing owner-path and enables out-of-order response readiness.

## Optimal Fix
Keep a single outbound owner in `GrpcClientIntegration`: allow any network send (`COLLECT` and `COMMIT`) only after release marker (`voice.recording_stop` for session).

## Verification
DoD:
1. Hold Ctrl+N: interim STT may update local buffer, but no `REQUEST_PHASE_COLLECT` log appears before release.
2. Release Ctrl+N: one terminal stop, then collect/commit (if enabled by policy) starts.
3. No assistant response starts while combo is still held.

## Информация об изменениях
- Что изменено: Проведён анализ owner-path и race-точек pre-release send.
- Файлы: client/integration/integrations/grpc_client_integration.py, client/integration/integrations/input_processing_integration.py, client/integration/integrations/voice_recognition_integration.py, client/Docs/FLOW_INTERACTION_SPEC.md
- Причина/цель: Найти источник ранней активации чанков до отпускания hotkey.
- Проверка: Статический трассинг событий и сверка с каноническим flow.
- Изменения не вносились.

## Запрос/цель
Проверить, почему чанки могут активироваться/уходить до отпускания комбинации Ctrl+N, и предложить архитектурно корректный фикс.

## Контекст
- Файлы: client/integration/integrations/grpc_client_integration.py, client/integration/integrations/input_processing_integration.py, client/integration/integrations/voice_recognition_integration.py
- Документы: Docs/PROJECT_REQUIREMENTS.md, Docs/ARCHITECTURE_OVERVIEW.md, Docs/ASSISTANT_COORDINATION_PROTOCOL.md, Docs/ANTIGRAVITY_PROMPT.md, Docs/CODEX_PROMPT.md, client/Docs/FLOW_INTERACTION_SPEC.md
- Ограничения: Без второго owner-path, без реархитектуры.

## Решения/выводы
- Pre-release отправка реально существует в `_schedule_collect_send -> _send_collect_in_grpc_loop(phase=REQUEST_PHASE_COLLECT)`.
- Канонический flow требует старт processing/gRPC только после `RELEASE`.
- Нужно централизовать release-gate в `GrpcClientIntegration` и убрать pre-release collect scheduling.

## Открытые вопросы
- Нужен ли collect вообще после release, или policy должна быть commit-only.

## Следующие шаги
- Внести release-gate в collect path и добавить тесты на запрет collect до `voice.recording_stop`.
