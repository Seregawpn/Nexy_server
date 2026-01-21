# 🚀 Последовательный план реализации платежной системы по фазам

**Feature ID:** F-2025-017-stripe-payment  
**Date:** 2025-12-13  
**Status:** 📋 План готов к реализации

---

## 📋 Обзор

Этот документ описывает **последовательный план реализации** платежной системы, разбитый на четкие фазы с зависимостями, критериями готовности и тестированием на каждом этапе.

**Принцип:** Каждая фаза должна быть полностью завершена и протестирована перед переходом к следующей.

---

## 🎯 Структура фаз

```
Фаза 0: Подготовка и инфраструктура
  ↓
Фаза 1: База данных и репозитории
  ↓
Фаза 2: Stripe интеграция (базовая)
  ↓
Фаза 3: Subscription Module (сервер)
  ↓
Фаза 4: Webhook обработка
  ↓
Фаза 5: LLM интеграция и команды
  ↓
Фаза 6: Клиентская часть (Deep Links + URL Opening)
  ↓
Фаза 7: Интеграционное тестирование
  ↓
Фаза 8: Финализация и документация
```

---

## 📦 Фаза 0: Подготовка и инфраструктура

**Цель:** Подготовить окружение, конфигурацию и структуру директорий.

**Время:** 1-2 дня

### Задачи

#### 0.1. Структура директорий

**Создать директории:**

```bash
# Server
server(Payment)/server/
├── modules/subscription/
│   ├── __init__.py
│   ├── module.py
│   ├── quota_checker.py
│   ├── state_machine.py
│   └── adapter.py
├── services/
│   ├── __init__.py
│   ├── stripe_service.py
│   ├── stripe_webhook_handler.py
│   ├── subscription_cache.py
│   └── subscription_context_builder.py
├── database/
│   ├── __init__.py
│   ├── migrations/
│   │   ├── 001_create_subscriptions_tables.sql
│   │   ├── 002_add_subscription_indexes.sql
│   │   └── ROLLBACK_001.sql
│   ├── subscription_repository.py
│   ├── payment_repository.py
│   └── quota_repository.py
└── api/
    └── webhooks/
        ├── __init__.py
        └── stripe_webhook.py

# Client
client(Payment)/
├── modules/
│   └── deep_link/
│       ├── __init__.py
│       ├── core/
│       │   └── deep_link_processor.py
│       └── README.md
└── integration/
    └── integrations/
        └── deep_link_integration.py
```

#### 0.2. Конфигурация

**Файл:** `server(Payment)/server/config/unified_config.py`

**Добавить dataclass:**

- [ ] `StripeConfig` (из `CONFIGURATION_PLAN.md`)
- [ ] `QuotaConfig` (из `CONFIGURATION_PLAN.md`)
- [ ] `SubscriptionConfig` (из `CONFIGURATION_PLAN.md`)
- [ ] Обновить `FeaturesConfig` (добавить `enable_payment_system: bool = False`)

**Файл:** `server(Payment)/server/config/unified_config.yaml`

**Добавить секции:**

```yaml
features:
  enable_payment_system: false  # Feature flag

stripe:
  use_test_mode: true
  checkout_cooldown_hours: 24
  grace_period_days: 1
  trial_days: 14

quota:
  enabled: true
  daily_limit: 5
  weekly_limit: 25
  monthly_limit: 50

subscription:
  cache_ttl_seconds: 30
  auto_checkout_enabled: true
  trial_warnings_enabled: true
  trial_warning_days: [2, 1, 0]
```

#### 0.3. Зависимости

**Файл:** `server(Payment)/server/requirements.txt`

**Добавить:**

```txt
stripe>=7.0.0
redis>=5.0.0  # Опционально, для кэша
```

**Файл:** `client(Payment)/requirements.txt`

**Проверить наличие:**

- `subprocess` (встроенный)
- `webbrowser` (встроенный)

#### 0.4. Environment Variables

**Создать `.env.example`:**

```bash
# Stripe
STRIPE_API_KEY_TEST=sk_test_...
STRIPE_API_KEY_LIVE=sk_live_...
STRIPE_WEBHOOK_SECRET_TEST=whsec_...
STRIPE_WEBHOOK_SECRET_LIVE=whsec_...
STRIPE_USE_TEST_MODE=true
STRIPE_CHECKOUT_COOLDOWN_HOURS=24
STRIPE_GRACE_PERIOD_DAYS=1
STRIPE_TRIAL_DAYS=14

# Quota
QUOTA_ENABLED=true
QUOTA_DAILY_LIMIT=5
QUOTA_WEEKLY_LIMIT=25
QUOTA_MONTHLY_LIMIT=50

# Subscription
SUBSCRIPTION_CACHE_TTL_SECONDS=30
SUBSCRIPTION_AUTO_CHECKOUT_ENABLED=true
SUBSCRIPTION_TRIAL_WARNINGS_ENABLED=true
SUBSCRIPTION_TRIAL_WARNING_DAYS=2,1,0
```

### Критерии готовности

- [ ] Все директории созданы
- [ ] Конфигурация добавлена в `unified_config.py`
- [ ] `unified_config.yaml` обновлен
- [ ] Зависимости добавлены в `requirements.txt`
- [ ] `.env.example` создан
- [ ] Конфигурация загружается без ошибок

