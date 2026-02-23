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
import asyncio
from typing import Dict, Any, Optional
from dataclasses import dataclass
from datetime import datetime, timezone

from config.unified_config import get_config
from .core.subscription_types import (
    AccessTier,
    PAID_STATUSES,
    map_status_to_tier,
    map_stripe_status_to_local_status,
)

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
        self._reconcile_locks: Dict[str, asyncio.Lock] = {}
        self._reconcile_locks_guard = threading.Lock()
        self._checkout_reuse_window_sec = 15 * 60
        # Lazy sync guard for status reads when webhooks are delayed/missed.
        self._status_sync_last_run: Dict[str, float] = {}
        self._status_sync_lock = threading.Lock()
        self._status_sync_min_interval_sec = 10.0

    def _current_stripe_mode(self) -> str:
        mode = str(getattr(self.config, "stripe_mode", "test")).strip().lower()
        return mode if mode in {"test", "live"} else "test"

    def _try_auto_assign_grandfathered(self) -> None:
        """
        Optional one-time-at-startup auto-backfill for existing users.
        Source of Truth remains subscriptions.status.
        """
        if self._repository is None:
            return
        if not self.config.grandfathered_enabled:
            return
        if not getattr(self.config, "grandfather_auto_assign_existing", False):
            return

        cutoff_date = (getattr(self.config, "grandfather_cutoff_date", "") or "").strip()

        if not cutoff_date:
            logger.warning(
                "[F-2025-017] Auto-grandfather enabled but SUBSCRIPTION_GRANDFATHER_CUTOFF_DATE is empty; skipping"
            )
            return

        try:
            datetime.strptime(cutoff_date, "%Y-%m-%d")
            result = self._repository.apply_grandfather_bootstrap_once(cutoff_date)
            if result.get("applied"):
                logger.info(
                    "[F-2025-017] Auto-grandfather bootstrap applied once: updated=%s cutoff_date=%s event_id=%s",
                    result.get("updated_count", 0),
                    cutoff_date,
                    result.get("event_id"),
                )
            else:
                logger.info(
                    "[F-2025-017] Auto-grandfather bootstrap skipped: already_applied cutoff_date=%s event_id=%s",
                    cutoff_date,
                    result.get("event_id"),
                )
        except ValueError:
            logger.error(
                "[F-2025-017] Invalid SUBSCRIPTION_GRANDFATHER_CUTOFF_DATE=%s (expected YYYY-MM-DD)",
                cutoff_date,
            )
        except Exception as e:
            logger.error(f"[F-2025-017] Auto-grandfather failed: {e}")

    def _validate_active_mode_config(self) -> bool:
        """
        Validate Stripe config for active mode to prevent hidden test/live drift.
        """
        mode = self._current_stripe_mode()
        secret = str(getattr(self.config, "stripe_secret_key", "") or "").strip()
        publishable = str(getattr(self.config, "stripe_publishable_key", "") or "").strip()
        webhook = str(getattr(self.config, "stripe_webhook_secret", "") or "").strip()
        price_id = str(getattr(self.config, "stripe_price_id", "") or "").strip()

        expected_secret_prefixes = ("sk_live_", "rk_live_") if mode == "live" else ("sk_test_", "rk_test_")
        expected_publishable_prefix = "pk_live_" if mode == "live" else "pk_test_"

        errors: list[str] = []
        if not secret:
            errors.append("stripe_secret_key is empty")
        elif not secret.startswith(expected_secret_prefixes):
            errors.append(
                f"stripe_secret_key must start with {expected_secret_prefixes} for mode={mode}"
            )

        if not publishable:
            errors.append("stripe_publishable_key is empty")
        elif not publishable.startswith(expected_publishable_prefix):
            errors.append(
                f"stripe_publishable_key must start with {expected_publishable_prefix} for mode={mode}"
            )

        if not webhook:
            errors.append("stripe_webhook_secret is empty")
        elif not webhook.startswith("whsec_"):
            errors.append("stripe_webhook_secret must start with whsec_")

        if not price_id:
            errors.append("stripe_price_id is empty")
        elif not price_id.startswith("price_"):
            errors.append("stripe_price_id must start with price_")

        if errors:
            logger.error(
                "[F-2025-017] Stripe config validation failed for mode=%s: %s",
                mode,
                "; ".join(errors),
            )
            return False
        return True

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
            self._try_auto_assign_grandfathered()
            
            if not self._validate_active_mode_config():
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
            result["stripe_mode"] = self._current_stripe_mode()
            return result
            
        except Exception as e:
            if self._looks_like_missing_customer_error(e):
                logger.warning(
                    f"[F-2025-017] Portal customer invalid for {hardware_id}; clearing stripe_customer_id to recover checkout path"
                )
                try:
                    self._repository.update_subscription(hardware_id, stripe_customer_id=None)
                    self.invalidate_all_cache()
                except Exception as recover_err:
                    logger.error(
                        f"[F-2025-017] Failed to clear stale stripe_customer_id for {hardware_id}: {recover_err}"
                    )
            logger.error(f"[F-2025-017] Error creating portal session: {e}")
            return None

    @staticmethod
    def _looks_like_missing_customer_error(error: Exception) -> bool:
        """Detect stale/invalid Stripe customer errors for safe local recovery."""
        text = str(error).strip().lower()
        if not text:
            return False
        if "no such customer" in text:
            return True
        if "customer" in text and "does not exist" in text:
            return True
        if "resource_missing" in text and "customer" in text:
            return True
        return False

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
            now_utc = datetime.now(timezone.utc)

            # 1.1 Server-side anti-spam/reuse guard: re-use recent open checkout session.
            if sub:
                last_session_id = sub.get("last_checkout_session_id")
                last_created_at = self._coerce_utc_datetime(sub.get("last_checkout_created_at"))
                age_sec = (now_utc - last_created_at).total_seconds() if last_created_at else None
                if (
                    last_session_id
                    and age_sec is not None
                    and age_sec <= self._checkout_reuse_window_sec
                ):
                    try:
                        existing = self._stripe_service.get_checkout_session(last_session_id)
                        if existing and existing.get("status") == "open":
                            logger.info(
                                "[F-2025-017] Reusing recent open checkout session",
                                extra={
                                    "scope": "subscription",
                                    "decision": "checkout_reuse",
                                    "ctx": {
                                        "hardware_id": hardware_id,
                                        "session_id": last_session_id,
                                        "age_sec": round(age_sec, 1),
                                    },
                                },
                            )
                            return {
                                "checkout_url": existing.get("url"),
                                "session_id": existing.get("id"),
                                "customer_id": existing.get("customer_id"),
                                "subscription_id": existing.get("subscription_id"),
                                "reused": True,
                                "stripe_mode": self._current_stripe_mode(),
                            }
                    except Exception as reuse_error:
                        logger.warning(
                            f"[F-2025-017] Checkout reuse probe failed, creating new session: {reuse_error}"
                        )

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
            # Persist linkage + checkout dedup metadata immediately.
            self._repository.update_subscription(
                hardware_id=hardware_id,
                stripe_customer_id=result.get("customer_id"),
                stripe_subscription_id=result.get("subscription_id"),
                last_checkout_session_id=result.get("session_id"),
                last_checkout_created_at=now_utc,
            )
            self.invalidate_all_cache()
            result["stripe_mode"] = self._current_stripe_mode()
            return result
            
        except Exception as e:
            logger.error(f"[F-2025-017] Error creating checkout session: {e}")
            return None

    @staticmethod
    def _coerce_utc_datetime(value: Any) -> Optional[datetime]:
        """Normalize DB datetime values (aware/naive/epoch/iso) for checkout reuse guard."""
        if value is None:
            return None
        if isinstance(value, datetime):
            return value if value.tzinfo else value.replace(tzinfo=timezone.utc)
        if isinstance(value, (int, float)):
            return datetime.fromtimestamp(value, tz=timezone.utc)
        if isinstance(value, str):
            raw = value.strip()
            if not raw:
                return None
            if raw.isdigit():
                return datetime.fromtimestamp(int(raw), tz=timezone.utc)
            try:
                parsed = datetime.fromisoformat(raw.replace("Z", "+00:00"))
                return parsed if parsed.tzinfo else parsed.replace(tzinfo=timezone.utc)
            except ValueError:
                return None
        return None

    @staticmethod
    def _serialize_current_period_end(value: Any) -> Any:
        """Return JSON-safe current_period_end while keeping existing numeric/string contract."""
        if isinstance(value, datetime):
            normalized = value if value.tzinfo else value.replace(tzinfo=timezone.utc)
            return normalized.isoformat()
        return value

    @staticmethod
    def _recommended_billing_route(sub: Dict[str, Any]) -> str:
        status = str(sub.get("status") or "").strip().lower()
        # For unpaid/free-limited users always start with checkout,
        # even if stale customer linkage exists.
        if status in {"none", "limited_free_trial"}:
            return "checkout"
        customer_id = (sub.get("stripe_customer_id") or "").strip()
        return "manage" if customer_id else "checkout"

    @staticmethod
    def _billing_action_for_status(
        *,
        active: bool,
        billing_active: bool,
        recommended_route: str,
    ) -> str:
        """
        Centralized owner decision for billing UI entrypoint.
        - none: user already has active billing access
        - manage: user should manage/resubscribe using existing customer
        - checkout: user should start new checkout flow
        """
        if active and billing_active:
            return "none"
        if recommended_route == "manage":
            return "manage"
        return "checkout"

    def _get_reconcile_lock(self, session_id: str) -> asyncio.Lock:
        """Get/create per-session async lock for checkout reconciliation."""
        with self._reconcile_locks_guard:
            lock = self._reconcile_locks.get(session_id)
            if lock is None:
                lock = asyncio.Lock()
                self._reconcile_locks[session_id] = lock
            return lock

    def _cleanup_reconcile_lock(self, session_id: str, lock: asyncio.Lock) -> None:
        """Remove lock if it is no longer in use."""
        with self._reconcile_locks_guard:
            current = self._reconcile_locks.get(session_id)
            if current is lock and not lock.locked():
                self._reconcile_locks.pop(session_id, None)

    async def reconcile_checkout_success(self, session_id: str) -> Dict[str, Any]:
        """
        Fallback synchronization path for successful checkout redirect.
        Source of truth remains Stripe checkout/subscription objects.
        """
        if not self._initialized or not self.config.is_active():
            return {"ok": False, "reason": "subscription_disabled"}
        if self._repository is None or self._stripe_service is None:
            return {"ok": False, "reason": "not_initialized"}

        lock = self._get_reconcile_lock(session_id)
        try:
            async with lock:
                session = self._stripe_service.get_checkout_session(session_id)
                if not session:
                    return {"ok": False, "reason": "session_not_found"}

                if session.get("status") != "complete" or session.get("payment_status") != "paid":
                    return {
                        "ok": False,
                        "reason": "session_not_paid",
                        "status": session.get("status"),
                        "payment_status": session.get("payment_status"),
                    }

                metadata = session.get("metadata") or {}
                hardware_id = metadata.get("hardware_id")
                subscription_id = session.get("subscription_id")
                customer_id = session.get("customer_id")

                if not hardware_id and subscription_id:
                    sub_row = self._repository.get_subscription_by_stripe_subscription_id(subscription_id)
                    hardware_id = sub_row.get("hardware_id") if sub_row else None
                if not hardware_id and customer_id:
                    sub_row = self._repository.get_subscription_by_stripe_customer_id(customer_id)
                    hardware_id = sub_row.get("hardware_id") if sub_row else None
                if not hardware_id:
                    return {"ok": False, "reason": "hardware_id_not_resolved"}

                stripe_status = "active"
                current_period_end = None
                cancel_at_period_end = False
                if subscription_id:
                    stripe_sub = self._stripe_service.get_subscription(subscription_id)
                    stripe_status = stripe_sub.get("status") or "active"
                    current_period_end = stripe_sub.get("current_period_end")
                    cancel_at_period_end = bool(stripe_sub.get("cancel_at_period_end", False))

                local_status = map_stripe_status_to_local_status(stripe_status, "paid")
                updated = self._repository.update_subscription(
                    hardware_id=hardware_id,
                    status=local_status,
                    stripe_status=stripe_status,
                    stripe_customer_id=customer_id,
                    stripe_subscription_id=subscription_id,
                    current_period_end=current_period_end,
                    cancel_at_period_end=cancel_at_period_end,
                    last_stripe_event_id=f"checkout_session:{session_id}",
                    last_stripe_event_at=datetime.now(timezone.utc),
                )
                # If test reset removed the row, create it and retry update.
                if not updated:
                    self._repository.create_subscription(
                        hardware_id=hardware_id,
                        status=local_status,
                    )
                    updated = self._repository.update_subscription(
                        hardware_id=hardware_id,
                        status=local_status,
                        stripe_status=stripe_status,
                        stripe_customer_id=customer_id,
                        stripe_subscription_id=subscription_id,
                        current_period_end=current_period_end,
                        cancel_at_period_end=cancel_at_period_end,
                        last_stripe_event_id=f"checkout_session:{session_id}",
                        last_stripe_event_at=datetime.now(timezone.utc),
                    )
                if not updated:
                    return {"ok": False, "reason": "subscription_update_failed"}
                self.invalidate_all_cache()
                return {
                    "ok": True,
                    "hardware_id": hardware_id,
                    "status": local_status,
                    "stripe_status": stripe_status,
                    "subscription_id": subscription_id,
                }
        except Exception as e:
            logger.error(f"[F-2025-017] reconcile_checkout_success failed: {e}")
            return {"ok": False, "reason": "exception", "error": str(e)}
        finally:
            self._cleanup_reconcile_lock(session_id, lock)
    
    async def get_subscription_status(self, hardware_id: str) -> Dict[str, Any]:
        """
        Получить текущий статус подписки для поллинга.
        
        Args:
            hardware_id: ID устройства
            
        Returns:
            Dict со статусом и метаданными
        """
        if not self._initialized or not self.config.is_active():
            return {'status': 'unknown', 'active': False, 'stripe_mode': self._current_stripe_mode()}
        if self._repository is None:
            return {'status': 'unknown', 'active': False, 'stripe_mode': self._current_stripe_mode()}
            
        try:
            sub = self._repository.get_subscription(hardware_id)
            if not sub:
                return {
                    'status': 'none',
                    'active': False,
                    'billing_active': False,
                    'recommended_billing_route': 'checkout',
                    'billing_action': 'checkout',
                    'stripe_mode': self._current_stripe_mode(),
                }
            sub = self._lazy_sync_subscription_status(hardware_id, sub)
            status = sub.get('status')
            tier = map_status_to_tier(
                status,
                grandfathered_enabled=self.config.grandfathered_enabled
            )
            active = tier in [AccessTier.UNLIMITED, AccessTier.LIMITED]
            billing_active = tier == AccessTier.UNLIMITED
            recommended_billing_route = self._recommended_billing_route(sub)

            return {
                'status': status,
                'stripe_status': sub.get('stripe_status'),
                'email': sub.get('email'),
                # active=true means user can use product now (unlimited or limited tier)
                'active': active,
                'billing_active': billing_active,
                'cancel_at_period_end': bool(sub.get('cancel_at_period_end', False)),
                'recommended_billing_route': recommended_billing_route,
                'billing_action': self._billing_action_for_status(
                    active=active,
                    billing_active=billing_active,
                    recommended_route=recommended_billing_route,
                ),
                'current_period_end': self._serialize_current_period_end(sub.get('current_period_end')),
                'stripe_mode': self._current_stripe_mode(),
            }
            
        except Exception as e:
            logger.error(f"[F-2025-017] Error getting subscription status: {e}")
            return {'status': 'error', 'message': str(e), 'stripe_mode': self._current_stripe_mode()}

    def _try_acquire_status_sync_slot(self, hardware_id: str) -> bool:
        """
        Rate-limit Stripe reads per hardware_id to avoid noisy polling bursts.
        """
        now_ts = datetime.now().timestamp()
        with self._status_sync_lock:
            last_ts = self._status_sync_last_run.get(hardware_id)
            if last_ts is not None and (now_ts - last_ts) < self._status_sync_min_interval_sec:
                return False
            self._status_sync_last_run[hardware_id] = now_ts
            return True

    def _lazy_sync_subscription_status(
        self, hardware_id: str, sub: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Best-effort status sync from Stripe to reduce dependency on webhook delivery.
        Source of Truth remains SubscriptionModule + repository row.
        """
        if self._repository is None or self._stripe_service is None:
            return sub

        subscription_id = (sub.get("stripe_subscription_id") or "").strip()
        if not subscription_id:
            return sub

        if not self._try_acquire_status_sync_slot(hardware_id):
            return sub

        try:
            stripe_sub = self._stripe_service.get_subscription(subscription_id)
        except Exception as e:
            logger.debug(
                f"[F-2025-017] Lazy Stripe sync skipped (read failed) for {hardware_id[:8]}...: {e}"
            )
            return sub

        stripe_status = stripe_sub.get("status")
        local_status = map_stripe_status_to_local_status(stripe_status, sub.get("status"))
        updates: Dict[str, Any] = {}

        if local_status and local_status != sub.get("status"):
            updates["status"] = local_status
        if stripe_status and stripe_status != sub.get("stripe_status"):
            updates["stripe_status"] = stripe_status

        current_period_end = stripe_sub.get("current_period_end")
        if current_period_end != sub.get("current_period_end"):
            updates["current_period_end"] = current_period_end

        cancel_at_period_end = bool(stripe_sub.get("cancel_at_period_end", False))
        if cancel_at_period_end != bool(sub.get("cancel_at_period_end", False)):
            updates["cancel_at_period_end"] = cancel_at_period_end

        if not updates:
            return sub

        try:
            updated = self._repository.update_subscription(hardware_id, **updates)
            if not updated:
                return sub
            merged = dict(sub)
            merged.update(updates)
            self._invalidate_cache(hardware_id)
            logger.info(
                "[F-2025-017] Lazy Stripe sync applied",
                extra={
                    "scope": "subscription",
                    "decision": "lazy_sync_applied",
                    "ctx": {
                        "hardware_id": hardware_id,
                        "status": merged.get("status"),
                        "stripe_status": merged.get("stripe_status"),
                        "cancel_at_period_end": merged.get("cancel_at_period_end"),
                    },
                },
            )
            return merged
        except Exception as e:
            logger.debug(
                f"[F-2025-017] Lazy Stripe sync update failed for {hardware_id[:8]}...: {e}"
            )
            return sub

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
            cancel_at_period_end = bool(sub_details.get('cancel_at_period_end', False))
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
                if cancel_at_period_end:
                    return f"[Subscription: Paid (Cancelled, Active until period end){date_str}]"
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
        with self._status_sync_lock:
            self._status_sync_last_run.clear()
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
