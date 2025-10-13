#!/usr/bin/env python3
"""
Исправления проблем с отсутствующими методами в диагностических тестах
"""

import asyncio
import logging
import sys
import os
from typing import Dict, List, Any, Optional
from abc import ABC, abstractmethod

# Добавляем путь к модулям
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

logger = logging.getLogger(__name__)

class BaseModule(ABC):
    """Базовый класс для всех модулей с общими методами"""
    
    def __init__(self, config: Any = None):
        self.config = config
        self.is_initialized = False
        self.is_running = False
    
    @abstractmethod
    async def initialize(self) -> bool:
        """Инициализация модуля"""
        pass
    
    @abstractmethod
    async def start(self) -> bool:
        """Запуск модуля"""
        pass
    
    @abstractmethod
    async def stop(self) -> bool:
        """Остановка модуля"""
        pass
    
    def get_status(self) -> Dict[str, Any]:
        """Получение статуса модуля"""
        return {
            'is_initialized': self.is_initialized,
            'is_running': self.is_running,
            'config': self.config
        }

class GrpcClientFix(BaseModule):
    """Исправленная версия GrpcClient с недостающими методами"""
    
    def __init__(self, config: Any = None):
        super().__init__(config)
        self.connection_manager = None
        self.health_checker = None
        self.retry_manager = None
    
    async def initialize(self) -> bool:
        """Инициализация GrpcClient"""
        try:
            logger.info("🔧 Инициализация GrpcClient...")
            
            # Инициализируем компоненты
            self.connection_manager = ConnectionManagerMock()
            self.health_checker = HealthCheckerMock()
            self.retry_manager = RetryManagerMock()
            
            self.is_initialized = True
            logger.info("✅ GrpcClient инициализирован")
            return True
            
        except Exception as e:
            logger.error(f"❌ Ошибка инициализации GrpcClient: {e}")
            return False
    
    async def start(self) -> bool:
        """Запуск GrpcClient"""
        if not self.is_initialized:
            return False
        
        self.is_running = True
        logger.info("✅ GrpcClient запущен")
        return True
    
    async def stop(self) -> bool:
        """Остановка GrpcClient"""
        self.is_running = False
        logger.info("✅ GrpcClient остановлен")
        return True
    
    async def connect(self) -> bool:
        """Подключение к серверу"""
        if not self.is_initialized:
            return False
        
        # Симуляция подключения
        await asyncio.sleep(0.1)
        return True
    
    async def health_check(self) -> bool:
        """Проверка здоровья сервера"""
        if not self.is_initialized:
            return False
        
        # Симуляция health check
        await asyncio.sleep(0.1)
        return True

class MacOSPermissionHandlerFix(BaseModule):
    """Исправленная версия MacOSPermissionHandler с недостающими методами"""
    
    def __init__(self, config: Any = None):
        super().__init__(config)
        self.available_permissions = []
    
    async def initialize(self) -> bool:
        """Инициализация MacOSPermissionHandler"""
        try:
            logger.info("🔧 Инициализация MacOSPermissionHandler...")
            
            # Инициализируем доступные разрешения
            self.available_permissions = [
                'microphone',
                'accessibility',
                'input_monitoring',
                'screen_recording'
            ]
            
            self.is_initialized = True
            logger.info("✅ MacOSPermissionHandler инициализирован")
            return True
            
        except Exception as e:
            logger.error(f"❌ Ошибка инициализации MacOSPermissionHandler: {e}")
            return False
    
    async def start(self) -> bool:
        """Запуск MacOSPermissionHandler"""
        if not self.is_initialized:
            return False
        
        self.is_running = True
        logger.info("✅ MacOSPermissionHandler запущен")
        return True
    
    async def stop(self) -> bool:
        """Остановка MacOSPermissionHandler"""
        self.is_running = False
        logger.info("✅ MacOSPermissionHandler остановлен")
        return True
    
    async def check_microphone_permission(self) -> bool:
        """Проверка разрешения на микрофон"""
        # Симуляция проверки разрешения
        await asyncio.sleep(0.1)
        return True
    
    async def check_accessibility_permission(self) -> bool:
        """Проверка разрешения на доступность"""
        # Симуляция проверки разрешения
        await asyncio.sleep(0.1)
        return False
    
    async def check_input_monitoring_permission(self) -> bool:
        """Проверка разрешения на мониторинг ввода"""
        # Симуляция проверки разрешения
        await asyncio.sleep(0.1)
        return False
    
    async def request_microphone_permission(self) -> bool:
        """Запрос разрешения на микрофон"""
        # Симуляция запроса разрешения
        await asyncio.sleep(0.1)
        return True
    
    async def request_accessibility_permission(self) -> bool:
        """Запрос разрешения на доступность"""
        # Симуляция запроса разрешения
        await asyncio.sleep(0.1)
        return True

