#!/usr/bin/env python3
"""
Stripe Sync Service для синхронизации подписок со Stripe

⚠️ КРИТИЧНО: Stripe - источник истины
Все расхождения решаются в пользу Stripe.

Feature ID: F-2025-017-stripe-payment
"""
import logging
from typing import Dict, Optional, List
from datetime import datetime, timezone, timedelta
import time
import stripe
from subscription_repository import SubscriptionRepository
from state_machine import SubscriptionStateMachine
from stripe_service import StripeService

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class StripeSyncService:
    """
    Сервис для синхронизации подписок со Stripe
    
    ⚠️ КРИТИЧНО: Stripe - источник истины
    Все расхождения решаются в пользу Stripe.
    """
    
    def __init__(
        self,
        repository: Optional[SubscriptionRepository] = None,
        state_machine: Optional[SubscriptionStateMachine] = None,
        stripe_service: Optional[StripeService] = None
    ):
        """Инициализация Stripe Sync Service"""
        self.repository = repository or SubscriptionRepository()
        self.state_machine = state_machine or SubscriptionStateMachine()
        self.stripe_service = stripe_service or StripeService()
    
    def sync_subscription(self, hardware_id: str) -> Dict:
        """
        Синхронизировать одну подписку со Stripe
        
        ⚠️ КРИТИЧНО:
        - Stripe - источник истины
        - Используем State Machine для переходов
        - Обрабатываем все edge cases
        
        Args:
            hardware_id: ID устройства
        
        Returns:
            Dict с результатом синхронизации:
            - success (bool): Успешность синхронизации
            - message (str): Сообщение о результате
            - mismatches (List): Обнаруженные расхождения
            - transitions (List): Выполненные переходы статусов
            - error (str): Ошибка (если есть)
        """
        logger.info(f"[SYNC] Starting sync for {hardware_id[:8]}...")
        
        # Получаем подписку из БД
        db_subscription = self.repository.get_subscription(hardware_id)
        if not db_subscription:
            logger.warning(f"[SYNC] Subscription not found in DB for {hardware_id[:8]}...")
            return {
                'success': False,
                'message': 'Subscription not found in database',
                'error': 'subscription_not_found'
            }
        
        # ⭐ КРИТИЧНО: Не синхронизируем подписки без stripe_subscription_id
        stripe_subscription_id = db_subscription.get('stripe_subscription_id')
        if not stripe_subscription_id:
            logger.debug(f"[SYNC] Skipping {hardware_id[:8]}...: no stripe_subscription_id")
            return {
                'success': True,
                'message': 'Skipped: no stripe_subscription_id',
                'skipped': True,
                'reason': 'no_stripe_subscription_id'
            }
        
        try:
            # Получаем данные из Stripe
            stripe_subscription = self._retrieve_stripe_subscription(stripe_subscription_id)
            
            # ⭐ КРИТИЧНО: Проверка hardware_id в metadata
            hardware_id_check = self._validate_hardware_id(
                hardware_id,
                stripe_subscription
            )
            if not hardware_id_check['valid']:
                logger.error(f"[SYNC] CRITICAL: {hardware_id_check['error']}")
                return {
                    'success': False,
                    'message': hardware_id_check['error'],
                    'error': 'hardware_id_mismatch',
                    'db_hardware_id': hardware_id,
                    'stripe_hardware_id': hardware_id_check.get('stripe_hardware_id')
                }
            
            # ⭐ КРИТИЧНО: Проверка race conditions
            # Если последнее событие новее, чем обновление в Stripe, пропускаем
            race_check = self._check_race_condition(db_subscription, stripe_subscription)
            if race_check['skip']:
                logger.debug(f"[SYNC] Skipping {hardware_id[:8]}...: {race_check['reason']}")
                return {
                    'success': True,
                    'message': f"Skipped: {race_check['reason']}",
                    'skipped': True,
                    'reason': race_check['reason']
                }
            
            # Обнаруживаем расхождения
            mismatches = self._detect_mismatches(db_subscription, stripe_subscription)
            
            if not mismatches:
                logger.debug(f"[SYNC] No mismatches for {hardware_id[:8]}...")
                return {
                    'success': True,
                    'message': 'No mismatches found',
                    'mismatches': [],
                    'transitions': []
                }
            
            # ⭐ КРИТИЧНО: Реконсиляция через State Machine
            result = self._reconcile_subscription(
                hardware_id,
                db_subscription,
                stripe_subscription,
                mismatches
            )
            
            logger.info(f"[SYNC] ✅ Sync completed for {hardware_id[:8]}...")
            return result
            
        except stripe.error.InvalidRequestError as e:
            # ⭐ КРИТИЧНО: Обработка удаленной подписки (404)
            if e.code == 'resource_missing':
                logger.warning(f"[SYNC] Subscription {stripe_subscription_id} deleted in Stripe")
                return self._handle_deleted_subscription(hardware_id, db_subscription)
            else:
                logger.error(f"[SYNC] Stripe API error: {e}")
                return {
                    'success': False,
                    'message': f'Stripe API error: {e}',
                    'error': 'stripe_api_error',
                    'stripe_error_code': e.code
                }
        
        except stripe.error.RateLimitError as e:
            logger.warning(f"[SYNC] Rate limit error: {e}")
            return {
                'success': False,
                'message': f'Rate limit error: {e}',
                'error': 'rate_limit_error',
                'retry_after': e.headers.get('Retry-After', 60)
            }
        
        except stripe.error.APIConnectionError as e:
            logger.error(f"[SYNC] Connection error: {e}")
            return {
                'success': False,
                'message': f'Connection error: {e}',
                'error': 'connection_error'
            }
        
        except Exception as e:
            logger.error(f"[SYNC] Unexpected error: {e}")
            import traceback
            traceback.print_exc()
            return {
                'success': False,
                'message': f'Unexpected error: {e}',
                'error': 'unexpected_error'
            }
    
    def sync_all_subscriptions(
        self,
        batch_size: int = 20,
        delay_ms: int = 40
    ) -> Dict:
        """
        Синхронизировать все подписки с stripe_subscription_id
        
        ⚠️ КРИТИЧНО: Batch processing для избежания rate limits
        
        Args:
            batch_size: Количество подписок за один запуск
            delay_ms: Задержка между запросами (мс)
        
        Returns:
            Dict с статистикой синхронизации
        """
        logger.info(f"[SYNC] Starting mass sync (batch_size={batch_size})")
        
        # Получаем все подписки с stripe_subscription_id
        subscriptions = self._get_subscriptions_with_stripe_id()
        
        if not subscriptions:
            logger.info("[SYNC] No subscriptions with stripe_subscription_id found")
            return {
                'total': 0,
                'success': 0,
                'skipped': 0,
                'errors': 0,
                'mismatches_found': 0,
                'transitions': 0
            }
        
        logger.info(f"[SYNC] Found {len(subscriptions)} subscriptions to sync")
        
        stats = {
            'total': len(subscriptions),
            'success': 0,
            'skipped': 0,
            'errors': 0,
            'mismatches_found': 0,
            'transitions': 0,
            'results': []
        }
        
        # Обрабатываем подписки батчами
        for i, subscription in enumerate(subscriptions):
            hardware_id = subscription.get('hardware_id')
            
            # Синхронизируем подписку
            result = self.sync_subscription(hardware_id)
            
            # Обновляем статистику
            if result.get('success'):
                if result.get('skipped'):
                    stats['skipped'] += 1
                else:
                    stats['success'] += 1
                    if result.get('mismatches'):
                        stats['mismatches_found'] += len(result['mismatches'])
                    if result.get('transitions'):
                        stats['transitions'] += len(result['transitions'])
            else:
                stats['errors'] += 1
            
            stats['results'].append({
                'hardware_id': hardware_id[:8] + '...',
                'result': result.get('message', 'Unknown'),
                'success': result.get('success', False)
            })
            
            # ⭐ КРИТИЧНО: Задержка для избежания rate limits
            if i < len(subscriptions) - 1:  # Не задерживаемся после последней
                time.sleep(delay_ms / 1000.0)
        
        logger.info(
            f"[SYNC] ✅ Mass sync completed: "
            f"total={stats['total']}, "
            f"success={stats['success']}, "
            f"skipped={stats['skipped']}, "
            f"errors={stats['errors']}, "
            f"mismatches={stats['mismatches_found']}, "
            f"transitions={stats['transitions']}"
        )
        
        return stats
    
    def _retrieve_stripe_subscription(self, subscription_id: str) -> Dict:
        """
        Получить данные подписки из Stripe
        
        ⚠️ КРИТИЧНО: Используем expand для получения связанных объектов
        """
        try:
            subscription = stripe.Subscription.retrieve(
                subscription_id,
                expand=['default_payment_method', 'customer']
            )
            return subscription.to_dict()
        except stripe.error.StripeError as e:
            logger.error(f"[SYNC] Error retrieving subscription {subscription_id}: {e}")
            raise
    
    def _validate_hardware_id(
        self,
        hardware_id: str,
        stripe_subscription: Dict
    ) -> Dict:
        """
        Проверить соответствие hardware_id в metadata Stripe
        
        ⚠️ КРИТИЧНО: Несоответствие - критическая ошибка
        """
        metadata = stripe_subscription.get('metadata', {})
        stripe_hardware_id = metadata.get('hardware_id')
        
        if stripe_hardware_id and stripe_hardware_id != hardware_id:
            return {
                'valid': False,
                'error': f'Hardware ID mismatch: DB={hardware_id}, Stripe={stripe_hardware_id}',
                'stripe_hardware_id': stripe_hardware_id
            }
        
        return {'valid': True}
    
    def _check_race_condition(
        self,
        db_subscription: Dict,
        stripe_subscription: Dict
    ) -> Dict:
        """
        Проверить race condition (webhook обработал событие раньше)
        
        ⚠️ КРИТИЧНО: Если последнее событие новее, чем обновление в Stripe, пропускаем
        """
        last_event_at = db_subscription.get('last_stripe_event_at')
        
        if not last_event_at:
            return {'skip': False}
        
        # Преобразуем в datetime если строка
        if isinstance(last_event_at, str):
            try:
                last_event_at = datetime.fromisoformat(last_event_at.replace('Z', '+00:00'))
            except:
                return {'skip': False}
        
        # Получаем время последнего обновления подписки в Stripe
        stripe_updated_ts = stripe_subscription.get('updated')
        if not stripe_updated_ts:
            return {'skip': False}
        
        stripe_updated = datetime.fromtimestamp(stripe_updated_ts, tz=timezone.utc)
        
        # Если последнее событие новее, чем обновление в Stripe
        if last_event_at > stripe_updated:
            return {
                'skip': True,
                'reason': 'event_newer_than_stripe',
                'last_event_at': last_event_at.isoformat(),
                'stripe_updated': stripe_updated.isoformat()
            }
        
        return {'skip': False}
    
    def _detect_mismatches(
        self,
        db_subscription: Dict,
        stripe_subscription: Dict
    ) -> List[Dict]:
        """
        Обнаружить расхождения между БД и Stripe
        
        ⚠️ КРИТИЧНО: Проверяем ВСЕ поля, которые синхронизируются
        """
        mismatches = []
        
        # 1. stripe_status
        db_status = db_subscription.get('stripe_status')
        stripe_status = stripe_subscription.get('status')
        if db_status != stripe_status:
            mismatches.append({
                'field': 'stripe_status',
                'db_value': db_status,
                'stripe_value': stripe_status,
                'critical': True
            })
        
        # 2. current_period_end
        db_period_end = db_subscription.get('current_period_end')
        stripe_period_end_ts = stripe_subscription.get('current_period_end')
        
        if stripe_period_end_ts:
            stripe_period_end = datetime.fromtimestamp(stripe_period_end_ts, tz=timezone.utc)
            
            # Преобразуем db_period_end в datetime если строка
            if isinstance(db_period_end, str):
                try:
                    db_period_end = datetime.fromisoformat(db_period_end.replace('Z', '+00:00'))
                except:
                    db_period_end = None
            
            if db_period_end:
                # Сравниваем с точностью до секунды
                if abs((db_period_end - stripe_period_end).total_seconds()) > 1:
                    mismatches.append({
                        'field': 'current_period_end',
                        'db_value': db_period_end.isoformat(),
                        'stripe_value': stripe_period_end.isoformat(),
                        'critical': True
                    })
            elif stripe_period_end:
                # В БД нет, но в Stripe есть
                mismatches.append({
                    'field': 'current_period_end',
                    'db_value': None,
                    'stripe_value': stripe_period_end.isoformat(),
                    'critical': True
                })
        
        # 3. cancel_at_period_end
        db_cancel = db_subscription.get('cancel_at_period_end', False)
        stripe_cancel = stripe_subscription.get('cancel_at_period_end', False)
        if db_cancel != stripe_cancel:
            mismatches.append({
                'field': 'cancel_at_period_end',
                'db_value': db_cancel,
                'stripe_value': stripe_cancel,
                'critical': False
            })
        
        # 4. payment_method_id
        db_pm = db_subscription.get('payment_method_id')
        stripe_pm = stripe_subscription.get('default_payment_method')
        
        # Если default_payment_method - объект, извлекаем ID
        if isinstance(stripe_pm, dict):
            stripe_pm = stripe_pm.get('id')
        
        if db_pm != stripe_pm:
            mismatches.append({
                'field': 'payment_method_id',
                'db_value': db_pm,
                'stripe_value': stripe_pm,
                'critical': False
            })
        
        return mismatches
    
    def _reconcile_subscription(
        self,
        hardware_id: str,
        db_subscription: Dict,
        stripe_subscription: Dict,
        mismatches: List[Dict]
    ) -> Dict:
        """
        Реконсиляция подписки (Stripe побеждает)
        
        ⚠️ КРИТИЧНО: Используем State Machine для переходов статусов
        """
        logger.info(f"[SYNC] Reconciling {hardware_id[:8]}... ({len(mismatches)} mismatches)")
        
        current_status = db_subscription.get('status')
        stripe_status = stripe_subscription.get('status')
        
        # Определяем новый статус на основе stripe_status
        new_status = self._determine_status_from_stripe(
            stripe_status,
            current_status,
            db_subscription,
            stripe_subscription
        )
        
        transitions = []
        
        # ⭐ КРИТИЧНО: Используем State Machine для переходов
        if new_status and new_status != current_status:
            result = self.state_machine.transition(
                hardware_id=hardware_id,
                from_status=current_status,
                to_status=new_status,
                event_type='sync.reconcile',
                repository=self.repository,
                stripe_status=stripe_status,
                current_period_end=self._get_current_period_end_dt(stripe_subscription),
                cancel_at_period_end=stripe_subscription.get('cancel_at_period_end', False),
                stripe_event_id=None,  # Нет события, это синхронизация
                stripe_event_at=datetime.now(timezone.utc)
            )
            
            if result.get('success'):
                transitions.append({
                    'from': current_status,
                    'to': new_status,
                    'reason': f'stripe_status={stripe_status}'
                })
                logger.info(f"[SYNC] Status transition: {current_status} → {new_status}")
            else:
                logger.error(f"[SYNC] Failed to transition: {result.get('error')}")
        
        # Обновляем остальные поля (если статус не меняется или переход не удался)
        updates = {}
        
        # Обновляем stripe_status
        if stripe_status:
            updates['stripe_status'] = stripe_status
        
        # Обновляем current_period_end
        period_end_dt = self._get_current_period_end_dt(stripe_subscription)
        if period_end_dt:
            updates['current_period_end'] = period_end_dt
        
        # Обновляем cancel_at_period_end
        updates['cancel_at_period_end'] = stripe_subscription.get('cancel_at_period_end', False)
        
        # Обновляем payment_method_id
        stripe_pm = stripe_subscription.get('default_payment_method')
        if isinstance(stripe_pm, dict):
            stripe_pm = stripe_pm.get('id')
        if stripe_pm:
            updates['payment_method_id'] = stripe_pm
        
        # Применяем обновления
        if updates:
            self.repository.update_subscription(hardware_id, **updates)
            logger.info(f"[SYNC] Updated fields: {list(updates.keys())}")
        
        return {
            'success': True,
            'message': f'Reconciled {len(mismatches)} mismatches',
            'mismatches': mismatches,
            'transitions': transitions
        }
    
    def _determine_status_from_stripe(
        self,
        stripe_status: str,
        current_status: str,
        db_subscription: Dict,
        stripe_subscription: Dict
    ) -> Optional[str]:
        """
        Определить новый статус на основе stripe_status
        
        ⚠️ КРИТИЧНО: 
        - active НЕ означает автоматический переход в paid
        - Источник истины для paid - invoice.payment_succeeded
        - При active обновляем только stripe_status, но не меняем status
        """
        if stripe_status == 'active':
            # ⭐ КРИТИЧНО: НЕ переводим в paid при active без invoice.payment_succeeded
            # Если статус уже paid, оставляем его
            if current_status == 'paid':
                return None  # Без изменений
            # Если статус не paid, но был invoice.payment_succeeded (проверяем по payments)
            # Для упрощения: если stripe_status=active и current_status не paid_trial,
            # то оставляем текущий статус (возможно, был invoice.payment_succeeded ранее)
            return None  # Без изменений статуса, только обновим stripe_status
        
        elif stripe_status == 'past_due':
            if current_status != 'billing_problem':
                return 'billing_problem'
        
        elif stripe_status == 'unpaid':
            # Проверяем grace_period_end_at
            grace_end = db_subscription.get('grace_period_end_at')
            if grace_end:
                if isinstance(grace_end, str):
                    try:
                        grace_end = datetime.fromisoformat(grace_end.replace('Z', '+00:00'))
                    except:
                        grace_end = None
                
                if grace_end and isinstance(grace_end, datetime):
                    if grace_end > datetime.now(timezone.utc):
                        # Grace period активен
                        return 'billing_problem'
            
            # Grace period истек или не был установлен → limited_free_trial
            return 'limited_free_trial'
        
        elif stripe_status in ['canceled', 'incomplete', 'incomplete_expired']:
            return 'limited_free_trial'
        
        elif stripe_status == 'trialing':
            # Если есть paid_trial_end_at, оставляем paid_trial
            if db_subscription.get('paid_trial_end_at'):
                return None  # Без изменений
            return 'paid_trial'
        
        return None  # Без изменений
    
    def _get_current_period_end_dt(self, stripe_subscription: Dict) -> Optional[datetime]:
        """Получить current_period_end как datetime"""
        period_end_ts = stripe_subscription.get('current_period_end')
        if period_end_ts:
            return datetime.fromtimestamp(period_end_ts, tz=timezone.utc)
        return None
    
    def _handle_deleted_subscription(
        self,
        hardware_id: str,
        db_subscription: Dict
    ) -> Dict:
        """
        Обработать удаленную подписку в Stripe
        
        ⚠️ КРИТИЧНО: Переход в limited_free_trial через State Machine
        """
        logger.warning(f"[SYNC] Handling deleted subscription for {hardware_id[:8]}...")
        
        current_status = db_subscription.get('status')
        
        # ⭐ КРИТИЧНО: Используем State Machine для перехода
        result = self.state_machine.transition(
            hardware_id=hardware_id,
            from_status=current_status,
            to_status='limited_free_trial',
            event_type='sync.subscription_deleted',
            repository=self.repository,
            stripe_status='deleted',
            stripe_event_id=None,
            stripe_event_at=datetime.now(timezone.utc)
        )
        
        if result.get('success'):
            # Очищаем stripe_subscription_id
            self.repository.update_subscription(
                hardware_id,
                stripe_subscription_id=None,
                stripe_status='deleted'
            )
            logger.info(f"[SYNC] ✅ Transitioned to limited_free_trial and cleared stripe_subscription_id")
            return {
                'success': True,
                'message': 'Subscription deleted in Stripe, moved to limited_free_trial',
                'transitions': [{
                    'from': current_status,
                    'to': 'limited_free_trial',
                    'reason': 'subscription_deleted_in_stripe'
                }]
            }
        else:
            logger.error(f"[SYNC] Failed to transition: {result.get('error')}")
            return {
                'success': False,
                'message': f'Error transitioning: {result.get("error")}',
                'error': 'transition_failed'
            }
    
    def _get_subscriptions_with_stripe_id(self) -> List[Dict]:
        """
        Получить все подписки с stripe_subscription_id
        
        ⚠️ КРИТИЧНО: Только подписки с stripe_subscription_id синхронизируем
        """
        # Используем прямой SQL запрос через repository
        conn = self.repository._get_connection()
        try:
            from psycopg2.extras import RealDictCursor
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(
                    """SELECT * FROM subscriptions 
                       WHERE stripe_subscription_id IS NOT NULL
                       ORDER BY updated_at DESC"""
                )
                return [dict(row) for row in cur.fetchall()]
        finally:
            conn.close()
