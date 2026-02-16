#!/usr/bin/env python3
"""
Subscription Module - единственный владелец статусов и квот подписок

Feature ID: F-2025-017-stripe-payment

⚠️ КРИТИЧНО: Это Source of Truth для всех решений о доступе и квотах.
Клиент НЕ выполняет никаких расчётов - только отображает статус.
"""
import logging
import os
import threading
from typing import Dict, Any, Optional
from dataclasses import dataclass
from datetime import datetime

from config.unified_config import get_config
from .core.subscription_types import AccessTier, PAID_STATUSES, map_status_to_tier

logger = logging.getLogger(__name__)


@dataclass
class CanProcessResult:
    """Результат проверки доступа"""
    allowed: bool
    reason: str
    status: Optional[str] = None
    message: Optional[str] = None
    subscription_context: Optional[Dict[str, Any]] = None


class SubscriptionModule:
    """
    Центральный модуль управления подписками.
    
    Владеет:
    - Проверкой доступа (can_process)
    - Инкрементом использования (increment_usage)
    - Контекстом для LLM (get_context_for_prompt)
    - Периодическими задачами (scheduler)
    
    ⚠️ КРИТИЧНО: Единственный способ проверить доступ пользователя.
    """
    
    def __init__(self):
        self.config = get_config().subscription
        self._repository: Optional[Any] = None
        self._quota_checker: Optional[Any] = None
        self._state_machine: Optional[Any] = None
        self._scheduler: Optional[Any] = None
        self._stripe_service: Optional[Any] = None
        self._initialized = False
        self._cache = {}  # Simple TTL cache
        self._cache_lock = threading.Lock()  # Защита кэша
        self._cache_ttl = self.config.cache_ttl_seconds
        # In-flight guard: prevents concurrent can_process from overshooting quotas.
        # Entries auto-expire to avoid stuck reservations if increment_usage is not called.
        self._pending_usage: Dict[str, list[float]] = {}
        self._pending_lock = threading.Lock()
        self._pending_ttl_seconds = self.config.pending_ttl_seconds

    def _prune_pending(self, hardware_id: str, now_ts: float) -> int:
        """Prune expired pending entries and return current pending count."""
        with self._pending_lock:
            entries = self._pending_usage.get(hardware_id, [])
            if not entries:
                return 0
            fresh = [ts for ts in entries if (now_ts - ts) <= self._pending_ttl_seconds]
            if fresh:
                self._pending_usage[hardware_id] = fresh
            else:
                self._pending_usage.pop(hardware_id, None)
            return len(fresh)

    def _add_pending(self, hardware_id: str, now_ts: float) -> None:
        """Add a pending slot for a hardware_id."""
        with self._pending_lock:
            self._pending_usage.setdefault(hardware_id, []).append(now_ts)

    def _release_pending(self, hardware_id: str) -> None:
        """Release one pending slot for a hardware_id (best-effort)."""
        with self._pending_lock:
            entries = self._pending_usage.get(hardware_id)
            if not entries:
                return
            entries.pop(0)
            if not entries:
                self._pending_usage.pop(hardware_id, None)
        
    async def initialize(self) -> bool:
        """
        Инициализация модуля.
        
        Returns:
            True если инициализация успешна
        """
        if not self.config.is_active():
            logger.info("[F-2025-017] Subscription module disabled by config")
            return False
        
        try:
            # Lazy import to avoid circular dependencies
            from .repository.subscription_repository import SubscriptionRepository
            from .core.quota_checker import QuotaChecker
            from .core.state_machine import SubscriptionStateMachine
            from .providers.stripe_service import StripeService
            
            # Construct DB URL from unified_config
            # This is critical because SubscriptionRepository relies on DATABASE_URL or passed url
            # and unified_config stores connection details in separate fields.
            db_cfg = get_config().get_module_config('database')
            # Support both object and dict access just in case
            if isinstance(db_cfg, dict):
                user = db_cfg.get('user', os.getenv('DB_USER', 'postgres'))
                password = db_cfg.get('password', os.getenv('DB_PASSWORD', ''))
                host = db_cfg.get('host', os.getenv('DB_HOST', 'localhost'))
                port = db_cfg.get('port', int(os.getenv('DB_PORT', '5432')))
                name = db_cfg.get('name', os.getenv('DB_NAME', 'voice_assistant_db'))
            else:
                # Fallback or if it returns object
                user = getattr(db_cfg, 'user', os.getenv('DB_USER', 'postgres'))
                password = getattr(db_cfg, 'password', os.getenv('DB_PASSWORD', ''))
                host = getattr(db_cfg, 'host', os.getenv('DB_HOST', 'localhost'))
                port = getattr(db_cfg, 'port', int(os.getenv('DB_PORT', '5432')))
                name = getattr(db_cfg, 'name', os.getenv('DB_NAME', 'voice_assistant_db'))

            # Construct safe URL
            db_url = f"postgresql://{user}:{password}@{host}:{port}/{name}"
            
            self._repository = SubscriptionRepository(db_url=db_url)
            self._quota_checker = QuotaChecker(repository=self._repository)
            self._state_machine = SubscriptionStateMachine
            
            # Use key from config
            if not self.config.stripe_secret_key:
                logger.error("[F-2025-017] STRIPE_SECRET_KEY not set in config!")
                return False
                
            self._stripe_service = StripeService(api_key=self.config.stripe_secret_key)
            
            self._initialized = True
            logger.info("[F-2025-017] Subscription module initialized")
            return True
            
        except Exception as e:
            logger.error(f"[F-2025-017] Failed to initialize subscription module: {e}")
            return False
    
    async def create_portal_session(self, hardware_id: str) -> Optional[Dict[str, str]]:
        """
        Создать сессию Customer Portal для управления подпиской.
        
        Args:
            hardware_id: ID устройства
            
        Returns:
            Dict с portal_url или None
        """
        if not self._initialized or not self.config.is_active():
            return None
        if self._repository is None or self._stripe_service is None:
            return None
            
        try:
            # 1. Получаем подписку чтобы найти stripe_customer_id
            sub = self._repository.get_subscription(hardware_id)
            if not sub:
                logger.warning(f"[F-2025-017] No subscription found for {hardware_id}")
                return None
                
            customer_id = sub.get('stripe_customer_id')
            if not customer_id:
                logger.warning(f"[F-2025-017] No stripe_customer_id for {hardware_id}")
                return None
                
            # 2. Создаем сессию портала через StripeService
            # Синхронизируем email из локальной БД в Stripe, если он там отличается
            email = sub.get('email')
            result = self._stripe_service.create_portal_session(
                customer_id=customer_id,
                email=email
            )
            return result
            
        except Exception as e:
            logger.error(f"[F-2025-017] Error creating portal session: {e}")
            return None

    async def create_checkout_session(
        self,
        hardware_id: str,
        base_url: Optional[str] = None
    ) -> Optional[Dict[str, str]]:
        """
        Создать сессию Checkout для покупки подписки.
        
        Args:
            hardware_id: ID устройства
            
        Returns:
            Dict с checkout_url или None
        """
        if not self._initialized or not self.config.is_active():
            return None
        if self._repository is None or self._stripe_service is None:
            return None
            
        try:
            # 1. Проверяем, есть ли уже customer_id
            sub = self._repository.get_subscription(hardware_id)
            customer_id = sub.get('stripe_customer_id') if sub else None

            # 2. Формируем success/cancel URLs
            # По умолчанию используем локальные страницы успешной оплаты.
            # Можно переопределить через STRIPE_SUCCESS_URL / STRIPE_CANCEL_URL.
            success_url = os.getenv("STRIPE_SUCCESS_URL")
            cancel_url = os.getenv("STRIPE_CANCEL_URL")
            if not success_url or not cancel_url:
                resolved_base = base_url or os.getenv("PAYMENT_SUCCESS_BASE_URL", "http://127.0.0.1:8080")
                resolved_base = resolved_base.rstrip("/")
                if not success_url:
                    success_url = f"{resolved_base}/payment/success?session_id={{CHECKOUT_SESSION_ID}}"
                if not cancel_url:
                    cancel_url = f"{resolved_base}/payment/cancel"
            
            # 3. Создаем сессию
            # Передаем hardware_id в metadata, чтобы связать после оплаты (если webhook придет раньше)
            # И customer_id если есть, чтобы не дублировать кастомеров
            result = await self._stripe_service.create_checkout_session(
                hardware_id=hardware_id,
                customer_id=customer_id,
                success_url=success_url,
                cancel_url=cancel_url,
                trial_days=self.config.trial_days
            )
            return result
            
        except Exception as e:
            logger.error(f"[F-2025-017] Error creating checkout session: {e}")
            return None
    
    async def get_subscription_status(self, hardware_id: str) -> Dict[str, Any]:
        """
        Получить текущий статус подписки для поллинга.
        
        Args:
            hardware_id: ID устройства
            
        Returns:
            Dict со статусом и метаданными
        """
        if not self._initialized or not self.config.is_active():
            return {'status': 'unknown', 'active': False}
        if self._repository is None:
            return {'status': 'unknown', 'active': False}
            
        try:
            sub = self._repository.get_subscription(hardware_id)
            if not sub:
                return {'status': 'none', 'active': False}
            status = sub.get('status')
            tier = map_status_to_tier(
                status,
                grandfathered_enabled=self.config.grandfathered_enabled
            )

            return {
                'status': status,
                'stripe_status': sub.get('stripe_status'),
                'email': sub.get('email'),
                # active=true means user can use product now (unlimited or limited tier)
                'active': tier in [AccessTier.UNLIMITED, AccessTier.LIMITED],
                'current_period_end': sub.get('current_period_end')
            }
            
        except Exception as e:
            logger.error(f"[F-2025-017] Error getting subscription status: {e}")
            return {'status': 'error', 'message': str(e)}

    async def can_process(self, hardware_id: str) -> CanProcessResult:
        """
        Единственный gate для проверки доступа.
        
        ⚠️ КРИТИЧНО: Все проверки доступа ДОЛЖНЫ проходить через этот метод.
        
        Args:
            hardware_id: ID устройства
            
        Returns:
            CanProcessResult с решением allow/deny
        """
        # Если модуль отключен по конфигу - разрешаем всё (продукт работает без подписок)
        if not self.config.is_active():
            return CanProcessResult(
                allowed=True,
                reason='subscription_disabled',
                subscription_context=None
            )
        
        # ⚠️ КРИТИЧНО: Если enabled=True, но не initialized - это ошибка конфигурации
        # Логируем ERROR и разрешаем (fail-open), но это НУЖНО ИСПРАВИТЬ
        if not self._initialized:
            logger.error(
                "[F-2025-017] CONFIGURATION ERROR: Subscription enabled but not initialized! "
                "Call await subscription_module.initialize() before use. Allowing request (fail-open)."
            )
            return CanProcessResult(
                allowed=True,
                reason='initialization_error',
                message='Subscription module not initialized'
            )
        if self._quota_checker is None:
            return CanProcessResult(
                allowed=True,
                reason='initialization_error',
                message='Quota checker not initialized'
            )
        
        try:
            # Проверяем cache
            cached = self._get_cached(hardware_id)
            if cached is not None:
                return cached
            
            # Проверяем квоты
            quota_result = self._quota_checker.check_quota(hardware_id)

            # In-flight guard (avoid concurrent requests overshooting limits)
            pending_count = self._prune_pending(hardware_id, now_ts=datetime.now().timestamp())
            if quota_result.get('allowed', False):
                limits = quota_result.get('limits') or {}
                daily = limits.get('daily') or {}
                weekly = limits.get('weekly') or {}
                monthly = limits.get('monthly') or {}
                # Only enforce if limits present (limited tier)
                if limits and pending_count > 0:
                    daily_used = int(daily.get('used', 0)) + pending_count
                    weekly_used = int(weekly.get('used', 0)) + pending_count
                    monthly_used = int(monthly.get('used', 0)) + pending_count
                    if daily and daily_used >= int(daily.get('limit', 0)):
                        quota_result = {
                            'allowed': False,
                            'reason': 'daily_limit_exceeded',
                            'status': quota_result.get('status'),
                            'message': 'Daily limit exceeded (in-flight)',
                            'limits': limits,
                        }
                    elif weekly and weekly_used >= int(weekly.get('limit', 0)):
                        quota_result = {
                            'allowed': False,
                            'reason': 'weekly_limit_exceeded',
                            'status': quota_result.get('status'),
                            'message': 'Weekly limit exceeded (in-flight)',
                            'limits': limits,
                        }
                    elif monthly and monthly_used >= int(monthly.get('limit', 0)):
                        quota_result = {
                            'allowed': False,
                            'reason': 'monthly_limit_exceeded',
                            'status': quota_result.get('status'),
                            'message': 'Monthly limit exceeded (in-flight)',
                            'limits': limits,
                        }
            
            result = CanProcessResult(
                allowed=quota_result.get('allowed', False),
                reason=quota_result.get('reason', 'unknown'),
                status=quota_result.get('status'),
                message=quota_result.get('message'),
                subscription_context=self._build_context(quota_result)
            )

            # Reserve a pending slot for allowed requests (limited tiers)
            if result.allowed:
                self._add_pending(hardware_id, datetime.now().timestamp())
            
            # Кэшируем результат (и allowed, и denied)
            # Внимание: инваладация происходит через Webhooks (оплата) 
            # и Scheduler (сброс квот), поэтому безопасно кэшировать всё.
            self._set_cached(hardware_id, result)
            
            return result
            
        except Exception as e:
            logger.error(f"[F-2025-017] Error checking subscription for {hardware_id[:8]}...: {e}")
            # При ошибке - разрешаем (fail-open для не блокирующих сценариев)
            return CanProcessResult(
                allowed=True,
                reason='error_failopen',
                message=str(e)
            )
    
    async def increment_usage(self, hardware_id: str) -> bool:
        """
        Инкремент использования ПОСЛЕ успешной генерации.
        
        ⚠️ КРИТИЧНО: Вызывать ТОЛЬКО после успешной обработки запроса.
        
        Args:
            hardware_id: ID устройства
            
        Returns:
            True если инкремент успешен
        """
        if not self._initialized or not self.config.is_active():
            return True
        if self._quota_checker is None:
            return True
        
        try:
            result = await self._quota_checker.increment_usage(hardware_id)
            # Release one pending slot after usage increment (best-effort)
            self._release_pending(hardware_id)
            
            if result.get('success'):
                # Инвалидируем кэш
                self._invalidate_cache(hardware_id)
                logger.debug(f"[F-2025-017] Usage incremented for {hardware_id[:8]}...")
                return True
            else:
                logger.warning(f"[F-2025-017] Failed to increment usage: {result.get('message')}")
                return False
                
        except Exception as e:
            logger.error(f"[F-2025-017] Error incrementing usage: {e}")
            return False
    
    async def get_context_for_prompt(self, hardware_id: str) -> str:
        """
        Получить контекст подписки для LLM prompt.
        
        Args:
            hardware_id: ID устройства
            
        Returns:
            Строка контекста для добавления в prompt
        """
        if not self._initialized or not self.config.is_active():
            return ""
        
        try:
            # 1. Get basic access result
            result = await self.can_process(hardware_id)
            
            # 2. Get detailed status (including dates)
            sub_details = await self.get_subscription_status(hardware_id)
            status = sub_details.get('status', 'unknown')
            active = sub_details.get('active', False)
            date = sub_details.get('current_period_end')
            
            # Format date if present
            date_str = ""
            if date:
                try:
                    # Date might be timestamp or string
                    if isinstance(date, (int, float)):
                        dt = datetime.fromtimestamp(date)
                        date_str = f". Renew: {dt.strftime('%Y-%m-%d')}"
                    else:
                        date_str = f". Renew: {date}"
                except:
                    pass

            # Build context string (centralized tier mapping)
            tier = map_status_to_tier(
                status,
                grandfathered_enabled=self.config.grandfathered_enabled
            )

            if status in PAID_STATUSES or tier == AccessTier.UNLIMITED:
                return f"[Subscription: Paid (Active){date_str}]"
            if status == 'billing_problem':
                return "[Subscription: Billing Problem - Payment Failed]"
            if tier == AccessTier.LIMITED:
                # Show remaining quota from context if available
                ctx = result.subscription_context or {}
                limits = ctx.get('limits', {})
                # Example limits: {'daily': {'used': 5, 'limit': 10}}
                quota_str = ""
                if limits:
                    daily = limits.get('daily', {})
                    if daily:
                        quota_str = f" (Daily: {daily.get('used')}/{daily.get('limit')})"
                return f"[Subscription: Free Limited{quota_str}]"

            return "[Subscription: None / Inactive]"
            
        except Exception as e:
            logger.error(f"[F-2025-017] Error getting context: {e}")
            return ""
    
    def start_scheduler(self) -> None:
        """
        Запуск периодических задач.
        
        ⚠️ КРИТИЧНО: Вызывать из main.py при старте сервера.
        Scheduler владеется этим модулем.
        """
        if not self._initialized or not self.config.is_active():
            logger.info("[F-2025-017] Scheduler not started - module disabled")
            return
        
        try:
            from apscheduler.schedulers.asyncio import AsyncIOScheduler
            
            self._scheduler = AsyncIOScheduler()
            
            # Trial lifecycle handled by Stripe via webhooks.
            
            # Grace period check
            self._scheduler.add_job(
                self._run_grace_period_check,
                'interval',
                hours=self.config.grace_period_check_interval_hours,
                id='grace_period_check'
            )
            
            # Daily quota reset (at midnight)
            self._scheduler.add_job(
                self._run_daily_quota_reset,
                'cron',
                hour=0,
                minute=0,
                id='daily_quota_reset'
            )
            
            # Weekly quota reset (Monday at midnight)
            self._scheduler.add_job(
                self._run_weekly_quota_reset,
                'cron',
                day_of_week='mon',
                hour=0,
                minute=0,
                id='weekly_quota_reset'
            )
            
            # Monthly quota reset (1st of month at midnight)
            self._scheduler.add_job(
                self._run_monthly_quota_reset,
                'cron',
                day=1,
                hour=0,
                minute=0,
                id='monthly_quota_reset'
            )
            
            self._scheduler.start()
            logger.info("[F-2025-017] Scheduler started with periodic tasks")
            
        except ImportError:
            logger.warning("[F-2025-017] APScheduler not installed - periodic tasks disabled")
        except Exception as e:
            logger.error(f"[F-2025-017] Failed to start scheduler: {e}")
    
    def stop_scheduler(self) -> None:
        """Остановка scheduler"""
        if self._scheduler:
            self._scheduler.shutdown(wait=False)
            logger.info("[F-2025-017] Scheduler stopped")
    
    # --- Private methods ---
    
    def _build_context(self, quota_result: Dict) -> Optional[Dict[str, Any]]:
        """Построить контекст из результата проверки квот"""
        if not quota_result:
            return None
        
        return {
            'status': quota_result.get('status'),
            'limits': quota_result.get('limits'),
            'reason': quota_result.get('reason')
        }
    
    def _get_cached(self, hardware_id: str) -> Optional[CanProcessResult]:
        """Получить результат из кэша"""
        with self._cache_lock:
            entry = self._cache.get(hardware_id)
            if entry:
                if (datetime.now() - entry['time']).seconds < self._cache_ttl:
                    return entry['result']
                else:
                    del self._cache[hardware_id]
            return None
    
    def _set_cached(self, hardware_id: str, result: CanProcessResult) -> None:
        """Сохранить результат в кэш"""
        with self._cache_lock:
            self._cache[hardware_id] = {
                'result': result,
                'time': datetime.now()
            }
    
    def _invalidate_cache(self, hardware_id: str) -> None:
        """Инвалидировать кэш для пользователя"""
        with self._cache_lock:
            if hardware_id in self._cache:
                del self._cache[hardware_id]
    
    def invalidate_all_cache(self) -> None:
        """Инвалидировать весь кэш (после webhook)"""
        with self._cache_lock:
            self._cache.clear()
        logger.debug("[F-2025-017] Cache invalidated")
    
    async def _run_trial_check(self) -> None:
        """Периодическая проверка истекших trial"""
        try:
            if self._repository is None:
                return
            from .core.trial_handler import TrialHandler
            handler = TrialHandler(self._repository)
            result = handler.process_expired_trials()
            logger.info(f"[F-2025-017] Trial check completed: {result}")
        except Exception as e:
            logger.error(f"[F-2025-017] Trial check failed: {e}")
    
    async def _run_grace_period_check(self) -> None:
        """Периодическая проверка истекших grace period"""
        try:
            if self._repository is None:
                return
            from .core.grace_period_handler import GracePeriodHandler
            handler = GracePeriodHandler(self._repository)
            result = handler.process_expired_grace_periods()
            logger.info(f"[F-2025-017] Grace period check completed: {result}")
        except Exception as e:
            logger.error(f"[F-2025-017] Grace period check failed: {e}")
    
    async def _run_daily_quota_reset(self) -> None:
        """Сброс ежедневных квот"""
        try:
            if self._quota_checker is None:
                return
            result = self._quota_checker.reset_daily_counters()
            self.invalidate_all_cache()
            logger.info(f"[F-2025-017] Daily quota reset completed: {result}")
        except Exception as e:
            logger.error(f"[F-2025-017] Daily quota reset failed: {e}")

    async def _run_weekly_quota_reset(self) -> None:
        """Сброс недельных квот"""
        try:
            if self._quota_checker is None:
                return
            result = self._quota_checker.reset_weekly_counters()
            self.invalidate_all_cache()
            logger.info(f"[F-2025-017] Weekly quota reset completed: {result}")
        except Exception as e:
            logger.error(f"[F-2025-017] Weekly quota reset failed: {e}")

    async def _run_monthly_quota_reset(self) -> None:
        """Сброс месячных квот"""
        try:
            if self._quota_checker is None:
                return
            result = self._quota_checker.reset_monthly_counters()
            self.invalidate_all_cache()
            logger.info(f"[F-2025-017] Monthly quota reset completed: {result}")
        except Exception as e:
            logger.error(f"[F-2025-017] Monthly quota reset failed: {e}")


