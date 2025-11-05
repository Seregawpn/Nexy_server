"""
Module Factory для динамического создания модулей
Реализует паттерн Factory для устранения прямых импортов в grpc_service_manager.py
"""

import logging
from typing import Dict, Optional
from integrations.core.universal_module_interface import UniversalModuleInterface

logger = logging.getLogger(__name__)


class ModuleFactory:
    """
    Фабрика для создания модулей без прямых импортов

    Использование:
        factory = ModuleFactory()
        module = factory.create('text_processing', config)
    """

    # Регистрация модулей через строковые пути
    _MODULE_REGISTRY: Dict[str, str] = {
        'text_processing': 'modules.text_processing.module:TextProcessingModule',
        'audio_generation': 'modules.audio_generation.adapter:AudioGenerationAdapter',
        'memory_management': 'modules.memory_management.adapter:MemoryManagementAdapter',
        'database': 'modules.database.adapter:DatabaseAdapter',
        'session_management': 'modules.session_management.adapter:SessionManagementAdapter',
        'interrupt_handling': 'modules.interrupt_handling.adapter:InterruptHandlingAdapter',
        'text_filtering': 'modules.text_filtering.adapter:TextFilteringAdapter',
    }

    @classmethod
    def create(cls, capability: str, config: Optional[Dict] = None) -> UniversalModuleInterface:
        """
        Создание модуля по имени capability

        Args:
            capability: Имя модуля (например, 'text_processing')
            config: Опциональная конфигурация модуля

        Returns:
            Экземпляр модуля, реализующий UniversalModuleInterface

        Raises:
            ValueError: Если модуль не найден в реестре
            ImportError: Если не удалось импортировать модуль
        """
        if capability not in cls._MODULE_REGISTRY:
            raise ValueError(f"Модуль '{capability}' не найден в реестре. "
                           f"Доступные модули: {list(cls._MODULE_REGISTRY.keys())}")

        module_path = cls._MODULE_REGISTRY[capability]

        try:
            # Динамический импорт: 'modules.text_processing.module:TextProcessingModule'
            module_file, class_name = module_path.split(':')

            # Импортируем модуль
            import importlib
            module = importlib.import_module(module_file)

            # Получаем класс
            module_class = getattr(module, class_name)

            # Создаём экземпляр
            instance = module_class()

            logger.info(f"✅ Модуль '{capability}' создан через фабрику: {class_name}")
            return instance

        except Exception as e:
            logger.error(f"❌ Ошибка создания модуля '{capability}': {e}")
            raise ImportError(f"Не удалось создать модуль '{capability}': {e}") from e

    @classmethod
    def register(cls, capability: str, module_path: str) -> None:
        """
        Регистрация нового модуля в фабрике

        Args:
            capability: Имя capability (например, 'my_module')
            module_path: Путь к модулю в формате 'package.module:ClassName'

        Example:
            ModuleFactory.register('my_module', 'modules.my_module.adapter:MyModuleAdapter')
        """
        cls._MODULE_REGISTRY[capability] = module_path
        logger.info(f"✅ Модуль '{capability}' зарегистрирован в фабрике: {module_path}")

    @classmethod
    def list_modules(cls) -> Dict[str, str]:
        """
        Получение списка всех зарегистрированных модулей

        Returns:
            Словарь {capability: module_path}
        """
        return cls._MODULE_REGISTRY.copy()