### Тестирование

```bash
# Проверка загрузки конфигурации
cd server(Payment)
python -c "from server.config.unified_config import load_config; print(load_config())"
```

---

## 🗄️ Фаза 1: База данных и репозитории

**Цель:** Создать миграции БД и репозитории для работы с данными.

**Время:** 2-3 дня

**Зависимости:** Фаза 0

### Задачи

#### 1.1. Миграции БД

**Файл:** `server(Payment)/server/database/migrations/001_create_subscriptions_tables.sql`

- [ ] Создать таблицу `subscriptions`
- [ ] Создать таблицу `subscription_events`
- [ ] Создать таблицу `payments`
- [ ] Создать таблицу `quota_usage`
- [ ] Добавить индексы
- [ ] Добавить constraints (UNIQUE для `stripe_event_id`)

**Файл:** `server(Payment)/server/database/migrations/002_add_subscription_indexes.sql`

- [ ] Индексы для `hardware_id`
- [ ] Индексы для `stripe_customer_id`
- [ ] Индексы для `stripe_subscription_id`
- [ ] Индексы для `status`
- [ ] Индексы для `quota_usage` (по датам)

**Файл:** `server(Payment)/server/database/migrations/ROLLBACK_001.sql`

- [ ] Rollback скрипт для удаления всех таблиц

#### 1.2. Репозитории

**Файл:** `server(Payment)/server/database/subscription_repository.py`

**Методы:**

- [ ] `get_subscription(hardware_id: str) -> Optional[Subscription]`
- [ ] `create_subscription(hardware_id: str, status: str) -> Subscription`
- [ ] `update_subscription(hardware_id: str, **kwargs) -> Subscription`
- [ ] `get_subscription_by_stripe_id(stripe_customer_id: str) -> Optional[Subscription]`
- [ ] `get_subscriptions_by_status(status: str) -> List[Subscription]`
- [ ] `update_status(hardware_id: str, status: str) -> Subscription`
- [ ] `update_payment_method_id(hardware_id: str, payment_method_id: str) -> Subscription`

**Файл:** `server(Payment)/server/database/payment_repository.py`

**Методы:**

- [ ] `create_payment(payment_data: dict) -> Payment`
- [ ] `get_payments_by_hardware_id(hardware_id: str) -> List[Payment]`
- [ ] `get_payment_by_stripe_id(stripe_payment_intent_id: str) -> Optional[Payment]`

**Файл:** `server(Payment)/server/database/quota_repository.py`

**Методы:**

- [ ] `increment_quota(hardware_id: str, date: date) -> QuotaUsage`
- [ ] `get_quota_usage(hardware_id: str, start_date: date, end_date: date) -> List[QuotaUsage]`
- [ ] `get_daily_usage(hardware_id: str, date: date) -> int`
- [ ] `get_weekly_usage(hardware_id: str, week_start: date) -> int`
- [ ] `get_monthly_usage(hardware_id: str, month_start: date) -> int`
- [ ] `reset_quota(hardware_id: str) -> None`

**Файл:** `server(Payment)/server/database/subscription_events_repository.py`

**Методы:**

- [ ] `create_event(stripe_event_id: str, event_type: str, hardware_id: str, event_data: dict) -> SubscriptionEvent`
- [ ] `get_event(stripe_event_id: str) -> Optional[SubscriptionEvent]`
- [ ] `event_exists(stripe_event_id: str) -> bool`

### Критерии готовности

- [ ] Миграции созданы и протестированы
- [ ] Все репозитории реализованы
- [ ] Unit тесты для репозиториев написаны и пройдены
- [ ] Rollback процедуры протестированы

### Тестирование

```bash
# Применить миграции
psql -d nexy_db -f server/database/migrations/001_create_subscriptions_tables.sql
psql -d nexy_db -f server/database/migrations/002_add_subscription_indexes.sql

# Запустить unit тесты
pytest server/database/tests/ -v

# Проверить rollback
psql -d nexy_db -f server/database/migrations/ROLLBACK_001.sql
```

---

## 💳 Фаза 2: Stripe интеграция (базовая)

**Цель:** Реализовать базовую интеграцию со Stripe API.

**Время:** 2-3 дня

**Зависимости:** Фаза 1

### Задачи

#### 2.1. Stripe Service

**Файл:** `server(Payment)/server/services/stripe_service.py`

**Класс:** `StripeService`

**Методы:**

- [ ] `__init__(config: StripeConfig)`
- [ ] `create_checkout_session(hardware_id: str, success_url: str, cancel_url: str) -> dict`
- [ ] `create_customer_portal_session(customer_id: str, return_url: str) -> dict`
- [ ] `get_customer(customer_id: str) -> dict`
- [ ] `get_subscription(subscription_id: str) -> dict`
- [ ] `cancel_subscription(subscription_id: str, immediately: bool = False) -> dict`
- [ ] `verify_webhook_signature(payload: bytes, signature: str) -> bool`
- [ ] `sync_payment_method(customer_id: str) -> dict`
- [ ] `get_payment_method_id(customer_id: str) -> Optional[str]`

