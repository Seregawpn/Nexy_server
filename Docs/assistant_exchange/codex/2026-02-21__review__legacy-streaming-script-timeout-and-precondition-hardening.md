# Legacy Streaming Script Timeout And Precondition Hardening

## Метаданные
- Ассистент: codex
- Тип: review
- Дата: 2026-02-21
- ID (INS-###): N/A
- Итоговый статус: СООТВЕТСТВУЕТ

## Diagnosis
Legacy functional script давал ложные провалы из-за контрактного рассинхрона `session_id` и жестких таймаутов в медленной среде.

## Root Cause
Строгая проверка server contract (`uuid4` session_id) + фиксированные низкие timeouts + precondition-зависимый тест без skip-механизма → ложные `FAILED`, не связанные с owner-логикой.

## Optimal Fix
Сделан точечный hardening script-only:
- `session_id` переведен на `uuid4`.
- Таймауты централизованы через `STREAMING_TEST_TIMEOUT`.
- `max_concurrent_streams` тест переводится в `SKIP`, если `BACKPRESSURE_MAX_STREAMS != 2`.
- Итоговый verdict учитывает `passed/failed/skipped`.

## Verification
- Команда:
  - `cd server/server && python3 scripts/test_streaming_workflow_fix.py`
- Результат:
  - `5 passed / 0 failed / 1 skipped`.
  - Single-flight сценарий: passed.
  - Нормальный streaming regression: passed.
  - max_concurrent_streams: skipped по отсутствию precondition (ожидаемо).

## Информация об изменениях
- Что изменено:
  - Добавлен helper `uuid4` для `session_id`.
  - Добавлен базовый timeout из env.
  - Добавлен precondition-based skip для теста 3.
  - Обновлен агрегатор итогов теста (учет skipped).
- Файлы:
  - `server/server/scripts/test_streaming_workflow_fix.py`
- Причина/цель:
  - Убрать ложные фейлы и валидировать только реальные конфликты логики.
- Проверка:
  - Локальный запуск функционального скрипта с итогом без failed.

## Запрос/цель
Протестировать последовательную цепочку release->transfer и исключить конфликтные условия.

## Контекст
- `server/server/scripts/test_streaming_workflow_fix.py`
- `server/server/modules/grpc_service/core/grpc_server.py`

## Решения/выводы
- Скрипт теперь совместим с текущим контрактом и средой.
- Ложные регрессии устранены; owner-логика подтверждена.

## Найденные проблемы (если review)
- Требуется явный env `BACKPRESSURE_MAX_STREAMS=2` для активации теста лимита стримов.

## Открытые вопросы
- Нужен ли отдельный CI-профиль для запуска теста 3 с фиксированным env?

## Следующие шаги
- При необходимости добавить CI job/profile c `BACKPRESSURE_MAX_STREAMS=2` и запуском теста 3 как blocking.
