"""
InterruptManagementIntegration - Интеграция InterruptCoordinator с EventBus
Тонкая обертка для интеграции InterruptCoordinator в общую архитектуру
"""

import asyncio
from dataclasses import dataclass
import logging
import time
from typing import Any

from integration.core import selectors
from integration.core.error_handler import ErrorHandler

# Пути уже добавлены в main.py - не дублируем
from integration.core.event_bus import EventBus, EventPriority
from integration.core.state_manager import ApplicationStateManager

# Import AppMode with fallback mechanism (same as state_manager.py and selectors.py)
try:
    # Preferred: top-level import (packaged or PYTHONPATH includes modules)
    from mode_management import AppMode  # type: ignore[reportMissingImports]
except Exception:
    # Fallback: explicit modules path if repository layout is used
    from modules.mode_management import AppMode  # type: ignore[reportMissingImports]

# Импорты модуля InterruptManagement
from modules.interrupt_management.core.interrupt_coordinator import (
    InterruptCoordinator,
    InterruptDependencies,
)
from modules.interrupt_management.core.types import (
    InterruptConfig,
    InterruptEvent,
    InterruptPriority,
    InterruptStatus,
    InterruptType,
)

logger = logging.getLogger(__name__)

@dataclass
class InterruptManagementIntegrationConfig:
    """Конфигурация InterruptManagementIntegration"""
    max_concurrent_interrupts: int = 5
    interrupt_timeout: float = 10.0
    retry_attempts: int = 3
    retry_delay: float = 1.0
    enable_speech_interrupts: bool = True
    enable_recording_interrupts: bool = True
    enable_session_interrupts: bool = True
    enable_full_reset: bool = True

