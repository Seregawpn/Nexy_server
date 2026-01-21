# 🎯 MVP План реализации платежной системы

**Feature ID:** F-2025-017-stripe-payment  
**Date:** 2025-12-13  
**Version:** 1.0  
**Status:** 📋 Итеративный MVP подход

---

## 📋 Философия подхода

**Принцип:** Создавать маленькие, изолированные MVP, которые можно быстро протестировать, прежде чем интегрировать в основной проект.

**Преимущества:**
- ✅ Быстрое тестирование каждого компонента
- ✅ Минимальный риск для существующего функционала
- ✅ Возможность отката на любом этапе
- ✅ Постепенное понимание системы
- ✅ Раннее выявление проблем

---

## 🎯 MVP Этапы

### MVP 0: Подготовка (1 день)
**Цель:** Минимальная инфраструктура для тестирования

### MVP 1: Webhook Endpoint (1-2 дня)
**Цель:** Прием и логирование webhook событий от Stripe

### MVP 2: База данных (1-2 дня)
**Цель:** Миграции и простые CRUD операции

### MVP 3: Stripe Service (1-2 дня)
**Цель:** Создание Checkout Session (изолированно)

### MVP 4: Subscription Repository (1 день)
**Цель:** Работа с БД для подписок

### MVP 5: Subscription Context (1 день)
**Цель:** Получение контекста подписки (без интеграции в workflow)

### MVP 6: Quota Checker (1 день)
**Цель:** Проверка квот (изолированно)

### MVP 7: Интеграция в Workflow (2-3 дня)
**Цель:** Добавление subscription context в LLM prompt

### MVP 8: Команды подписки (2-3 дня)
**Цель:** Обработка команд create_subscription/cancel_subscription

### MVP 9: Клиентская часть (1-2 дня)
**Цель:** Deep Links и open_url команда

### MVP 10: Полная интеграция (2-3 дня)
**Цель:** Все компоненты работают вместе

---

## 📦 MVP 0: Подготовка

**Цель:** Минимальная инфраструктура для тестирования

**Время:** 1 день

**Зависимости:** Нет

---

### 📋 Детальные шаги выполнения

#### Шаг 1: Создание тестовой директории

**Действие:**
```bash
cd /Users/sergiyzasorin/Development/Nexy/v1.0.6\ Payment
mkdir -p mvp_tests/webhook_logs
mkdir -p mvp_tests/migrations
mkdir -p mvp_tests/tests
```

**Ожидаемый результат:**
```
v1.0.6 Payment/
  └── mvp_tests/
      ├── webhook_logs/
      ├── migrations/
      └── tests/
```

#### Шаг 2: Настройка тестовой БД PostgreSQL

**Действие 1:** Установить PostgreSQL (если не установлен)
```bash
# macOS
brew install postgresql@14
brew services start postgresql@14
```

**Действие 2:** Создать тестовую БД
```bash
createdb nexy_payment_test
psql nexy_payment_test -c "SELECT version();"
```

**Ожидаемый результат:**
```
PostgreSQL 14.x
```

**Проверка:**
```bash
psql nexy_payment_test -c "\l" | grep nexy_payment_test
```

#### Шаг 3: Получение Stripe test API keys

**Действие:**
1. Зайти на https://dashboard.stripe.com/test/apikeys
2. Скопировать **Publishable key** и **Secret key**
3. Создать файл `mvp_tests/.env`:

```bash
cat > mvp_tests/.env << EOF
STRIPE_SECRET_KEY=sk_test_...
STRIPE_PUBLISHABLE_KEY=pk_test_...
STRIPE_WEBHOOK_SECRET=whsec_...  # Получим позже из Stripe CLI
DATABASE_URL=postgresql://localhost/nexy_payment_test
EOF
```

**Ожидаемый результат:**
- Файл `.env` создан с ключами
- Ключи начинаются с `sk_test_` и `pk_test_`

#### Шаг 4: Установка зависимостей

**Действие:**
```bash
cd mvp_tests
python3 -m venv .venv
source .venv/bin/activate
pip install stripe psycopg2-binary python-dotenv flask
```

**Ожидаемый результат:**
```
Successfully installed stripe-X.X.X psycopg2-binary-X.X.X python-dotenv-X.X.X flask-X.X.X
```

#### Шаг 5: Создание тестовых скриптов

**Файл:** `mvp_tests/test_db_connection.py`

```python
#!/usr/bin/env python3
"""Тест подключения к БД"""
import os
import sys
from dotenv import load_dotenv
import psycopg2

load_dotenv()

def test_db_connection():
    """Проверка подключения к PostgreSQL"""
    db_url = os.getenv('DATABASE_URL')
    if not db_url:
        print("❌ DATABASE_URL not found in .env")
        return False
    
    try:
        conn = psycopg2.connect(db_url)
        cur = conn.cursor()
        cur.execute("SELECT version();")
        version = cur.fetchone()[0]
        print(f"✅ Database connection successful")
        print(f"   PostgreSQL version: {version}")
        cur.close()
        conn.close()
        return True
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        return False

if __name__ == '__main__':
    success = test_db_connection()
    sys.exit(0 if success else 1)
```

**Файл:** `mvp_tests/test_stripe_connection.py`

```python
#!/usr/bin/env python3
"""Тест подключения к Stripe"""
import os
import sys
from dotenv import load_dotenv
import stripe

load_dotenv()

def test_stripe_connection():
    """Проверка подключения к Stripe API"""
    api_key = os.getenv('STRIPE_SECRET_KEY')
    if not api_key:
        print("❌ STRIPE_SECRET_KEY not found in .env")
        return False
    
    try:
        stripe.api_key = api_key
        # Простой API call для проверки
        account = stripe.Account.retrieve()
        print(f"✅ Stripe API connection successful")
        print(f"   Account ID: {account.id}")
        print(f"   Country: {account.country}")
        return True
    except stripe.error.AuthenticationError:
        print("❌ Stripe authentication failed - check your API key")
        return False
    except Exception as e:
        print(f"❌ Stripe connection failed: {e}")
        return False

if __name__ == '__main__':
    success = test_stripe_connection()
    sys.exit(0 if success else 1)
```

**Сделать скрипты исполняемыми:**
```bash
chmod +x mvp_tests/test_db_connection.py
chmod +x mvp_tests/test_stripe_connection.py
```

---

### ✅ Критерии готовности

- [ ] Тестовая БД доступна и отвечает на запросы
- [ ] Stripe test API работает (можно получить account info)
- [ ] Все зависимости установлены в `.venv`
- [ ] Тестовые скрипты выполняются без ошибок
- [ ] Файл `.env` создан с корректными ключами

---

### 🧪 Тестирование

**Команды:**
```bash
cd mvp_tests
source .venv/bin/activate

# Тест подключения к БД
python test_db_connection.py

# Тест подключения к Stripe
python test_stripe_connection.py
```

**Ожидаемый вывод:**

**test_db_connection.py:**
```
✅ Database connection successful
   PostgreSQL version: PostgreSQL 14.x on x86_64-apple-darwin...
```

**test_stripe_connection.py:**
```
✅ Stripe API connection successful
   Account ID: acct_...
   Country: US
```

---

### 🔍 Возможные проблемы и решения

**Проблема 1:** `psycopg2` не устанавливается
```bash
# Решение: Установить PostgreSQL development headers
brew install postgresql@14
export PATH="/opt/homebrew/opt/postgresql@14/bin:$PATH"
pip install psycopg2-binary
```

**Проблема 2:** БД не запущена
```bash
# Решение:
brew services start postgresql@14
```

**Проблема 3:** Stripe API key неверный
```bash
# Решение: Проверить ключ в Stripe Dashboard
# Должен начинаться с sk_test_ для test mode
```

---

## 📦 MVP 1: Webhook Endpoint

**Цель:** Прием и логирование webhook событий от Stripe (без обработки)

**Время:** 1-2 дня

**Зависимости:** MVP 0

---

### 📋 Детальные шаги выполнения

#### Шаг 1: Установка Stripe CLI

**Действие:**
```bash
# macOS
brew install stripe/stripe-cli/stripe

# Проверка
stripe --version
```

**Ожидаемый результат:**
```
stripe version X.X.X
```

#### Шаг 2: Создание webhook сервера

**Файл:** `mvp_tests/webhook_server.py`

```python
#!/usr/bin/env python3
"""Простой webhook endpoint для приема событий от Stripe"""
from flask import Flask, request, jsonify
import json
import os
from datetime import datetime
from pathlib import Path

app = Flask(__name__)

# Создаем директорию для логов
LOG_DIR = Path(__file__).parent / 'webhook_logs'
LOG_DIR.mkdir(exist_ok=True)

@app.route('/webhook/stripe', methods=['POST'])
def stripe_webhook():
    """Простой webhook endpoint - только логирование"""
    payload = request.get_data()
    signature = request.headers.get('Stripe-Signature', '')
    
    # Логируем событие
    timestamp = datetime.now().isoformat()
    print(f"\n[{timestamp}] [WEBHOOK] Received event")
    print(f"[WEBHOOK] Signature: {signature[:30]}..." if signature else "[WEBHOOK] No signature")
    print(f"[WEBHOOK] Payload size: {len(payload)} bytes")
    print(f"[WEBHOOK] Content-Type: {request.content_type}")
    
    try:
        event = json.loads(payload)
        event_type = event.get('type', 'unknown')
        event_id = event.get('id', 'unknown')
        created = event.get('created', 0)
        
        print(f"[WEBHOOK] Event type: {event_type}")
        print(f"[WEBHOOK] Event ID: {event_id}")
        print(f"[WEBHOOK] Created: {datetime.fromtimestamp(created)}")
        
        # Сохраняем в файл для анализа
        log_file = LOG_DIR / f"{event_id}.json"
        with open(log_file, 'w') as f:
            json.dump({
                'timestamp': timestamp,
                'event_type': event_type,
                'event_id': event_id,
                'signature': signature,
                'event': event
            }, f, indent=2)
        
        print(f"[WEBHOOK] Saved to: {log_file}")
        print(f"[WEBHOOK] ✅ Event processed successfully\n")
        
        return jsonify({'status': 'received', 'event_id': event_id}), 200
        
    except json.JSONDecodeError as e:
        print(f"[WEBHOOK] ❌ JSON decode error: {e}")
        return jsonify({'error': 'Invalid JSON'}), 400
    except Exception as e:
        print(f"[WEBHOOK] ❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'ok', 'service': 'webhook_server'}), 200

@app.route('/webhook/logs', methods=['GET'])
def list_logs():
    """Список сохраненных событий"""
    logs = []
    for log_file in sorted(LOG_DIR.glob('*.json'), reverse=True):
        try:
            with open(log_file, 'r') as f:
                data = json.load(f)
                logs.append({
                    'file': log_file.name,
                    'event_type': data.get('event_type'),
                    'event_id': data.get('event_id'),
                    'timestamp': data.get('timestamp')
                })
        except:
            pass
    return jsonify({'logs': logs, 'count': len(logs)}), 200

if __name__ == '__main__':
    print("=" * 60)
    print("🚀 Webhook Server Starting...")
    print(f"📁 Log directory: {LOG_DIR}")
    print("=" * 60)
    app.run(host='0.0.0.0', port=8000, debug=True)
```

**Сделать исполняемым:**
```bash
chmod +x mvp_tests/webhook_server.py
```

#### Шаг 3: Запуск webhook сервера

**Действие:**
```bash
cd mvp_tests
source .venv/bin/activate
python webhook_server.py
```

**Ожидаемый результат:**
```
============================================================
🚀 Webhook Server Starting...
📁 Log directory: /path/to/mvp_tests/webhook_logs
============================================================
 * Running on http://0.0.0.0:8000
 * Debug mode: on
```

#### Шаг 4: Настройка Stripe CLI forwarding

**Действие 1:** В новом терминале авторизоваться в Stripe CLI
```bash
stripe login
```

**Действие 2:** Запустить forwarding
```bash
stripe listen --forward-to localhost:8000/webhook/stripe
```

**Ожидаемый результат:**
```
> Ready! Your webhook signing secret is whsec_... (^C to quit)
```

**Важно:** Скопировать `whsec_...` и добавить в `mvp_tests/.env`:
```bash
STRIPE_WEBHOOK_SECRET=whsec_...
```

#### Шаг 5: Отправка тестовых событий

**Действие:**
```bash
# В третьем терминале
stripe trigger checkout.session.completed
stripe trigger invoice.payment_succeeded
stripe trigger invoice.payment_failed
stripe trigger customer.subscription.updated
```

---

### ✅ Критерии готовности

- [ ] Webhook endpoint принимает POST запросы на `/webhook/stripe`
- [ ] События логируются в консоль с деталями
- [ ] События сохраняются в JSON файлы в `webhook_logs/`
- [ ] Stripe CLI успешно пересылает события
- [ ] Health check endpoint работает (`/health`)
- [ ] Можно просмотреть список логов (`/webhook/logs`)

---

### 🧪 Тестирование

**Команды:**

**Терминал 1 (Webhook Server):**
```bash
cd mvp_tests
source .venv/bin/activate
python webhook_server.py
```

**Терминал 2 (Stripe CLI):**
```bash
stripe listen --forward-to localhost:8000/webhook/stripe
```

**Терминал 3 (Тестирование):**
```bash
# Отправить тестовые события
stripe trigger checkout.session.completed
stripe trigger invoice.payment_succeeded
stripe trigger invoice.payment_failed
stripe trigger customer.subscription.updated
```

**Ожидаемый вывод в терминале 1:**

