"""
Простой монитор аудио устройств для отслеживания смены input устройства
Минимальная реализация для проверки концепции стабилизации
"""

import logging
import threading
import time
from typing import Optional, Callable, Any
import sounddevice as sd

logger = logging.getLogger(__name__)

class AudioDeviceMonitor:
    """Простой монитор для отслеживания текущего input устройства"""
    
    def __init__(self, check_interval: float = 0.5):
        """
        Инициализация монитора
        
        Args:
            check_interval: Интервал проверки устройств в секундах
        """
        self.check_interval = check_interval
        # ✅ ИЗМЕНЕНО: Храним имя устройства, а не ID (ID может меняться!)
        self.current_input_device_name: Optional[str] = None
        self.current_input_device_id: Optional[Any] = None
        self.device_change_callback: Optional[Callable[[Any, Any], None]] = None
        
        # Threading
        self._monitor_thread: Optional[threading.Thread] = None
        self._stop_event = threading.Event()
        self._lock = threading.Lock()
        
        # Инициализация
        self._init_current_device()
        
        logger.info(f"🔧 AudioDeviceMonitor создан (интервал: {check_interval}с)")
    
    def _init_current_device(self):
        """Инициализация текущего устройства"""
        try:
            # ✅ Получаем имя и ID устройства
            device_name, device_id = self._get_current_input_device()
            self.current_input_device_name = device_name
            self.current_input_device_id = device_id
            logger.info(f"🎤 Текущий input device: \"{device_name}\" (ID: {device_id})")
            
        except Exception as e:
            logger.warning(f"⚠️ Ошибка получения текущего устройства: {e}")
            self.current_input_device_name = None
            self.current_input_device_id = None
    
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
                # ✅ Проверяем текущее устройство (получаем имя и ID)
                new_device_name, new_device_id = self._get_current_input_device()
                
                with self._lock:
                    # ✅ КРИТИЧНО: Сравниваем по ИМЕНИ, а не по ID!
                    # ID может меняться при переподключении, но имя остаётся тем же
                    if new_device_name != self.current_input_device_name:
                        old_device_name = self.current_input_device_name
                        old_device_id = self.current_input_device_id
                        
                        # Обновляем оба значения
                        self.current_input_device_name = new_device_name
                        self.current_input_device_id = new_device_id
                        
                        logger.info(
                            f"🔄 Смена input устройства: \"{old_device_name}\" (ID: {old_device_id}) -> "
                            f"\"{new_device_name}\" (ID: {new_device_id})"
                        )
                        
                        # Уведомляем о смене (передаём ID для обратной совместимости)
                        if self.device_change_callback:
                            try:
                                self.device_change_callback(old_device_id, new_device_id)
                            except Exception as e:
                                logger.error(f"❌ Ошибка в callback смены устройства: {e}")
                    elif new_device_id != self.current_input_device_id:
                        # ✅ ID изменился, но имя то же - обновляем только ID
                        logger.debug(
                            f"🔄 ID устройства изменился, но имя то же: "
                            f"\"{new_device_name}\" (ID: {self.current_input_device_id} -> {new_device_id})"
                        )
                        self.current_input_device_id = new_device_id
                
                # Ждем до следующей проверки
                self._stop_event.wait(self.check_interval)
                
            except Exception as e:
                logger.error(f"❌ Ошибка в цикле мониторинга: {e}")
                self._stop_event.wait(1.0)  # Пауза при ошибке
    
    def _get_current_input_device(self) -> tuple[Optional[str], Optional[Any]]:
        """
        Получение текущего input устройства (имя и ID).
        
        ✅ УЛУЧШЕННАЯ ЛОГИКА:
        1. Сначала пробуем получить через macOS API (SwitchAudioSource) - актуальное устройство
        2. Находим ID устройства по имени в PortAudio
        3. Если не работает, используем sd.default.device как fallback
        4. Возвращаем (имя, ID) - имя используется для сравнения, ID для работы с PortAudio
        
        Returns:
            tuple: (device_name, device_id) или (None, None) если не найдено
        """
        try:
            # ✅ ПРИОРИТЕТ 1: Получаем через macOS API (актуальное устройство)
            device_name, device_id = self._get_device_via_macos_api()
            if device_name is not None and device_id is not None:
                return device_name, device_id
            
            # ✅ ПРИОРИТЕТ 2: Fallback через PortAudio
            default_setting = sd.default.device
            if hasattr(default_setting, '__getitem__'):
                try:
                    device_id = default_setting[0]
                    # Получаем имя устройства по ID
                    device_info = sd.query_devices(device_id, 'input')
                    if device_info:
                        device_name = device_info.get('name', 'Unknown')
                        return device_name, device_id
                except (IndexError, Exception) as e:
                    logger.debug(f"⚠️ Ошибка получения устройства через sd.default.device: {e}")
            
            return None, None
        except Exception as e:
            logger.debug(f"⚠️ Ошибка получения устройства: {e}")
            return None, None
    
    def _get_device_via_macos_api(self, max_retries: int = 3, base_delay: float = 0.3) -> tuple[Optional[str], Optional[Any]]:
        """
        Получает имя и ID устройства через macOS API (SwitchAudioSource).
        
        ✅ УЛУЧШЕНИЕ: Добавлен экспоненциальный backoff при поиске ID устройства в PortAudio
        (особенно полезно для Bluetooth устройств, которые могут появиться с задержкой)
        
        Args:
            max_retries: Максимальное количество попыток поиска ID (по умолчанию 3)
            base_delay: Базовая задержка для экспоненциального backoff (по умолчанию 0.3с)
        
        Returns:
            tuple: (device_name, device_id) или (None, None) если не найдено
        """
        try:
            import subprocess
            import json
            
            # Получаем имя устройства через macOS API
            result = subprocess.run(
                ['SwitchAudioSource', '-c', '-t', 'input', '-f', 'json'],
                capture_output=True,
                text=True,
                timeout=2
            )
            
            if result.returncode == 0:
                device_info = json.loads(result.stdout.strip())
                device_name = device_info.get('name', '')
                
                if device_name:
                    # ✅ УЛУЧШЕНИЕ: Ищем ID устройства по имени в PortAudio с экспоненциальным backoff
                    # Это гарантирует, что мы всегда найдём правильный ID, даже если он изменился
                    # или устройство только что подключилось
                    
                    def _find_id_once() -> Optional[int]:
                        """Одна попытка поиска ID устройства"""
                        try:
                            all_devices = sd.query_devices()
                            for idx, dev in enumerate(all_devices):
                                if dev.get('max_input_channels', 0) > 0:
                                    if dev.get('name', '') == device_name:
                                        return idx
                            return None
                        except Exception as e:
                            logger.debug(f"⚠️ [MONITOR] Ошибка поиска ID: {e}")
                            return None
                    
                    # Попытки с экспоненциальным backoff
                    start_time = time.time()
                    for attempt in range(max_retries):
                        logger.debug(f"🔍 [MONITOR] Попытка {attempt + 1}/{max_retries} поиска ID для \"{device_name}\"")
                        
                        device_id = _find_id_once()
                        if device_id is not None:
                            elapsed = time.time() - start_time
                            if attempt > 0:
                                logger.info(f"✅ [MONITOR] Найдено на попытке {attempt + 1}: \"{device_name}\" → ID {device_id} (время поиска: {elapsed:.2f}с)")
                            else:
                                logger.debug(f"✅ [MONITOR] Найдено устройство через macOS API: \"{device_name}\" → ID {device_id} (время поиска: {elapsed:.2f}с)")
                            return device_name, device_id
                        
                        # Если не последняя попытка - ждём с экспоненциальной задержкой
                        if attempt < max_retries - 1:
                            delay = base_delay * (2 ** attempt)  # 0.3, 0.6, 1.2
                            logger.debug(f"⏳ [MONITOR] Задержка перед следующей попыткой: {delay:.2f}с (экспоненциальный backoff)")
                            time.sleep(delay)
                    
                    elapsed = time.time() - start_time
                    logger.warning(f"⚠️ [MONITOR] Устройство \"{device_name}\" не найдено в PortAudio после {max_retries} попыток (время поиска: {elapsed:.2f}с)")
                    
                    # ✅ СИСТЕМНОЕ РЕШЕНИЕ: Для BT устройств пропускаем обновление кэша PortAudio
                    # BT устройства часто не видны в PortAudio сразу, и обновление кэша не поможет
                    # Это экономит время и предотвращает множественные попытки поиска
                    is_bluetooth = False
                    if device_name:
                        lowered = device_name.lower()
                        is_bluetooth = any(keyword in lowered for keyword in ("bluetooth", "airpod", "airpods", "beats", "headset", "earbud"))
                    
                    if is_bluetooth:
                        logger.info(f"💡 [MONITOR] BT устройство '{device_name}' не найдено в PortAudio - это нормально, используем device=None (системный дефолт)")
                        logger.info(f"💡 [MONITOR] Пропускаем обновление кэша PortAudio для BT устройства (не поможет)")
                        return device_name, None
                    
                    # ✅ ШАГ 1.3: Обновляем кэш PortAudio при обнаружении нового устройства через macOS API (только для НЕ-BT устройств)
                    # macOS API видит устройство, но PortAudio его не видит - нужно обновить кэш
                    logger.info("🔄 [MONITOR] ШАГ 1.3: Обновление кэша PortAudio при обнаружении нового устройства через macOS API...")
                    try:
                        # Безопасное обновление кэша PortAudio
                        if hasattr(sd.query_devices, 'clear_cache'):
                            sd.query_devices.clear_cache()
                            logger.debug("✅ [MONITOR] Кэш PortAudio очищен через clear_cache()")
                        else:
                            # ✅ АЛЬТЕРНАТИВНЫЙ СПОСОБ: Если clear_cache() недоступен, делаем несколько запросов с задержкой
                            # Это принудительно обновит список устройств в PortAudio
                            logger.debug("⚠️ [MONITOR] Метод clear_cache() недоступен, используем альтернативный способ обновления кэша...")
                            for retry in range(3):
                                time.sleep(0.2 * (retry + 1))  # Увеличиваем задержку с каждой попыткой
                                logger.debug(f"🔍 [MONITOR] Попытка {retry + 1}/3 обновления кэша через повторный запрос...")
                                # Принудительно запрашиваем список устройств заново
                                _ = sd.query_devices()
                        
                        # Пробуем найти устройство еще раз после обновления кэша
                        logger.debug(f"🔍 [MONITOR] Повторный поиск \"{device_name}\" после обновления кэша...")
                        device_id = _find_id_once()
                        if device_id is not None:
                            logger.info(f"✅ [MONITOR] Устройство найдено после обновления кэша: \"{device_name}\" → ID {device_id}")
                            return device_name, device_id
                    except Exception as e:
                        logger.warning(f"⚠️ [MONITOR] Ошибка обновления кэша PortAudio: {e}")
            
        except FileNotFoundError:
            # SwitchAudioSource не установлен - это нормально
            logger.debug("⚠️ [MONITOR] SwitchAudioSource не найден, используем PortAudio")
        except Exception as e:
            logger.debug(f"⚠️ [MONITOR] Ошибка получения через macOS API: {e}")
        
        return None, None
    
    def get_current_device(self) -> Optional[Any]:
        """Получение текущего устройства ID (thread-safe, для обратной совместимости)"""
        with self._lock:
            return self.current_input_device_id
    
    def get_current_device_name(self) -> Optional[str]:
        """Получение текущего устройства по имени (thread-safe)"""
        with self._lock:
            return self.current_input_device_name
    
    def is_monitoring(self) -> bool:
        """Проверка, запущен ли мониторинг"""
        return (self._monitor_thread is not None and 
                self._monitor_thread.is_alive() and 
                not self._stop_event.is_set())