#### 2.2. Webhook Handler (базовый)

**Файл:** `server(Payment)/server/services/stripe_webhook_handler.py`

**Класс:** `StripeWebhookHandler`

**Методы:**

- [ ] `__init__(stripe_service: StripeService, subscription_repo: SubscriptionRepository)`
- [ ] `handle_event(event: dict) -> dict`
- [ ] `_handle_checkout_session_completed(event: dict) -> None`
- [ ] `_handle_customer_subscription_updated(event: dict) -> None`
- [ ] `_handle_customer_subscription_deleted(event: dict) -> None`
- [ ] `_handle_invoice_payment_succeeded(event: dict) -> None`
- [ ] `_handle_invoice_payment_failed(event: dict) -> None`
- [ ] `_handle_invoice_payment_action_required(event: dict) -> None`

#### 2.3. Webhook Endpoint

**Файл:** `server(Payment)/server/api/webhooks/stripe_webhook.py`

**HTTP Endpoint:** `POST /webhook/stripe`

**Логика:**

- [ ] Верификация подписи Stripe
- [ ] Парсинг JSON payload
- [ ] Вызов `StripeWebhookHandler.handle_event()`
- [ ] Возврат `200 OK` или `400 Bad Request`

**Интеграция с HTTP сервером:**

- [ ] Добавить route в HTTP server (если используется Flask/FastAPI)
- [ ] Или добавить в существующий HTTP handler

### Критерии готовности

- [ ] `StripeService` реализован и протестирован
- [ ] `StripeWebhookHandler` обрабатывает все must-have события
- [ ] Webhook endpoint создан и доступен
- [ ] Верификация подписи работает
- [ ] Unit тесты написаны и пройдены

### Тестирование

```bash
# Unit тесты
pytest server/services/tests/test_stripe_service.py -v
pytest server/services/tests/test_stripe_webhook_handler.py -v

# Локальное тестирование с Stripe CLI
stripe listen --forward-to localhost:8000/webhook/stripe
stripe trigger checkout.session.completed
```

---

## 🧩 Фаза 3: Subscription Module (сервер)

**Цель:** Создать Subscription Module для сервера с интеграцией в ModuleCoordinator.

**Время:** 3-4 дня

**Зависимости:** Фаза 2

### Задачи

#### 3.1. Subscription State Machine

**Файл:** `server(Payment)/server/modules/subscription/state_machine.py`

**Класс:** `SubscriptionStateMachine`

**Методы:**

- [ ] `can_transition(from_status: str, to_status: str, event: str) -> bool`
- [ ] `transition(hardware_id: str, new_status: str, event: str, **kwargs) -> Subscription`
- [ ] `get_allowed_transitions(status: str) -> List[str]`
- [ ] `validate_transition(from_status: str, to_status: str) -> bool`

**Переходы (из `COMPLETE_SYSTEM_LOGIC.md`):**

- [ ] `paid_trial` → `paid` (при `invoice.payment_succeeded`)
- [ ] `paid_trial` → `limited_free_trial` (при истечении trial)
- [ ] `paid` → `billing_problem` (при `invoice.payment_failed`)
- [ ] `billing_problem` → `paid` (при `invoice.payment_succeeded`)
- [ ] `billing_problem` → `limited_free_trial` (при истечении grace period)
- [ ] `paid` → `limited_free_trial` (при `customer.subscription.deleted`)

#### 3.2. Quota Checker

**Файл:** `server(Payment)/server/modules/subscription/quota_checker.py`

**Класс:** `QuotaChecker`

**Методы:**

- [ ] `__init__(quota_repo: QuotaRepository, config: QuotaConfig)`
- [ ] `check_quota(hardware_id: str, subscription_status: str) -> QuotaResult`
- [ ] `increment_usage(hardware_id: str) -> None`
- [ ] `is_within_limits(hardware_id: str, status: str) -> bool`
- [ ] `get_remaining_quota(hardware_id: str, status: str) -> dict`

**Логика:**

- [ ] Для `paid_trial`, `paid`, `admin_active`, `grandfathered` → безлимитный доступ
- [ ] Для `billing_problem` → безлимитный доступ до истечения grace period
- [ ] Для `limited_free_trial` → проверка лимитов (5/день, 25/неделя, 50/месяц)

#### 3.3. Subscription Cache

**Файл:** `server(Payment)/server/services/subscription_cache.py`

**Класс:** `SubscriptionContextCache`

**Методы:**

- [ ] `__init__(subscription_repo: SubscriptionRepository, config: SubscriptionConfig)`
- [ ] `get_context(hardware_id: str) -> dict`
- [ ] `invalidate(hardware_id: str) -> None`
- [ ] `invalidate_all() -> None`

**Логика:**

- [ ] TTL 30 секунд
- [ ] Инвалидация при webhook/командах
- [ ] Форматирование контекста для LLM

**Файл:** `server(Payment)/server/services/subscription_context_builder.py`

**Класс:** `SubscriptionContextBuilder`

**Методы:**

- [ ] `build_context(subscription: Subscription, quota_info: dict) -> str`
- [ ] `format_for_llm(subscription: Subscription) -> str`

#### 3.4. Trial Period Manager

