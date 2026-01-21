#!/usr/bin/env python3
"""
Тесты для Webhook Handler
MVP 6: Webhook Handler
"""
import sys
import json
from datetime import datetime, timedelta
from webhook_handler import WebhookHandler
from subscription_repository import SubscriptionRepository
from stripe_service import StripeService

def create_test_event(event_type: str, hardware_id: str, event_id: str = None, **kwargs) -> dict:
    """Создать тестовое событие Stripe"""
    if not event_id:
        event_id = f"evt_test_{event_type}_{int(datetime.now().timestamp() * 1000)}"
    base_event = {
        'id': event_id,
        'type': event_type,
        'created': int(datetime.now().timestamp()),
        'data': {
            'object': {}
        }
    }
    
    # Добавляем metadata с hardware_id в зависимости от типа события
    if event_type == 'checkout.session.completed':
        base_event['data']['object'] = {
            'id': 'cs_test_123',
            'customer': kwargs.get('customer_id', 'cus_test_123'),
            'subscription': kwargs.get('subscription_id', 'sub_test_123'),
            'metadata': {'hardware_id': hardware_id}
        }
    elif event_type.startswith('customer.subscription.'):
        base_event['data']['object'] = {
            'id': kwargs.get('subscription_id', 'sub_test_123'),
            'customer': kwargs.get('customer_id', 'cus_test_123'),
            'status': kwargs.get('stripe_status', 'active'),
            'current_period_end': kwargs.get('current_period_end', int((datetime.now() + timedelta(days=30)).timestamp())),
            'cancel_at_period_end': kwargs.get('cancel_at_period_end', False),
            'metadata': {'hardware_id': hardware_id}
        }
    elif event_type.startswith('invoice.'):
        base_event['data']['object'] = {
            'id': kwargs.get('invoice_id', 'in_test_123'),
            'customer': kwargs.get('customer_id', 'cus_test_123'),
            'subscription': kwargs.get('subscription_id', 'sub_test_123'),
            'amount_paid': kwargs.get('amount_paid', 999),
            'amount_due': kwargs.get('amount_due', kwargs.get('amount_paid', 999)),  # Для payment_failed используется amount_due
            'currency': kwargs.get('currency', 'usd')
        }
    
    return base_event

def test_checkout_completed():
    """Тест обработки checkout.session.completed"""
    print("\n📝 Тест 1: checkout.session.completed")
    
    repo = SubscriptionRepository()
    handler = WebhookHandler(repo)
    test_hardware_id = f"test_hw_checkout_{int(datetime.now().timestamp())}"
    
    # Создаем подписку
    repo.create_subscription(test_hardware_id, status='paid_trial')
    
    # Создаем событие
    event = create_test_event(
        'checkout.session.completed',
        test_hardware_id,
        customer_id='cus_test_123',
        subscription_id='sub_test_123'
    )
    
    # Обрабатываем событие
    result = handler.handle_event(event)
    
    assert result['success'], f"Event should be processed: {result.get('message')}"
    assert result['hardware_id'] == test_hardware_id, "hardware_id should match"
    
    # Проверяем, что customer/subscription связаны
    subscription = repo.get_subscription(test_hardware_id)
    assert subscription['stripe_customer_id'] == 'cus_test_123', "Customer ID should be linked"
    assert subscription['stripe_subscription_id'] == 'sub_test_123', "Subscription ID should be linked"
    
    # Проверяем, что статус НЕ изменился на paid (checkout ≠ оплата)
    assert subscription['status'] == 'paid_trial', "Status should remain paid_trial (not paid yet)"
    
    print("   ✅ Checkout completed: customer/subscription linked, status unchanged")
    return True

