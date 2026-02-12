# Client-Server Flow Audit

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-11
- ID (INS-###): INS-UNKNOWN

## Diagnosis
Клиент-серверный поток в целом централизован через EventBus/ModeManagement/GrpcClientIntegration, но есть расхождения с каноническим контрактом: legacy action path через `text_chunk`, session-less cancel fallback и дубли cancel-trigger в ActionExecution.

## Root Cause
Исторические compatibility-ветки и локальные safety-обходы остались активными после миграции на канонический контракт `ActionMessage + interrupt.request -> grpc.request_cancel`.

## Optimal Fix
- Оставить единый owner протокола действий: `grpc.response.action` только из `action_message`.
- Запретить session-less cancel fallback (требовать `session_id` в `grpc.request_cancel`).
- Убрать дублирующий cancel trigger (`keyboard.short_press`) в `ActionExecutionIntegration`; оставить `interrupt.request` как единый вход.
- Исправить чтение payload в `InterruptManagementIntegration._on_app_state_changed` через `event.data`.
- Для `app.mode_changed` вернуть детерминированный dispatch (без fire-and-forget для критичных подписчиков) или выделить sync-critical subscribers.

## Verification
- Проверка, что `grpc.response.action` публикуется только из `action_message`.
- Проверка, что `grpc.request_cancel` без `session_id` не отменяет «последнюю» сессию.
- Проверка отсутствия двойной отмены actions на один short tap.
- Проверка, что `InterruptManagementIntegration` видит `old_mode/new_mode` и корректно чистит active interrupts на переходе в SLEEPING.

## Pre-Change Gate Evidence (обязательно)
- Прочитанные документы: `AGENTS.md`, `../AGENTS.md`, `Docs/DOCS_INDEX.md`, `Docs/PRE_CHANGE_CHECKLIST.md`, `Docs/PROJECT_REQUIREMENTS.md`, `Docs/ARCHITECTURE_OVERVIEW.md`, `Docs/FLOW_INTERACTION_SPEC.md`, `Docs/STATE_CATALOG.md`, `Docs/FEATURE_FLAGS.md`, `../Docs/DOCS_INDEX.md`, `../Docs/PRE_CHANGE_CHECKLIST.md`, `../Docs/ASSISTANT_COORDINATION_PROTOCOL.md`, `../Docs/FEATURE_FLAGS.md`, `../Docs/ANTIGRAVITY_PROMPT.md`, `../Docs/CODEX_PROMPT.md`, `../Docs/assistant_exchange/TEMPLATE.md`.
- Source of Truth: `Docs/FLOW_INTERACTION_SPEC.md` (контракты событий), `integration/integrations/grpc_client_integration.py` (owner gRPC I/O), `integration/integrations/interrupt_management_integration.py` (owner cancel request), `integration/integrations/mode_management_integration.py` (owner mode transitions).
- Дублирование: найдено (legacy action-tunneling + двойной cancel trigger).
- Feature Flags check: новых флагов не требуется.
- Race check: найдено (session-less cancel fallback, async fast dispatch для `app.mode_changed`).

## Запрос/цель
Проверить корректность передачи/обработки данных между клиентом и сервером, найти конфликты, дубли, гонки и точки централизации.

## Контекст
- Файлы: `integration/integrations/grpc_client_integration.py`, `integration/integrations/interrupt_management_integration.py`, `integration/integrations/action_execution_integration.py`, `integration/core/event_bus.py`, `integration/integrations/mode_management_integration.py`, `integration/workflows/processing_workflow.py`.
- Документы: `Docs/FLOW_INTERACTION_SPEC.md`, `Docs/ARCHITECTURE_OVERVIEW.md`, `Docs/STATE_CATALOG.md`, `Docs/PROJECT_REQUIREMENTS.md`.
- Ограничения: без реархитектуры; сохранить текущие границы модулей.

## Решения/выводы
- Базовая архитектура правильная (централизация через EventBus + ModeManagement + state manager).
- Основные риски сосредоточены в legacy-ветках и недетерминированных/дублирующих cancel-path.
- Требуется consolidation 3 точек: action transport, cancel semantics, mode event ordering.

## Открытые вопросы
- Допускается ли полностью удалить поддержку `text_chunk_legacy` без обратной совместимости сервера?
- Нужен ли жесткий контракт: `grpc.request_cancel` всегда с `session_id` (drop invalid) или допустим explicit fallback policy?

## Следующие шаги
- Подготовить PR с удалением legacy action path и session-less cancel fallback.
- Ввести единый cancel trigger в ActionExecution.
- Добавить regression tests на cancel ordering и action transport contract.
