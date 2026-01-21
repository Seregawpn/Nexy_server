#!/usr/bin/env python3
"""
Webhook Handler для обработки событий от Stripe
MVP 6: Webhook Handler

Feature ID: F-2025-017-stripe-payment
"""
import logging
from typing import Dict, Optional
from datetime import datetime, timedelta
from subscription_repository import SubscriptionRepository
from stripe_service import StripeService
from state_machine import SubscriptionStateMachine
import stripe

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class WebhookHandler:
    """Обработчик webhook событий от Stripe"""
    
    def __init__(
        self,
        repository: Optional[SubscriptionRepository] = None,
        stripe_service: Optional[StripeService] = None
    ):
        """Инициализация Webhook Handler"""
        self.repository = repository or SubscriptionRepository()
        self.stripe_service = stripe_service or StripeService()
        self.state_machine = SubscriptionStateMachine()
    
    def handle_event(self, event: Dict) -> Dict:
        """
        Обработка webhook события
        
        Args:
            event: Stripe event object (dict)
        
        Returns:
            Dict с success (bool), message (str), hardware_id (str)
        """
        event_type = event.get('type')
        event_id = event.get('id')
        stripe_created_at = event.get('created')  # Unix timestamp
        
        logger.info(f"[WEBHOOK] Processing event: {event_type} (id: {event_id})")
        
        # ⭐ КРИТИЧНО: Проверка идемпотентности
        # Проверяем только события с processed=TRUE (события без hardware_id имеют processed=FALSE)
        if self.repository.event_exists(event_id, processed_only=True):
            logger.info(f"[WEBHOOK] Event {event_id} already processed (idempotency)")
            return {
                'success': True,
                'message': 'Event already processed',
                'event_id': event_id
            }
        
        try:
            # Восстанавливаем hardware_id из события
            hardware_id = self._extract_hardware_id(event)
            
            if not hardware_id:
                logger.warning(f"[WEBHOOK] No hardware_id found for event {event_id}")
                # ⭐ КРИТИЧНО: Сохраняем событие как processed=FALSE для повторной обработки
                # Это позволяет обработать событие позже, когда hardware_id появится в БД
                self.repository.record_event(
                    stripe_event_id=event_id,
                    event_type=event_type,
                    hardware_id=None,
                    event_data=event.get('data', {}),
                    stripe_created_at=stripe_created_at,
                    processed=False  # ⭐ КРИТИЧНО: processed=FALSE для повторной обработки
                )
                return {
                    'success': False,
                    'message': 'hardware_id not found in event metadata (saved for retry)',
                    'event_id': event_id
                }
            
            # Маршрутизация по типу события
            handler = self._get_handler(event_type)
            if not handler:
                logger.warning(f"[WEBHOOK] No handler for event type: {event_type}")
                # Сохраняем событие, но не обрабатываем
                self.repository.record_event(
                    stripe_event_id=event_id,
                    event_type=event_type,
                    hardware_id=hardware_id,
                    event_data=event.get('data', {}),
                    stripe_created_at=stripe_created_at
                )
                return {
                    'success': False,
                    'message': f'Unknown event type: {event_type}',
                    'event_id': event_id,
                    'hardware_id': hardware_id
                }
            
            # Обработка события
            result = handler(event, hardware_id)
            
            # Сохраняем событие (идемпотентность)
            self.repository.record_event(
                stripe_event_id=event_id,
                event_type=event_type,
                hardware_id=hardware_id,
                event_data=event.get('data', {}),
                stripe_created_at=stripe_created_at
            )
            
            logger.info(f"[WEBHOOK] ✅ Event {event_id} processed successfully for {hardware_id}")
            return {
                'success': True,
                'message': result.get('message', 'Event processed'),
                'event_id': event_id,
                'hardware_id': hardware_id,
                **result
            }
            
        except Exception as e:
            logger.error(f"[WEBHOOK] ❌ Error handling event {event_id}: {e}")
            import traceback
            traceback.print_exc()
            return {
                'success': False,
                'message': str(e),
                'event_id': event_id
            }
    
    def _extract_hardware_id(self, event: Dict) -> Optional[str]:
        """
        Восстановить hardware_id из metadata события
        
        ⭐ КРИТИЧНО: hardware_id должен быть в metadata Session/Customer/Subscription
        (согласно ARCHITECTURE_FIXES.md)
        
        Порядок проверки:
        1. Session metadata (для checkout.session.completed)
        2. Subscription metadata (для customer.subscription.*)
        3. Customer metadata (для invoice.*)
        4. Поиск в БД по customer_id/subscription_id (fallback)
        """
        event_type = event.get('type', '')
        data_obj = event.get('data', {}).get('object', {})
        
        # 1. Проверяем Session metadata (для checkout.session.completed)
        if event_type.startswith('checkout.session.'):
            metadata = data_obj.get('metadata', {})
            hardware_id = metadata.get('hardware_id')
            if hardware_id:
                logger.debug(f"[WEBHOOK] Found hardware_id in Session metadata: {hardware_id}")
                return hardware_id
        
        # 2. Проверяем Subscription metadata (для customer.subscription.*)
        if 'subscription' in event_type:
            metadata = data_obj.get('metadata', {})
            hardware_id = metadata.get('hardware_id')
            if hardware_id:
                logger.debug(f"[WEBHOOK] Found hardware_id in Subscription metadata: {hardware_id}")
                return hardware_id
        
        # 3. Проверяем Customer metadata (для invoice.*)
        if event_type.startswith('invoice.'):
            customer_id = data_obj.get('customer')
            if customer_id:
                try:
                    customer = stripe.Customer.retrieve(customer_id)
                    hardware_id = customer.metadata.get('hardware_id')
                    if hardware_id:
                        logger.debug(f"[WEBHOOK] Found hardware_id in Customer metadata: {hardware_id}")
                        return hardware_id
                except Exception as e:
                    logger.warning(f"[WEBHOOK] Error retrieving customer {customer_id}: {e}")
        
        # 4. Fallback: поиск в БД по customer_id/subscription_id
        customer_id = data_obj.get('customer')
        subscription_id = data_obj.get('subscription') or data_obj.get('id')
        
        if subscription_id:
            subscription = self.repository.get_subscription_by_stripe_subscription_id(subscription_id)
            if subscription:
                hardware_id = subscription.get('hardware_id')
                if hardware_id:
                    logger.debug(f"[WEBHOOK] Found hardware_id in DB by subscription_id: {hardware_id}")
                    return hardware_id
        
        if customer_id:
            subscription = self.repository.get_subscription_by_stripe_customer_id(customer_id)
            if subscription:
                hardware_id = subscription.get('hardware_id')
                if hardware_id:
                    logger.debug(f"[WEBHOOK] Found hardware_id in DB by customer_id: {hardware_id}")
                    return hardware_id
        
        return None
    
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
    
    def _handle_checkout_completed(self, event: Dict, hardware_id: str) -> Dict:
        """
        Обработка checkout.session.completed
        
        ⚠️ КРИТИЧНО: НЕ меняем статус на paid!
        checkout.session.completed ≠ оплата, ждем invoice.payment_succeeded
        """
        session = event['data']['object']
        customer_id = session.get('customer')
        subscription_id = session.get('subscription')
        
        logger.info(f"[WEBHOOK] Checkout completed for {hardware_id}, linking customer/subscription")
        
        # Линковка customer/subscription
        self.repository.update_stripe_ids(
            hardware_id,
            customer_id=customer_id,
            subscription_id=subscription_id
        )
        
        # Обновляем last_stripe_event_id/at
        self.repository.update_subscription(
            hardware_id,
            last_stripe_event_id=event.get('id'),
            last_stripe_event_at=datetime.fromtimestamp(event.get('created', 0), tz=datetime.now().tzinfo)
        )
        
        return {
            'message': 'Checkout completed, customer/subscription linked',
            'customer_id': customer_id,
            'subscription_id': subscription_id
        }
    
    def _handle_subscription_updated(self, event: Dict, hardware_id: str) -> Dict:
        """Обработка customer.subscription.updated"""
        subscription_obj = event['data']['object']
        stripe_status = subscription_obj.get('status')  # active, past_due, unpaid, canceled, etc.
        current_period_end = subscription_obj.get('current_period_end')
        cancel_at_period_end = subscription_obj.get('cancel_at_period_end', False)
        
        logger.info(f"[WEBHOOK] Subscription updated for {hardware_id}, status: {stripe_status}")
        
        # Получаем текущую подписку
        subscription = self.repository.get_subscription(hardware_id)
        if not subscription:
            # ⭐ КРИТИЧНО (MVP 8 fix): Если hardware_id найден, но подписки нет в БД - создаем
            # Это обрабатывает сценарий "webhook пришёл раньше записи в БД"
            logger.info(f"[WEBHOOK] Subscription not found for {hardware_id}, creating new subscription from webhook")
            subscription = self.repository.create_subscription(
                hardware_id=hardware_id,
                status='paid_trial'  # Базовый статус, будет обновлен ниже
            )
            logger.info(f"[WEBHOOK] Created subscription for {hardware_id} from webhook event")
        
        current_status = subscription.get('status')
        stripe_event_at = datetime.fromtimestamp(event.get('created', 0), tz=datetime.now().tzinfo)
        
        # Преобразуем current_period_end в datetime если есть
        current_period_end_dt = None
        if current_period_end:
            current_period_end_dt = datetime.fromtimestamp(current_period_end, tz=datetime.now().tzinfo)
        
        # ⭐ КРИТИЧНО: Определяем новый статус на основе stripe_status
        # НО: НЕ переводим в paid при stripe_status='active' без invoice.payment_succeeded
        # (источник истины для paid - invoice.payment_succeeded)
        new_status = self._determine_status_from_stripe(stripe_status, current_status, cancel_at_period_end, hardware_id)
        
        # Если статус не меняется, обновляем только поля без изменения статуса
        if not new_status or new_status == current_status:
            # Обновляем только stripe_status и другие поля без изменения статуса
            updates = {
                'stripe_status': stripe_status,
                'cancel_at_period_end': cancel_at_period_end,
                'last_stripe_event_id': event.get('id'),
                'last_stripe_event_at': stripe_event_at
            }
            if current_period_end_dt:
                updates['current_period_end'] = current_period_end_dt
            self.repository.update_subscription(hardware_id, **updates)
            return {
                'message': f'Subscription updated, stripe_status: {stripe_status}',
                'stripe_status': stripe_status,
                'new_status': current_status
            }
        
        # ⭐ КРИТИЧНО: Используем State Machine для перехода статуса
        result = self.state_machine.transition(
            hardware_id=hardware_id,
            from_status=current_status,
            to_status=new_status,
            event_type='customer.subscription.updated',
            repository=self.repository,
            stripe_status=stripe_status,
            current_period_end=current_period_end_dt,
            cancel_at_period_end=cancel_at_period_end,
            stripe_event_id=event.get('id'),
            stripe_event_at=stripe_event_at
        )
        
        if result.get('success'):
            logger.info(f"[WEBHOOK] Status transition: {current_status} → {new_status} for {hardware_id}")
            return {
                'message': f'Subscription updated, stripe_status: {stripe_status}',
                'stripe_status': stripe_status,
                'new_status': new_status
            }
        else:
            logger.error(f"[WEBHOOK] Failed to transition: {result.get('error')}")
            # Fallback: обновляем только stripe_status без изменения статуса
            updates = {
                'stripe_status': stripe_status,
                'cancel_at_period_end': cancel_at_period_end,
                'last_stripe_event_id': event.get('id'),
                'last_stripe_event_at': stripe_event_at
            }
            if current_period_end_dt:
                updates['current_period_end'] = current_period_end_dt
            self.repository.update_subscription(hardware_id, **updates)
            return {
                'message': f'Subscription updated (status transition failed: {result.get("error")})',
                'stripe_status': stripe_status,
                'new_status': current_status
            }
    
    def _handle_subscription_deleted(self, event: Dict, hardware_id: str) -> Dict:
        """Обработка customer.subscription.deleted"""
        logger.info(f"[WEBHOOK] Subscription deleted for {hardware_id}")
        
        # Получаем текущую подписку
        subscription = self.repository.get_subscription(hardware_id)
        if not subscription:
            logger.warning(f"[WEBHOOK] Subscription not found for {hardware_id}, cannot delete")
            return {'message': 'Subscription not found'}
        
        current_status = subscription.get('status')
        stripe_event_at = datetime.fromtimestamp(event.get('created', 0), tz=datetime.now().tzinfo)
        
        # ⭐ КРИТИЧНО: Используем State Machine для перехода в limited_free_trial
        result = self.state_machine.transition(
            hardware_id=hardware_id,
            from_status=current_status,
            to_status='limited_free_trial',
            event_type='customer.subscription.deleted',
            repository=self.repository,
            stripe_status='deleted',
            stripe_event_id=event.get('id'),
            stripe_event_at=stripe_event_at
        )
        
        if result.get('success'):
            return {'message': 'Subscription deleted, moved to limited_free_trial'}
        else:
            logger.error(f"[WEBHOOK] Failed to transition to limited_free_trial: {result.get('error')}")
            return {'message': f'Error: {result.get("error")}'}
    
    def _handle_payment_succeeded(self, event: Dict, hardware_id: str) -> Dict:
        """
        Обработка invoice.payment_succeeded
        
        ⭐ КРИТИЧНО: Это источник истины для статуса paid
        
        Обновляет:
        - status → paid
        - stripe_status → active
        - current_period_end (из subscription)
        - grace_period_end_at → NULL (очистка)
        """
        invoice = event['data']['object']
        invoice_id = invoice.get('id')
        amount = invoice.get('amount_paid', 0)  # В центах
        currency = invoice.get('currency', 'usd')
        subscription_id = invoice.get('subscription')
        
        logger.info(f"[WEBHOOK] Payment succeeded for {hardware_id}, amount: ${amount/100:.2f}")
        
        # Проверяем идемпотентность платежа
        if self.repository.payment_exists(invoice_id):
            logger.info(f"[WEBHOOK] Payment {invoice_id} already recorded (idempotency)")
        else:
            # Сохраняем платеж
            self.repository.create_payment(
                hardware_id=hardware_id,
                stripe_invoice_id=invoice_id,
                amount=amount,
                currency=currency,
                status='succeeded'
            )
        
        # Получаем текущую подписку
        subscription = self.repository.get_subscription(hardware_id)
        if not subscription:
            # ⭐ КРИТИЧНО (MVP 8 fix): Если hardware_id найден, но подписки нет в БД - создаем
            # Это обрабатывает сценарий "webhook пришёл раньше записи в БД"
            logger.info(f"[WEBHOOK] Subscription not found for {hardware_id}, creating new subscription from webhook")
            subscription = self.repository.create_subscription(
                hardware_id=hardware_id,
                status='paid_trial'  # Базовый статус, будет обновлен ниже
            )
            logger.info(f"[WEBHOOK] Created subscription for {hardware_id} from webhook event")
        
        current_status = subscription.get('status')
        
        # ⭐ КРИТИЧНО: Получаем current_period_end из subscription (если есть)
        # Если subscription_id есть, можно получить из Stripe, но для MVP используем из invoice
        # В реальности нужно получить subscription из Stripe для current_period_end
        current_period_end = None
        if subscription_id:
            try:
                stripe_subscription = stripe.Subscription.retrieve(subscription_id)
                current_period_end_ts = stripe_subscription.get('current_period_end')
                if current_period_end_ts:
                    current_period_end = datetime.fromtimestamp(current_period_end_ts, tz=datetime.now().tzinfo)
            except Exception as e:
                logger.warning(f"[WEBHOOK] Error retrieving subscription {subscription_id}: {e}")
        
        # ⭐ КРИТИЧНО: Используем State Machine для перехода в paid (источник истины)
        stripe_event_at = datetime.fromtimestamp(event.get('created', 0), tz=datetime.now().tzinfo)
        
        result = self.state_machine.transition(
            hardware_id=hardware_id,
            from_status=current_status,
            to_status='paid',
            event_type='invoice.payment_succeeded',
            repository=self.repository,
            stripe_status='active',
            current_period_end=current_period_end,
            stripe_event_id=event.get('id'),
            stripe_event_at=stripe_event_at
        )
        
        if result.get('success'):
            if current_status != 'paid':
                logger.info(f"[WEBHOOK] Status → paid for {hardware_id} (source of truth: invoice.payment_succeeded)")
            else:
                logger.info(f"[WEBHOOK] Payment succeeded, already paid (updated stripe_status and cleared grace_period)")
        else:
            logger.error(f"[WEBHOOK] Failed to transition to paid: {result.get('error')}")
        
        return {
            'message': 'Payment succeeded, status updated to paid',
            'amount': amount / 100,  # В долларах
            'currency': currency
        }
    
    def _handle_payment_failed(self, event: Dict, hardware_id: str) -> Dict:
        """
        Обработка invoice.payment_failed
        
        ⭐ КРИТИЧНО: Сохраняем запись в payments со статусом failed для аудита
        """
        invoice = event['data']['object']
        invoice_id = invoice.get('id')
        amount = invoice.get('amount_due', 0)  # В центах
        currency = invoice.get('currency', 'usd')
        
        logger.warning(f"[WEBHOOK] Payment failed for {hardware_id}")
        
        # ⭐ КРИТИЧНО (MVP 8 fix): Создаем подписку если записи нет
        subscription = self.repository.get_subscription(hardware_id)
        if not subscription:
            logger.info(f"[WEBHOOK] Subscription not found for {hardware_id}, creating new subscription from webhook")
            subscription = self.repository.create_subscription(
                hardware_id=hardware_id,
                status='paid_trial'  # Базовый статус, будет обновлен ниже
            )
        
        # ⭐ КРИТИЧНО: Сохраняем запись в payments со статусом failed (для аудита)
        if not self.repository.payment_exists(invoice_id):
            self.repository.create_payment(
                hardware_id=hardware_id,
                stripe_invoice_id=invoice_id,
                amount=amount,
                currency=currency,
                status='failed'
            )
            logger.info(f"[WEBHOOK] Payment {invoice_id} recorded as failed (audit)")
        
        # ⭐ КРИТИЧНО: Используем State Machine для перехода в billing_problem
        current_status = subscription.get('status')
        stripe_event_at = datetime.fromtimestamp(event.get('created', 0), tz=datetime.now().tzinfo)
        
        result = self.state_machine.transition(
            hardware_id=hardware_id,
            from_status=current_status,
            to_status='billing_problem',
            event_type='invoice.payment_failed',
            repository=self.repository,
            stripe_status='past_due',
            stripe_event_id=event.get('id'),
            stripe_event_at=stripe_event_at
        )
        
        if result.get('success'):
            # Получаем обновленную подписку для получения grace_period_end_at
            updated_subscription = self.repository.get_subscription(hardware_id)
            grace_end = updated_subscription.get('grace_period_end_at')
            logger.info(f"[WEBHOOK] Status → billing_problem (grace period until {grace_end}) for {hardware_id}")
        else:
            logger.error(f"[WEBHOOK] Failed to transition to billing_problem: {result.get('error')}")
        
        return {
            'message': 'Payment failed, grace period started',
            'grace_period_end_at': grace_end.isoformat()
        }
    
    def _handle_payment_action_required(self, event: Dict, hardware_id: str) -> Dict:
        """Обработка invoice.payment_action_required (требуется SCA/3DS)"""
        logger.warning(f"[WEBHOOK] Payment action required for {hardware_id} (SCA/3DS)")
        
        # ⭐ КРИТИЧНО (MVP 8 fix): Создаем подписку если записи нет
        subscription = self.repository.get_subscription(hardware_id)
        if not subscription:
            logger.info(f"[WEBHOOK] Subscription not found for {hardware_id}, creating new subscription from webhook")
            subscription = self.repository.create_subscription(
                hardware_id=hardware_id,
                status='paid_trial'  # Базовый статус, будет обновлен ниже
            )
        
        # ⭐ КРИТИЧНО: Используем State Machine для перехода в billing_problem
        current_status = subscription.get('status')
        stripe_event_at = datetime.fromtimestamp(event.get('created', 0), tz=datetime.now().tzinfo)
        
        result = self.state_machine.transition(
            hardware_id=hardware_id,
            from_status=current_status,
            to_status='billing_problem',
            event_type='invoice.payment_action_required',
            repository=self.repository,
            stripe_status='past_due',
            stripe_event_id=event.get('id'),
            stripe_event_at=stripe_event_at
        )
        
        if result.get('success'):
            # Получаем обновленную подписку для получения grace_period_end_at
            updated_subscription = self.repository.get_subscription(hardware_id)
            grace_end = updated_subscription.get('grace_period_end_at')
            return {
                'message': 'Payment action required (SCA/3DS), grace period started',
                'grace_period_end_at': grace_end.isoformat() if grace_end else None
            }
        else:
            logger.error(f"[WEBHOOK] Failed to transition to billing_problem: {result.get('error')}")
            return {
                'message': f'Error: {result.get("error")}',
                'grace_period_end_at': None
            }
    
    def _determine_status_from_stripe(
        self,
        stripe_status: str,
        current_status: str,
        cancel_at_period_end: bool,
        hardware_id: str
    ) -> Optional[str]:
        """
        Определить новый статус на основе stripe_status
        
        ⭐ КРИТИЧНО: НЕ переводим в paid при stripe_status='active' без invoice.payment_succeeded
        (источник истины для paid - invoice.payment_succeeded)
        
        State Machine переходы (из COMPLETE_SYSTEM_LOGIC.md):
        - active → НЕ меняем статус (ждем invoice.payment_succeeded)
        - past_due → billing_problem (с grace_period_end_at)
        - unpaid → limited_free_trial (если grace period истек)
        - canceled → limited_free_trial
        - incomplete/incomplete_expired → limited_free_trial
        """
        if stripe_status == 'active':
            # ⭐ КРИТИЧНО: НЕ переводим в paid при active без invoice.payment_succeeded
            # Источник истины для paid - invoice.payment_succeeded
            # Просто обновляем stripe_status='active', но статус остается текущим
            return None  # Без изменений статуса
        elif stripe_status == 'past_due':
            if current_status != 'billing_problem':
                # ⭐ КРИТИЧНО: При переходе в billing_problem устанавливаем grace_period_end_at
                # (устанавливается в _handle_subscription_updated)
                return 'billing_problem'
        elif stripe_status == 'unpaid':
            # Проверяем grace period
            subscription = self.repository.get_subscription(hardware_id)
            if subscription:
                grace_end = subscription.get('grace_period_end_at')
                if grace_end:
                    if isinstance(grace_end, str):
                        # Пробуем разные форматы
                        try:
                            grace_end = datetime.fromisoformat(grace_end.replace('Z', '+00:00'))
                        except:
                            try:
                                grace_end = datetime.strptime(grace_end, '%Y-%m-%d %H:%M:%S')
                            except:
                                logger.warning(f"[WEBHOOK] Cannot parse grace_period_end_at: {grace_end}")
                                grace_end = None
                    if grace_end and isinstance(grace_end, datetime):
                        if grace_end > datetime.now():
                            # Grace period активен
                            return 'billing_problem'
            # Grace period истек или не был установлен → limited_free_trial
            return 'limited_free_trial'
        elif stripe_status in ['canceled', 'incomplete', 'incomplete_expired']:
            return 'limited_free_trial'
        
        # Если cancel_at_period_end=True, статус остается paid до current_period_end
        if cancel_at_period_end and current_status == 'paid':
            return 'paid'  # Остается paid
        
        return None  # Без изменений