# Singleton instance
_subscription_module: Optional[SubscriptionModule] = None
_initialization_attempted: bool = False


async def initialize_subscription_module() -> Optional[SubscriptionModule]:
    """
    Инициализировать и вернуть singleton SubscriptionModule.
    
    ⚠️ КРИТИЧНО: Вызывать при старте сервера, ДО первого использования.
    
    Returns:
        SubscriptionModule если активен и инициализация успешна, иначе None
    """
    global _subscription_module, _initialization_attempted
    
    if _initialization_attempted:
        return _subscription_module
    
    _initialization_attempted = True
    
    config = get_config().subscription
    if not config.is_active():
        logger.info("[F-2025-017] Subscription module disabled by config - skipping initialization")
        return None
    
    _subscription_module = SubscriptionModule()
    success = await _subscription_module.initialize()
    
    if not success:
        logger.error("[F-2025-017] Failed to initialize subscription module")
        _subscription_module = None
        return None
    
    return _subscription_module


def get_subscription_module() -> Optional[SubscriptionModule]:
    """
    Получить singleton экземпляр SubscriptionModule.
    
    ⚠️ ВАЖНО: Модуль должен быть предварительно инициализирован
    через initialize_subscription_module(). Если не инициализирован,
    возвращает None.
    
    Returns:
        SubscriptionModule если инициализирован, иначе None
    """
    global _subscription_module
    
    # Проверяем, был ли модуль отключен по конфигу
    config = get_config().subscription
    if not config.is_active():
        return None
    
    # Если попытка инициализации была, но модуль None - значит failed или disabled
    if _initialization_attempted:
        return _subscription_module
    
    # Если initialize_subscription_module не была вызвана, логируем предупреждение
    logger.warning(
        "[F-2025-017] get_subscription_module() called before initialization. "
        "Call initialize_subscription_module() at server startup."
    )
    return None