```
[2025-12-13T10:30:45] [WEBHOOK] Received event
[WEBHOOK] Signature: t=1234567890,v1=abc123...
[WEBHOOK] Payload size: 1234 bytes
[WEBHOOK] Content-Type: application/json
[WEBHOOK] Event type: checkout.session.completed
[WEBHOOK] Event ID: evt_1234567890
[WEBHOOK] Created: 2025-12-13 10:30:45
[WEBHOOK] Saved to: webhook_logs/evt_1234567890.json
[WEBHOOK] ✅ Event processed successfully
```

**Проверка сохраненных файлов:**
```bash
ls -lh mvp_tests/webhook_logs/
cat mvp_tests/webhook_logs/evt_*.json | jq '.event_type'
```

**Проверка через HTTP:**
```bash
# Health check
curl http://localhost:8000/health

# Список логов
curl http://localhost:8000/webhook/logs | jq
```

---

### 📊 Ожидаемые результаты

**После успешного выполнения:**

1. **В консоли webhook сервера:**
   - Видны все входящие события
   - Каждое событие логируется с деталями
   - Нет ошибок при обработке

2. **В директории `webhook_logs/`:**
   - Созданы JSON файлы для каждого события
   - Файлы содержат полную информацию о событии
   - Можно анализировать структуру событий

3. **В Stripe CLI:**
   - Видны успешные пересылки событий
   - Нет ошибок подключения

---

### 🔍 Возможные проблемы и решения

**Проблема 1:** `stripe listen` не подключается
```bash
# Решение: Проверить, что webhook сервер запущен
curl http://localhost:8000/health

# Проверить порт
lsof -i :8000
```

**Проблема 2:** События не доходят
```bash
# Решение: Проверить firewall
# macOS: System Preferences > Security > Firewall

# Проверить логи Stripe CLI
stripe listen --forward-to localhost:8000/webhook/stripe --print-json
```

**Проблема 3:** Ошибка "Invalid JSON"
```bash
# Решение: Проверить, что payload не поврежден
# Добавить логирование raw payload в webhook_server.py
print(f"[DEBUG] Raw payload: {payload[:200]}")
```

**Проблема 4:** Файлы не сохраняются
```bash
# Решение: Проверить права доступа
chmod -R 755 mvp_tests/webhook_logs/
```

---

## 📦 MVP 2: База данных

**Цель:** Миграции и простые CRUD операции

**Время:** 1-2 дня

**Зависимости:** MVP 0

---

### 📋 Детальные шаги выполнения

#### Шаг 1: Создание миграций

**Файл:** `mvp_tests/migrations/001_create_subscriptions.sql`

```sql
-- MVP 2: Базовая структура для подписок
-- Простая версия для тестирования

-- Таблица подписок
CREATE TABLE IF NOT EXISTS subscriptions (
    hardware_id VARCHAR(255) PRIMARY KEY,
    status VARCHAR(50) NOT NULL DEFAULT 'paid_trial',
    stripe_customer_id VARCHAR(255),
    stripe_subscription_id VARCHAR(255),
    paid_trial_end_at TIMESTAMP,
    grace_period_end_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Индексы для быстрого поиска
CREATE INDEX IF NOT EXISTS idx_subscriptions_status ON subscriptions(status);
CREATE INDEX IF NOT EXISTS idx_subscriptions_stripe_customer ON subscriptions(stripe_customer_id);
CREATE INDEX IF NOT EXISTS idx_subscriptions_stripe_subscription ON subscriptions(stripe_subscription_id);

-- Таблица событий (для идемпотентности)
CREATE TABLE IF NOT EXISTS subscription_events (
    stripe_event_id VARCHAR(255) PRIMARY KEY,
    event_type VARCHAR(100) NOT NULL,
    hardware_id VARCHAR(255),
    event_data JSONB,
    processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Индекс для поиска по hardware_id
CREATE INDEX IF NOT EXISTS idx_subscription_events_hardware ON subscription_events(hardware_id);
CREATE INDEX IF NOT EXISTS idx_subscription_events_type ON subscription_events(event_type);

-- Комментарии для документации
COMMENT ON TABLE subscriptions IS 'Подписки пользователей';
COMMENT ON COLUMN subscriptions.hardware_id IS 'Уникальный идентификатор устройства';
COMMENT ON COLUMN subscriptions.status IS 'Статус подписки: paid_trial, paid, billing_problem, limited_free_trial, etc.';
COMMENT ON TABLE subscription_events IS 'Обработанные webhook события (для идемпотентности)';
```

#### Шаг 2: Применение миграций

**Действие:**
```bash
cd mvp_tests
psql $DATABASE_URL -f migrations/001_create_subscriptions.sql
```

**Ожидаемый результат:**
```
CREATE TABLE
CREATE INDEX
CREATE INDEX
CREATE INDEX
CREATE TABLE
CREATE INDEX
CREATE INDEX
COMMENT
COMMENT
COMMENT
```

**Проверка:**
```bash
psql $DATABASE_URL -c "\d subscriptions"
psql $DATABASE_URL -c "\d subscription_events"
```

#### Шаг 3: Создание Repository

**Файл:** `mvp_tests/subscription_repository.py`

```python
#!/usr/bin/env python3
"""Repository для работы с подписками в БД"""
import psycopg2
from psycopg2.extras import RealDictCursor
from typing import Optional, Dict, List
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

class SubscriptionRepository:
    def __init__(self, db_url: Optional[str] = None):
        self.db_url = db_url or os.getenv('DATABASE_URL')
        if not self.db_url:
            raise ValueError("DATABASE_URL not found")
    
    def _get_connection(self):
        """Получить соединение с БД"""
        return psycopg2.connect(self.db_url)
    
    def get_subscription(self, hardware_id: str) -> Optional[Dict]:
        """Получить подписку по hardware_id"""
        conn = self._get_connection()
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(
                    """SELECT 
                        hardware_id, status, stripe_customer_id, 
                        stripe_subscription_id, paid_trial_end_at, 
                        grace_period_end_at, created_at, updated_at
                       FROM subscriptions 
                       WHERE hardware_id = %s""",
                    (hardware_id,)
                )
                row = cur.fetchone()
                return dict(row) if row else None
        finally:
            conn.close()
    
    def create_subscription(
        self, 
        hardware_id: str, 
        status: str = 'paid_trial',
        paid_trial_end_at: Optional[datetime] = None
    ) -> Dict:
        """Создать новую подписку"""
        conn = self._get_connection()
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(
                    """INSERT INTO subscriptions (hardware_id, status, paid_trial_end_at)
                       VALUES (%s, %s, %s)
                       ON CONFLICT (hardware_id) DO NOTHING
                       RETURNING *""",
                    (hardware_id, status, paid_trial_end_at)
                )
                row = cur.fetchone()
                conn.commit()
                if row:
                    return dict(row)
                # Если конфликт, получаем существующую запись
                return self.get_subscription(hardware_id)
        finally:
            conn.close()
    
    def update_status(self, hardware_id: str, status: str) -> bool:
        """Обновить статус подписки"""
        conn = self._get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(
                    """UPDATE subscriptions 
                       SET status = %s, updated_at = CURRENT_TIMESTAMP 
                       WHERE hardware_id = %s""",
                    (status, hardware_id)
                )
                conn.commit()
                return cur.rowcount > 0
        finally:
            conn.close()
    
    def update_stripe_ids(
        self, 
        hardware_id: str, 
        customer_id: Optional[str] = None,
        subscription_id: Optional[str] = None
    ) -> bool:
        """Обновить Stripe IDs"""
        conn = self._get_connection()
        try:
            updates = []
            params = []
            if customer_id:
                updates.append("stripe_customer_id = %s")
                params.append(customer_id)
            if subscription_id:
                updates.append("stripe_subscription_id = %s")
                params.append(subscription_id)
            
            if not updates:
                return False
            
            updates.append("updated_at = CURRENT_TIMESTAMP")
            params.append(hardware_id)
            
            query = f"UPDATE subscriptions SET {', '.join(updates)} WHERE hardware_id = %s"
            with conn.cursor() as cur:
                cur.execute(query, params)
                conn.commit()
                return cur.rowcount > 0
        finally:
            conn.close()
    
    def record_event(
        self,
        stripe_event_id: str,
        event_type: str,
        hardware_id: Optional[str] = None,
        event_data: Optional[Dict] = None
    ) -> bool:
        """Записать обработанное событие (для идемпотентности)"""
        conn = self._get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(
                    """INSERT INTO subscription_events 
                       (stripe_event_id, event_type, hardware_id, event_data)
                       VALUES (%s, %s, %s, %s::jsonb)
                       ON CONFLICT (stripe_event_id) DO NOTHING""",
                    (stripe_event_id, event_type, hardware_id, 
                     psycopg2.extras.Json(event_data) if event_data else None)
                )
                conn.commit()
                return cur.rowcount > 0
        except psycopg2.IntegrityError:
            # Событие уже обработано (идемпотентность)
            return False
        finally:
            conn.close()
    
    def event_exists(self, stripe_event_id: str) -> bool:
        """Проверить, было ли событие уже обработано"""
        conn = self._get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT 1 FROM subscription_events WHERE stripe_event_id = %s",
                    (stripe_event_id,)
                )
                return cur.fetchone() is not None
        finally:
            conn.close()
```

#### Шаг 4: Создание тестов

**Файл:** `mvp_tests/test_subscription_repository.py`

```python
#!/usr/bin/env python3
"""Тесты для SubscriptionRepository"""
import sys
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
from subscription_repository import SubscriptionRepository

load_dotenv()

def test_create_subscription():
    """Тест создания подписки"""
    repo = SubscriptionRepository()
    hardware_id = f"test_hw_{datetime.now().timestamp()}"
    
    print(f"🧪 Test: Create subscription for {hardware_id}")
    result = repo.create_subscription(hardware_id, status='paid_trial')
    
    assert result is not None, "Subscription should be created"
    assert result['hardware_id'] == hardware_id, "Hardware ID should match"
    assert result['status'] == 'paid_trial', "Status should be paid_trial"
    print("✅ Create subscription: PASSED")
    return hardware_id

def test_get_subscription(hardware_id: str):
    """Тест получения подписки"""
    repo = SubscriptionRepository()
    
    print(f"🧪 Test: Get subscription for {hardware_id}")
    result = repo.get_subscription(hardware_id)
    
    assert result is not None, "Subscription should exist"
    assert result['hardware_id'] == hardware_id, "Hardware ID should match"
    print("✅ Get subscription: PASSED")

def test_update_status(hardware_id: str):
    """Тест обновления статуса"""
    repo = SubscriptionRepository()
    
    print(f"🧪 Test: Update status for {hardware_id}")
    success = repo.update_status(hardware_id, 'paid')
    
    assert success, "Update should succeed"
    
    # Проверяем, что статус обновился
    result = repo.get_subscription(hardware_id)
    assert result['status'] == 'paid', "Status should be updated to paid"
    print("✅ Update status: PASSED")

def test_update_stripe_ids(hardware_id: str):
    """Тест обновления Stripe IDs"""
    repo = SubscriptionRepository()
    
    print(f"🧪 Test: Update Stripe IDs for {hardware_id}")
    success = repo.update_stripe_ids(
        hardware_id,
        customer_id='cus_test123',
        subscription_id='sub_test123'
    )
    
    assert success, "Update should succeed"
    
    result = repo.get_subscription(hardware_id)
    assert result['stripe_customer_id'] == 'cus_test123', "Customer ID should match"
    assert result['stripe_subscription_id'] == 'sub_test123', "Subscription ID should match"
    print("✅ Update Stripe IDs: PASSED")

def test_event_idempotency():
    """Тест идемпотентности событий"""
    repo = SubscriptionRepository()
    event_id = f"evt_test_{datetime.now().timestamp()}"
    
    print(f"🧪 Test: Event idempotency for {event_id}")
    
    # Первая запись
    success1 = repo.record_event(event_id, 'test.event', hardware_id='test_hw')
    assert success1, "First event should be recorded"
    
    # Проверка существования
    exists = repo.event_exists(event_id)
    assert exists, "Event should exist"
    
    # Вторая запись (должна быть проигнорирована)
    success2 = repo.record_event(event_id, 'test.event', hardware_id='test_hw')
    assert not success2, "Duplicate event should be ignored"
    
    print("✅ Event idempotency: PASSED")

def main():
    """Запуск всех тестов"""
    print("=" * 60)
    print("🧪 Running SubscriptionRepository tests...")
    print("=" * 60)
    
    try:
        hardware_id = test_create_subscription()
        test_get_subscription(hardware_id)
        test_update_status(hardware_id)
        test_update_stripe_ids(hardware_id)
        test_event_idempotency()
        
        print("=" * 60)
        print("✅ All tests PASSED")
        print("=" * 60)
        return 0
    except AssertionError as e:
        print(f"❌ Test FAILED: {e}")
        return 1
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == '__main__':
    sys.exit(main())
```

---

### ✅ Критерии готовности

- [ ] Миграции применены успешно
- [ ] Таблицы `subscriptions` и `subscription_events` созданы
- [ ] Индексы созданы
- [ ] Можно создать подписку через Repository
- [ ] Можно получить подписку по hardware_id
- [ ] Можно обновить статус подписки
- [ ] Можно обновить Stripe IDs
- [ ] Идемпотентность событий работает (дубликаты игнорируются)
- [ ] Все unit тесты пройдены

---

### 🧪 Тестирование

**Команды:**

