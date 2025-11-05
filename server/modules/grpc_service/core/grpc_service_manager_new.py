"""
Новый GrpcServiceManager с использованием ModuleCoordinator
Реализует PR-2.1: миграция на координатор модулей
"""

import asyncio
import logging
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

# Импорты адаптеров (не прямые импорты модулей!)
from modules.text_processing.module import TextProcessingModule
from modules.audio_generation.adapter import AudioGenerationAdapter
from modules.memory_management.adapter import MemoryManagementAdapter
from modules.database.adapter import DatabaseAdapter
from modules.session_management.adapter import SessionManagementAdapter
from modules.interrupt_handling.adapter import InterruptHandlingAdapter
from modules.text_filtering.adapter import TextFilteringAdapter

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
            
            # Проверяем фича-флаг и kill-switch
            use_coordinator = (
                self.unified_config.is_feature_enabled('use_module_coordinator') and
                not self.unified_config.is_kill_switch_active('disable_module_coordinator')
            )
            
            self._use_coordinator = use_coordinator
            
            if use_coordinator:
                logger.info("✅ Используется ModuleCoordinator (новый подход)")
                await self._initialize_with_coordinator()
            else:
                logger.warning("⚠️ Используется legacy подход (прямые импорты)")
                await self._initialize_legacy()
            
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
        await self._register_modules()
        
        # Инициализируем координатор
        await self.coordinator.initialize_all()
        
        # Создаем workflow интеграции (используют модули из координатора)
        await self._create_workflow_integrations_with_coordinator()
        
        # Создаем service интеграции
        await self._create_service_integrations()
        
        # Инициализируем интеграции
        await self._initialize_integrations()
    
    async def _initialize_legacy(self) -> None:
        """Legacy инициализация (для отката)"""
        logger.warning("⚠️ Используется legacy подход - прямой импорт модулей")
        # Здесь можно оставить старую логику для отката
        # Но для PR-2.1 мы не реализуем это, так как цель - убрать legacy
        raise NotImplementedError("Legacy подход не поддерживается в PR-2.1")
    
    async def _register_modules(self) -> None:
        """Регистрация модулей в координаторе"""
        logger.info("Регистрация модулей в координаторе...")
        
        # Получаем конфигурации модулей из unified_config
        modules_config = {
            'text_processing': self.unified_config.get_module_config('text_processing'),
            'audio_generation': self.unified_config.get_module_config('audio'),
            'memory_management': self.unified_config.get_module_config('memory'),
            'database': self.unified_config.get_module_config('database'),
            'session_management': self.unified_config.get_module_config('session'),
            'interrupt_handling': self.unified_config.get_module_config('interrupt'),
            'text_filtering': {},  # Конфигурация будет из TextFilteringConfig
        }
        
        # Регистрируем модули
        modules_map = {
            'text_processing': TextProcessingModule(),
            'audio_generation': AudioGenerationAdapter(),
            'memory_management': MemoryManagementAdapter(),
            'database': DatabaseAdapter(),
            'session_management': SessionManagementAdapter(),
            'interrupt_handling': InterruptHandlingAdapter(),
            'text_filtering': TextFilteringAdapter(),
        }
        
        for capability, module in modules_map.items():
            try:
                module_config = modules_config.get(capability, {})
                await self.coordinator.register(capability, module, module_config)
                logger.info(f"✅ Модуль '{capability}' зарегистрирован")
                
                # Специальная логика для database -> memory_management
                if capability == 'database':
                    memory_module = self.coordinator.get('memory_management')
                    if hasattr(memory_module, 'set_database_manager'):
                        memory_module.set_database_manager(module.get_manager())
                
            except Exception as e:
                logger.error(f"❌ Ошибка регистрации модуля '{capability}': {e}")
                raise
    
    async def _create_workflow_integrations_with_coordinator(self) -> None:
        """Создание workflow интеграций с использованием координатора"""
        logger.info("Создание workflow интеграций с координатором...")
        
        try:
            # Получаем модули из координатора
            text_module = self.coordinator.get('text_processing')
            audio_module = self.coordinator.get('audio_generation')
            memory_module = self.coordinator.get('memory_management')
            interrupt_module = self.coordinator.get('interrupt_handling')
            filter_module = self.coordinator.get('text_filtering')
            
            # Получаем внутренние процессоры/менеджеры для совместимости
            text_processor = text_module.get_processor() if hasattr(text_module, 'get_processor') else None
            audio_processor = audio_module.get_processor() if hasattr(audio_module, 'get_processor') else None
            memory_manager = memory_module.get_manager() if hasattr(memory_module, 'get_manager') else None
            interrupt_manager = interrupt_module.get_manager() if hasattr(interrupt_module, 'get_manager') else None
            filter_manager = filter_module.get_manager() if hasattr(filter_module, 'get_manager') else None
            
            # Создаем workflow интеграции с модулями
            self.streaming_workflow = StreamingWorkflowIntegration(
                text_processor=text_processor,
                audio_processor=audio_processor,
                memory_workflow=None,  # Будет установлен ниже
                text_filter_manager=filter_manager
            )
            
            self.memory_workflow = MemoryWorkflowIntegration(
                memory_manager=memory_manager
            )
            
            self.interrupt_workflow = InterruptWorkflowIntegration(
                interrupt_manager=interrupt_manager
            )
            
            # Устанавливаем memory_workflow в streaming_workflow
            self.streaming_workflow.memory_workflow = self.memory_workflow
            
            logger.info("✅ Workflow интеграции созданы с использованием координатора")
            
        except Exception as e:
            logger.error(f"❌ Ошибка создания workflow интеграций: {e}")
            raise
    
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
        status_dict = status_obj.to_dict() if hasattr(status_obj, 'to_dict') else {
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

