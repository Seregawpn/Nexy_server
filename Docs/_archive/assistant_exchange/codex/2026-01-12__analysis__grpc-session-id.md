# gRPC session_id mismatch

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-12
- ID (INS-###): INS-008

## Diagnosis
gRPC запрос не уходит из-за падения в GrpcClientIntegration: session_id приходит как float, вызывается .strip().

## Root Cause
ApplicationStateManager принимает session_id без валидации, а ModeManagementIntegration может передать его из mode.request без нормализации → float попадает в состояние → gRPC падает до отправки.

## Optimal Fix
Цель: централизованно валидировать/нормализовать session_id в Source of Truth и не допускать нестроковых значений.

## Verification
DoD: при session_id float gRPC не падает, либо запрос отклоняется с понятной ошибкой; корректные uuid4 проходят.

## Запрос/цель
Разобрать, почему gRPC запрос не отправляется, и дать архитектурно-совместимый фикс.

## Контекст
- Файлы: integration/integrations/grpc_client_integration.py, integration/core/state_manager.py, integration/integrations/mode_management_integration.py
- Документы: Docs/ARCHITECTURE_OVERVIEW.md, Docs/PROJECT_REQUIREMENTS.md
- Ограничения: централизованная логика, единый Source of Truth для session_id.

## Решения/выводы
- Корень в отсутствии валидации session_id на уровне ApplicationStateManager.

## Открытые вопросы
- Есть ли легаси-источник, который реально посылает float session_id в mode.request?

## Следующие шаги
- Добавить валидацию session_id в ApplicationStateManager.set_mode/update_session_id.
- При необходимости отклонять invalid session_id на входе mode.request.