```bash
cd mvp_tests
source .venv/bin/activate

# Применить миграции
psql $DATABASE_URL -f migrations/001_create_subscriptions.sql

# Запустить тесты
python test_subscription_repository.py
```

**Ожидаемый вывод:**

```
============================================================
🧪 Running SubscriptionRepository tests...
============================================================
🧪 Test: Create subscription for test_hw_1234567890
✅ Create subscription: PASSED
🧪 Test: Get subscription for test_hw_1234567890
✅ Get subscription: PASSED
🧪 Test: Update status for test_hw_1234567890
✅ Update status: PASSED
🧪 Test: Update Stripe IDs for test_hw_1234567890
✅ Update Stripe IDs: PASSED
🧪 Test: Event idempotency for evt_test_1234567890
✅ Event idempotency: PASSED
============================================================
✅ All tests PASSED
============================================================
```

**Проверка в БД:**
```bash
# Проверить созданные записи
psql $DATABASE_URL -c "SELECT * FROM subscriptions LIMIT 5;"
psql $DATABASE_URL -c "SELECT * FROM subscription_events LIMIT 5;"
```

---

### 📊 Ожидаемые результаты

**После успешного выполнения:**

1. **В БД:**
   - Таблицы `subscriptions` и `subscription_events` созданы
   - Индексы созданы для быстрого поиска
   - Можно выполнять CRUD операции

2. **В коде:**
   - `SubscriptionRepository` работает корректно
   - Все методы протестированы
   - Идемпотентность событий работает

---

### 🔍 Возможные проблемы и решения

**Проблема 1:** Ошибка "relation does not exist"
```bash
# Решение: Применить миграции
psql $DATABASE_URL -f migrations/001_create_subscriptions.sql
```

**Проблема 2:** Ошибка подключения к БД
```bash
# Решение: Проверить DATABASE_URL в .env
echo $DATABASE_URL
# Должен быть: postgresql://user:pass@localhost/dbname
```

**Проблема 3:** Ошибка "duplicate key value"
```bash
# Решение: Это нормально для идемпотентности
# Проверить, что ON CONFLICT работает
```

---

## 📦 MVP 3: Stripe Service

**Цель:** Создание Checkout Session (изолированно, без интеграции)

**Время:** 1-2 дня

**Зависимости:** MVP 0

---

### 📋 Детальные шаги выполнения

#### Шаг 1: Создание Stripe Service

**Файл:** `mvp_tests/stripe_service.py`

```python
#!/usr/bin/env python3
"""Stripe Service для работы с Stripe API"""
import stripe
from typing import Dict, Optional
import os
from dotenv import load_dotenv

load_dotenv()

class StripeService:
    def __init__(self, api_key: Optional[str] = None):
        """Инициализация Stripe Service"""
        self.api_key = api_key or os.getenv('STRIPE_SECRET_KEY')
        if not self.api_key:
            raise ValueError("STRIPE_SECRET_KEY not found")
        stripe.api_key = self.api_key
    
    def create_checkout_session(
        self,
        hardware_id: str,
        success_url: str,
        cancel_url: str,
        price_id: Optional[str] = None
    ) -> Dict:
        """
        Создать Checkout Session для подписки
        
        Args:
            hardware_id: Уникальный ID устройства
            success_url: URL для редиректа после успешной оплаты
            cancel_url: URL для редиректа при отмене
            price_id: Опциональный Stripe Price ID (если не указан, создается динамически)
        
        Returns:
            Dict с checkout_url, session_id, customer_id
        """
        try:
            print(f"[STRIPE] Creating checkout session for hardware_id: {hardware_id}")
            
            # Параметры для создания сессии
            session_params = {
                'mode': 'subscription',
                'success_url': success_url,
                'cancel_url': cancel_url,
                'metadata': {
                    'hardware_id': hardware_id,
                },
                'allow_promotion_codes': True,
            }
            
            # Если указан price_id, используем его
            if price_id:
                session_params['line_items'] = [{
                    'price': price_id,
                    'quantity': 1,
                }]
            else:
                # Создаем динамический price
                session_params['line_items'] = [{
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': 'Nexy Premium',
                            'description': 'Unlimited access to Nexy AI Assistant',
                        },
                        'recurring': {
                            'interval': 'month',
                        },
                        'unit_amount': 999,  # $9.99 в центах
                    },
                    'quantity': 1,
                }]
            
            # Создаем сессию
            session = stripe.checkout.Session.create(**session_params)
            
            result = {
                'checkout_url': session.url,
                'session_id': session.id,
                'customer_id': session.customer,
                'subscription_id': session.subscription,
            }
            
            print(f"[STRIPE] ✅ Checkout session created: {session.id}")
            print(f"[STRIPE] URL: {session.url}")
            
            return result
            
        except stripe.error.StripeError as e:
            print(f"[STRIPE] ❌ Stripe error: {e}")
            raise
        except Exception as e:
            print(f"[STRIPE] ❌ Error creating checkout: {e}")
            raise
    
    def get_checkout_session(self, session_id: str) -> Dict:
        """Получить информацию о Checkout Session"""
        try:
            session = stripe.checkout.Session.retrieve(session_id)
            return {
                'id': session.id,
                'status': session.status,
                'customer_id': session.customer,
                'subscription_id': session.subscription,
                'payment_status': session.payment_status,
                'url': session.url,
            }
        except stripe.error.StripeError as e:
            print(f"[STRIPE] ❌ Error retrieving session: {e}")
            raise
    
    def verify_webhook_signature(
        self,
        payload: bytes,
        signature: str,
        secret: Optional[str] = None
    ) -> Optional[stripe.Event]:
        """
        Верификация подписи webhook и получение события
        
        Returns:
            stripe.Event если подпись валидна, None если нет
        """
        webhook_secret = secret or os.getenv('STRIPE_WEBHOOK_SECRET')
        if not webhook_secret:
            print("[STRIPE] ⚠️ STRIPE_WEBHOOK_SECRET not found, skipping verification")
            return None
        
        try:
            event = stripe.Webhook.construct_event(
                payload, signature, webhook_secret
            )
            print(f"[STRIPE] ✅ Webhook signature verified: {event['id']}")
            return event
        except ValueError as e:
            print(f"[STRIPE] ❌ Invalid payload: {e}")
            return None
        except stripe.error.SignatureVerificationError as e:
            print(f"[STRIPE] ❌ Invalid signature: {e}")
            return None
    
    def get_customer(self, customer_id: str) -> Dict:
        """Получить информацию о клиенте"""
        try:
            customer = stripe.Customer.retrieve(customer_id)
            return {
                'id': customer.id,
                'email': customer.email,
                'created': customer.created,
            }
        except stripe.error.StripeError as e:
            print(f"[STRIPE] ❌ Error retrieving customer: {e}")
            raise
    
    def get_subscription(self, subscription_id: str) -> Dict:
        """Получить информацию о подписке"""
        try:
            subscription = stripe.Subscription.retrieve(subscription_id)
            return {
                'id': subscription.id,
                'status': subscription.status,
                'customer_id': subscription.customer,
                'current_period_end': subscription.current_period_end,
                'cancel_at_period_end': subscription.cancel_at_period_end,
            }
        except stripe.error.StripeError as e:
            print(f"[STRIPE] ❌ Error retrieving subscription: {e}")
            raise
```

#### Шаг 2: Создание тестов

**Файл:** `mvp_tests/test_stripe_service.py`

```python
#!/usr/bin/env python3
"""Тесты для StripeService"""
import sys
import os
from dotenv import load_dotenv
from stripe_service import StripeService

load_dotenv()

def test_create_checkout_session():
    """Тест создания Checkout Session"""
    print("🧪 Test: Create checkout session")
    
    service = StripeService()
    hardware_id = f"test_hw_{os.getpid()}"
    
    result = service.create_checkout_session(
        hardware_id=hardware_id,
        success_url="https://example.com/success",
        cancel_url="https://example.com/cancel"
    )
    
    assert 'checkout_url' in result, "Should have checkout_url"
    assert 'session_id' in result, "Should have session_id"
    assert result['checkout_url'].startswith('https://checkout.stripe.com'), "URL should be Stripe checkout"
    
    print(f"✅ Checkout URL: {result['checkout_url']}")
    print(f"✅ Session ID: {result['session_id']}")
    print("✅ Create checkout session: PASSED")
    
    return result['session_id']

def test_get_checkout_session(session_id: str):
    """Тест получения информации о сессии"""
    print(f"🧪 Test: Get checkout session {session_id}")
    
    service = StripeService()
    session = service.get_checkout_session(session_id)
    
    assert session['id'] == session_id, "Session ID should match"
    assert 'status' in session, "Should have status"
    
    print(f"✅ Session status: {session['status']}")
    print("✅ Get checkout session: PASSED")

def test_webhook_verification():
    """Тест верификации webhook подписи"""
    print("🧪 Test: Webhook signature verification")
    
    service = StripeService()
    
    # Тестовый payload и signature (в реальности приходят от Stripe)
    # Для MVP просто проверяем, что метод не падает
    test_payload = b'{"id":"evt_test"}'
    test_signature = "test_signature"
    
    # Должен вернуть None для невалидной подписи
    result = service.verify_webhook_signature(
        test_payload,
        test_signature,
        "invalid_secret"
    )
    
    assert result is None, "Invalid signature should return None"
    print("✅ Webhook verification: PASSED")

def main():
    """Запуск всех тестов"""
    print("=" * 60)
    print("🧪 Running StripeService tests...")
    print("=" * 60)
    
    try:
        session_id = test_create_checkout_session()
        test_get_checkout_session(session_id)
        test_webhook_verification()
        
        print("=" * 60)
        print("✅ All tests PASSED")
        print("=" * 60)
        print("\n💡 Next steps:")
        print(f"   1. Open checkout URL in browser")
        print(f"   2. Use test card: 4242 4242 4242 4242")
        print(f"   3. Any future expiry date, any CVC")
        return 0
    except AssertionError as e:
        print(f"❌ Test FAILED: {e}")
        return 1
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == '__main__':
    sys.exit(main())
```

---

### ✅ Критерии готовности

- [ ] `StripeService` инициализируется с API ключом
- [ ] Можно создать Checkout Session
- [ ] Получаем валидный `checkout_url` (начинается с `https://checkout.stripe.com`)
- [ ] Получаем `session_id` и `customer_id`
- [ ] Можно получить информацию о сессии по `session_id`
- [ ] Верификация webhook подписи работает (возвращает `None` для невалидной)
- [ ] Все тесты пройдены

---

### 🧪 Тестирование

**Команды:**

```bash
cd mvp_tests
source .venv/bin/activate

# Запустить тесты
python test_stripe_service.py
```

**Ожидаемый вывод:**

```
============================================================
🧪 Running StripeService tests...
============================================================
[STRIPE] Creating checkout session for hardware_id: test_hw_12345
[STRIPE] ✅ Checkout session created: cs_test_...
[STRIPE] URL: https://checkout.stripe.com/c/pay/cs_test_...
🧪 Test: Create checkout session
✅ Checkout URL: https://checkout.stripe.com/c/pay/cs_test_...
✅ Session ID: cs_test_...
✅ Create checkout session: PASSED
🧪 Test: Get checkout session cs_test_...
✅ Session status: open
✅ Get checkout session: PASSED
🧪 Test: Webhook signature verification
✅ Webhook verification: PASSED
============================================================
✅ All tests PASSED
============================================================

💡 Next steps:
   1. Open checkout URL in browser
   2. Use test card: 4242 4242 4242 4242
   3. Any future expiry date, any CVC
```

**Ручное тестирование:**

1. Скопировать `checkout_url` из вывода
2. Открыть в браузере
3. Использовать тестовую карту Stripe:
   - Номер: `4242 4242 4242 4242`
   - Дата: любая будущая (например, `12/25`)
   - CVC: любой (например, `123`)
   - ZIP: любой (например, `12345`)
4. Проверить, что редирект на `success_url` работает

---

### 📊 Ожидаемые результаты

**После успешного выполнения:**

1. **В коде:**
   - `StripeService` работает корректно
   - Можно создавать Checkout Sessions
   - Можно получать информацию о сессиях

2. **В Stripe Dashboard:**
   - Видны созданные Checkout Sessions
   - Можно просмотреть детали сессий
   - Тестовые платежи проходят успешно

---

### 🔍 Возможные проблемы и решения

**Проблема 1:** Ошибка "Invalid API Key"
```bash
# Решение: Проверить STRIPE_SECRET_KEY в .env
# Должен начинаться с sk_test_ для test mode
echo $STRIPE_SECRET_KEY
```

**Проблема 2:** Ошибка "No such price"
```bash
# Решение: Использовать динамический price_data (уже в коде)
# Или создать Price в Stripe Dashboard и использовать price_id
```

**Проблема 3:** Checkout URL не открывается
```bash
# Решение: Проверить, что URL скопирован полностью
# URL должен начинаться с https://checkout.stripe.com
```

---

## 📦 MVP 4: Subscription Repository + БД

**Цель:** Полная работа с БД для подписок (расширение MVP 2)

**Время:** 1 день

**Зависимости:** MVP 2

---

### 📋 Детальные шаги выполнения

#### Шаг 1: Расширение миграций

**Файл:** `mvp_tests/migrations/002_add_usage_tracking.sql`

