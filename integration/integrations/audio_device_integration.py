"""
AudioDeviceIntegration - Интеграция AudioDeviceManager с EventBus
Тонкая обертка для интеграции AudioDeviceManager в общую архитектуру
"""

import asyncio
import logging
from dataclasses import dataclass
from typing import Optional, Dict, Any, Set, Tuple

# import sounddevice as sd  # УДАЛЕНО: больше не используем sounddevice напрямую

# Пути уже добавлены в main.py - не дублируем

from integration.core.event_bus import EventBus, EventPriority
from integration.core.state_manager import ApplicationStateManager, AppMode
from integration.core.error_handler import ErrorHandler

# Импорты модуля AudioDeviceManager
from modules.audio_device_manager.core.device_manager import AudioDeviceManager
from modules.audio_device_manager.core.types import (
    AudioDevice, DeviceType, DeviceStatus, AudioDeviceManagerConfig
)
# VoiceOver логика перенесена в VoiceOverDuckingIntegration

# Импорт конфигурации
from config.unified_config_loader import UnifiedConfigLoader

logger = logging.getLogger(__name__)

# Убираем дублированную конфигурацию - используем AudioDeviceManagerConfig из модуля
# и дополнительные настройки из unified_config.yaml

class AudioDeviceIntegration:
    """Интеграция AudioDeviceManager с EventBus и ApplicationStateManager"""
    
    def __init__(
        self,
        event_bus: EventBus,
        state_manager: ApplicationStateManager,
        error_handler: ErrorHandler,
        config: Optional[AudioDeviceManagerConfig] = None,
    ):
        self.event_bus = event_bus
        self.state_manager = state_manager
        self.error_handler = error_handler
        # Загружаем конфигурацию из unified_config.yaml
        unified_config = UnifiedConfigLoader()
        if config is None:
            # Создаем конфигурацию модуля из unified_config
            config_data = unified_config._load_config()
            audio_cfg = (config_data.get('audio') or {}).get('device_manager') or {}
            integration_cfg = (config_data.get('integrations') or {}).get('audio_device') or {}
            
            config = AudioDeviceManagerConfig(
                auto_switch_enabled=integration_cfg.get('auto_switch_enabled', (config_data.get('audio') or {}).get('auto_switch', True)),
                monitoring_interval=integration_cfg.get('monitoring_interval', audio_cfg.get('monitoring_interval', 3.0)),
                switch_delay=integration_cfg.get('switch_delay', (config_data.get('audio') or {}).get('switch_delay', 0.5)),
                user_preferences=None,  # Будет заполнено в __post_init__
                macos_settings=None     # Будет заполнено в __post_init__
            )
        
        self.config = config
        
        # Дополнительные настройки интеграции из unified_config
        config_data = unified_config._load_config()
        integration_cfg = (config_data.get('integrations') or {}).get('audio_device') or {}
        self.enable_microphone_on_listening = integration_cfg.get('enable_microphone_on_listening', True)
        self.disable_microphone_on_sleeping = integration_cfg.get('disable_microphone_on_sleeping', True)
        self.disable_microphone_on_processing = integration_cfg.get('disable_microphone_on_processing', True)

        # VoiceOver логика перенесена в VoiceOverDuckingIntegration

        # AudioDeviceManager экземпляр
        self._manager: Optional[AudioDeviceManager] = None
        self._initialized = False
        self._running = False
        self._current_mode: Optional[AppMode] = None
        self._current_input_device_index: Optional[int] = None
        self._current_input_device_name: Optional[str] = None
        
        logger.info("AudioDeviceIntegration created")
    
    async def initialize(self) -> bool:
        """Инициализация AudioDeviceIntegration"""
        try:
            logger.info("Initializing AudioDeviceIntegration...")
            
            # Создаем конфигурацию AudioDeviceManager
            audio_config = AudioDeviceManagerConfig(
                auto_switch_enabled=self.config.auto_switch_enabled,
                monitoring_interval=self.config.monitoring_interval,
                switch_delay=self.config.switch_delay
            )
            
            # Создаем AudioDeviceManager
            self._manager = AudioDeviceManager(audio_config)
            
            # Настраиваем callbacks
            self._manager.set_device_changed_callback(self._sync_device_changed_wrapper)
            self._manager.set_device_switched_callback(self._on_device_switched)
            self._manager.set_error_callback(self._on_audio_error)
            
            # Не запускаем AudioDeviceManager на этапе initialize;
            # запуск выполняется в методе start()
            
            # Подписываемся на события приложения
            await self.event_bus.subscribe("app.startup", self._on_app_startup, EventPriority.MEDIUM)
            await self.event_bus.subscribe("app.shutdown", self._on_app_shutdown, EventPriority.MEDIUM)
            await self.event_bus.subscribe("app.state_changed", self._on_app_state_changed, EventPriority.HIGH)
            await self.event_bus.subscribe("app.mode_changed", self._on_app_mode_changed, EventPriority.HIGH)
            await self.event_bus.subscribe("audio.request_current_input_device", self._on_request_current_input_device, EventPriority.HIGH)
            await self.event_bus.subscribe("audio.request_unified_device", self._on_request_unified_device, EventPriority.HIGH)

            # VoiceOver подписки перенесены в VoiceOverDuckingIntegration
            
            self._initialized = True
            logger.info("AudioDeviceIntegration initialized successfully")
            return True
            
        except Exception as e:
            if hasattr(self.error_handler, 'handle_error'):
                await self.error_handler.handle_error(
                    severity="error",
                    category="audio",
                    message=f"Ошибка инициализации AudioDeviceIntegration: {e}",
                    context={"where": "audio.initialize"}
                )
            else:
                logger.error(f"Error in AudioDeviceIntegration.initialize: {e}")
            logger.error(f"Failed to initialize AudioDeviceIntegration: {e}")
            return False
    
    async def start(self) -> bool:
        """Запуск AudioDeviceIntegration"""
        if not self._initialized or not self._manager:
            logger.error("AudioDeviceIntegration not initialized")
            return False
        
        if self._running:
            logger.warning("AudioDeviceIntegration already running")
            return True
        
        try:
            logger.info("Starting AudioDeviceIntegration...")
            
            # Проверяем разрешения перед запуском аудио системы
            await self._check_audio_permissions()
            
            # Запускаем AudioDeviceManager
            success = await self._manager.start()
            if not success:
                logger.error("Failed to start AudioDeviceManager")
                return False
            
            self._running = True
            
            # Получаем текущий режим и настраиваем микрофон
            current_mode = self.state_manager.get_current_mode()
            await self._handle_mode_change(None, current_mode)
            
            # Инициализация устройств при старте через централизованный метод
            logger.debug("🔍 [AUDIO_DEBUG] Инициализация аудио устройств при старте...")
            best_input_device = await self._manager.get_best_input_device()
            best_output_device = await self._manager.get_best_output_device()
            
            # Небольшая задержка для завершения подписок на события
            await asyncio.sleep(0.1)
            
            # Публикуем события через централизованный метод
            await self._publish_device_events(
                input_device=best_input_device,
                output_device=best_output_device,
                reason="app_startup",
                source="AudioDeviceManager"
            )
            
            logger.info("AudioDeviceIntegration started successfully")
            return True
            
        except Exception as e:
            if hasattr(self.error_handler, 'handle_error'):
                await self.error_handler.handle_error(
                    severity="error",
                    category="audio",
                    message=f"Ошибка запуска AudioDeviceIntegration: {e}",
                    context={"where": "audio.start"}
                )
            else:
                logger.error(f"Error in AudioDeviceIntegration.start: {e}")
            logger.error(f"Failed to start AudioDeviceIntegration: {e}")
            return False
    
    async def stop(self) -> bool:
        """Остановка AudioDeviceIntegration"""
        if not self._manager:
            return True
        
        if not self._running:
            return True
        
        try:
            logger.info("Stopping AudioDeviceIntegration...")
            
            # Выключаем микрофон перед остановкой
            await self._disable_microphone()
            
            # Останавливаем AudioDeviceManager
            success = await self._manager.stop()
            if not success:
                logger.error("Failed to stop AudioDeviceManager")

            self._running = False
            # VoiceOver shutdown перенесен в VoiceOverDuckingIntegration
            logger.info("AudioDeviceIntegration stopped")
            return success
            
        except Exception as e:
            if hasattr(self.error_handler, 'handle_error'):
                await self.error_handler.handle_error(
                    severity="error",
                    category="audio",
                    message=f"Ошибка остановки AudioDeviceIntegration: {e}",
                    context={"where": "audio.stop"}
                )
            else:
                logger.error(f"Error in AudioDeviceIntegration.stop: {e}")
            logger.error(f"Failed to stop AudioDeviceIntegration: {e}")
            return False
    
    async def _on_app_startup(self, event):
        """Обработка события запуска приложения"""
        try:
            logger.info("App startup - initializing audio devices")
            
            if self._manager:
                # Получаем текущее аудио устройство
                current_device = await self._manager.get_current_device()
                
                # Публикуем снапшот аудио состояния
                await self.event_bus.publish("audio.device_snapshot", {
                    "current_device": current_device.name if current_device else "None",
                    "device_type": current_device.type.value if current_device else "unknown",
                    "is_available": current_device.is_available if current_device else False
                })

            # Инициализация устройств при старте через централизованный метод
            logger.debug("🔍 [AUDIO_DEBUG] Инициализация аудио устройств при старте...")
            best_input_device = await self._manager.get_best_input_device()
            best_output_device = await self._manager.get_best_output_device()
            
            # Публикуем события через централизованный метод
            await self._publish_device_events(
                input_device=best_input_device,
                output_device=best_output_device,
                reason="app_startup",
                source="AudioDeviceManager"
            )
            
        except Exception as e:
            if hasattr(self.error_handler, 'handle_error'):
                await self.error_handler.handle_error(
                    severity="warning",
                    category="audio",
                    message=f"Ошибка обработки app startup: {e}",
                    context={"where": "audio.app_startup"}
                )
            else:
                logger.error(f"Error in AudioDeviceIntegration.app_startup: {e}")
    
    async def _on_app_shutdown(self, event):
        """Обработка события остановки приложения"""
        try:
            logger.info("App shutdown - stopping AudioDeviceIntegration")
            await self.stop()
        except Exception as e:
            if hasattr(self.error_handler, 'handle_error'):
                await self.error_handler.handle_error(
                    severity="warning",
                    category="audio",
                    message=f"Ошибка обработки app shutdown: {e}",
                    context={"where": "audio.app_shutdown"}
                )
            else:
                logger.error(f"Error in AudioDeviceIntegration.app_shutdown: {e}")
    
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
                    category="audio",
                    message=f"Ошибка обработки смены режима: {e}",
                    context={"where": "audio.state_changed"}
                )
            else:
                logger.error(f"Error in AudioDeviceIntegration.state_changed: {e}")

    async def _on_app_mode_changed(self, event):
        """Обработка современного события смены режима (app.mode_changed)"""
        try:
            data = (event or {}).get("data", {})
            new_mode = data.get("mode")
            logger.info(f"AudioIntegration: app.mode_changed received mode={getattr(new_mode,'value',new_mode)}")
            logger.debug(f"AudioIntegration: app.mode_changed received data={data}, parsed new_mode={new_mode}")
            if new_mode is not None:
                await self._handle_mode_change(self._current_mode, new_mode)
        except Exception as e:
            if hasattr(self.error_handler, 'handle_error'):
                await self.error_handler.handle_error(
                    severity="warning",
                    category="audio",
                    message=f"Ошибка обработки app.mode_changed: {e}",
                    context={"where": "audio.mode_changed"}
                )
            else:
                logger.error(f"Error in AudioDeviceIntegration.mode_changed: {e}")
    
    async def _handle_mode_change(self, old_mode: Optional[AppMode], new_mode: AppMode):
        """Обработка смены режима приложения"""
        try:
            logger.info(f"Audio mode change: {old_mode} -> {new_mode}")
            logger.debug(f"AudioIntegration: current_mode(before)={self._current_mode}")

            self._current_mode = new_mode
            mode_value_str = getattr(new_mode, 'value', str(new_mode)).lower() if new_mode else ""

            if new_mode == AppMode.LISTENING:
                logger.debug("AudioIntegration: enabling microphone due to LISTENING")
                # В режиме прослушивания - включаем микрофон
                await self._enable_microphone()
            elif new_mode in [AppMode.SLEEPING, AppMode.PROCESSING]:
                logger.debug("AudioIntegration: disabling microphone due to SLEEPING/PROCESSING")
                # В режиме сна или обработки - выключаем микрофон
                await self._disable_microphone()

            # VoiceOver mode handling перенесен в VoiceOverDuckingIntegration

        except Exception as e:
            if hasattr(self.error_handler, 'handle_error'):
                await self.error_handler.handle_error(
                    severity="warning",
                    category="audio",
                    message=f"Ошибка обработки смены режима: {e}",
                    context={"where": "audio.mode_change"}
                )
            else:
                logger.error(f"Error in AudioDeviceIntegration.mode_change: {e}")
    
    async def _enable_microphone(self):
        """Включение микрофона через AudioDeviceManager"""
        try:
            if not self._manager:
                logger.warning("⚠️ [AUDIO_DEBUG] AudioDeviceManager не инициализирован")
                return
            
            logger.info("🔄 [AUDIO_SWITCH] Enabling microphone through AudioDeviceManager...")

            # Получаем лучшее INPUT устройство через AudioDeviceManager
            best_input_device = await self._manager.get_best_input_device()
            if not best_input_device:
                logger.warning("⚠️ [AUDIO_DEBUG] Нет доступных INPUT устройств")
                await self.event_bus.publish("audio.microphone_error", {
                    "error": "no_input_devices_available",
                    "context": "enable_microphone"
                })
                return
            
            # Переключаемся на лучшее INPUT устройство
            success = await self._manager.switch_to_input_device(best_input_device.id)
            if not success:
                logger.warning("⚠️ [AUDIO_ERROR] Не удалось переключиться на INPUT устройство")
                await self.event_bus.publish("audio.microphone_error", {
                    "error": "input_device_switch_failed",
                    "context": "enable_microphone"
                })
                return
            
            # Публикуем событие audio.input_device_selected с правильным portaudio_index
            await self._publish_device_events(
                input_device=best_input_device,
                output_device=None,
                reason="microphone_enabled",
                source="AudioDeviceIntegration"
            )
            
            logger.info(f"✅ [AUDIO_SUCCESS] Microphone enabled: {best_input_device.name}")
            
            # Публикуем событие включения микрофона (без физического переключения)
            await self.event_bus.publish("audio.microphone_enabled", {
                "device": "current_system_device",  # Используем текущее системное устройство
                "device_type": "input", 
                "is_available": True,
                "mode": "logical_enable"  # Указываем что это логическое включение
            })
            
            logger.info("🎤 Microphone enabled for voice recording (logical mode)")
            
        except Exception as e:
            logger.error(f"Error enabling microphone: {e}")
            await self.event_bus.publish("audio.microphone_error", {
                "error": str(e),
                "context": "enable_microphone"
            })
    
    async def _disable_microphone(self):
        """Выключение микрофона"""
        try:
            if not self._manager:
                return
            
            logger.info("Disabling microphone...")
            
            # ЛОГИЧЕСКОЕ выключение микрофона
            logger.info("✅ Microphone logically disabled")
            
            # Публикуем событие выключения микрофона
            await self.event_bus.publish("audio.microphone_disabled", {
                "reason": "mode_change",
                "mode": self._current_mode.value if self._current_mode else "unknown",
                "logical_disable": True
            })
            
            logger.info("🔇 Microphone disabled (logical mode)")
            
        except Exception as e:
            logger.error(f"Error disabling microphone: {e}")
            await self.event_bus.publish("audio.microphone_error", {
                "error": str(e),
                "context": "disable_microphone"
            })

    # УДАЛЕНО: _ensure_input_device_selected()
    # Теперь используем AudioDeviceManager.get_best_input_device() и switch_to_input_device()
    
    # УДАЛЕНО: Дублирующие методы для работы с sounddevice
    # Теперь используем AudioDeviceManager для управления устройствами
    # 
    # Удаленные методы:
    # - _get_sounddevice_defaults()
    # - _apply_sounddevice_input_default()
    # - _probe_input_device()
    # - _select_input_device_index()
    # - _reinitialize_portaudio()

    # VoiceOver методы перенесены в VoiceOverDuckingIntegration

    async def _on_device_changed(self, change):
        """Обработка изменения аудио устройств"""
        try:
            logger.debug(f"Audio devices changed: +{len(change.added)} -{len(change.removed)}")
            
            # Публикуем событие изменения устройств
            await self.event_bus.publish("audio.device_changed", {
                "added": [device.name for device in change.added],
                "removed": [device.name for device in change.removed],
                "total_devices": len(change.added) + len(change.removed)
            })
            
            # Если микрофон включен и устройство ввода изменилось, переключаемся
            if self._current_mode == AppMode.LISTENING:
                await self._enable_microphone()
            
        except Exception as e:
            if hasattr(self.error_handler, 'handle_error'):
                await self.error_handler.handle_error(
                    severity="warning",
                    category="audio",
                    message=f"Ошибка обработки изменения устройств: {e}",
                    context={"where": "audio.device_changed"}
                )
            else:
                logger.error(f"Error in AudioDeviceIntegration.device_changed: {e}")
    
    async def _on_device_switched(self, from_device: AudioDevice, to_device: AudioDevice):
        """Обработка переключения аудио устройства"""
        try:
            logger.info(f"Audio device switched: {from_device.name} -> {to_device.name}")
            
            # Публикуем событие переключения устройства
            await self.event_bus.publish("audio.device_switched", {
                "from_device": from_device.name,
                "to_device": to_device.name,
                "device_type": to_device.type.value,
                "is_available": to_device.is_available
            })
            # События audio.input_device_selected и audio.output_device_selected 
            # будут опубликованы в _on_app_mode_changed после успешного переключения
            
            # События audio.input_device_selected и audio.output_device_selected 
            # будут опубликованы в _on_app_mode_changed после успешного переключения

        except Exception as e:
            if hasattr(self.error_handler, 'handle_error'):
                await self.error_handler.handle_error(
                    severity="warning",
                    category="audio",
                    message=f"Ошибка обработки переключения устройства: {e}",
                    context={"where": "audio.device_switched"}
                )
            else:
                logger.error(f"Error in AudioDeviceIntegration.device_switched: {e}")
    
    async def _on_audio_error(self, error, context):
        """Обработка ошибок аудио"""
        try:
            logger.error(f"Audio error in {context}: {error}")
            
            # Публикуем событие ошибки аудио
            await self.event_bus.publish("audio.error", {
                "error": str(error),
                "context": context,
                "severity": "error"
            })
            
        except Exception as e:
            logger.error(f"Error handling audio error: {e}")
    
    def _sync_device_changed_wrapper(self, change):
        """Sync wrapper для async _on_device_changed"""
        try:
            import asyncio
            loop = asyncio.get_event_loop()
            if loop.is_running():
                asyncio.run_coroutine_threadsafe(self._on_device_changed(change), loop)
            else:
                asyncio.run(self._on_device_changed(change))
        except Exception as e:
            logger.error(f"❌ Ошибка в sync wrapper device_changed: {e}")
    
    def get_status(self) -> Dict[str, Any]:
        """Получить статус AudioDeviceIntegration"""
        if not self._manager:
            return {
                "initialized": self._initialized,
                "running": self._running,
                "audio": {"status": "unknown"}
            }
        
        return {
            "initialized": self._initialized,
            "running": self._running,
            "current_mode": self._current_mode.value if self._current_mode else "unknown",
            "audio": {
                "manager_running": self._manager.is_running if hasattr(self._manager, 'is_running') else False,
                "current_device": self._manager.current_device.name if self._manager.current_device else "None"
            }
        }
    
    async def get_current_device(self) -> Optional[AudioDevice]:
        """Получить текущее аудио устройство"""
        if not self._manager:
            return None
        
        try:
            return await self._manager.get_current_device()
        except Exception as e:
            logger.error(f"Error getting current device: {e}")
            return None
    
    async def switch_to_device(self, device: AudioDevice) -> bool:
        """Переключиться на указанное устройство"""
        if not self._manager:
            return False
        
        try:
            return await self._manager.switch_to_device(device)
        except Exception as e:
            logger.error(f"Error switching to device {device.name}: {e}")
            return False
    
    async def _check_audio_permissions(self):
        """Проверить разрешения для аудио системы через AudioDeviceManager"""
        try:
            logger.debug("🔍 [AUDIO_DEBUG] Проверка разрешений через AudioDeviceManager...")
            
            # Проверяем доступность INPUT устройств через AudioDeviceManager
            best_input_device = await self._manager.get_best_input_device()
            if best_input_device:
                logger.info(f"✅ [AUDIO_SUCCESS] Microphone accessible: {best_input_device.name}")
                return True
            else:
                logger.info("ℹ️ [AUDIO_DEBUG] No INPUT devices available")
                return False
                
        except Exception as e:
            logger.info(f"ℹ️ [AUDIO_DEBUG] Audio input check failed: {e}")
            # Не блокируем запуск, просто информируем
            return False
    
    async def _on_request_current_input_device(self, event_data: dict):
        """Обработка запроса текущего INPUT устройства"""
        try:
            source = event_data.get("source", "unknown")
            reason = event_data.get("reason", "unknown")
            
            logger.debug(f"🔍 [AUDIO_DEBUG] Запрос текущего INPUT устройства от {source} (причина: {reason})")
            
            # Получаем текущее лучшее INPUT устройство
            best_input_device = await self._manager.get_best_input_device()
            
            if best_input_device:
                # Публикуем событие с текущим INPUT устройством
                await self.event_bus.publish("audio.input_device_selected", {
                    "device_id": best_input_device.id,
                    "name": best_input_device.name,
                    "type": best_input_device.type.value,
                    "channels": best_input_device.channels,
                    "priority": self._manager._get_input_priority(best_input_device),
                    "status": best_input_device.status.value,
                    "portaudio_index": best_input_device.portaudio_index,
                    "reason": f"requested_by_{source}",
                    "source": "AudioDeviceIntegration"
                })
                logger.info(f"✅ [AUDIO_SUCCESS] INPUT устройство отправлено в {source}: {best_input_device.name} (portaudio_index: {best_input_device.portaudio_index})")
            else:
                logger.warning(f"⚠️ [AUDIO_DEBUG] Нет доступных INPUT устройств для отправки в {source}")
                
        except Exception as e:
            logger.error(f"❌ [AUDIO_ERROR] Ошибка обработки запроса текущего INPUT устройства: {e}")
            if hasattr(self.error_handler, 'handle_error'):
                await self.error_handler.handle_error(
                    severity="error",
                    category="audio",
                    message=f"Ошибка обработки запроса текущего INPUT устройства: {e}",
                    context={"where": "audio.request_current_input_device"}
                )

    async def _on_request_unified_device(self, event_data: dict):
        """Обработка запроса унифицированного аудио устройства"""
        try:
            source = event_data.get("source", "unknown")
            reason = event_data.get("reason", "unknown")
            
            logger.debug(f"🔍 [AUDIO_DEBUG] Запрос унифицированного устройства от {source} (причина: {reason})")
            
            # Получаем унифицированное устройство
            unified_result = await self._manager.get_unified_audio_device()
            
            if unified_result["unified"]:
                # Одно устройство для обеих функций
                device = unified_result["input"]  # input и output одинаковые
                await self.event_bus.publish("audio.unified_device_selected", {
                    "device_id": device.id,
                    "name": device.name,
                    "type": device.type.value,
                    "channels": device.channels,
                    "priority": self._manager._get_input_priority(device),
                    "status": device.status.value,
                    "portaudio_index": device.portaudio_index,
                    "unified": True,
                    "input_device": {
                        "id": device.id,
                        "name": device.name,
                        "type": device.type.value,
                        "portaudio_index": device.portaudio_index
                    },
                    "output_device": {
                        "id": device.id,
                        "name": device.name,
                        "type": device.type.value,
                        "portaudio_index": device.portaudio_index
                    },
                    "reason": f"unified_requested_by_{source}",
                    "source": "AudioDeviceIntegration"
                })
                logger.info(f"✅ [AUDIO_SUCCESS] Унифицированное устройство отправлено в {source}: {device.name}")
            else:
                # Раздельные устройства
                input_device = unified_result["input"]
                output_device = unified_result["output"]
                
                await self.event_bus.publish("audio.unified_device_selected", {
                    "device_id": input_device.id if input_device else None,
                    "name": input_device.name if input_device else "None",
                    "type": input_device.type.value if input_device else "None",
                    "channels": input_device.channels if input_device else 0,
                    "priority": self._manager._get_input_priority(input_device) if input_device else 999,
                    "status": input_device.status.value if input_device else "None",
                    "portaudio_index": input_device.portaudio_index if input_device else None,
                    "unified": False,
                    "input_device": {
                        "id": input_device.id if input_device else None,
                        "name": input_device.name if input_device else "None",
                        "type": input_device.type.value if input_device else "None",
                        "portaudio_index": input_device.portaudio_index if input_device else None
                    },
                    "output_device": {
                        "id": output_device.id if output_device else None,
                        "name": output_device.name if output_device else "None",
                        "type": output_device.type.value if output_device else "None",
                        "portaudio_index": output_device.portaudio_index if output_device else None
                    },
                    "reason": f"separate_requested_by_{source}",
                    "source": "AudioDeviceIntegration"
                })
                logger.info(f"✅ [AUDIO_SUCCESS] Раздельные устройства отправлены в {source}: INPUT={input_device.name if input_device else 'None'}, OUTPUT={output_device.name if output_device else 'None'}")
                
        except Exception as e:
            logger.error(f"❌ [AUDIO_ERROR] Ошибка обработки запроса унифицированного устройства: {e}")
            if hasattr(self.error_handler, 'handle_error'):
                await self.error_handler.handle_error(
                    severity="error",
                    category="audio",
                    message=f"Ошибка обработки запроса унифицированного устройства: {e}",
                    context={"where": "audio.request_unified_device"}
                )

    async def _publish_device_events(self, input_device=None, output_device=None, reason="unknown", source="AudioDeviceManager"):
        """
        Централизованная публикация событий выбора аудио устройств.
        
        Args:
            input_device: AudioDevice для INPUT функции
            output_device: AudioDevice для OUTPUT функции  
            reason: Причина публикации события
            source: Источник события
        """
        try:
            # Публикуем событие INPUT устройства
            if input_device:
                portaudio_index = getattr(input_device, 'portaudio_index', None)
                logger.debug(f"🔍 [AUDIO_DEBUG] Публикация INPUT устройства: {input_device.name}, portaudio_index: {portaudio_index}")
                await self.event_bus.publish("audio.input_device_selected", {
                    "device_id": input_device.id,
                    "name": input_device.name,
                    "type": input_device.type.value,
                    "channels": input_device.channels,
                    "priority": input_device.priority.value,
                    "status": input_device.status.value,
                    "reason": reason,
                    "source": source,
                    "portaudio_index": portaudio_index
                })
                logger.info(f"✅ [AUDIO_SUCCESS] INPUT устройство опубликовано: {input_device.name} (reason: {reason}, portaudio_index: {portaudio_index})")
            
            # Публикуем событие OUTPUT устройства
            if output_device:
                portaudio_index = getattr(output_device, 'portaudio_index', None)
                logger.debug(f"🔍 [AUDIO_DEBUG] Публикация OUTPUT устройства: {output_device.name}, portaudio_index: {portaudio_index}")
                await self.event_bus.publish("audio.output_device_selected", {
                    "device_id": output_device.id,
                    "name": output_device.name,
                    "type": output_device.type.value,
                    "channels": output_device.channels,
                    "priority": output_device.priority.value,
                    "status": output_device.status.value,
                    "reason": reason,
                    "source": source,
                    "portaudio_index": portaudio_index
                })
                logger.info(f"✅ [AUDIO_SUCCESS] OUTPUT устройство опубликовано: {output_device.name} (reason: {reason}, portaudio_index: {portaudio_index})")
                
        except Exception as e:
            logger.error(f"❌ [AUDIO_ERROR] Ошибка публикации событий устройств: {e}")
            if hasattr(self.error_handler, 'handle_error'):
                await self.error_handler.handle_error(
                    severity="error",
                    category="audio",
                    message=f"Ошибка публикации событий устройств: {e}",
                    context={"where": "_publish_device_events", "reason": reason}
                )
