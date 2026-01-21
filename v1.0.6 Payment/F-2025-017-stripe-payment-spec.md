# Feature F-2025-017: Stripe Payment System Integration

> **Feature ID**: `F-2025-017-stripe-payment`

This ID MUST be reused across:
- Branch name: `feature/F-2025-017-stripe-payment`
- PR title: `[F-2025-017] Stripe Payment System Integration`
- Logs and metrics (every stage)
- Diagnostics scenarios
- Trace correlation

---

## 1. Goal & Success Criteria

- **User value**: 
  - Seamless subscription management through Stripe
  - Clear trial period with automatic transition to paid subscription
  - Grace period for billing issues
  - Quota enforcement for free tier users
  - Voice-controlled subscription commands (subscribe, cancel, status)

- **System impact**: 
  - **Server**: New subscription module, Stripe integration, webhook handler, quota checker, database migrations
  - **Client**: Deep link handling, payment UI integration (future)
  - **Database**: New tables (subscriptions, subscription_events, quota_usage, payments)

- **Success metrics**: 
  - Subscription conversion rate (trial → paid)
  - Webhook processing latency < 500ms
  - Quota check latency < 50ms (cached)
  - Zero payment data loss
  - 99.9% webhook processing success rate

---

## 2. User Scenario

### Primary Flow: New User Trial

1. User downloads and opens Nexy app
2. System automatically creates `paid_trial` subscription (14 days, no card required)
3. User can use all features during trial
4. System warns user 2 days, 1 day, and on the last day before trial ends
5. On trial expiration, system automatically opens Stripe Checkout (with 24h cooldown)
6. User completes payment → status changes to `paid`
7. User has full access

### Secondary Flow: Billing Problem

1. User has active `paid` subscription
2. Payment fails (card declined, insufficient funds)
3. System transitions to `billing_problem` status
4. Grace period (1 day) starts → user still has full access
5. If payment succeeds during grace period → back to `paid`
6. If grace period expires → transition to `limited_free_trial` (5/25/50 quotas)

### Tertiary Flow: Subscription Commands

1. User says: "What's my subscription status?"
2. LLM recognizes intent → generates `subscribe_status` command
3. System reads subscription context → generates TTS response
4. User hears: "You have 5 days left in your trial period"

---

## 3. End-to-End Data Flow

```
U1 User Trigger (voice input)
    ↓
C1 Client Input (StreamRequest with hardware_id)
    ↓
C2 Client State (PROCESSING mode)
    ↓
T1 Transport (gRPC StreamRequest)
    ↓
S1 Server Handler (extract hardware_id)
    ↓
S2 Server Logic (SubscriptionContextCache → get context)
    ↓
S2 Server Logic (QuotaChecker → check limits if limited_free_trial)
    ↓
S2 Server Logic (build LLM prompt with subscription context)
    ↓
S2 Server Logic (LLM processing → may generate subscription commands)
    ↓
S3 Server Logic (process subscription commands if any)
    ↓
S3 Server Logic (Stripe API calls if needed)
    ↓
T2 Transport (gRPC StreamResponse with text/audio)
    ↓
C3 Client Processing (deep link handling if payment return)
    ↓
C4 Client Output (TTS playback)
```

**Parallel Flow: Webhooks**

```
Stripe Webhook Event
    ↓
S1 Server Handler (verify signature)
    ↓
S3 Server Logic (check duplicate → subscription_events table)
    ↓
S3 Server Logic (process event → update subscriptions table)
    ↓
S3 Server Logic (invalidate cache)
    ↓
S3 Server Logic (send notification if needed)
```

---

## 4. Requirements Matrix Snapshot

See [STAGE_REQUIREMENT_MATRIX.md](STAGE_REQUIREMENT_MATRIX.md) for complete matrix.

**Key Requirements:**
- **Format**: hardware_id in all requests, subscription context in LLM prompts
- **Validation**: UUID format for hardware_id, enum validation for status
- **Security**: Stripe webhook signature verification, API keys in env
- **Errors**: Fallback to paid_trial on DB errors, retry for Stripe API
- **Observability**: Feature ID (F-2025-017-stripe-payment) in all logs
- **Performance**: Cache TTL 30s, atomic quota operations
- **Compatibility**: Backward compat for clients without hardware_id
- **Testing**: Unit, integration, E2E, webhook, race condition tests

---

## 5. Scope Breakdown

