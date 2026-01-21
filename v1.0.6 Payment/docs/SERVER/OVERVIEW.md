# 🖥️ Серверная часть платежной системы

**Feature ID:** F-2025-017-stripe-payment  
**Last Updated:** 2025-12-13

---

## 📋 Обзор

Серверная часть обрабатывает все запросы пользователей, интегрируется со Stripe, управляет подписками и генерирует ответы через LLM.

---

## 🏗️ Архитектура компонентов

### 1. StreamingWorkflowIntegration

**Файл:** `server(Messages)/server/integrations/workflow_integrations/streaming_workflow_integration.py`

**Ответственность:**
- Обработка gRPC запросов
- Получение контекста подписки
- Формирование prompts для LLM
- Парсинг ответов LLM
- Выполнение команд подписки
- Генерация TTS

**Ключевые методы:**
- `process_request_streaming()` — основной метод обработки
- `_execute_subscription_command()` — выполнение команд
- `_get_subscription_context()` — получение контекста

---

### 2. SubscriptionContextCache

**Файл:** `server(Messages)/server/modules/subscription/subscription_context_cache.py` (NEW)

**Ответственность:**
- Кэширование контекста подписки (TTL 30 секунд)
- Получение данных из БД
- Создание пробного периода для новых пользователей
- Форматирование контекста в JSON

**Ключевые методы:**
- `get_context(hardware_id)` — получение контекста
- `invalidate(hardware_id)` — инвалидация кэша
- `_format_context()` — форматирование в JSON

---

### 3. StripeService

**Файл:** `server(Messages)/server/modules/stripe/stripe_service.py` (NEW)

**Ответственность:**
- Создание Checkout Sessions
- Создание Customer Portal Sessions
- Обработка Stripe API ошибок
- Retry механизмы

**Ключевые методы:**
- `create_checkout_session(hardware_id)` — создание checkout
- `create_portal_session(hardware_id)` — создание portal
- `retrieve_subscription(subscription_id)` — получение подписки

---

### 4. SubscriptionStateMachine

**Файл:** `server(Messages)/server/modules/subscription/subscription_state_machine.py` (NEW)

**Ответственность:**
- Управление переходами статусов
- Валидация переходов
- Применение правил state machine

**Ключевые методы:**
- `can_transition(from_status, to_status, event)` — проверка возможности перехода
- `transition(hardware_id, new_status, event)` — выполнение перехода

---

### 5. QuotaChecker

**Файл:** `server(Messages)/server/modules/subscription/quota_checker.py` (NEW)

**Ответственность:**
- Проверка квот для `limited_free_trial`
- Atomic операции для предотвращения race conditions
- Инкремент счетчиков

**Ключевые методы:**
- `check_and_increment(hardware_id)` — проверка и инкремент
- `get_usage(hardware_id)` — получение текущего использования

---

### 6. StripeWebhookHandler

**Файл:** `server(Messages)/server/services/stripe_webhook_handler.py` (NEW)

**Ответственность:**
- Верификация webhook signatures
- Идемпотентная обработка событий
- Обновление БД
- Инвалидация кэша

**Ключевые методы:**
- `handle_webhook(payload, signature)` — обработка webhook
- `_process_event(event)` — обработка конкретного события
- `_is_duplicate_event(event_id)` — проверка дубликатов

---

## 📚 Документация по направлениям

### Конфигурация
**→ `CONFIGURATION_PLAN.md`** или **`CONFIGURATION.md`**

**Что включает:**
- `StripeConfig` — API keys, webhook secrets
- `QuotaConfig` — лимиты (5/25/50)
- `SubscriptionConfig` — cache TTL, auto checkout
- Feature flags и kill switches

---

### База данных
**→ `DATABASE_MIGRATIONS.md`** или **`DATABASE.md`**

**Что включает:**
- SQL миграции для всех таблиц
- Индексы для производительности
- Rollback процедуры
- Структура таблиц

---

### Интеграция со Stripe
**→ `STRIPE_DATA_PARSING.md`** или **`STRIPE_INTEGRATION.md`**

**Что включает:**
- Верификация webhook signatures
- Парсинг всех типов событий
- API calls (Checkout, Portal, Subscription)
- Обработка ошибок Stripe API

---

### Интеграция с LLM (Gemini)
**→ `LLM_INTEGRATION.md`**

**Что включает:**
- System prompt для subscription management
- Формирование контекста подписки
- Генерация команд через LLM
- Обработка ответов

**См. `COMPLETE_SYSTEM_LOGIC.md` раздел "🤖 LLM Промпты"**

---

### Парсинг ответов LLM
**→ `LLM_JSON_PARSING_FIXES.md`** или **`PARSING.md`**

**Что включает:**
- Канонический формат: `{"command": "...", "args": {}, "text": "..."}`
- Balanced braces extraction
- Валидация схемы
- Guardrails (лимиты размера)

**См. `COMPLETE_SYSTEM_LOGIC.md` раздел "Этап 4: Парсинг JSON ответа от LLM"**

---

### Обработка ошибок
**→ `ERROR_HANDLING_PLAN.md`** или **`ERROR_HANDLING.md`**

**Что включает:**
- Все типы Stripe ошибок (Rate Limit, Invalid Request, Connection, Authentication)
- Все типы БД ошибок (Connection, Transaction, Constraint)
- Cache ошибки
- Webhook ошибки
- Quota race conditions

**См. `COMPLETE_SYSTEM_LOGIC.md` раздел 21**

---

## 🔄 Основные flow

### 1. Обработка запроса пользователя

```
StreamRequest → StreamingWorkflowIntegration
  ↓
SubscriptionContextCache.get_context()
  ↓
Формирование prompt для LLM (с контекстом)
  ↓
Gemini API → ответ (JSON команда или текст)
  ↓
AssistantResponseParser → парсинг
  ↓
_execute_subscription_command() → выполнение
  ↓
Отправка URL на клиент (если нужно)
  ↓
TTS генерация → StreamResponse
```

### 2. Обработка webhook

```
Stripe Webhook → StripeWebhookHandler
  ↓
Верификация signature
  ↓
Проверка дубликатов (subscription_events)
  ↓
Парсинг события
  ↓
SubscriptionStateMachine.transition()
  ↓
Обновление БД
  ↓
Инвалидация кэша
```

---

## 🔗 Связанные документы

- **`COMPLETE_SYSTEM_LOGIC.md`** — полная логика системы
- **`../ARCHITECTURE/OVERVIEW.md`** — обзор архитектуры
- **`CONFIGURATION_PLAN.md`** — конфигурация
- **`DATABASE_MIGRATIONS.md`** — миграции БД
- **`STRIPE_DATA_PARSING.md`** — интеграция со Stripe
- **`LLM_JSON_PARSING_FIXES.md`** — парсинг LLM
- **`ERROR_HANDLING_PLAN.md`** — обработка ошибок

---

**Следующий шаг:** Изучите конкретные направления (Configuration, Database, Stripe Integration, etc.)

