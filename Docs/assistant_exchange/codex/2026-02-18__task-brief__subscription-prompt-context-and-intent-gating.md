# Task Brief: Subscription prompt context and intent gating

Date: 2026-02-18
Assistant: Codex

## Goal
Make subscription answers concrete (dates/status/days left) and prevent wrong command triggering for informational billing questions.

## Changes
1. Updated prompt contract in `server/server/config/prompts.py` (`PROMPT_PAYMENT`):
- Added "Subscription Q&A Contract".
- Explicitly requires text-only answers for informational subscription questions.
- Requires concrete values from `SUBSCRIPTION_FACTS`.

2. Updated workflow context building in `server/server/integrations/workflow_integrations/streaming_workflow_integration.py`:
- Enriched `subscription_context` with:
  - `access_tier`
  - `billing_active`
  - `recommended_billing_route`
  - `period_end_utc`
  - `days_left`
  - `facts_line` (`[SUBSCRIPTION_FACTS ...]`)
- Added explicit-intent detector `_is_explicit_billing_open_intent(...)`.
- Command forcing now runs only for explicit open/manage/buy/upgrade intent.
- Command selection is route-based (`manage_subscription` vs `buy_subscription`) from `recommended_billing_route`.
- Informational subscription questions are instructed to stay text-only.

## Architecture gates
- Single owner: subscription status source is `subscription_module.get_subscription_status(...)`.
- Zero duplication: reused existing subscription module status API instead of introducing new state owner.
- Anti-race: no new mutable shared state; request-scoped enrichment only.
- Flag lifecycle: no new flags introduced.

## Verification
- `python3 -m py_compile server/server/integrations/workflow_integrations/streaming_workflow_integration.py server/server/config/prompts.py`
- Grep checks for new `SUBSCRIPTION_FACTS` and contract strings completed.
