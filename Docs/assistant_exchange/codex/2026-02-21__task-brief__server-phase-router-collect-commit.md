# Server Phase Router Collect Commit

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-21
- ID (INS-###): N/A

## Diagnosis
Сервер не различал `COLLECT/COMMIT` на runtime и запускал полный workflow для любых `StreamAudio`, из-за чего ответ мог стартовать до release.

## Root Cause
Phase-поля были в клиентском контракте, но отсутствовали в server protobuf/runtime owner-path, поэтому `COLLECT` и `COMMIT` обрабатывались одинаково.

## Optimal Fix
Введён единый server owner-path phase-routing:
- `REQUEST_PHASE_COLLECT` → buffer-only + ack (`COLLECT_ACCEPTED`), без запуска workflow.
- `REQUEST_PHASE_COMMIT` → atomically consume buffered collect и запуск текущего workflow.

## Verification
- `cd server/server && pytest -q tests/test_grpc_phase_collect_commit.py`
- `cd server/server && pytest -q tests/test_grpc_identifier_validation.py`

## Информация об изменениях
- Что изменено:
  - Добавлены phase-поля в server proto (`phase`, `chunk_seq`, `chunk_text`) и enum `RequestPhase`.
  - Добавлен phase-router в `StreamAudio`.
  - Добавлен in-memory collect-buffer с idempotency по `chunk_seq` и atomic consume-on-commit.
  - Добавлены серверные тесты на `COLLECT/COMMIT` поведение.
- Файлы:
  - `server/server/modules/grpc_service/streaming.proto`
  - `server/server/modules/grpc_service/streaming_pb2.py`
  - `server/server/modules/grpc_service/streaming_pb2_grpc.py`
  - `server/server/modules/grpc_service/core/grpc_server.py`
  - `server/server/tests/test_grpc_phase_collect_commit.py`
- Причина/цель:
  - Устранить ранний запуск LLM до release при сохранении передачи чанков во время удержания.
- Проверка:
  - Таргетные unit-тесты phase routing и валидации gRPC идентификаторов.

## Запрос/цель
Сохранить отправку чанков до release, но запретить активацию LLM до commit/release.

## Контекст
- Файлы: `client/integration/integrations/grpc_client_integration.py`, `server/server/modules/grpc_service/core/grpc_server.py`
- Документы: `Docs/ARCHITECTURE_OVERVIEW.md`, `client/Docs/FLOW_INTERACTION_SPEC.md`, `server/server/Docs/FLOW_INTERACTION_SPEC.md`
- Ограничения: не ломать текущий workflow, минимально-инвазивные изменения.

## Решения/выводы
- Серверный phase-owner теперь централизован.
- Backward compatibility: `REQUEST_PHASE_UNSPECIFIED` трактуется как `COMMIT`.
- Дубликаты/старые collect чанки не перезаписывают более новый буфер.

## Открытые вопросы
- Нужен ли TTL-cleanup collect-buffer для долгих/брошенных сессий.

## Следующие шаги
- Добавить e2e-тест hold→collect→release→commit с реальным клиентским path.
- Добавить TTL cleanup и метрику размера collect-buffer.
