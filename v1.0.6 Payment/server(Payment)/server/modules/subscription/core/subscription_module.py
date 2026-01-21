#!/usr/bin/env python3
"""
Subscription Module для сервера
MVP 7: Интеграция в Workflow

Feature ID: F-2025-017-stripe-payment
"""
import logging
import os
import sys
from typing import Dict, Optional
from datetime import datetime, timedelta

# Добавляем путь к mvp_tests для импорта компонентов
mvp_tests_path = os.path.join(os.path.dirname(__file__), '../../../../../mvp_tests')
if mvp_tests_path not in sys.path:
    sys.path.insert(0, mvp_tests_path)

from subscription_context import SubscriptionContext
from subscription_repository import SubscriptionRepository

# Quota Checker (полная версия)
try:
    from quota_checker import QuotaChecker
    QUOTA_CHECKER_AVAILABLE = True
except ImportError:
    QUOTA_CHECKER_AVAILABLE = False
    QuotaChecker = None

# Subscription Cache
try:
    from subscription_cache import SubscriptionCache
    SUBSCRIPTION_CACHE_AVAILABLE = True
except ImportError:
    SUBSCRIPTION_CACHE_AVAILABLE = False
    SubscriptionCache = None

# MVP 8: Stripe Service для создания Checkout
try:
    from stripe_service import StripeService
    STRIPE_SERVICE_AVAILABLE = True
except ImportError:
    STRIPE_SERVICE_AVAILABLE = False
    StripeService = None

logger = logging.getLogger(__name__)