**Файл:** `server(Payment)/server/modules/subscription/trial_manager.py`

**Класс:** `TrialPeriodManager`

**Методы:**

- [ ] `__init__(subscription_repo: SubscriptionRepository, config: SubscriptionConfig)`
- [ ] `check_trial_expiration(subscription: Subscription) -> dict`
  - Проверка дней до истечения trial
  - Возврат информации о статусе trial
- [ ] `should_show_warning(subscription: Subscription) -> bool`
  - Проверка, нужно ли показывать предупреждение (2, 1, 0 дней)
- [ ] `should_auto_checkout(subscription: Subscription) -> bool`
  - Проверка, можно ли создать auto-checkout (cooldown 24 часа)
- [ ] `get_warning_message(subscription: Subscription) -> str`
  - Генерация сообщения предупреждения для LLM

**Логика:**

- [ ] Проверка дней до истечения trial (14 дней)
- [ ] Генерация предупреждений за 2, 1, 0 дней до истечения
- [ ] Проверка cooldown для auto-checkout (24 часа между созданиями)
- [ ] Интеграция с SubscriptionContextCache для включения в контекст

#### 3.5. Reconcile Service

**Файл:** `server(Payment)/server/services/reconcile_service.py`

**Класс:** `ReconcileService`

**Методы:**

- [ ] `__init__(stripe_service: StripeService, subscription_repo: SubscriptionRepository, state_machine: SubscriptionStateMachine)`
- [ ] `reconcile_with_stripe(hardware_id: str, subscription: Subscription) -> bool`
  - Проверка расхождений между БД и Stripe
  - Обновление БД из Stripe (Stripe - источник истины)
  - Инвалидация кэша после реконсиляции
- [ ] `check_reconciliation_needed(subscription: Subscription) -> bool`
  - Проверка, нужна ли реконсиляция (подозрительные состояния)
- [ ] `reconcile_all_active_subscriptions() -> int`
  - Batch реконсиляция всех активных подписок (для cron)

**Логика:**

- [ ] Реконсиляция при первом запросе после истечения кэша (если подозрительное состояние)
- [ ] Реконсиляция при подозрительных состояниях:
  - Статус в БД `paid`, но нет `stripe_subscription_id`
  - Статус в БД `limited_free_trial`, но есть активный `stripe_subscription_id`
  - Статус `billing_problem` и `grace_period_end_at` прошел
  - Статус `paid` но `current_period_end` прошел
- [ ] Stripe всегда побеждает при расхождении

#### 3.6. Subscription Module

**Файл:** `server(Payment)/server/modules/subscription/module.py`

**Класс:** `SubscriptionModule` (реализует `UniversalModuleInterface`)

**Методы:**

- [ ] `initialize(config: dict) -> None`
- [ ] `process(request: dict) -> dict`
- [ ] `cleanup() -> None`
- [ ] `get_status() -> dict`

**Capabilities:**

- [ ] `subscription_context` — получение контекста для LLM
- [ ] `quota_check` — проверка квот
- [ ] `create_checkout` — создание Checkout Session
- [ ] `open_portal` — открытие Customer Portal
- [ ] `cancel_subscription` — отмена подписки

#### 3.5. Module Adapter

**Файл:** `server(Payment)/server/modules/subscription/adapter.py`

**Класс:** `SubscriptionModuleAdapter`

**Логика:**

- [ ] Адаптер для `SubscriptionModule` под `UniversalModuleInterface`
- [ ] Интеграция с `ModuleFactory`

#### 3.6. Интеграция в ModuleCoordinator

**Файл:** `server(Payment)/server/integrations/core/module_factory.py`

**Обновить:**

- [ ] Добавить `SubscriptionModule` в `ModuleFactory.create_module()`
- [ ] Зарегистрировать capability `subscription`

### Критерии готовности

- [ ] State Machine реализован и протестирован
- [ ] Quota Checker реализован и протестирован
- [ ] Subscription Cache реализован и протестирован
- [ ] Trial Period Manager реализован и протестирован
- [ ] Reconcile Service реализован и протестирован
- [ ] Subscription Module создан и зарегистрирован
- [ ] Module интегрирован в `ModuleCoordinator`
- [ ] Unit тесты написаны и пройдены

### Тестирование

```bash
# Unit тесты
pytest server/modules/subscription/tests/ -v

# Интеграционные тесты
pytest server/tests/integration/test_subscription_module.py -v
```

---

## 🔔 Фаза 4: Webhook обработка (полная)

**Цель:** Реализовать полную обработку всех webhook событий с State Machine.

**Время:** 2-3 дня

**Зависимости:** Фаза 3

### Задачи

#### 4.1. Расширение Webhook Handler

**Файл:** `server(Payment)/server/services/stripe_webhook_handler.py`

**Обновить:**

- [ ] Интеграция с `SubscriptionStateMachine`
- [ ] Интеграция с `SubscriptionContextCache` (инвалидация)
- [ ] Обработка всех must-have событий:
  - [ ] `checkout.session.completed` → линковка customer/subscription
  - [ ] `customer.subscription.updated` → обновление статуса (включая `incomplete`, `past_due`, `unpaid`, `canceled`)
  - [ ] `customer.subscription.deleted` → переход в `limited_free_trial`
  - [ ] `invoice.payment_succeeded` → переход в `paid` (источник истины)
  - [ ] `invoice.payment_failed` → переход в `billing_problem` + установка grace period
  - [ ] `invoice.payment_action_required` → уведомление пользователя

