#!/usr/bin/env python3
"""
Quota Checker - полная версия с отслеживанием использования

Отслеживает использование квот для limited_free_trial:
- 5 запросов/день
- 25 запросов/неделя
- 50 запросов/месяц

Feature ID: F-2025-017-stripe-payment
"""
import logging
from typing import Dict, Optional, TYPE_CHECKING
from datetime import datetime, date, timedelta

if TYPE_CHECKING:
    from ..repository.subscription_repository import SubscriptionRepository

logger = logging.getLogger(__name__)



class QuotaChecker:
    """
    Quota Checker для проверки и отслеживания использования квот
    
    Лимиты берутся из SubscriptionConfig (unified_config.py)
    По умолчанию для limited_free_trial:
    - quota_daily запросов/день
    - quota_weekly запросов/неделя
    - quota_monthly запросов/месяц
    """
    
    def __init__(self, repository=None, config=None):
        """
        Инициализация QuotaChecker
        
        Args:
            repository: SubscriptionRepository instance
            config: SubscriptionConfig (если None, берётся из get_config())
        """
        from config.unified_config import get_config
        from ..repository.subscription_repository import SubscriptionRepository
        
        self.config = config or get_config().subscription
        self.repository = repository or SubscriptionRepository()
        
        # Лимиты из конфига (Source of Truth)
        self.DAILY_LIMIT = self.config.quota_daily
        self.WEEKLY_LIMIT = self.config.quota_weekly
        self.MONTHLY_LIMIT = self.config.quota_monthly
    
    def check_quota(self, hardware_id: str) -> Dict:
        """
        Проверить квоты для пользователя
        
        ⚠️ КРИТИЧНО: Проверяет лимиты для limited_free_trial
        
        Args:
            hardware_id: ID устройства
        
        Returns:
            Dict с:
            - 'allowed': bool (True если разрешено, False если лимит превышен)
            - 'reason': str (причина)
            - 'status': str (текущий статус подписки)
            - 'limits': Dict (детали лимитов и использования)
            - 'message': Optional[str] (сообщение для пользователя)
        """
        subscription = self.repository.get_subscription(hardware_id)
        
        if not subscription:
            # Новый пользователь - разрешаем, будет создан paid_trial
            return {
                'allowed': True,
                'reason': 'new_user',
                'status': 'none',
                'limits': None
            }
        
        status = subscription.get('status')
        
        # Безлимитный доступ для определенных статусов
        if status in ['paid_trial', 'paid', 'admin_active', 'grandfathered']:
            return {
                'allowed': True,
                'reason': 'unlimited_access',
                'status': status,
                'limits': None
            }
        
        # Billing problem - проверяем grace period
        if status == 'billing_problem':
            grace_end = subscription.get('grace_period_end_at')
            if grace_end and isinstance(grace_end, datetime) and grace_end > datetime.now():
                return {
                    'allowed': True,
                    'reason': 'grace_period_active',
                    'status': status,
                    'limits': None
                }
            # Grace period истек, или его не было
            return {
                'allowed': False,
                'reason': 'grace_period_expired',
                'status': status,
                'message': 'Payment failed. Please update your payment method to continue.',
                'limits': None
            }
        
        # Limited free trial - проверяем квоты
        if status == 'limited_free_trial':
            today = date.today()
            
            # Автоматический сброс счетчиков, если дата последнего сброса устарела
            last_reset_date = subscription.get('usage_last_reset_date')
            if last_reset_date and isinstance(last_reset_date, date) and last_reset_date < today:
                # Сбрасываем только те счетчики, которые должны быть сброшены
                # (например, если last_reset_date был вчера, сбрасываем daily)
                # Более сложные сбросы (weekly/monthly) делаются через периодические задачи
                logger.info(f"[QuotaChecker] Auto-resetting daily quota for {hardware_id[:8]}...")
                self.repository.update_subscription(
                    hardware_id,
                    usage_daily_count=0,
                    usage_last_reset_date=today # Обновляем дату сброса
                )
                subscription['usage_daily_count'] = 0
                subscription['usage_last_reset_date'] = today
            
            daily_used = subscription.get('usage_daily_count', 0)
            weekly_used = subscription.get('usage_weekly_count', 0)
            monthly_used = subscription.get('usage_monthly_count', 0)
            
            limits = {
                'daily': {'used': daily_used, 'limit': self.DAILY_LIMIT},
                'weekly': {'used': weekly_used, 'limit': self.WEEKLY_LIMIT},
                'monthly': {'used': monthly_used, 'limit': self.MONTHLY_LIMIT}
            }
            
            if daily_used >= self.DAILY_LIMIT:
                return {
                    'allowed': False,
                    'reason': 'daily_limit_exceeded',
                    'status': status,
                    'message': f'Daily request limit ({self.DAILY_LIMIT}) exceeded. Please subscribe for unlimited access.',
                    'limits': limits
                }
            if weekly_used >= self.WEEKLY_LIMIT:
                return {
                    'allowed': False,
                    'reason': 'weekly_limit_exceeded',
                    'status': status,
                    'message': f'Weekly request limit ({self.WEEKLY_LIMIT}) exceeded. Please subscribe for unlimited access.',
                    'limits': limits
                }
            if monthly_used >= self.MONTHLY_LIMIT:
                return {
                    'allowed': False,
                    'reason': 'monthly_limit_exceeded',
                    'status': status,
                    'message': f'Monthly request limit ({self.MONTHLY_LIMIT}) exceeded. Please subscribe for unlimited access.',
                    'limits': limits
                }
            
            return {
                'allowed': True,
                'reason': 'within_quota',
                'status': status,
                'message': f'You have {self.DAILY_LIMIT - daily_used} daily requests remaining.',
                'limits': limits
            }
        
        # Неизвестный статус - по умолчанию запрещаем, чтобы не было бесконечного использования
        logger.warning(f"[QuotaChecker] Unknown status {status} for {hardware_id[:8]}..., denying access by default.")
        return {
            'allowed': False,
            'reason': 'unknown_status',
            'status': status,
            'message': 'Your subscription status is unknown. Please contact support.',
            'limits': None
        }

    def increment_usage(self, hardware_id: str) -> Dict:
        """
        Инкрементирует счетчики использования для пользователя.
        Вызывается после успешной обработки запроса.
        """
        subscription = self.repository.get_subscription(hardware_id)
        if not subscription or subscription.get('status') != 'limited_free_trial':
            return {'success': False, 'message': 'Not a limited_free_trial user or subscription not found'}
        
        current_date = date.today()
        success = self.repository.increment_usage(hardware_id, current_date)
        
        if success:
            logger.debug(f"[QuotaChecker] Incremented usage for {hardware_id[:8]}...")
            return {'success': True, 'message': 'Usage incremented'}
        else:
            logger.error(f"[QuotaChecker] Failed to increment usage for {hardware_id[:8]}...")
            return {'success': False, 'message': 'Failed to increment usage'}

    def reset_daily_counters(self) -> Dict:
        """
        Сбрасывает ежедневные счетчики использования для всех пользователей,
        у которых usage_last_reset_date не равен сегодняшней дате.
        """
        today = date.today()
        subscriptions_to_reset = self.repository.get_subscriptions_for_daily_reset(today)
        
        reset_count = 0
        for sub in subscriptions_to_reset:
            # Проверяем, что сброс действительно нужен (может быть уже сброшен weekly/monthly)
            if sub['usage_last_reset_date'] < today:
                self.repository.update_subscription(
                    sub['hardware_id'],
                    usage_daily_count=0,
                    usage_last_reset_date=today # Обновляем дату сброса
                )
                reset_count += 1
        
        logger.info(f"[QuotaChecker] Reset daily counters: {reset_count} subscriptions")
        return {'success': True, 'reset_count': reset_count, 'reset_date': today.isoformat()}

    def reset_weekly_counters(self) -> Dict:
        """
        Сбрасывает еженедельные счетчики использования для всех пользователей,
        у которых usage_last_reset_date не равен началу текущей недели.
        """
        today = date.today()
        week_start = today - timedelta(days=today.weekday()) # Понедельник
        
        subscriptions_to_reset = self.repository.get_subscriptions_for_weekly_reset(week_start)
        
        reset_count = 0
        for sub in subscriptions_to_reset:
            if sub['usage_last_reset_date'] < week_start:
                self.repository.update_subscription(
                    sub['hardware_id'],
                    usage_weekly_count=0,
                    usage_last_reset_date=week_start # Обновляем дату сброса
                )
                reset_count += 1
        
        logger.info(f"[QuotaChecker] Reset weekly counters: {reset_count} subscriptions")
        return {'success': True, 'reset_count': reset_count, 'reset_date': week_start.isoformat()}

    def reset_monthly_counters(self) -> Dict:
        """
        Сбрасывает ежемесячные счетчики использования для всех пользователей,
        у которых usage_last_reset_date не равен началу текущего месяца.
        """
        today = date.today()
        month_start = date(today.year, today.month, 1)
        
        subscriptions_to_reset = self.repository.get_subscriptions_for_monthly_reset(month_start)
        
        reset_count = 0
        for sub in subscriptions_to_reset:
            if sub['usage_last_reset_date'] < month_start:
                self.repository.update_subscription(
                    sub['hardware_id'],
                    usage_monthly_count=0,
                    usage_last_reset_date=month_start # Обновляем дату сброса
                )
                reset_count += 1
        
        logger.info(f"[QuotaChecker] Reset monthly counters: {reset_count} subscriptions")
        return {'success': True, 'reset_count': reset_count, 'reset_date': month_start.isoformat()}

