# Server Risk Audit

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-11
- ID (INS-###): INS-005

## Diagnosis
Потенциальные риски в серверной части связаны с контрактами session_id/hardware_id и областью прерываний (interrupt) — возможны несогласованности и чрезмерное прерывание.

## Root Cause
Нестрогий контракт для session_id и hardware_id в gRPC, плюс interrupt по hardware_id без session_id → риск рассинхрона и ложных/глобальных прерываний.

## Optimal Fix
Цель: привести контракты к единому источнику истины и минимизировать риск глобальных прерываний.

## Verification
Сверить proto + grpc_server + unified_config требования; проверить поведение при пустом session_id/hardware_id и при параллельных сессиях одного hardware_id.

## Запрос/цель
Аудит серверной части: потенциально опасные точки, дубли, конфликты, гонки.

## Контекст
- Файлы: server/server/modules/grpc_service/core/grpc_server.py, server/server/modules/grpc_service/streaming.proto, server/server/integrations/workflow_integrations/streaming_workflow_integration.py, server/server/modules/interrupt_handling/*, server/server/modules/session_management/providers/session_tracker.py
- Документы: server/server/Docs/ARCHITECTURE_OVERVIEW.md, server/server/config/unified_config.yaml

## Решения/выводы
- session_id: grpc_server генерирует при отсутствии, но конфиг требует reuse из request; возможен контрактный конфликт.
- hardware_id: допускается "unknown" без hard-fail → риск неверной корреляции и interrupt.
- interrupt: InterruptSession работает по hardware_id, без session_id → при нескольких сессиях одного hardware_id прерывание будет слишком широким.

## Найденные проблемы (если review)
- N/A

## Открытые вопросы
- Нужно ли запретить "unknown" hardware_id на уровне grpc_server?
- Нужен ли session_id в InterruptRequest для точного прерывания?

## Следующие шаги
- Сверить требования unified_config с фактическим поведением grpc_server.
- При необходимости — минимально уточнить контракт (fail on missing hardware_id, session_id must be provided).
