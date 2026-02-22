# Legacy Streaming Workflow Script Contract Sync

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-21
- ID (INS-###): N/A

## Diagnosis
Legacy-скрипт `test_streaming_workflow_fix.py` использовал невалидный для текущего контракта формат `session_id`, что давало ложные ошибки и мешало оценивать реальные конфликты.

## Root Cause
Ужесточение контракта на сервере (`session_id` строго `uuid4`) + старые шаблоны идентификаторов в functional script → запросы отклонялись до проверки основной логики.

## Optimal Fix
- Синхронизировать script с контрактом: генерировать `uuid4` для всех тестовых `session_id`.
- Сохранить архитектуру без изменений: owner-path остается в `grpc_server.py` (`COLLECT` буфер, `COMMIT` запуск).

## Verification
- Каноничные тесты и guard-скрипты ранее прошли успешно.
- Повторный запуск legacy script после фикса:
  - исчезла ошибка `session_id is required and must be provided by client`;
  - `single-flight` сценарий отработал корректно;
  - часть тестов всё ещё падает по `DEADLINE_EXCEEDED` (средовая/latency-зависимость, не контракт).

## Информация об изменениях
- Что изменено:
  - Добавлен генератор валидного `session_id` (`uuid4`) в legacy script.
  - Все тестовые места генерации `session_id` переведены на новый helper.
- Файлы:
  - `server/server/scripts/test_streaming_workflow_fix.py`
- Причина/цель:
  - Убрать ложные падения, вызванные рассинхроном с текущим контрактом идентификаторов.
- Проверка:
  - `cd server/server && python3 scripts/test_streaming_workflow_fix.py`

## Запрос/цель
Подтвердить корректность цепочки удержание/отпускание/передача без конфликтов и дублей.

## Контекст
- `server/server/modules/grpc_service/core/grpc_server.py`
- `server/server/scripts/test_streaming_workflow_fix.py`
- `server/server/tests/test_grpc_phase_collect_commit.py`

## Решения/выводы
- Контрактный конфликт legacy script устранен.
- Основная архитектурная цепочка остается централизованной и подтверждена каноничными тестами.

## Открытые вопросы
- Нужно ли повысить timeout/добавить stubbed provider режим для legacy functional script, чтобы убрать `DEADLINE_EXCEEDED` в локальной среде?

## Следующие шаги
- Если нужно сделать legacy script стабильным для CI: вынести его в режим stub/mock либо увеличить таймауты и зафиксировать профиль окружения.
