#!/usr/bin/env python3
"""
State Machine для управления переходами статусов подписок

Этот модуль является единственным источником истины для всех переходов статусов.
Все изменения статусов должны проходить через State Machine для валидации.

Feature ID: F-2025-017-stripe-payment
"""
import logging
from typing import Dict, Optional, List
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)


class SubscriptionStateMachine:
    """
    State Machine для переходов статусов подписок
    
    ⚠️ КРИТИЧНО: Эта таблица является единственным источником истины для всех переходов статусов.
    Все изменения статусов должны следовать этой таблице.
    """
    
    # Валидные статусы
    VALID_STATUSES = [
        'paid_trial',
        'paid',
        'billing_problem',
        'limited_free_trial',
        'admin_active',
        'grandfathered'
    ]
    
    # Валидные переходы (из COMPLETE_SYSTEM_LOGIC.md, раздел 12.1)
    VALID_TRANSITIONS = {
        'paid_trial': ['paid', 'limited_free_trial'],
        'paid': ['billing_problem', 'limited_free_trial'],
        'billing_problem': ['paid', 'limited_free_trial'],
        'limited_free_trial': ['paid'],
        'admin_active': [],  # Неизменяемый статус
        'grandfathered': []  # Неизменяемый статус
    }
    
    # Запрещенные переходы (из COMPLETE_SYSTEM_LOGIC.md, раздел 12.3)
    FORBIDDEN_TRANSITIONS = [
        ('limited_free_trial', 'paid_trial'),
        ('paid', 'paid_trial'),
        ('billing_problem', 'paid_trial'),
        ('admin_active', 'paid_trial'),
        ('admin_active', 'paid'),
        ('admin_active', 'billing_problem'),
        ('admin_active', 'limited_free_trial'),
        ('grandfathered', 'paid_trial'),
        ('grandfathered', 'paid'),
        ('grandfathered', 'billing_problem'),
        ('grandfathered', 'limited_free_trial'),
    ]
    
    @classmethod
    def can_transition(cls, from_status: Optional[str], to_status: str) -> bool:
        """
        Проверить, возможен ли переход между статусами
        
        Args:
            from_status: Текущий статус (может быть None для нового пользователя)
            to_status: Целевой статус
        
        Returns:
            True если переход разрешен, False иначе
        """
        # Проверка валидности статусов
        if to_status not in cls.VALID_STATUSES:
            logger.warning(f"[StateMachine] Invalid target status: {to_status}")
            return False
        
        # Если from_status None (новый пользователь), разрешаем только paid_trial
        if from_status is None:
            return to_status == 'paid_trial'
        
        if from_status not in cls.VALID_STATUSES:
            logger.warning(f"[StateMachine] Invalid source status: {from_status}")
            return False
        
        # Проверка запрещенных переходов
        if (from_status, to_status) in cls.FORBIDDEN_TRANSITIONS:
            logger.warning(f"[StateMachine] Forbidden transition: {from_status} → {to_status}")
            return False
        
        # Проверка разрешенных переходов
        allowed = cls.VALID_TRANSITIONS.get(from_status, [])
        if to_status not in allowed:
            logger.warning(f"[StateMachine] Transition not allowed: {from_status} → {to_status} (allowed: {allowed})")
            return False
        
        return True
    
    @classmethod
    def get_allowed_transitions(cls, from_status: Optional[str]) -> List[str]:
        """
        Получить список разрешенных переходов из текущего статуса
        
        Args:
            from_status: Текущий статус (может быть None для нового пользователя)
        
        Returns:
            Список разрешенных целевых статусов
        """
        if from_status is None:
            return ['paid_trial']
        
        if from_status not in cls.VALID_STATUSES:
            return []
        
        return cls.VALID_TRANSITIONS.get(from_status, [])
    
    @classmethod
    def transition(
        cls,
        hardware_id: str,
        from_status: Optional[str],
        to_status: str,
        event_type: str,
        repository,
        **kwargs
    ) -> Dict:
        """
        Выполнить переход статуса с валидацией и подготовкой обновлений БД
        
        ⚠️ КРИТИЧНО: Это единственный способ изменить статус подписки.
        Все обновления статусов должны проходить через этот метод.
        
        Args:
            hardware_id: ID устройства
            from_status: Текущий статус (может быть None для нового пользователя)
            to_status: Целевой статус
            event_type: Тип события Stripe (например, 'invoice.payment_succeeded')
            repository: Экземпляр SubscriptionRepository для обновления БД
            **kwargs: Дополнительные параметры для подготовки обновлений:
                - stripe_status: Статус из Stripe (active, past_due, unpaid, canceled, deleted)
                - current_period_end: Дата окончания текущего периода (datetime)
                - cancel_at_period_end: Флаг отмены подписки (bool)
                - stripe_event_id: ID события Stripe
                - stripe_event_at: Время события (datetime)
                - invoice_id: ID инвойса (для сохранения в payments)
                - invoice_amount: Сумма платежа (int, в центах)
                - invoice_currency: Валюта платежа (str)
                - invoice_status: Статус платежа ('succeeded', 'failed')
        
        Returns:
            Dict с:
                - success (bool): Успешность перехода
                - message (str): Сообщение о результате
                - new_status (str): Новый статус (если переход выполнен)
                - error (str): Ошибка (если переход не выполнен)
        """
        # Если статус не меняется (например, paid → paid при invoice.payment_succeeded)
        # В этом случае валидация не нужна, просто обновляем поля
        if from_status == to_status:
            logger.debug(f"[StateMachine] Status unchanged: {from_status} (event: {event_type})")
            # Подготавливаем обновления без изменения статуса
            updates = cls._prepare_updates(event_type, from_status, to_status, **kwargs)
            if updates:
                repository.update_subscription(hardware_id, **updates)
            return {
                'success': True,
                'message': f'Status unchanged: {from_status}',
                'new_status': from_status
            }
        
        # Валидация перехода (только если статус меняется)
        if not cls.can_transition(from_status, to_status):
            error_msg = f"Invalid transition: {from_status} → {to_status} for event {event_type}"
            logger.error(f"[StateMachine] {error_msg}")
            return {
                'success': False,
                'error': error_msg,
                'new_status': from_status
            }
        
        # Подготавливаем обновления БД
        updates = cls._prepare_updates(event_type, from_status, to_status, **kwargs)
        
        # Добавляем новый статус
        updates['status'] = to_status
        
        # Выполняем обновление в БД
        try:
            repository.update_subscription(hardware_id, **updates)
            logger.info(f"[StateMachine] ✅ Transition: {from_status} → {to_status} for {hardware_id[:8]}... (event: {event_type})")
            return {
                'success': True,
                'message': f'Transition successful: {from_status} → {to_status}',
                'new_status': to_status
            }
        except Exception as e:
            error_msg = f"Error updating subscription: {e}"
            logger.error(f"[StateMachine] ❌ {error_msg}")
            return {
                'success': False,
                'error': error_msg,
                'new_status': from_status
            }
    
    @classmethod
    def _prepare_updates(
        cls,
        event_type: str,
        from_status: Optional[str],
        to_status: str,
        **kwargs
    ) -> Dict:
        """
        Подготовить обновления БД на основе события и перехода
        
        ⚠️ КРИТИЧНО: Эта логика основана на таблице переходов из COMPLETE_SYSTEM_LOGIC.md (раздел 12.1)
        
        Args:
            event_type: Тип события Stripe
            from_status: Текущий статус
            to_status: Целевой статус
            **kwargs: Параметры события
        
        Returns:
            Dict с обновлениями для БД
        """
        updates = {}
        now = datetime.now()
        
        # Извлечение параметров
        stripe_status = kwargs.get('stripe_status')
        current_period_end = kwargs.get('current_period_end')
        cancel_at_period_end = kwargs.get('cancel_at_period_end')
        stripe_event_id = kwargs.get('stripe_event_id')
        stripe_event_at = kwargs.get('stripe_event_at', now)
        
        # Обновление stripe_status (если передан)
        if stripe_status:
            updates['stripe_status'] = stripe_status
        
        # Обновление last_stripe_event_id и last_stripe_event_at
        if stripe_event_id:
            updates['last_stripe_event_id'] = stripe_event_id
        if stripe_event_at:
            updates['last_stripe_event_at'] = stripe_event_at
        
        # Обновление current_period_end
        if current_period_end:
            updates['current_period_end'] = current_period_end
        
        # Обновление cancel_at_period_end
        if cancel_at_period_end is not None:
            updates['cancel_at_period_end'] = cancel_at_period_end
        
        # Специфичные обновления для каждого типа события
        if event_type == 'invoice.payment_succeeded':
            # Очистка grace_period_end_at при успешной оплате
            if to_status == 'paid':
                updates['grace_period_end_at'] = None
                # Обновление stripe_status на active
                if not stripe_status:
                    updates['stripe_status'] = 'active'
        
        elif event_type == 'invoice.payment_failed':
            # Установка grace_period_end_at при неудачной оплате
            if to_status == 'billing_problem':
                grace_end = now + timedelta(days=1)
                updates['grace_period_end_at'] = grace_end
                # Обновление stripe_status на past_due
                if not stripe_status:
                    updates['stripe_status'] = 'past_due'
        
        elif event_type == 'invoice.payment_action_required':
            # Установка grace_period_end_at при требовании действия
            if to_status == 'billing_problem':
                grace_end = now + timedelta(days=1)
                updates['grace_period_end_at'] = grace_end
                # Обновление stripe_status на past_due
                if not stripe_status:
                    updates['stripe_status'] = 'past_due'
        
        elif event_type == 'customer.subscription.updated':
            # Обработка различных stripe_status
            if stripe_status == 'active' and to_status == 'paid':
                # Очистка grace_period_end_at при возврате в paid
                updates['grace_period_end_at'] = None
            elif stripe_status == 'past_due' and to_status == 'billing_problem':
                # Установка grace_period_end_at при past_due
                if 'grace_period_end_at' not in updates:
                    grace_end = now + timedelta(days=1)
                    updates['grace_period_end_at'] = grace_end
            elif stripe_status in ['unpaid', 'canceled'] and to_status == 'limited_free_trial':
                # Очистка grace_period_end_at при переходе в limited_free_trial
                updates['grace_period_end_at'] = None
        
        elif event_type == 'customer.subscription.deleted':
            # Очистка stripe_subscription_id при удалении подписки
            updates['stripe_subscription_id'] = None
            if not stripe_status:
                updates['stripe_status'] = 'deleted'
        
        elif event_type == 'grace_period_expired':
            # Очистка grace_period_end_at при истечении grace period
            if to_status == 'limited_free_trial':
                updates['grace_period_end_at'] = None
                # Обновление stripe_status на unpaid
                if not stripe_status:
                    updates['stripe_status'] = 'unpaid'
        
        elif event_type == 'trial_expired':
            # Очистка при истечении trial (paid_trial_end_at не меняем, оставляем для истории)
            # Никаких дополнительных обновлений не требуется
            pass
        
        # Очистка grace_period_end_at при выходе из billing_problem
        if from_status == 'billing_problem' and to_status != 'billing_problem':
            if 'grace_period_end_at' not in updates:
                updates['grace_period_end_at'] = None
        
        return updates