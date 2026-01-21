# 🔗 План обработки Deep Links на клиенте

**Feature ID:** F-2025-017-stripe-payment  
**Date:** 2025-12-09

---

## 📋 Обзор

Этот документ описывает детальный план обработки deep links `nexy://payment/*` на клиенте для возврата из Stripe Checkout и Customer Portal.

---

## 🔗 URL Schemes

### Поддерживаемые URL

1. **Success:** `nexy://payment/success?session_id={CHECKOUT_SESSION_ID}`
2. **Cancel:** `nexy://payment/cancel`
3. **Portal Return:** `nexy://payment/portal_return`

---

## 📱 Регистрация URL Scheme

### Файл: `client(Messages)/Info.plist`

```xml
<key>CFBundleURLTypes</key>
<array>
    <dict>
        <key>CFBundleURLSchemes</key>
        <array>
            <string>nexy</string>
        </array>
        <key>CFBundleURLName</key>
        <string>com.nexy.payment</string>
        <key>CFBundleTypeRole</key>
        <string>Editor</string>
    </dict>
</array>
```

**Альтернатива:** Если используется Xcode, добавить в Target → Info → URL Types

---

## 🔧 Реализация на клиенте

### Файл: `client(Messages)/integration/integrations/payment_integration.py` (NEW)

```python
"""
Payment Integration - обработка deep links для платежной системы
"""
import logging
from typing import Dict, Any, Optional
from urllib.parse import urlparse, parse_qs

from integration.core.base_integration import BaseIntegration
from integration.core.event_bus import EventBus
from modules.grpc_client.core.grpc_client import GrpcClient

logger = logging.getLogger(__name__)

class PaymentIntegration(BaseIntegration):
    """Обработка платежных deep links"""
    
    def __init__(
        self,
        event_bus: EventBus,
        grpc_client: GrpcClient,
        state_manager: 'ApplicationStateManager',
        error_handler: 'ErrorHandler'
    ):
        super().__init__(
            event_bus=event_bus,
            state_manager=state_manager,
            error_handler=error_handler,
            name="PaymentIntegration"
        )
        self._grpc_client = grpc_client
        self._pending_sync = False
    
    async def initialize(self):
        """Инициализация интеграции"""
        # Подписка на deep link события
        await self.event_bus.subscribe("deep_link.payment", self._handle_payment_deep_link)
        
        # Подписка на события приложения (для обработки URL при запуске)
        await self.event_bus.subscribe("app.url_opened", self._handle_app_url_opened)
        
        logger.info("[F-2025-017-stripe-payment] PaymentIntegration initialized")
    
    async def _handle_app_url_opened(self, event_data: Dict[str, Any]):
        """Обработка URL при открытии приложения"""
        url = event_data.get("url", "")
        if url.startswith("nexy://payment/"):
            await self._handle_payment_deep_link({"url": url})
    
    async def _handle_payment_deep_link(self, event_data: Dict[str, Any]):
        """Обработка nexy://payment/* URLs"""
        url = event_data.get("url", "")
        
        if not url or not url.startswith("nexy://payment/"):
            logger.warning(
                f"[F-2025-017-stripe-payment] Invalid payment URL format: {url}",
                extra={"url": url}
            )
            return
        
        try:
            parsed = urlparse(url)
            path_parts = parsed.path.strip('/').split('/')
            action = path_parts[-1] if path_parts else None
            params = parse_qs(parsed.query)
            
            logger.info(
                f"[F-2025-017-stripe-payment] Processing payment deep link: {action}",
                extra={"url": url, "action": action, "params": params}
            )
            
            if action == "success":
                session_id = params.get("session_id", [None])[0]
                await self._handle_payment_success(session_id)
            elif action == "cancel":
                await self._handle_payment_cancel()
            elif action == "portal_return":
                await self._handle_portal_return()
            else:
                logger.warning(
                    f"[F-2025-017-stripe-payment] Unknown payment action: {action}",
                    extra={"url": url}
                )
        except Exception as e:
            logger.exception(
                f"[F-2025-017-stripe-payment] Error processing payment URL: {e}",
                extra={"url": url}
            )
            self.error_handler.handle_error(e, context="payment_deep_link")
    
    async def _handle_payment_success(self, session_id: Optional[str]):
        """Обработка успешной подписки"""
        logger.info(
            f"[F-2025-017-stripe-payment] Payment success: {session_id}",
            extra={"session_id": session_id}
        )
        
        # Публикация события для синхронизации
        await self.event_bus.publish("payment.success", {
            "session_id": session_id,
            "timestamp": self._get_timestamp()
        })
        
        # Синхронизация подписки с сервером
        await self._sync_subscription()
        
        # Уведомление пользователя (опционально)
        # Можно показать уведомление или воспроизвести TTS
        
    async def _handle_payment_cancel(self):
        """Обработка отмены подписки"""
        logger.info("[F-2025-017-stripe-payment] Payment cancelled by user")
        
        # Публикация события
        await self.event_bus.publish("payment.cancel", {
            "timestamp": self._get_timestamp()
        })
        
        # Синхронизация (на случай, если статус изменился)
        await self._sync_subscription()
    
    async def _handle_portal_return(self):
        """Обработка возврата из Customer Portal"""
        logger.info("[F-2025-017-stripe-payment] Returned from Customer Portal")
        
        # Публикация события
        await self.event_bus.publish("payment.portal_return", {
            "timestamp": self._get_timestamp()
        })
        
        # Синхронизация подписки (могли изменить payment method, отменить подписку и т.д.)
        await self._sync_subscription()
    
    async def _sync_subscription(self):
        """Синхронизация статуса подписки с сервером"""
        try:
            hardware_id = self.state_manager.get_hardware_id()
            if not hardware_id:
                logger.warning("[F-2025-017-stripe-payment] No hardware_id for sync")
                return
            
            # Запрос к серверу для получения актуального статуса
            # Это можно сделать через специальный RPC или через обычный запрос
            # Пока используем обычный запрос с специальным prompt
            
            logger.info(
                f"[F-2025-017-stripe-payment] Syncing subscription status",
                extra={"hardware_id": hardware_id[:8] + "..."}  # Маскирование
            )
            
            # Инвалидация локального кэша (если есть)
            # Сервер обновит кэш при следующем запросе
            
        except Exception as e:
            logger.exception(
                f"[F-2025-017-stripe-payment] Error syncing subscription: {e}"
            )
    
    def _get_timestamp(self) -> float:
        """Получение текущего timestamp"""
        import time
        return time.time()
```