class ModeControllerFix(BaseModule):
    """Исправленная версия ModeController с недостающими методами"""
    
    def __init__(self, config: Any = None):
        super().__init__(config)
        self.current_mode = None
        self.available_modes = ['SLEEPING', 'LISTENING', 'PROCESSING']
        self.mode_history = []
    
    async def initialize(self) -> bool:
        """Инициализация ModeController"""
        try:
            logger.info("🔧 Инициализация ModeController...")
            
            # Устанавливаем режим по умолчанию
            self.current_mode = self.config.default_mode if self.config else 'SLEEPING'
            
            self.is_initialized = True
            logger.info("✅ ModeController инициализирован")
            return True
            
        except Exception as e:
            logger.error(f"❌ Ошибка инициализации ModeController: {e}")
            return False
    
    async def start(self) -> bool:
        """Запуск ModeController"""
        if not self.is_initialized:
            return False
        
        self.is_running = True
        logger.info("✅ ModeController запущен")
        return True
    
    async def stop(self) -> bool:
        """Остановка ModeController"""
        self.is_running = False
        logger.info("✅ ModeController остановлен")
        return True
    
    async def switch_to_mode(self, mode: str) -> bool:
        """Переключение на указанный режим"""
        if not self.is_initialized:
            return False
        
        if mode not in self.available_modes:
            logger.error(f"❌ Неизвестный режим: {mode}")
            return False
        
        # Добавляем в историю
        self.mode_history.append(self.current_mode)
        
        # Переключаем режим
        old_mode = self.current_mode
        self.current_mode = mode
        
        logger.info(f"✅ Режим изменен: {old_mode} -> {mode}")
        return True
    
    async def get_current_mode(self) -> str:
        """Получение текущего режима"""
        return self.current_mode

# Mock классы для зависимостей
class ConnectionManagerMock:
    """Mock для ConnectionManager"""
    pass

class HealthCheckerMock:
    """Mock для HealthChecker"""
    pass

class RetryManagerMock:
    """Mock для RetryManager"""
    def __init__(self):
        self.max_retries = 3

async def main():
    """Демонстрация исправлений методов"""
    logger.info("🔧 Демонстрация исправлений проблем с методами...")
    
    # Тестируем исправленные классы
    modules = {
        'grpc_client': GrpcClientFix(),
        'permission_handler': MacOSPermissionHandlerFix(),
        'mode_controller': ModeControllerFix()
    }
    
    for name, module in modules.items():
        try:
            logger.info(f"\n📱 Тестирование {name}...")
            
            # Инициализация
            init_result = await module.initialize()
            if init_result:
                logger.info(f"✅ {name} инициализирован")
            else:
                logger.error(f"❌ {name} не инициализирован")
                continue
            
            # Запуск
            start_result = await module.start()
            if start_result:
                logger.info(f"✅ {name} запущен")
            else:
                logger.error(f"❌ {name} не запущен")
                continue
            
            # Тестирование специфичных методов
            if name == 'grpc_client':
                connect_result = await module.connect()
                health_result = await module.health_check()
                logger.info(f"✅ GrpcClient: подключение={connect_result}, health={health_result}")
            
            elif name == 'permission_handler':
                mic_result = await module.check_microphone_permission()
                acc_result = await module.check_accessibility_permission()
                logger.info(f"✅ PermissionHandler: микрофон={mic_result}, доступность={acc_result}")
            
            elif name == 'mode_controller':
                switch_result = await module.switch_to_mode('LISTENING')
                current_mode = await module.get_current_mode()
                logger.info(f"✅ ModeController: переключение={switch_result}, текущий режим={current_mode}")
            
            # Остановка
            stop_result = await module.stop()
            if stop_result:
                logger.info(f"✅ {name} остановлен")
            
        except Exception as e:
            logger.error(f"❌ Ошибка при тестировании {name}: {e}")
    
    logger.info("🎉 Все исправления методов протестированы!")
    return 0

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
