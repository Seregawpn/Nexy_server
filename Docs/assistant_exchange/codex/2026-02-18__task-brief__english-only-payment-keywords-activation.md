# Task Brief: English-only payment keyword activation

Date: 2026-02-18
Assistant: Codex

## Goal
Activate payment prompt context only by English billing/subscription keywords and keep action intent strict.

## Changes
1. Expanded `payment` keywords (English only) in:
- `server/server/config/intent_keywords.yaml`
- `server/server/config/prompts.py` (`_DEFAULT_PROMPT_KEYWORDS['payment']` fallback)

2. Removed non-English action-intent patterns from:
- `server/server/integrations/workflow_integrations/streaming_workflow_integration.py`
- method: `_is_explicit_billing_open_intent(...)`

## Effect
- Payment prompt section is activated by English billing/subscription terms.
- Informational payment/subscription queries still get text answers.
- Command action remains gated by explicit English open/manage/buy/upgrade/pay intent.

## Validation
- `python3 -m py_compile server/server/config/prompts.py server/server/integrations/workflow_integrations/streaming_workflow_integration.py`
- spot checks via `resolve_prompt_sections`:
  - "when does my subscription end" -> payment=True
  - "open billing portal" -> payment=True
  - "how are you" -> payment=False