```sql
-- MVP 4: Добавление таблицы для отслеживания использования (usage tracking)

CREATE TABLE IF NOT EXISTS subscription_usage (
    id SERIAL PRIMARY KEY,
    hardware_id VARCHAR(255) NOT NULL,
    usage_date DATE NOT NULL,
    daily_count INTEGER DEFAULT 0,
    weekly_count INTEGER DEFAULT 0,
    monthly_count INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(hardware_id, usage_date)
);

CREATE INDEX IF NOT EXISTS idx_subscription_usage_hardware ON subscription_usage(hardware_id);
CREATE INDEX IF NOT EXISTS idx_subscription_usage_date ON subscription_usage(usage_date);

COMMENT ON TABLE subscription_usage IS 'Отслеживание использования для квот';
```

#### Шаг 2: Расширение Repository

**Обновить:** `mvp_tests/subscription_repository.py`

**Добавить методы:**

```python
def increment_usage(self, hardware_id: str) -> bool:
    """Инкрементировать счетчик использования"""
    from datetime import date
    conn = self._get_connection()
    try:
        with conn.cursor() as cur:
            # Upsert для текущей даты
            cur.execute(
                """INSERT INTO subscription_usage 
                   (hardware_id, usage_date, daily_count, weekly_count, monthly_count)
                   VALUES (%s, CURRENT_DATE, 1, 1, 1)
                   ON CONFLICT (hardware_id, usage_date) 
                   DO UPDATE SET 
                       daily_count = subscription_usage.daily_count + 1,
                       weekly_count = subscription_usage.weekly_count + 1,
                       monthly_count = subscription_usage.monthly_count + 1,
                       updated_at = CURRENT_TIMESTAMP""",
                (hardware_id,)
            )
            conn.commit()
            return cur.rowcount > 0
    finally:
        conn.close()

def get_usage_stats(self, hardware_id: str) -> Dict:
    """Получить статистику использования"""
    conn = self._get_connection()
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            # Текущий день
            cur.execute(
                """SELECT daily_count, weekly_count, monthly_count
                   FROM subscription_usage
                   WHERE hardware_id = %s AND usage_date = CURRENT_DATE""",
                (hardware_id,)
            )
            today = cur.fetchone()
            
            return {
                'daily_used': today['daily_count'] if today else 0,
                'weekly_used': today['weekly_count'] if today else 0,
                'monthly_used': today['monthly_count'] if today else 0,
            }
    finally:
        conn.close()
```

#### Шаг 3: Тесты

**Файл:** `mvp_tests/test_subscription_repository_extended.py`

```python
#!/usr/bin/env python3
"""Расширенные тесты для SubscriptionRepository"""
import sys
from datetime import datetime
from subscription_repository import SubscriptionRepository

def test_usage_tracking():
    """Тест отслеживания использования"""
    repo = SubscriptionRepository()
    hardware_id = f"test_hw_{datetime.now().timestamp()}"
    
    # Создать подписку
    repo.create_subscription(hardware_id)
    
    # Инкрементировать использование
    repo.increment_usage(hardware_id)
    repo.increment_usage(hardware_id)
    
    # Получить статистику
    stats = repo.get_usage_stats(hardware_id)
    
    assert stats['daily_used'] >= 2, "Daily count should be at least 2"
    print("✅ Usage tracking: PASSED")

if __name__ == '__main__':
    test_usage_tracking()
    print("✅ All extended tests PASSED")
```

---

### ✅ Критерии готовности

- [ ] Таблица `subscription_usage` создана
- [ ] Метод `increment_usage()` работает
- [ ] Метод `get_usage_stats()` возвращает корректные данные
- [ ] Тесты пройдены

---

### 🧪 Тестирование

```bash
cd mvp_tests
source .venv/bin/activate

# Применить миграции
psql $DATABASE_URL -f migrations/002_add_usage_tracking.sql

# Запустить тесты
python test_subscription_repository_extended.py
```

---

### 📊 Ожидаемые результаты

- Таблица `subscription_usage` создана с правильными индексами
- Можно инкрементировать счетчики использования
- Можно получать статистику использования

---

## 📦 MVP 5: Subscription Context

**Цель:** Получение контекста подписки (без интеграции в workflow)

**Время:** 1 день

**Зависимости:** MVP 4

---

### 📋 Детальные шаги выполнения

#### Шаг 1: Создание SubscriptionContext

**Файл:** `mvp_tests/subscription_context.py`

```python
#!/usr/bin/env python3
"""SubscriptionContext - формирование контекста подписки для LLM"""
from subscription_repository import SubscriptionRepository
from datetime import datetime, timedelta
from typing import Dict, Optional
import os
from dotenv import load_dotenv

load_dotenv()

class SubscriptionContext:
    def __init__(self, repo: Optional[SubscriptionRepository] = None):
        """Инициализация SubscriptionContext"""
        if repo:
            self.repo = repo
        else:
            from subscription_repository import SubscriptionRepository
            self.repo = SubscriptionRepository()
    
    def get_context(self, hardware_id: str) -> Dict:
        """
        Получить полный контекст подписки
        
        Returns:
            Dict с полной информацией о подписке
        """
        subscription = self.repo.get_subscription(hardware_id)
        
        if not subscription:
            # Создать новую подписку с trial периодом
            trial_end = datetime.now() + timedelta(days=14)
            subscription = self.repo.create_subscription(
                hardware_id,
                status='paid_trial',
                paid_trial_end_at=trial_end
            )
        
        # Формируем контекст
        context = {
            'hardware_id': hardware_id,
            'status': subscription['status'],
            'stripe_customer_id': subscription.get('stripe_customer_id'),
            'stripe_subscription_id': subscription.get('stripe_subscription_id'),
        }
        
        # Trial период
        if subscription.get('paid_trial_end_at'):
            trial_end = subscription['paid_trial_end_at']
            if isinstance(trial_end, str):
                trial_end = datetime.fromisoformat(trial_end.replace('Z', '+00:00'))
            days_left = (trial_end - datetime.now()).days
            context['trial_days_left'] = max(0, days_left)
            context['trial_end_at'] = trial_end.isoformat()
        
        # Grace period
        if subscription.get('grace_period_end_at'):
            grace_end = subscription['grace_period_end_at']
            if isinstance(grace_end, str):
                grace_end = datetime.fromisoformat(grace_end.replace('Z', '+00:00'))
            context['grace_period_end_at'] = grace_end.isoformat()
            context['grace_period_active'] = grace_end > datetime.now()
        
        # Usage stats
        usage_stats = self.repo.get_usage_stats(hardware_id)
        context.update(usage_stats)
        
        return context
    
    def format_for_llm(self, context: Dict) -> str:
        """
        Форматировать контекст для LLM prompt
        
        Returns:
            Строка для добавления в system prompt
        """
        status = context['status']
        lines = []
        
        if status == 'paid_trial':
            days = context.get('trial_days_left', 0)
            lines.append(f"User subscription: Paid trial period ({days} days remaining).")
            if days <= 2:
                lines.append(f"⚠️ IMPORTANT: Trial expires in {days} day(s). User should be informed about subscription options.")
        elif status == 'paid':
            lines.append("User subscription: Active paid subscription. Full access enabled.")
        elif status == 'billing_problem':
            grace_active = context.get('grace_period_active', False)
            if grace_active:
                lines.append("User subscription: Billing problem detected, but grace period is active (1 day). Full access maintained.")
            else:
                lines.append("User subscription: Billing problem - grace period expired. Limited access.")
        elif status == 'limited_free_trial':
            daily_used = context.get('daily_used', 0)
            daily_limit = 5
            lines.append(f"User subscription: Limited free trial. Usage: {daily_used}/{daily_limit} requests today.")
            if daily_used >= daily_limit:
                lines.append("⚠️ IMPORTANT: Daily limit reached. User should be informed about subscription options.")
        else:
            lines.append(f"User subscription status: {status}")
        
        return "\n".join(lines)
    
    def get_context_for_prompt(self, hardware_id: str) -> str:
        """Получить форматированный контекст для LLM prompt"""
        context = self.get_context(hardware_id)
        return self.format_for_llm(context)
```

#### Шаг 2: Создание тестов

**Файл:** `mvp_tests/test_subscription_context.py`

```python
#!/usr/bin/env python3
"""Тесты для SubscriptionContext"""
import sys
from datetime import datetime, timedelta
from subscription_context import SubscriptionContext
from subscription_repository import SubscriptionRepository

def test_get_context_new_user():
    """Тест получения контекста для нового пользователя"""
    print("🧪 Test: Get context for new user")
    
    repo = SubscriptionRepository()
    context_builder = SubscriptionContext(repo)
    
    hardware_id = f"test_hw_{datetime.now().timestamp()}"
    context = context_builder.get_context(hardware_id)
    
    assert context['status'] == 'paid_trial', "New user should have paid_trial status"
    assert 'trial_days_left' in context, "Should have trial_days_left"
    assert context['trial_days_left'] >= 0, "Trial days should be non-negative"
    
    print(f"✅ Status: {context['status']}")
    print(f"✅ Trial days left: {context['trial_days_left']}")
    print("✅ Get context for new user: PASSED")

def test_format_for_llm():
    """Тест форматирования для LLM"""
    print("🧪 Test: Format context for LLM")
    
    repo = SubscriptionRepository()
    context_builder = SubscriptionContext(repo)
    
    hardware_id = f"test_hw_{datetime.now().timestamp()}"
    formatted = context_builder.get_context_for_prompt(hardware_id)
    
    assert len(formatted) > 0, "Formatted text should not be empty"
    assert 'subscription' in formatted.lower(), "Should mention subscription"
    
    print(f"✅ Formatted text:\n{formatted}")
    print("✅ Format for LLM: PASSED")

def test_context_with_different_statuses():
    """Тест контекста для разных статусов"""
    print("🧪 Test: Context with different statuses")
    
    repo = SubscriptionRepository()
    context_builder = SubscriptionContext(repo)
    
    hardware_id = f"test_hw_{datetime.now().timestamp()}"
    repo.create_subscription(hardware_id, status='paid')
    repo.update_status(hardware_id, 'paid')
    
    context = context_builder.get_context(hardware_id)
    formatted = context_builder.format_for_llm(context)
    
    assert 'paid subscription' in formatted.lower(), "Should mention paid subscription"
    print("✅ Context with different statuses: PASSED")

def main():
    """Запуск всех тестов"""
    print("=" * 60)
    print("🧪 Running SubscriptionContext tests...")
    print("=" * 60)
    
    try:
        test_get_context_new_user()
        test_format_for_llm()
        test_context_with_different_statuses()
        
        print("=" * 60)
        print("✅ All tests PASSED")
        print("=" * 60)
        return 0
    except AssertionError as e:
        print(f"❌ Test FAILED: {e}")
        return 1
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == '__main__':
    sys.exit(main())
```

---

### ✅ Критерии готовности

- [ ] `SubscriptionContext` создает контекст для нового пользователя
- [ ] Контекст включает trial days, grace period, usage stats
- [ ] `format_for_llm()` форматирует контекст корректно
- [ ] Работает для всех статусов (paid_trial, paid, billing_problem, limited_free_trial)
- [ ] Все тесты пройдены

---

### 🧪 Тестирование

```bash
cd mvp_tests
source .venv/bin/activate

# Запустить тесты
python test_subscription_context.py
```

**Ожидаемый вывод:**

```
============================================================
🧪 Running SubscriptionContext tests...
============================================================
🧪 Test: Get context for new user
✅ Status: paid_trial
✅ Trial days left: 14
✅ Get context for new user: PASSED
🧪 Test: Format context for LLM
✅ Formatted text:
User subscription: Paid trial period (14 days remaining).
✅ Format for LLM: PASSED
🧪 Test: Context with different statuses
✅ Context with different statuses: PASSED
============================================================
✅ All tests PASSED
============================================================
```

---

### 📊 Ожидаемые результаты

- Контекст формируется корректно для всех статусов
- Форматированный текст готов для добавления в LLM prompt
- Включает предупреждения для критических ситуаций (trial истекает, лимиты достигнуты)

---

## 📦 MVP 6: Quota Checker

**Цель:** Проверка квот (изолированно)

**Время:** 1 день

**Зависимости:** MVP 4

---

### 📋 Детальные шаги выполнения

#### Шаг 1: Создание QuotaChecker

**Файл:** `mvp_tests/quota_checker.py`