#### 4.2. Идемпотентность

**Логика:**

- [ ] Проверка `subscription_events` перед обработкой
- [ ] Игнорирование дубликатов (UNIQUE constraint)
- [ ] Логирование пропущенных событий

#### 4.3. Out-of-order обработка

**Логика:**

- [ ] Обработка событий в любом порядке
- [ ] Reconcile логика для синхронизации состояния

#### 4.4. Grace Period обработка

**Логика:**

- [ ] Установка `grace_period_end_at` при `invoice.payment_failed`
- [ ] Проверка истечения grace period (cron job или при каждом запросе)
- [ ] Переход в `limited_free_trial` при истечении

### Критерии готовности

- [ ] Все must-have события обрабатываются
- [ ] State Machine переходы работают корректно
- [ ] Идемпотентность реализована
- [ ] Out-of-order обработка работает
- [ ] Grace period логика реализована (проверка при каждом запросе)
- [ ] Reconcile интеграция работает
- [ ] Кэш инвалидируется при каждом webhook
- [ ] Интеграционные тесты написаны и пройдены

### Тестирование

```bash
# Тесты webhook обработки
pytest server/services/tests/test_stripe_webhook_handler.py -v

# Тесты State Machine
pytest server/modules/subscription/tests/test_state_machine.py -v

# E2E тесты с Stripe CLI
stripe listen --forward-to localhost:8000/webhook/stripe
stripe trigger invoice.payment_succeeded
stripe trigger invoice.payment_failed
stripe trigger customer.subscription.updated
```

---

## 🤖 Фаза 5: LLM интеграция и команды

**Цель:** Интегрировать subscription команды в LLM workflow.

**Время:** 3-4 дня

**Зависимости:** Фаза 4

### Задачи

#### 5.1. Обновление AssistantResponseParser

**Файл:** `server(Payment)/server/integrations/core/assistant_response_parser.py`

**Обновить:**

- [ ] Добавить парсинг команд:
  - [ ] `create_subscription` → `{"command": "create_subscription", "args": {}}`
  - [ ] `cancel_subscription` → `{"command": "cancel_subscription", "args": {}}`
  - [ ] `update_payment_method` → `{"command": "update_payment_method", "args": {}}`
- [ ] Валидация команд (бизнес-логика)
- [ ] Rate limiting для команд (cooldown)

#### 5.2. Обновление System Prompt

**Файл:** `server(Payment)/server/modules/text_processing/providers/gemini_live_provider.py`

**Обновить:**

- [ ] Добавить subscription context в system prompt
- [ ] Инструкции для LLM по объяснению подписки
- [ ] Trial warnings (2 дня, 1 день, 0 дней)
- [ ] Формат ответов для subscription команд

**Логика:**

- [ ] Subscription context добавляется к каждому запросу через `SubscriptionContextCache`
- [ ] LLM получает информацию о статусе подписки, квотах, trial end date

#### 5.3. Интеграция в StreamingWorkflowIntegration

**Файл:** `server(Payment)/server/integrations/workflow_integrations/streaming_workflow_integration.py`

**Обновить:**

- [ ] Добавить получение subscription context перед LLM запросом
- [ ] Добавить проверку квот перед обработкой запроса
- [ ] Добавить обработку subscription команд:
  - [ ] `create_subscription` → вызов `SubscriptionModule.create_checkout()`
  - [ ] `cancel_subscription` → вызов `SubscriptionModule.cancel_subscription()`
  - [ ] `update_payment_method` → вызов `SubscriptionModule.open_portal()`
- [ ] Генерация URL для `open_url` команды (checkout_url, portal_url)
- [ ] Отправка `action_message` с `open_url` командой на клиент

**Логика:**

```python
# Псевдокод
def _process_request_streaming(self, request):
    # 1. Получить subscription context
    subscription_context = self.subscription_module.get_context(hardware_id)
    
    # 2. Проверить квоты
    quota_result = self.subscription_module.check_quota(hardware_id)
    if not quota_result.allowed:
        # Вернуть сообщение о превышении квот
        yield self._generate_quota_exceeded_message(quota_result)
        return
    
    # 3. Добавить context в LLM prompt
    enhanced_prompt = self._add_subscription_context(prompt, subscription_context)
    
    # 4. Обработать LLM ответ
    llm_response = self.text_processor.process(enhanced_prompt)
    
    # 5. Парсить команды
    commands = self.assistant_parser.parse(llm_response)
    
    # 6. Выполнить subscription команды
    for command in commands:
        if command['command'] == 'create_subscription':
            result = self.subscription_module.create_checkout(hardware_id)
            if result.get('checkout_url'):
                yield {
                    'action_message': {
                        'action_json': json.dumps({
                            'command': 'open_url',
                            'args': {'url': result['checkout_url']}
                        }),
                        'session_id': session_id,
                        'feature_id': 'F-2025-017-stripe-payment'
                    }
                }
        # ... другие команды
```

