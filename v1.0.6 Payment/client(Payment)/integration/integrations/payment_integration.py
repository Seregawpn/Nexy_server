#!/usr/bin/env python3
"""
Payment Integration - обработка deep links для платежной системы

Feature ID: F-2025-017-stripe-payment
MVP 9: Deep Links клиентская часть
"""
import logging
from typing import Dict, Any, Optional
from urllib.parse import urlparse, parse_qs

from integration.core.base_integration import BaseIntegration

logger = logging.getLogger(__name__)


class PaymentIntegration(BaseIntegration):
    """Обработка платежных deep links"""
    
    def __init__(
        self,
        event_bus,
        state_manager,
        error_handler
    ):
        super().__init__(
            event_bus=event_bus,
            state_manager=state_manager,
            error_handler=error_handler,
            name="PaymentIntegration"
        )
        self._pending_sync = False
    
    async def _do_initialize(self) -> bool:
        """Инициализация интеграции"""
        try:
            # Подписка на deep link события
            await self.event_bus.subscribe("deep_link.payment", self._handle_payment_deep_link)
            
            # Подписка на события приложения (для обработки URL при запуске)
            await self.event_bus.subscribe("app.url_opened", self._handle_app_url_opened)
            
            logger.info("[F-2025-017-stripe-payment] PaymentIntegration initialized")
            return True
        except Exception as e:
            logger.error(f"[F-2025-017-stripe-payment] PaymentIntegration initialization error: {e}")
            return False
    
    async def _do_start(self) -> bool:
        """Запуск интеграции"""
        logger.info("[F-2025-017-stripe-payment] PaymentIntegration started")
        return True
    
    async def _do_stop(self) -> bool:
        """Остановка интеграции"""
        logger.info("[F-2025-017-stripe-payment] PaymentIntegration stopped")
        return True
    
    async def _handle_app_url_opened(self, event_data: Dict[str, Any]):
        """Обработка URL при открытии приложения"""
        url = event_data.get("url", "")
        if url.startswith("nexy://payment/"):
            await self._handle_payment_deep_link({"url": url})
    
    async def _handle_payment_deep_link(self, event_data: Dict[str, Any]):
        """Обработка платежного deep link"""
        try:
            url = event_data.get("url", "")
            if not url:
                logger.warning("[F-2025-017-stripe-payment] Empty URL in deep link event")
                return
            
            # Парсим URL
            parsed = urlparse(url)
            path = parsed.path.strip('/')
            
            logger.info(f"[F-2025-017-stripe-payment] Processing payment deep link: {url}")
            
            # Определяем тип события
            if path == "payment/success":
                session_id = parsed.query.split('session_id=')[1].split('&')[0] if 'session_id=' in parsed.query else None
                await self._handle_payment_success(session_id)
            elif path == "payment/cancel":
                await self._handle_payment_cancel()
            elif path == "payment/portal_return":
                await self._handle_portal_return()
            else:
                logger.warning(f"[F-2025-017-stripe-payment] Unknown payment deep link path: {path}")
                
        except Exception as e:
            logger.error(f"[F-2025-017-stripe-payment] Error handling payment deep link: {e}")
            await self._handle_error(e, where="handle_payment_deep_link")
    
    async def _handle_payment_success(self, session_id: Optional[str]):
        """Обработка успешной подписки"""
        try:
            logger.info(f"[F-2025-017-stripe-payment] Payment success: session_id={session_id}")
            
            # Публикуем событие успешной подписки
            await self.event_bus.publish(
                "payment.success",
                {
                    "session_id": session_id,
                    "timestamp": self._get_timestamp()
                }
            )
            
            # Синхронизируем статус подписки
            await self._sync_subscription()
            
        except Exception as e:
            logger.error(f"[F-2025-017-stripe-payment] Error handling payment success: {e}")
            await self._handle_error(e, where="handle_payment_success")
    
    async def _handle_payment_cancel(self):
        """Обработка отмены подписки"""
        try:
            logger.info("[F-2025-017-stripe-payment] Payment cancelled")
            
            # Публикуем событие отмены
            await self.event_bus.publish(
                "payment.cancel",
                {
                    "timestamp": self._get_timestamp()
                }
            )
            
        except Exception as e:
            logger.error(f"[F-2025-017-stripe-payment] Error handling payment cancel: {e}")
            await self._handle_error(e, where="handle_payment_cancel")
    
    async def _handle_portal_return(self):
        """Обработка возврата из Customer Portal"""
        try:
            logger.info("[F-2025-017-stripe-payment] Portal return")
            
            # Публикуем событие возврата из Portal
            await self.event_bus.publish(
                "payment.portal_return",
                {
                    "timestamp": self._get_timestamp()
                }
            )
            
            # Синхронизируем статус подписки
            await self._sync_subscription()
            
        except Exception as e:
            logger.error(f"[F-2025-017-stripe-payment] Error handling portal return: {e}")
            await self._handle_error(e, where="handle_portal_return")
    
    async def _sync_subscription(self):
        """Синхронизация статуса подписки с сервером"""
        try:
            # Получаем hardware_id из state_manager
            hardware_id = self.state_manager.get_hardware_id()
            if not hardware_id:
                logger.warning("[F-2025-017-stripe-payment] Cannot sync: hardware_id not found")
                return
            
            logger.info(f"[F-2025-017-stripe-payment] Syncing subscription for {hardware_id[:8]}...")
            
            # Публикуем событие для синхронизации (GrpcClientIntegration должен обработать)
            await self.event_bus.publish(
                "payment.sync_request",
                {
                    "hardware_id": hardware_id,
                    "timestamp": self._get_timestamp()
                }
            )
            
        except Exception as e:
            logger.error(f"[F-2025-017-stripe-payment] Error syncing subscription: {e}")
            await self._handle_error(e, where="sync_subscription")
    
    def _get_timestamp(self) -> float:
        """Получить текущий timestamp"""
        import time
        return time.time()
    
    async def _handle_error(self, error: Exception, where: str):
        """Обработка ошибок"""
        await self.error_handler.handle_error(
            error=error,
            context=f"PaymentIntegration.{where}",
            feature_id="F-2025-017-stripe-payment"
        )