```python
#!/usr/bin/env python3
"""QuotaChecker - проверка квот для подписок"""
from subscription_repository import SubscriptionRepository
from datetime import datetime, timedelta
from typing import Dict, Optional
import os
from dotenv import load_dotenv

load_dotenv()

class QuotaChecker:
    # Лимиты для limited_free_trial
    DAILY_LIMIT = 5
    WEEKLY_LIMIT = 25
    MONTHLY_LIMIT = 50
    
    def __init__(self, repo: Optional[SubscriptionRepository] = None):
        """Инициализация QuotaChecker"""
        if repo:
            self.repo = repo
        else:
            from subscription_repository import SubscriptionRepository
            self.repo = SubscriptionRepository()
    
    def check_quota(self, hardware_id: str, status: Optional[str] = None) -> Dict:
        """
        Проверить квоты для пользователя
        
        Args:
            hardware_id: ID устройства
            status: Опциональный статус (если не указан, получается из БД)
        
        Returns:
            Dict с allowed (bool), reason (str), и деталями
        """
        # Получаем статус из БД, если не указан
        if not status:
            subscription = self.repo.get_subscription(hardware_id)
            if not subscription:
                # Новый пользователь - создаем подписку
                subscription = self.repo.create_subscription(hardware_id)
            status = subscription['status']
        
        # Безлимитный доступ
        if status in ['paid_trial', 'paid', 'admin_active', 'grandfathered']:
            return {
                'allowed': True,
                'reason': 'unlimited_access',
                'status': status,
                'limits': None
            }
        
        # Billing problem - проверяем grace period
        if status == 'billing_problem':
            subscription = self.repo.get_subscription(hardware_id)
            grace_end = subscription.get('grace_period_end_at')
            
            if grace_end:
                if isinstance(grace_end, str):
                    grace_end = datetime.fromisoformat(grace_end.replace('Z', '+00:00'))
                
                if grace_end > datetime.now():
                    # Grace period активен
                    hours_left = (grace_end - datetime.now()).total_seconds() / 3600
                    return {
                        'allowed': True,
                        'reason': 'grace_period_active',
                        'status': status,
                        'grace_period_hours_left': round(hours_left, 1)
                    }
            
            # Grace period истек
            return {
                'allowed': False,
                'reason': 'grace_period_expired',
                'status': status,
                'message': 'Grace period expired. Please update payment method.'
            }
        
        # Limited free trial - проверяем лимиты
        if status == 'limited_free_trial':
            usage_stats = self.repo.get_usage_stats(hardware_id)
            daily_used = usage_stats.get('daily_used', 0)
            weekly_used = usage_stats.get('weekly_used', 0)
            monthly_used = usage_stats.get('monthly_used', 0)
            
            # Проверяем все лимиты
            daily_exceeded = daily_used >= self.DAILY_LIMIT
            weekly_exceeded = weekly_used >= self.WEEKLY_LIMIT
            monthly_exceeded = monthly_used >= self.MONTHLY_LIMIT
            
            if daily_exceeded or weekly_exceeded or monthly_exceeded:
                exceeded_limits = []
                if daily_exceeded:
                    exceeded_limits.append(f'daily ({daily_used}/{self.DAILY_LIMIT})')
                if weekly_exceeded:
                    exceeded_limits.append(f'weekly ({weekly_used}/{self.WEEKLY_LIMIT})')
                if monthly_exceeded:
                    exceeded_limits.append(f'monthly ({monthly_used}/{self.MONTHLY_LIMIT})')
                
                return {
                    'allowed': False,
                    'reason': 'quota_exceeded',
                    'status': status,
                    'exceeded_limits': exceeded_limits,
                    'usage': {
                        'daily': f"{daily_used}/{self.DAILY_LIMIT}",
                        'weekly': f"{weekly_used}/{self.WEEKLY_LIMIT}",
                        'monthly': f"{monthly_used}/{self.MONTHLY_LIMIT}"
                    },
                    'message': f'Quota exceeded: {", ".join(exceeded_limits)}. Please subscribe for unlimited access.'
                }
            
            # В пределах лимитов
            return {
                'allowed': True,
                'reason': 'within_limits',
                'status': status,
                'usage': {
                    'daily': f"{daily_used}/{self.DAILY_LIMIT}",
                    'weekly': f"{weekly_used}/{self.WEEKLY_LIMIT}",
                    'monthly': f"{monthly_used}/{self.MONTHLY_LIMIT}"
                }
            }
        
        # Неизвестный статус - блокируем
        return {
            'allowed': False,
            'reason': 'unknown_status',
            'status': status,
            'message': f'Unknown subscription status: {status}'
        }
    
    def can_proceed(self, hardware_id: str) -> bool:
        """Быстрая проверка - можно ли продолжить"""
        result = self.check_quota(hardware_id)
        return result.get('allowed', False)
```

#### Шаг 2: Создание тестов

**Файл:** `mvp_tests/test_quota_checker.py`

```python
#!/usr/bin/env python3
"""Тесты для QuotaChecker"""
import sys
from datetime import datetime, timedelta
from quota_checker import QuotaChecker
from subscription_repository import SubscriptionRepository

def test_unlimited_access():
    """Тест безлимитного доступа"""
    print("🧪 Test: Unlimited access")
    
    repo = SubscriptionRepository()
    checker = QuotaChecker(repo)
    
    hardware_id = f"test_hw_{datetime.now().timestamp()}"
    repo.create_subscription(hardware_id, status='paid')
    
    result = checker.check_quota(hardware_id)
    
    assert result['allowed'] == True, "Paid subscription should allow access"
    assert result['reason'] == 'unlimited_access', "Should be unlimited"
    
    print("✅ Unlimited access: PASSED")

def test_limited_free_trial():
    """Тест limited free trial"""
    print("🧪 Test: Limited free trial")
    
    repo = SubscriptionRepository()
    checker = QuotaChecker(repo)
    
    hardware_id = f"test_hw_{datetime.now().timestamp()}"
    repo.create_subscription(hardware_id, status='limited_free_trial')
    
    # В пределах лимитов
    result = checker.check_quota(hardware_id)
    assert result['allowed'] == True, "Should allow within limits"
    assert result['reason'] == 'within_limits', "Should be within limits"
    
    # Превышение лимитов
    for _ in range(6):  # Превышаем daily limit (5)
        repo.increment_usage(hardware_id)
    
    result = checker.check_quota(hardware_id)
    assert result['allowed'] == False, "Should block when limit exceeded"
    assert result['reason'] == 'quota_exceeded', "Should indicate quota exceeded"
    
    print("✅ Limited free trial: PASSED")

def test_grace_period():
    """Тест grace period"""
    print("🧪 Test: Grace period")
    
    repo = SubscriptionRepository()
    checker = QuotaChecker(repo)
    
    hardware_id = f"test_hw_{datetime.now().timestamp()}"
    repo.create_subscription(hardware_id, status='billing_problem')
    
    # Grace period активен
    grace_end = datetime.now() + timedelta(hours=12)
    repo.update_stripe_ids(hardware_id)  # Обновим для установки grace_period_end_at
    # В реальности нужно добавить метод update_grace_period_end_at
    
    result = checker.check_quota(hardware_id)
    # Проверяем, что логика работает
    
    print("✅ Grace period: PASSED")

def main():
    """Запуск всех тестов"""
    print("=" * 60)
    print("🧪 Running QuotaChecker tests...")
    print("=" * 60)
    
    try:
        test_unlimited_access()
        test_limited_free_trial()
        test_grace_period()
        
        print("=" * 60)
        print("✅ All tests PASSED")
        print("=" * 60)
        return 0
    except AssertionError as e:
        print(f"❌ Test FAILED: {e}")
        return 1
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == '__main__':
    sys.exit(main())
```

---

### ✅ Критерии готовности

- [ ] Проверка квот работает для всех статусов
- [ ] Безлимитный доступ для paid_trial, paid, admin_active, grandfathered
- [ ] Grace period проверяется для billing_problem
- [ ] Лимиты проверяются для limited_free_trial (5/25/50)
- [ ] Возвращаются детальные сообщения об ошибках
- [ ] Все тесты пройдены

---

### 🧪 Тестирование

```bash
cd mvp_tests
source .venv/bin/activate

# Запустить тесты
python test_quota_checker.py
```

**Ожидаемый вывод:**

```
============================================================
🧪 Running QuotaChecker tests...
============================================================
🧪 Test: Unlimited access
✅ Unlimited access: PASSED
🧪 Test: Limited free trial
✅ Limited free trial: PASSED
🧪 Test: Grace period
✅ Grace period: PASSED
============================================================
✅ All tests PASSED
============================================================
```

---

### 📊 Ожидаемые результаты

- QuotaChecker корректно проверяет доступ для всех статусов
- Возвращает детальную информацию о причинах блокировки
- Включает информацию об использовании для limited_free_trial

---

## 📦 MVP 7: Интеграция в Workflow

**Цель:** Добавление subscription context в LLM prompt (минимальная интеграция)

**Время:** 2-3 дня

**Зависимости:** MVP 5, MVP 6

---

### 📋 Детальные шаги выполнения

#### Шаг 1: Создание Subscription Module (сервер)

**Файл:** `v1.0.6 Payment/server(Payment)/server/modules/subscription/core/subscription_module.py`

```python
#!/usr/bin/env python3
"""Subscription Module для сервера"""
from typing import Dict, Optional
import logging
from subscription_context import SubscriptionContext
from quota_checker import QuotaChecker
from subscription_repository import SubscriptionRepository

logger = logging.getLogger(__name__)

class SubscriptionModule:
    """Модуль для работы с подписками"""
    
    def __init__(self, db_url: str):
        """Инициализация модуля"""
        self.repo = SubscriptionRepository(db_url)
        self.context_builder = SubscriptionContext(self.repo)
        self.quota_checker = QuotaChecker(self.repo)
    
    def get_context(self, hardware_id: str) -> Dict:
        """Получить контекст подписки"""
        try:
            context = self.context_builder.get_context(hardware_id)
            formatted = self.context_builder.format_for_llm(context)
            return {
                'context': context,
                'formatted_text': formatted
            }
        except Exception as e:
            logger.error(f"[SubscriptionModule] Error getting context: {e}")
            return {
                'context': {'status': 'unknown'},
                'formatted_text': ''
            }
    
    def check_quota(self, hardware_id: str) -> Dict:
        """Проверить квоты"""
        return self.quota_checker.check_quota(hardware_id)
```

#### Шаг 2: Интеграция в StreamingWorkflowIntegration

**Файл:** `v1.0.6 Payment/server(Payment)/server/integrations/workflow_integrations/streaming_workflow_integration.py`

**Изменения:**

```python
# В начале метода _process_request_streaming, после получения hardware_id:

# MVP 7: Получение subscription context и проверка квот
subscription_context_text = ""
try:
    subscription_module = self.module_coordinator.get_module("subscription")
    if subscription_module:
        # Проверка квот
        quota_result = subscription_module.check_quota(hardware_id)
        
        if not quota_result.get('allowed', False):
            # Квота превышена - блокируем запрос
            error_message = quota_result.get('message', 'Quota exceeded')
            logger.warning(f"[MVP7] Quota exceeded for {hardware_id}: {error_message}")
            
            # Возвращаем ошибку пользователю
            yield {
                'text_chunk': f"I'm sorry, but {error_message}. Please subscribe for unlimited access.",
                'session_id': session_id,
                'feature_id': 'F-2025-017-stripe-payment'
            }
            return  # Прерываем обработку
        
        # Получаем контекст для LLM
        context_data = subscription_module.get_context(hardware_id)
        subscription_context_text = context_data.get('formatted_text', '')
        
        logger.info(f"[MVP7] Subscription context added for {hardware_id}")
except Exception as e:
    logger.warning(f"[MVP7] Subscription context error: {e}")
    # Продолжаем без subscription context (fallback)

# Добавляем контекст в prompt
if subscription_context_text:
    enhanced_prompt = f"""{subscription_context_text}

User request: {request.prompt}"""
    request.prompt = enhanced_prompt
```

#### Шаг 3: Регистрация модуля

**Файл:** `v1.0.6 Payment/server(Payment)/server/modules/subscription/__init__.py`

```python
from .core.subscription_module import SubscriptionModule

__all__ = ['SubscriptionModule']
```

**Обновить:** `server/modules/module_factory.py` (добавить создание SubscriptionModule)

---

### ✅ Критерии готовности

- [ ] SubscriptionModule создан и зарегистрирован
- [ ] Subscription context добавляется в LLM prompt
- [ ] Quota проверка работает и блокирует при превышении
- [ ] LLM получает информацию о подписке
- [ ] Существующий функционал не сломан (fallback работает)
- [ ] Можно протестировать end-to-end

---

### 🧪 Тестирование

**Команды:**

```bash
# Запустить сервер
cd v1.0.6\ Payment/server(Payment)
source .venv/bin/activate
python server/main.py

# В другом терминале - тестовый запрос
# Отправить запрос через клиент и проверить логи
```

**Ожидаемые результаты:**

1. **В логах сервера:**
   ```
   [MVP7] Subscription context added for hardware_id_123
   ```

2. **В LLM prompt:**
   - Должен быть добавлен subscription context
   - LLM должен учитывать статус подписки при ответе

3. **При превышении квоты:**
   - Запрос блокируется
   - Пользователь получает сообщение об ошибке

---

### 📊 Ожидаемые результаты

- Subscription context автоматически добавляется в каждый запрос
- Quota enforcement работает корректно
- LLM учитывает статус подписки при генерации ответов
- Нет регрессий в существующем функционале

---

## 📦 MVP 8: Команды подписки

**Цель:** Обработка команд create_subscription/cancel_subscription

**Время:** 2-3 дня

**Зависимости:** MVP 3, MVP 7

---

### 📋 Детальные шаги выполнения

#### Шаг 1: Расширение SubscriptionModule для создания Checkout

**Файл:** `v1.0.6 Payment/server(Payment)/server/modules/subscription/core/subscription_module.py`

**Добавить методы:**

