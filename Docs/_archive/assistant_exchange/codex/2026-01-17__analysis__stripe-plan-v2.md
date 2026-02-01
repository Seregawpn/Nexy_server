# Stripe Integration Plan v2 Review

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-17
- ID (INS-###): INS-005

## Diagnosis
Plan v2 is architecture-aligned but still needs explicit ModuleFactory/Coordinator wiring and clear SoT boundaries for scheduler ownership to avoid split control paths.

## Root Cause
Focus on component list without binding to existing server orchestration flow can introduce parallel initialization and cache invalidation inconsistencies.

## Optimal Fix
Bind subscription_module to ModuleFactory/Coordinator, keep scheduler inside module, and gate StreamingWorkflow through the single can_process path; avoid any client-side state decisions.

## Verification
Use Stripe CLI for webhook idempotency, unit tests for quota and state machine, and log-based validation of subscription_gate allow/deny.

## Запрос/цель
Confirm and refine the pre-plan for Stripe integration (v2).

## Контекст
- Файлы: Docs/ARCHITECTURE_OVERVIEW.md
- Документы: Docs/PROJECT_REQUIREMENTS.md, Docs/ASSISTANT_COORDINATION_PROTOCOL.md
- Ограничения: no re-architecture, no duplicate SoT

## Решения/выводы
- Server is sole SoT for subscription/quota/usage; client only reflects status.
- Webhook idempotency + SELECT FOR UPDATE are mandatory for concurrency safety.

## Открытые вопросы
- Scheduler choice (APScheduler vs existing scheduler conventions).
- DB credentials and migration runner.

## Следующие шаги
- Map module wiring in ModuleFactory/Coordinator and define EventBus contract docs for client.
