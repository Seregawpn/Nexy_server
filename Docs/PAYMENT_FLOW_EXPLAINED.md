# Payment System Logic & Schema (As Implemented)

See: Docs/PAYMENT_UPDATE_CONTROLLER.md for command/fallback governance.
See: Docs/PAYMENT_REQUIREMENTS.md for ownership and server-only speech rules.

## 1. Architecture Overview (High-Level)

Система работает по принципу **Centralized Source of Truth** (Server) с реактивным клиентом.

*   **Server (`SubscriptionModule`):** Единственный владелец логики. Решает "Можно ли обработать запрос?" (`can_process`). Управляет квотами и статусами.
*   **Stripe:** Платёжный шлюз. Хранит данные карт, проводит списания.
*   **Client (`PaymentIntegration`):** Тонкий клиент. Не считает квоты. Только отображает статус (через EventBus) и перенаправляет на оплату.

### Data Flow Diagram

```mermaid
sequenceDiagram
    participant User
    participant Client
    participant Server (Gate)
    participant DB
    participant Stripe

    %% Startup Check
    User->>Client: Launch App
    Client->>Server: gRPC Handshake
    Server->>DB: Check Subscription Status
    DB-->>Server: Status (paid_trial/paid/billing_problem/limited_free_trial/...)
    Server-->>Client: Context (if billing issue)

    %% Request Processing (The Gate)
    User->>Client: "Calculate this..."
    Client->>Server: gRPC Request (HardwareID)
    Note over Server: SubscriptionModule.can_process()
    
    rect rgb(240, 248, 255)
    Note right of Server: 1. Config Check (enabled/kill_switch)
    Note right of Server: 2. Init Check
    Note right of Server: 3. Cache Check (TTL 30s)
    Note right of Server: 4. Quota Check (DB) 
    end
    
    alt Allowed
        Server->>Server: Process Request (LLM)
        Server->>DB: Increment Usage (Post-process)
        Server-->>Client: Result
    else Denied (Quota Exceeded / Grace Expired / Unknown Status)
        Server-->>Client: Error (Payment Required)
        Client->>User: Show "Upgrade" Dialog
    end

    %% Payment Flow
    User->>Client: Click "Upgrade"
    Client->>Stripe: Open Stripe Checkout (URL)
    User->>Stripe: Pay $$
    Stripe->>Server: Webhook (checkout.session.completed)
    Server->>DB: Create subscription -> paid_trial
    Server->>Server: Invalidate Cache
    
    %% Sync Back
    Stripe->>Client: Redirect to nexy://payment/success
    Client->>Client: Event: payment.sync_requested
    Client->>Server: Request Status Update
    Server-->>Client: New Status: paid
    Client->>User: "Thanks! You are Pro."
```

---

## 2. Логика Проверок (The Gate Logic)

Вся логика сосредоточена в методе `SubscriptionModule.can_process(hardware_id)`.

Порядок проверок (Waterfall):

1.  **Config Check:** если `SubscriptionConfig.enabled=False` или `kill_switch=True` → доступ разрешён (**Fail-Open**, reason=`subscription_disabled`).
2.  **Initialization Check:** если модуль включен, но не инициализирован → логируется ошибка, доступ разрешён (**Fail-Open**).
3.  **Cache Check:** in-memory кэш с TTL (`cache_ttl_seconds`). Если есть свежий результат → возврат из кэша.
4.  **Quota/Status Check (DB):**
    *   **Запрос в БД:** получаем текущий `status` и счетчики использования.
    *   **Status Logic (как в коде):**
        *   `paid_trial`, `paid`, `admin_active`, `grandfathered`: **ALLOWED** (безлимит).
        *   `billing_problem`:
            *   если `grace_period_end_at > now` → **ALLOWED** (`reason='grace_period_active'`)
            *   иначе → **DENIED** (`reason='grace_period_expired'`)
        *   `limited_free_trial`: проверка квот:
            *   `daily_used >= limit` → **DENIED** (`reason='daily_limit_exceeded'`)
            *   `weekly_used >= limit` → **DENIED** (`reason='weekly_limit_exceeded'`)
            *   `monthly_used >= limit` → **DENIED** (`reason='monthly_limit_exceeded'`)
            *   иначе → **ALLOWED** (`reason='within_quota'`)
        *   неизвестный статус → **DENIED** (`reason='unknown_status'`)
    *   **Нет записи в БД:** **ALLOWED** (`reason='new_user'`), запись создаётся позже через webhook.
5.  **Result Caching:** кэшируются только **ALLOWED** результаты.

---

## 3. Quota Management (Счетчики)

Для пользователей в статусе `limited_free_trial` действуют лимиты.

**Default Limits (Config):**
*   **Daily:** 5 запросов
*   **Weekly:** 25 запросов
*   **Monthly:** 50 запросов

**Сброс Квот (Scheduler):**
*   **Daily Reset:** Каждую ночь в 00:05 (локальное время сервера).
*   **Weekly Reset:** Каждый понедельник в 00:05.
*   **Monthly Reset:** 1-го числа каждого месяца в 00:05.

*После сброса кэш всех пользователей инвалидируется.*

---

## 4. Payment Lifecycle (Смена Статусов)

Как пользователь переходит между состояниями:

1.  **New User:** при первом запросе запись **не создаётся**. Gate возвращает `allowed=True` с `reason='new_user'`.
2.  **Trial / First Payment:**
    *   `checkout.session.completed` → если записи нет, создаётся `paid_trial`.