### 5.1 Client

**Modules to touch:**
- `integration/integrations/grpc_client_integration.py` — hardware_id в StreamRequest
- `integration/integrations/deep_link_integration.py` (NEW) — обработка `nexy://payment/*`
- `integration/integrations/speech_playback_integration.py` — TTS для сообщений о подписке

**State transitions:**
- LISTENING → PROCESSING (при запросе)
- PROCESSING → SLEEPING (после ответа)
- Нет специальных состояний для платежей

**Edge cases:**
- Отсутствие hardware_id → генерировать на клиенте
- Invalid deep link URL → игнорировать
- TTS ошибка → fallback на текстовое уведомление
- Offline режим → кэшировать deep link, синхронизировать при подключении

**Telemetry/logging additions:**
- Feature ID (`F-2025-017-stripe-payment`) во всех логах
- Trace ID для корреляции запросов
- Метрики: количество deep link обработок, TTS ошибки

**ALLOWED on client:**
- UX logic: обработка deep links, синхронизация после возврата
- Local fallbacks: кэширование deep link для offline
- Presentation formatting: форматирование сообщений о подписке

**FORBIDDEN on client:**
- Business logic: определение статуса подписки, проверка квот
- Access control: блокировка запросов по статусу
- Domain rules: правила перехода статусов

---

### 5.2 Server

**RPC/handlers:**
- `StreamAudio` (existing) — основной поток с проверкой подписки
- `StripeWebhook` (NEW) — обработка webhook событий от Stripe

**Validation strategy:**
- hardware_id: UUID формат, не пустой
- subscription status: enum validation (paid_trial, paid, billing_problem, limited_free_trial, etc.)
- Stripe webhook: signature verification (HMAC)
- Quota limits: числовые проверки (5/25/50)

**Business rules updates:**
- State machine для статусов подписки
- Quota enforcement для limited_free_trial
- Auto-checkout при истечении trial (с cooldown 24h)
- Trial warnings (2, 1, 0 days before expiration)
- Grace period (1 day) для billing_problem

**Database/storage impact:**
- **BLOCKING**: Миграции БД обязательны
- Таблицы: `subscriptions`, `subscription_events`, `quota_usage`, `payments`
- Индексы для производительности
- Rollback процедуры документированы

**Migration plan:**
- See [DATABASE_MIGRATIONS.md](DATABASE_MIGRATIONS.md)
- Миграция 001: создание таблиц
- Миграция 002: индексы
- ROLLBACK_001: полный откат

**Feature ID logging:**
- Все логи: `[F-2025-017-stripe-payment] ...`
- Метрики: тег `feature_id=F-2025-017-stripe-payment`
- Webhook события: `stripe_event_id` + `feature_id`

---

## 6. Contract Changes

**Proto diff summary:**
- Нет изменений в `streaming.proto` (используем существующие поля)
- `hardware_id` уже есть в `StreamRequest`
- Webhook endpoint — отдельный HTTP endpoint (не gRPC)

**New/updated messages:**
- Нет новых proto messages
- Используем существующие `StreamRequest` и `StreamResponse`

**Error semantics:**
- Invalid hardware_id → `grpc.StatusCode.INVALID_ARGUMENT`
- Quota exceeded → текстовый ответ через LLM (не gRPC error)
- Stripe API error → fallback на текстовый ответ
- Webhook signature error → HTTP 400

**Compatibility plan:**
- Старые клиенты без `hardware_id` → генерировать на сервере
- Feature flag `enable_payment_system` для постепенного rollout
- Kill-switch для экстренного отключения

---

## 7. Risks & Mitigations

| Risk | Stage | Impact | Likelihood | Mitigation |
|------|-------|--------|------------|------------|
| Stripe API недоступен | S3 | High | Low | Retry с exponential backoff, fallback на paid_trial |
| БД недоступна | S2, S3 | High | Low | Fallback на paid_trial, кэш с TTL |
| Race condition в квотах | S3 | Medium | Medium | Atomic операции (SELECT FOR UPDATE), retry |
| Webhook дубликаты | S3 | Medium | Medium | UNIQUE constraint на stripe_event_id, идемпотентность |
| Grace period истек → потеря доступа | S3 | High | Low | Автоматический переход в limited_free_trial |
| Deep link не обработан | C3 | Medium | Low | Логирование, синхронизация при следующем запросе |
| TTS ошибка для сообщений о подписке | C4 | Low | Low | Fallback на текстовое уведомление |
| Миграции БД в production | S3 | Critical | Low | Тестирование на staging, backup, rollback процедуры |

