"""
Фикстуры для smoke-тестов платежной системы
"""
import pytest
import json
import time
from datetime import datetime, timedelta, timezone
from typing import Dict, Any, Optional
from unittest.mock import Mock, MagicMock, patch

# Stripe опционален (используется только в комментариях)
try:
    import stripe
except ImportError:
    stripe = None  # Для тестов не критично


# ============================================================================
# Моки для БД и кэша
# ============================================================================

class MockDB:
    """Мок базы данных для тестов"""
    
    def __init__(self):
        self.subscriptions: Dict[str, Dict] = {}
        self.subscription_events: Dict[str, Dict] = {}
        self.payments: list = []
        self.quota_usage: Dict[str, Dict] = {}
    
    def get_subscription(self, hardware_id: str) -> Optional[Dict]:
        return self.subscriptions.get(hardware_id)
    
    def create_subscription(self, hardware_id: str, data: Dict):
        self.subscriptions[hardware_id] = data.copy()
        return data
    
    def update_subscription(self, hardware_id: str, updates: Dict):
        if hardware_id in self.subscriptions:
            self.subscriptions[hardware_id].update(updates)
        return self.subscriptions.get(hardware_id)
    
    def insert_subscription_event(self, event_id: str, event_data: Dict) -> bool:
        """Возвращает True если вставлено, False если дубликат"""
        if event_id in self.subscription_events:
            return False  # Дубликат
        self.subscription_events[event_id] = {
            **event_data,
            'processed_at': datetime.now(timezone.utc)
        }
        return True
    
    def get_subscription_event(self, event_id: str) -> Optional[Dict]:
        return self.subscription_events.get(event_id)
    
    def create_payment(self, payment_data: Dict):
        self.payments.append(payment_data)
        return payment_data


class MockCache:
    """Мок кэша подписок"""
    
    def __init__(self):
        self._cache: Dict[str, Dict] = {}
        self._invalidated: set = set()
    
    def get(self, hardware_id: str) -> Optional[Dict]:
        if hardware_id in self._invalidated:
            return None  # Кэш промах
        return self._cache.get(hardware_id)
    
    def set(self, hardware_id: str, data: Dict, ttl: int = 30):
        self._cache[hardware_id] = data
        if hardware_id in self._invalidated:
            self._invalidated.remove(hardware_id)
    
    def invalidate(self, hardware_id: str):
        """Инвалидация кэша"""
        self._invalidated.add(hardware_id)
        if hardware_id in self._cache:
            del self._cache[hardware_id]
    
    def is_invalidated(self, hardware_id: str) -> bool:
        return hardware_id in self._invalidated


# ============================================================================
# Фикстуры
# ============================================================================

@pytest.fixture
def mock_db():
    """Фикстура для мока БД"""
    return MockDB()


@pytest.fixture
def mock_cache():
    """Фикстура для мока кэша"""
    return MockCache()


@pytest.fixture
def test_hardware_id():
    """Тестовый hardware_id"""
    return "test_hw_12345"


@pytest.fixture
def test_customer_id():
    """Тестовый Stripe customer_id"""
    return "cus_test123"


@pytest.fixture
def test_subscription_id():
    """Тестовый Stripe subscription_id"""
    return "sub_test123"


@pytest.fixture
def webhook_secret():
    """Тестовый webhook secret"""
    return "whsec_test_secret_12345"


# ============================================================================
# Хелперы для создания Stripe событий
# ============================================================================

def create_stripe_event(
    event_type: str,
    event_id: str,
    data: Dict[str, Any],
    created: Optional[int] = None
) -> Dict[str, Any]:
    """Создает структуру Stripe event"""
    if created is None:
        created = int(time.time())
    
    return {
        "id": event_id,
        "type": event_type,
        "created": created,
        "data": {
            "object": data
        }
    }


def create_checkout_completed_event(
    event_id: str,
    customer_id: str,
    subscription_id: str
) -> Dict[str, Any]:
    """Создает checkout.session.completed event"""
    return create_stripe_event(
        "checkout.session.completed",
        event_id,
        {
            "id": f"cs_{event_id}",
            "customer": customer_id,
            "subscription": subscription_id,
            "payment_status": "paid"
        }
    )


def create_invoice_payment_succeeded_event(
    event_id: str,
    customer_id: str,
    subscription_id: str,
    amount: int = 999
) -> Dict[str, Any]:
    """Создает invoice.payment_succeeded event"""
    return create_stripe_event(
        "invoice.payment_succeeded",
        event_id,
        {
            "id": f"in_{event_id}",
            "customer": customer_id,
            "subscription": subscription_id,
            "amount_paid": amount,
            "currency": "usd",
            "status": "paid"
        }
    )


def create_invoice_payment_failed_event(
    event_id: str,
    customer_id: str,
    subscription_id: str
) -> Dict[str, Any]:
    """Создает invoice.payment_failed event"""
    return create_stripe_event(
        "invoice.payment_failed",
        event_id,
        {
            "id": f"in_{event_id}",
            "customer": customer_id,
            "subscription": subscription_id,
            "amount_due": 999,
            "currency": "usd",
            "status": "open"
        }
    )


def create_subscription_updated_event(
    event_id: str,
    customer_id: str,
    subscription_id: str,
    status: str = "active"
) -> Dict[str, Any]:
    """Создает customer.subscription.updated event"""
    return create_stripe_event(
        "customer.subscription.updated",
        event_id,
        {
            "id": subscription_id,
            "customer": customer_id,
            "status": status,
            "current_period_end": int((datetime.now(timezone.utc) + timedelta(days=30)).timestamp()),
            "cancel_at_period_end": False
        }
    )


def sign_stripe_webhook(payload: bytes, secret: str) -> str:
    """Создает валидную подпись для Stripe webhook (упрощенная версия для тестов)"""
    # В реальности используется stripe.Webhook.construct_event
    # Для тестов мы можем использовать мок
    import hmac
    import hashlib
    timestamp = str(int(time.time()))
    signed_payload = f"{timestamp}.{payload.decode()}"
    signature = hmac.new(
        secret.encode(),
        signed_payload.encode(),
        hashlib.sha256
    ).hexdigest()
    return f"t={timestamp},v1={signature}"

