#!/usr/bin/env python3
"""
Тест для проверки доступности методов оплаты в Stripe Checkout

Проверяет, что в Checkout Session доступны:
1. Карта (card)
2. Stripe Link (link)
3. Apple Pay (автоматически, если включен в Dashboard)
"""
import os
import sys
from dotenv import load_dotenv

# Добавляем путь к модулям
sys.path.insert(0, os.path.dirname(__file__))

load_dotenv()

def test_payment_methods():
    """Проверить, что все методы оплаты доступны в Checkout"""
    print("=" * 60)
    print("🧪 Тест методов оплаты в Stripe Checkout")
    print("=" * 60)
    
    # Проверяем наличие STRIPE_SECRET_KEY
    api_key = os.getenv('STRIPE_SECRET_KEY')
    if not api_key:
        print("❌ STRIPE_SECRET_KEY не найден в .env")
        print("⚠️  Тест пропущен (нужен реальный Stripe ключ)")
        return False
    
    try:
        from stripe_service import StripeService
        import stripe
        
        # Создаем StripeService
        service = StripeService(api_key=api_key)
        print("✅ StripeService создан")
        
        # Параметры для тестового Checkout
        hardware_id = 'test_payment_methods'
        success_url = 'nexy://payment/checkout/success?session_id={CHECKOUT_SESSION_ID}'
        cancel_url = 'nexy://payment/checkout/cancel'
        
        print(f"\n📋 Создание тестового Checkout Session...")
        print(f"   Hardware ID: {hardware_id}")
        
        # Создаем Checkout Session
        result = service.create_checkout_session(
            hardware_id=hardware_id,
            success_url=success_url,
            cancel_url=cancel_url
        )
        
        session_id = result.get('session_id')
        checkout_url = result.get('checkout_url')
        
        print(f"\n✅ Checkout Session создан:")
        print(f"   Session ID: {session_id}")
        print(f"   URL: {checkout_url}")
        
        # Получаем информацию о сессии из Stripe API
        print(f"\n🔍 Проверка методов оплаты в сессии...")
        session = stripe.checkout.Session.retrieve(session_id)
        
        # Проверяем payment_method_types
        payment_method_types = session.payment_method_types or []
        print(f"\n📋 Доступные методы оплаты в сессии:")
        for method in payment_method_types:
            print(f"   ✅ {method}")
        
        # Проверяем ожидаемые методы (card и link явно указаны)
        expected_methods = ['card', 'link']
        missing_methods = []
        
        for method in expected_methods:
            if method not in payment_method_types:
                missing_methods.append(method)
                print(f"   ❌ {method} - НЕ НАЙДЕН!")
            else:
                print(f"   ✅ {method} - найден")
        
        # Информация об Apple Pay (активируется автоматически)
        print(f"\n🍎 Apple Pay:")
        print(f"   ℹ️  Apple Pay НЕ указывается в payment_method_types")
        print(f"   ℹ️  Он активируется автоматически Stripe, если:")
        print(f"      - Включен в Stripe Dashboard (Settings → Payment methods)")
        print(f"      - Домен верифицирован (для production) или используется localhost")
        print(f"      - Открыто в Safari (или Chrome на macOS)")
        print(f"      - Apple Pay настроен на Mac и есть карта в Apple Wallet")
        
        # Итоговый результат
        print(f"\n" + "=" * 60)
        if missing_methods:
            print(f"❌ Тест НЕ ПРОЙДЕН:")
            print(f"   Отсутствуют методы: {', '.join(missing_methods)}")
            return False
        else:
            print(f"✅ Тест ПРОЙДЕН:")
            print(f"   Все явно указанные методы найдены: {', '.join(payment_method_types)}")
            print(f"   Apple Pay активируется автоматически (если включен в Dashboard)")
            print(f"\n🌐 Откройте URL в Safari для проверки Apple Pay:")
            print(f"   {checkout_url}")
            return True
        
    except ImportError as e:
        print(f"❌ Ошибка импорта: {e}")
        print(f"   Убедитесь, что все зависимости установлены")
        return False
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == '__main__':
    success = test_payment_methods()
    sys.exit(0 if success else 1)
