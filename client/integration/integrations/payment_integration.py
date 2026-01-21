#!/usr/bin/env python3
"""
Payment Integration - Client Side
Feature ID: F-2025-017-stripe-payment

Эта интеграция отвечает за:
1. Обработку deep links (nexy://payment/*) -> публикация в EventBus
2. Подписку на обновление статуса (subscription.status_updated) -> обновление локального кэша/UI
3. Запрос синхронизации статуса с сервера

⚠️ КРИТИЧНО: Никакой бизнес-логики или расчёта квот на клиенте!
Только отображение того, что прислал сервер.
"""
import logging
from typing import Dict, Any, Optional

from integration.core.base_integration import BaseIntegration
from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler

logger = logging.getLogger(__name__)


class PaymentIntegration(BaseIntegration):
    """
    Интеграция платежной системы на клиенте.
    Слушает EventBus и управляет отображением статуса подписки.
    """
    
    def __init__(
        self,
        event_bus: EventBus,
        state_manager: ApplicationStateManager,
        error_handler: ErrorHandler,
    ):
        super().__init__(
            event_bus=event_bus,
            state_manager=state_manager,
            error_handler=error_handler,
            name="Payment"
        )
        self.feature_id = "F-2025-017-stripe-payment"
        # Локальный кэш статуса (только для UI)
        self._subscription_status: Dict[str, Any] = {
            'status': 'unknown',
            'active': False,
            'limits': None
        }
        
    async def _do_initialize(self) -> bool:
        """Инициализация интеграции"""
        logger.info(f"[{self.feature_id}] Initializing PaymentIntegration")
        
        # Подписка на события обновления статуса
        await self.event_bus.subscribe("subscription.status_updated", self._on_status_updated)
        
        # Подписка на deep links
        await self.event_bus.subscribe("navigation.deep_link", self._on_deep_link)
        
        # Подписка на событие успешного подключения к серверу
        await self.event_bus.subscribe("grpc.connected", self._on_server_connected)
        
        return True

    async def _do_start(self) -> bool:
        """Запуск интеграции"""
        logger.info(f"[{self.feature_id}] Starting PaymentIntegration")
        return True

    async def _do_stop(self) -> bool:
        """Остановка интеграции"""
        return True
        
    # --- Event Handlers ---

    async def _on_status_updated(self, payload: Dict[str, Any]):
        """
        Обработка обновления статуса подписки от сервера.
        EventBus: subscription.status_updated
        """
        logger.info(f"[{self.feature_id}] Received subscription status update: {payload}")
        
        status = payload.get('status')
        limits = payload.get('limits')
        reason = payload.get('reason')
        
        # Обновляем локальный кэш
        self._subscription_status = payload
        
        # Публикуем событие для UI (если UI подсаживается на другое событие)
        # В данном случае UI может слушать то же самое subscription.status_updated
        
    async def _on_deep_link(self, payload: Dict[str, Any]):
        """
        Обработка deep link.
        EventBus: navigation.deep_link {url: "nexy://payment/sample"}
        """
        url = payload.get('url', '')
        if not url.startswith('nexy://payment/'):
            return
            
        logger.info(f"[{self.feature_id}] Processing deep link: {url}")
        
        # Парсим URL
        # nexy://payment/success?session_id=...
        # nexy://payment/cancel
        # nexy://payment/billing_portal
        
        path = url.replace('nexy://payment/', '')
        action = path.split('?')[0]
        
        # Публикуем событие о получении deep link для аналитики и трекинга
        await self.event_bus.publish("payment.deep_link_received", {
            'url': url,
            'action': action,
            'timestamp': payload.get('timestamp')
        })
        
        if action == 'success':
            # Оплата прошла успешно - запрашиваем синхронизацию статуса
            logger.info(f"[{self.feature_id}] Payment successful deep link received. Requesting sync.")
            await self.event_bus.publish("payment.sync_requested", {
                'reason': 'deep_link_success'
            })
            
            # Показываем уведомление пользователю
            await self.event_bus.publish("ui.notification.show", {
                'type': 'success',
                'title': 'Payment Successful',
                'message': 'Thank you for your subscription! Updating status...'
            })

        elif action == 'cancel':
            logger.info(f"[{self.feature_id}] Payment cancelled deep link received.")
            await self.event_bus.publish("ui.notification.show", {
                'type': 'info',
                'title': 'Payment Cancelled',
                'message': 'The payment process was cancelled.'
            })
            
        elif action == 'billing_problem':
            logger.warning(f"[{self.feature_id}] Billing problem deep link received.")
            await self.event_bus.publish("ui.notification.show", {
                'type': 'error',
                'title': 'Payment Issue',
                'message': 'There was an issue with your payment. Please check your billing details.'
            })

    async def _on_server_connected(self, payload: Dict[str, Any]):
        """
        При подключении к серверу запрашиваем актуальный статус.
        """
        logger.info(f"[{self.feature_id}] Server connected. Requesting subscription status sync.")
        await self.event_bus.publish("payment.sync_requested", {
            'reason': 'reconnect'
        })
    
    # --- Public API (for other client modules) ---
    
    def get_local_status(self) -> Dict[str, Any]:
        """
        Получить ТЕКУЩИЙ известный статус (из кэша).
        НЕ делает запрос к серверу.
        """
        return self._subscription_status
