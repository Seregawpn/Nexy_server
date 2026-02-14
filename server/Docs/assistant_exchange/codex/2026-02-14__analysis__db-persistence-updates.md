# Analysis: DB data collection and persistence across remote server updates

## Request
Понять, какие данные сейчас записываются в БД, и как исключить их потерю при обновлениях удаленного сервера.

## Mandatory sources check
Missing in current cwd:
- `Docs/PROJECT_REQUIREMENTS.md`
- `Docs/ARCHITECTURE_OVERVIEW.md`
- `Docs/ASSISTANT_COORDINATION_PROTOCOL.md`
- `Docs/ANTIGRAVITY_PROMPT.md`
- `Docs/CODEX_PROMPT.md`
- `Docs/assistant_exchange/TEMPLATE.md`

Used valid fallback/available sources:
- `AGENTS.md`
- `../Docs/PROJECT_REQUIREMENTS.md`
- `../Docs/ARCHITECTURE_OVERVIEW.md`
- `../Docs/_archive/ASSISTANT_COORDINATION_PROTOCOL.md`
- `../Docs/_archive/ANTIGRAVITY_PROMPT.md`
- `../Docs/_archive/CODEX_PROMPT.md`
- `../Docs/_archive/assistant_exchange/TEMPLATE.md`
- `server/Docs/ARCHITECTURE_OVERVIEW.md`
- `server/Docs/DATABASE_SCHEMA.sql`
- `server/scripts/apply_payment_migrations.py`
- `server/modules/database/repository/token_usage_repository.py`
- `server/modules/subscription/repository/subscription_repository.py`
- `server/api/webhooks/stripe_webhook.py`
- `server/scripts/setup_database.sh`

## Current DB data (from schema + repository usage)
Core tables:
- `users`, `sessions`, `commands`, `llm_answers`, `screenshots`, `performance_metrics`
- `token_usage`

Payment/subscription tables:
- `subscriptions`, `subscription_events`, `quota_usage`, `payments`

Data actually written in active flows:
- Token usage (`token_usage`) from LLM and memory/browser token tracking.
- Subscription status and Stripe IDs (`subscriptions`).
- Stripe webhook events and idempotency ledger (`subscription_events`).
- Payment rows (`payments`) in repository methods.
- Memory context (`users.short_term_memory/long_term_memory`) when memory manager is enabled.

## Risk found
`server/scripts/setup_database.sh` includes optional DB recreation path with:
- `DROP DATABASE $DB_NAME`
- `CREATE DATABASE $DB_NAME ...`

If chosen during maintenance/update, this causes total data loss.

## Recommended persistence model
- Keep PostgreSQL outside deploy artifact lifecycle (separate managed DB or separate VM disk/volume).
- Treat app deploy and DB lifecycle as separate pipelines.
- Only additive/idempotent migrations during update.
- Pre-update backup + post-update verification + rollback playbook.

## Quick operational checklist (no architecture rewrite)
1. Before deploy: `pg_dump` snapshot (or managed DB PITR snapshot).
2. Deploy app code only; never run DB recreation scripts in update flow.
3. Run only migration scripts (`CREATE TABLE IF NOT EXISTS`, additive ALTERs).
4. Verify row counts for critical tables (`subscriptions`, `subscription_events`, `token_usage`).
5. Keep rollback: app version rollback + DB restore point.

