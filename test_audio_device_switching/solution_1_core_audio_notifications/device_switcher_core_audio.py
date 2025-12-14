"""
Решение 1: Core Audio Notifications (событийный подход)

Использование Core Audio Property Listeners через PyObjC для получения
событий изменения default input/output устройства в реальном времени.

Преимущества:
- Мгновенная реакция на изменения (без задержек polling)
- Минимальное использование CPU (только при реальных изменениях)
- Нативный подход macOS (используется системой)
- Работает для всех типов устройств (BT, USB, встроенные)
"""

import logging
import threading
import time
import asyncio
from typing import Optional, Callable, Dict, Any, Literal
import platform

logger = logging.getLogger(__name__)

# Попытка импорта PyObjC CoreAudio
try:
    from CoreAudio import (
        AudioObjectAddPropertyListener,
        AudioObjectRemovePropertyListener,
        AudioObjectGetPropertyData,
        AudioObjectPropertyAddress,
        kAudioObjectSystemObject,
        kAudioHardwarePropertyDefaultOutputDevice,
        kAudioHardwarePropertyDefaultInputDevice,
        kAudioObjectPropertyScopeGlobal,
        kAudioObjectPropertyElementMain,
    )
    import objc
    CORE_AUDIO_AVAILABLE = True
except ImportError:
    CORE_AUDIO_AVAILABLE = False
    logger.warning("⚠️ PyObjC CoreAudio недоступен, используем fallback на polling")
    AudioObjectAddPropertyListener = None
    AudioObjectRemovePropertyListener = None
    AudioObjectGetPropertyData = None
    AudioObjectPropertyAddress = None
    kAudioObjectSystemObject = None
    kAudioHardwarePropertyDefaultInputDevice = None
    kAudioHardwarePropertyDefaultOutputDevice = None
    kAudioObjectPropertyScopeGlobal = None
    kAudioObjectPropertyElementMain = None

# Импорт для работы с устройствами
try:
    import sounddevice as sd
except ImportError:
    sd = None
    logger.warning("⚠️ sounddevice недоступен")


