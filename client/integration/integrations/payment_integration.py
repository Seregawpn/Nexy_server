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

import asyncio
import logging
import time
from typing import Any

import aiohttp

from integration.core.base_integration import BaseIntegration
from integration.core.error_handler import ErrorHandler
from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager

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
            name="Payment",
        )
        self.feature_id = "F-2025-017-stripe-payment"
        # Локальный кэш статуса (только для UI)
        self._subscription_status: dict[str, Any] = {
            "status": "unknown",
            "active": False,
            "limits": None,
        }
        self._hardware_id: str | None = None
        self._poll_task: asyncio.Task[Any] | None = None
        self._payment_success_announced_at: float | None = None
        self._checkout_in_flight: bool = False
        self._last_checkout_session_id: str | None = None
        self._last_checkout_opened_at: float | None = None
        self._checkout_dedup_window_sec: float = 10.0

    async def _do_initialize(self) -> bool:
        """Инициализация интеграции"""
        logger.info(f"[{self.feature_id}] Initializing PaymentIntegration")

        # Подписка на события обновления статуса
        await self.event_bus.subscribe("subscription.status_updated", self._on_status_updated)

        # Запрос синхронизации статуса (deep link / reconnect / manual)
        await self.event_bus.subscribe("payment.sync_requested", self._on_payment_sync_requested)

        # Подписка на deep links
        await self.event_bus.subscribe("navigation.deep_link", self._on_deep_link)

        # Подписка на событие успешного подключения к серверу
        await self.event_bus.subscribe("grpc.connected", self._on_server_connected)

        # Подписка на действия UI
        await self.event_bus.subscribe(
            "ui.action.manage_subscription", self._on_manage_subscription
        )
        await self.event_bus.subscribe("ui.action.buy_subscription", self._on_buy_subscription)

        # Подписка на Hardware ID
        await self.event_bus.subscribe("hardware.id_obtained", self._on_hardware_id_received)
        await self.event_bus.subscribe("hardware.id_response", self._on_hardware_id_received)

        return True

    async def _do_start(self) -> bool:
        """Запуск интеграции"""
        logger.info(f"[{self.feature_id}] Starting PaymentIntegration")
        # Запрашиваем Hardware ID (если он уже доступен)
        await self.event_bus.publish("hardware.id_request", {"wait_ready": False})
        return True

    async def _do_stop(self) -> bool:
        """Остановка интеграции"""
        return True

    # --- Event Handlers ---

    async def _on_buy_subscription(self, payload: dict[str, Any]):
        """
        Обработка запроса на покупку подписки.
        EventBus: ui.action.buy_subscription
        """
        session_id = payload.get("session_id") if payload else None
        logger.info(
            f"[{self.feature_id}] Buy subscription requested via UI (session_id={session_id})"
        )
        await self.open_buy_subscription(session_id=session_id)

    async def _on_manage_subscription(self, payload: dict[str, Any]):
        """
        Обработка запроса на открытие управления подпиской (из UI/Tray).
        EventBus: ui.action.manage_subscription
        """
        logger.info(f"[{self.feature_id}] Manage subscription requested via UI")
        await self.open_manage_subscription()

    async def _on_status_updated(self, payload: dict[str, Any]):
        """
        Обработка обновления статуса подписки от сервера.
        EventBus: subscription.status_updated
        """
        logger.info(f"[{self.feature_id}] Received subscription status update: {payload}")

        # Unwrap data if nested (EventBus wrapping?)
        data = payload.get("data", payload) if isinstance(payload.get("data"), dict) else payload

        status = data.get("status")
        limits = data.get("limits")
        reason = data.get("reason")

        # Обновляем локальный кэш
        previous_status = self._subscription_status.get("status")
        if previous_status is None and isinstance(self._subscription_status.get("data"), dict):
            # Handle case where cache also has nested data
            previous_status = self._subscription_status.get("data", {}).get("status")

        self._subscription_status = (
            payload  # Keep original payload for consistency? Or store params?
        )
        # Better to store what we received logic-wise, but other parts might expect full structure.
        # Let's keep self._subscription_status as the raw payload for safety in get_local_status

        # Единая точка уведомления об успешной оплате (для всех источников)
        if status in ["paid", "paid_trial", "grandfathered"] and previous_status != status:
            await self.event_bus.publish(
                "system.notification",
                {
                    "type": "success",
                    "title": "Payment Successful!",
                    "message": "Your subscription is now active. Thank you!",
                },
            )
            if self._payment_success_announced_at is None:
                await self._announce_payment_success()
                self._payment_success_announced_at = time.time()
            await self.event_bus.publish("browser.close.request", {"reason": "payment_success"})

    async def _on_payment_sync_requested(self, payload: dict[str, Any]):
        """
        Запрос на синхронизацию статуса подписки.
        EventBus: payment.sync_requested
        """
        reason = payload.get("reason", "unknown")
        session_id = payload.get("session_id")
        session_info = f", session_id={session_id}" if session_id else ""
        logger.info(
            f"[{self.feature_id}] Payment sync requested (reason={reason}{session_info}). Starting polling."
        )
        self._ensure_polling()

    async def _on_deep_link(self, payload: dict[str, Any]):
        """
        Обработка deep link.
        EventBus: navigation.deep_link {url: "nexy://payment/sample"}
        """
        url = payload.get("url", "")
        if not url.startswith("nexy://payment/"):
            return

        logger.info(f"[{self.feature_id}] Processing deep link: {url}")

        # Парсим URL
        # nexy://payment/success?session_id=...

        path = url.replace("nexy://payment/", "")
        if "?" in path:
            action, query = path.split("?", 1)
            # Simple parsing for session_id to avoid importing urllib
            session_id = None
            for param in query.split("&"):
                if param.startswith("session_id="):
                    session_id = param.split("=", 1)[1]
                    break
        else:
            action = path
            session_id = None

        # Публикуем событие о получении deep link для аналитики и трекинга
        await self.event_bus.publish(
            "payment.deep_link_received",
            {
                "url": url,
                "action": action,
                "session_id": session_id,
                "timestamp": payload.get("timestamp"),
            },
        )

        if action == "success":
            # Оплата прошла успешно - запрашиваем синхронизацию статуса
            logger.info(
                f"[{self.feature_id}] Payment successful deep link received (session_id={session_id}). Requesting sync."
            )
            # Optimistic TTS: announce immediately, then confirm via polling
            if self._payment_success_announced_at is None:
                await self._announce_payment_success()
                self._payment_success_announced_at = time.time()
            await self.event_bus.publish(
                "payment.sync_requested", {"reason": "deep_link_success", "session_id": session_id}
            )

            # Показываем уведомление пользователю
            await self.event_bus.publish(
                "system.notification",
                {
                    "type": "success",
                    "title": "Payment Successful",
                    "message": "Thank you for your subscription! Updating status...",
                },
            )

        elif action == "cancel":
            logger.info(f"[{self.feature_id}] Payment cancelled deep link received.")
            await self.event_bus.publish(
                "system.notification",
                {
                    "type": "info",
                    "title": "Payment Cancelled",
                    "message": "The payment process was cancelled.",
                },
            )

        elif action == "billing_problem":
            logger.warning(f"[{self.feature_id}] Billing problem deep link received.")
            await self.event_bus.publish(
                "system.notification",
                {
                    "type": "error",
                    "title": "Payment Issue",
                    "message": "There was an issue with your payment. Please check your billing details.",
                },
            )

        elif "portal_return" in action:
            logger.info(f"[{self.feature_id}] Returned from Customer Portal.")
            await self.event_bus.publish("payment.sync_requested", {"reason": "portal_return"})

    async def _on_server_connected(self, payload: dict[str, Any]):
        """
        При подключении к серверу запрашиваем актуальный статус.
        """
        logger.info(f"[{self.feature_id}] Server connected. Requesting subscription status sync.")
        await self.event_bus.publish("payment.sync_requested", {"reason": "reconnect"})

    async def _on_hardware_id_received(self, payload: dict[str, Any]):
        """Получен Hardware ID"""
        # UUID is nested inside 'data' key in the event payload
        data = payload.get("data", {})
        uuid = data.get("uuid") if isinstance(data, dict) else payload.get("uuid")
        logger.info(
            f"[{self.feature_id}] _on_hardware_id_received: uuid={uuid[:8] if uuid else 'None'}..."
        )
        if uuid:
            self._hardware_id = uuid
            logger.info(f"[{self.feature_id}] Hardware ID SET: {uuid[:8]}...")
        else:
            logger.warning(
                f"[{self.feature_id}] Hardware ID NOT SET - uuid missing. payload keys: {list(payload.keys())}"
            )

    # --- Public API (for other client modules) ---

    async def _open_url_safely(self, url: str):
        """
        Safely opens a URL using system-native commands (non-blocking).
        """
        import sys

        logger.info(f"[{self.feature_id}] Opening URL safely: {url}")
        try:
            if sys.platform == "darwin":
                # Use asyncio to avoid blocking the event loop
                # 'open' command usually returns immediately, but best to be safe
                proc = await asyncio.create_subprocess_exec(
                    "open",
                    url,
                    stdout=asyncio.subprocess.DEVNULL,
                    stderr=asyncio.subprocess.DEVNULL,
                )
                rc = await proc.wait()
                if rc != 0:
                    logger.error(
                        f"[{self.feature_id}] 'open' command failed with code {rc} for {url}"
                    )
                else:
                    logger.info(f"[{self.feature_id}] 'open' command succeeded for {url}")
            else:
                import webbrowser

                # Run blocking webbrowser.open in executor
                loop = asyncio.get_running_loop()
                await loop.run_in_executor(None, lambda: webbrowser.open(url))
        except Exception as e:
            logger.error(f"[{self.feature_id}] Error opening URL safely: {e}")
            # Fallback (blocking, but should be rare)
            try:
                import webbrowser

                webbrowser.open(url)
            except Exception as we:
                logger.error(f"[{self.feature_id}] Fallback failed: {we}")

    async def open_buy_subscription(self, session_id: str | None = None):
        """
        Открыть страницу покупки подписки (Stripe Checkout).
        """
        try:
            now = time.time()
            if self._checkout_in_flight:
                logger.warning(
                    f"[{self.feature_id}] Checkout already in flight, skipping (session_id={session_id})"
                )
                return
            if (
                self._last_checkout_opened_at
                and (now - self._last_checkout_opened_at) < self._checkout_dedup_window_sec
            ):
                if session_id and self._last_checkout_session_id == session_id:
                    logger.warning(
                        f"[{self.feature_id}] Duplicate checkout suppressed (session_id={session_id})"
                    )
                    return
                if not session_id:
                    logger.warning(
                        f"[{self.feature_id}] Recent checkout exists, skipping (session_id=None)"
                    )
                    return
            self._checkout_in_flight = True

            # If hardware ID not ready, request and wait for it
            if not self._hardware_id:
                logger.info(f"[{self.feature_id}] Hardware ID not ready, requesting...")
                await self.event_bus.publish("hardware.id_request", {"wait_ready": True})

                # Wait up to 5 seconds for the ID to arrive (50 * 0.1s)
                for i in range(50):
                    await asyncio.sleep(0.1)
                    if self._hardware_id:
                        logger.info(
                            f"[{self.feature_id}] Hardware ID received after {i * 0.1:.1f}s"
                        )
                        break

                if not self._hardware_id:
                    logger.error(
                        f"[{self.feature_id}] Timeout: Hardware ID still not ready after 5s waiting"
                    )
                    # Try one last fetch request before giving up
                    await self.event_bus.publish("hardware.id_request", {"wait_ready": False})

                    await self.event_bus.publish(
                        "system.notification",
                        {
                            "type": "error",
                            "title": "Payment Error",
                            "message": "System not ready (ID missing). Please try again.",
                        },
                    )
                    return

            logger.info(f"[{self.feature_id}] Hardware ID ready: {self._hardware_id[:8]}...")

            # Определяем URL API
            from config.unified_config_loader import get_grpc_host

            host = get_grpc_host()
            logger.info(f"[{self.feature_id}] Resolved gRPC host: '{host}' (from unified_config)")
            api_url = f"http://{host}:8080/api/subscription/checkout"

            logger.info(f"[{self.feature_id}] Requesting checkout session from {api_url}")

            # Set explicit timeout for connection
            timeout = aiohttp.ClientTimeout(total=15)

            async with aiohttp.ClientSession(timeout=timeout) as session:
                async with session.post(api_url, json={"hardware_id": self._hardware_id}) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        # StripeService returns 'checkout_url'
                        checkout_url = data.get("checkout_url") or data.get("url")
                        if checkout_url:
                            await self._open_url_safely(checkout_url)
                            self._last_checkout_opened_at = time.time()
                            self._last_checkout_session_id = session_id
                            # Start polling for status update
                            self._ensure_polling()
                        else:
                            logger.error(f"[{self.feature_id}] No url in checkout response")
                            await self.event_bus.publish(
                                "system.notification",
                                {
                                    "type": "error",
                                    "title": "Payment Error",
                                    "message": "Invalid response from payment server. Please try again.",
                                },
                            )
                    else:
                        text = await resp.text()
                        logger.error(
                            f"[{self.feature_id}] Failed to get checkout URL: {resp.status} {text}"
                        )
                        await self.event_bus.publish(
                            "system.notification",
                            {
                                "type": "error",
                                "title": "Connection Error",
                                "message": "Failed to connect to payment service.",
                            },
                        )

        except asyncio.TimeoutError:
            logger.error(f"[{self.feature_id}] Timeout connecting to payment service")
            await self.event_bus.publish(
                "system.notification",
                {
                    "type": "error",
                    "title": "Connection Timeout",
                    "message": "Server is taking too long to respond. Please check your internet connection.",
                },
            )
        except Exception as e:
            logger.error(f"[{self.feature_id}] Error opening checkout: {e}")
            await self.event_bus.publish(
                "system.notification",
                {"type": "error", "title": "Error", "message": f"Failed to open checkout: {e}"},
            )
        finally:
            self._checkout_in_flight = False

    async def open_manage_subscription(self):
        """
        Открыть портал управления подпиской.
        1. Запрашиваем URL у сервера.
        2. Открываем в браузере.
        """
        try:
            if not self._hardware_id:
                logger.warning(f"[{self.feature_id}] Hardware ID not ready, cannot open portal")
                # Запрашиваем ID и пробуем снова через паузу? Нет, просто уведомляем
                await self.event_bus.publish(
                    "system.notification",
                    {
                        "type": "error",
                        "title": "Payment Error",
                        "message": "System not ready (ID missing). Please try again in 5 seconds.",
                    },
                )
                # Trigger refresh
                await self.event_bus.publish("hardware.id_request", {"wait_ready": False})
                return

            # Определяем URL API
            from config.unified_config_loader import get_grpc_host

            host = get_grpc_host()
            # Предполагаем порт 8080 по умолчанию
            api_url = f"http://{host}:8080/api/subscription/portal"

            logger.info(
                f"[{self.feature_id}] Requesting portal session from {api_url} for {self._hardware_id}"
            )

            # Set explicit timeout for connection
            timeout = aiohttp.ClientTimeout(total=15)

            async with aiohttp.ClientSession(timeout=timeout) as session:
                async with session.post(api_url, json={"hardware_id": self._hardware_id}) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        portal_url = data.get("portal_url")
                        if portal_url:
                            await self._open_url_safely(portal_url)
                        else:
                            logger.error(f"[{self.feature_id}] No portal_url in response")
                            await self.event_bus.publish(
                                "system.notification",
                                {
                                    "type": "error",
                                    "title": "Payment Error",
                                    "message": "Invalid response from payment server. Please try again.",
                                },
                            )
                    elif resp.status == 404:
                        logger.warning(
                            f"[{self.feature_id}] No subscription found. Redirecting to buy flow."
                        )
                        await self.event_bus.publish(
                            "system.notification",
                            {
                                "type": "info",
                                "title": "No Subscription Found",
                                "message": "Redirecting to subscription plan selection...",
                            },
                        )
                        # Fallback to buy flow
                        await self.open_buy_subscription(session_id=None)
                    else:
                        text = await resp.text()
                        logger.error(
                            f"[{self.feature_id}] Failed to get portal URL: {resp.status} {text}"
                        )
                        await self.event_bus.publish(
                            "system.notification",
                            {
                                "type": "error",
                                "title": "Connection Error",
                                "message": "Failed to connect to subscription service.",
                            },
                        )

        except asyncio.TimeoutError:
            logger.error(f"[{self.feature_id}] Timeout connecting to portal service")
            await self.event_bus.publish(
                "system.notification",
                {
                    "type": "error",
                    "title": "Connection Timeout",
                    "message": "Server is taking too long to respond. Please check your internet connection.",
                },
            )
        except Exception as e:
            logger.error(f"[{self.feature_id}] Error opening portal: {e}")
            await self.event_bus.publish(
                "system.notification",
                {"type": "error", "title": "Error", "message": f"Failed to open portal: {e}"},
            )

    async def start_polling_status(self):
        """
        Start polling server for subscription status update.
        Runs every 5 seconds for 5 minutes (60 attempts).
        """
        logger.info(f"[{self.feature_id}] Starting subscription status polling...")

        from config.unified_config_loader import get_grpc_host

        host = get_grpc_host()
        api_url = f"http://{host}:8080/api/subscription/status"

        attempts = 60  # 5 minutes

        try:
            for i in range(attempts):
                try:
                    if not self._hardware_id:
                        break

                    async with aiohttp.ClientSession() as session:
                        async with session.get(
                            api_url, params={"hardware_id": self._hardware_id}
                        ) as resp:
                            if resp.status == 200:
                                data = await resp.json()
                                status = data.get("status")

                                # If status is paid, update UI and stop polling
                                if (
                                    status in ["paid", "paid_trial", "grandfathered"]
                                    and self._subscription_status.get("status") != status
                                ):
                                    logger.info(
                                        f"[{self.feature_id}] Polling success! Status is now {status}"
                                    )

                                    # Broadcast update
                                    await self.event_bus.publish(
                                        "subscription.status_updated", data
                                    )
                                    return
                            else:
                                logger.warning(
                                    f"[{self.feature_id}] Status poll failed: {resp.status}"
                                )

                except Exception as e:
                    logger.error(f"[{self.feature_id}] Polling error: {e}")

                await asyncio.sleep(5)

            logger.info(f"[{self.feature_id}] Polling stopped after timeout")
        finally:
            self._poll_task = None

    def _ensure_polling(self) -> None:
        """Start polling once, avoid duplicate poll loops."""
        if self._poll_task and not self._poll_task.done():
            logger.debug(f"[{self.feature_id}] Polling already in progress, skipping.")
            return
        self._poll_task = asyncio.create_task(self.start_polling_status())

    async def _announce_payment_success(self):
        """
        Announce successful payment via SERVER TTS.
        """
        try:
            message = "Payment successful! Your subscription is now active. You have unlimited access. Thank you for your support!"
            logger.info(f"[{self.feature_id}] 🔊 Announcing payment success via SERVER TTS")

            # Publish event for gRPC integration to handle via Server TTS
            await self.event_bus.publish(
                "grpc.tts_request",
                {
                    "text": message,
                    "session_id": f"payment_success_{int(time.time())}",
                    "source": "payment_integration",
                },
            )

        except Exception as e:
            logger.error(f"[{self.feature_id}] TTS announcement error: {e}")

    def get_local_status(self) -> dict[str, Any]:
        """
        Получить ТЕКУЩИЙ известный статус (из кэша).
        НЕ делает запрос к серверу.
        """
        return self._subscription_status