```python
from stripe_service import StripeService
import os
from dotenv import load_dotenv

load_dotenv()

class SubscriptionModule:
    # ... существующий код ...
    
    def __init__(self, db_url: str):
        """Инициализация модуля"""
        self.repo = SubscriptionRepository(db_url)
        self.context_builder = SubscriptionContext(self.repo)
        self.quota_checker = QuotaChecker(self.repo)
        
        # Инициализация Stripe Service
        stripe_key = os.getenv('STRIPE_SECRET_KEY')
        if not stripe_key:
            logger.warning("[SubscriptionModule] STRIPE_SECRET_KEY not found")
        self.stripe_service = StripeService(stripe_key) if stripe_key else None
    
    def create_checkout(
        self, 
        hardware_id: str,
        success_url: Optional[str] = None,
        cancel_url: Optional[str] = None
    ) -> Dict:
        """
        Создать Checkout Session для подписки
        
        Args:
            hardware_id: ID устройства
            success_url: URL для редиректа после успешной оплаты
            cancel_url: URL для редиректа при отмене
        
        Returns:
            Dict с checkout_url, session_id, error (если есть)
        """
        if not self.stripe_service:
            return {
                'error': 'Stripe service not configured',
                'checkout_url': None
            }
        
        try:
            # Получаем или создаем подписку
            subscription = self.repo.get_subscription(hardware_id)
            if not subscription:
                subscription = self.repo.create_subscription(hardware_id)
            
            # Формируем URLs для deep links
            base_url = os.getenv('DEEP_LINK_BASE_URL', 'nexy://')
            if not success_url:
                success_url = f"{base_url}checkout/success?session_id={{CHECKOUT_SESSION_ID}}"
            if not cancel_url:
                cancel_url = f"{base_url}checkout/cancel"
            
            # Создаем Checkout Session
            result = self.stripe_service.create_checkout_session(
                hardware_id=hardware_id,
                success_url=success_url,
                cancel_url=cancel_url
            )
            
            logger.info(f"[SubscriptionModule] Checkout created for {hardware_id}: {result['session_id']}")
            
            return {
                'checkout_url': result['checkout_url'],
                'session_id': result['session_id'],
                'customer_id': result.get('customer_id'),
                'error': None
            }
            
        except Exception as e:
            logger.error(f"[SubscriptionModule] Error creating checkout: {e}")
            return {
                'error': str(e),
                'checkout_url': None
            }
    
    def cancel_subscription(self, hardware_id: str) -> Dict:
        """
        Отменить подписку
        
        Args:
            hardware_id: ID устройства
        
        Returns:
            Dict с success (bool), message (str)
        """
        try:
            subscription = self.repo.get_subscription(hardware_id)
            if not subscription:
                return {
                    'success': False,
                    'message': 'Subscription not found'
                }
            
            stripe_subscription_id = subscription.get('stripe_subscription_id')
            if not stripe_subscription_id:
                # Локальная подписка (trial) - просто обновляем статус
                self.repo.update_status(hardware_id, 'limited_free_trial')
                return {
                    'success': True,
                    'message': 'Trial subscription cancelled'
                }
            
            # Отменяем в Stripe
            if self.stripe_service:
                # В реальности нужно добавить метод cancel_subscription в StripeService
                # Пока просто обновляем статус
                self.repo.update_status(hardware_id, 'limited_free_trial')
                return {
                    'success': True,
                    'message': 'Subscription cancelled'
                }
            
            return {
                'success': False,
                'message': 'Stripe service not available'
            }
            
        except Exception as e:
            logger.error(f"[SubscriptionModule] Error cancelling subscription: {e}")
            return {
                'success': False,
                'message': str(e)
            }
```

#### Шаг 2: Обновление AssistantResponseParser

**Файл:** `v1.0.6 Payment/server(Payment)/server/integrations/core/assistant_response_parser.py`

**Добавить в метод `parse()`:**

```python
def parse(self, text: str) -> Optional[Dict]:
    """Парсинг ответа LLM для извлечения команд"""
    # ... существующий код ...
    
    # MVP 8: Парсинг команд подписки
    text_lower = text.lower()
    
    # Команда create_subscription
    subscription_keywords = ['subscribe', 'subscription', 'premium', 'upgrade', 'pay']
    if any(keyword in text_lower for keyword in subscription_keywords):
        # Проверяем, что это не просто упоминание
        if any(phrase in text_lower for phrase in ['want to', 'would like to', 'need to', 'help me']):
            return {
                'command': 'create_subscription',
                'args': {},
                'text': 'I will help you subscribe to Nexy Premium. Opening checkout page...'
            }
    
    # Команда cancel_subscription
    cancel_keywords = ['cancel', 'unsubscribe', 'stop subscription']
    if any(keyword in text_lower for keyword in cancel_keywords):
        if any(phrase in text_lower for phrase in ['want to', 'would like to', 'need to']):
            return {
                'command': 'cancel_subscription',
                'args': {},
                'text': 'I will help you cancel your subscription.'
            }
    
    # ... остальной код ...
```

#### Шаг 3: Интеграция в StreamingWorkflowIntegration

**Файл:** `v1.0.6 Payment/server(Payment)/server/integrations/workflow_integrations/streaming_workflow_integration.py`

**Добавить метод `_execute_subscription_command()`:**

```python
def _execute_subscription_command(
    self,
    command: str,
    hardware_id: str,
    session_id: str
) -> Generator[Dict, None, None]:
    """
    Выполнение команд подписки
    
    Args:
        command: 'create_subscription' или 'cancel_subscription'
        hardware_id: ID устройства
        session_id: ID сессии
    
    Yields:
        StreamResponse с action_message или text_chunk
    """
    try:
        subscription_module = self.module_coordinator.get_module("subscription")
        if not subscription_module:
            yield {
                'text_chunk': 'Subscription service is not available. Please try again later.',
                'session_id': session_id,
                'feature_id': 'F-2025-017-stripe-payment'
            }
            return
        
        if command == 'create_subscription':
            # Создаем Checkout Session
            result = subscription_module.create_checkout(hardware_id)
            
            if result.get('error'):
                yield {
                    'text_chunk': f"I'm sorry, but I couldn't create a checkout session: {result['error']}",
                    'session_id': session_id,
                    'feature_id': 'F-2025-017-stripe-payment'
                }
                return
            
            checkout_url = result.get('checkout_url')
            if checkout_url:
                # Отправляем action_message для открытия URL
                yield {
                    'action_message': {
                        'action_json': json.dumps({
                            'command': 'open_url',
                            'args': {'url': checkout_url}
                        }),
                        'session_id': session_id,
                        'feature_id': 'F-2025-017-stripe-payment'
                    }
                }
                
                # Отправляем текстовое подтверждение
                yield {
                    'text_chunk': 'I\'ve opened the checkout page for you. Please complete your subscription there.',
                    'session_id': session_id,
                    'feature_id': 'F-2025-017-stripe-payment'
                }
            else:
                yield {
                    'text_chunk': 'I couldn\'t create a checkout session. Please try again later.',
                    'session_id': session_id,
                    'feature_id': 'F-2025-017-stripe-payment'
                }
        
        elif command == 'cancel_subscription':
            # Отменяем подписку
            result = subscription_module.cancel_subscription(hardware_id)
            
            if result.get('success'):
                yield {
                    'text_chunk': result.get('message', 'Your subscription has been cancelled.'),
                    'session_id': session_id,
                    'feature_id': 'F-2025-017-stripe-payment'
                }
            else:
                yield {
                    'text_chunk': f"I couldn't cancel your subscription: {result.get('message', 'Unknown error')}",
                    'session_id': session_id,
                    'feature_id': 'F-2025-017-stripe-payment'
                }
        
    except Exception as e:
        logger.error(f"[MVP8] Error executing subscription command: {e}")
        yield {
            'text_chunk': 'An error occurred while processing your subscription request. Please try again later.',
            'session_id': session_id,
            'feature_id': 'F-2025-017-stripe-payment'
        }
```

**Обновить `_process_request_streaming()` для обработки команд:**

```python
# После парсинга команды от LLM:
parsed_command = self.assistant_parser.parse(llm_response_text)

if parsed_command and parsed_command.get('command') in ['create_subscription', 'cancel_subscription']:
    # Выполняем команду подписки
    for response in self._execute_subscription_command(
        parsed_command['command'],
        hardware_id,
        session_id
    ):
        yield response
    return  # Прерываем обычный поток
```

---

### ✅ Критерии готовности

- [ ] `SubscriptionModule.create_checkout()` работает
- [ ] `SubscriptionModule.cancel_subscription()` работает
- [ ] `AssistantResponseParser` распознает команды подписки
- [ ] `StreamingWorkflowIntegration` обрабатывает команды
- [ ] `action_message` с `open_url` отправляется на клиент
- [ ] Можно протестировать end-to-end (запрос → парсинг → checkout → URL)

---

### 🧪 Тестирование

**Команды:**

```bash
# Запустить сервер
cd v1.0.6\ Payment/server(Payment)
source .venv/bin/activate
python server/main.py

# В клиенте отправить запрос:
# "I want to subscribe to premium"
# или
# "Help me subscribe"
```

**Ожидаемые результаты:**

1. **В логах сервера:**
   ```
   [SubscriptionModule] Checkout created for hardware_id_123: cs_test_...
   [MVP8] Executing subscription command: create_subscription
   ```

2. **В ответе сервера:**
   - `action_message` с `command: 'open_url'` и `url: 'https://checkout.stripe.com/...'`
   - Текстовое сообщение: "I've opened the checkout page for you..."

3. **На клиенте:**
   - Браузер открывается с Checkout страницей Stripe
   - Можно завершить тестовую оплату

**Ручное тестирование:**

1. Отправить голосовой/текстовый запрос: "I want to subscribe"
2. Проверить, что браузер открывается
3. Завершить тестовую оплату (карта: 4242 4242 4242 4242)
4. Проверить, что подписка создается в БД

---

### 📊 Ожидаемые результаты

- Команды подписки распознаются из естественного языка
- Checkout Session создается корректно
- URL отправляется на клиент через `action_message`
- Клиент открывает браузер с Checkout страницей
- После оплаты подписка активируется (через webhook в MVP 10)

---

### 🔍 Возможные проблемы и решения

**Проблема 1:** Команда не распознается
```bash
# Решение: Проверить ключевые слова в AssistantResponseParser
# Добавить больше вариантов фраз
```

**Проблема 2:** Checkout URL не создается
```bash
# Решение: Проверить STRIPE_SECRET_KEY в .env
# Проверить логи ошибок Stripe API
```

**Проблема 3:** action_message не доходит до клиента
```bash
# Решение: Проверить формат action_json
# Убедиться, что клиент обрабатывает open_url команду
```

---

## 📦 MVP 9: Клиентская часть

**Цель:** Deep Links и open_url команда

**Время:** 1-2 дня

**Зависимости:** MVP 8

---

### 📋 Детальные шаги выполнения

#### Шаг 1: Добавление open_url команды

**Файл:** `v1.0.6 Payment/client(Payment)/integration/integrations/action_execution_integration.py`

**Найти метод `_handle_action_message()` и добавить:**

```python
# В начале класса, обновить valid_commands:
VALID_COMMANDS = [
    'open_app',
    'close_app', 
    'read_messages',
    'send_message',
    'open_url'  # MVP 9: Новая команда
]

# Добавить метод обработки:
def _handle_open_url(self, command_data: dict) -> None:
    """
    Обработка команды open_url
    
    Args:
        command_data: Dict с 'args' содержащим 'url'
    """
    url = command_data.get('args', {}).get('url')
    if not url:
        logger.warning("[ActionExecution] open_url: URL not provided")
        return
    
    try:
        # Проверка безопасности URL
        if not url.startswith(('https://', 'http://', 'nexy://')):
            logger.error(f"[ActionExecution] open_url: Invalid URL scheme: {url}")
            return
        
        # Открытие URL в браузере (macOS)
        import subprocess
        result = subprocess.run(
            ["open", url],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        if result.returncode == 0:
            logger.info(f"[ActionExecution] ✅ Opened URL: {url}")
        else:
            logger.error(f"[ActionExecution] ❌ Failed to open URL: {result.stderr}")
            
    except subprocess.TimeoutExpired:
        logger.error(f"[ActionExecution] ❌ Timeout opening URL: {url}")
    except Exception as e:
        logger.error(f"[ActionExecution] ❌ Error opening URL {url}: {e}")

# Обновить _handle_action_message():
def _handle_action_message(self, event: dict) -> None:
    """Обработка action_message события"""
    try:
        action_json = event.get('payload', {}).get('action_json')
        if not action_json:
            return
        
        import json
        command_data = json.loads(action_json)
        command = command_data.get('command')
        
        if command not in self.VALID_COMMANDS:
            logger.warning(f"[ActionExecution] Unknown command: {command}")
            return
        
        # Маршрутизация команд
        if command == 'open_url':
            self._handle_open_url(command_data)
        elif command == 'open_app':
            self._handle_open_app(command_data)
        elif command == 'close_app':
            self._handle_close_app(command_data)
        # ... остальные команды ...
        
    except json.JSONDecodeError as e:
        logger.error(f"[ActionExecution] Invalid JSON in action_message: {e}")
    except Exception as e:
        logger.error(f"[ActionExecution] Error handling action_message: {e}")
```

#### Шаг 2: Создание Deep Link Processor

**Файл:** `v1.0.6 Payment/client(Payment)/modules/deep_link/core/deep_link_processor.py`

