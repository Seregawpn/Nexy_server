"""
Решение 3: Hybrid Monitoring (Core Audio + Polling с экспоненциальным backoff)

Комбинация Core Audio Notifications (основной механизм) + Polling с экспоненциальным
backoff (fallback для случаев, когда нотификации не работают).

Преимущества:
- Надежность (два механизма обнаружения)
- Минимальное использование CPU (polling только как fallback)
- Работает даже если Core Audio Notifications не работают
- Простая реализация (улучшение текущего подхода)
"""

import logging
import threading
import time
from typing import Optional, Callable, Dict, Any, Literal
import platform

logger = logging.getLogger(__name__)

# Импорт Core Audio Notifications (Решение 1)
try:
    import sys
    import os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../solution_1_core_audio_notifications'))
    from device_switcher_core_audio import CoreAudioDeviceSwitcher
    CORE_AUDIO_SWITCHER_AVAILABLE = True
except ImportError:
    CORE_AUDIO_SWITCHER_AVAILABLE = False
    logger.warning("⚠️ CoreAudioDeviceSwitcher недоступен, используем только polling")

# Импорт для работы с устройствами
try:
    import sounddevice as sd
except ImportError:
    sd = None
    logger.warning("⚠️ sounddevice недоступен")


class HybridDeviceSwitcher:
    """
    Гибридный переключатель устройств.
    
    Использует Core Audio Notifications как основной механизм и
    Polling с экспоненциальным backoff как fallback.
    """
    
    def __init__(
        self,
        device_type: Literal["input", "output"] = "input",
        callback: Optional[Callable[[str, Optional[int], Dict[str, Any]], None]] = None,
        poll_interval: float = 0.5,
        max_poll_interval: float = 5.0,
        backoff_factor: float = 1.5
    ):
        """
        Инициализация гибридного переключателя устройств.
        
        Args:
            device_type: Тип устройства (input/output)
            callback: Функция, вызываемая при изменении устройства
            poll_interval: Начальный интервал polling (секунды)
            max_poll_interval: Максимальный интервал polling (секунды)
            backoff_factor: Фактор увеличения интервала polling
        """
        self.device_type = device_type
        self.callback = callback
        self.poll_interval = poll_interval
        self.max_poll_interval = max_poll_interval
        self.backoff_factor = backoff_factor
        
        # Core Audio Notifications (основной механизм)
        self._core_audio_switcher: Optional[CoreAudioDeviceSwitcher] = None
        self._core_audio_available = False
        
        # Polling (fallback)
        self._polling_thread: Optional[threading.Thread] = None
        self._stop_event = threading.Event()
        self._current_poll_interval = poll_interval
        
        # Состояние
        self._current_device_name: Optional[str] = None
        self._current_device_id: Optional[int] = None
        self._lock = threading.Lock()
        
        logger.info(
            f"🔧 HybridDeviceSwitcher создан "
            f"(device_type={device_type}, core_audio_available={CORE_AUDIO_SWITCHER_AVAILABLE})"
        )
    
    def start(self) -> bool:
        """
        Запуск гибридного мониторинга устройств.
        
        Returns:
            True если запуск успешен, False иначе
        """
        if not self.callback:
            logger.warning("⚠️ Callback не установлен, мониторинг не запущен")
            return False
        
        # ПРИОРИТЕТ 1: Пробуем запустить Core Audio Notifications
        if CORE_AUDIO_SWITCHER_AVAILABLE:
            try:
                self._core_audio_switcher = CoreAudioDeviceSwitcher(
                    device_type=self.device_type,
                    callback=self._on_device_changed
                )
                if self._core_audio_switcher.start():
                    self._core_audio_available = True
                    logger.info("✅ Core Audio Notifications запущены (основной механизм)")
                else:
                    logger.warning("⚠️ Core Audio Notifications не запустились, используем polling")
            except Exception as e:
                logger.warning(f"⚠️ Ошибка запуска Core Audio Notifications: {e}, используем polling")
        
        # ПРИОРИТЕТ 2: Запускаем Polling (всегда, как fallback или основной механизм)
        self._stop_event.clear()
        self._polling_thread = threading.Thread(
            target=self._polling_loop,
            name=f"HybridDeviceSwitcher-Polling-{self.device_type}",
            daemon=True
        )
        self._polling_thread.start()
        logger.info("✅ Polling запущен (fallback или основной механизм)")
        
        # Инициализируем текущее устройство
        self._update_current_device()
        
        return True
    
    def stop(self):
        """Остановка гибридного мониторинга устройств"""
        # Останавливаем Core Audio Notifications
        if self._core_audio_switcher:
            try:
                self._core_audio_switcher.stop()
                logger.info("✅ Core Audio Notifications остановлены")
            except Exception as e:
                logger.error(f"❌ Ошибка остановки Core Audio Notifications: {e}")
        
        # Останавливаем Polling
        self._stop_event.set()
        if self._polling_thread and self._polling_thread.is_alive():
            self._polling_thread.join(timeout=2.0)
            logger.info("✅ Polling остановлен")
    
    def _on_device_changed(self, device_name: str, device_id: Optional[int], device_info: Dict[str, Any]):
        """Обработка изменения устройства (вызывается из Core Audio или Polling)"""
        try:
            with self._lock:
                if device_name == self._current_device_name:
                    # Устройство не изменилось, но сбросим интервал polling
                    if not self._core_audio_available:
                        self._current_poll_interval = self.poll_interval
                    return
                
                old_device_name = self._current_device_name
                old_device_id = self._current_device_id
                
                self._current_device_name = device_name
                self._current_device_id = device_id
                
                # Сброс интервала polling при изменении устройства
                self._current_poll_interval = self.poll_interval
            
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
    
    def _polling_loop(self):
        """Цикл polling с экспоненциальным backoff"""
        logger.debug("🔄 Запуск цикла polling...")
        
        while not self._stop_event.is_set():
            try:
                # Проверяем изменение устройства
                device_name, device_id, device_info = self._get_current_device_info()
                
                if device_name:
                    # Устройство найдено, проверяем изменение
                    with self._lock:
                        if device_name != self._current_device_name:
                            # Устройство изменилось
                            self._on_device_changed(device_name, device_id, device_info)
                        else:
                            # Устройство не изменилось, увеличиваем интервал (экспоненциальный backoff)
                            if not self._core_audio_available:
                                self._current_poll_interval = min(
                                    self._current_poll_interval * self.backoff_factor,
                                    self.max_poll_interval
                                )
                
                # Ждем до следующей проверки
                self._stop_event.wait(self._current_poll_interval)
                
            except Exception as e:
                logger.error(f"❌ Ошибка в цикле polling: {e}", exc_info=True)
                self._stop_event.wait(1.0)  # Пауза при ошибке
        
        logger.debug("🔄 Цикл polling завершен")
    
    def _update_current_device(self):
        """Обновление информации о текущем устройстве"""
        try:
            device_name, device_id, device_info = self._get_current_device_info()
            with self._lock:
                self._current_device_name = device_name
                self._current_device_id = device_id
            logger.debug(f"📊 Текущее {self.device_type} устройство: {device_name} (ID: {device_id})")
        except Exception as e:
            logger.warning(f"⚠️ Ошибка обновления текущего устройства: {e}")
    
    def _get_current_device_info(self) -> tuple[Optional[str], Optional[int], Dict[str, Any]]:
        """Получение информации о текущем устройстве"""
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
        with self._lock:
            return self._current_device_name, self._current_device_id


if __name__ == "__main__":
    # Тестирование
    logging.basicConfig(level=logging.INFO)
    
    def on_device_changed(device_name: str, device_id: Optional[int], device_info: Dict[str, Any]):
        """Callback для тестирования"""
        print(f"🔄 Устройство изменилось: {device_name} (ID: {device_id})")
        print(f"   Информация: {device_info}")
    
    switcher = HybridDeviceSwitcher(
        device_type="input",
        callback=on_device_changed
    )
    
    print("🚀 Запуск гибридного мониторинга устройств...")
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
