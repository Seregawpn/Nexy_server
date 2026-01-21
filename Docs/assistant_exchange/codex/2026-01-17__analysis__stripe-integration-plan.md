# Stripe Integration Plan (Pre-Plan)

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-17
- ID (INS-###): INS-005

## Diagnosis
Current plan outlines component moves but misses explicit architecture ownership (ModuleFactory/ModuleCoordinator, EventBus contracts) and SoT boundaries, risking duplicate state and ad-hoc flow.

## Root Cause
Migration plan focused on file placement, not on architecture flow constraints (centralized coordination and SoT), leading to potential parallel decision paths and inconsistent state.

## Optimal Fix
Define module ownership and integration points first, then map each migrated component to a single SoT and coordinator path, with idempotency/race guards aligned to existing server/client architecture.

## Verification
Confirm webhook idempotency, quota updates, and workflow gating are centralized and tested via unit + Stripe CLI smoke.

## Запрос/цель
Provide architecture-aligned pre-plan for Stripe integration across server and client.

## Контекст
- Файлы: Docs/ARCHITECTURE_OVERVIEW.md, Docs/PROJECT_REQUIREMENTS.md
- Документы: Docs/ASSISTANT_COORDINATION_PROTOCOL.md, Docs/CODEX_PROMPT.md
- Ограничения: no re-architecture, no duplicate state owners

## Решения/выводы
- Server SoT: subscription module + database; client SoT: EventBus + integration contract.
- Centralize quota decisions in server workflow gate, not in client.

## Открытые вопросы
- Stripe keys/test vs prod, DB credentials, scheduler preference, feature-flag policy.

## Следующие шаги
- Align module boundaries and finalize migration map; then create implementation tasks for server/client.
