# Production Checklist — Server

Минимальный go/no‑go чеклист для прод‑релиза сервера.

## 1) Tests
1. `pytest server/tests -q` проходит без ошибок.

## 2) gRPC Контракты
1. StreamAudio: валидные `hardware_id` и `session_id` дают стабильный стрим.
1. InterruptSession: прерывание активной сессии работает.

## 3) Конфиг и флаги
1. `server/server/config.env` заполнен (секреты, Stripe, Gemini, Azure).
1. Feature flags согласованы с клиентом.
1. `SUBSCRIPTION_ENABLED` и `SUBSCRIPTION_KILL_SWITCH` выставлены осознанно.

## 4) Observability
1. Логи пишутся в едином формате.
1. Маскирование секретов включено и проверено.
1. Метрики не падают и не шумят.

## 5) Payment/Subscription (если включено)
1. Webhook secrets корректны.
1. Статусы подписки соответствуют state machine.
1. Fail‑open поведение подтверждено.

## 6) Rollback
1. Понятно, как выключить фичи через flags.
1. Понятно, как быстро отключить подписки через kill‑switch.
