"""
Основная политика автопереключения аудио устройств
"""

import time
import threading
import logging
from typing import Dict, Any, Optional, List
from .core import AudioCore
from .config import get_config

logger = logging.getLogger(__name__)

class AutoSwitch:
    """Основной класс автопереключения аудио устройств"""
    
    def __init__(self, config: Dict[str, Any] = None, logger_func=None):
        self.config = config or get_config()
        self.core = AudioCore(self.config)
        self.logger_func = logger_func or logger.info
        
        # Состояние
        self.running = False
        self.thread = None
        self.last_snapshot = None
        self.last_change_time = 0
        self.fail_count = 0
        self.quarantine_until = 0
        self.current_device = None
        
        # Блокировка для thread-safe операций
        self.lock = threading.Lock()
        
        self.logger_func("🚀 AutoSwitch инициализирован")
    
    def start(self):
        """Запускает фоновый поток автопереключения"""
        with self.lock:
            if self.running:
                self.logger_func("⚠️  AutoSwitch уже запущен")
                return
            
            self.running = True
            self.thread = threading.Thread(target=self._loop, daemon=True)
            self.thread.start()
            self.logger_func("✅ AutoSwitch запущен")
    
    def stop(self):
        """Останавливает фоновый поток"""
        with self.lock:
            if not self.running:
                self.logger_func("⚠️  AutoSwitch уже остановлен")
                return
            
            self.running = False
            if self.thread:
                self.thread.join(timeout=2)
            self.logger_func("🛑 AutoSwitch остановлен")
    
    def _loop(self):
        """Основной цикл автопереключения"""
        self.logger_func("🔄 Запуск основного цикла автопереключения")
        
        while self.running:
            try:
                # Получаем снимок текущего состояния
                snapshot = self.core.get_device_snapshot()
                
                # Проверяем изменения
                if self._changed(self.last_snapshot, snapshot):
                    self.logger_func("🔄 Обнаружены изменения в устройствах")
                    self.last_change_time = time.time()
                    self.last_snapshot = snapshot
                
                # Применяем политику с дебаунсом
                if (self.last_change_time > 0 and 
                    time.time() - self.last_change_time >= self.config['debounce_ms'] / 1000):
                    
                    self._apply_policy(snapshot)
                    self.last_change_time = 0  # Сбрасываем после применения
                
                # Ждем до следующего опроса
                time.sleep(self.config['poll_interval'])
                
            except Exception as e:
                logger.error(f"❌ Ошибка в основном цикле: {e}")
                time.sleep(self.config['poll_interval'])
    
    def _changed(self, old_snapshot: Optional[Dict], new_snapshot: Dict) -> bool:
        """Проверяет, изменилось ли состояние устройств"""
        if old_snapshot is None:
            return True
        
        # Сравниваем списки устройств
        if (set(old_snapshot.get('inputs', [])) != set(new_snapshot.get('inputs', [])) or
            set(old_snapshot.get('outputs', [])) != set(new_snapshot.get('outputs', []))):
            return True
        
        # Сравниваем текущие устройства
        if (old_snapshot.get('current_input') != new_snapshot.get('current_input') or
            old_snapshot.get('current_output') != new_snapshot.get('current_output')):
            return True
        
        return False
    
    def _choose_headset(self, snapshot: Dict) -> Optional[str]:
        """Выбирает гарнитуру по приоритету"""
        inputs = snapshot.get('inputs', [])
        outputs = snapshot.get('outputs', [])
        
        # Ищем AirPods
        airpods = self.core.find_by_patterns(inputs, ['airpods'])
        if airpods and airpods in outputs:
            self.logger_func(f"🎧 Найдены AirPods: {airpods}")
            return airpods
        
        # Ищем другие гарнитуры
        headsets = self.core.find_by_patterns(inputs, ['headset'])
        for headset in headsets:
            if headset in outputs:
                self.logger_func(f"🎧 Найдена гарнитура: {headset}")
                return headset
        
        return None
    
    def _choose_builtin(self, snapshot: Dict) -> Optional[str]:
        """Выбирает встроенное устройство"""
        inputs = snapshot.get('inputs', [])
        outputs = snapshot.get('outputs', [])
        
        # Ищем встроенный микрофон
        builtin_input = self.core.find_by_patterns(inputs, ['builtin_input'])
        if builtin_input:
            self.logger_func(f"💻 Найден встроенный микрофон: {builtin_input}")
            return builtin_input
        
        return None
    
    def _activate_coupled(self, device_name: str) -> bool:
        """Активирует устройство сцепкой с проверкой здоровья"""
        retry_delays = self.config['retry_delays']
        
        for attempt in range(self.config['max_retries']):
            if attempt > 0:
                delay = retry_delays[min(attempt - 1, len(retry_delays) - 1)]
                self.logger_func(f"🔄 Попытка {attempt + 1}/{self.config['max_retries']}, задержка {delay}s")
                time.sleep(delay)
            
            # Пытаемся установить сцепку
            if self.core.set_inout(device_name):
                # Небольшая задержка для стабилизации
                time.sleep(0.2)
                
                # Проверяем здоровье
                if self.core.is_device_working(device_name):
                    self.logger_func(f"✅ Устройство {device_name} успешно активировано")
                    self.fail_count = 0  # Сбрасываем счетчик провалов
                    self.current_device = device_name
                    return True
                else:
                    self.logger_func(f"⚠️  Устройство {device_name} не работает (тишина)")
            else:
                self.logger_func(f"❌ Не удалось установить сцепку на {device_name}")
        
        return False
    
    def _fallback_builtin(self, snapshot: Dict) -> bool:
        """Переключается на встроенное устройство"""
        inputs = snapshot.get('inputs', [])
        outputs = snapshot.get('outputs', [])
        
        # Ищем встроенный микрофон
        builtin_input = self.core.find_by_patterns(inputs, ['builtin_input'])
        if not builtin_input:
            self.logger_func("❌ Встроенный микрофон не найден")
            return False
        
        # Ищем встроенные динамики
        builtin_output = self.core.find_by_patterns(outputs, ['builtin_output'])
        if not builtin_output:
            self.logger_func("❌ Встроенные динамики не найдены")
            return False
        
        self.logger_func(f"🔄 Fallback на встроенные устройства: {builtin_input} + {builtin_output}")
        
        # Устанавливаем input
        if not self.core.set_input(builtin_input):
            return False
        
        time.sleep(0.1)
        
        # Устанавливаем output
        if not self.core.set_output(builtin_output):
            return False
        
        # Проверяем здоровье микрофона
        if self.core.is_device_working(builtin_input):
            self.logger_func(f"✅ Встроенные устройства активированы: {builtin_input} + {builtin_output}")
            self.current_device = f"{builtin_input}+{builtin_output}"
            return True
        else:
            self.logger_func(f"❌ Встроенный микрофон не работает: {builtin_input}")
            return False
    
    def _apply_policy(self, snapshot: Dict):
        """Применяет политику автопереключения"""
        current_time = time.time()
        
        # Проверяем карантин
        if current_time < self.quarantine_until:
            remaining = int(self.quarantine_until - current_time)
            self.logger_func(f"🚫 В карантине, осталось {remaining}s")
            self._fallback_builtin(snapshot)
            return
        
        # Ищем гарнитуру
        headset = self._choose_headset(snapshot)
        if headset:
            self.logger_func(f"🎧 Пытаемся активировать гарнитуру: {headset}")
            
            if self._activate_coupled(headset):
                self.logger_func(f"✅ Гарнитура {headset} активирована")
                return
            else:
                # Увеличиваем счетчик провалов
                self.fail_count += 1
                self.logger_func(f"❌ Провал гарнитуры {headset}, счетчик: {self.fail_count}")
                
                # Проверяем, нужно ли включить карантин
                if self.fail_count >= self.config['fails_to_quarantine']:
                    self.quarantine_until = current_time + self.config['quarantine_duration']
                    self.logger_func(f"🚫 Включаем карантин на {self.config['quarantine_duration']}s")
        
        # Fallback на встроенное устройство
        self.logger_func("🔄 Переключение на встроенное устройство")
        if self._fallback_builtin(snapshot):
            self.logger_func("✅ Встроенное устройство активировано")
        else:
            self.logger_func("❌ Не удалось активировать встроенное устройство")
    
    def get_status(self) -> Dict[str, Any]:
        """Получает текущий статус"""
        with self.lock:
            return {
                'running': self.running,
                'current_device': self.current_device,
                'fail_count': self.fail_count,
                'quarantine_until': self.quarantine_until,
                'in_quarantine': time.time() < self.quarantine_until,
                'last_snapshot': self.last_snapshot
            }
    
    def force_switch(self, device_name: str) -> bool:
        """Принудительно переключает на устройство"""
        self.logger_func(f"🔄 Принудительное переключение на: {device_name}")
        
        if self._activate_coupled(device_name):
            self.fail_count = 0
            self.quarantine_until = 0
            return True
        return False
    
    def reset_quarantine(self):
        """Сбрасывает карантин"""
        with self.lock:
            self.quarantine_until = 0
            self.fail_count = 0
            self.logger_func("🔄 Карантин сброшен")

