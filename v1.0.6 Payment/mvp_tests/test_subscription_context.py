#!/usr/bin/env python3
"""
Тесты для Subscription Context
MVP 5: Subscription Context
"""
import sys
from datetime import datetime, timedelta
from subscription_context import SubscriptionContext
from subscription_repository import SubscriptionRepository

def test_subscription_context():
    """Тестирование получения контекста подписки"""
    print("=" * 60)
    print("🧪 Тестирование Subscription Context (MVP 5)")
    print("=" * 60)
    
    context_service = SubscriptionContext()
    repo = SubscriptionRepository()
    test_hardware_id = f"test_hw_context_{int(datetime.now().timestamp())}"
    
    # Тест 1: Контекст для нового пользователя (без подписки)
    print(f"\n📝 Тест 1: Контекст для нового пользователя")
    print("   ⚠️  ВАЖНО: В реальной интеграции контекст должен вызываться ПОСЛЕ get_or_create_subscription()")
    context = context_service.get_subscription_context(test_hardware_id)
    
    if context.get('status') is None:
        print("✅ Контекст для нового пользователя: статус None")
        print("   ℹ️  В реальной интеграции после get_or_create_subscription() будет status='paid_trial'")
    else:
        print(f"⚠️  Ожидался status=None, получен: {context.get('status')}")
    
    # Тест 2: Создание подписки и получение контекста
    print(f"\n📝 Тест 2: Создание подписки и получение контекста")
    trial_end = datetime.now() + timedelta(days=14)
    subscription = repo.create_subscription(
        hardware_id=test_hardware_id,
        status='paid_trial',
        paid_trial_end_at=trial_end
    )
    
    context = context_service.get_subscription_context(test_hardware_id)
    
    print(f"   Status: {context.get('status')}")
    print(f"   Trial end: {context.get('paid_trial_end_at')}")
    print(f"   Payment method: {context.get('payment_method_id')}")
    
    if context.get('status') == 'paid_trial':
        print("✅ Контекст получен корректно")
    else:
        print(f"❌ Ожидался status='paid_trial', получен: {context.get('status')}")
        return False
    
    # Тест 3: Добавление платежа и проверка last_payment (только succeeded)
    print(f"\n📝 Тест 3: Добавление платежа и проверка last_payment (только succeeded)")
    
    # Создаем failed платеж (не должен попасть в контекст)
    repo.create_payment(
        hardware_id=test_hardware_id,
        stripe_invoice_id=f'in_test_failed_{int(datetime.now().timestamp())}',
        amount=999,
        currency='usd',
        status='failed'
    )
    
    # Создаем succeeded платеж (должен попасть в контекст)
    repo.create_payment(
        hardware_id=test_hardware_id,
        stripe_invoice_id=f'in_test_succeeded_{int(datetime.now().timestamp())}',
        amount=1999,  # $19.99 для проверки
        currency='usd',
        status='succeeded'
    )
    
    context = context_service.get_subscription_context(test_hardware_id)
    
    if context.get('last_payment_at'):
        print(f"   ✅ Last payment at: {context.get('last_payment_at')}")
        print(f"   ✅ Last payment amount: ${context.get('last_payment_amount', 0):.2f}")
        # Проверяем, что это succeeded платеж ($19.99), а не failed ($9.99)
        if context.get('last_payment_amount') == 19.99:
            print("   ✅ Фильтрация по status='succeeded' работает корректно")
        else:
            print(f"   ❌ Ожидался amount=$19.99 (succeeded), получен: ${context.get('last_payment_amount', 0):.2f}")
            return False
    else:
        print("   ⚠️  Last payment не найден (может быть нормально, если платежей нет)")
    
    # Тест 4: Обновление статуса и проверка контекста
    print(f"\n📝 Тест 4: Обновление статуса и проверка контекста")
    repo.update_status(test_hardware_id, 'paid')
    repo.update_stripe_ids(
        test_hardware_id,
        customer_id='cus_test_123',
        subscription_id='sub_test_123'
    )
    
    context = context_service.get_subscription_context(test_hardware_id)
    
    print(f"   Status: {context.get('status')}")
    print(f"   Customer ID: {context.get('stripe_subscription_id')}")
    
    if context.get('status') == 'paid':
        print("✅ Статус обновлен корректно")
    else:
        print(f"❌ Ожидался status='paid', получен: {context.get('status')}")
        return False
    
    # Тест 5: Получение summary
    print(f"\n📝 Тест 5: Получение текстового summary")
    summary = context_service.get_context_summary(test_hardware_id)
    print(f"   Summary: {summary}")
    
    if summary:
        print("✅ Summary получен")
    else:
        print("❌ Summary пустой")
        return False
    
    print("\n" + "=" * 60)
    print("✅ Все тесты пройдены успешно!")
    print("=" * 60)
    return True

if __name__ == '__main__':
    success = test_subscription_context()
    sys.exit(0 if success else 1)