class InterruptManagementIntegration:
    """Интеграция InterruptCoordinator с EventBus и ApplicationStateManager"""
    
    def __init__(
        self,
        event_bus: EventBus,
        state_manager: ApplicationStateManager,
        error_handler: ErrorHandler,
        config: InterruptManagementIntegrationConfig | None = None,
    ):
        self.event_bus = event_bus
        self.state_manager = state_manager
        self.error_handler = error_handler
        self.config = config or InterruptManagementIntegrationConfig()
        
        # InterruptCoordinator экземпляр
        self._coordinator: InterruptCoordinator | None = None
        self._initialized = False
        self._running = False
        self._interrupt_dedup_window_sec: float = 0.5
        self._last_interrupt_publish_ts: dict[tuple[str, str], float] = {}
        self._interrupt_event_ttl_sec: float = 5.0
        self._seen_interrupt_events: dict[str, float] = {}
        
        logger.info("InterruptManagementIntegration created")
    
    async def initialize(self) -> bool:
        """Инициализация InterruptManagementIntegration"""
        try:
            logger.info("Initializing InterruptManagementIntegration...")
            
            # Создаем конфигурацию InterruptCoordinator
            interrupt_config = InterruptConfig(
                max_concurrent_interrupts=self.config.max_concurrent_interrupts,
                interrupt_timeout=self.config.interrupt_timeout,
                retry_attempts=self.config.retry_attempts,
                retry_delay=self.config.retry_delay
            )
            
            # Создаем InterruptCoordinator
            self._coordinator = InterruptCoordinator(interrupt_config)
            
            # Настраиваем зависимости
            dependencies = InterruptDependencies(
                state_manager=self.state_manager
            )
            self._coordinator.initialize(dependencies)
            
            # Настраиваем обработчики прерываний
            self._setup_interrupt_handlers()
            
            # Подписываемся на события приложения
            await self.event_bus.subscribe("app.startup", self._on_app_startup, EventPriority.MEDIUM)
            await self.event_bus.subscribe("app.shutdown", self._on_app_shutdown, EventPriority.HIGH)
            await self.event_bus.subscribe("app.state_changed", self._on_app_state_changed, EventPriority.HIGH)
            
            # Подписываемся на события прерываний
            await self.event_bus.subscribe("interrupt.request", self._on_interrupt_request, EventPriority.HIGH)
            await self.event_bus.subscribe("interrupt.cancel", self._on_interrupt_cancel, EventPriority.HIGH)
            
            self._initialized = True
            logger.info("InterruptManagementIntegration initialized successfully")
            return True
            
        except Exception as e:
            if hasattr(self.error_handler, 'handle_error'):
                await self.error_handler.handle_error(
                    severity="error",
                    category="interrupt",
                    message=f"Ошибка инициализации InterruptManagementIntegration: {e}",
                    context={"where": "interrupt.initialize"}
                )
            else:
                logger.error(f"Error in InterruptManagementIntegration.initialize: {e}")
            logger.error(f"Failed to initialize InterruptManagementIntegration: {e}")
            return False
    
    async def start(self) -> bool:
        """Запуск InterruptManagementIntegration"""
        if not self._initialized or not self._coordinator:
            logger.error("InterruptManagementIntegration not initialized")
            return False
        
        if self._running:
            logger.warning("InterruptManagementIntegration already running")
            return True
        
        try:
            logger.info("Starting InterruptManagementIntegration...")
            
            # InterruptCoordinator не требует запуска, только инициализации
            self._running = True
            logger.info("InterruptManagementIntegration started successfully")
            return True
            
        except Exception as e:
            if hasattr(self.error_handler, 'handle_error'):
                await self.error_handler.handle_error(
                    severity="error",
                    category="interrupt",
                    message=f"Ошибка запуска InterruptManagementIntegration: {e}",
                    context={"where": "interrupt.start"}
                )
            else:
                logger.error(f"Error in InterruptManagementIntegration.start: {e}")
            logger.error(f"Failed to start InterruptManagementIntegration: {e}")
            return False
    
    async def stop(self) -> bool:
        """Остановка InterruptManagementIntegration"""
        if not self._coordinator:
            return True
        
        if not self._running:
            return True
        
        try:
            logger.info("Stopping InterruptManagementIntegration...")
            
            # Отменяем все активные прерывания
            await self._cancel_all_interrupts()
            
            self._running = False
            logger.info("InterruptManagementIntegration stopped")
            return True
            
        except Exception as e:
            if hasattr(self.error_handler, 'handle_error'):
                await self.error_handler.handle_error(
                    severity="error",
                    category="interrupt",
                    message=f"Ошибка остановки InterruptManagementIntegration: {e}",
                    context={"where": "interrupt.stop"}
                )
            else:
                logger.error(f"Error in InterruptManagementIntegration.stop: {e}")
            logger.error(f"Failed to stop InterruptManagementIntegration: {e}")
            return False
    
    def _setup_interrupt_handlers(self):
        """Настройка обработчиков прерываний"""
        if self._coordinator is None:
            logger.warning("InterruptCoordinator not initialized, cannot setup handlers")
            return
        
        try:
            # Регистрируем обработчики для каждого типа прерывания
            if self.config.enable_speech_interrupts:
                self._coordinator.register_handler(
                    InterruptType.SPEECH_STOP, 
                    self._handle_speech_stop
                )
                self._coordinator.register_handler(
                    InterruptType.SPEECH_PAUSE, 
                    self._handle_speech_pause
                )
            
            if self.config.enable_recording_interrupts:
                self._coordinator.register_handler(
                    InterruptType.RECORDING_STOP, 
                    self._handle_recording_stop
                )
            
            if self.config.enable_session_interrupts:
                self._coordinator.register_handler(
                    InterruptType.SESSION_CLEAR, 
                    self._handle_session_clear
                )
            
            if self.config.enable_full_reset:
                self._coordinator.register_handler(
                    InterruptType.FULL_RESET, 
                    self._handle_full_reset
                )
            
            logger.info("Interrupt handlers registered successfully")
            
        except Exception as e:
            logger.error(f"Error setting up interrupt handlers: {e}")
            raise
    
    async def _on_app_startup(self, event):
        """Обработка события запуска приложения"""
        try:
            logger.info("App startup - initializing interrupt management")
            
            if self._coordinator:
                # Публикуем снапшот состояния прерываний
                await self.event_bus.publish("interrupt.status_snapshot", {
                    "active_interrupts": len(self._coordinator.active_interrupts),
                    "total_interrupts": len(self._coordinator.interrupt_history),
                    "is_running": self._running
                })
            
        except Exception as e:
            if hasattr(self.error_handler, 'handle_error'):
                await self.error_handler.handle_error(
                    severity="warning",
                    category="interrupt",
                    message=f"Ошибка обработки app startup: {e}",
                    context={"where": "interrupt.app_startup"}
                )
            else:
                logger.error(f"Error in InterruptManagementIntegration.app_startup: {e}")
    
    async def _on_app_shutdown(self, event):
        """Обработка события остановки приложения"""
        try:
            logger.info("App shutdown - stopping interrupt management")
            await self.stop()
        except Exception as e:
            if hasattr(self.error_handler, 'handle_error'):
                await self.error_handler.handle_error(
                    severity="warning",
                    category="interrupt",
                    message=f"Ошибка обработки app shutdown: {e}",
                    context={"where": "interrupt.app_shutdown"}
                )
            else:
                logger.error(f"Error in InterruptManagementIntegration.app_shutdown: {e}")
    
    async def _on_app_state_changed(self, event):
        """Обработка изменения режима приложения"""
        try:
            data = event.get("data", {}) if isinstance(event, dict) else {}
            old_mode = data.get("old_mode")
            new_mode = data.get("new_mode")
            
            if old_mode and new_mode:
                await self._handle_mode_change(old_mode, new_mode)
            
        except Exception as e:
            if hasattr(self.error_handler, 'handle_error'):
                await self.error_handler.handle_error(
                    severity="warning",
                    category="interrupt",
                    message=f"Ошибка обработки смены режима: {e}",
                    context={"where": "interrupt.state_changed"}
                )
            else:
                logger.error(f"Error in InterruptManagementIntegration.state_changed: {e}")
    
    async def _handle_mode_change(self, old_mode: AppMode, new_mode: AppMode):
        """Обработка смены режима приложения"""
        try:
            logger.info(f"Interrupt mode change: {old_mode} -> {new_mode}")
            
            # Если переходим в SLEEPING, отменяем все активные прерывания
            if new_mode == AppMode.SLEEPING:
                await self._cancel_all_interrupts()
            
        except Exception as e:
            if hasattr(self.error_handler, 'handle_error'):
                await self.error_handler.handle_error(
                    severity="warning",
                    category="interrupt",
                    message=f"Ошибка обработки смены режима: {e}",
                    context={"where": "interrupt.mode_change"}
                )
            else:
                logger.error(f"Error in InterruptManagementIntegration.mode_change: {e}")
    
    async def _on_interrupt_request(self, event):
        """Обработка запроса на прерывание"""
        try:
            # Contract: payload interrupt.request хранится только в event.data.
            data = event.get("data", {}) if isinstance(event, dict) else {}
            interrupt_type = data.get("type")
            session_id = data.get("session_id")
            priority = data.get("priority", InterruptPriority.NORMAL)
            source = data.get("source", "unknown")
            press_id = data.get("press_id")
            event_id = data.get("event_id")
            
            # REQ-004: use selector to get session_id as fallback
            if session_id is None:
                session_id = selectors.get_current_session_id(self.state_manager)
            
            logger.debug(
                "🛑 InterruptManager: interrupt.request - type=%s, data.session_id=%s, final.session_id=%s",
                interrupt_type,
                data.get("session_id"),
                session_id,
            )
            
            if not interrupt_type:
                logger.warning("Interrupt request without type, event=%s", event)
                return

            now = time.monotonic()

            # Contract guard: strict idempotency by event_id.
            if isinstance(event_id, str) and event_id:
                expired_ids = [
                    key
                    for key, ts in self._seen_interrupt_events.items()
                    if (now - ts) > self._interrupt_event_ttl_sec
                ]
                for key in expired_ids:
                    self._seen_interrupt_events.pop(key, None)
                if event_id in self._seen_interrupt_events:
                    logger.debug(
                        "🛑 InterruptManager: dedup by event_id (event_id=%s, session_id=%s)",
                        event_id,
                        session_id,
                    )
                    return
                self._seen_interrupt_events[event_id] = now
            
            # КРИТИЧНО: Централизованная остановка речи для type == "speech_stop"
            if interrupt_type == "speech_stop":
                sid_key = str(session_id) if session_id is not None else "__none__"
                pid_key = str(press_id) if press_id is not None else "__no_press__"
                dedup_key = (interrupt_type, f"{sid_key}:{pid_key}")
                last_ts = self._last_interrupt_publish_ts.get(dedup_key, 0.0)
                if (now - last_ts) < self._interrupt_dedup_window_sec:
                    logger.debug(
                        "🛑 InterruptManager: speech_stop dedup (session_id=%s, press_id=%s, dt=%.3fs)",
                        session_id,
                        press_id,
                        now - last_ts,
                    )
                    return
                else:
                    self._last_interrupt_publish_ts[dedup_key] = now
                    logger.info(f"🛑 InterruptManager: останавливаем речь (session_id={session_id})")
                    # Enforce session-scoped cancel contract.
                    if session_id is None:
                        logger.warning("🛑 InterruptManager: grpc.request_cancel skipped (missing session_id)")
                        return
                    await self.event_bus.publish("grpc.request_cancel", {
                        "session_id": session_id,
                        "press_id": press_id,
                        "event_id": event_id,
                        "source": source,
                        "reason": str(data.get("reason") or "user_interrupt"),
                        "initiator": "keyboard" if str(source).startswith("keyboard.") else "system",
                    })
                    logger.info(
                        "🛑 InterruptManager: grpc.request_cancel опубликован (session_id=%s)",
                        session_id,
                    )
            
            # Создаем событие прерывания
            interrupt_event = InterruptEvent(
                type=InterruptType(interrupt_type),
                priority=InterruptPriority(priority) if isinstance(priority, str) else priority,
                source=source,
                timestamp=asyncio.get_event_loop().time(),
                data=data
            )
            
            # Отправляем на обработку
            if self._coordinator is None:
                logger.error("InterruptCoordinator not initialized, cannot trigger interrupt")
                return
            await self._coordinator.trigger_interrupt(interrupt_event)
            
        except Exception as e:
            if hasattr(self.error_handler, 'handle_error'):
                await self.error_handler.handle_error(
                    severity="warning",
                    category="interrupt",
                    message=f"Ошибка обработки запроса прерывания: {e}",
                    context={"where": "interrupt.request"}
                )
            else:
                logger.error(f"Error in InterruptManagementIntegration.interrupt_request: {e}")
    
    async def _on_interrupt_cancel(self, event):
        """Обработка отмены прерывания"""
        try:
            interrupt_id = event.get("interrupt_id")
            if interrupt_id and self._coordinator:
                # Отменяем конкретное прерывание через _cancel_all_interrupts (метод cancel_interrupt не существует)
                await self._cancel_all_interrupts()
            else:
                # Отменяем все прерывания
                await self._cancel_all_interrupts()
            
        except Exception as e:
            if hasattr(self.error_handler, 'handle_error'):
                await self.error_handler.handle_error(
                    severity="warning",
                    category="interrupt",
                    message=f"Ошибка отмены прерывания: {e}",
                    context={"where": "interrupt.cancel"}
                )
            else:
                logger.error(f"Error in InterruptManagementIntegration.interrupt_cancel: {e}")
    
    async def _handle_speech_stop(self, interrupt_event: InterruptEvent):
        """Обработка остановки речи"""
        try:
            logger.info("Handling speech stop interrupt")
            payload = interrupt_event.data if isinstance(interrupt_event.data, dict) else {}
            session_id = payload.get("session_id")

            # Переводим в режим SLEEPING централизованно
            if self.event_bus:
                try:
                    await self.event_bus.publish("mode.request", {
                        "target": AppMode.SLEEPING,
                        "source": "interrupt_management",
                        "session_id": session_id,
                    })
                except Exception as e:
                    logger.error(f"Error publishing mode.request SLEEPING: {e}")
            
            interrupt_event.status = InterruptStatus.COMPLETED
            interrupt_event.result = "Speech stopped successfully"
            return True  # ✅ Возвращаем True при успехе
            
        except Exception as e:
            logger.error(f"Error handling speech stop: {e}")
            interrupt_event.status = InterruptStatus.FAILED
            interrupt_event.error = str(e)
            return False  # ✅ Возвращаем False при ошибке
    
    async def _handle_speech_pause(self, interrupt_event: InterruptEvent):
        """Обработка паузы речи"""
        try:
            logger.info("Handling speech pause interrupt")
            
            # Публикуем событие паузы речи
            if self.event_bus:
                await self.event_bus.publish("speech.pause_requested", {
                    "interrupt_id": id(interrupt_event),
                    "source": interrupt_event.source,
                    "timestamp": interrupt_event.timestamp
                })
            
            interrupt_event.status = InterruptStatus.COMPLETED
            interrupt_event.result = "Speech paused successfully"
            return True  # ✅ Возвращаем True при успехе
            
        except Exception as e:
            logger.error(f"Error handling speech pause: {e}")
            interrupt_event.status = InterruptStatus.FAILED
            interrupt_event.error = str(e)
            return False  # ✅ Возвращаем False при ошибке
    
    async def _handle_recording_stop(self, interrupt_event: InterruptEvent):
        """Обработка остановки записи"""
        try:
            logger.info("Handling recording stop interrupt")
            data = interrupt_event.data or {}
            session_id = data.get("session_id")

            # Переводим в режим PROCESSING централизованно
            if self.event_bus:
                try:
                    await self.event_bus.publish("mode.request", {
                        "target": AppMode.PROCESSING,
                        "source": "interrupt_management",
                        "session_id": session_id,
                    })
                except Exception as e:
                    logger.error(f"Error publishing mode.request PROCESSING: {e}")
            
            interrupt_event.status = InterruptStatus.COMPLETED
            interrupt_event.result = "Recording stopped successfully"
            return True  # ✅ Возвращаем True при успехе
            
        except Exception as e:
            logger.error(f"Error handling recording stop: {e}")
            interrupt_event.status = InterruptStatus.FAILED
            interrupt_event.error = str(e)
            return False  # ✅ Возвращаем False при ошибке
    
    async def _handle_session_clear(self, interrupt_event: InterruptEvent):
        """Обработка очистки сессии"""
        try:
            logger.info("Handling session clear interrupt")

            # Переводим в режим SLEEPING централизованно
            if self.event_bus:
                try:
                    await self.event_bus.publish("mode.request", {
                        "target": AppMode.SLEEPING,
                        "source": "interrupt_management"
                    })
                except Exception as e:
                    logger.error(f"Error publishing mode.request SLEEPING: {e}")
            
            interrupt_event.status = InterruptStatus.COMPLETED
            interrupt_event.result = "Session cleared successfully"
            return True  # ✅ Возвращаем True при успехе
            
        except Exception as e:
            logger.error(f"Error handling session clear: {e}")
            interrupt_event.status = InterruptStatus.FAILED
            interrupt_event.error = str(e)
            return False  # ✅ Возвращаем False при ошибке
    
    async def _handle_full_reset(self, interrupt_event: InterruptEvent):
        """Обработка полного сброса"""
        try:
            logger.info("Handling full reset interrupt")
            
            # Публикуем событие полного сброса
            if self.event_bus:
                await self.event_bus.publish("system.reset_requested", {
                    "interrupt_id": id(interrupt_event),
                    "source": interrupt_event.source,
                    "timestamp": interrupt_event.timestamp
                })
            
            # Отменяем все активные прерывания
            await self._cancel_all_interrupts()
            
            # Переводим в режим SLEEPING централизованно
            if self.event_bus:
                try:
                    await self.event_bus.publish("mode.request", {
                        "target": AppMode.SLEEPING,
                        "source": "interrupt_management"
                    })
                except Exception as e:
                    logger.error(f"Error publishing mode.request SLEEPING: {e}")
            
            interrupt_event.status = InterruptStatus.COMPLETED
            interrupt_event.result = "Full reset completed successfully"
            
        except Exception as e:
            logger.error(f"Error handling full reset: {e}")
            interrupt_event.status = InterruptStatus.FAILED
            interrupt_event.error = str(e)
    
    async def _cancel_all_interrupts(self):
        """Отмена всех активных прерываний"""
        try:
            if self._coordinator:
                cancelled = await self._coordinator.cancel_all_interrupts()
                if cancelled > 0:
                    logger.info("All active interrupts cancelled")
        except Exception as e:
            logger.error(f"Error cancelling all interrupts: {e}")
    
    def get_status(self) -> dict[str, Any]:
        """Получить статус InterruptManagementIntegration"""
        coordinator = self._coordinator
        if coordinator is None:
            return {
                "initialized": self._initialized,
                "running": self._running,
                "interrupts": {"status": "unknown"}
            }
        
        return {
            "initialized": self._initialized,
            "running": self._running,
            "interrupts": {
                "active_count": len(coordinator.active_interrupts) if hasattr(coordinator, 'active_interrupts') else 0,
                "total_count": len(coordinator.interrupt_history) if hasattr(coordinator, 'interrupt_history') else 0,
                "is_running": coordinator.is_running if hasattr(coordinator, 'is_running') else False  # type: ignore[attr-defined]
            }
        }
    
    async def request_interrupt(self, interrupt_type: InterruptType, priority: InterruptPriority = InterruptPriority.NORMAL, source: str = "integration", data: dict[str, Any] | None = None) -> bool:
        """Запросить прерывание"""
        if not self._coordinator:
            return False
        
        try:
            interrupt_event = InterruptEvent(
                type=interrupt_type,
                priority=priority,
                source=source,
                timestamp=asyncio.get_event_loop().time(),
                data=data or {}
            )
            
            return await self._coordinator.trigger_interrupt(interrupt_event)
        except Exception as e:
            logger.error(f"Error requesting interrupt {interrupt_type}: {e}")
            return False