"""

import time
import threading
import logging
from typing import Dict, Any, Optional, List
from .core import AudioCore
from .config import get_config

logger = logging.getLogger(__name__)

class AutoSwitch:
    """Основной класс автопереключения аудио устройств"""
    
    def __init__(self, config: Dict[str, Any] = None, logger_func=None):
        self.config = config or get_config()
        self.core = AudioCore(self.config)
        self.logger_func = logger_func or logger.info
        
        # Состояние
        self.running = False
        self.thread = None
        self.last_snapshot = None
        self.last_change_time = 0
        self.fail_count = 0
        self.quarantine_until = 0
        self.current_device = None
        
        # Блокировка для thread-safe операций
        self.lock = threading.Lock()
        
        self.logger_func("🚀 AutoSwitch инициализирован")
    
    def start(self):
        """Запускает фоновый поток автопереключения"""
        with self.lock:
            if self.running:
                self.logger_func("⚠️  AutoSwitch уже запущен")
                return
            
            self.running = True
            self.thread = threading.Thread(target=self._loop, daemon=True)
            self.thread.start()
            self.logger_func("✅ AutoSwitch запущен")
    
    def stop(self):
        """Останавливает фоновый поток"""
        with self.lock:
            if not self.running:
                self.logger_func("⚠️  AutoSwitch уже остановлен")
                return
            
            self.running = False
            if self.thread:
                self.thread.join(timeout=2)
            self.logger_func("🛑 AutoSwitch остановлен")
    
    def _loop(self):
        """Основной цикл автопереключения"""
        self.logger_func("🔄 Запуск основного цикла автопереключения")
        
        while self.running:
            try:
                # Получаем снимок текущего состояния
                snapshot = self.core.get_device_snapshot()
                
                # Проверяем изменения
                if self._changed(self.last_snapshot, snapshot):
                    self.logger_func("🔄 Обнаружены изменения в устройствах")
                    self.last_change_time = time.time()
                    self.last_snapshot = snapshot
                
                # Применяем политику с дебаунсом
                if (self.last_change_time > 0 and 
                    time.time() - self.last_change_time >= self.config['debounce_ms'] / 1000):
                    
                    self._apply_policy(snapshot)
                    self.last_change_time = 0  # Сбрасываем после применения
                
                # Ждем до следующего опроса
                time.sleep(self.config['poll_interval'])
                
            except Exception as e:
                logger.error(f"❌ Ошибка в основном цикле: {e}")
                time.sleep(self.config['poll_interval'])
    
    def _changed(self, old_snapshot: Optional[Dict], new_snapshot: Dict) -> bool:
        """Проверяет, изменилось ли состояние устройств"""
        if old_snapshot is None:
            return True
        
        # Сравниваем списки устройств
        if (set(old_snapshot.get('inputs', [])) != set(new_snapshot.get('inputs', [])) or
            set(old_snapshot.get('outputs', [])) != set(new_snapshot.get('outputs', []))):
            return True
        
        # Сравниваем текущие устройства
        if (old_snapshot.get('current_input') != new_snapshot.get('current_input') or
            old_snapshot.get('current_output') != new_snapshot.get('current_output')):
            return True
        
        return False
    
    def _choose_headset(self, snapshot: Dict) -> Optional[str]:
        """Выбирает гарнитуру по приоритету"""
        inputs = snapshot.get('inputs', [])
        outputs = snapshot.get('outputs', [])
        
        # Ищем AirPods
        airpods = self.core.find_by_patterns(inputs, ['airpods'])
        if airpods and airpods in outputs:
            self.logger_func(f"🎧 Найдены AirPods: {airpods}")
            return airpods
        
        # Ищем другие гарнитуры
        headsets = self.core.find_by_patterns(inputs, ['headset'])
        for headset in headsets:
            if headset in outputs:
                self.logger_func(f"🎧 Найдена гарнитура: {headset}")
                return headset
        
        return None
    
    def _choose_builtin(self, snapshot: Dict) -> Optional[str]:
        """Выбирает встроенное устройство"""
        inputs = snapshot.get('inputs', [])
        outputs = snapshot.get('outputs', [])
        
        # Ищем встроенный микрофон
        builtin_input = self.core.find_by_patterns(inputs, ['builtin_input'])
        if builtin_input:
            self.logger_func(f"💻 Найден встроенный микрофон: {builtin_input}")
            return builtin_input
        
        return None
    
    def _activate_coupled(self, device_name: str) -> bool:
        """Активирует устройство сцепкой с проверкой здоровья"""
        retry_delays = self.config['retry_delays']
        
        for attempt in range(self.config['max_retries']):
            if attempt > 0:
                delay = retry_delays[min(attempt - 1, len(retry_delays) - 1)]
                self.logger_func(f"🔄 Попытка {attempt + 1}/{self.config['max_retries']}, задержка {delay}s")
                time.sleep(delay)
            
            # Пытаемся установить сцепку
            if self.core.set_inout(device_name):
                # Небольшая задержка для стабилизации
                time.sleep(0.2)
                
                # Проверяем здоровье
                if self.core.is_device_working(device_name):
                    self.logger_func(f"✅ Устройство {device_name} успешно активировано")
                    self.fail_count = 0  # Сбрасываем счетчик провалов
                    self.current_device = device_name
                    return True
                else:
                    self.logger_func(f"⚠️  Устройство {device_name} не работает (тишина)")
            else:
                self.logger_func(f"❌ Не удалось установить сцепку на {device_name}")
        
        return False
    
    def _fallback_builtin(self, snapshot: Dict) -> bool:
        """Переключается на встроенное устройство"""
        inputs = snapshot.get('inputs', [])
        outputs = snapshot.get('outputs', [])
        
        # Ищем встроенный микрофон
        builtin_input = self.core.find_by_patterns(inputs, ['builtin_input'])
        if not builtin_input:
            self.logger_func("❌ Встроенный микрофон не найден")
            return False
        
        # Ищем встроенные динамики
        builtin_output = self.core.find_by_patterns(outputs, ['builtin_output'])
        if not builtin_output:
            self.logger_func("❌ Встроенные динамики не найдены")
            return False
        
        self.logger_func(f"🔄 Fallback на встроенные устройства: {builtin_input} + {builtin_output}")
        
        # Устанавливаем input
        if not self.core.set_input(builtin_input):
            return False
        
        time.sleep(0.1)
        
        # Устанавливаем output
        if not self.core.set_output(builtin_output):
            return False
        
        # Проверяем здоровье микрофона
        if self.core.is_device_working(builtin_input):
            self.logger_func(f"✅ Встроенные устройства активированы: {builtin_input} + {builtin_output}")
            self.current_device = f"{builtin_input}+{builtin_output}"
            return True
        else:
            self.logger_func(f"❌ Встроенный микрофон не работает: {builtin_input}")
            return False
    
    def _apply_policy(self, snapshot: Dict):
        """Применяет политику автопереключения"""
        current_time = time.time()
        
        # Проверяем карантин
        if current_time < self.quarantine_until:
            remaining = int(self.quarantine_until - current_time)
            self.logger_func(f"🚫 В карантине, осталось {remaining}s")
            self._fallback_builtin(snapshot)
            return
        
        # Ищем гарнитуру
        headset = self._choose_headset(snapshot)
        if headset:
            self.logger_func(f"🎧 Пытаемся активировать гарнитуру: {headset}")
            
            if self._activate_coupled(headset):
                self.logger_func(f"✅ Гарнитура {headset} активирована")
                return
            else:
                # Увеличиваем счетчик провалов
                self.fail_count += 1
                self.logger_func(f"❌ Провал гарнитуры {headset}, счетчик: {self.fail_count}")
                
                # Проверяем, нужно ли включить карантин
                if self.fail_count >= self.config['fails_to_quarantine']:
                    self.quarantine_until = current_time + self.config['quarantine_duration']
                    self.logger_func(f"🚫 Включаем карантин на {self.config['quarantine_duration']}s")
        
        # Fallback на встроенное устройство
        self.logger_func("🔄 Переключение на встроенное устройство")
        if self._fallback_builtin(snapshot):
            self.logger_func("✅ Встроенное устройство активировано")
        else:
            self.logger_func("❌ Не удалось активировать встроенное устройство")
    
    def get_status(self) -> Dict[str, Any]:
        """Получает текущий статус"""
        with self.lock:
            return {
                'running': self.running,
                'current_device': self.current_device,
                'fail_count': self.fail_count,
                'quarantine_until': self.quarantine_until,
                'in_quarantine': time.time() < self.quarantine_until,
                'last_snapshot': self.last_snapshot
            }
    
    def force_switch(self, device_name: str) -> bool:
        """Принудительно переключает на устройство"""
        self.logger_func(f"🔄 Принудительное переключение на: {device_name}")
        
        if self._activate_coupled(device_name):
            self.fail_count = 0
            self.quarantine_until = 0
            return True
        return False
    
    def reset_quarantine(self):
        """Сбрасывает карантин"""
        with self.lock:
            self.quarantine_until = 0
            self.fail_count = 0
            self.logger_func("🔄 Карантин сброшен")
