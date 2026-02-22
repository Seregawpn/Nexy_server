# Phase Routing Regression Sweep

## Метаданные
- Ассистент: codex
- Тип: review
- Дата: 2026-02-21
- ID (INS-###): N/A

## Diagnosis
Проведён расширенный прогон тестов по зонам дублирования/конфликтов/гонок после внедрения server phase-router (`COLLECT/COMMIT`). Критических регрессий в покрытых сценариях не выявлено.

## Root Cause
Основной риск был в конфликте owner-path между pre-release collect и commit lifecycle. Проверки подтвердили, что целевые guard-сценарии работают стабильно в покрытых тестах.

## Optimal Fix
Для текущего этапа изменений не требуется: фикс phase-router проходит целевые и смежные регрессии. Следующий шаг — закрыть отдельное уже существующее client architecture-нарушение вне текущего change-set.

## Verification
Выполненные проверки:
- `cd server/server && pytest -q tests/test_grpc_phase_collect_commit.py tests/test_grpc_identifier_validation.py tests/test_streaming_workflow_concurrency_guards.py tests/test_memory_single_call_smoke.py`
  - Результат: `14 passed`
- `cd client && pytest -q tests/test_grpc_client_interim_commit_gate.py tests/test_microphone_activation.py tests/test_input_secure_input_healthcheck.py tests/test_mode_management_mode_request_dedup.py tests/test_event_bus_subscription_dedup.py tests/test_browser_action_race_condition.py tests/test_voice_audio_owner_guards.py tests/test_processing_workflow_session_guard.py`
  - Результат: `39 passed`
- `cd server/server && pytest -q tests/test_grpc_mcp_integration.py tests/test_grpc_interceptor_metrics_order.py tests/test_metrics_collector_method_normalization.py`
  - Результат: `8 passed`
- `cd client && pytest -q tests/test_centralization_regressions.py tests/test_interrupt_playback.py tests/test_speech_playback_pipeline_diagnostic.py`
  - Результат: `21 passed`
- `cd client && python3 scripts/verify_no_direct_state_access.py`
  - Результат: `No direct state access violations detected.`
- `cd server/server && python3 scripts/verify_architecture_guards.py`
  - Результат: `OK`
- `cd client && python3 scripts/verify_architecture_guards.py`
  - Результат: `1 existing violation` (`modules/grpc_client/core/grpc_client.py:706`, `sys_path_insert_outside_entrypoint`)

## Информация об изменениях
- Что изменено:
  - Выполнен расширенный регрессионный тестовый прогон по зонам конфликтов/дублей/гонок.
- Файлы:
  - Изменения в код не вносились в рамках этого шага.
- Причина/цель:
  - Проверить отсутствие конфликтов и дублей после phase-routing фикса.
- Проверка:
  - См. список прогонов в разделе Verification.
- Изменения не вносились.

## Запрос/цель
Подтвердить, что в разных участках системы нет конфликтов/дублей/гонок после фикса phase routing.

## Контекст
- Основные зоны: gRPC phase-router, PTT/release lifecycle, mode/request dedup, playback terminal dedup, concurrency guards.

## Решения/выводы
- Фикс phase routing устойчив в покрытых тестах.
- Остался один уже существующий client architecture guard issue вне текущего change-set.

## Найденные проблемы (если review)
- Итоговый статус: ЧАСТИЧНОЕ
- Наблюдение: `client/scripts/verify_architecture_guards.py` фиксирует существующее нарушение `sys_path_insert_outside_entrypoint` в `client/modules/grpc_client/core/grpc_client.py:706`.

## Открытые вопросы
- Закрывать ли найденное architecture guard нарушение отдельным минимальным change-set сейчас.

## Следующие шаги
- Приоритетно: отдельным PR/changeset устранить `sys_path_insert_outside_entrypoint` в `client/modules/grpc_client/core/grpc_client.py`.
