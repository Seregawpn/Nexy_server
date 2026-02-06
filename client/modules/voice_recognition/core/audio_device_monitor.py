"""
Простой монитор аудио устройств для отслеживания смены input устройства
Минимальная реализация для проверки концепции стабилизации
"""

import logging
import threading
from typing import Any, Callable

logger = logging.getLogger(__name__)

# Lazy sounddevice import to prevent TCC trigger on module load
_sd_module = None

def _get_sd():
    """Lazy import sounddevice only when first needed."""
    global _sd_module
    if _sd_module is None:
        import sounddevice as sd
        _sd_module = sd
        logger.debug("🔧 sounddevice imported lazily in AudioDeviceMonitor")
    return _sd_module

class AudioDeviceMonitor:
    """Простой монитор для отслеживания текущего input устройства"""
    
    def __init__(self, check_interval: float = 0.5):
        """
        Инициализация монитора
        
        Args:
            check_interval: Интервал проверки устройств в секундах
        """
        self.check_interval = check_interval
        self.current_input_device: Any | None = None
        self.device_change_callback: Callable[[Any, Any], None] | None = None
        
        # Threading
        self._monitor_thread: threading.Thread | None = None
        self._stop_event = threading.Event()
        self._lock = threading.Lock()
        
        # Инициализация
        self._init_current_device()
        
        logger.info(f"🔧 AudioDeviceMonitor создан (интервал: {check_interval}с)")
    
    def _init_current_device(self):
        """Инициализация текущего устройства"""
        try:
            # Получаем текущий default input
            default_setting = _get_sd().default.device
            if hasattr(default_setting, '__getitem__'):
                self.current_input_device = default_setting[0]
            else:
                self.current_input_device = None
                
            logger.info(f"🎤 Текущий input device: {self.current_input_device}")
            
        except Exception as e:
            logger.warning(f"⚠️ Ошибка получения текущего устройства: {e}")
            self.current_input_device = None
    
    def set_device_change_callback(self, callback: Callable[[Any, Any], None]):
        """
        Установка callback для уведомления о смене устройства
        
        Args:
            callback: Функция, вызываемая при смене устройства
                     Принимает (old_device, new_device)
        """
        self.device_change_callback = callback
        logger.debug("🔔 Callback смены устройства установлен")
    
    def start_monitoring(self):
        """Запуск мониторинга устройств"""
        if self._monitor_thread and self._monitor_thread.is_alive():
            logger.warning("⚠️ Мониторинг уже запущен")
            return
            
        self._stop_event.clear()
        self._monitor_thread = threading.Thread(
            target=self._monitor_loop,
            name="AudioDeviceMonitor",
            daemon=True
        )
        self._monitor_thread.start()
        logger.info("🚀 Мониторинг аудио устройств запущен")
    
    def stop_monitoring(self):
        """Остановка мониторинга устройств"""
        if not self._monitor_thread or not self._monitor_thread.is_alive():
            return
            
        self._stop_event.set()
        self._monitor_thread.join(timeout=2.0)
        logger.info("🛑 Мониторинг аудио устройств остановлен")
    
    def _monitor_loop(self):
        """Основной цикл мониторинга"""
        logger.debug("🔄 Запуск цикла мониторинга устройств")
        
        while not self._stop_event.is_set():
            try:
                # Проверяем текущее устройство
                new_device = self._get_current_input_device()
                
                with self._lock:
                    if new_device != self.current_input_device:
                        old_device = self.current_input_device
                        self.current_input_device = new_device
                        
                        logger.info(f"🔄 Смена input устройства: {old_device} -> {new_device}")
                        
                        # Уведомляем о смене
                        if self.device_change_callback:
                            try:
                                self.device_change_callback(old_device, new_device)
                            except Exception as e:
                                logger.error(f"❌ Ошибка в callback смены устройства: {e}")
                
                # Ждем до следующей проверки
                self._stop_event.wait(self.check_interval)
                
            except Exception as e:
                logger.error(f"❌ Ошибка в цикле мониторинга: {e}")
                self._stop_event.wait(1.0)  # Пауза при ошибке
    
    def _get_current_input_device(self) -> Any | None:
        """Получение текущего input устройства"""
        try:
            default_setting = _get_sd().default.device
            if hasattr(default_setting, '__getitem__'):
                return default_setting[0]
            return None
        except Exception as e:
            logger.debug(f"⚠️ Ошибка получения устройства: {e}")
            return None
    
    def get_current_device(self) -> Any | None:
        """Получение текущего устройства (thread-safe)"""
        with self._lock:
            return self.current_input_device
    
    def is_monitoring(self) -> bool:
        """Проверка, запущен ли мониторинг"""
        return (self._monitor_thread is not None and 
                self._monitor_thread.is_alive() and 
                not self._stop_event.is_set())