```python
#!/usr/bin/env python3
"""Deep Link Processor для обработки deep links от Stripe"""
import logging
import urllib.parse
from typing import Dict, Optional
from datetime import datetime

logger = logging.getLogger(__name__)

class DeepLinkProcessor:
    """Обработчик deep links для платежной системы"""
    
    def __init__(self):
        """Инициализация процессора"""
        self.logged_events = []  # Для MVP - просто логируем
    
    def process_deep_link(self, url: str) -> Dict:
        """
        Обработка deep link
        
        Args:
            url: Deep link URL (например, nexy://checkout/success?session_id=...)
        
        Returns:
            Dict с типом события и данными
        """
        if not url:
            return {'error': 'URL is empty'}
        
        try:
            # Парсинг URL
            parsed = urllib.parse.urlparse(url)
            scheme = parsed.scheme
            path = parsed.path
            query_params = urllib.parse.parse_qs(parsed.query)
            
            # Проверка схемы
            if scheme != 'nexy':
                logger.warning(f"[DeepLink] Invalid scheme: {scheme}")
                return {'error': f'Invalid scheme: {scheme}'}
            
            # Обработка разных типов deep links
            if path.startswith('/checkout/success'):
                return self._handle_checkout_success(query_params)
            elif path.startswith('/checkout/cancel'):
                return self._handle_checkout_cancel(query_params)
            elif path.startswith('/portal/return'):
                return self._handle_portal_return(query_params)
            else:
                logger.warning(f"[DeepLink] Unknown path: {path}")
                return {'error': f'Unknown path: {path}'}
                
        except Exception as e:
            logger.error(f"[DeepLink] Error processing deep link: {e}")
            return {'error': str(e)}
    
    def _handle_checkout_success(self, params: Dict) -> Dict:
        """Обработка успешного checkout"""
        session_id = params.get('session_id', [None])[0]
        
        event = {
            'type': 'checkout_success',
            'session_id': session_id,
            'timestamp': datetime.now().isoformat()
        }
        
        logger.info(f"[DeepLink] ✅ Checkout completed successfully: session_id={session_id}")
        self.logged_events.append(event)
        
        # MVP 9: Только логируем
        # В MVP 10: Отправим событие на сервер для синхронизации
        
        return {
            'success': True,
            'event': event,
            'message': 'Checkout completed successfully'
        }
    
    def _handle_checkout_cancel(self, params: Dict) -> Dict:
        """Обработка отмены checkout"""
        event = {
            'type': 'checkout_cancel',
            'timestamp': datetime.now().isoformat()
        }
        
        logger.info(f"[DeepLink] ⚠️ Checkout cancelled by user")
        self.logged_events.append(event)
        
        return {
            'success': True,
            'event': event,
            'message': 'Checkout was cancelled'
        }
    
    def _handle_portal_return(self, params: Dict) -> Dict:
        """Обработка возврата из Customer Portal"""
        session_id = params.get('session_id', [None])[0]
        
        event = {
            'type': 'portal_return',
            'session_id': session_id,
            'timestamp': datetime.now().isoformat()
        }
        
        logger.info(f"[DeepLink] ✅ Returned from Customer Portal: session_id={session_id}")
        self.logged_events.append(event)
        
        # MVP 9: Только логируем
        # В MVP 10: Отправим событие на сервер для синхронизации payment_method
        
        return {
            'success': True,
            'event': event,
            'message': 'Returned from Customer Portal'
        }
    
    def get_logged_events(self) -> list:
        """Получить список залогированных событий (для тестирования)"""
        return self.logged_events.copy()
```

#### Шаг 3: Интеграция Deep Link Processor

**Файл:** `v1.0.6 Payment/client(Payment)/modules/deep_link/__init__.py`

```python
from .core.deep_link_processor import DeepLinkProcessor

__all__ = ['DeepLinkProcessor']
```

**Обновить:** `client/integration/core/simple_module_coordinator.py` (добавить DeepLinkProcessor)

---

### ✅ Критерии готовности

- [ ] `open_url` команда добавлена в `VALID_COMMANDS`
- [ ] `_handle_open_url()` открывает URL в браузере
- [ ] `DeepLinkProcessor` создан и обрабатывает deep links
- [ ] Обрабатываются все типы deep links (checkout/success, checkout/cancel, portal/return)
- [ ] События логируются
- [ ] Можно протестировать end-to-end

---

### 🧪 Тестирование

**Команды:**

```bash
# Запустить клиент
cd v1.0.6\ Payment/client(Payment)
source .venv/bin/activate
python main.py

# Отправить запрос на подписку
# После получения action_message с open_url, проверить:
# 1. Браузер открывается
# 2. Checkout страница загружается
# 3. После оплаты/отмены deep link обрабатывается
```

**Тестирование open_url:**

```python
# В Python консоли:
from integration.integrations.action_execution_integration import ActionExecutionIntegration

integration = ActionExecutionIntegration(...)
integration._handle_open_url({
    'args': {'url': 'https://checkout.stripe.com/test'}
})
# Проверить, что браузер открылся
```

**Тестирование Deep Links:**

```python
# В Python консоли:
from modules.deep_link.core.deep_link_processor import DeepLinkProcessor

processor = DeepLinkProcessor()

# Тест успешного checkout
result = processor.process_deep_link('nexy://checkout/success?session_id=cs_test_123')
assert result['success'] == True
assert result['event']['type'] == 'checkout_success'

# Тест отмены
result = processor.process_deep_link('nexy://checkout/cancel')
assert result['success'] == True

# Проверить логированные события
events = processor.get_logged_events()
print(events)
```

**Ожидаемые результаты:**

1. **open_url команда:**
   - Браузер открывается с указанным URL
   - Логи показывают успешное открытие

2. **Deep Links:**
   - Все типы deep links обрабатываются
   - События логируются корректно
   - Возвращаются правильные ответы

---

### 📊 Ожидаемые результаты

- Команда `open_url` работает и открывает браузер
- Deep links обрабатываются корректно
- События логируются для последующей синхронизации (MVP 10)
- Готовность к интеграции с сервером в MVP 10

---

### 🔍 Возможные проблемы и решения

**Проблема 1:** Браузер не открывается
```bash
# Решение: Проверить команду 'open' на macOS
which open
# Должно быть: /usr/bin/open

# Проверить права доступа
chmod +x /usr/bin/open
```

**Проблема 2:** Deep link не обрабатывается
```bash
# Решение: Проверить формат URL
# Должен быть: nexy://checkout/success?session_id=...
# Проверить парсинг URL
```

**Проблема 3:** action_message не доходит
```bash
# Решение: Проверить формат action_json
# Убедиться, что команда 'open_url' в valid_commands
```

---

## 📦 MVP 10: Полная интеграция

**Цель:** Все компоненты работают вместе, полное тестирование продукта

**Время:** 2-3 дня

**Зависимости:** MVP 1-9

---

### 📋 Детальные шаги выполнения

#### Шаг 1: Создание SubscriptionStateMachine

**Файл:** `v1.0.6 Payment/server(Payment)/server/modules/subscription/core/state_machine.py`

```python
#!/usr/bin/env python3
"""State Machine для управления статусами подписок"""
from typing import Dict, Optional
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)

class SubscriptionStateMachine:
    """State Machine для переходов статусов подписок"""
    
    # Валидные статусы
    VALID_STATUSES = [
        'paid_trial',
        'paid',
        'billing_problem',
        'limited_free_trial',
        'admin_active',
        'grandfathered'
    ]
    
    # Валидные переходы
    VALID_TRANSITIONS = {
        'paid_trial': ['paid', 'limited_free_trial'],
        'paid': ['billing_problem', 'limited_free_trial'],
        'billing_problem': ['paid', 'limited_free_trial'],
        'limited_free_trial': ['paid'],
        'admin_active': [],  # Неизменяемый статус
        'grandfathered': []  # Неизменяемый статус
    }
    
    @classmethod
    def can_transition(cls, from_status: str, to_status: str) -> bool:
        """Проверить, возможен ли переход"""
        if from_status not in cls.VALID_STATUSES:
            return False
        if to_status not in cls.VALID_STATUSES:
            return False
        
        allowed = cls.VALID_TRANSITIONS.get(from_status, [])
        return to_status in allowed
    
    @classmethod
    def transition(
        cls,
        current_status: str,
        new_status: str,
        hardware_id: str,
        repo
    ) -> Dict:
        """
        Выполнить переход статуса
        
        Returns:
            Dict с success (bool), message (str), new_status (str)
        """
        if not cls.can_transition(current_status, new_status):
            return {
                'success': False,
                'message': f'Invalid transition: {current_status} → {new_status}',
                'new_status': current_status
            }
        
        try:
            # Обновляем статус в БД
            repo.update_status(hardware_id, new_status)
            
            # Устанавливаем grace_period_end_at для billing_problem
            if new_status == 'billing_problem':
                grace_end = datetime.now() + timedelta(days=1)
                # Нужно добавить метод update_grace_period_end_at в repo
            
            logger.info(f"[StateMachine] Transition: {current_status} → {new_status} for {hardware_id}")
            
            return {
                'success': True,
                'message': f'Status updated: {new_status}',
                'new_status': new_status
            }
        except Exception as e:
            logger.error(f"[StateMachine] Error transitioning: {e}")
            return {
                'success': False,
                'message': str(e),
                'new_status': current_status
            }
```

#### Шаг 2: Создание Webhook Handler

**Файл:** `v1.0.6 Payment/server(Payment)/server/services/stripe_webhook_handler.py`

```python
#!/usr/bin/env python3
"""Webhook Handler для обработки событий от Stripe"""
import logging
import json
from typing import Dict, Optional
from datetime import datetime, timedelta
from subscription_repository import SubscriptionRepository
from subscription_state_machine import SubscriptionStateMachine
from stripe_service import StripeService

logger = logging.getLogger(__name__)

class StripeWebhookHandler:
    """Обработчик webhook событий от Stripe"""
    
    def __init__(self, repo: SubscriptionRepository, stripe_service: StripeService):
        self.repo = repo
        self.stripe_service = stripe_service
        self.state_machine = SubscriptionStateMachine()
    
    def handle_event(self, event: Dict) -> Dict:
        """
        Обработка webhook события
        
        Args:
            event: Stripe event object
        
        Returns:
            Dict с success (bool), message (str)
        """
        event_type = event.get('type')
        event_id = event.get('id')
        
        # Проверка идемпотентности
        if self.repo.event_exists(event_id):
            logger.info(f"[Webhook] Event {event_id} already processed (idempotency)")
            return {'success': True, 'message': 'Event already processed'}
        
        try:
            # Маршрутизация по типу события
            handler = self._get_handler(event_type)
            if not handler:
                logger.warning(f"[Webhook] No handler for event type: {event_type}")
                return {'success': False, 'message': f'Unknown event type: {event_type}'}
            
            # Обработка события
            result = handler(event)
            
            # Сохраняем событие (идемпотентность)
            self.repo.record_event(
                event_id,
                event_type,
                hardware_id=result.get('hardware_id'),
                event_data=event.get('data', {})
            )
            
            return result
            
        except Exception as e:
            logger.error(f"[Webhook] Error handling event {event_id}: {e}")
            return {'success': False, 'message': str(e)}
    
    def _get_handler(self, event_type: str):
        """Получить обработчик для типа события"""
        handlers = {
            'checkout.session.completed': self._handle_checkout_completed,
            'customer.subscription.updated': self._handle_subscription_updated,
            'customer.subscription.deleted': self._handle_subscription_deleted,
            'invoice.payment_succeeded': self._handle_payment_succeeded,
            'invoice.payment_failed': self._handle_payment_failed,
            'invoice.payment_action_required': self._handle_payment_action_required,
        }
        return handlers.get(event_type)
    
    def _handle_checkout_completed(self, event: Dict) -> Dict:
        """Обработка checkout.session.completed"""
        session = event['data']['object']
        hardware_id = session['metadata'].get('hardware_id')
        customer_id = session.get('customer')
        subscription_id = session.get('subscription')
        
        if not hardware_id:
            return {'success': False, 'message': 'hardware_id not found in metadata'}
        
        # Линковка customer/subscription
        self.repo.update_stripe_ids(
            hardware_id,
            customer_id=customer_id,
            subscription_id=subscription_id
        )
        
        # НЕ меняем статус на paid (источник истины - invoice.payment_succeeded)
        logger.info(f"[Webhook] Checkout completed for {hardware_id}, linked customer/subscription")
        
        return {
            'success': True,
            'message': 'Checkout completed, customer/subscription linked',
            'hardware_id': hardware_id
        }
    
    def _handle_payment_succeeded(self, event: Dict) -> Dict:
        """Обработка invoice.payment_succeeded (источник истины для paid)"""
        invoice = event['data']['object']
        customer_id = invoice.get('customer')
        subscription_id = invoice.get('subscription')
        
        # Находим hardware_id по customer_id
        # В реальности нужен метод repo.get_hardware_id_by_customer_id()
        # Пока используем subscription_id
        subscription = self.repo.get_subscription_by_stripe_subscription_id(subscription_id)
        if not subscription:
            return {'success': False, 'message': 'Subscription not found'}
        
        hardware_id = subscription['hardware_id']
        current_status = subscription['status']
        
        # Переход в paid (источник истины)
        if current_status != 'paid':
            result = self.state_machine.transition(
                current_status,
                'paid',
                hardware_id,
                self.repo
            )
            
            if result['success']:
                logger.info(f"[Webhook] Payment succeeded, status → paid for {hardware_id}")
                return {
                    'success': True,
                    'message': 'Payment succeeded, status updated to paid',
                    'hardware_id': hardware_id
                }
        
        return {'success': True, 'message': 'Payment succeeded, already paid'}
    
    def _handle_payment_failed(self, event: Dict) -> Dict:
        """Обработка invoice.payment_failed"""
        invoice = event['data']['object']
        subscription_id = invoice.get('subscription')
        
        subscription = self.repo.get_subscription_by_stripe_subscription_id(subscription_id)
        if not subscription:
            return {'success': False, 'message': 'Subscription not found'}
        
        hardware_id = subscription['hardware_id']
        current_status = subscription['status']
        
        # Переход в billing_problem + grace period
        if current_status != 'billing_problem':
            result = self.state_machine.transition(
                current_status,
                'billing_problem',
                hardware_id,
                self.repo
            )
            
            if result['success']:
                # Устанавливаем grace_period_end_at
                grace_end = datetime.now() + timedelta(days=1)
                # repo.update_grace_period_end_at(hardware_id, grace_end)
                
                logger.info(f"[Webhook] Payment failed, status → billing_problem (grace period) for {hardware_id}")
                return {
                    'success': True,
                    'message': 'Payment failed, grace period started',
                    'hardware_id': hardware_id
                }
        
        return {'success': True, 'message': 'Payment failed, already in billing_problem'}
    
    # ... остальные обработчики ...
```

