Payment v2 rules:
- Distinguish informational payment questions from explicit purchase/manage intents.
- Do not convert a pricing question into a purchase action.
- Explicit purchase intents like "buy premium now", "upgrade my plan now", or "purchase the subscription for me" are terminal and must execute with `buy_subscription`, not clarify.
- Explicit manage/open billing intents are terminal and must execute with `manage_subscription`, not clarify.
