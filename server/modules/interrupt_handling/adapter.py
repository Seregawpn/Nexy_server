"""
Адаптер для InterruptManager - временный адаптер для использования через ModuleCoordinator
"""

import logging
from typing import Dict, Any, AsyncIterator, Union

from integrations.core.universal_module_interface import UniversalModuleInterface
from integrations.core.module_status import ModuleStatus, ModuleState

from modules.interrupt_handling.core.interrupt_manager import InterruptManager

logger = logging.getLogger(__name__)


class InterruptHandlingAdapter(UniversalModuleInterface):
    """
    Адаптер для InterruptManager
    
    Временный адаптер для использования существующего InterruptManager
    через ModuleCoordinator до полной миграции на UniversalModuleInterface.
    
    Примечание: InterruptManager уже наследует UniversalModuleInterface,
    но использует старый интерфейс. Этот адаптер оборачивает его для
    использования через новый ModuleCoordinator.
    """
    
    def __init__(self):
        """Инициализация адаптера"""
        super().__init__(name="interrupt_handling")
        self._manager: InterruptManager = None
        self._config: Dict[str, Any] = {}
        self._status = ModuleStatus(state=ModuleState.INIT)
    
    async def initialize(self, config: dict) -> None:
        """
        Инициализация адаптера
        
        Args:
            config: Конфигурация модуля (из unified_config)
        
        Raises:
            Exception: Если инициализация не удалась
        """
        try:
            self._status = ModuleStatus(state=ModuleState.INIT, health="degraded")
            logger.info(f"Инициализация адаптера {self.name}...")
            
            self._config = config
            
            # Создаем менеджер
            from modules.interrupt_handling.config import InterruptHandlingConfig
            interrupt_config = InterruptHandlingConfig()
            self._manager = InterruptManager(interrupt_config)
            
            # Инициализируем менеджер (используем старый метод)
            if await self._manager.initialize():
                self._status = ModuleStatus(state=ModuleState.READY, health="ok")
                logger.info(f"✅ Адаптер {self.name} инициализирован")
            else:
                raise Exception("Не удалось инициализировать InterruptManager")
                
        except Exception as e:
            self._status = ModuleStatus(
                state=ModuleState.ERROR,
                health="down",
                last_error=str(e)
            )
            logger.error(f"❌ Ошибка инициализации адаптера {self.name}: {e}")
            raise
    
    async def process(self, request: Dict[str, Any]) -> Union[Dict[str, Any], AsyncIterator[Dict[str, Any]]]:
        """
        Обработка запроса
        
        Args:
            request: Запрос на обработку прерывания
                - action: str - действие (interrupt_session, check_interrupt, clear_interrupt)
                - session_id: str - идентификатор сессии
                - hardware_id: str (опционально) - идентификатор устройства
        
        Returns:
            Результат обработки
        """
        try:
            self._status = ModuleStatus(state=ModuleState.PROCESSING, health="ok")
            
            action = request.get("action", "check_interrupt")
            session_id = request.get("session_id")
            
            result = {}
            
            if action == "interrupt_session":
                if not session_id:
                    raise ValueError("session_id не указан")
                # Прерываем сессию
                await self._manager.interrupt_session(session_id)
                result = {"success": True}
            elif action == "check_interrupt":
                if not session_id:
                    raise ValueError("session_id не указан")
                # Проверяем прерывание
                is_interrupted = await self._manager.is_session_interrupted(session_id)
                result = {"interrupted": is_interrupted}
            elif action == "clear_interrupt":
                # Очищаем глобальное прерывание
                await self._manager.clear_global_interrupt()
                result = {"success": True}
            else:
                raise ValueError(f"Неизвестное действие: {action}")
            
            return result
                
        except Exception as e:
            self._status = ModuleStatus(
                state=ModuleState.ERROR,
                health="down",
                last_error=str(e)
            )
            logger.error(f"❌ Ошибка обработки в адаптере {self.name}: {e}")
            raise
        finally:
            # Возвращаем статус в READY после обработки
            if self._status.state == ModuleState.PROCESSING:
                self._status = ModuleStatus(state=ModuleState.READY, health="ok")
    
    async def cleanup(self) -> None:
        """
        Очистка ресурсов адаптера
        """
        try:
            logger.info(f"Очистка адаптера {self.name}...")
            
            if self._manager and hasattr(self._manager, 'cleanup'):
                await self._manager.cleanup()
            
            self._manager = None
            self._config = {}
            self._status = ModuleStatus(state=ModuleState.STOPPED, health="down")
            
            logger.info(f"✅ Адаптер {self.name} очищен")
            
        except Exception as e:
            logger.error(f"❌ Ошибка очистки адаптера {self.name}: {e}")
            self._status = ModuleStatus(
                state=ModuleState.ERROR,
                health="down",
                last_error=str(e)
            )
    
    def status(self) -> ModuleStatus:
        """
        Получение статуса адаптера
        
        Returns:
            ModuleStatus с текущим состоянием
        """
        return self._status
    
    def get_manager(self) -> InterruptManager:
        """
        Получение внутреннего менеджера (для совместимости)
        
        Returns:
            Экземпляр InterruptManager
        """
        return self._manager