---

## 🔄 Интеграция с существующими компонентами

### 1. Регистрация в SimpleModuleCoordinator

**Файл:** `client(Messages)/integration/core/simple_module_coordinator.py`

```python
# В методе _initialize_integrations()
from integration.integrations.payment_integration import PaymentIntegration

# Создание PaymentIntegration
payment_integration = PaymentIntegration(
    event_bus=self.event_bus,
    grpc_client=grpc_client,
    state_manager=self.state_manager,
    error_handler=self.error_handler
)

# Регистрация
self._integrations["payment"] = payment_integration
await payment_integration.initialize()
```

---

### 2. Обработка URL при запуске приложения

**Файл:** `client(Messages)/main.py` или AppDelegate

```python
# В обработчике открытия URL
def application(_ application: NSApplication, open urls: [URL]) -> Bool {
    for url in urls {
        if url.scheme == "nexy" && url.host == "payment" {
            // Публикация события
            event_bus.publish("deep_link.payment", {"url": url.absoluteString})
        }
    }
    return true
}
```

---

## 🧪 Тестирование

### Unit тесты

**Файл:** `client(Messages)/tests/test_payment_integration.py`

```python
import pytest
from unittest.mock import AsyncMock, MagicMock
from integration.integrations.payment_integration import PaymentIntegration

@pytest.mark.asyncio
async def test_payment_success_deep_link():
    """Тест обработки success deep link"""
    event_bus = AsyncMock()
    grpc_client = MagicMock()
    state_manager = MagicMock()
    error_handler = MagicMock()
    
    integration = PaymentIntegration(
        event_bus=event_bus,
        grpc_client=grpc_client,
        state_manager=state_manager,
        error_handler=error_handler
    )
    
    await integration._handle_payment_deep_link({
        "url": "nexy://payment/success?session_id=cs_test_123"
    })
    
    # Проверка публикации события
    event_bus.publish.assert_called_with("payment.success", ...)

@pytest.mark.asyncio
async def test_payment_cancel_deep_link():
    """Тест обработки cancel deep link"""
    # Аналогично

@pytest.mark.asyncio
async def test_invalid_url_format():
    """Тест обработки невалидного URL"""
    # Должен игнорироваться
```

---

## 📋 Чеклист реализации

- [ ] Добавить URL scheme в Info.plist
- [ ] Создать `PaymentIntegration` класс
- [ ] Реализовать обработку success URL
- [ ] Реализовать обработку cancel URL
- [ ] Реализовать обработку portal_return URL
- [ ] Реализовать синхронизацию подписки
- [ ] Зарегистрировать в `SimpleModuleCoordinator`
- [ ] Добавить обработку URL при запуске приложения
- [ ] Создать unit тесты
- [ ] Протестировать на реальном устройстве

---

**Статус:** ✅ Готово к реализации




