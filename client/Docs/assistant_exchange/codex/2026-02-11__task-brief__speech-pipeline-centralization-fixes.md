# Speech Pipeline Centralization Fixes

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-11
- ID (INS-###): N/A

## Diagnosis
В speech-потоке оставались competing paths для terminal-mode decision и конфликт по `grpc.request_cancel` при `session_id=None`.

## Root Cause
Дублирующий owner в `ListeningWorkflow` + несовпадающий контракт publisher/consumer cancel-события.

## Optimal Fix
- Убрана competing mode decision ветка short-recording из `ListeningWorkflow`.
- Добавлен fallback cancel в `GrpcClientIntegration` на latest inflight request при отсутствии `session_id`.
- Установлен конечный `request_timeout_sec=30.0` для gRPC в unified config.
- Обновлён контрактный тест на новый fallback.

## Verification
- Команда: `PYTHONPATH=. pytest -q tests/test_client_server_flow_contracts.py tests/test_interrupt_management_contract.py tests/test_speech_playback_session_id.py`
- Результат: `7 passed`

## Pre-Change Gate Evidence (обязательно)
- Прочитанные документы: canonical root/client docs + checklist + architecture + feature flags + flow/state specs.
- Source of Truth:
  - PTT lifecycle: `InputProcessingIntegration`
  - Mode transitions: `ModeManagementIntegration`
  - Session axis: `ApplicationStateManager`
- Дублирование: short-recording mode path в workflow устранён как вторичный путь.
- Feature Flags check: новые флаги не добавлялись.
- Race check: sessionless cancel → fallback to latest inflight.

## Запрос/цель
Выполнить практическое устранение конфликтов/гонок/задержек в speech/STT серверном потоке.

## Контекст
- Файлы: integrations/workflows/config/tests для speech pipeline.

## Решения/выводы
- Централизация усилена без реархитектуры.
- Cancel-путь стал устойчив к sessionless событию.

## Открытые вопросы
- Нужен ли строгий reject `session_id=None` в будущей версии протокола без fallback (после миграции всех publishers).

## Следующие шаги
1. Прогнать runtime smoke (PTT long-press/release + short-tap interrupt).
2. Проверить TRACE latency (`recording_stop -> grpc.start -> first_chunk`).
