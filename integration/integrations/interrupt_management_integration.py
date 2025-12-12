"""
InterruptManagementIntegration - Интеграция InterruptCoordinator с EventBus
Тонкая обертка для интеграции InterruptCoordinator в общую архитектуру
"""

import asyncio
import logging
from dataclasses import dataclass
from typing import Optional, Dict, Any

# Пути уже добавлены в main.py - не дублируем

from integration.core.event_bus import EventBus, EventPriority
from integration.core.state_manager import ApplicationStateManager, AppMode
from integration.core.error_handler import ErrorHandler

# Импорты модуля InterruptManagement
from modules.interrupt_management.core.interrupt_coordinator import InterruptCoordinator, InterruptDependencies
from modules.interrupt_management.core.types import (
    InterruptType, InterruptPriority, InterruptStatus, InterruptEvent, InterruptConfig
)
from modules.interrupt_management.config.interrupt_config import InterruptModuleConfig

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
        config: Optional[InterruptManagementIntegrationConfig] = None,
    ):
        self.event_bus = event_bus
        self.state_manager = state_manager
        self.error_handler = error_handler
        self.config = config or InterruptManagementIntegrationConfig()
        
        # InterruptCoordinator экземпляр
        self._coordinator: Optional[InterruptCoordinator] = None
        self._initialized = False
        self._running = False
        
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
            old_mode = event.get("old_mode")
            new_mode = event.get("new_mode")
            
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
            # ✅ КРИТИЧНО: EventBus создает событие со структурой {"type": "interrupt.request", "data": {...}}
            # Поэтому type, source, reason и другие поля находятся в data, а не в корне события
            data = event.get("data", {})
            if not data and isinstance(event, dict):
                # Если data пустой, возможно данные в корне события (для обратной совместимости)
                data = {k: v for k, v in event.items() if k not in ("type", "timestamp")}
            
            # ✅ FIX: Получаем type из data, а не из корня события
            interrupt_type = data.get("type")
            priority = data.get("priority", InterruptPriority.NORMAL)
            source = data.get("source", "unknown")
            reason = data.get("reason", "")
            
            # ✅ FIX: Если type не указан, определяем по reason или source
            if not interrupt_type:
                # ✅ КРИТИЧНО: Проверяем режим приложения для определения типа прерывания
                # Если режим PROCESSING, вероятно активно воспроизведение - используем SPEECH_STOP
                current_mode = None
                if self.state_manager:
                    try:
                        current_mode = self.state_manager.get_current_mode()
                    except Exception:
                        pass
                
                # Определяем тип прерывания по reason, source или режиму
                if "recording" in reason.lower() or "recording" in source.lower():
                    interrupt_type = InterruptType.RECORDING_STOP
                elif "speech" in reason.lower() or "playback" in source.lower():
                    interrupt_type = InterruptType.SPEECH_STOP
                elif current_mode == AppMode.PROCESSING:
                    # ✅ КРИТИЧНО: В режиме PROCESSING обычно активно воспроизведение - прерываем речь
                    interrupt_type = InterruptType.SPEECH_STOP
                    logger.debug(f"🔍 InterruptManagement: режим PROCESSING, используем SPEECH_STOP для прерывания воспроизведения")
                elif reason == "user_interrupt" or source == "keyboard":
                    interrupt_type = InterruptType.SESSION_CLEAR  # Очистка сессии при прерывании пользователем
                else:
                    # По умолчанию - очистка сессии
                    interrupt_type = InterruptType.SESSION_CLEAR
                    logger.debug(f"⚠️ Interrupt type не указан, используем SESSION_CLEAR по умолчанию (reason={reason}, source={source}, mode={current_mode})")
            
            # ✅ FIX: Проверяем что interrupt_type валидный
            if isinstance(interrupt_type, str):
                try:
                    interrupt_type = InterruptType(interrupt_type)
                except ValueError:
                    logger.warning(f"⚠️ Неизвестный тип прерывания: {interrupt_type}, используем SESSION_CLEAR")
                    interrupt_type = InterruptType.SESSION_CLEAR
            
            # Создаем событие прерывания
            interrupt_event = InterruptEvent(
                type=interrupt_type,
                priority=InterruptPriority(priority) if isinstance(priority, str) else priority,
                source=source,
                timestamp=asyncio.get_event_loop().time(),
                data={**data, "reason": reason, "session_id": data.get("session_id")}  # ✅ FIX: Добавляем reason и session_id в data
            )
            
            # Отправляем на обработку
            await self._coordinator.trigger_interrupt(interrupt_event)
            
        except Exception as e:
            if hasattr(self.error_handler, 'handle_error'):
                await self.error_handler.handle_error(
                    severity="warning",
                    category="interrupt",
                    message=f"Ошибка обработки запроса прерывания: {e}",
                    context={"where": "interrupt.request", "event": event}
                )
            else:
                logger.error(f"Error in InterruptManagementIntegration.interrupt_request: {e}", exc_info=True)
    
    async def _on_interrupt_cancel(self, event):
        """Обработка отмены прерывания"""
        try:
            interrupt_id = event.get("interrupt_id")
            if interrupt_id and self._coordinator and hasattr(self._coordinator, 'cancel_interrupt'):
                await self._coordinator.cancel_interrupt(interrupt_id)
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
            
            # ✅ КРИТИЧНО: Получаем session_id из state_manager для остановки воспроизведения
            current_session_id = None
            if self.state_manager:
                try:
                    current_session_id = self.state_manager.get_current_session_id()
                except Exception as e:
                    logger.debug(f"Could not get session_id from state_manager: {e}")
            
            # ✅ КРИТИЧНО: Публикуем playback.cancelled для остановки воспроизведения
            # SpeechPlaybackIntegration подписан на playback.cancelled и остановит воспроизведение
            if self.event_bus:
                await self.event_bus.publish("playback.cancelled", {
                    "session_id": current_session_id,
                    "source": interrupt_event.source or "interrupt_management",
                    "reason": interrupt_event.data.get("reason", "user_interrupt"),
                    "interrupt_id": id(interrupt_event),
                    "timestamp": interrupt_event.timestamp
                })
                logger.info(f"🛑 InterruptManagement: playback.cancelled опубликовано для остановки воспроизведения (session_id={current_session_id})")
            
            # Публикуем событие остановки речи (для обратной совместимости)
            if self.event_bus:
                await self.event_bus.publish("speech.stop_requested", {
                    "interrupt_id": id(interrupt_event),
                    "source": interrupt_event.source,
                    "timestamp": interrupt_event.timestamp
                })
            
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
            interrupt_event.result = "Speech stopped successfully"
            return True  # ✅ КРИТИЧНО: Возвращаем True для успешного выполнения
            
        except Exception as e:
            logger.error(f"Error handling speech stop: {e}")
            interrupt_event.status = InterruptStatus.FAILED
            interrupt_event.error = str(e)
            return False  # ✅ КРИТИЧНО: Возвращаем False при ошибке
    
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
            return True  # ✅ КРИТИЧНО: Возвращаем True для успешного выполнения
            
        except Exception as e:
            logger.error(f"Error handling speech pause: {e}")
            interrupt_event.status = InterruptStatus.FAILED
            interrupt_event.error = str(e)
            return False  # ✅ КРИТИЧНО: Возвращаем False при ошибке
    
    async def _handle_recording_stop(self, interrupt_event: InterruptEvent):
        """Обработка остановки записи"""
        try:
            logger.info("Handling recording stop interrupt")
            
            # Публикуем событие остановки записи
            if self.event_bus:
                await self.event_bus.publish("recording.stop_requested", {
                    "interrupt_id": id(interrupt_event),
                    "source": interrupt_event.source,
                    "timestamp": interrupt_event.timestamp
                })
            
            # Переводим в режим PROCESSING централизованно
            if self.event_bus:
                try:
                    await self.event_bus.publish("mode.request", {
                        "target": AppMode.PROCESSING,
                        "source": "interrupt_management"
                    })
                except Exception as e:
                    logger.error(f"Error publishing mode.request PROCESSING: {e}")
            
            interrupt_event.status = InterruptStatus.COMPLETED
            interrupt_event.result = "Recording stopped successfully"
            return True  # ✅ КРИТИЧНО: Возвращаем True для успешного выполнения
            
        except Exception as e:
            logger.error(f"Error handling recording stop: {e}")
            interrupt_event.status = InterruptStatus.FAILED
            interrupt_event.error = str(e)
            return False  # ✅ КРИТИЧНО: Возвращаем False при ошибке
    
    async def _handle_session_clear(self, interrupt_event: InterruptEvent):
        """Обработка очистки сессии"""
        try:
            logger.info("Handling session clear interrupt")
            
            # Публикуем событие очистки сессии
            if self.event_bus:
                await self.event_bus.publish("session.clear_requested", {
                    "interrupt_id": id(interrupt_event),
                    "source": interrupt_event.source,
                    "timestamp": interrupt_event.timestamp
                })
            
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
            return True  # ✅ КРИТИЧНО: Возвращаем True для успешного выполнения
            
        except Exception as e:
            logger.error(f"Error handling session clear: {e}")
            interrupt_event.status = InterruptStatus.FAILED
            interrupt_event.error = str(e)
            return False  # ✅ КРИТИЧНО: Возвращаем False при ошибке
    
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
            return True  # ✅ КРИТИЧНО: Возвращаем True для успешного выполнения
            
        except Exception as e:
            logger.error(f"Error handling full reset: {e}")
            interrupt_event.status = InterruptStatus.FAILED
            interrupt_event.error = str(e)
            return False  # ✅ КРИТИЧНО: Возвращаем False при ошибке
    
    async def _cancel_all_interrupts(self):
        """Отмена всех активных прерываний"""
        try:
            if self._coordinator and hasattr(self._coordinator, 'cancel_all_interrupts'):
                await self._coordinator.cancel_all_interrupts()
                logger.info("All active interrupts cancelled")
            elif self._coordinator and hasattr(self._coordinator, 'active_interrupts'):
                # Отменяем все активные прерывания вручную
                for interrupt in self._coordinator.active_interrupts:
                    interrupt.status = InterruptStatus.CANCELLED
                self._coordinator.active_interrupts.clear()
                logger.info("All active interrupts cancelled manually")
        except Exception as e:
            logger.error(f"Error cancelling all interrupts: {e}")
    
    def get_status(self) -> Dict[str, Any]:
        """Получить статус InterruptManagementIntegration"""
        if not self._coordinator:
            return {
                "initialized": self._initialized,
                "running": self._running,
                "interrupts": {"status": "unknown"}
            }
        
        return {
            "initialized": self._initialized,
            "running": self._running,
            "interrupts": {
                "active_count": len(self._coordinator.active_interrupts),
                "total_count": len(self._coordinator.interrupt_history),
                "is_running": self._coordinator.is_running if hasattr(self._coordinator, 'is_running') else False
            }
        }
    
    async def request_interrupt(self, interrupt_type: InterruptType, priority: InterruptPriority = InterruptPriority.NORMAL, source: str = "integration", data: Dict[str, Any] = None) -> bool:
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
