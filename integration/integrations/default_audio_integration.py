"""
DefaultAudioIntegration - Интеграция DefaultAudioManager с EventBus
Тонкая обертка для интеграции DefaultAudioManager в общую архитектуру
"""

import asyncio
import logging
from dataclasses import dataclass
from typing import Optional, Dict, Any

from integration.core.event_bus import EventBus, EventPriority
from integration.core.state_manager import ApplicationStateManager, AppMode
from integration.core.error_handler import ErrorHandler

# Импорты нового модуля DefaultAudioManager
from modules.default_audio_manager import DefaultAudioManager, DefaultAudioConfig
from modules.default_audio_manager.core.types import (
    AudioStreamState, HealthStatus, StreamError, AudioMetrics
)
from modules.default_audio_manager.config.default_config import DefaultAudioConfigLoader

# Импорт конфигурации
from config.unified_config_loader import UnifiedConfigLoader

logger = logging.getLogger(__name__)

@dataclass
class DefaultAudioIntegrationConfig:
    """Конфигурация DefaultAudioIntegration"""
    enabled: bool = True
    auto_start: bool = True
    publish_health_events: bool = True
    publish_stream_events: bool = True
    publish_metrics_events: bool = True

class DefaultAudioIntegration:
    """Интеграция DefaultAudioManager с EventBus и ApplicationStateManager"""
    
    def __init__(
        self,
        event_bus: EventBus,
        state_manager: ApplicationStateManager,
        error_handler: ErrorHandler,
        config: Optional[DefaultAudioIntegrationConfig] = None,
    ):
        self.event_bus = event_bus
        self.state_manager = state_manager
        self.error_handler = error_handler
        
        # Конфигурация интеграции
        self.config = config or DefaultAudioIntegrationConfig()
        
        # Загружаем конфигурацию из unified_config.yaml
        unified_config = UnifiedConfigLoader()
        self.audio_config = DefaultAudioConfigLoader.load_from_unified_config(
            unified_config.get_default_audio_config()
        )
        
        # Создаем DefaultAudioManager
        self.audio_manager = DefaultAudioManager(self.audio_config)
        
        # Состояние
        self.is_initialized = False
        self.is_running = False
        
        # Настраиваем callbacks
        self._setup_callbacks()
        
        logger.info("🔧 [AUDIO] DefaultAudioIntegration инициализирован")
    
    def _setup_callbacks(self):
        """Настройка callback функций для DefaultAudioManager"""
        
        def on_stream_state_change(state: AudioStreamState):
            """Callback изменения состояния потока"""
            if self.config.publish_stream_events:
                asyncio.create_task(self._publish_stream_state_event(state))
        
        def on_health_status_change(status: HealthStatus):
            """Callback изменения статуса здоровья"""
            if self.config.publish_health_events:
                asyncio.create_task(self._publish_health_status_event(status))
        
        def on_error(error: StreamError):
            """Callback ошибки"""
            asyncio.create_task(self._handle_audio_error(error))
        
        def on_metrics_update(metrics: AudioMetrics):
            """Callback обновления метрик"""
            if self.config.publish_metrics_events:
                asyncio.create_task(self._publish_metrics_event(metrics))
        
        # Устанавливаем callbacks
        self.audio_config.on_stream_state_change = on_stream_state_change
        self.audio_config.on_health_status_change = on_health_status_change
        self.audio_config.on_error = on_error
        self.audio_config.on_metrics_update = on_metrics_update
    
    async def initialize(self) -> bool:
        """Инициализация интеграции"""
        try:
            if self.is_initialized:
                logger.warning("⚠️ [AUDIO] DefaultAudioIntegration уже инициализирован")
                return True
            
            logger.info("🔄 [AUDIO] Инициализация DefaultAudioIntegration...")
            
            # Подписываемся на события
            await self._setup_event_subscriptions()
            
            self.is_initialized = True
            logger.info("✅ [AUDIO] DefaultAudioIntegration инициализирован успешно")
            return True
            
        except Exception as e:
            logger.error(f"❌ [AUDIO] Ошибка инициализации DefaultAudioIntegration: {e}")
            await self.error_handler.handle_error(
                error=e,
                context="DefaultAudioIntegration.initialize",
                severity="error"
            )
            return False
    
    async def start(self) -> bool:
        """Запуск интеграции"""
        try:
            if not self.is_initialized:
                logger.error("❌ [AUDIO] DefaultAudioIntegration не инициализирован")
                return False
            
            if self.is_running:
                logger.warning("⚠️ [AUDIO] DefaultAudioIntegration уже запущен")
                return True
            
            logger.info("🔄 [AUDIO] Запуск DefaultAudioIntegration...")
            
            # Запускаем DefaultAudioManager
            success = await self.audio_manager.start()
            
            if success:
                self.is_running = True
                logger.info("✅ [AUDIO] DefaultAudioIntegration запущен успешно")
                
                # Публикуем событие запуска
                await self._publish_startup_event()
                
                return True
            else:
                logger.error("❌ [AUDIO] Не удалось запустить DefaultAudioManager")
                return False
                
        except Exception as e:
            logger.error(f"❌ [AUDIO] Ошибка запуска DefaultAudioIntegration: {e}")
            await self.error_handler.handle_error(
                error=e,
                context="DefaultAudioIntegration.start",
                severity="error"
            )
            return False
    
    async def stop(self) -> bool:
        """Остановка интеграции"""
        try:
            if not self.is_running:
                logger.warning("⚠️ [AUDIO] DefaultAudioIntegration не запущен")
                return True
            
            logger.info("🔄 [AUDIO] Остановка DefaultAudioIntegration...")
            
            # Останавливаем DefaultAudioManager
            success = await self.audio_manager.stop()
            
            if success:
                self.is_running = False
                logger.info("✅ [AUDIO] DefaultAudioIntegration остановлен успешно")
                
                # Публикуем событие остановки
                await self._publish_shutdown_event()
                
                return True
            else:
                logger.error("❌ [AUDIO] Не удалось остановить DefaultAudioManager")
                return False
                
        except Exception as e:
            logger.error(f"❌ [AUDIO] Ошибка остановки DefaultAudioIntegration: {e}")
            await self.error_handler.handle_error(
                error=e,
                context="DefaultAudioIntegration.stop",
                severity="error"
            )
            return False
    
    async def _setup_event_subscriptions(self):
        """Настройка подписок на события"""
        try:
            # Подписываемся на события режимов приложения
            await self.event_bus.subscribe(
                "mode.request",
                self._handle_mode_request,
                priority=EventPriority.MEDIUM
            )
            
            # Подписываемся на события состояния приложения
            await self.event_bus.subscribe(
                "app.state_change",
                self._handle_app_state_change,
                priority=EventPriority.MEDIUM
            )
            
            # Подписываемся на события смены режима приложения
            await self.event_bus.subscribe(
                "app.mode_changed",
                self._handle_app_mode_changed,
                priority=EventPriority.MEDIUM
            )
            
            logger.debug("🔍 [AUDIO] Подписки на события настроены")
            
        except Exception as e:
            logger.error(f"❌ [AUDIO] Ошибка настройки подписок: {e}")
    
    async def _handle_mode_request(self, event_data: Dict[str, Any]):
        """Обработка запроса смены режима"""
        try:
            target = event_data.get("target")
            if not target:
                return
            
            # Логируем смену режима
            logger.debug(f"🔄 [AUDIO] Получен запрос смены режима: {target}")
            
            # В зависимости от режима можем изменить поведение аудио
            if target == AppMode.LISTENING:
                # Режим прослушивания - запускаем аудио если не запущено
                if not self.is_running:
                    logger.info("🎤 [AUDIO] Запуск аудио для режима LISTENING")
                    await self.start()
            elif target == AppMode.SLEEPING:
                # Режим сна - можем остановить аудио для экономии ресурсов
                if self.is_running:
                    logger.info("😴 [AUDIO] Остановка аудио для режима SLEEPING")
                    await self.stop()
                
        except Exception as e:
            logger.error(f"❌ [AUDIO] Ошибка обработки запроса режима: {e}")
    
    async def _handle_app_state_change(self, event_data: Dict[str, Any]):
        """Обработка изменения состояния приложения"""
        try:
            state = event_data.get("state")
            if not state:
                return
            
            logger.debug(f"🔄 [AUDIO] Изменение состояния приложения: {state}")
            
            # Можем реагировать на изменения состояния приложения
            # Например, при сворачивании/разворачивании окна
            
        except Exception as e:
            logger.error(f"❌ [AUDIO] Ошибка обработки изменения состояния: {e}")
    
    async def _handle_app_mode_changed(self, event_data: Dict[str, Any]):
        """Обработка изменения режима приложения"""
        try:
            logger.info(f"🔍 [AUDIO] Получено событие app.mode_changed: {event_data}")
            
            data = event_data.get("data", {})
            # Проверяем разные возможные структуры события
            mode = data.get("mode")
            if not mode and "data" in data:
                # Возможна вложенная структура data.data.mode
                mode = data.get("data", {}).get("mode")
            
            if not mode:
                logger.warning(f"⚠️ [AUDIO] Нет данных о режиме в событии. Структура: {event_data}")
                return
            
            # Получаем значение режима
            if hasattr(mode, 'value'):
                mode_value = mode.value
            else:
                mode_value = str(mode).lower()
            
            logger.info(f"🔄 [AUDIO] Режим приложения изменен: {mode_value}")
            
            # Управляем аудио в зависимости от режима
            if mode_value == "listening":
                # Режим прослушивания - запускаем аудио если не запущено
                logger.info(f"🎤 [AUDIO] Обработка режима LISTENING, is_running={self.is_running}")
                if not self.is_running:
                    logger.info("🎤 [AUDIO] Запуск аудио для режима LISTENING")
                    await self.start()
                else:
                    logger.info("🎤 [AUDIO] Аудио уже запущено для режима LISTENING")
            elif mode_value == "sleeping":
                # Режим сна - останавливаем аудио для экономии ресурсов
                logger.info(f"😴 [AUDIO] Обработка режима SLEEPING, is_running={self.is_running}")
                if self.is_running:
                    logger.info("😴 [AUDIO] Остановка аудио для режима SLEEPING")
                    await self.stop()
                else:
                    logger.info("😴 [AUDIO] Аудио уже остановлено для режима SLEEPING")
            elif mode_value == "processing":
                # Режим обработки - останавливаем аудио (микрофон не нужен)
                logger.info(f"⚙️ [AUDIO] Обработка режима PROCESSING, is_running={self.is_running}")
                if self.is_running:
                    logger.info("⚙️ [AUDIO] Остановка аудио для режима PROCESSING")
                    await self.stop()
                else:
                    logger.info("⚙️ [AUDIO] Аудио уже остановлено для режима PROCESSING")
            
        except Exception as e:
            logger.error(f"❌ [AUDIO] Ошибка обработки изменения режима: {e}")
            import traceback
            traceback.print_exc()
    
    async def _publish_stream_state_event(self, state: AudioStreamState):
        """Публикация события изменения состояния потока"""
        try:
            await self.event_bus.publish("audio.stream_state_changed", {
                "state": state.value,
                "source": "DefaultAudioIntegration",
                "timestamp": asyncio.get_event_loop().time()
            })
            
        except Exception as e:
            logger.error(f"❌ [AUDIO] Ошибка публикации события состояния потока: {e}")
    
    async def _publish_health_status_event(self, status: HealthStatus):
        """Публикация события изменения статуса здоровья"""
        try:
            await self.event_bus.publish("audio.health_status_changed", {
                "status": status.value,
                "source": "DefaultAudioIntegration",
                "timestamp": asyncio.get_event_loop().time()
            })
            
        except Exception as e:
            logger.error(f"❌ [AUDIO] Ошибка публикации события статуса здоровья: {e}")
    
    async def _publish_metrics_event(self, metrics: AudioMetrics):
        """Публикация события обновления метрик"""
        try:
            await self.event_bus.publish("audio.metrics_updated", {
                "rms_value": metrics.rms_value,
                "peak_value": metrics.peak_value,
                "sample_count": metrics.sample_count,
                "error_count": metrics.error_count,
                "source": "DefaultAudioIntegration",
                "timestamp": asyncio.get_event_loop().time()
            })
            
        except Exception as e:
            logger.error(f"❌ [AUDIO] Ошибка публикации события метрик: {e}")
    
    async def _publish_startup_event(self):
        """Публикация события запуска"""
        try:
            await self.event_bus.publish("audio.integration_started", {
                "source": "DefaultAudioIntegration",
                "timestamp": asyncio.get_event_loop().time()
            })
            
        except Exception as e:
            logger.error(f"❌ [AUDIO] Ошибка публикации события запуска: {e}")
    
    async def _publish_shutdown_event(self):
        """Публикация события остановки"""
        try:
            await self.event_bus.publish("audio.integration_stopped", {
                "source": "DefaultAudioIntegration",
                "timestamp": asyncio.get_event_loop().time()
            })
            
        except Exception as e:
            logger.error(f"❌ [AUDIO] Ошибка публикации события остановки: {e}")
    
    async def _handle_audio_error(self, error: StreamError):
        """Обработка ошибки аудио"""
        try:
            # Публикуем событие ошибки
            await self.event_bus.publish("audio.error", {
                "error_type": error.error_type,
                "error_message": error.error_message,
                "retry_count": error.retry_count,
                "source": "DefaultAudioIntegration",
                "timestamp": error.timestamp
            })
            
            # Обрабатываем через ErrorHandler
            await self.error_handler.handle_error(
                error=Exception(f"{error.error_type}: {error.error_message}"),
                context="DefaultAudioIntegration.audio_error",
                severity="warning"
            )
            
        except Exception as e:
            logger.error(f"❌ [AUDIO] Ошибка обработки аудио ошибки: {e}")
    
    # Публичные методы для доступа к функциональности
    
    def get_audio_manager(self) -> DefaultAudioManager:
        """Получение экземпляра DefaultAudioManager"""
        return self.audio_manager
    
    def is_healthy(self) -> bool:
        """Проверка здоровья микрофона"""
        return self.audio_manager.is_healthy()
    
    def get_health_status(self) -> HealthStatus:
        """Получение статуса здоровья"""
        return self.audio_manager.get_health_status()
    
    def get_metrics(self) -> AudioMetrics:
        """Получение метрик аудио"""
        return self.audio_manager.get_metrics()
    
    def get_audio_data(self, max_samples: Optional[int] = None):
        """Получение аудио данных"""
        return self.audio_manager.get_audio_data(max_samples)
    
    async def __aenter__(self):
        """Async context manager entry"""
        await self.initialize()
        await self.start()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit"""
        await self.stop()