#### 5.4. Hardware ID обработка

**Файл:** `server(Payment)/server/integrations/workflow_integrations/streaming_workflow_integration.py`

**Обновить:**

- [ ] Проверка наличия `hardware_id` в StreamRequest
- [ ] Генерация `hardware_id` на сервере, если отсутствует
  - Использовать UUID4 для генерации
  - Логировать генерацию для отслеживания
- [ ] Сохранение сгенерированного `hardware_id` для последующих запросов
  - (Опционально) Сохранение в сессии или возврат клиенту для сохранения
- [ ] Логирование генерации для отслеживания

**Логика:**

```python
# Псевдокод
def _get_hardware_id(self, request: StreamRequest) -> str:
    """Получение или генерация hardware_id"""
    if request.hardware_id:
        return request.hardware_id
    
    # Генерация на сервере для старых клиентов
    import uuid
    generated_id = str(uuid.uuid4())
    logger.info(f"[HARDWARE_ID] Generated hardware_id for client: {generated_id[:8]}...")
    return generated_id
```

#### 5.5. Portal Return обработка

**Файл:** `server(Payment)/server/integrations/workflow_integrations/streaming_workflow_integration.py`

**Обновить:**

- [ ] Проверка флага `portal_return` в StreamRequest (или специального поля)
- [ ] Вызов синхронизации payment_method из Stripe:
  - Использовать `StripeService.sync_payment_method(customer_id)`
  - Получить актуальный `payment_method_id`
- [ ] Обновление БД:
  - Вызвать `SubscriptionRepository.update_payment_method_id()`
  - Обновить `last_portal_return_at` timestamp
- [ ] Инвалидация кэша подписки
- [ ] Генерация ответа для пользователя (через LLM)

**Логика:**

```python
# Псевдокод
def _handle_portal_return(self, request: StreamRequest, hardware_id: str):
    """Обработка возврата из Portal"""
    subscription = self.subscription_repo.get_subscription(hardware_id)
    if not subscription or not subscription.stripe_customer_id:
        return
    
    # Синхронизация payment_method из Stripe
    payment_method_data = self.stripe_service.sync_payment_method(
        subscription.stripe_customer_id
    )
    
    # Обновление БД
    self.subscription_repo.update_payment_method_id(
        hardware_id,
        payment_method_data['payment_method_id']
    )
    
    # Инвалидация кэша
    self.subscription_cache.invalidate(hardware_id)
    
    # Генерация ответа через LLM
    return self._generate_portal_return_message()
```

#### 5.6. Quota Enforcement

**Логика:**

- [ ] Проверка квот перед каждым запросом
- [ ] Инкремент usage после успешного запроса
- [ ] Блокировка запросов при превышении лимитов

### Критерии готовности

- [ ] `AssistantResponseParser` парсит subscription команды
- [ ] System prompt обновлен с subscription context
- [ ] `StreamingWorkflowIntegration` интегрирован с Subscription Module
- [ ] Hardware ID обработка работает (генерация на сервере)
- [ ] Portal Return обработка работает
- [ ] Quota enforcement работает
- [ ] URL генерация и отправка на клиент работает
- [ ] Интеграционные тесты написаны и пройдены

### Тестирование

```bash
# Тесты парсинга
pytest server/integrations/core/tests/test_assistant_response_parser.py -v

# Тесты LLM интеграции
pytest server/integrations/workflow_integrations/tests/test_streaming_workflow_integration.py -v

# E2E тесты с реальным LLM
pytest server/tests/e2e/test_subscription_commands.py -v
```

---

## 📱 Фаза 6: Клиентская часть (Deep Links + URL Opening)

**Цель:** Реализовать обработку deep links и открытие URL на клиенте.

**Время:** 2-3 дня

**Зависимости:** Фаза 5

### Задачи

#### 6.1. Deep Link Processor

**Файл:** `client(Payment)/modules/deep_link/core/deep_link_processor.py`

**Класс:** `DeepLinkProcessor`

**Методы:**

- [ ] `__init__()`
- [ ] `process_deep_link(url: str) -> DeepLinkResult`
- [ ] `parse_url(url: str) -> dict`
- [ ] `handle_checkout_success(session_id: str) -> None`
- [ ] `handle_checkout_cancel() -> None`
- [ ] `handle_portal_return() -> None`

**Поддерживаемые URL:**

- [ ] `nexy://checkout/success?session_id=xxx`
- [ ] `nexy://checkout/cancel`
- [ ] `nexy://portal/return`

#### 6.2. Deep Link Integration

**Файл:** `client(Payment)/integration/integrations/deep_link_integration.py`

**Класс:** `DeepLinkIntegration`

**Логика:**

- [ ] Подписка на события `deep_link.received`
- [ ] Обработка deep links через `DeepLinkProcessor`
- [ ] Публикация событий `deep_link.processed`
- [ ] Интеграция с `SimpleModuleCoordinator`

#### 6.3. URL Opening (open_url команда)

**Файл:** `client(Payment)/integration/integrations/action_execution_integration.py`

**Обновить:**

- [ ] Добавить `open_url` в `valid_commands`
- [ ] Реализовать обработку `open_url` команды:

