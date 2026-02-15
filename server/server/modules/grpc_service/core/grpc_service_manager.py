"""
Новый GrpcServiceManager с использованием ModuleCoordinator
Реализует PR-2.1: миграция на координатор модулей
"""

import asyncio
import logging
import os
from typing import Dict, Any, Optional, AsyncGenerator
from datetime import datetime

from integrations.core.universal_module_interface import UniversalModuleInterface
from integrations.core.module_status import ModuleStatus, ModuleState
from integrations.service_integrations.module_coordinator import ModuleCoordinator
from integrations.service_integrations.grpc_service_integration import GrpcServiceIntegration
from integrations.workflow_integrations.streaming_workflow_integration import StreamingWorkflowIntegration
from integrations.workflow_integrations.memory_workflow_integration import MemoryWorkflowIntegration
from integrations.workflow_integrations.interrupt_workflow_integration import InterruptWorkflowIntegration

from config.unified_config import get_config
from integrations.core.module_factory import ModuleFactory

from modules.grpc_service.config import GrpcServiceConfig

logger = logging.getLogger(__name__)


class GrpcServiceManager(UniversalModuleInterface):
    """
    GrpcServiceManager с использованием ModuleCoordinator
    
    Использует новый подход:
    - ModuleCoordinator для управления модулями
    - Все модули регистрируются через координатор
    - Прямые импорты модулей убраны
    """
    
    def __init__(self, config: Optional[GrpcServiceConfig] = None):
        """
        Инициализация менеджера gRPC сервиса
        
        Args:
            config: Конфигурация gRPC сервиса
        """
        super().__init__(name="grpc_service")
        
        self.config = config or GrpcServiceConfig()
        self.unified_config = get_config()
        
        # ModuleCoordinator (новый подход)
        self.coordinator: Optional[ModuleCoordinator] = None
        self._legacy_modules: Dict[str, UniversalModuleInterface] = {}
        
        # Workflow интеграции
        self.streaming_workflow: Optional[StreamingWorkflowIntegration] = None
        self.memory_workflow: Optional[MemoryWorkflowIntegration] = None
        self.interrupt_workflow: Optional[InterruptWorkflowIntegration] = None
        
        # Service интеграции
        self.grpc_service_integration: Optional[GrpcServiceIntegration] = None
        
        # Статус
        self._status = ModuleStatus(state=ModuleState.INIT)
        self._use_coordinator = False  # Определяется при инициализации
        
        logger.info("gRPC Service Manager created")
    
    async def initialize(self, config: dict) -> None:
        """
        Инициализация менеджера gRPC сервиса
        
        Args:
            config: Конфигурация модуля (из unified_config)
        
        Raises:
            Exception: Если инициализация не удалась
        """
        try:
            self._status = ModuleStatus(state=ModuleState.INIT, health="degraded")
            logger.info("Инициализация gRPC Service Manager...")
            
            force_legacy_init = os.getenv('NEXY_FORCE_LEGACY_GRPC_INIT', 'false').lower() == 'true'
            feature_enabled = self.unified_config.is_feature_enabled('use_module_coordinator')
            kill_switch_active = self.unified_config.is_kill_switch_active('disable_module_coordinator')

            self._use_coordinator = not force_legacy_init

            if force_legacy_init:
                logger.warning(
                    "⚠️ Включен аварийный legacy init-path (NEXY_FORCE_LEGACY_GRPC_INIT=true). "
                    "Это режим экстренного отката."
                )
                await self._initialize_legacy()
            else:
                if not feature_enabled or kill_switch_active:
                    logger.warning(
                        "⚠️ Флаг/kill-switch coordinator отключен, но legacy-path не используется. "
                        "Для экстренного legacy rollback используйте NEXY_FORCE_LEGACY_GRPC_INIT=true."
                    )
                logger.info("✅ Используется ModuleCoordinator (каноничный путь)")
                await self._initialize_with_coordinator()
            
            self._status = ModuleStatus(state=ModuleState.READY, health="ok")
            logger.info("✅ gRPC Service Manager инициализирован")
            
        except Exception as e:
            self._status = ModuleStatus(
                state=ModuleState.ERROR,
                health="down",
                last_error=str(e)
            )
            logger.error(f"❌ Ошибка инициализации gRPC Service Manager: {e}")
            raise
    
    async def _initialize_with_coordinator(self) -> None:
        """Инициализация с использованием ModuleCoordinator (новый подход)"""
        logger.info("Инициализация с ModuleCoordinator...")
        
        # Создаем координатор
        self.coordinator = ModuleCoordinator(self.unified_config.__dict__)
        
        # Регистрируем модули через координатор
        await self._register_modules(self.coordinator.register)
        
        # Инициализируем координатор
        await self.coordinator.initialize_all()
        
        # Wiring: Inject DatabaseManager into MemoryManager
        try:
            if self.coordinator.has('memory_management') and self.coordinator.has('database'):
                memory_module = self.coordinator.get('memory_management')
                database_module = self.coordinator.get('database')
                
                # Check if database is ready (it's optional, so might have failed or be missing config)
                if database_module.status().is_ready():
                    logger.info("Wiring DatabaseManager to MemoryManager...")
                    # Adapters should implementation these methods
                    if hasattr(memory_module, 'set_database_manager') and hasattr(database_module, 'get_manager'):
                        memory_module.set_database_manager(database_module.get_manager())
                        logger.info("✅ DatabaseManager wired to MemoryManager")
                    else:
                        logger.warning("⚠️ MemoryManager or DatabaseManager missing required methods for wiring")
                else:
                    logger.warning(f"⚠️ Database module is not ready ({database_module.status().state}), skipping wiring")
        except Exception as e:
            logger.error(f"❌ Error wiring modules: {e}")
        
        # Создаем workflow интеграции (используют модули из координатора)
        await self._create_workflow_integrations()
        
        # Создаем service интеграции
        await self._create_service_integrations()
        
        # Инициализируем интеграции
        await self._initialize_integrations()
    
    async def _initialize_legacy(self) -> None:
        """Legacy инициализация (для отката)"""
        logger.warning("⚠️ Используется legacy подход - прямой импорт модулей")
        
        self._legacy_modules = {}

        async def legacy_register(capability: str, module: UniversalModuleInterface, module_config: Dict[str, Any]):
            await module.initialize(module_config)
            self._legacy_modules[capability] = module
            logger.info(f"✅ Legacy модуль '{capability}' инициализирован без координатора")

        await self._register_modules(legacy_register)

        await self._create_workflow_integrations()
        await self._create_service_integrations()
        await self._initialize_integrations()
    
    def _get_module_configs(self) -> Dict[str, Dict[str, Any]]:
        """Собирает конфигурации модулей из unified_config."""
        return {
            'text_processing': self.unified_config.get_module_config('text_processing'),
            'audio_generation': self.unified_config.get_module_config('audio'),
            'memory_management': self.unified_config.get_module_config('memory'),
            'database': self.unified_config.get_module_config('database'),
            'session_management': self.unified_config.get_module_config('session'),
            'interrupt_handling': self.unified_config.get_module_config('interrupt'),
            'text_filtering': {},
            'browser_use': self.unified_config.get_module_config('browser_use'),
        }

    def _module_capabilities(self) -> list:
        return [
            'text_processing',
            'audio_generation',
            'memory_management',
            'database',
            'session_management',
            'interrupt_handling',
            'text_filtering',
            'browser_use',
        ]

    async def _register_modules(self, registrar) -> None:
        """Регистрация модулей через переданный registrar."""
        logger.info("Регистрация модулей через ModuleFactory...")

        modules_config = self._get_module_configs()

        for capability in self._module_capabilities():
            try:
                module = ModuleFactory.create(capability)
                module_config = modules_config.get(capability, {})
                await registrar(capability, module, module_config)
                logger.info(f"✅ Модуль '{capability}' создан и зарегистрирован")
            except Exception as e:
                logger.error(f"❌ Ошибка регистрации модуля '{capability}': {e}")
                raise
    
    async def _create_workflow_integrations(self) -> None:
        """Создание workflow интеграций"""
        logger.info("Создание workflow интеграций...")

        try:
            text_module = self._get_module('text_processing')
            audio_module = self._get_module('audio_generation')
            memory_module = self._get_module('memory_management')
            interrupt_module = self._get_module('interrupt_handling')
            filter_module = self._get_module('text_filtering')

            self.streaming_workflow = StreamingWorkflowIntegration(
                text_processor=text_module,
                audio_processor=audio_module,
                memory_workflow=None,  # Будет установлен ниже
                text_filter_manager=filter_module,
                workflow_config=self.unified_config.get_workflow_thresholds(),
                coordinator=self.coordinator,  # Для доступа к browser_use модулю
            )

            self.memory_workflow = MemoryWorkflowIntegration(
                memory_manager=memory_module
            )

            self.interrupt_workflow = InterruptWorkflowIntegration(
                interrupt_manager=interrupt_module
            )

            self.streaming_workflow.memory_workflow = self.memory_workflow

            logger.info("✅ Workflow интеграции созданы")

        except Exception as e:
            logger.error(f"❌ Ошибка создания workflow интеграций: {e}")
            raise
    
    def _get_module(self, capability: str) -> UniversalModuleInterface:
        """Получает модуль из координатора или legacy-реестра."""
        if self.coordinator and self.coordinator.has(capability):
            return self.coordinator.get(capability)
        if capability in self._legacy_modules:
            return self._legacy_modules[capability]
        raise KeyError(f"Capability '{capability}' недоступен в текущей конфигурации")
    
    async def _create_service_integrations(self) -> None:
        """Создание service интеграций"""
        logger.info("Создание service интеграций...")
        
        try:
            self.grpc_service_integration = GrpcServiceIntegration(
                streaming_workflow=self.streaming_workflow,
                memory_workflow=self.memory_workflow,
                interrupt_workflow=self.interrupt_workflow
            )
            
            logger.info("✅ Service интеграции созданы")
            
        except Exception as e:
            logger.error(f"❌ Ошибка создания service интеграций: {e}")
            raise
    
    async def _initialize_integrations(self) -> None:
        """Инициализация всех интеграций"""
        logger.info("Инициализация интеграций...")
        
        try:
            # Инициализируем workflow интеграции
            if self.streaming_workflow:
                await self.streaming_workflow.initialize()
                logger.info("✅ StreamingWorkflowIntegration инициализирован")
            
            if self.memory_workflow:
                await self.memory_workflow.initialize()
                logger.info("✅ MemoryWorkflowIntegration инициализирован")
            
            if self.interrupt_workflow:
                await self.interrupt_workflow.initialize()
                logger.info("✅ InterruptWorkflowIntegration инициализирован")
            
            # Инициализируем service интеграции
            if self.grpc_service_integration:
                await self.grpc_service_integration.initialize()
                logger.info("✅ GrpcServiceIntegration инициализирован")
            
        except Exception as e:
            logger.error(f"❌ Ошибка инициализации интеграций: {e}")
            raise
    
    async def process(self, request: Dict[str, Any]) -> AsyncGenerator[Dict[str, Any], None]:
        """
        Обработка запроса через gRPC сервис
        
        Args:
            request: Входные данные для обработки
            
        Yields:
            Результаты обработки
        """
        try:
            self._status = ModuleStatus(state=ModuleState.PROCESSING, health="ok")
            
            # Обрабатываем через GrpcServiceIntegration
            if self.grpc_service_integration:
                async for result in self.grpc_service_integration.process_request_complete(request):
                    yield result
            else:
                logger.error("GrpcServiceIntegration не доступен")
                yield {
                    'success': False,
                    'error': 'GrpcServiceIntegration not available'
                }
                
        except Exception as e:
            logger.error(f"Ошибка обработки в gRPC Service Manager: {e}")
            yield {
                'success': False,
                'error': str(e)
            }
        finally:
            self._status = ModuleStatus(state=ModuleState.READY, health="ok")
    
    async def cleanup(self) -> None:
        """
        Очистка ресурсов gRPC сервиса
        """
        try:
            logger.info("Очистка gRPC Service Manager...")
            
            # Очищаем service интеграции
            if self.grpc_service_integration:
                await self.grpc_service_integration.cleanup()
                logger.info("✅ GrpcServiceIntegration очищен")
            
            # Очищаем workflow интеграции
            if self.streaming_workflow:
                await self.streaming_workflow.cleanup()
                logger.info("✅ StreamingWorkflowIntegration очищен")
            
            if self.memory_workflow:
                await self.memory_workflow.cleanup()
                logger.info("✅ MemoryWorkflowIntegration очищен")
            
            if self.interrupt_workflow:
                await self.interrupt_workflow.cleanup()
                logger.info("✅ InterruptWorkflowIntegration очищен")
            
            # Очищаем координатор (это очистит все модули)
            if self.coordinator:
                await self.coordinator.cleanup_all()
                logger.info("✅ ModuleCoordinator очищен")
            
            if self._legacy_modules:
                for module_name, module in list(self._legacy_modules.items()):
                    try:
                        await module.cleanup()
                        logger.debug(f"✅ Legacy модуль '{module_name}' очищен")
                    except Exception as legacy_err:
                        logger.error(f"❌ Ошибка очистки legacy модуля '{module_name}': {legacy_err}")
                self._legacy_modules.clear()
            
            self._status = ModuleStatus(state=ModuleState.STOPPED, health="down")
            logger.info("✅ gRPC Service Manager очищен")
            
        except Exception as e:
            logger.error(f"❌ Ошибка очистки gRPC Service Manager: {e}")
            self._status = ModuleStatus(
                state=ModuleState.ERROR,
                health="down",
                last_error=str(e)
            )
    
    def status(self) -> ModuleStatus:
        """
        Получение статуса gRPC сервиса
        
        Returns:
            ModuleStatus с текущим состоянием
        """
        return self._status
    
    def get_status_dict(self) -> Dict[str, Any]:
        """
        Получение статуса в виде словаря
        
        Returns:
            Словарь со статусом
        """
        status_obj = self.status()
        status_dict: Dict[str, Any] = status_obj.to_dict() if hasattr(status_obj, 'to_dict') else {
            'state': status_obj.state.value if hasattr(status_obj.state, 'value') else str(status_obj.state),
            'health': status_obj.health if hasattr(status_obj, 'health') else 'unknown'
        }
        status_dict['name'] = self.name
        status_dict['use_coordinator'] = self._use_coordinator
        
        # Добавляем статус координатора
        if self.coordinator:
            status_dict['coordinator'] = self.coordinator.get_status()
        
        return status_dict
    
    def get_coordinator(self) -> Optional[ModuleCoordinator]:
        """
        Получение координатора (для совместимости)
        
        Returns:
            Экземпляр ModuleCoordinator или None
        """
        return self.coordinator