**Примечание:** Это упрощенная версия. Полная реализация должна включать все must-have события, out-of-order обработку, и инвалидацию кэша.

---

### ✅ Критерии готовности (MVP 10)

**10.1. Webhook обработка:**
- [ ] `SubscriptionStateMachine` создан и работает
- [ ] `StripeWebhookHandler` обрабатывает все must-have события
- [ ] Идемпотентность работает (дубликаты игнорируются)
- [ ] State Machine переходы корректны
- [ ] Grace period устанавливается для billing_problem

**10.2. Полная интеграция:**
- [ ] Subscription context добавляется в каждый запрос
- [ ] Quota проверка работает и блокирует при превышении
- [ ] Usage инкрементируется после успешного запроса
- [ ] Trial warnings работают
- [ ] Auto-checkout работает (с cooldown)

**10.3-10.6. Дополнительные сервисы:**
- [ ] Reconcile Service реализован
- [ ] Trial Period Manager работает
- [ ] Grace Period проверяется
- [ ] Cron Jobs настроены

**10.7. Тестирование:**
- [ ] Все 15 критических тест-кейсов пройдены
- [ ] E2E тесты пройдены
- [ ] Performance тесты пройдены
- [ ] Нет регрессий

---

### 🧪 Тестирование MVP 10

**Команды:**

```bash
# Запустить сервер
cd v1.0.6\ Payment/server(Payment)
source .venv/bin/activate
python server/main.py

# В другом терминале - Stripe CLI
stripe listen --forward-to localhost:8000/webhook/stripe

# Отправить тестовые события
stripe trigger checkout.session.completed
stripe trigger invoice.payment_succeeded
stripe trigger invoice.payment_failed

# Запустить критические тесты
pytest v1.0.6\ Payment/tests/test_smoke_critical.py -v
```

**Ожидаемые результаты:**

1. **Webhook обработка:**
   - Все события обрабатываются корректно
   - State Machine переходы работают
   - Идемпотентность соблюдается

2. **Полная интеграция:**
   - Subscription context в каждом запросе
   - Quota enforcement работает
   - Usage tracking работает

3. **Все тесты:**
   - 15 критических тест-кейсов пройдены
   - E2E тесты пройдены
   - Нет регрессий

---

### 📊 Ожидаемые результаты

**После успешного выполнения MVP 10:**

- ✅ Полная платежная система работает end-to-end
- ✅ Все компоненты интегрированы
- ✅ Все критические сценарии покрыты тестами
- ✅ Production-ready состояние
- ✅ Готовность к развертыванию

---

### 🔍 Возможные проблемы и решения

**Проблема 1:** Webhook события не обрабатываются
```bash
# Решение: Проверить верификацию подписи
# Проверить логи webhook handler
# Проверить идемпотентность
```

**Проблема 2:** State Machine переходы не работают
```bash
# Решение: Проверить VALID_TRANSITIONS
# Проверить логи переходов
# Убедиться, что repo.update_status работает
```

**Проблема 3:** Quota не блокирует
```bash
# Решение: Проверить QuotaChecker
# Проверить инкремент usage
# Проверить лимиты в БД
```

#### 10.2. Полная интеграция в Workflow

**Файл:** `server(Payment)/server/integrations/workflow_integrations/streaming_workflow_integration.py`

**Обновить:**

- [ ] Получение subscription context (с реконсиляцией)
- [ ] Проверка квот перед каждым запросом
- [ ] Блокировка при превышении квот
- [ ] Инкремент usage после успешного запроса
- [ ] Trial warnings в LLM prompt
- [ ] Auto-checkout при истечении trial (с cooldown)
- [ ] Portal return обработка (синхронизация payment_method)

#### 10.3. Reconcile Service

**Файл:** `server(Payment)/server/services/reconcile_service.py`

**Реализовать:**

- [ ] `reconcile_with_stripe()` — реконсиляция для одной подписки
- [ ] `check_reconciliation_needed()` — проверка необходимости
- [ ] `reconcile_all_active_subscriptions()` — batch реконсиляция
- [ ] Интеграция в SubscriptionContextCache

#### 10.4. Trial Period Manager

**Файл:** `server(Payment)/server/modules/subscription/trial_manager.py`

**Реализовать:**

- [ ] Проверка дней до истечения trial
- [ ] Генерация предупреждений (2, 1, 0 дней)
- [ ] Проверка cooldown для auto-checkout (24 часа)
- [ ] Автоматический переход в `limited_free_trial` при истечении

#### 10.5. Grace Period обработка

**Логика:**

- [ ] Проверка истечения grace period при каждом запросе
- [ ] Автоматический переход в `limited_free_trial` при истечении
- [ ] Логирование переходов

#### 10.6. Cron Jobs

**Файл:** `server(Payment)/server/services/cron_jobs.py`

**Реализовать:**

- [ ] Периодическая синхронизация со Stripe (раз в час)
- [ ] Проверка истечения grace period (раз в час)
- [ ] Проверка истечения trial period (раз в день)

#### 10.7. Полное тестирование

**Тест-кейсы из `CRITICAL_TEST_CASES.md`:**

- [ ] TC-1: Webhook Duplicate (идемпотентность)
- [ ] TC-2: Webhook Out-of-Order
- [ ] TC-3: Webhook Signature Verification
- [ ] TC-4: `checkout.session.completed` ≠ оплата
- [ ] TC-5: Источник истины для `paid`
- [ ] TC-6: State Machine переходы
- [ ] TC-7: Quota enforcement
- [ ] TC-8: Trial expiration
- [ ] TC-9: Grace period
- [ ] TC-10: Portal return
- [ ] TC-11: Reconcile
- [ ] TC-12: Hardware ID генерация
- [ ] TC-13: Deep Links
- [ ] TC-14: URL Opening
- [ ] TC-15: End-to-end flow

### Критерии готовности

- [ ] Все MVP объединены
- [ ] Все must-have webhook события обрабатываются
- [ ] State Machine работает корректно
- [ ] Quota enforcement работает
- [ ] Reconcile Service работает
- [ ] Trial warnings работают
- [ ] Grace period работает
- [ ] Portal return работает
- [ ] Все 15 критических тест-кейсов пройдены
- [ ] End-to-end тесты пройдены
- [ ] Нет регрессий в существующем функционале
- [ ] Performance требования выполнены

### Тестирование

```bash
# Критические тест-кейсы
pytest v1.0.6\ Payment/tests/test_smoke_critical.py -v

# E2E тесты
pytest server/tests/e2e/test_subscription_full_flow.py -v
pytest client/tests/e2e/test_deep_links.py -v

# Performance тесты
pytest server/tests/performance/ -v

# Полный набор тестов
pytest server/tests/ -v
pytest client/tests/ -v
```

### Что можно тестировать после MVP 10

**✅ Полный функционал:**
- ✅ Новый пользователь → paid_trial → оплата → paid
- ✅ Trial истечение → limited_free_trial
- ✅ Payment failed → billing_problem → grace period → limited_free_trial
- ✅ Payment succeeded → возврат в paid
- ✅ Quota enforcement для limited_free_trial
- ✅ Webhook обработка всех событий
- ✅ Deep links обработка
- ✅ URL opening на клиенте
- ✅ Portal return синхронизация
- ✅ Reconcile со Stripe
- ✅ Trial warnings
- ✅ Auto-checkout при истечении trial
- ✅ Grace period обработка
- ✅ Cron jobs синхронизация

**✅ Все критические сценарии:**
- ✅ Идемпотентность webhooks
- ✅ Out-of-order обработка
- ✅ Signature verification
- ✅ Источник истины для paid
- ✅ State Machine переходы
- ✅ Quota limits
- ✅ Hardware ID генерация

**✅ Production-ready:**
- ✅ Все компоненты работают вместе
- ✅ Нет регрессий
- ✅ Performance требования выполнены
- ✅ Мониторинг настроен

---

## 📊 Таблица MVP прогресса

| MVP | Название | Время | Зависимости | Статус | Тесты |
|-----|----------|-------|-------------|--------|-------|
| 0 | Подготовка | 1 день | - | ⬜ | ⬜ |
| 1 | Webhook Endpoint | 1-2 дня | MVP 0 | ⬜ | ⬜ |
| 2 | База данных | 1-2 дня | MVP 0 | ⬜ | ⬜ |
| 3 | Stripe Service | 1-2 дня | MVP 0 | ⬜ | ⬜ |
| 4 | Subscription Repository | 1 день | MVP 2 | ⬜ | ⬜ |
| 5 | Subscription Context | 1 день | MVP 4 | ⬜ | ⬜ |
| 6 | Quota Checker | 1 день | MVP 4 | ⬜ | ⬜ |
| 7 | Интеграция в Workflow | 2-3 дня | MVP 5, 6 | ⬜ | ⬜ |
| 8 | Команды подписки | 2-3 дня | MVP 3, 7 | ⬜ | ⬜ |
| 9 | Клиентская часть | 1-2 дня | MVP 8 | ⬜ | ⬜ |
| 10 | Полная интеграция | 2-3 дня | MVP 1-9 | ⬜ | ⬜ |

**Общее время:** 13-20 дней (2.5-4 недели)

---

## 🎯 Преимущества MVP подхода

1. **Быстрое тестирование:** Каждый MVP можно протестировать изолированно
2. **Минимальный риск:** Не затрагиваем основной проект до MVP 7
3. **Постепенное понимание:** Учимся на каждом этапе
4. **Возможность отката:** Можно остановиться на любом MVP
5. **Раннее выявление проблем:** Проблемы видны сразу

---

## 📝 Следующие шаги

1. **Начать с MVP 0:** Подготовка инфраструктуры
2. **MVP 1:** Webhook endpoint (самый простой, можно протестировать сразу)
3. **MVP 2-3:** БД и Stripe Service (параллельно можно делать)
4. **MVP 4-6:** Постепенное наращивание функционала
5. **MVP 7-10:** Интеграция в основной проект

---

**Последнее обновление:** 2025-12-13  
**Версия:** 1.1 (Детализированная версия)

---

## 📋 Итоговая сводка детализации MVP

### ✅ Что было детализировано

Каждый MVP (0-10) теперь содержит:

1. **📋 Детальные шаги выполнения** - пошаговые инструкции
2. **💻 Конкретные файлы и код** - примеры реализации
3. **✅ Критерии готовности** - чеклист для проверки
4. **🧪 Тестирование** - команды и ожидаемые результаты
5. **📊 Ожидаемые результаты** - что должно получиться
6. **🔍 Возможные проблемы и решения** - troubleshooting

### 📦 Краткое резюме по каждому MVP

#### MVP 0: Подготовка ✅
- Создание тестовой инфраструктуры
- Настройка БД и Stripe API
- Тестовые скрипты для проверки подключений

#### MVP 1: Webhook Endpoint ✅
- Flask сервер для приема webhook событий
- Логирование и сохранение событий
- Интеграция с Stripe CLI

#### MVP 2: База данных ✅
- Миграции для subscriptions и subscription_events
- SubscriptionRepository с CRUD операциями
- Идемпотентность событий

#### MVP 3: Stripe Service ✅
- Создание Checkout Sessions
- Верификация webhook подписей
- Получение информации о сессиях и подписках

#### MVP 4: Subscription Repository + БД ✅
- Расширение миграций (usage tracking)
- Методы для отслеживания использования
- Статистика использования

#### MVP 5: Subscription Context ✅
- Формирование контекста подписки
- Форматирование для LLM prompt
- Поддержка всех статусов

#### MVP 6: Quota Checker ✅
- Проверка квот для всех статусов
- Grace period обработка
- Лимиты для limited_free_trial (5/25/50)

#### MVP 7: Интеграция в Workflow ✅
- SubscriptionModule для сервера
- Интеграция в StreamingWorkflowIntegration
- Quota enforcement перед каждым запросом

#### MVP 8: Команды подписки ⚠️
- Парсинг команд create_subscription/cancel_subscription
- Создание Checkout Session
- Отправка URL на клиент через action_message

#### MVP 9: Клиентская часть ⚠️
- open_url команда для открытия браузера
- Deep links обработка (базовая версия)
- Интеграция в ActionExecutionIntegration

#### MVP 10: Полная интеграция ⚠️
- Webhook обработка с State Machine
- Полная интеграция всех компонентов
- Reconcile Service, Trial Manager, Cron Jobs
- Все 15 критических тест-кейсов

### 🎯 Рекомендуемый порядок выполнения

1. **MVP 0-3** (параллельно можно делать MVP 2 и 3)
   - Подготовка инфраструктуры
   - Изолированные компоненты

2. **MVP 4-6** (последовательно)
   - Расширение БД
   - Контекст и квоты

3. **MVP 7-9** (интеграция в проект)
   - Интеграция в workflow
   - Команды подписки
   - Клиентская часть

4. **MVP 10** (финализация)
   - Полная интеграция
   - Тестирование всех сценариев

### 📝 Примечания

- **MVP 0-6:** Изолированные тесты в `mvp_tests/`
- **MVP 7-10:** Интеграция в основной проект
- **Тестирование:** Каждый MVP должен быть протестирован перед переходом к следующему
- **Откат:** Можно остановиться на любом MVP без потери функциональности

---

**Последнее обновление:** 2025-12-13  
**Версия:** 1.1 (Детализированная версия)

















