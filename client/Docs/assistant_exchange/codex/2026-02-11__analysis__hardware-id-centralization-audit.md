# Hardware ID/Salt Audit

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-11
- ID (INS-###): N/A

## Diagnosis
Проверка показала, что централизованный контур `hardware_id` в целом соблюден, но есть локально дублированная логика ожидания ID в `PaymentIntegration`.
Отдельного механизма `salt` для ID в клиенте нет: передается нативный `hardware_id`.

## Root Cause
Архитектура задает одного owner (`hardware_id_integration`), но часть потребителей реализует собственные wait/retry ветки вместо общего await-контракта.
Это повышает риск рассинхронизации и race-сценариев при одновременных `hardware.id_request`.

## Optimal Fix
Сохранить `hardware_id_integration` как единственный Source of Truth и убрать polling-wait из `PaymentIntegration` в пользу общего await-механизма (аналогично `GrpcClientIntegration._await_hardware_id`).

## Verification
- Подтвердить единый owner: `integration/integrations/hardware_id_integration.py`
- Подтвердить отправку в gRPC: `integration/integrations/grpc_client_integration.py` + `modules/grpc_client/core/grpc_client.py` + `modules/grpc_client/proto/streaming.proto`
- Проверить отсутствие `salt`-трансформаций: поиск по `salt|hash|uuid5` в `modules/hardware_id` и `integration/integrations`

## Pre-Change Gate Evidence (обязательно)
- Прочитанные документы: `AGENTS.md`, `Docs/DOCS_INDEX.md`, `Docs/PRE_CHANGE_CHECKLIST.md`, `Docs/PROJECT_REQUIREMENTS.md`, `Docs/ARCHITECTURE_OVERVIEW.md`, `Docs/FLOW_INTERACTION_SPEC.md`, `Docs/STATE_CATALOG.md`, `Docs/FEATURE_FLAGS.md`, `../Docs/DOCS_INDEX.md`, `../Docs/PRE_CHANGE_CHECKLIST.md`, `../Docs/PROJECT_REQUIREMENTS.md`, `../Docs/ARCHITECTURE_OVERVIEW.md`, `../Docs/ASSISTANT_COORDINATION_PROTOCOL.md`, `../Docs/ANTIGRAVITY_PROMPT.md`, `../Docs/CODEX_PROMPT.md`, `../Docs/FEATURE_FLAGS.md`, `../Docs/assistant_exchange/TEMPLATE.md`
- Source of Truth: `integration/integrations/hardware_id_integration.py` (получение/кэш/ответ), `modules/hardware_id/*` (детекция/валидация/кэш)
- Дублирование: локальный polling wait в `integration/integrations/payment_integration.py` дублирует await-паттерн из `integration/integrations/grpc_client_integration.py`
- Feature Flags check: новых флагов нет, конфликтов с `Docs/FEATURE_FLAGS.md` не внесено
- Race check: concurrent `hardware.id_request` + локальные wait-loop в потребителях; guard: single owner + single-flight await API

## Запрос/цель
Проверить корректность получения и передачи ID, наличие дублей/конфликтов/гонок и степень централизации.

## Контекст
- Файлы: `integration/integrations/hardware_id_integration.py`, `integration/integrations/grpc_client_integration.py`, `integration/integrations/payment_integration.py`, `modules/hardware_id/*`, `modules/grpc_client/*`
- Ограничения: без реархитектуры, в рамках текущих модулей.

## Решения/выводы
- `hardware_id` берется из `SystemProfilerBridge` и кэшируется; `fallback_to_random=false` по умолчанию.
- В gRPC StreamRequest `hardware_id` передается явно как required field.
- `salt`-слой в клиенте отсутствует.
- Централизация частично нарушена локальным ожиданием ID в PaymentIntegration.

## Следующие шаги
- Вынести единый helper ожидания hardware_id (или reuse существующего паттерна) и удалить polling loop в PaymentIntegration.
