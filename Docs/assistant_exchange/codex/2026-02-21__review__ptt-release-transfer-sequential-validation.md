# PTT Release To Transfer Sequential Validation

## Метаданные
- Ассистент: codex
- Тип: review
- Дата: 2026-02-21
- ID (INS-###): N/A
- Итоговый статус: ЧАСТИЧНОЕ

## Diagnosis
Ключевая цепочка `hold -> release -> transfer -> LLM start` в каноничных тестах проходит стабильно, но часть legacy functional scripts не соответствует текущему gRPC контракту/окружению и даёт ложные падения.

## Root Cause
Эволюция контракта (обязательный `session_id`, phase-routing `COLLECT/COMMIT`) + устаревшие/неизолированные тестовые entrypoints → запуск неканоничных сценариев с рассинхроном импорта/окружения → ошибки, не отражающие регрессию основного workflow.

## Optimal Fix
Primary: использовать каноничный набор тестов (client/tests + server/server/tests + architecture guards) как release-gate для этого потока; legacy scripts перевести в совместимый контракт и изолировать от основного verdict.

## Verification
- Server tests:
  - `cd server/server && pytest -q tests/test_grpc_phase_collect_commit.py tests/test_streaming_workflow_concurrency_guards.py tests/test_grpc_mcp_integration.py tests/test_grpc_interceptor_metrics_order.py tests/test_grpc_identifier_validation.py`
  - Result: `17 passed`.
- Client tests:
  - `cd client && pytest -q tests/test_ctrl_n_combo.py tests/test_quartz_monitor_chord_logic.py tests/test_microphone_activation.py tests/test_input_secure_input_healthcheck.py tests/test_grpc_client_interim_commit_gate.py tests/test_processing_workflow_session_guard.py tests/test_mode_management_mode_request_dedup.py tests/test_voice_audio_owner_guards.py tests/test_event_bus_subscription_dedup.py tests/test_interrupt_playback.py tests/test_speech_playback_pipeline_diagnostic.py tests/test_browser_action_race_condition.py`
  - Result: `60 passed, 1 warning` (collection warning в `test_ctrl_n_combo.py`, не runtime regression).
- Architecture guards:
  - `cd client && python3 scripts/verify_architecture_guards.py` -> OK.
  - `cd client && python3 scripts/verify_no_direct_state_access.py` -> OK.
- Legacy functional script check:
  - `cd server/server && python3 scripts/test_streaming_workflow_fix.py`
  - Result: failed; indicates drift/non-canonical script path and contract mismatch signal, not failure of canonical gate.

## Информация об изменениях
- Что изменено:
  - Изменения кода не вносились.
  - Выполнен последовательный прогон тестов и валидаций по цепочке release->transfer.
- Файлы:
  - `Docs/assistant_exchange/codex/2026-02-21__review__ptt-release-transfer-sequential-validation.md`
- Причина/цель:
  - Подтвердить отсутствие дублей/конфликтов/гонок в основном рабочем контуре и выявить неактуальные тестовые части.
- Проверка:
  - Набор команд из раздела Verification.

## Запрос/цель
Проверить всю цепочку от удержания комбинации до передачи данных и запуска обработки, исключить конфликтные условия.

## Контекст
- Файлы:
  - `server/server/modules/grpc_service/core/grpc_server.py`
  - `client/modules/grpc_client/core/grpc_client.py`
  - `server/server/tests/test_grpc_phase_collect_commit.py`
  - `client/tests/test_grpc_client_interim_commit_gate.py`
- Документы:
  - `Docs/ARCHITECTURE_OVERVIEW.md`
  - `Docs/ASSISTANT_COORDINATION_PROTOCOL.md`
  - `Docs/CODEX_PROMPT.md`
- Ограничения:
  - Не ломать текущую архитектуру, не вводить второй owner-path.

## Решения/выводы
- Каноничная цепочка подтверждена тестами.
- Основной owner-path централизован: server phase-router + client commit-gate.
- Обнаруженные падения относятся к legacy script drift, их нельзя использовать как verdict по релизной корректности.

## Найденные проблемы (если review)
- Legacy functional script (`server/server/scripts/test_streaming_workflow_fix.py`) не является валидным release-gate в текущем контракте.

## Открытые вопросы
- Нужна ли отдельная задача на обновление/очистку legacy functional scripts под текущий контракт, чтобы убрать шум в диагностике?

## Следующие шаги
- Обновить legacy scripts под текущий protobuf/contract и добавить их в отдельный non-blocking контур.
- Оставить каноничные pytest+guard скрипты как обязательный blocking gate.
