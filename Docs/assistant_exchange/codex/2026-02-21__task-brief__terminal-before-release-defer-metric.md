# Terminal Before Release Defer Metric

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-21
- ID (INS-###): N/A

## Diagnosis
Основной gate исправлен, но не хватало встроенной наблюдаемости: не было явного счетчика, сколько раз terminal STT пришел до release и был отложен.

## Root Cause
Отсутствие диагностического счетчика defer-сценария в owner-модуле gRPC клиента.

## Optimal Fix
Добавлен runtime-счетчик `terminal_before_release_deferred` в `GrpcClientIntegration`:
- инкремент в месте defer (`terminal получен, release еще не пришел`),
- экспорт в `get_status()` для диагностики и мониторинга.

## Verification
- `cd client && pytest -q tests/test_grpc_client_interim_commit_gate.py tests/test_processing_workflow_session_guard.py tests/test_mode_management_mode_request_dedup.py`
  - Result: `15 passed`
- `cd client && python3 scripts/verify_architecture_guards.py`
  - Result: OK

## Информация об изменениях
- Что изменено:
  - Добавлен диагностический счетчик `terminal_before_release_deferred`.
  - Добавлен вывод счетчика в `get_status()`.
  - Обновлен тест на defer-сценарий с проверкой инкремента.
- Файлы:
  - `client/integration/integrations/grpc_client_integration.py`
  - `client/tests/test_grpc_client_interim_commit_gate.py`
- Причина/цель:
  - Повысить наблюдаемость и упростить подтверждение корректности release-gate в runtime.
- Проверка:
  - Набор команд из раздела Verification.

## Запрос/цель
После закрытия основной проблемы закрепить стабильность и архитектурный контроль.

## Контекст
- `client/integration/integrations/grpc_client_integration.py`
- `client/tests/test_grpc_client_interim_commit_gate.py`

## Решения/выводы
- Owner-path не изменен, только улучшена диагностируемость.
- Дубликаты/новые ветки решений не введены.

## Открытые вопросы
- Нужна ли публикация этого счетчика в телеметрию/лог heartbeat, а не только в `get_status()`?

## Следующие шаги
- При согласовании вынести `terminal_before_release_deferred` в централизованную метрику release health.