---

## 8. Testing Strategy

**Unit tests:**
- Client: `deep_link_integration.py`, hardware_id генерация
- Server: `SubscriptionContextCache`, `QuotaChecker`, `StripeService`, webhook handler

**Contract tests:**
- gRPC StreamRequest/StreamResponse с hardware_id
- Webhook HTTP endpoint (signature verification)

**Integration tests:**
- Полный цикл: запрос → проверка подписки → ответ
- Webhook обработка: все типы событий
- Quota enforcement: проверка лимитов
- State machine: все переходы статусов

**End-to-end diagnostics:**
- Расширить `run_diagnostics.py` сценариями:
  - `test_subscription_trial_flow`
  - `test_subscription_quota_enforcement`
  - `test_subscription_webhook_processing`
- Feature ID должен появляться в diagnostics output

**Failure simulations:**
- Stripe API timeout → fallback
- БД недоступна → fallback на paid_trial
- Webhook duplicate → идемпотентность
- Race condition в квотах → atomic операции

---

## 9. Observability & Permissions

**Feature ID usage:**
- Все логи: `[F-2025-017-stripe-payment] ...`
- Метрики: тег `feature_id=F-2025-017-stripe-payment`
- Trace correlation: `trace_id` + `feature_id` + `hardware_id`

**Logs/metrics/traces by stage:**

| Stage | Logs | Metrics | Traces |
|-------|------|---------|--------|
| U1 | feature_id | - | trace_id |
| C1 | feature_id + hardware_id | - | trace_id |
| S1 | feature_id + hardware_id | - | trace_id |
| S2 | feature_id + subscription_status | subscription_check_latency | trace_id |
| S3 | feature_id + stripe_event_id | webhook_processing_latency | trace_id |
| S3 | feature_id + quota_status | quota_check_latency | trace_id |
| C3 | feature_id + deep_link_action | deep_link_processed | trace_id |
| C4 | feature_id | tts_playback_latency | trace_id |

**Sensitive data handling:**
- Stripe customer_id, subscription_id — логировать только первые 4 символа
- Payment amounts — логировать только суммы (не карты)
- Webhook payload — логировать только event_type и metadata (не полный payload)

**Permission/access updates:**
- Webhook endpoint: публичный (Stripe должен иметь доступ)
- Webhook signature verification: обязательна
- Admin endpoints (future): требуют authentication

---

## 10. Release & Rollout

**Feature flag / config key:**
- `features.enable_payment_system` (default: `false`)
- `kill_switches.disable_payment_system` (default: `false`)

**Rollout plan:**
1. **Phase 1**: Feature flag OFF, миграции БД применены
2. **Phase 2**: Feature flag ON для тестовых пользователей (10%)
3. **Phase 3**: Feature flag ON для всех пользователей
4. **Phase 4**: Мониторинг метрик, оптимизация

**Rollback procedure:**
1. Установить `kill_switches.disable_payment_system = true`
2. Система автоматически переключится на дефолтный доступ (paid_trial для всех)
3. Webhook обработка продолжит работать (для синхронизации)
4. При необходимости: откат миграций БД (ROLLBACK_001.sql)

**Support/documentation updates:**
- README для модуля subscription
- API документация для webhook endpoint
- Troubleshooting guide
- User documentation (trial, subscription, billing)

---

## 11. Checklist Link

See [PAYMENT_PLAN_COMPLETENESS_CHECK.md](PAYMENT_PLAN_COMPLETENESS_CHECK.md) for readiness checklist.

---

## 12. Open Questions

1. **Q**: Нужен ли отдельный модуль для subscription или интегрировать в StreamingWorkflowIntegration?
   **A**: Отдельный модуль `SubscriptionModule` для разделения ответственности.

2. **Q**: Как обрабатывать пользователей без hardware_id (старые клиенты)?
   **A**: Генерировать hardware_id на сервере при первом запросе.

3. **Q**: Нужен ли admin dashboard для управления подписками?
   **A**: Пока нет, можно добавить позже.

4. **Q**: Как обрабатывать частичные refunds?
   **A**: Пока не обрабатываем, можно добавить позже при необходимости.

---

**Status:** ✅ Specification complete, ready for implementation




