# Task Summary
- Goal: speak payment success immediately after successful payment.
- Result: added optimistic TTS on payment deep link success with guard to avoid double-announce.

# Changes
- client/integration/integrations/payment_integration.py
  - Added `_payment_success_announced_at` guard.
  - On `payment/success` deep link, immediately call server TTS and then sync status.
  - On `subscription.status_updated` paid/paid_trial, announce only if not already announced.

# Verification Steps (Manual)
1. Complete payment (deep link success triggered).
2. Confirm immediate TTS: "Payment successful…"
3. Verify polling updates status without re-announcing.

# Notes / Risks
- If deep link triggers but server status later fails, user might hear optimistic success; polling will still update UI.
- Required docs (Docs/CODEX_PROMPT.md, Docs/ANTIGRAVITY_PROMPT.md, Docs/assistant_exchange/TEMPLATE.md) were not found in repo.

# Follow-ups
- Consider adding a short "Checking status" notification if server does not confirm within N seconds.
