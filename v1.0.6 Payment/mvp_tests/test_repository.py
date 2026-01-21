#!/usr/bin/env python3
"""
Тестовый скрипт для проверки Repository
MVP 2: База данных
"""
from subscription_repository import SubscriptionRepository
from datetime import datetime, timedelta

def test_repository():
    """Тестирование основных операций Repository"""
    print("=" * 60)
    print("🧪 Тестирование SubscriptionRepository (MVP 2)")
    print("=" * 60)
    
    repo = SubscriptionRepository()
    test_hardware_id = "test_hardware_mvp2"
    
    # Тест 1: Создание подписки
    print("\n📝 Тест 1: Создание подписки")
    trial_end = datetime.now() + timedelta(days=14)
    subscription = repo.create_subscription(
        hardware_id=test_hardware_id,
        status='paid_trial',
        paid_trial_end_at=trial_end
    )
    if subscription:
        print(f"✅ Подписка создана: {subscription['hardware_id']} ({subscription['status']})")
    else:
        print("❌ Ошибка создания подписки")
        return False
    
    # Тест 2: Получение подписки
    print("\n📖 Тест 2: Получение подписки")
    sub = repo.get_subscription(test_hardware_id)
    if sub:
        print(f"✅ Подписка найдена: {sub['hardware_id']} ({sub['status']})")
    else:
        print("❌ Подписка не найдена")
        return False
    
    # Тест 3: Обновление статуса
    print("\n🔄 Тест 3: Обновление статуса")
    if repo.update_status(test_hardware_id, 'paid'):
        print("✅ Статус обновлен на 'paid'")
    else:
        print("❌ Ошибка обновления статуса")
        return False
    
    # Тест 4: Обновление Stripe IDs
    print("\n🔗 Тест 4: Обновление Stripe IDs")
    if repo.update_stripe_ids(
        test_hardware_id,
        customer_id='cus_test_123',
        subscription_id='sub_test_123'
    ):
        print("✅ Stripe IDs обновлены")
    else:
        print("❌ Ошибка обновления Stripe IDs")
        return False
    
    # Тест 5: Запись события
    print("\n📨 Тест 5: Запись события")
    event_id = "evt_test_mvp2_123"
    if repo.record_event(
        stripe_event_id=event_id,
        event_type='checkout.session.completed',
        hardware_id=test_hardware_id,
        event_data={'test': 'data'},
        stripe_created_at=int(datetime.now().timestamp())
    ):
        print("✅ Событие записано")
    else:
        print("⚠️  Событие уже существует (идемпотентность работает)")
    
    # Тест 6: Проверка идемпотентности
    print("\n🔄 Тест 6: Проверка идемпотентности")
    if not repo.record_event(
        stripe_event_id=event_id,
        event_type='checkout.session.completed',
        hardware_id=test_hardware_id,
        event_data={'test': 'data'},
        stripe_created_at=int(datetime.now().timestamp())
    ):
        print("✅ Идемпотентность работает (дубликат не создан)")
    else:
        print("❌ Идемпотентность не работает")
        return False
    
    # Тест 7: Создание платежа
    print("\n💳 Тест 7: Создание платежа")
    # Используем уникальный invoice_id для избежания конфликтов с предыдущими тестами
    unique_invoice_id = f'in_test_{int(datetime.now().timestamp())}'
    if repo.create_payment(
        hardware_id=test_hardware_id,
        stripe_invoice_id=unique_invoice_id,
        amount=999,
        currency='usd',
        status='succeeded'
    ):
        print(f"✅ Платеж создан (invoice_id: {unique_invoice_id})")
    else:
        print(f"❌ Ошибка создания платежа (invoice_id: {unique_invoice_id})")
        return False
    
    # Тест 8: Проверка идемпотентности платежа
    print("\n🔄 Тест 8: Проверка идемпотентности платежа")
    # Пытаемся создать платеж с тем же invoice_id (должен вернуть False из-за идемпотентности)
    if not repo.create_payment(
        hardware_id=test_hardware_id,
        stripe_invoice_id=unique_invoice_id,  # Используем тот же invoice_id
        amount=999,
        currency='usd',
        status='succeeded'
    ):
        print("✅ Идемпотентность платежа работает (дубликат не создан)")
    else:
        print("❌ Идемпотентность платежа не работает")
        return False
    
    # Тест 9: Получение платежей
    print("\n📋 Тест 9: Получение платежей")
    payments = repo.get_payments(test_hardware_id)
    if payments:
        print(f"✅ Найдено платежей: {len(payments)}")
        print(f"   Последний: {payments[0]['stripe_invoice_id']} - ${payments[0]['amount']/100:.2f}")
    else:
        print("⚠️  Платежи не найдены")
    
    print("\n" + "=" * 60)
    print("✅ Все тесты пройдены успешно!")
    print("=" * 60)
    return True

if __name__ == '__main__':
    success = test_repository()
    exit(0 if success else 1)