```python
def _handle_open_url(self, command_data: dict):
    """Обработка open_url команды"""
    url = command_data.get('args', {}).get('url')
    if not url:
        logger.error("open_url: URL not provided")
        return
    
    # Открыть URL в браузере
    import subprocess
    subprocess.run(["open", url])  # macOS
    
    # Или использовать webbrowser
    # import webbrowser
    # webbrowser.open(url)
    
    logger.info(f"open_url: Opened URL {url}")
```

#### 6.4. Регистрация в SimpleModuleCoordinator

**Файл:** `client(Payment)/integration/core/simple_module_coordinator.py`

**Обновить:**

- [ ] Добавить `DeepLinkIntegration` в список интеграций
- [ ] Установить правильный порядок инициализации

### Критерии готовности

- [ ] `DeepLinkProcessor` реализован и протестирован
- [ ] `DeepLinkIntegration` создана и зарегистрирована
- [ ] `open_url` команда обрабатывается в `ActionExecutionIntegration`
- [ ] Deep links обрабатываются корректно
- [ ] URL открываются в браузере
- [ ] Unit тесты написаны и пройдены

### Тестирование

```bash
# Unit тесты
pytest modules/deep_link/tests/ -v
pytest integration/integrations/tests/test_deep_link_integration.py -v

# Интеграционные тесты
pytest tests/integration/test_deep_links.py -v

# Ручное тестирование
# Открыть URL: nexy://checkout/success?session_id=test123
```

---

## 🧪 Фаза 7: Интеграционное тестирование

**Цель:** Полное E2E тестирование всей системы.

**Время:** 3-4 дня

**Зависимости:** Фаза 6

### Задачи

#### 7.1. E2E тесты

**Файл:** `server(Payment)/server/tests/e2e/test_subscription_full_flow.py`

**Сценарии:**

- [ ] Новый пользователь → paid_trial → оплата → paid
- [ ] Trial истечение → limited_free_trial
- [ ] Payment failed → billing_problem → grace period → limited_free_trial
- [ ] Payment succeeded → возврат в paid
- [ ] Quota enforcement для limited_free_trial
- [ ] Webhook обработка всех событий
- [ ] Deep links обработка
- [ ] URL opening на клиенте

#### 7.2. Критические тест-кейсы

**Файл:** `v1.0.6 Payment/tests/test_smoke_critical.py`

**Обновить:**

- [ ] Интегрировать с реальным кодом
- [ ] Все 15 критических тест-кейсов должны пройти

#### 7.3. Performance тесты

**Тесты:**

- [ ] Webhook обработка latency < 500ms
- [ ] Quota check latency < 50ms (cached)
- [ ] Subscription context получение < 100ms (cached)

#### 7.4. Failure simulation

**Сценарии:**

- [ ] Stripe API недоступен → fallback
- [ ] БД недоступна → fallback
- [ ] Webhook дубликаты → идемпотентность
- [ ] Race conditions в квотах → atomic операции

### Критерии готовности

- [ ] Все E2E тесты пройдены
- [ ] Все критические тест-кейсы пройдены
- [ ] Performance требования выполнены
- [ ] Failure scenarios протестированы
- [ ] Нет регрессий в существующем функционале

### Тестирование

```bash
# E2E тесты
pytest server/tests/e2e/ -v
pytest client/tests/e2e/ -v

# Критические тесты
pytest v1.0.6\ Payment/tests/test_smoke_critical.py -v

# Performance тесты
pytest server/tests/performance/ -v
```

---

## 📝 Фаза 8: Финализация и документация

**Цель:** Завершить реализацию, обновить документацию, подготовить к релизу.

**Время:** 2-3 дня

**Зависимости:** Фаза 7

### Задачи

#### 8.1. Код ревью

- [ ] Проверить соответствие архитектуре
- [ ] Проверить отсутствие дублирования
- [ ] Проверить обработку ошибок
- [ ] Проверить логирование и observability

#### 8.2. Cron Jobs

**Файл:** `server(Payment)/server/services/cron_jobs.py` (или использовать существующую систему cron)

**Задачи:**

- [ ] **Периодическая синхронизация со Stripe (раз в час)**
  - Вызов `ReconcileService.reconcile_all_active_subscriptions()`
  - Для всех подписок с `status='paid'` или `status='billing_problem'`
  - Логирование результатов синхронизации

- [ ] **Проверка истечения grace period (раз в час)**
  - Поиск подписок с `status='billing_problem'` и истекшим `grace_period_end_at`
  - Автоматический переход в `limited_free_trial`
  - Логирование переходов

- [ ] **Проверка истечения trial period (раз в день)**
  - Поиск подписок с `status='paid_trial'` и истекшим `paid_trial_end_at`
  - Автоматический переход в `limited_free_trial`
  - (Опционально) Создание auto-checkout (если cooldown прошел)

**Реализация:**