def test_payment_succeeded():
    """Тест обработки invoice.payment_succeeded"""
    print("\n📝 Тест 2: invoice.payment_succeeded")
    
    repo = SubscriptionRepository()
    handler = WebhookHandler(repo)
    test_hardware_id = f"test_hw_payment_{int(datetime.now().timestamp())}"
    test_customer_id = f"cus_test_{int(datetime.now().timestamp())}"
    test_subscription_id = f"sub_test_{int(datetime.now().timestamp())}"
    
    # Создаем подписку с customer/subscription
    repo.create_subscription(test_hardware_id, status='paid_trial')
    repo.update_stripe_ids(test_hardware_id, customer_id=test_customer_id, subscription_id=test_subscription_id)
    
    # Создаем событие (hardware_id будет восстановлен через subscription_id из БД)
    event = create_test_event(
        'invoice.payment_succeeded',
        test_hardware_id,  # Для справки, но будет восстановлен из БД
        event_id=f'evt_payment_{int(datetime.now().timestamp() * 1000)}',
        customer_id=test_customer_id,
        subscription_id=test_subscription_id,
        invoice_id=f'in_test_{int(datetime.now().timestamp())}',
        amount_paid=999
    )
    
    # Обрабатываем событие
    result = handler.handle_event(event)
    
    assert result['success'], f"Event should be processed: {result.get('message')}"
    assert result['hardware_id'] == test_hardware_id, "hardware_id should match"
    
    # Проверяем, что статус изменился на paid
    subscription = repo.get_subscription(test_hardware_id)
    assert subscription['status'] == 'paid', "Status should be paid"
    
    # Проверяем, что платеж сохранен
    payments = repo.get_payments(test_hardware_id, status='succeeded')
    assert len(payments) > 0, "Payment should be recorded"
    assert payments[0]['amount'] == 999, "Amount should match"
    
    # ⭐ КРИТИЧНО: Проверяем, что invoice.payment_succeeded обновил все поля
    subscription = repo.get_subscription(test_hardware_id)
    assert subscription['stripe_status'] == 'active', "stripe_status should be active"
    # grace_period_end_at должен быть NULL (очищен)
    assert subscription.get('grace_period_end_at') is None, "grace_period_end_at should be cleared"
    
    print("   ✅ Payment succeeded: status → paid, payment recorded, stripe_status=active, grace_period cleared")
    return True

def test_payment_failed():
    """Тест обработки invoice.payment_failed"""
    print("\n📝 Тест 3: invoice.payment_failed")
    
    repo = SubscriptionRepository()
    handler = WebhookHandler(repo)
    test_hardware_id = f"test_hw_failed_{int(datetime.now().timestamp())}"
    test_customer_id = f"cus_test_failed_{int(datetime.now().timestamp())}"
    test_subscription_id = f"sub_test_failed_{int(datetime.now().timestamp())}"
    
    # Создаем подписку со статусом paid
    repo.create_subscription(test_hardware_id, status='paid')
    repo.update_stripe_ids(test_hardware_id, customer_id=test_customer_id, subscription_id=test_subscription_id)
    
    # Создаем событие (hardware_id будет восстановлен через subscription_id из БД)
    test_invoice_id = f'in_test_failed_{int(datetime.now().timestamp())}'
    event = create_test_event(
        'invoice.payment_failed',
        test_hardware_id,
        event_id=f'evt_failed_{int(datetime.now().timestamp() * 1000)}',
        customer_id=test_customer_id,
        subscription_id=test_subscription_id,
        invoice_id=test_invoice_id,
        amount_due=999  # Для payment_failed используется amount_due
    )
    
    # Обрабатываем событие
    result = handler.handle_event(event)
    
    assert result['success'], f"Event should be processed: {result.get('message')}"
    
    # Проверяем, что статус изменился на billing_problem
    subscription = repo.get_subscription(test_hardware_id)
    assert subscription['status'] == 'billing_problem', "Status should be billing_problem"
    assert subscription['grace_period_end_at'] is not None, "Grace period should be set"
    
    # ⭐ КРИТИЧНО: Проверяем, что платеж сохранен в payments со статусом failed (для аудита)
    payments = repo.get_payments(test_hardware_id, status='failed')
    assert len(payments) > 0, "Failed payment should be recorded for audit"
    
    print("   ✅ Payment failed: status → billing_problem, grace period set, payment recorded (failed)")
    return True

def test_subscription_updated():
    """Тест обработки customer.subscription.updated"""
    print("\n📝 Тест 4: customer.subscription.updated")
    
    repo = SubscriptionRepository()
    handler = WebhookHandler(repo)
    test_hardware_id = f"test_hw_updated_{int(datetime.now().timestamp())}"
    test_customer_id = f"cus_test_updated_{int(datetime.now().timestamp())}"
    test_subscription_id = f"sub_test_updated_{int(datetime.now().timestamp())}"
    
    # Создаем подписку
    repo.create_subscription(test_hardware_id, status='paid_trial')
    repo.update_stripe_ids(test_hardware_id, customer_id=test_customer_id, subscription_id=test_subscription_id)
    
    # Создаем событие с active статусом
    event = create_test_event(
        'customer.subscription.updated',
        test_hardware_id,
        event_id=f'evt_updated_{int(datetime.now().timestamp() * 1000)}',
        customer_id=test_customer_id,
        subscription_id=test_subscription_id,
        stripe_status='active',
        current_period_end=int((datetime.now() + timedelta(days=30)).timestamp()),
        cancel_at_period_end=False
    )
    
    # Обрабатываем событие
    result = handler.handle_event(event)
    
    assert result['success'], f"Event should be processed: {result.get('message')}"
    
    # Проверяем, что stripe_status обновлен
    subscription = repo.get_subscription(test_hardware_id)
    assert subscription['stripe_status'] == 'active', "stripe_status should be active"
    
    # ⭐ КРИТИЧНО: Проверяем, что статус НЕ изменился на paid при active
    # (источник истины для paid - invoice.payment_succeeded)
    assert subscription['status'] == 'paid_trial', "Status should remain paid_trial (not changed to paid by subscription.updated)"
    
    print("   ✅ Subscription updated: stripe_status updated, status unchanged (not paid)")
    return True

