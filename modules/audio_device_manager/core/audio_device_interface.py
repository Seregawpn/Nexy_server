"""
AudioDeviceInterface - Единый интерфейс для работы с аудио устройствами

Предоставляет удобные методы для:
- Получения списка доступных устройств
- Выбора лучших устройств для INPUT/OUTPUT
- Переключения между устройствами
- Тестирования подключения устройств
- Мониторинга состояния устройств
"""

import asyncio
import logging
from typing import List, Optional, Dict, Any, Tuple
from dataclasses import dataclass

from .device_manager import AudioDeviceManager
from .types import AudioDevice, DeviceType, DeviceStatus, DevicePriority
from .device_switcher import DeviceSwitcher
from .device_monitor import DeviceMonitor

logger = logging.getLogger(__name__)


@dataclass
class DeviceTestResult:
    """Результат тестирования устройства"""
    device: AudioDevice
    success: bool
    error_message: Optional[str] = None
    test_duration_ms: float = 0.0
    audio_quality_score: float = 0.0


class AudioDeviceInterface:
    """Единый интерфейс для работы с аудио устройствами"""
    
    def __init__(self, config=None):
        """
        Инициализация интерфейса
        
        Args:
            config: Конфигурация AudioDeviceManager (опционально)
        """
        self._manager = AudioDeviceManager(config)
        self._initialized = False
        
        logger.info("🔧 [AUDIO_DEBUG] AudioDeviceInterface создан")
    
    async def initialize(self) -> bool:
        """Инициализация интерфейса"""
        try:
            logger.info("🔧 [AUDIO_DEBUG] Инициализация AudioDeviceInterface...")
            
            # Запускаем менеджер
            success = await self._manager.start()
            if not success:
                logger.error("❌ [AUDIO_ERROR] Не удалось запустить AudioDeviceManager")
                return False
            
            self._initialized = True
            logger.info("✅ [AUDIO_SUCCESS] AudioDeviceInterface инициализирован")
            return True
            
        except Exception as e:
            logger.error(f"❌ [AUDIO_ERROR] Ошибка инициализации AudioDeviceInterface: {e}")
            return False
    
    # ==================== ОСНОВНЫЕ МЕТОДЫ ====================
    
    async def get_available_devices(self, device_type: Optional[DeviceType] = None) -> List[AudioDevice]:
        """
        Получить список доступных устройств
        
        Args:
            device_type: Тип устройства (INPUT, OUTPUT, BOTH) или None для всех
            
        Returns:
            Список доступных устройств
        """
        try:
            if not self._initialized:
                logger.warning("⚠️ [AUDIO_DEBUG] AudioDeviceInterface не инициализирован")
                return []
            
            devices = await self._manager.get_available_devices()
            
            if device_type is None:
                return devices
            
            # Фильтруем по типу
            filtered_devices = []
            for device in devices:
                if device_type == DeviceType.INPUT and device.type in [DeviceType.INPUT, DeviceType.BOTH]:
                    filtered_devices.append(device)
                elif device_type == DeviceType.OUTPUT and device.type in [DeviceType.OUTPUT, DeviceType.BOTH]:
                    filtered_devices.append(device)
                elif device_type == DeviceType.BOTH and device.type == DeviceType.BOTH:
                    filtered_devices.append(device)
            
            logger.debug(f"🔍 [AUDIO_DEBUG] Найдено {len(filtered_devices)} устройств типа {device_type.value if device_type else 'ALL'}")
            return filtered_devices
            
        except Exception as e:
            logger.error(f"❌ [AUDIO_ERROR] Ошибка получения устройств: {e}")
            return []
    
    async def get_all_devices(self) -> List[AudioDevice]:
        """Получить все доступные устройства"""
        return await self.get_available_devices()
    
    async def get_input_devices(self) -> List[AudioDevice]:
        """Получить все INPUT устройства"""
        return await self.get_available_devices(DeviceType.INPUT)
    
    async def get_output_devices(self) -> List[AudioDevice]:
        """Получить все OUTPUT устройства"""
        return await self.get_available_devices(DeviceType.OUTPUT)
    
    async def get_best_input_device(self) -> Optional[AudioDevice]:
        """Получить лучшее INPUT устройство"""
        try:
            if not self._initialized:
                logger.warning("⚠️ [AUDIO_DEBUG] AudioDeviceInterface не инициализирован")
                return None
            
            device = await self._manager.get_best_input_device()
            if device:
                logger.debug(f"🔍 [AUDIO_DEBUG] Лучшее INPUT устройство: {device.name}")
            else:
                logger.warning("⚠️ [AUDIO_DEBUG] Нет доступных INPUT устройств")
            
            return device
            
        except Exception as e:
            logger.error(f"❌ [AUDIO_ERROR] Ошибка получения лучшего INPUT устройства: {e}")
            return None
    
    async def get_best_output_device(self) -> Optional[AudioDevice]:
        """Получить лучшее OUTPUT устройство"""
        try:
            if not self._initialized:
                logger.warning("⚠️ [AUDIO_DEBUG] AudioDeviceInterface не инициализирован")
                return None
            
            device = await self._manager.get_best_output_device()
            if device:
                logger.debug(f"🔍 [AUDIO_DEBUG] Лучшее OUTPUT устройство: {device.name}")
            else:
                logger.warning("⚠️ [AUDIO_DEBUG] Нет доступных OUTPUT устройств")
            
            return device
            
        except Exception as e:
            logger.error(f"❌ [AUDIO_ERROR] Ошибка получения лучшего OUTPUT устройства: {e}")
            return None
    
    async def switch_to_input_device(self, device_id: str) -> bool:
        """Переключиться на INPUT устройство"""
        try:
            if not self._initialized:
                logger.warning("⚠️ [AUDIO_DEBUG] AudioDeviceInterface не инициализирован")
                return False
            
            # Находим устройство по ID
            device = await self.find_device_by_id(device_id)
            if not device:
                logger.warning(f"⚠️ [AUDIO_DEBUG] Устройство с ID {device_id} не найдено")
                return False
            
            success = await self._manager.switch_to_input_device(device_id)
            if success:
                logger.info(f"✅ [AUDIO_SUCCESS] Переключились на INPUT устройство: {device.name}")
            else:
                logger.warning(f"⚠️ [AUDIO_DEBUG] Не удалось переключиться на INPUT устройство: {device.name}")
            
            return success
            
        except Exception as e:
            logger.error(f"❌ [AUDIO_ERROR] Ошибка переключения на INPUT устройство: {e}")
            return False
    
    async def switch_to_output_device(self, device_id: str) -> bool:
        """Переключиться на OUTPUT устройство"""
        try:
            if not self._initialized:
                logger.warning("⚠️ [AUDIO_DEBUG] AudioDeviceInterface не инициализирован")
                return False
            
            # Находим устройство по ID
            device = await self.find_device_by_id(device_id)
            if not device:
                logger.warning(f"⚠️ [AUDIO_DEBUG] Устройство с ID {device_id} не найдено")
                return False
            
            success = await self._manager.switch_to_output_device(device_id)
            if success:
                logger.info(f"✅ [AUDIO_SUCCESS] Переключились на OUTPUT устройство: {device.name}")
            else:
                logger.warning(f"⚠️ [AUDIO_DEBUG] Не удалось переключиться на OUTPUT устройство: {device.name}")
            
            return success
            
        except Exception as e:
            logger.error(f"❌ [AUDIO_ERROR] Ошибка переключения на OUTPUT устройство: {e}")
            return False
    
    # ==================== МЕТОДЫ ДЛЯ ТЕСТИРОВАНИЯ ====================
    
    async def test_device_connection(self, device: AudioDevice, test_duration_sec: float = 2.0) -> DeviceTestResult:
        """
        Тестировать подключение устройства
        
        Args:
            device: Устройство для тестирования
            test_duration_sec: Длительность теста в секундах
            
        Returns:
            Результат тестирования
        """
        import time
        start_time = time.time()
        
        try:
            logger.info(f"🔍 [AUDIO_DEBUG] Тестирование устройства: {device.name}")
            
            # Проверяем доступность устройства
            if not device.is_available:
                return DeviceTestResult(
                    device=device,
                    success=False,
                    error_message="Устройство недоступно",
                    test_duration_ms=(time.time() - start_time) * 1000
                )
            
            # Тестируем переключение
            if device.type in [DeviceType.INPUT, DeviceType.BOTH]:
                success = await self.switch_to_input_device(device.id)
                if not success:
                    return DeviceTestResult(
                        device=device,
                        success=False,
                        error_message="Не удалось переключиться на INPUT",
                        test_duration_ms=(time.time() - start_time) * 1000
                    )
            
            if device.type in [DeviceType.OUTPUT, DeviceType.BOTH]:
                success = await self.switch_to_output_device(device.id)
                if not success:
                    return DeviceTestResult(
                        device=device,
                        success=False,
                        error_message="Не удалось переключиться на OUTPUT",
                        test_duration_ms=(time.time() - start_time) * 1000
                    )
            
            # Симулируем тест качества (в реальности здесь был бы тест записи/воспроизведения)
            await asyncio.sleep(test_duration_sec)
            audio_quality_score = 0.8 + (device.priority.value * 0.1)  # Простая оценка на основе приоритета
            
            test_duration_ms = (time.time() - start_time) * 1000
            
            logger.info(f"✅ [AUDIO_SUCCESS] Устройство {device.name} протестировано успешно")
            
            return DeviceTestResult(
                device=device,
                success=True,
                test_duration_ms=test_duration_ms,
                audio_quality_score=audio_quality_score
            )
            
        except Exception as e:
            test_duration_ms = (time.time() - start_time) * 1000
            logger.error(f"❌ [AUDIO_ERROR] Ошибка тестирования устройства {device.name}: {e}")
            
            return DeviceTestResult(
                device=device,
                success=False,
                error_message=str(e),
                test_duration_ms=test_duration_ms
            )
    
    async def test_all_devices(self, test_duration_sec: float = 1.0) -> List[DeviceTestResult]:
        """
        Тестировать все доступные устройства
        
        Args:
            test_duration_sec: Длительность теста для каждого устройства
            
        Returns:
            Список результатов тестирования
        """
        try:
            logger.info("🔍 [AUDIO_DEBUG] Начинаем тестирование всех устройств...")
            
            devices = await self.get_available_devices()
            results = []
            
            for device in devices:
                result = await self.test_device_connection(device, test_duration_sec)
                results.append(result)
                
                # Небольшая пауза между тестами
                await asyncio.sleep(0.1)
            
            successful_tests = sum(1 for r in results if r.success)
            logger.info(f"✅ [AUDIO_SUCCESS] Тестирование завершено: {successful_tests}/{len(results)} устройств работают")
            
            return results
            
        except Exception as e:
            logger.error(f"❌ [AUDIO_ERROR] Ошибка тестирования всех устройств: {e}")
            return []
    
    # ==================== МЕТОДЫ ДЛЯ МОНИТОРИНГА ====================
    
    async def get_device_status(self) -> Dict[str, Any]:
        """Получить статус всех устройств"""
        try:
            if not self._initialized:
                return {"error": "AudioDeviceInterface не инициализирован"}
            
            devices = await self.get_available_devices()
            input_devices = await self.get_available_devices(DeviceType.INPUT)
            output_devices = await self.get_available_devices(DeviceType.OUTPUT)
            both_devices = await self.get_available_devices(DeviceType.BOTH)
            
            best_input = await self.get_best_input_device()
            best_output = await self.get_best_output_device()
            
            return {
                "total_devices": len(devices),
                "input_devices": len(input_devices),
                "output_devices": len(output_devices),
                "both_devices": len(both_devices),
                "best_input_device": best_input.name if best_input else None,
                "best_output_device": best_output.name if best_output else None,
                "devices": [
                    {
                        "id": device.id,
                        "name": device.name,
                        "type": device.type.value,
                        "status": device.status.value,
                        "priority": device.priority.value,
                        "channels": device.channels,
                        "is_available": device.is_available
                    }
                    for device in devices
                ]
            }
            
        except Exception as e:
            logger.error(f"❌ [AUDIO_ERROR] Ошибка получения статуса устройств: {e}")
            return {"error": str(e)}
    
    async def print_device_info(self):
        """Вывести информацию об устройствах в консоль"""
        try:
            status = await self.get_device_status()
            
            if "error" in status:
                print(f"❌ Ошибка: {status['error']}")
                return
            
            print("\n" + "="*60)
            print("🎵 ИНФОРМАЦИЯ ОБ АУДИО УСТРОЙСТВАХ")
            print("="*60)
            
            print(f"📊 Общая статистика:")
            print(f"   Всего устройств: {status['total_devices']}")
            print(f"   INPUT устройств: {status['input_devices']}")
            print(f"   OUTPUT устройств: {status['output_devices']}")
            print(f"   BOTH устройств: {status['both_devices']}")
            
            print(f"\n🏆 Лучшие устройства:")
            print(f"   INPUT: {status['best_input_device'] or 'Не найдено'}")
            print(f"   OUTPUT: {status['best_output_device'] or 'Не найдено'}")
            
            print(f"\n📋 Список всех устройств:")
            for i, device in enumerate(status['devices'], 1):
                status_icon = "✅" if device['is_available'] else "❌"
                type_icon = "🎤" if device['type'] == 'input' else "🔊" if device['type'] == 'output' else "🎧"
                
                print(f"   {i:2d}. {status_icon} {type_icon} {device['name']}")
                print(f"       ID: {device['id']}")
                print(f"       Тип: {device['type'].upper()}")
                print(f"       Статус: {device['status']}")
                print(f"       Приоритет: {device['priority']}")
                print(f"       Каналы: {device['channels']}")
                print()
            
            print("="*60)
            
        except Exception as e:
            logger.error(f"❌ [AUDIO_ERROR] Ошибка вывода информации об устройствах: {e}")
            print(f"❌ Ошибка: {e}")
    
    # ==================== МЕТОДЫ ДЛЯ УДОБСТВА ====================
    
    async def find_device_by_name(self, name: str) -> Optional[AudioDevice]:
        """Найти устройство по имени"""
        try:
            devices = await self.get_available_devices()
            for device in devices:
                if name.lower() in device.name.lower():
                    return device
            return None
        except Exception as e:
            logger.error(f"❌ [AUDIO_ERROR] Ошибка поиска устройства по имени: {e}")
            return None
    
    async def find_device_by_id(self, device_id: str) -> Optional[AudioDevice]:
        """Найти устройство по ID"""
        try:
            devices = await self.get_available_devices()
            for device in devices:
                if device.id == device_id:
                    return device
            return None
        except Exception as e:
            logger.error(f"❌ [AUDIO_ERROR] Ошибка поиска устройства по ID: {e}")
            return None
    
    async def switch_to_device_by_name(self, name: str, device_type: DeviceType) -> bool:
        """Переключиться на устройство по имени"""
        try:
            device = await self.find_device_by_name(name)
            if not device:
                logger.warning(f"⚠️ [AUDIO_DEBUG] Устройство с именем '{name}' не найдено")
                return False
            
            if device_type == DeviceType.INPUT:
                return await self.switch_to_input_device(device.id)
            elif device_type == DeviceType.OUTPUT:
                return await self.switch_to_output_device(device.id)
            else:
                logger.warning(f"⚠️ [AUDIO_DEBUG] Неподдерживаемый тип устройства: {device_type}")
                return False
                
        except Exception as e:
            logger.error(f"❌ [AUDIO_ERROR] Ошибка переключения на устройство по имени: {e}")
            return False
    
    async def get_system_status(self) -> Dict[str, Any]:
        """Получить статус аудиосистемы"""
        try:
            if not self._initialized:
                logger.warning("⚠️ [AUDIO_DEBUG] AudioDeviceInterface не инициализирован")
                return {}
            
            all_devices = await self.get_all_devices()
            input_devices = await self.get_input_devices()
            output_devices = await self.get_output_devices()
            
            return {
                "total_devices": len(all_devices),
                "input_devices_count": len(input_devices),
                "output_devices_count": len(output_devices),
                "both_devices_count": sum(1 for d in all_devices if d.type == DeviceType.BOTH),
                "current_input_device": self._manager.current_input_device.name if self._manager.current_input_device else "None",
                "current_output_device": self._manager.current_output_device.name if self._manager.current_output_device else "None",
                "is_manager_running": self._manager.is_running
            }
            
        except Exception as e:
            logger.error(f"❌ [AUDIO_ERROR] Ошибка получения статуса системы: {e}")
            return {}
    
    async def cleanup(self):
        """Очистка ресурсов"""
        try:
            if self._manager:
                await self._manager.stop()
            self._initialized = False
            logger.info("✅ [AUDIO_SUCCESS] AudioDeviceInterface очищен")
        except Exception as e:
            logger.error(f"❌ [AUDIO_ERROR] Ошибка очистки AudioDeviceInterface: {e}")
