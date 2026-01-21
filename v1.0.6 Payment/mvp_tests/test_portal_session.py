#!/usr/bin/env python3
"""
Тест создания Portal Session через StripeService
MVP 10: Customer Portal

Запуск:
    cd mvp_tests
    source venv/bin/activate  # или .venv/bin/activate
    python test_portal_session.py
"""
import os
import sys
from dotenv import load_dotenv

# Добавляем путь к модулям
sys.path.insert(0, os.path.dirname(__file__))

load_dotenv()

from stripe_service import StripeService

def test_create_portal_session():
    """Тест создания Portal Session"""
    print("🧪 Тест создания Portal Session")
    print("=" * 60)
    
    # Проверяем наличие STRIPE_SECRET_KEY
    api_key = os.getenv('STRIPE_SECRET_KEY')
    if not api_key:
        print("❌ STRIPE_SECRET_KEY не найден в .env")
        return False
    
    try:
        # Создаем StripeService
        service = StripeService(api_key=api_key)
        print("✅ StripeService создан")
        
        # Для теста нужен валидный customer_id
        # Можно использовать существующий или создать новый
        test_customer_id = os.getenv('TEST_CUSTOMER_ID')
        if not test_customer_id:
            print("⚠️  TEST_CUSTOMER_ID не найден в .env")
            print("   Создаем тестового customer...")
            
            # Создаем тестового customer
            customer = service.create_customer(hardware_id="test_portal_hardware_id")
            test_customer_id = customer['customer_id']
            print(f"✅ Тестовый customer создан: {test_customer_id}")
        
        # Тестируем создание Portal Session
        print(f"\n📋 Создание Portal Session для customer: {test_customer_id}")
        result = service.create_portal_session(
            customer_id=test_customer_id,
            return_url="nexy://payment/portal_return"
        )
        
        # Проверяем результат
        assert 'portal_url' in result, "portal_url должен быть в результате"
        assert result['portal_url'].startswith('https://billing.stripe.com/'), \
            f"portal_url должен начинаться с https://billing.stripe.com/, получен: {result['portal_url']}"
        
        print(f"✅ Portal Session создан успешно")
        print(f"   Portal URL: {result['portal_url'][:50]}...")
        print(f"   Session ID: {result.get('session_id', 'N/A')}")
        
        return True
        
    except Exception as e:
        print(f"❌ Ошибка при создании Portal Session: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_create_portal_session()
    sys.exit(0 if success else 1)

