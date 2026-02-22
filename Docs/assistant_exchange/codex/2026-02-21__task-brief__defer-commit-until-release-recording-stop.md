# Defer Commit Until Release Recording Stop

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-21
- ID (INS-###): N/A

## Diagnosis
Возможен ранний старт gRPC/LLM: terminal STT (`interim=false`) мог открыть `ready_to_send` до фактического `release` (до `voice.recording_stop`).

## Root Cause
`grpc_client_integration._on_voice_completed` трактовал terminal STT как достаточное условие для commit-dispatch без подтвержденного release-события.

## Optimal Fix
Добавлен owner-gate в `GrpcClientIntegration`: commit разрешается только после пары условий для одной `session_id`:
1) terminal STT получен;
2) зафиксирован `voice.recording_stop` (release).

## Verification
- `cd client && pytest -q tests/test_grpc_client_interim_commit_gate.py tests/test_processing_workflow_session_guard.py tests/test_mode_management_mode_request_dedup.py tests/test_microphone_activation.py tests/test_quartz_monitor_chord_logic.py`
  - Result: `23 passed`
- `cd server/server && pytest -q tests/test_grpc_phase_collect_commit.py tests/test_streaming_workflow_concurrency_guards.py`
  - Result: `5 passed`
- `cd client && python3 scripts/verify_architecture_guards.py`
  - Result: OK
- `cd client && python3 scripts/verify_no_direct_state_access.py`
  - Result: OK

## Информация об изменениях
- Что изменено:
  - Введен release-gate для commit: terminal STT больше не отправляет commit до `recording_stop`.
  - Добавлено хранение флагов сессии: `terminal_recognition_received`, `recording_stopped`.
  - Добавлен bridge-path: если terminal пришел раньше release, отправка стартует на событии `recording_stop`.
  - Добавлены/обновлены тесты под сценарий terminal-before-release.
- Файлы:
  - `client/integration/integrations/grpc_client_integration.py`
  - `client/tests/test_grpc_client_interim_commit_gate.py`
- Причина/цель:
  - Исключить раннюю активацию LLM до отпускания комбинации при сохранении существующей архитектуры COLLECT/COMMIT.
- Проверка:
  - Набор команд из секции Verification.

## Запрос/цель
Сделать так, чтобы чанки могли уходить на сервер во время удержания, но обработка LLM запускалась только после отпускания комбинации.

## Контекст
- `client/integration/integrations/grpc_client_integration.py`
- `client/integration/integrations/input_processing_integration.py`
- `server/server/modules/grpc_service/core/grpc_server.py`

## Решения/выводы
- Source of Truth для старта обработки теперь однозначный: terminal STT + release (`recording_stop`) в одной `session_id`.
- COLLECT-path сохраняется активным во время удержания и не активирует LLM.

## Открытые вопросы
- Нужен ли отдельный метрик/лог-счетчик `terminal_before_release_deferred` для мониторинга частоты этого сценария в проде?

## Следующие шаги
- При необходимости добавить явный диагностический лог/метрику defer-сценария в production monitoring.
