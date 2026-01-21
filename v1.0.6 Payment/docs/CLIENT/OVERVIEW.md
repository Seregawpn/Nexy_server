# 📱 Клиентская часть платежной системы

**Feature ID:** F-2025-017-stripe-payment  
**Last Updated:** 2025-12-13

---

## 📋 Обзор

Клиентская часть обрабатывает deep links от Stripe, открывает URL в браузере и синхронизирует статус подписки.

---

## 🏗️ Архитектура компонентов

### 1. PaymentIntegration

**Файл:** `client(Messages)/integration/integrations/payment_integration.py` (NEW)

**Ответственность:**
- Обработка deep links `nexy://payment/*`
- Синхронизация статуса подписки
- Публикация событий в EventBus

**Ключевые методы:**
- `handle_payment_url(url)` — обработка deep link URL
- `_handle_payment_success(session_id)` — обработка успешной подписки
- `_handle_payment_cancel()` — обработка отмены
- `_handle_portal_return()` — обработка возврата из Portal
- `sync_subscription_after_return(hardware_id)` — синхронизация статуса

**Интеграция:**
- Регистрация в `SimpleModuleCoordinator`
- Подписка на события `deep_link.payment` и `app.url_opened`
- Публикация событий `payment.success`, `payment.cancel`, `payment.portal_return`

---

### 2. ActionExecutionIntegration

**Файл:** `client(Messages)/integration/integrations/action_execution_integration.py`

**Ответственность:**
- Выполнение команд от сервера (включая `open_url`)
- Обработка `action_message` из `StreamResponse`

**Обновления для Payment:**
- Добавить `open_url` в `valid_commands`
- Реализовать открытие URL через macOS `open` или Python `webbrowser`

**Ключевые методы:**
- `_on_action_received(event)` — обработка команды от сервера
- `_handle_open_url(args)` — открытие URL в браузере (NEW)

---

### 3. GrpcClientIntegration

**Файл:** `client(Messages)/integration/integrations/grpc_client_integration.py`

**Ответственность:**
- gRPC коммуникация с сервером
- Обработка `StreamResponse`
- Публикация `action_message` в EventBus

**Использование:**
- Получение `action_message` с командой `open_url`
- Передача в `ActionExecutionIntegration`

---

## 🔄 Основные flow

### 1. Обработка deep link

```
Stripe Checkout/Portal → Deep Link (nexy://payment/*)
  ↓
AppDelegate → PaymentIntegration.handle_payment_url()
  ↓
Парсинг URL (success/cancel/portal_return)
  ↓
gRPC запрос на синхронизацию (если нужно)
  ↓
Публикация события в EventBus
  ↓
Обновление UI/статуса
```

### 2. Открытие URL (checkout/portal)

```
Server → StreamResponse.action_message
  ↓
GrpcClientIntegration → EventBus (grpc.response.action)
  ↓
ActionExecutionIntegration._on_action_received()
  ↓
Парсинг: {"command": "open_url", "args": {"url": "..."}}
  ↓
subprocess.run(["open", url]) или webbrowser.open(url)
  ↓
Браузер открывается с URL
```

---

## 📚 Документация по направлениям

### Deep Links
**→ `DEEP_LINKS_PLAN.md`** или **`DEEP_LINKS.md`**

**Что включает:**
- Регистрация URL scheme в `Info.plist`
- Реализация `PaymentIntegration`
- Обработка success/cancel/portal_return URLs
- Синхронизация подписки

---

### Открытие URL
**→ `URL_OPENING.md`**

**Что включает:**
- Команда `open_url` от сервера
- Формат `action_json`: `{"command": "open_url", "args": {"url": "..."}}`
- Реализация через macOS `open` или Python `webbrowser`
- Обработка ошибок

**См. `COMPLETE_SYSTEM_LOGIC.md` раздел "Этап 7: Отправка URL на клиент"**

---

## 🔗 Связанные документы

- **`COMPLETE_SYSTEM_LOGIC.md`** — полная логика системы
- **`../ARCHITECTURE/OVERVIEW.md`** — обзор архитектуры
- **`DEEP_LINKS_PLAN.md`** — план обработки deep links
- **`COMPLETE_SYSTEM_LOGIC.md` раздел 24** — deep links на клиенте

---

**Следующий шаг:** Изучите `DEEP_LINKS_PLAN.md` для детального плана реализации

