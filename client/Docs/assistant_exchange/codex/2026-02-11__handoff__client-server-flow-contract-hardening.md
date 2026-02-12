# Client-Server Flow Contract Hardening

## Метаданные
- Ассистент: codex
- Тип: handoff
- Дата: 2026-02-11
- ID (INS-###): INS-UNKNOWN

## Diagnosis
Были активны параллельные/legacy пути в action transport и cancel semantics, что нарушало единый контракт Flow.

## Root Cause
Историческая обратная совместимость и локальные fallback-пути не были полностью удалены после централизации EventBus/Mode/Interrupt.

## Optimal Fix
Выполнено:
1. Удалён legacy action path через `text_chunk` в `GrpcClientIntegration`.
2. `grpc.request_cancel` сделан строго session-scoped (без fallback на «последний inflight»).
3. Удалён дублирующий cancel-trigger по `keyboard.short_press` в `ActionExecutionIntegration`.
4. Исправлено чтение payload (`event.data`) в `InterruptManagementIntegration._on_app_state_changed`.
5. Отключён fast-path для mode/state событий в `EventBus` для детерминированной последовательности.

## Verification
- `python3 -m py_compile` для изменённых файлов: OK.
- Поиск legacy/дубликатов:
  - `_on_keyboard_short_press` в `ActionExecutionIntegration`: отсутствует.
  - `text_chunk_legacy` и `_extract_action_from_legacy_text` в `GrpcClientIntegration`: отсутствуют.

## Pre-Change Gate Evidence (обязательно)
- Прочитанные документы: root/client AGENTS, DOCS_INDEX, PRE_CHANGE_CHECKLIST, PROJECT_REQUIREMENTS, ARCHITECTURE_OVERVIEW, FLOW_INTERACTION_SPEC, STATE_CATALOG, FEATURE_FLAGS.
- Source of Truth: `Docs/FLOW_INTERACTION_SPEC.md`, `ModeManagementIntegration`, `InterruptManagementIntegration`, `GrpcClientIntegration`.
- Дублирование: legacy action-text path + double cancel trigger.
- Feature Flags check: новых флагов не добавлялось.
- Race check: устранён session-less cancel fallback; снижен риск out-of-order mode callbacks.

## Запрос/цель
Имплементировать найденные исправления по централизации клиент-серверного взаимодействия.

## Контекст
- Файлы: `integration/integrations/grpc_client_integration.py`, `integration/integrations/action_execution_integration.py`, `integration/integrations/interrupt_management_integration.py`, `integration/core/event_bus.py`.

## Решения/выводы
- Контракт transport/cancel стал строже и ближе к канону Flow.
- Удалён один дублирующий путь отмены и один legacy путь доставки actions.

## Открытые вопросы
- Нужен ли временный telemetry-флаг для контроля редких серверов, которые ещё шлют action через text_chunk.

## Следующие шаги
- Добавить тесты: session-less cancel reject, action_message-only transport, отсутствие double-cancel на short tap.
