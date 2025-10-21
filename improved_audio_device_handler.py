#!/usr/bin/env python3
"""
Улучшенный обработчик аудио устройств для Nexy
Решает проблему "залипания" AirPods в CoreAudio/PortAudio
"""

import logging
import time
import subprocess
from typing import Optional, Dict, Any, List
import sounddevice as sd

logger = logging.getLogger(__name__)

class ImprovedAudioDeviceHandler:
    """Улучшенный обработчик аудио устройств с принудительным обновлением CoreAudio"""
    
    def __init__(self):
        self.last_device_check = 0.0
        self.device_check_interval = 1.0  # Проверяем каждую секунду
        self.force_coreaudio_refresh = True  # Принудительно обновляем CoreAudio
        
    def get_current_input_device(self) -> Optional[Dict[str, Any]]:
        """Получает текущее входное устройство с принудительным обновлением"""
        try:
            # Принудительно обновляем CoreAudio если нужно
            if self.force_coreaudio_refresh:
                self._force_coreaudio_refresh()
            
            # Сбрасываем кеш PortAudio
            self._refresh_portaudio_cache()
            
            # Получаем текущее устройство
            default_setting = sd.default.device
            if hasattr(default_setting, '__getitem__'):
                device_id = default_setting[0]
                if device_id is not None:
                    try:
                        device_info = sd.query_devices(device_id, 'input')
                        return {
                            'id': device_id,
                            'info': device_info,
                            'name': device_info.get('name', 'Unknown')
                        }
                    except Exception as e:
                        logger.warning(f"⚠️ Не удалось получить информацию об устройстве {device_id}: {e}")
            
            return None
            
        except Exception as e:
            logger.error(f"❌ Ошибка получения текущего устройства: {e}")
            return None
    
    def _force_coreaudio_refresh(self):
        """Принудительно обновляет CoreAudio через системные команды"""
        try:
            # Выполняем команду для обновления CoreAudio
            result = subprocess.run(
                ["sudo", "killall", "coreaudiod"],
                capture_output=True,
                text=True,
                timeout=5
            )
            
            if result.returncode == 0:
                logger.info("🔄 CoreAudio перезапущен успешно")
                # Ждем стабилизации
                time.sleep(2.0)
            else:
                logger.warning(f"⚠️ Не удалось перезапустить CoreAudio: {result.stderr}")
                
        except subprocess.TimeoutExpired:
            logger.error("❌ Таймаут при перезапуске CoreAudio")
        except Exception as e:
            logger.error(f"❌ Ошибка перезапуска CoreAudio: {e}")
    
    def _refresh_portaudio_cache(self):
        """Сбрасывает кеш PortAudio"""
        try:
            # Сохраняем текущие настройки
            original_default = sd.default.device
            
            # Сбрасываем кеш
            sd.default.device = (None, None)
            
            # Восстанавливаем настройки
            sd.default.device = original_default
            
            logger.debug("🔄 Кеш PortAudio сброшен")
            
        except Exception as e:
            logger.warning(f"⚠️ Ошибка сброса кеша PortAudio: {e}")
    
    def check_device_availability(self, device_id: Any) -> bool:
        """Проверяет доступность устройства"""
        try:
            device_info = sd.query_devices(device_id, 'input')
            
            # Проверяем, что устройство имеет входные каналы
            if device_info.get('max_input_channels', 0) <= 0:
                return False
            
            # Проверяем настройки устройства
            try:
                sd.check_input_settings(
                    device=device_id,
                    samplerate=44100,
                    channels=1,
                    dtype='float32'
                )
                return True
            except Exception:
                return False
                
        except Exception as e:
            logger.debug(f"⚠️ Устройство {device_id} недоступно: {e}")
            return False
    
    def get_available_input_devices(self) -> List[Dict[str, Any]]:
        """Получает список доступных входных устройств"""
        try:
            devices = sd.query_devices()
            available_devices = []
            
            for i, device in enumerate(devices):
                if device.get('max_input_channels', 0) > 0:
                    if self.check_device_availability(i):
                        available_devices.append({
                            'id': i,
                            'info': device,
                            'name': device.get('name', 'Unknown')
                        })
            
            return available_devices
            
        except Exception as e:
            logger.error(f"❌ Ошибка получения списка устройств: {e}")
            return []
    
    def find_best_input_device(self) -> Optional[Dict[str, Any]]:
        """Находит лучшее доступное входное устройство"""
        try:
            # Сначала пытаемся получить системное default
            current_device = self.get_current_input_device()
            if current_device and self.check_device_availability(current_device['id']):
                return current_device
            
            # Если default недоступен, ищем альтернативы
            available_devices = self.get_available_input_devices()
            
            # Сортируем по приоритету
            def device_priority(device):
                name = device['name'].lower()
                if 'built-in' in name or 'internal' in name:
                    return 0  # Встроенный микрофон - высший приоритет
                elif 'bluetooth' in name or 'airpods' in name:
                    return 2  # Bluetooth - низкий приоритет
                else:
                    return 1  # Остальные устройства
            
            available_devices.sort(key=device_priority)
            
            if available_devices:
                return available_devices[0]
            
            return None
            
        except Exception as e:
            logger.error(f"❌ Ошибка поиска лучшего устройства: {e}")
            return None
    
    def monitor_device_changes(self, callback: callable, interval: float = 1.0):
        """Мониторит изменения устройств"""
        import threading
        
        def monitor_loop():
            last_device = None
            
            while True:
                try:
                    current_device = self.get_current_input_device()
                    
                    if current_device != last_device:
                        if last_device is not None:
                            logger.info(f"🔄 Смена устройства: {last_device} -> {current_device}")
                            callback(last_device, current_device)
                        
                        last_device = current_device
                    
                    time.sleep(interval)
                    
                except Exception as e:
                    logger.error(f"❌ Ошибка мониторинга устройств: {e}")
                    time.sleep(interval)
        
        monitor_thread = threading.Thread(target=monitor_loop, daemon=True)
        monitor_thread.start()
        return monitor_thread

def test_improved_handler():
    """Тестирует улучшенный обработчик"""
    print("🚀 Тестируем улучшенный обработчик аудио устройств...")
    
    handler = ImprovedAudioDeviceHandler()
    
    # Получаем текущее устройство
    current_device = handler.get_current_input_device()
    if current_device:
        print(f"🎤 Текущее устройство: {current_device['name']} (ID: {current_device['id']})")
    else:
        print("❌ Текущее устройство не найдено")
    
    # Получаем список доступных устройств
    available_devices = handler.get_available_input_devices()
    print(f"📱 Доступно {len(available_devices)} входных устройств:")
    for device in available_devices:
        print(f"  - {device['name']} (ID: {device['id']})")
    
    # Находим лучшее устройство
    best_device = handler.find_best_input_device()
    if best_device:
        print(f"⭐ Лучшее устройство: {best_device['name']} (ID: {best_device['id']})")
    else:
        print("❌ Лучшее устройство не найдено")
    
    return True

if __name__ == "__main__":
    test_improved_handler()