class CoreAudioDeviceSwitcher:
    """
    Переключатель устройств на основе Core Audio Notifications.
    
    Подписывается на события изменения default input/output устройства
    через Core Audio Property Listeners и вызывает callback при изменении.
    """
    
    def __init__(
        self,
        device_type: Literal["input", "output"] = "input",
        callback: Optional[Callable[[str, Optional[int], Dict[str, Any]], None]] = None
    ):
        """
        Инициализация переключателя устройств.
        
        Args:
            device_type: Тип устройства (input/output)
            callback: Функция, вызываемая при изменении устройства
                     Принимает (device_name, device_id, device_info)
        """
        self.device_type = device_type
        self.callback = callback
        self._is_macos = platform.system() == "Darwin"
        self._core_audio_available = CORE_AUDIO_AVAILABLE and self._is_macos
        
        # Состояние
        self._listener_id: Optional[Any] = None
        self._property_address: Optional[Any] = None
        self._notification_lock = threading.Lock()
        self._current_device_name: Optional[str] = None
        self._current_device_id: Optional[int] = None
        
        # Event loop для async callback
        self._event_loop: Optional[asyncio.AbstractEventLoop] = None
        
        logger.info(
            f"🔧 CoreAudioDeviceSwitcher создан "
            f"(device_type={device_type}, core_audio={self._core_audio_available})"
        )
    
    def set_event_loop(self, loop: asyncio.AbstractEventLoop):
        """Установка event loop для async callback"""
        self._event_loop = loop
        logger.debug("✅ Event loop установлен для CoreAudioDeviceSwitcher")
    
    def start(self) -> bool:
        """
        Запуск мониторинга устройств через Core Audio Notifications.
        
        Returns:
            True если подписка успешна, False иначе (fallback на polling)
        """
        if not self._core_audio_available:
            logger.warning("⚠️ Core Audio недоступен, используем fallback на polling")
            return False
        
        if not self.callback:
            logger.warning("⚠️ Callback не установлен, мониторинг не запущен")
            return False
        
        try:
            with self._notification_lock:
                if self._listener_id is not None:
                    logger.warning("⚠️ Мониторинг уже запущен")
                    return True
                
                # Создаем callback для Core Audio
                def property_listener_callback(
                    inObjectID: int,
                    inNumberAddresses: int,
                    inAddresses: Any,
                    inClientData: Any
                ) -> int:
                    """Callback для нотификаций Core Audio"""
                    try:
                        logger.info(
                            f"🔔 Core Audio нотификация: default {self.device_type} устройство изменилось"
                        )
                        # Вызываем callback в отдельном потоке
                        threading.Thread(
                            target=self._handle_device_change,
                            name=f"DeviceChangeHandler-{self.device_type}",
                            daemon=True
                        ).start()
                        return 0  # kAudioObjectPropertyListenerSucceeded
                    except Exception as e:
                        logger.error(f"❌ Ошибка в callback нотификации: {e}", exc_info=True)
                        return 1  # kAudioObjectPropertyListenerFailed
                
                # Создаем адрес свойства для подписки
                property_id = (
                    kAudioHardwarePropertyDefaultInputDevice 
                    if self.device_type == "input" 
                    else kAudioHardwarePropertyDefaultOutputDevice
                )
                property_address = AudioObjectPropertyAddress(
                    property_id,
                    kAudioObjectPropertyScopeGlobal,
                    kAudioObjectPropertyElementMain
                )
                
                # Подписываемся на нотификации
                result = AudioObjectAddPropertyListener(
                    kAudioObjectSystemObject,
                    property_address,
                    property_listener_callback,
                    None  # inClientData
                )
                
                if result == 0:  # kAudioObjectPropertyListenerSucceeded
                    self._listener_id = property_listener_callback
                    self._property_address = property_address
                    logger.info(
                        f"✅ Подписка на Core Audio нотификации успешна ({self.device_type})"
                    )
                    
                    # Инициализируем текущее устройство
                    self._update_current_device()
                    
                    return True
                else:
                    logger.warning(
                        f"⚠️ Не удалось подписаться на Core Audio нотификации "
                        f"(код: {result}, device_type={self.device_type})"
                    )
                    return False
                    
        except Exception as e:
            logger.error(
                f"❌ Ошибка подписки на Core Audio нотификации ({self.device_type}): {e}",
                exc_info=True
            )
            return False
    
    def stop(self):
        """Остановка мониторинга устройств"""
        try:
            with self._notification_lock:
                if self._listener_id is None:
                    return
                
                if self._core_audio_available and self._property_address:
                    try:
                        result = AudioObjectRemovePropertyListener(
                            kAudioObjectSystemObject,
                            self._property_address,
                            self._listener_id,
                            None
                        )
                        if result == 0:
                            logger.info(f"✅ Отписка от Core Audio нотификаций успешна ({self.device_type})")
                        else:
                            logger.warning(f"⚠️ Ошибка отписки от нотификаций (код: {result})")
                    except Exception as e:
                        logger.error(f"❌ Ошибка при отписке от нотификаций: {e}", exc_info=True)
                
                self._listener_id = None
                self._property_address = None
                
        except Exception as e:
            logger.error(f"❌ Ошибка остановки мониторинга: {e}", exc_info=True)
    
    def _handle_device_change(self):
        """Обработка изменения устройства (вызывается из callback)"""
        try:
            # Получаем информацию о новом устройстве
            device_name, device_id, device_info = self._get_current_device_info()
            
            if device_name is None:
                logger.warning("⚠️ Не удалось получить информацию о новом устройстве")
                return
            
            # Проверяем, изменилось ли устройство
            with self._notification_lock:
                if device_name == self._current_device_name:
                    logger.debug(f"🔍 Устройство не изменилось: {device_name}")
                    return
                
                old_device_name = self._current_device_name
                old_device_id = self._current_device_id
                
                self._current_device_name = device_name
                self._current_device_id = device_id
            
            logger.info(
                f"🔄 Смена {self.device_type} устройства: "
                f"\"{old_device_name}\" (ID: {old_device_id}) -> "
                f"\"{device_name}\" (ID: {device_id})"
            )
            
            # Вызываем callback
            if self.callback:
                try:
                    self.callback(device_name, device_id, device_info)
                except Exception as e:
                    logger.error(f"❌ Ошибка в callback смены устройства: {e}", exc_info=True)
                    
        except Exception as e:
            logger.error(f"❌ Ошибка обработки изменения устройства: {e}", exc_info=True)
    
    def _update_current_device(self):
        """Обновление информации о текущем устройстве"""
        try:
            device_name, device_id, device_info = self._get_current_device_info()
            with self._notification_lock:
                self._current_device_name = device_name
                self._current_device_id = device_id
            logger.debug(f"📊 Текущее {self.device_type} устройство: {device_name} (ID: {device_id})")
        except Exception as e:
            logger.warning(f"⚠️ Ошибка обновления текущего устройства: {e}")
    
    def _get_current_device_info(self) -> tuple[Optional[str], Optional[int], Dict[str, Any]]:
        """
        Получение информации о текущем устройстве.
        
        Returns:
            tuple: (device_name, device_id, device_info)
        """
        try:
            # ПРИОРИТЕТ 1: Получаем через macOS API (SwitchAudioSource)
            device_name = self._get_device_name_via_macos_api()
            if device_name:
                # Ищем ID устройства в PortAudio
                device_id = self._find_device_id_by_name(device_name)
                device_info = {
                    "name": device_name,
                    "device_id": device_id,
                    "is_bluetooth": self._is_bluetooth_device(device_name),
                    "source": "macos_api"
                }
                return device_name, device_id, device_info
            
            # ПРИОРИТЕТ 2: Fallback через PortAudio
            if sd:
                default_setting = sd.default.device
                if hasattr(default_setting, '__getitem__'):
                    device_id = default_setting[0] if self.device_type == "input" else default_setting[1]
                    device_info_sd = sd.query_devices(device_id, self.device_type)
                    if device_info_sd:
                        device_name = device_info_sd.get('name', 'Unknown')
                        device_info = {
                            "name": device_name,
                            "device_id": device_id,
                            "is_bluetooth": self._is_bluetooth_device(device_name),
                            "source": "portaudio"
                        }
                        return device_name, device_id, device_info
            
            return None, None, {}
            
        except Exception as e:
            logger.warning(f"⚠️ Ошибка получения информации об устройстве: {e}")
            return None, None, {}
    
    def _get_device_name_via_macos_api(self) -> Optional[str]:
        """Получение имени устройства через macOS API (SwitchAudioSource)"""
        try:
            import subprocess
            import json
            
            result = subprocess.run(
                ['SwitchAudioSource', '-c', '-t', self.device_type, '-f', 'json'],
                capture_output=True,
                text=True,
                timeout=2
            )
            
            if result.returncode == 0:
                device_info = json.loads(result.stdout.strip())
                return device_info.get('name', '')
            
            return None
            
        except FileNotFoundError:
            logger.debug("⚠️ SwitchAudioSource не найден")
            return None
        except Exception as e:
            logger.debug(f"⚠️ Ошибка получения устройства через macOS API: {e}")
            return None
    
    def _find_device_id_by_name(self, device_name: str) -> Optional[int]:
        """Поиск ID устройства по имени в PortAudio"""
        if not sd:
            return None
        
        try:
            all_devices = sd.query_devices()
            for idx, dev in enumerate(all_devices):
                if self.device_type == "input":
                    if dev.get('max_input_channels', 0) > 0 and dev.get('name', '') == device_name:
                        return idx
                else:
                    if dev.get('max_output_channels', 0) > 0 and dev.get('name', '') == device_name:
                        return idx
            return None
        except Exception as e:
            logger.debug(f"⚠️ Ошибка поиска устройства по имени: {e}")
            return None
    
    def _is_bluetooth_device(self, device_name: str) -> bool:
        """Проверка, является ли устройство Bluetooth"""
        if not device_name:
            return False
        lowered = device_name.lower()
        return any(keyword in lowered for keyword in (
            "bluetooth", "airpod", "airpods", "beats", "headset", "earbud"
        ))
    
    def get_current_device(self) -> tuple[Optional[str], Optional[int]]:
        """Получение текущего устройства (thread-safe)"""
        with self._notification_lock:
            return self._current_device_name, self._current_device_id


if __name__ == "__main__":
    # Тестирование
    logging.basicConfig(level=logging.INFO)
    
    def on_device_changed(device_name: str, device_id: Optional[int], device_info: Dict[str, Any]):
        """Callback для тестирования"""
        print(f"🔄 Устройство изменилось: {device_name} (ID: {device_id})")
        print(f"   Информация: {device_info}")
    
    switcher = CoreAudioDeviceSwitcher(
        device_type="input",
        callback=on_device_changed
    )
    
    print("🚀 Запуск мониторинга устройств...")
    if switcher.start():
        print("✅ Мониторинг запущен. Переключите устройство в System Preferences для тестирования.")
        print("   Нажмите Ctrl+C для остановки...")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n🛑 Остановка мониторинга...")
            switcher.stop()
            print("✅ Мониторинг остановлен")
    else:
        print("❌ Не удалось запустить мониторинг (используйте fallback на polling)")