```python
# Псевдокод
def cron_reconcile_subscriptions():
    """Cron job для периодической синхронизации"""
    reconcile_service = ReconcileService(...)
    count = reconcile_service.reconcile_all_active_subscriptions()
    logger.info(f"[CRON] Reconciled {count} subscriptions")

def cron_check_grace_period():
    """Cron job для проверки grace period"""
    subscriptions = subscription_repo.get_subscriptions_by_status('billing_problem')
    for sub in subscriptions:
        if sub.grace_period_end_at and sub.grace_period_end_at < now():
            state_machine.transition(sub.hardware_id, 'limited_free_trial', 'grace_period_expired')

def cron_check_trial_expiration():
    """Cron job для проверки trial expiration"""
    subscriptions = subscription_repo.get_subscriptions_by_status('paid_trial')
    for sub in subscriptions:
        if sub.paid_trial_end_at and sub.paid_trial_end_at < now():
            state_machine.transition(sub.hardware_id, 'limited_free_trial', 'trial_expired')
```

**Интеграция:**

- [ ] Использовать существующую систему cron (если есть)
- [ ] Или создать отдельный cron service
- [ ] Настроить расписание (hourly/daily)

#### 8.3. Документация

**Обновить:**

- [ ] `README.md` в `server(Payment)/server/modules/subscription/`
- [ ] `README.md` в `client(Payment)/modules/deep_link/`
- [ ] API документация для webhook endpoint
- [ ] Инструкции по настройке Stripe
- [ ] Документация по cron jobs

#### 8.4. Feature Flag

**Проверить:**

- [ ] Feature flag `enable_payment_system` работает
- [ ] Kill-switch работает
- [ ] Rollback процедуры готовы

#### 8.5. Мониторинг

**Настроить:**

- [ ] Метрики для subscription команд
- [ ] Метрики для webhook обработки
- [ ] Метрики для quota enforcement
- [ ] Метрики для реконсиляции (количество, успешность)
- [ ] Метрики для cron jobs (выполнение, результаты)
- [ ] Алерты для критических ошибок

#### 8.6. Release Notes

**Создать:**

- [ ] Release notes для v1.0.6
- [ ] Changelog
- [ ] Migration guide

### Критерии готовности

- [ ] Код ревью пройден
- [ ] Документация обновлена
- [ ] Cron jobs настроены и протестированы
- [ ] Feature flag протестирован
- [ ] Мониторинг настроен
- [ ] Release notes готовы
- [ ] Готово к production deployment

---

## 📊 Итоговая таблица фаз

| Фаза | Название | Время | Зависимости | Статус |
|------|----------|-------|-------------|--------|
| 0 | Подготовка и инфраструктура | 1-2 дня | - | ⬜ |
| 1 | База данных и репозитории | 2-3 дня | Фаза 0 | ⬜ |
| 2 | Stripe интеграция (базовая) | 2-3 дня | Фаза 1 | ⬜ |
| 3 | Subscription Module (сервер) | 3-4 дня | Фаза 2 | ⬜ |
| 4 | Webhook обработка | 2-3 дня | Фаза 3 | ⬜ |
| 5 | LLM интеграция и команды | 3-4 дня | Фаза 4 | ⬜ |
| 6 | Клиентская часть | 2-3 дня | Фаза 5 | ⬜ |
| 7 | Интеграционное тестирование | 3-4 дня | Фаза 6 | ⬜ |
| 8 | Финализация и документация | 2-3 дня | Фаза 7 | ⬜ |

**Общее время:** 20-29 дней (4-6 недель)

---

## 🎯 Критерии успеха

### Технические

- [ ] Все фазы завершены
- [ ] Все тесты пройдены
- [ ] Нет регрессий
- [ ] Performance требования выполнены
- [ ] Мониторинг настроен

### Функциональные

- [ ] Trial период работает
- [ ] Оплата работает
- [ ] Webhooks обрабатываются
- [ ] Quota enforcement работает
- [ ] Deep links работают
- [ ] URL opening работает

### Бизнес

- [ ] Feature flag позволяет постепенный rollout
- [ ] Kill-switch позволяет экстренное отключение
- [ ] Rollback процедуры готовы
- [ ] Документация для поддержки готова

---

## 📚 Связанные документы

- `COMPLETE_SYSTEM_LOGIC.md` — полная логика системы
- `F-2025-017-stripe-payment-spec.md` — формальная спецификация
- `DATABASE_MIGRATIONS.md` — миграции БД
- `CONFIGURATION_PLAN.md` — конфигурация
- `ERROR_HANDLING_PLAN.md` — обработка ошибок
- `DEEP_LINKS_PLAN.md` — deep links
- `CRITICAL_TEST_CASES.md` — критические тест-кейсы

---

**Последнее обновление:** 2025-12-13  
**Версия:** 1.1 (обновлено с учетом анализа последовательности)

---

## 📝 История изменений

### Версия 1.1 (2025-12-13)
- ✅ Добавлен **Payment Method синхронизация** (Фаза 2)
- ✅ Добавлен **Trial Period Manager** (Фаза 3)
- ✅ Добавлен **Reconcile Service** (Фаза 3)
- ✅ Уточнена **Grace Period обработка** (Фаза 4)
- ✅ Добавлена **Reconcile Integration** (Фаза 4)
- ✅ Добавлена **Hardware ID обработка** (Фаза 5)
- ✅ Добавлена **Portal Return обработка** (Фаза 5)
- ✅ Добавлены **Cron Jobs** (Фаза 8)

**Все выявленные пропуски устранены.**