class SubscriptionModule:
    """
    Модуль для работы с подписками
    
    Предоставляет:
    - Получение контекста подписки для LLM
    - Проверку квот
    - Создание/обновление подписок
    """
    
    def __init__(self, db_url: Optional[str] = None):
        """
        Инициализация модуля
        
        Args:
            db_url: URL базы данных (если не указан, берется из DATABASE_URL)
        """
        self.db_url = db_url or os.getenv('DATABASE_URL')
        if not self.db_url:
            logger.warning("[SubscriptionModule] DATABASE_URL not found, subscription features will be disabled")
            self.repository = None
            self.context_service = None
            self.quota_checker = None
            self.cache = None
            self.stripe_service = None
        else:
            try:
                self.repository = SubscriptionRepository(self.db_url)
                self.context_service = SubscriptionContext(self.repository)
                
                # Quota Checker (полная версия)
                if QUOTA_CHECKER_AVAILABLE:
                    try:
                        self.quota_checker = QuotaChecker(repository=self.repository)
                        logger.info("[SubscriptionModule] QuotaChecker initialized")
                    except Exception as e:
                        logger.warning(f"[SubscriptionModule] Failed to initialize QuotaChecker: {e}")
                        self.quota_checker = None
                else:
                    self.quota_checker = None
                
                # Subscription Cache
                if SUBSCRIPTION_CACHE_AVAILABLE:
                    try:
                        self.cache = SubscriptionCache()
                        logger.info("[SubscriptionModule] SubscriptionCache initialized")
                    except Exception as e:
                        logger.warning(f"[SubscriptionModule] Failed to initialize SubscriptionCache: {e}")
                        self.cache = None
                else:
                    self.cache = None
                
                # MVP 8: Инициализация Stripe Service
                stripe_key = os.getenv('STRIPE_SECRET_KEY')
                if stripe_key and STRIPE_SERVICE_AVAILABLE:
                    try:
                        self.stripe_service = StripeService(stripe_key)
                        logger.info("[SubscriptionModule] StripeService initialized")
                    except Exception as e:
                        logger.warning(f"[SubscriptionModule] Failed to initialize StripeService: {e}")
                        self.stripe_service = None
                else:
                    if not stripe_key:
                        logger.warning("[SubscriptionModule] STRIPE_SECRET_KEY not found, checkout features disabled")
                    if not STRIPE_SERVICE_AVAILABLE:
                        logger.warning("[SubscriptionModule] StripeService not available (import failed)")
                    self.stripe_service = None
                
                logger.info("[SubscriptionModule] Initialized successfully")
            except Exception as e:
                logger.error(f"[SubscriptionModule] Failed to initialize: {e}")
                self.repository = None
                self.context_service = None
                self.quota_checker = None
                self.cache = None
                self.stripe_service = None
    
    def get_or_create_subscription(self, hardware_id: str) -> Dict:
        """
        Получить или создать подписку (создает paid_trial для нового пользователя)
        
        ⚠️ КРИТИЧНО: Это должно вызываться ПЕРЕД get_subscription_context()
        для гарантии, что новый пользователь получит paid_trial
        
        Args:
            hardware_id: Уникальный ID устройства
        
        Returns:
            Dict с информацией о подписке
        """
        if not self.repository:
            return {'status': None, 'error': 'Subscription module not initialized'}
        
        try:
            subscription = self.repository.get_subscription(hardware_id)
            
            if not subscription:
                # Новый пользователь - создаем paid_trial
                trial_end = datetime.now() + timedelta(days=14)
                subscription = self.repository.create_subscription(
                    hardware_id=hardware_id,
                    status='paid_trial',
                    paid_trial_end_at=trial_end
                )
                logger.info(f"[SubscriptionModule] Created paid_trial for {hardware_id[:8]}..., ends_at={trial_end}")
            else:
                # Проверяем, не истек ли trial период
                if subscription.get('status') == 'paid_trial' and subscription.get('paid_trial_end_at'):
                    trial_end = subscription['paid_trial_end_at']
                    if isinstance(trial_end, str):
                        trial_end = datetime.fromisoformat(trial_end.replace('Z', '+00:00'))
                    if isinstance(trial_end, datetime) and trial_end <= datetime.now():
                        # Trial истек - переводим в limited_free_trial
                        self.repository.update_status(hardware_id, 'limited_free_trial')
                        subscription = self.repository.get_subscription(hardware_id)
                        self.invalidate_cache(hardware_id)
                        logger.info(f"[SubscriptionModule] Trial expired for {hardware_id[:8]}..., moved to limited_free_trial")
            
            return subscription
        except Exception as e:
            logger.error(f"[SubscriptionModule] Error in get_or_create_subscription: {e}")
            return {'status': None, 'error': str(e)}
    
    def get_subscription_context(self, hardware_id: str, use_cache: bool = True) -> Dict:
        """
        Получить контекст подписки для передачи в LLM
        
        ⚠️ ВАЖНО: Должен вызываться ПОСЛЕ get_or_create_subscription()
        
        Args:
            hardware_id: Уникальный ID устройства
            use_cache: Использовать кэш (по умолчанию True)
        
        Returns:
            Dict с контекстом подписки и форматированным текстом для LLM
        """
        if not self.context_service:
            return {
                'context': {'status': 'unknown'},
                'formatted_text': ''
            }
        
        try:
            # Проверяем кэш
            if use_cache and self.cache:
                cached_context = self.cache.get(hardware_id)
                if cached_context:
                    logger.debug(f"[SubscriptionModule] Using cached context for {hardware_id[:8]}...")
                    return cached_context
            
            # Получаем контекст из сервиса
            context = self.context_service.get_subscription_context(hardware_id)
            summary = self.context_service.get_context_summary(hardware_id)
            
            # Форматируем для LLM prompt
            formatted_text = self._format_context_for_llm(context, summary)
            
            result = {
                'context': context,
                'formatted_text': formatted_text,
                'summary': summary
            }
            
            # Сохраняем в кэш
            if use_cache and self.cache:
                self.cache.set(hardware_id, result)
            
            return result
        except Exception as e:
            logger.error(f"[SubscriptionModule] Error getting context: {e}")
            return {
                'context': {'status': 'unknown'},
                'formatted_text': ''
            }
    
    def check_quota(self, hardware_id: str) -> Dict:
        """
        Проверить квоты для пользователя
        
        ✅ Использует QuotaChecker (полная версия) для отслеживания использования
        
        Args:
            hardware_id: ID устройства
        
        Returns:
            Dict с allowed (bool), reason (str), и деталями
        """
        if not self.repository:
            # Fallback: разрешаем доступ если модуль не инициализирован
            logger.warning("[SubscriptionModule] Quota check skipped (module not initialized)")
            return {'allowed': True, 'reason': 'module_not_initialized'}
        
        # Используем QuotaChecker если доступен
        if self.quota_checker:
            try:
                return self.quota_checker.check_quota(hardware_id)
            except Exception as e:
                logger.error(f"[SubscriptionModule] Error in QuotaChecker: {e}")
                # Fallback: разрешаем доступ при ошибке
                return {'allowed': True, 'reason': 'error_fallback', 'error': str(e)}
        
        # Fallback: базовая проверка если QuotaChecker не доступен
        logger.warning("[SubscriptionModule] QuotaChecker not available, using fallback")
        try:
            subscription = self.repository.get_subscription(hardware_id)
            
            if not subscription:
                return {'allowed': True, 'reason': 'new_user'}
            
            status = subscription.get('status')
            
            # Безлимитный доступ
            if status in ['paid_trial', 'paid', 'admin_active', 'grandfathered']:
                return {
                    'allowed': True,
                    'reason': 'unlimited_access',
                    'status': status
                }
            
            # Billing problem - проверяем grace period
            if status == 'billing_problem':
                grace_end = subscription.get('grace_period_end_at')
                if grace_end:
                    if isinstance(grace_end, str):
                        grace_end = datetime.fromisoformat(grace_end.replace('Z', '+00:00'))
                    if isinstance(grace_end, datetime) and grace_end > datetime.now():
                        return {
                            'allowed': True,
                            'reason': 'grace_period_active',
                            'status': status
                        }
                return {
                    'allowed': False,
                    'reason': 'grace_period_expired',
                    'status': status,
                    'message': 'Payment failed. Please update your payment method to continue.'
                }
            
            # Limited free trial - разрешаем (QuotaChecker должен обработать)
            if status == 'limited_free_trial':
                return {
                    'allowed': True,
                    'reason': 'limited_free_trial',
                    'status': status
                }
            
            return {
                'allowed': True,
                'reason': 'unknown_status',
                'status': status
            }
            
        except Exception as e:
            logger.error(f"[SubscriptionModule] Error checking quota: {e}")
            return {'allowed': True, 'reason': 'error_fallback', 'error': str(e)}
    
    def increment_usage(self, hardware_id: str) -> Dict:
        """
        Инкрементировать счетчики использования
        
        ⚠️ КРИТИЧНО: Вызывается после успешной обработки запроса
        
        Args:
            hardware_id: ID устройства
        
        Returns:
            Dict с результатом инкремента
        """
        if not self.quota_checker:
            return {'success': False, 'error': 'quota_checker_not_available'}
        
        try:
            return self.quota_checker.increment_usage(hardware_id)
        except Exception as e:
            logger.error(f"[SubscriptionModule] Error incrementing usage: {e}")
            return {'success': False, 'error': str(e)}
    
    def _format_context_for_llm(self, context: Dict, summary: str) -> str:
        """
        Форматировать контекст подписки для добавления в LLM prompt
        
        Args:
            context: Контекст подписки
            summary: Текстовое описание статуса
        
        Returns:
            Форматированный текст для LLM
        """
        if not context or context.get('status') is None:
            return ""
        
        status = context.get('status')
        lines = []
        
        # Добавляем информацию о подписке
        lines.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        lines.append("Subscription Information:")
        lines.append(f"Status: {status}")
        
        if context.get('paid_trial_end_at'):
            lines.append(f"Trial ends: {context['paid_trial_end_at']}")
        
        if context.get('current_period_end'):
            lines.append(f"Current period ends: {context['current_period_end']}")
        
        if context.get('cancel_at_period_end'):
            lines.append("(Subscription scheduled for cancellation)")
        
        if context.get('last_payment_at'):
            amount = context.get('last_payment_amount', 0)
            lines.append(f"Last payment: {context['last_payment_at']} (${amount:.2f})")
        
        if status == 'paid_trial':
            lines.append("")
            lines.append("⚠️ IMPORTANT: User is on a 14-day trial period.")
            lines.append("When the trial ends, subscription options will be available.")
        elif status == 'paid':
            lines.append("")
            lines.append("✅ User has an active paid subscription with unlimited access.")
        elif status == 'billing_problem':
            grace_end = context.get('grace_period_end_at')
            if grace_end:
                lines.append("")
                lines.append("⚠️ Payment issue detected. Grace period active.")
                lines.append("User should update payment method.")
        elif status == 'limited_free_trial':
            lines.append("")
            lines.append("⚠️ User is on limited free trial (5 requests/day, 25/week, 50/month).")
            lines.append("Subscription available for unlimited access.")
        
        lines.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        
        return "\n".join(lines)
    
    def invalidate_cache(self, hardware_id: str) -> None:
        """
        Инвалидировать кэш контекста подписки
        
        Вызывается при изменении подписки через webhook или другие операции
        
        Args:
            hardware_id: ID устройства
        """
        if self.cache:
            self.cache.invalidate(hardware_id)
            logger.debug(f"[SubscriptionModule] Cache invalidated for {hardware_id[:8]}...")
    
    # MVP 8: Команды подписки
    def create_checkout(
        self,
        hardware_id: str,
        success_url: Optional[str] = None,
        cancel_url: Optional[str] = None,
        price_id: Optional[str] = None
    ) -> Dict:
        """
        Создать Checkout Session для подписки
        
        Args:
            hardware_id: ID устройства
            success_url: URL для редиректа после успешной оплаты (deep link)
            cancel_url: URL для редиректа при отмене (deep link)
            price_id: Опциональный Stripe Price ID
        
        Returns:
            Dict с checkout_url, session_id, customer_id, error (если есть)
        """
        if not self.stripe_service:
            return {
                'error': 'Stripe service not configured',
                'checkout_url': None,
                'session_id': None
            }
        
        if not self.repository:
            return {
                'error': 'Database not configured',
                'checkout_url': None,
                'session_id': None
            }
        
        try:
            # Получаем или создаем подписку
            subscription = self.repository.get_subscription(hardware_id)
            if not subscription:
                subscription = self.get_or_create_subscription(hardware_id)
            
            # Проверяем, есть ли уже активная подписка
            if subscription.get('status') == 'paid' and subscription.get('stripe_subscription_id'):
                return {
                    'error': 'User already has an active subscription',
                    'checkout_url': None,
                    'session_id': None
                }
            
            # Формируем URLs для deep links
            base_url = os.getenv('DEEP_LINK_BASE_URL', 'nexy://payment/')
            if not success_url:
                success_url = f"{base_url}checkout/success?session_id={{CHECKOUT_SESSION_ID}}"
            if not cancel_url:
                cancel_url = f"{base_url}checkout/cancel"
            
            # Получаем существующий customer_id если есть
            customer_id = subscription.get('stripe_customer_id')
            
            # Создаем Checkout Session
            result = self.stripe_service.create_checkout_session(
                hardware_id=hardware_id,
                success_url=success_url,
                cancel_url=cancel_url,
                price_id=price_id,
                customer_id=customer_id
            )
            
            session_id = result.get('session_id')
            checkout_url = result.get('checkout_url')
            returned_customer_id = result.get('customer_id')
            
            logger.info(f"[SubscriptionModule] Checkout created for {hardware_id[:8]}...: {session_id}")
            
            # ⭐ КРИТИЧНО (MVP 8 fix): Сохраняем stripe_customer_id и last_checkout_* в БД
            # Это необходимо для:
            # 1. Корректной привязки при повторном checkout/отмене
            # 2. Anti-spam и cooldown механизмов
            from datetime import datetime
            updates = {
                'last_checkout_created_at': datetime.now(),
                'last_checkout_session_id': session_id
            }
            
            # Сохраняем customer_id если он был создан/возвращен
            if returned_customer_id:
                updates['stripe_customer_id'] = returned_customer_id
                logger.debug(f"[SubscriptionModule] Saving stripe_customer_id={returned_customer_id[:20]}... to DB")
            
            self.repository.update_subscription(hardware_id, **updates)
            # Инвалидируем кэш при изменении подписки
            self.invalidate_cache(hardware_id)
            
            return {
                'checkout_url': checkout_url,
                'session_id': session_id,
                'customer_id': returned_customer_id,
                'error': None
            }
            
        except Exception as e:
            logger.error(f"[SubscriptionModule] Error creating checkout: {e}")
            return {
                'error': str(e),
                'checkout_url': None,
                'session_id': None
            }
    
    def cancel_subscription(self, hardware_id: str) -> Dict:
        """
        Отменить подписку
        
        Args:
            hardware_id: ID устройства
        
        Returns:
            Dict с success (bool), message (str)
        """
        if not self.repository:
            return {
                'success': False,
                'message': 'Database not configured'
            }
        
        try:
            subscription = self.repository.get_subscription(hardware_id)
            if not subscription:
                return {
                    'success': False,
                    'message': 'Subscription not found'
                }
            
            stripe_subscription_id = subscription.get('stripe_subscription_id')
            
            if not stripe_subscription_id:
                # Локальная подписка (trial) - просто обновляем статус
                self.repository.update_status(hardware_id, 'limited_free_trial')
                logger.info(f"[SubscriptionModule] Trial subscription cancelled for {hardware_id[:8]}...")
                return {
                    'success': True,
                    'message': 'Trial subscription cancelled'
                }
            
            # Отменяем в Stripe (если есть stripe_service)
            if self.stripe_service:
                try:
                    import stripe
                    stripe_subscription = stripe.Subscription.retrieve(stripe_subscription_id)
                    stripe.Subscription.modify(
                        stripe_subscription_id,
                        cancel_at_period_end=True
                    )
                    logger.info(f"[SubscriptionModule] Stripe subscription {stripe_subscription_id} scheduled for cancellation")
                    
                    # ⭐ КРИТИЧНО (MVP 8 fix): Обновляем cancel_at_period_end=True в БД
                    # Статус остается paid до конца периода, но флаг отмены сохраняется
                    self.repository.update_subscription(
                        hardware_id,
                        cancel_at_period_end=True,
                        status='paid'  # Остается paid до конца периода
                    )
                    # Инвалидируем кэш при изменении подписки
                    self.invalidate_cache(hardware_id)
                    
                    return {
                        'success': True,
                        'message': 'Subscription will be cancelled at the end of the current period'
                    }
                except Exception as e:
                    logger.error(f"[SubscriptionModule] Error cancelling Stripe subscription: {e}")
                    return {
                        'success': False,
                        'message': f'Error cancelling subscription: {str(e)}'
                    }
            else:
                # Stripe service недоступен - просто обновляем статус
                self.repository.update_status(hardware_id, 'limited_free_trial')
                return {
                    'success': True,
                    'message': 'Subscription cancelled (Stripe service not available)'
                }
            
        except Exception as e:
            logger.error(f"[SubscriptionModule] Error cancelling subscription: {e}")
            return {
                'success': False,
                'message': str(e)
            }
    
    def get_portal_url(
        self,
        hardware_id: str,
        return_url: Optional[str] = None
    ) -> Dict:
        """
        Получить URL для Customer Portal (управление подпиской)
        
        MVP 10: Customer Portal для обновления payment method, просмотра истории платежей и т.д.
        
        Args:
            hardware_id: Уникальный ID устройства
            return_url: Опциональный URL для возврата из Portal
        
        Returns:
            Dict с portal_url или error
        """
        try:
            # Получаем подписку
            subscription = self.repository.get_subscription(hardware_id)
            if not subscription:
                return {
                    'error': 'Subscription not found',
                    'portal_url': None
                }
            
            # Проверяем, есть ли stripe_customer_id
            customer_id = subscription.get('stripe_customer_id')
            if not customer_id:
                return {
                    'error': 'No Stripe customer found. Please create a subscription first.',
                    'portal_url': None
                }
            
            # Проверяем, есть ли активная подписка в Stripe
            stripe_subscription_id = subscription.get('stripe_subscription_id')
            if not stripe_subscription_id:
                return {
                    'error': 'No active Stripe subscription found. Payment method can only be updated for active subscriptions.',
                    'portal_url': None
                }
            
            # Формируем return_url для deep link
            if not return_url:
                base_url = os.getenv('DEEP_LINK_BASE_URL', 'nexy://payment/')
                return_url = f"{base_url}portal_return"
            
            # Создаем Portal Session через StripeService
            result = self.stripe_service.create_portal_session(
                customer_id=customer_id,
                return_url=return_url
            )
            
            portal_url = result.get('portal_url')
            logger.info(f"[SubscriptionModule] Portal URL created for {hardware_id[:8]}...: {portal_url[:50]}...")
            
            return {
                'success': True,
                'portal_url': portal_url,
                'session_id': result.get('session_id')
            }
            
        except Exception as e:
            logger.error(f"[SubscriptionModule] Error creating portal URL: {e}")
            return {
                'success': False,
                'error': str(e),
                'portal_url': None
            }
