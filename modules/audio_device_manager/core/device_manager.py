"""
Главный менеджер аудио устройств
"""

import asyncio
import logging
from typing import Optional, Dict, Any, List, Callable

from .types import (
    AudioDevice, DeviceChange, DeviceType, DeviceStatus, 
    DeviceMetrics, AudioDeviceManagerConfig,
    DeviceChangeCallback, DeviceSwitchCallback, ErrorCallback, MetricsCallback
)
from .device_monitor import DeviceMonitor
from .device_switcher import DeviceSwitcher

logger = logging.getLogger(__name__)


class AudioDeviceManager:
    """Главный менеджер аудио устройств"""
    
    def __init__(self, config: Optional[AudioDeviceManagerConfig] = None):
        logger.info("🎯 [AUDIO_REFACTOR] Начало инициализации AudioDeviceManager...")
        self.config = config or AudioDeviceManagerConfig()
        logger.debug(f"🔍 [AUDIO_DEBUG] Загрузка конфигурации: separate_input_output={self.config.separate_input_output_management}")
        
        # Компоненты модуля
        self.device_monitor = DeviceMonitor()
        self.device_switcher = DeviceSwitcher(self.device_monitor)
        
        # Состояние
        self.is_running = False
        self.current_device: Optional[AudioDevice] = None
        self.metrics = DeviceMetrics()
        
        # Новые поля для поддержки INPUT/OUTPUT
        self.current_input_device: Optional[AudioDevice] = None
        self.current_output_device: Optional[AudioDevice] = None
        self.input_devices: Dict[str, AudioDevice] = {}
        self.output_devices: Dict[str, AudioDevice] = {}
        
        # Callbacks
        self.on_device_changed: Optional[DeviceChangeCallback] = None
        self.on_device_switched: Optional[DeviceSwitchCallback] = None
        self.on_error: Optional[ErrorCallback] = None
        self.on_metrics_updated: Optional[MetricsCallback] = None
        
        # Настройка компонентов
        self._setup_components()
        logger.info("✅ [AUDIO_SUCCESS] AudioDeviceManager инициализирован")
    
    def _setup_components(self):
        """Настройка компонентов"""
        try:
            # Настраиваем DeviceMonitor
            self.device_monitor.register_callback("device_manager", self._on_device_changed)
            
            # Настраиваем DeviceSwitcher
            self.device_switcher.set_switch_callback(self._on_device_switched)
            
            logger.info("✅ Компоненты AudioDeviceManager настроены")
        except Exception as e:
            logger.error(f"❌ Ошибка настройки компонентов: {e}")
            raise
    
    async def start(self) -> bool:
        """Запуск менеджера устройств"""
        try:
            if self.is_running:
                logger.warning("⚠️ AudioDeviceManager уже запущен")
                return True
            
            logger.info("🚀 Запуск AudioDeviceManager...")
            
            # Запускаем мониторинг
            await self.device_monitor.start_monitoring()
            
            # Получаем начальный список устройств через DeviceMonitor
            devices = await self.device_monitor.get_available_devices()
            self.metrics.total_devices = len(devices)
            self.metrics.available_devices = len([d for d in devices if d.is_available])
            self.metrics.unavailable_devices = len([d for d in devices if not d.is_available])
            
            # Разделяем устройства по типам
            await self._categorize_devices(devices)
            
            # Определяем текущее устройство
            self.current_device = self._find_current_device(devices)
            
            # Автоматически переключаемся на лучшее доступное устройство
            if self.config.auto_switch_enabled:
                await self._auto_switch_to_best_device()
            
            self.is_running = True
            logger.info(f"✅ AudioDeviceManager запущен, найдено {len(devices)} устройств")
            logger.info(f"📊 [AUDIO_STATS] INPUT устройств: {len(self.input_devices)}, OUTPUT устройств: {len(self.output_devices)}")
            
            # Уведомляем о метриках
            self._notify_metrics_updated()
            
            return True
            
        except Exception as e:
            logger.error(f"❌ Ошибка запуска AudioDeviceManager: {e}")
            self._notify_error(e, "start")
            return False
    
    async def stop(self) -> bool:
        """Остановка менеджера устройств"""
        try:
            if not self.is_running:
                logger.warning("⚠️ AudioDeviceManager не запущен")
                return True
            
            logger.info("🛑 Остановка AudioDeviceManager...")
            
            # Останавливаем мониторинг
            await self.device_monitor.stop_monitoring()
            
            self.is_running = False
            self.current_device = None
            
            logger.info("✅ AudioDeviceManager остановлен")
            return True
            
        except Exception as e:
            logger.error(f"❌ Ошибка остановки AudioDeviceManager: {e}")
            self._notify_error(e, "stop")
            return False
    
    async def get_available_devices(self, device_type: Optional[DeviceType] = None) -> List[AudioDevice]:
        """Получение списка доступных устройств"""
        try:
            devices = await self.device_monitor.get_available_devices()
            
            if device_type:
                devices = [d for d in devices if d.type == device_type]
            
            return devices
        except Exception as e:
            logger.error(f"❌ Ошибка получения устройств: {e}")
            self._notify_error(e, "get_available_devices")
            return []
    
    async def get_current_device(self) -> Optional[AudioDevice]:
        """Получение текущего устройства"""
        try:
            if not self.is_running:
                return None
            
            # Обновляем текущее устройство
            devices = await self.device_monitor.get_available_devices()
            self.current_device = self._find_current_device(devices)
            
            return self.current_device
        except Exception as e:
            logger.error(f"❌ Ошибка получения текущего устройства: {e}")
            self._notify_error(e, "get_current_device")
            return None
    
    async def switch_to_device(self, device: AudioDevice) -> bool:
        """Переключение на конкретное устройство"""
        try:
            if not self.is_running:
                logger.warning("⚠️ AudioDeviceManager не запущен")
                return False
            
            logger.info(f"🔄 Переключение на устройство: {device.name}")
            
            # Выполняем переключение через DeviceSwitcher
            success = await self.device_switcher._switch_to_device(device)
            
            if success:
                self.current_device = device
                self.metrics.total_switches += 1
                self.metrics.successful_switches += 1
                self.metrics.last_switch_time = device.last_seen
                logger.info(f"✅ Успешно переключились на: {device.name}")
            else:
                self.metrics.total_switches += 1
                self.metrics.failed_switches += 1
                logger.error(f"❌ Не удалось переключиться на: {device.name}")
            
            # Уведомляем о переключении
            self._notify_device_switched(device, success)
            self._notify_metrics_updated()
            
            return success
            
        except Exception as e:
            logger.error(f"❌ Ошибка переключения устройства: {e}")
            self._notify_error(e, "switch_to_device")
            return False
    
    async def get_best_device(self, device_type: DeviceType = DeviceType.OUTPUT) -> Optional[AudioDevice]:
        """Получение лучшего устройства по типу"""
        try:
            devices = await self.get_available_devices(device_type)
            if not devices:
                return None
            
            # Используем логику DeviceSwitcher для поиска лучшего устройства
            if hasattr(self.device_switcher, '_find_best_device'):
                return self.device_switcher._find_best_device(devices)
            else:
                # Если метод недоступен, используем простую логику
                output_devices = [d for d in devices if d.type == DeviceType.OUTPUT and d.is_available]
                if output_devices:
                    return min(output_devices, key=lambda x: x.priority.value)
                return None
        except Exception as e:
            logger.error(f"❌ Ошибка поиска лучшего устройства: {e}")
            self._notify_error(e, "get_best_device")
            return None
    
    def get_metrics(self) -> DeviceMetrics:
        """Получение метрик"""
        return self.metrics
    
    def is_device_available(self, device_id: str) -> bool:
        """Проверка доступности устройства"""
        try:
            device = self.device_monitor.get_device_by_id(device_id)
            return device is not None and device.is_available
        except Exception as e:
            logger.error(f"❌ Ошибка проверки доступности устройства: {e}")
            return False
    
    def set_auto_switch_enabled(self, enabled: bool):
        """Включение/отключение автоматического переключения"""
        self.config.auto_switch_enabled = enabled
        self.device_switcher.auto_switch_enabled = enabled
        logger.info(f"🔄 Автоматическое переключение: {'включено' if enabled else 'отключено'}")
    
    def set_device_priority(self, device_id: str, priority: int, device_type: str = "input"):
        """
        Установка приоритета устройства.
        УСТАРЕЛО: используйте set_input_device_priority или set_output_device_priority
        """
        logger.warning(f"⚠️ [AUDIO_DEBUG] set_device_priority устарел - используйте set_{device_type}_device_priority")
        if device_type == "input":
            self.set_input_device_priority(device_id, priority)
        elif device_type == "output":
            self.set_output_device_priority(device_id, priority)
    
    def set_input_device_priority(self, device_id: str, priority: int):
        """Установка приоритета INPUT устройства"""
        try:
            self.config.input_device_priorities[device_id] = priority
            logger.info(f"📊 Приоритет INPUT устройства {device_id} установлен: {priority}")
        except Exception as e:
            logger.error(f"❌ Ошибка установки приоритета INPUT устройства: {e}")
            self._notify_error(e, "set_input_device_priority")
    
    def set_output_device_priority(self, device_id: str, priority: int):
        """Установка приоритета OUTPUT устройства"""
        try:
            self.config.output_device_priorities[device_id] = priority
            logger.info(f"📊 Приоритет OUTPUT устройства {device_id} установлен: {priority}")
        except Exception as e:
            logger.error(f"❌ Ошибка установки приоритета OUTPUT устройства: {e}")
            self._notify_error(e, "set_output_device_priority")
    
    # Callback методы
    def set_device_changed_callback(self, callback: DeviceChangeCallback):
        """Установка callback для изменений устройств"""
        self.on_device_changed = callback
    
    def set_device_switched_callback(self, callback: DeviceSwitchCallback):
        """Установка callback для переключений устройств"""
        self.on_device_switched = callback
    
    def set_error_callback(self, callback: ErrorCallback):
        """Установка callback для ошибок"""
        self.on_error = callback
    
    def set_metrics_callback(self, callback: MetricsCallback):
        """Установка callback для метрик"""
        self.on_metrics_updated = callback
    
    # Внутренние методы
    def _find_current_device(self, devices: List[AudioDevice]) -> Optional[AudioDevice]:
        """Поиск текущего устройства"""
        try:
            # Ищем устройство по умолчанию
            default_devices = [d for d in devices if d.is_default and d.is_available]
            if default_devices:
                return default_devices[0]
            
            # Если нет устройства по умолчанию, ищем лучшее доступное устройство вывода
            output_devices = [d for d in devices if d.type in [DeviceType.OUTPUT, DeviceType.BOTH] and d.is_available]
            if output_devices:
                # Сортируем по приоритету (меньшее число = выше приоритет)
                best_device = min(output_devices, key=lambda x: self._get_output_priority(x))
                priority = self._get_output_priority(best_device)
                logger.info(f"🎯 Найдено лучшее устройство: {best_device.name} (приоритет: {priority})")
                return best_device
            
            return None
        except Exception as e:
            logger.error(f"❌ Ошибка поиска текущего устройства: {e}")
            return None
    
    async def _auto_switch_to_best_device(self):
        """Автоматическое переключение на лучшее устройство"""
        try:
            devices = await self.get_available_devices()
            if not devices:
                logger.warning("⚠️ Нет устройств для автоматического переключения")
                return
            
            # Находим лучшее устройство
            best_device = self._find_current_device(devices)
            if not best_device:
                logger.warning("⚠️ Не найдено подходящее устройство для переключения")
                return
            
            # Переключаемся на лучшее устройство
            logger.info(f"🔄 Автоматическое переключение на: {best_device.name}")
            success = await self.device_switcher.switch_to_best_output_device()
            
            if success:
                self.current_device = best_device
                logger.info(f"✅ Успешно переключились на: {best_device.name}")
                self.metrics.total_switches += 1
                self.metrics.successful_switches += 1
            else:
                logger.warning(f"⚠️ Не удалось переключиться на: {best_device.name}")
                self.metrics.total_switches += 1
            
        except Exception as e:
            logger.error(f"❌ Ошибка автоматического переключения: {e}")
    
    async def _handle_device_changes_async(self, change: DeviceChange):
        """Асинхронная обработка изменений устройств"""
        try:
            logger.debug("🔍 [DEBUG] Начало обработки изменений устройств")
            
            # Проверяем что DeviceSwitcher доступен
            if not self.device_switcher:
                logger.warning("⚠️ DeviceSwitcher недоступен")
                return
            
            logger.debug(f"🔍 [DEBUG] DeviceSwitcher: {type(self.device_switcher)}")
            logger.debug(f"🔍 [DEBUG] DeviceSwitcher методы: {dir(self.device_switcher)}")
            
            # Обрабатываем изменения через DeviceSwitcher
            if hasattr(self.device_switcher, 'handle_device_changes'):
                logger.debug("🔍 [DEBUG] Вызываем device_switcher.handle_device_changes")
                result = await self.device_switcher.handle_device_changes(change)
                logger.debug(f"🔍 [DEBUG] Результат handle_device_changes: {result}")
            else:
                logger.warning("⚠️ DeviceSwitcher не имеет метода handle_device_changes")
            
            # Если есть новые устройства, переключаемся на лучшее
            if change.added:
                logger.info(f"➕ Обнаружены новые устройства: {[d.name for d in change.added]}")
                logger.debug("🔍 [DEBUG] Вызываем _auto_switch_to_best_device")
                await self._auto_switch_to_best_device()
            
            logger.debug("🔍 [DEBUG] Завершение обработки изменений устройств")
            
        except Exception as e:
            logger.error(f"❌ Ошибка асинхронной обработки изменений: {e}")
            import traceback
            logger.error(f"🔍 [DEBUG] Traceback: {traceback.format_exc()}")
    
    def _on_device_changed(self, change: DeviceChange):
        """Обработка изменений устройств"""
        try:
            # Обновляем метрики
            self.metrics.total_devices = len(change.current_devices)
            self.metrics.available_devices = len([d for d in change.current_devices.values() if d.is_available])
            self.metrics.unavailable_devices = len([d for d in change.current_devices.values() if not d.is_available])
            
            # Обрабатываем изменения через DeviceSwitcher (без await)
            if hasattr(self.config, 'auto_switch_enabled') and self.config.auto_switch_enabled:
                # Создаем задачу для асинхронной обработки
                try:
                    logger.debug("🔍 [DEBUG] Создание задачи для обработки изменений")
                    loop = asyncio.get_event_loop()
                    logger.debug(f"🔍 [DEBUG] Event loop: {loop}")
                    logger.debug(f"🔍 [DEBUG] Event loop запущен: {loop.is_running()}")
                    
                    if loop.is_running():
                        # Используем create_task правильно
                        logger.debug("🔍 [DEBUG] Создаем задачу _handle_device_changes_async")
                        task = loop.create_task(self._handle_device_changes_async(change))
                        logger.debug(f"🔍 [DEBUG] Задача создана: {task}")
                        # Не ждем завершения задачи
                    else:
                        logger.debug("Event loop не запущен, пропускаем обработку изменений")
                except RuntimeError as e:
                    logger.debug(f"Нет активного event loop: {e}")
                except Exception as e:
                    logger.error(f"Ошибка создания задачи: {e}")
                    import traceback
                    logger.error(f"🔍 [DEBUG] Traceback создания задачи: {traceback.format_exc()}")
            
            # Уведомляем о изменениях
            self._notify_device_changed(change)
            self._notify_metrics_updated()
            
        except Exception as e:
            logger.error(f"❌ Ошибка обработки изменений устройств: {e}")
            self._notify_error(e, "_on_device_changed")
    
    def _on_device_switched(self, device: AudioDevice, success: bool):
        """Обработка переключения устройств"""
        try:
            if success:
                self.current_device = device
                self.metrics.successful_switches += 1
            else:
                self.metrics.failed_switches += 1
            
            self.metrics.total_switches += 1
            self.metrics.last_switch_time = device.last_seen
            
            # Уведомляем о переключении
            self._notify_device_switched(device, success)
            self._notify_metrics_updated()
            
        except Exception as e:
            logger.error(f"❌ Ошибка обработки переключения устройств: {e}")
            self._notify_error(e, "_on_device_switched")
    
    def _notify_device_changed(self, change: DeviceChange):
        """Уведомление об изменениях устройств"""
        if self.on_device_changed:
            try:
                self.on_device_changed(change)
            except Exception as e:
                logger.error(f"❌ Ошибка в callback изменений устройств: {e}")
    
    def _notify_device_switched(self, device: AudioDevice, success: bool):
        """Уведомление о переключении устройств"""
        if self.on_device_switched:
            try:
                self.on_device_switched(device, success)
            except Exception as e:
                logger.error(f"❌ Ошибка в callback переключения устройств: {e}")
    
    def _notify_error(self, error: Exception, context: str):
        """Уведомление об ошибках"""
        if self.on_error:
            try:
                self.on_error(error, context)
            except Exception as e:
                logger.error(f"❌ Ошибка в error callback: {e}")
    
    def _notify_metrics_updated(self):
        """Уведомление об обновлении метрик"""
        if self.on_metrics_updated:
            try:
                self.on_metrics_updated(self.metrics)
            except Exception as e:
                logger.error(f"❌ Ошибка в metrics callback: {e}")
    
    async def _categorize_devices(self, devices: List[AudioDevice]):
        """Разделение устройств по функциям INPUT/OUTPUT (одно устройство может быть в обеих категориях)"""
        logger.debug(f"🔍 [AUDIO_DEBUG] Категоризация {len(devices)} устройств по функциям...")
        
        self.input_devices.clear()
        self.output_devices.clear()
        
        for device in devices:
            # Устройство может поддерживать INPUT функцию
            if device.type in [DeviceType.INPUT, DeviceType.BOTH]:
                self.input_devices[device.id] = device
                logger.debug(f"🔍 [AUDIO_DEBUG] Устройство поддерживает INPUT: {device.name}")
            
            # Устройство может поддерживать OUTPUT функцию
            if device.type in [DeviceType.OUTPUT, DeviceType.BOTH]:
                self.output_devices[device.id] = device
                logger.debug(f"🔍 [AUDIO_DEBUG] Устройство поддерживает OUTPUT: {device.name}")
        
        logger.info(f"📊 [AUDIO_STATS] Категоризация завершена: {len(self.input_devices)} устройств с INPUT, {len(self.output_devices)} устройств с OUTPUT")
        logger.info(f"🔍 [AUDIO_DEBUG] Пример: AirPods будут в обеих категориях (INPUT и OUTPUT функции)")
    
    async def get_best_input_device(self) -> Optional[AudioDevice]:
        """Получение лучшего устройства для INPUT функции (микрофон)"""
        logger.debug(f"🔍 [AUDIO_DEBUG] Запрос лучшего устройства для INPUT функции...")
        
        if not self.input_devices:
            logger.warning(f"⚠️ [AUDIO_DEBUG] Нет устройств с INPUT функцией")
            return None
        
        # Ищем устройство с наивысшим приоритетом для INPUT функции
        best_device = None
        best_priority = float('inf')
        
        for device in self.input_devices.values():
            priority = self._get_input_priority(device)
            if priority < best_priority:
                best_priority = priority
                best_device = device
        
        if best_device:
            logger.info(f"✅ [AUDIO_SUCCESS] Лучшее устройство для INPUT: {best_device.name} (приоритет: {best_priority})")
        else:
            logger.warning(f"⚠️ [AUDIO_DEBUG] Не удалось найти лучшее устройство для INPUT")
        
        return best_device
    
    async def get_best_output_device(self) -> Optional[AudioDevice]:
        """Получение лучшего устройства для OUTPUT функции (динамики)"""
        logger.debug(f"🔍 [AUDIO_DEBUG] Запрос лучшего устройства для OUTPUT функции...")
        
        if not self.output_devices:
            logger.warning(f"⚠️ [AUDIO_DEBUG] Нет устройств с OUTPUT функцией")
            return None
        
        # Ищем устройство с наивысшим приоритетом для OUTPUT функции
        best_device = None
        best_priority = float('inf')
        
        for device in self.output_devices.values():
            priority = self._get_output_priority(device)
            if priority < best_priority:
                best_priority = priority
                best_device = device
        
        if best_device:
            logger.info(f"✅ [AUDIO_SUCCESS] Лучшее устройство для OUTPUT: {best_device.name} (приоритет: {best_priority})")
        else:
            logger.warning(f"⚠️ [AUDIO_DEBUG] Не удалось найти лучшее устройство для OUTPUT")
        
        return best_device

    async def get_unified_audio_device(self) -> Dict[str, Optional[AudioDevice]]:
        """
        Получение унифицированного аудио устройства.
        Приоритет: OUTPUT устройство, затем проверка поддержки INPUT.
        """
        logger.debug("🔍 [AUDIO_DEBUG] Запрос унифицированного аудио устройства...")
        
        # 1. Получаем лучшее OUTPUT устройство
        best_output = await self.get_best_output_device()
        
        if not best_output:
            logger.warning("⚠️ [AUDIO_DEBUG] Нет доступных OUTPUT устройств")
            return {
                "input": None,
                "output": None,
                "unified": False
            }
        
        # 2. Проверяем, поддерживает ли оно INPUT
        if best_output.type == DeviceType.BOTH:
            # Используем одно устройство для обеих функций
            logger.info(f"✅ [AUDIO_SUCCESS] Унифицированное устройство: {best_output.name} (INPUT + OUTPUT)")
            return {
                "input": best_output,
                "output": best_output,
                "unified": True
            }
        
        # 3. Если нет - выбираем отдельно
        best_input = await self.get_best_input_device()
        logger.info(f"🔍 [AUDIO_DEBUG] Раздельные устройства: INPUT={best_input.name if best_input else 'None'}, OUTPUT={best_output.name}")
        
        return {
            "input": best_input,
            "output": best_output,
            "unified": False
        }
    
    async def switch_to_input_device(self, device_id: str) -> bool:
        """Переключение на INPUT функцию устройства (например, микрофон AirPods)"""
        try:
            # Находим устройство по ID
            device = self.input_devices.get(device_id)
            if not device:
                logger.warning(f"⚠️ [AUDIO_DEBUG] INPUT устройство с ID {device_id} не найдено")
                return False
            
            logger.info(f"🔄 [AUDIO_SWITCH] Переключение на INPUT функцию устройства: {device.name}")
            
            success = await self.device_switcher._switch_to_input_device(device)
            if success:
                self.current_input_device = device
                logger.info(f"✅ [AUDIO_SUCCESS] Переключено на INPUT функцию: {device.name}")
            else:
                logger.error(f"❌ [AUDIO_ERROR] Не удалось переключиться на INPUT функцию: {device.name}")
            
            return success
        except Exception as e:
            logger.error(f"❌ [AUDIO_ERROR] Ошибка переключения INPUT функции: {e}")
            return False
    
    async def switch_to_output_device(self, device_id: str) -> bool:
        """Переключение на OUTPUT функцию устройства (например, динамики AirPods)"""
        try:
            # Находим устройство по ID
            device = self.output_devices.get(device_id)
            if not device:
                logger.warning(f"⚠️ [AUDIO_DEBUG] OUTPUT устройство с ID {device_id} не найдено")
                return False
            
            logger.info(f"🔄 [AUDIO_SWITCH] Переключение на OUTPUT функцию устройства: {device.name}")
            
            success = await self.device_switcher._switch_to_output_device(device)
            if success:
                self.current_output_device = device
                logger.info(f"✅ [AUDIO_SUCCESS] Переключено на OUTPUT функцию: {device.name}")
            else:
                logger.error(f"❌ [AUDIO_ERROR] Не удалось переключиться на OUTPUT функцию: {device.name}")
            
            return success
        except Exception as e:
            logger.error(f"❌ [AUDIO_ERROR] Ошибка переключения OUTPUT функции: {e}")
            return False
    
    def _get_input_priority(self, device: AudioDevice) -> int:
        """Получение приоритета INPUT устройства"""
        device_name_lower = device.name.lower()
        
        # Проверяем приоритеты из конфигурации в порядке важности
        for keyword, priority in self.config.input_device_priorities.items():
            if keyword in device_name_lower:
                logger.debug(f"🔍 [AUDIO_DEBUG] Устройство {device.name} соответствует ключевому слову '{keyword}' -> приоритет {priority}")
                return priority
        
        # Специальная обработка для iPhone Microphone (низкий приоритет)
        if 'iphone' in device_name_lower and 'microphone' in device_name_lower:
            logger.debug(f"🔍 [AUDIO_DEBUG] iPhone Microphone обнаружен: {device.name} -> приоритет 10")
            return 10
        
        # Специальная обработка для AirPods (высший приоритет)
        if 'airpods' in device_name_lower:
            logger.debug(f"🔍 [AUDIO_DEBUG] AirPods обнаружены: {device.name} -> приоритет 1")
            return 1
        
        # Специальная обработка для Beats (высокий приоритет)
        if 'beats' in device_name_lower:
            logger.debug(f"🔍 [AUDIO_DEBUG] Beats обнаружены: {device.name} -> приоритет 2")
            return 2
        
        # Специальная обработка для Bluetooth устройств
        if 'bluetooth' in device_name_lower:
            if 'microphone' in device_name_lower or 'headphones' in device_name_lower:
                logger.debug(f"🔍 [AUDIO_DEBUG] Bluetooth устройство обнаружено: {device.name} -> приоритет 3")
                return 3
        
        # Специальная обработка для встроенного микрофона MacBook (средний приоритет)
        if ('macbook' in device_name_lower or 'built-in' in device_name_lower or 'builtin' in device_name_lower):
            if 'microphone' in device_name_lower or 'input' in device_name_lower:
                logger.debug(f"🔍 [AUDIO_DEBUG] Встроенный микрофон обнаружен: {device.name} -> приоритет 7")
                return 7
        
        logger.debug(f"🔍 [AUDIO_DEBUG] Устройство {device.name} не соответствует ни одному ключевому слову -> приоритет 15")
        return 15  # Приоритет по умолчанию
    
    def _get_output_priority(self, device: AudioDevice) -> int:
        """Получение приоритета OUTPUT устройства"""
        device_name_lower = device.name.lower()
        
        # Проверяем приоритеты из конфигурации в порядке важности
        for keyword, priority in self.config.output_device_priorities.items():
            if keyword in device_name_lower:
                logger.debug(f"🔍 [AUDIO_DEBUG] Устройство {device.name} соответствует ключевому слову '{keyword}' -> приоритет {priority}")
                return priority
        
        # Специальная обработка для AirPods (высший приоритет)
        if 'airpods' in device_name_lower:
            logger.debug(f"🔍 [AUDIO_DEBUG] AirPods обнаружены: {device.name} -> приоритет 1")
            return 1
        
        # Специальная обработка для Beats (высокий приоритет)
        if 'beats' in device_name_lower:
            logger.debug(f"🔍 [AUDIO_DEBUG] Beats обнаружены: {device.name} -> приоритет 2")
            return 2
        
        # Специальная обработка для Bluetooth устройств
        if 'bluetooth' in device_name_lower:
            if 'headphones' in device_name_lower or 'speakers' in device_name_lower:
                logger.debug(f"🔍 [AUDIO_DEBUG] Bluetooth устройство обнаружено: {device.name} -> приоритет 3")
                return 3
        
        # Специальная обработка для встроенных динамиков MacBook (низкий приоритет)
        if ('macbook' in device_name_lower or 'built-in' in device_name_lower or 'builtin' in device_name_lower):
            if 'speakers' in device_name_lower or 'output' in device_name_lower:
                logger.debug(f"🔍 [AUDIO_DEBUG] Встроенные динамики обнаружены: {device.name} -> приоритет 8")
                return 8
        
        logger.debug(f"🔍 [AUDIO_DEBUG] Устройство {device.name} не соответствует ни одному ключевому слову -> приоритет 15")
        return 15  # Приоритет по умолчанию

    async def cleanup(self):
        """Очистка ресурсов"""
        try:
            await self.stop()
            logger.info("🧹 AudioDeviceManager очищен")
        except Exception as e:
            logger.error(f"❌ Ошибка очистки AudioDeviceManager: {e}")