def test_subscription_updated_past_due():
    """Тест обработки customer.subscription.updated с past_due (должен установить grace_period_end_at)"""
    print("\n📝 Тест 6: customer.subscription.updated (past_due → billing_problem)")
    
    repo = SubscriptionRepository()
    handler = WebhookHandler(repo)
    test_hardware_id = f"test_hw_past_due_{int(datetime.now().timestamp())}"
    test_customer_id = f"cus_test_past_due_{int(datetime.now().timestamp())}"
    test_subscription_id = f"sub_test_past_due_{int(datetime.now().timestamp())}"
    
    # Создаем подписку со статусом paid
    repo.create_subscription(test_hardware_id, status='paid')
    repo.update_stripe_ids(test_hardware_id, customer_id=test_customer_id, subscription_id=test_subscription_id)
    
    # Создаем событие с past_due статусом
    event = create_test_event(
        'customer.subscription.updated',
        test_hardware_id,
        event_id=f'evt_past_due_{int(datetime.now().timestamp() * 1000)}',
        customer_id=test_customer_id,
        subscription_id=test_subscription_id,
        stripe_status='past_due',
        current_period_end=int((datetime.now() + timedelta(days=30)).timestamp()),
        cancel_at_period_end=False
    )
    
    # Обрабатываем событие
    result = handler.handle_event(event)
    
    assert result['success'], f"Event should be processed: {result.get('message')}"
    
    # Проверяем, что статус изменился на billing_problem
    subscription = repo.get_subscription(test_hardware_id)
    assert subscription['status'] == 'billing_problem', "Status should be billing_problem"
    assert subscription['stripe_status'] == 'past_due', "stripe_status should be past_due"
    
    # ⭐ КРИТИЧНО: Проверяем, что grace_period_end_at установлен
    assert subscription['grace_period_end_at'] is not None, "grace_period_end_at should be set"
    
    print("   ✅ Subscription updated (past_due): status → billing_problem, grace_period_end_at set")
    return True

def test_idempotency():
    """Тест идемпотентности"""
    print("\n📝 Тест 5: Идемпотентность")
    
    repo = SubscriptionRepository()
    handler = WebhookHandler(repo)
    test_hardware_id = f"test_hw_idemp_{int(datetime.now().timestamp())}"
    
    # Создаем подписку
    repo.create_subscription(test_hardware_id, status='paid_trial')
    
    # Создаем событие
    test_customer_id = f'cus_test_idemp_{int(datetime.now().timestamp())}'
    test_subscription_id = f'sub_test_idemp_{int(datetime.now().timestamp())}'
    event_id = f'evt_idemp_{int(datetime.now().timestamp() * 1000)}'
    event = create_test_event(
        'checkout.session.completed',
        test_hardware_id,
        event_id=event_id,
        customer_id=test_customer_id,
        subscription_id=test_subscription_id
    )
    
    # Обрабатываем событие первый раз
    result1 = handler.handle_event(event)
    assert result1['success'], "First processing should succeed"
    
    # Обрабатываем событие второй раз (дубликат) - используем тот же event_id
    result2 = handler.handle_event(event)
    assert result2['success'], "Duplicate processing should succeed (idempotency)"
    assert 'already processed' in result2['message'].lower(), "Should indicate already processed"
    
    print("   ✅ Idempotency: duplicate event ignored")
    return True

def main():
    """Запуск всех тестов"""
    print("=" * 60)
    print("🧪 Тестирование Webhook Handler (MVP 6)")
    print("=" * 60)
    
    try:
        test_checkout_completed()
        test_payment_succeeded()
        test_payment_failed()
        test_subscription_updated()
        test_idempotency()
        test_subscription_updated_past_due()
        
        print("\n" + "=" * 60)
        print("✅ Все тесты пройдены успешно!")
        print("=" * 60)
        return 0
    except AssertionError as e:
        print(f"\n❌ Тест FAILED: {e}")
        import traceback
        traceback.print_exc()
        return 1
    except Exception as e:
        print(f"\n❌ Ошибка: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == '__main__':
    sys.exit(main())
