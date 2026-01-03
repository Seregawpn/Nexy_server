"""
ModuleCoordinator - координатор модулей
Регистрирует модули по конфигурации и управляет их жизненным циклом
"""

import logging
from typing import Dict, Any, Optional, List
from datetime import datetime

from integrations.core.universal_module_interface import UniversalModuleInterface
from integrations.core.module_status import ModuleStatus, ModuleState

logger = logging.getLogger(__name__)


class ModuleCoordinator:
    """
    Координатор модулей
    
    Управляет жизненным циклом модулей: регистрация, инициализация,
    получение по capability, очистка.
    
    Все модули регистрируются через координатор и доступны только через него.
    Прямые вызовы между модулями запрещены.
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Инициализация координатора
        
        Args:
            config: Конфигурация координатора (из unified_config)
        """
        self.config = config or {}
        self._modules: Dict[str, UniversalModuleInterface] = {}
        self._capabilities: Dict[str, str] = {}  # capability -> module_name
        self._initialized = False
        # Опциональные модули - при ошибке инициализации не падаем
        self._optional_modules = {'audio_generation', 'text_filtering', 'interrupt_handling'}
        # Неудачно инициализированные модули (для отслеживания)
        self._failed_modules: Dict[str, str] = {}  # capability -> error_message
        
        logger.info("ModuleCoordinator создан")
    
    async def register(
        self,
        capability: str,
        module: UniversalModuleInterface,
        module_config: Dict[str, Any],
        optional: bool = False
    ) -> bool:
        """
        Регистрация модуля по capability
        
        Args:
            capability: Способность модуля (например, "text_processing", "audio_generation")
            module: Экземпляр модуля, реализующий UniversalModuleInterface
            module_config: Конфигурация модуля (из unified_config)
            optional: Если True, ошибка инициализации не приведет к исключению
        
        Returns:
            True если модуль успешно зарегистрирован, False если инициализация не удалась (для optional)
        
        Raises:
            ValueError: Если capability уже зарегистрирован
            Exception: Если инициализация модуля не удалась и модуль не опциональный
        """
        if capability in self._capabilities:
            raise ValueError(f"Capability '{capability}' уже зарегистрирован")
        
        # Проверяем, является ли модуль опциональным
        is_optional = optional or capability in self._optional_modules
        
        logger.info(f"Регистрация модуля '{module.name}' с capability '{capability}' (optional={is_optional})")
        
        try:
            # Инициализируем модуль
            await module.initialize(module_config)
            
            # Регистрируем модуль
            self._modules[module.name] = module
            self._capabilities[capability] = module.name
            
            logger.info(f"✅ Модуль '{module.name}' зарегистрирован с capability '{capability}'")
            return True
            
        except Exception as e:
            error_msg = str(e)
            logger.error(f"❌ Ошибка регистрации модуля '{module.name}': {error_msg}")
            
            if is_optional:
                # Для опциональных модулей логируем предупреждение и продолжаем работу
                logger.warning(
                    f"⚠️ Модуль '{capability}' не инициализирован (опциональный), "
                    f"сервер продолжит работу без него. Ошибка: {error_msg}",
                    extra={'scope': 'module', 'decision': 'degrade', 'ctx': {'capability': capability, 'error': error_msg}}
                )
                self._failed_modules[capability] = error_msg
                return False
            else:
                # Для критических модулей пробрасываем исключение
                raise
    
    def get(self, capability: str) -> UniversalModuleInterface:
        """
        Получение модуля по capability
        
        Args:
            capability: Способность модуля
            
        Returns:
            Экземпляр модуля
            
        Raises:
            KeyError: Если capability не зарегистрирован
        """
        if capability not in self._capabilities:
            raise KeyError(f"Capability '{capability}' не зарегистрирован")
        
        module_name = self._capabilities[capability]
        return self._modules[module_name]
    
    def has(self, capability: str) -> bool:
        """
        Проверка наличия capability
        
        Args:
            capability: Способность модуля
            
        Returns:
            True если capability зарегистрирован, False иначе
        """
        return capability in self._capabilities
    
    def list_capabilities(self) -> List[str]:
        """
        Получение списка всех зарегистрированных capabilities
        
        Returns:
            Список capabilities
        """
        return list(self._capabilities.keys())
    
    def list_modules(self) -> List[str]:
        """
        Получение списка всех зарегистрированных модулей
        
        Returns:
            Список имен модулей
        """
        return list(self._modules.keys())
    
    async def initialize_all(self) -> None:
        """
        Инициализация всех модулей (если требуется)
        
        Модули уже инициализируются при регистрации, но этот метод
        можно использовать для дополнительной проверки готовности.
        """
        if self._initialized:
            logger.debug("Координатор уже инициализирован")
            return
        
        logger.info("Инициализация всех модулей...")
        
        for module_name, module in self._modules.items():
            status = module.status()
            if not status.is_ready():
                logger.warning(f"Модуль '{module_name}' не готов: {status.state.value}")
        
        self._initialized = True
        logger.info(f"✅ Координатор инициализирован: {len(self._modules)} модулей")
    
    async def cleanup_all(self) -> None:
        """
        Очистка всех модулей
        
        Вызывается при остановке сервера.
        """
        logger.info("Очистка всех модулей...")
        
        for module_name, module in self._modules.items():
            try:
                await module.cleanup()
                logger.debug(f"✅ Модуль '{module_name}' очищен")
            except Exception as e:
                logger.error(f"❌ Ошибка очистки модуля '{module_name}': {e}")
        
        self._modules.clear()
        self._capabilities.clear()
        self._initialized = False
        
        logger.info("✅ Все модули очищены")
    
    def get_status(self) -> Dict[str, Any]:
        """
        Получение статуса координатора
        
        Returns:
            Словарь со статусом координатора и всех модулей
        """
        modules_status = {}
        for module_name, module in self._modules.items():
            status = module.status()
            modules_status[module_name] = status.to_dict() if hasattr(status, 'to_dict') else {
                'state': status.state.value if hasattr(status.state, 'value') else str(status.state),
                'health': status.health if hasattr(status, 'health') else 'unknown'
            }
        
        capabilities_map = {}
        for capability, module_name in self._capabilities.items():
            capabilities_map[capability] = module_name
        
        return {
            "initialized": self._initialized,
            "modules_count": len(self._modules),
            "capabilities_count": len(self._capabilities),
            "modules": modules_status,
            "capabilities": capabilities_map
        }
    
    def get_module_status(self, capability: str) -> Optional[ModuleStatus]:
        """
        Получение статуса модуля по capability
        
        Args:
            capability: Способность модуля
            
        Returns:
            ModuleStatus или None если capability не найден
        """
        try:
            module = self.get(capability)
            return module.status()
        except KeyError:
            return None

