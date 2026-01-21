#!/usr/bin/env python3
"""
Тесты для State Machine переходов статусов подписок

Feature ID: F-2025-017-stripe-payment
"""
import sys
import os
from datetime import datetime, timedelta

# Добавляем путь к mvp_tests для импорта
sys.path.insert(0, os.path.dirname(__file__))

from state_machine import SubscriptionStateMachine
from subscription_repository import SubscriptionRepository


class MockRepository:
    """Mock репозиторий для тестирования State Machine"""
    
    def __init__(self):
        self.subscriptions = {}
        self.updates_called = []
    
    def update_subscription(self, hardware_id: str, **updates):
        """Сохранить обновления для проверки"""
        self.updates_called.append({
            'hardware_id': hardware_id,
            'updates': updates
        })
        if hardware_id not in self.subscriptions:
            self.subscriptions[hardware_id] = {}
        self.subscriptions[hardware_id].update(updates)
    
    def get_subscription(self, hardware_id: str):
        """Получить подписку"""
        return self.subscriptions.get(hardware_id, {})


def test_can_transition():
    """Тест проверки возможности переходов"""
    print("\n=== Тест: can_transition() ===")
    
    # Валидные переходы
    assert SubscriptionStateMachine.can_transition('paid_trial', 'paid') == True
    assert SubscriptionStateMachine.can_transition('paid_trial', 'limited_free_trial') == True
    assert SubscriptionStateMachine.can_transition('paid', 'billing_problem') == True
    assert SubscriptionStateMachine.can_transition('paid', 'limited_free_trial') == True
    assert SubscriptionStateMachine.can_transition('billing_problem', 'paid') == True
    assert SubscriptionStateMachine.can_transition('billing_problem', 'limited_free_trial') == True
    assert SubscriptionStateMachine.can_transition('limited_free_trial', 'paid') == True
    assert SubscriptionStateMachine.can_transition(None, 'paid_trial') == True  # Новый пользователь
    
    # Запрещенные переходы
    assert SubscriptionStateMachine.can_transition('limited_free_trial', 'paid_trial') == False
    assert SubscriptionStateMachine.can_transition('paid', 'paid_trial') == False
    assert SubscriptionStateMachine.can_transition('billing_problem', 'paid_trial') == False
    assert SubscriptionStateMachine.can_transition('admin_active', 'paid') == False
    assert SubscriptionStateMachine.can_transition('grandfathered', 'paid') == False
    
    # Недопустимые статусы
    assert SubscriptionStateMachine.can_transition('paid', 'invalid_status') == False
    assert SubscriptionStateMachine.can_transition('invalid_status', 'paid') == False
    
    print("✅ Все проверки can_transition() пройдены")


def test_transition_payment_succeeded():
    """Тест перехода при invoice.payment_succeeded"""
    print("\n=== Тест: transition() - invoice.payment_succeeded ===")
    
    repo = MockRepository()
    hardware_id = "test_hw_001"
    
    # Создаем подписку с paid_trial
    repo.subscriptions[hardware_id] = {'status': 'paid_trial'}
    
    # Переход в paid при payment_succeeded
    stripe_event_at = datetime.now()
    current_period_end = datetime.now() + timedelta(days=30)
    
    result = SubscriptionStateMachine.transition(
        hardware_id=hardware_id,
        from_status='paid_trial',
        to_status='paid',
        event_type='invoice.payment_succeeded',
        repository=repo,
        stripe_status='active',
        current_period_end=current_period_end,
        stripe_event_id='evt_test_123',
        stripe_event_at=stripe_event_at
    )
    
    assert result['success'] == True
    assert result['new_status'] == 'paid'
    assert len(repo.updates_called) == 1
    
    updates = repo.updates_called[0]['updates']
    assert updates['status'] == 'paid'
    assert updates['stripe_status'] == 'active'
    assert updates['grace_period_end_at'] is None
    assert updates['current_period_end'] == current_period_end
    assert 'last_stripe_event_id' in updates
    assert updates['last_stripe_event_id'] == 'evt_test_123'
    assert 'last_stripe_event_at' in updates
    
    print("✅ Переход paid_trial → paid при payment_succeeded работает")


def test_transition_payment_failed():
    """Тест перехода при invoice.payment_failed"""
    print("\n=== Тест: transition() - invoice.payment_failed ===")
    
    repo = MockRepository()
    hardware_id = "test_hw_002"
    
    # Создаем подписку с paid
    repo.subscriptions[hardware_id] = {'status': 'paid'}
    
    # Переход в billing_problem при payment_failed
    stripe_event_at = datetime.now()
    
    result = SubscriptionStateMachine.transition(
        hardware_id=hardware_id,
        from_status='paid',
        to_status='billing_problem',
        event_type='invoice.payment_failed',
        repository=repo,
        stripe_status='past_due',
        stripe_event_id='evt_test_456',
        stripe_event_at=stripe_event_at
    )
    
    assert result['success'] == True
    assert result['new_status'] == 'billing_problem'
    assert len(repo.updates_called) == 1
    
    updates = repo.updates_called[0]['updates']
    assert updates['status'] == 'billing_problem'
    assert updates['stripe_status'] == 'past_due'
    assert updates['grace_period_end_at'] is not None
    # Проверяем, что grace_period_end_at примерно через 1 день (допускаем небольшую погрешность)
    grace_end = updates['grace_period_end_at']
    assert isinstance(grace_end, datetime)
    days_diff = (grace_end - datetime.now()).days
    assert 0 <= days_diff <= 1, f"Expected grace_period_end_at to be ~1 day from now, got {days_diff} days"
    assert 'last_stripe_event_id' in updates
    assert updates['last_stripe_event_id'] == 'evt_test_456'
    
    print("✅ Переход paid → billing_problem при payment_failed работает")