3.  **Paid:**
    *   `invoice.payment_succeeded` → статус `paid`.
4.  **Payment Failure:**
    *   `invoice.payment_failed` → статус `billing_problem` + `grace_period_end_at`.
    *   Пока grace не истёк → **ALLOWED**.
    *   После grace → `grace_period_check` переводит статус в `limited_free_trial`.
5.  **Subscription Updated/Deleted:**
    *   `customer.subscription.updated`:
        *   `active` → `paid`
        *   `past_due|unpaid` → `billing_problem`
        *   `canceled|incomplete_expired` → `limited_free_trial`
    *   `customer.subscription.deleted` → `limited_free_trial`

---

## 5. Client Integration Details

Клиент (`PaymentIntegration.py`) работает реактивно.

*   **Deep Links:**
    *   `nexy://payment/success` → публикует `payment.sync_requested`.
    *   `nexy://payment/cancel` → показывает уведомление об отмене.
    *   `nexy://payment/billing_problem` → показывает ошибку оплаты.
*   **EventBus:**
    *   Слушает `subscription.status_updated`.
    *   Обновляет локальный `cached_status` (UI кэш).
    *   Также запрашивает sync при `grpc.connected`.

---

## 6. Ключевые файлы (Code Reference)

*   **Logic Core:** `server/server/modules/subscription/subscription_module.py`
*   **Limits:** `server/server/modules/subscription/core/quota_checker.py`
*   **Config:** `server/server/config/unified_config.py` (`SubscriptionConfig`)
*   **Client:** `client/integration/integrations/payment_integration.py`

---

## 7. Fallbacks & Customer Portal (User Experience)

### Payment Failure / Quota Exceeded
*   **Audio Response:** отсутствует. Сервер возвращает ошибку (без генерации аудио).
*   **Error Code:** `PERMISSION_DENIED` (или аналог в gRPC ответе).
*   **Client Handling:** UI должен показать диалог “Upgrade”, когда gate вернул deny.

### Customer Portal (Managing Payment Methods)
To allow users to update their credit card or view billing history:

#### Implementation Status (Done)
- **Server:** API `POST /api/subscription/portal` is active.
- **Client:** "Manage Subscription" menu item calls this API.

#### Manage Subscription Flow (Simplified)
```mermaid
sequenceDiagram
    participant User
    participant App
    participant Server
    participant Stripe

    User->>App: Click "Manage Subscription"
    App->>Server: Get Portal Link
    Server->>Stripe: Request Session
    Stripe-->>Server: Return https://billing.stripe.com/...
    Server-->>App: Return Link
    App->>User: Open Browser (Stripe Portal)
    
    Note over User, Stripe: User changes plan / cancels
    
    User->>Stripe: Click "Return to Nexy"
    Stripe->>App: Redirect back (Deep Link)
    App->>Server: Sync new status
```

## 8. AI Logic & Command Flow (User -> AI -> Action)

This diagram illustrates how the system processes natural language requests (e.g., "I want to change my card") into actionable links.

**The Logic:**
1.  **Context Injection:** The Server injects the user's subscription status into the LLM Prompt.
2.  **LLM Decision:** The AI decides which JSON command to output based on that status.
    *   **Paid User** -> `manage_subscription` (Portal)
    *   **Free User** -> `buy_subscription` (Checkout)
3.  **Client Execution:** The Client receives the JSON, dispatches an event, and opens the link returned by the server.

```mermaid
sequenceDiagram
    participant User
    participant LLM (Server)
    participant Client (ActionIntegration)
    participant Server (API)
    participant Browser

    User->>LLM: "I want to change my card"
    
    Note over LLM: **System Prompt Check:**
    Note over LLM: If Status == PAID:
    Note over LLM: Output `manage_subscription`
    
    LLM-->>Client: Stream Response + JSON
    Note right of LLM: { "command": "manage_subscription" }
    
    Client->>Client: Event: ui.action.manage_subscription
    
    Note over Client: PaymentIntegration handles event
    Client->>Server: POST /api/subscription/portal
    Server-->>Client: { "url": "https://billing.stripe.com/..." }
    
    Client->>Browser: Open URL
    Browser->>User: Show Generic Stripe Portal
```

## 9. Simplified Scheme: "How AI Knows You Paid"

This diagram shows exactly how the Server "whispers" your status to the AI before it answers.

```mermaid
graph TD
    User[👤 User] -->|1. Says: 'Change my card'| Client[📱 App]
    Client -->|2. Sends Audio + HardwareID| Server[🖥️ Server]
    
    subgraph Server Logic
        Server -->|3. Checks Database| DB[(🗄️ Database)]
        DB -->|4. Returns: 'Status = PAID'| Server
        
        Server -->|5. Creates Secret Note| Note[📝 System Prompt]
        Note -.->|"Hidden Text: User is PAID"| AI[🤖 Gemini AI]
        
        Server -->|6. Sends User Request| AI
    end
    
    subgraph AI Thinking
        AI -->|7. Reads Note + Request| Decision{🧠 Decision}
        Decision -->|'User is PAID'| PlanA[✅ Output: manage_subscription]
        Decision -.->|'User is FREE'| PlanB[❌ Output: buy_subscription]
    end
    
    PlanA -->|8. JSON Command| Client
    Client -->|9. Opens Portal| Stripe[💳 Stripe]
```