def test_transition_subscription_deleted():
    """Тест перехода при customer.subscription.deleted"""
    print("\n=== Тест: transition() - customer.subscription.deleted ===")
    
    repo = MockRepository()
    hardware_id = "test_hw_003"
    
    # Создаем подписку с paid
    repo.subscriptions[hardware_id] = {
        'status': 'paid',
        'stripe_subscription_id': 'sub_test_123'
    }
    
    # Переход в limited_free_trial при subscription.deleted
    stripe_event_at = datetime.now()
    
    result = SubscriptionStateMachine.transition(
        hardware_id=hardware_id,
        from_status='paid',
        to_status='limited_free_trial',
        event_type='customer.subscription.deleted',
        repository=repo,
        stripe_status='deleted',
        stripe_event_id='evt_test_789',
        stripe_event_at=stripe_event_at
    )
    
    assert result['success'] == True
    assert result['new_status'] == 'limited_free_trial'
    assert len(repo.updates_called) == 1
    
    updates = repo.updates_called[0]['updates']
    assert updates['status'] == 'limited_free_trial'
    assert updates['stripe_status'] == 'deleted'
    assert updates['stripe_subscription_id'] is None
    assert 'last_stripe_event_id' in updates
    assert updates['last_stripe_event_id'] == 'evt_test_789'
    
    print("✅ Переход paid → limited_free_trial при subscription.deleted работает")


def test_transition_invalid():
    """Тест невалидного перехода"""
    print("\n=== Тест: transition() - невалидный переход ===")
    
    repo = MockRepository()
    hardware_id = "test_hw_004"
    
    # Создаем подписку с paid
    repo.subscriptions[hardware_id] = {'status': 'paid'}
    
    # Попытка невалидного перехода (paid → paid_trial запрещен)
    result = SubscriptionStateMachine.transition(
        hardware_id=hardware_id,
        from_status='paid',
        to_status='paid_trial',
        event_type='test_event',
        repository=repo
    )
    
    assert result['success'] == False
    assert 'error' in result
    assert result['new_status'] == 'paid'  # Статус не изменился
    assert len(repo.updates_called) == 0  # Обновление не вызвано
    
    print("✅ Невалидный переход правильно отклонен")


def test_transition_same_status():
    """Тест перехода в тот же статус (обновление полей без изменения статуса)"""
    print("\n=== Тест: transition() - тот же статус ===")
    
    repo = MockRepository()
    hardware_id = "test_hw_005"
    
    # Создаем подписку с paid
    repo.subscriptions[hardware_id] = {'status': 'paid'}
    
    # Переход paid → paid (обновление полей при payment_succeeded)
    stripe_event_at = datetime.now()
    current_period_end = datetime.now() + timedelta(days=30)
    
    result = SubscriptionStateMachine.transition(
        hardware_id=hardware_id,
        from_status='paid',
        to_status='paid',
        event_type='invoice.payment_succeeded',
        repository=repo,
        stripe_status='active',
        current_period_end=current_period_end,
        stripe_event_id='evt_test_same',
        stripe_event_at=stripe_event_at
    )
    
    assert result['success'] == True
    assert result['new_status'] == 'paid'
    assert len(repo.updates_called) == 1
    
    updates = repo.updates_called[0]['updates']
    assert 'status' not in updates  # Статус не обновляется
    assert updates['stripe_status'] == 'active'
    assert updates['grace_period_end_at'] is None
    assert updates['current_period_end'] == current_period_end
    
    print("✅ Обновление полей без изменения статуса работает")


def test_get_allowed_transitions():
    """Тест получения разрешенных переходов"""
    print("\n=== Тест: get_allowed_transitions() ===")
    
    # Проверяем разрешенные переходы для каждого статуса
    assert 'paid' in SubscriptionStateMachine.get_allowed_transitions('paid_trial')
    assert 'limited_free_trial' in SubscriptionStateMachine.get_allowed_transitions('paid_trial')
    
    assert 'billing_problem' in SubscriptionStateMachine.get_allowed_transitions('paid')
    assert 'limited_free_trial' in SubscriptionStateMachine.get_allowed_transitions('paid')
    
    assert 'paid' in SubscriptionStateMachine.get_allowed_transitions('billing_problem')
    assert 'limited_free_trial' in SubscriptionStateMachine.get_allowed_transitions('billing_problem')
    
    assert 'paid' in SubscriptionStateMachine.get_allowed_transitions('limited_free_trial')
    
    # Неизменяемые статусы
    assert SubscriptionStateMachine.get_allowed_transitions('admin_active') == []
    assert SubscriptionStateMachine.get_allowed_transitions('grandfathered') == []
    
    # Новый пользователь
    assert SubscriptionStateMachine.get_allowed_transitions(None) == ['paid_trial']
    
    print("✅ get_allowed_transitions() работает корректно")


def run_all_tests():
    """Запустить все тесты"""
    print("\n" + "="*60)
    print("ТЕСТИРОВАНИЕ STATE MACHINE")
    print("="*60)
    
    try:
        test_can_transition()
        test_transition_payment_succeeded()
        test_transition_payment_failed()
        test_transition_subscription_deleted()
        test_transition_invalid()
        test_transition_same_status()
        test_get_allowed_transitions()
        
        print("\n" + "="*60)
        print("✅ ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО!")
        print("="*60)
        return True
    except AssertionError as e:
        print(f"\n❌ ТЕСТ ПРОВАЛЕН: {e}")
        import traceback
        traceback.print_exc()
        return False
    except Exception as e:
        print(f"\n❌ ОШИБКА: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == '__main__':
    success = run_all_tests()
    sys.exit(0 if success else 1)
