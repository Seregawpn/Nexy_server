"""
Основной координатор Interrupt Handling Module

Управляет прерываниями, глобальными флагами и отменой операций
"""

import asyncio
import logging
import time
from typing import Dict, Any, Optional, Set, Callable
from datetime import datetime

from integrations.core.universal_module_interface import UniversalModuleInterface
from integrations.core.module_status import ModuleStatus, ModuleState
from modules.interrupt_handling.config import InterruptHandlingConfig
from modules.session_management.core.session_registry import SessionRegistry

logger = logging.getLogger(__name__)

class InterruptManager(UniversalModuleInterface):
    """
    Основной координатор обработки прерываний
    
    Управляет глобальными флагами, активными сессиями и отменой операций
    """
    
    def __init__(self, config: Optional[InterruptHandlingConfig] = None):
        """
        Инициализация менеджера прерываний
        
        Args:
            config: Конфигурация модуля прерываний
        """
        super().__init__("interrupt_handling")
        
        self.config = config or InterruptHandlingConfig()
        
        # GlobalFlagProvider будет инициализирован в _initialize_components
        self.global_flag_provider = None
        
        # Реестр сессий
        self.registry = SessionRegistry()
        
        # Зарегистрированные модули для прерывания
        self.registered_modules: Dict[str, Any] = {}
        
        # Callback функции для прерывания
        self.interrupt_callbacks: Set[Callable] = set()
        
        # Статистика
        self.total_interrupts = 0
        self.successful_interrupts = 0
        self.failed_interrupts = 0
        
        logger.info("Interrupt Manager created")
    
    async def initialize(self) -> bool:
        """
        Инициализация модуля прерываний
        
        Returns:
            True если инициализация успешна, False иначе
        """
        try:
            logger.info("Initializing Interrupt Manager...")
            
            self._status = ModuleStatus(state=ModuleState.INIT, health="degraded")
            
            # Проверяем конфигурацию
            if not self.config.get("global_interrupt_enabled", True):
                logger.warning("Global interrupt is disabled in configuration")
            
            # Инициализируем базовые компоненты
            await self._initialize_components()
            
            self._status = ModuleStatus(state=ModuleState.READY, health="ok")
            self.is_initialized = True
            
            logger.info("Interrupt Manager initialized successfully")
            return True
            
        except Exception as e:
            logger.error(f"Failed to initialize Interrupt Manager: {e}")
            self._status = ModuleStatus(state=ModuleState.ERROR, health="down", last_error=str(e))
            return False
    
    async def _initialize_components(self):
        """Инициализация базовых компонентов"""
        try:
            # Инициализируем провайдеры прерывания
            from modules.interrupt_handling.providers.global_flag_provider import GlobalFlagProvider
            
            # Преобразуем конфигурацию в словарь
            config_dict = self.config.config if hasattr(self.config, 'config') else {}
            
            self.global_flag_provider = GlobalFlagProvider(config_dict)
            await self.global_flag_provider.initialize()
            
            logger.info("Interrupt providers initialized")
            
        except Exception as e:
            logger.error(f"Failed to initialize interrupt providers: {e}")
            raise
    
    async def process(self, input_data: Dict[str, Any]) -> Any:
        """
        Основная обработка прерываний
        
        Args:
            input_data: Данные для обработки прерывания
            
        Returns:
            Результат обработки прерывания
        """
        try:
            operation = input_data.get("operation", "interrupt_session")
            
            if operation == "interrupt_session":
                return await self.interrupt_session(input_data.get("hardware_id", ""))
            elif operation == "register_module":
                return await self.register_module(
                    input_data.get("module_name", ""),
                    input_data.get("module_instance")
                )
            elif operation == "register_callback":
                callback = input_data.get("callback")
                if callback is None:
                    return {"success": False, "error": "callback is required"}
                return await self.register_callback(callback)
            elif operation == "check_interrupt":
                return self.should_interrupt(input_data.get("hardware_id", ""))
            else:
                logger.warning(f"Unknown interrupt operation: {operation}")
                return {"success": False, "error": f"Unknown operation: {operation}"}
                
        except Exception as e:
            logger.error(f"Error processing interrupt request: {e}")
            return {"success": False, "error": str(e)}
    
    async def interrupt_session(self, hardware_id: str) -> Dict[str, Any]:
        """
        Прерывание сессии для указанного hardware_id
        
        Args:
            hardware_id: ID оборудования для прерывания
            
        Returns:
            Результат прерывания
        """
        try:
            interrupt_start_time = time.time()
            
            logger.warning(f"🚨 Interrupt session requested for hardware_id: {hardware_id}")
            
            # Получаем активные сессии из реестра
            sessions = self.registry.get_sessions_by_hardware_id(hardware_id)
            active_sessions_for_hw = [s for s in sessions if s.status == "active"]
            
            if len(active_sessions_for_hw) > 1:
                session_ids = [s.session_id for s in active_sessions_for_hw]
                logger.warning(
                    f"⚠️ [INTERRUPT_DIAG] Прерывание hardware_id={hardware_id} с {len(active_sessions_for_hw)} активными сессиями: {session_ids}",
                    extra={
                        'scope': 'interrupt',
                        'method': 'interrupt_session',
                        'hardware_id': hardware_id,
                        'active_sessions_count': len(active_sessions_for_hw),
                        'session_ids': session_ids,
                        'decision': 'warning',
                        'ctx': {
                            'reason': 'multiple_active_sessions',
                            'hardware_id': hardware_id,
                            'session_count': len(active_sessions_for_hw),
                            'session_ids': session_ids
                        }
                    }
                )
            elif len(active_sessions_for_hw) == 1:
                session_id = active_sessions_for_hw[0].session_id
                logger.debug(f"✅ [INTERRUPT_DIAG] Прерывание hardware_id={hardware_id} с 1 активной сессией: {session_id}")
            else:
                logger.debug(f"ℹ️ [INTERRUPT_DIAG] Прерывание hardware_id={hardware_id} без активных сессий")
            
            # Устанавливаем глобальные флаги
            await self._set_global_interrupt_flags(hardware_id)
            
            # Прерываем все зарегистрированные модули
            interrupted_modules = await self._interrupt_all_modules(hardware_id)
            
            # Прерываем активные сессии
            cleaned_sessions = []
            for session in active_sessions_for_hw:
                if self.registry.interrupt_session(session.session_id, "interrupt_manager_request"):
                    cleaned_sessions.append(session.session_id)
            
            # Обновляем статистику
            self.total_interrupts += 1
            self.successful_interrupts += 1
            
            interrupt_end_time = time.time()
            total_time = (interrupt_end_time - interrupt_start_time) * 1000
            
            logger.warning(f"✅ Interrupt completed for {hardware_id} in {total_time:.1f}ms (interrupted {len(cleaned_sessions)} sessions)")
            
            return {
                "success": True,
                "hardware_id": hardware_id,
                "interrupted_modules": interrupted_modules,
                "cleaned_sessions": cleaned_sessions,
                "total_time_ms": total_time,
                "timestamp": interrupt_start_time
            }
            
        except Exception as e:
            logger.error(f"Error interrupting session for {hardware_id}: {e}")
            self.failed_interrupts += 1
            
            return {
                "success": False,
                "hardware_id": hardware_id,
                "error": str(e),
                "timestamp": time.time()
            }
    
    async def _set_global_interrupt_flags(self, hardware_id: str):
        """Установка глобальных флагов прерывания через GlobalFlagProvider"""
        try:
            if self.global_flag_provider:
                await self.global_flag_provider.set_interrupt_flag(hardware_id)
            
            logger.warning(f"🚨 Global interrupt flags set for {hardware_id}")
            
        except Exception as e:
            logger.error(f"Error setting global interrupt flags: {e}")
            raise
    
    async def _interrupt_all_modules(self, hardware_id: str) -> list:
        """Прерывание всех зарегистрированных модулей"""
        interrupted_modules = []
        
        try:
            for module_name, module_instance in self.registered_modules.items():
                try:
                    if not self.config.is_module_interrupt_enabled(module_name):
                        logger.debug(f"Interrupt disabled for module: {module_name}")
                        continue
                    
                    # Получаем методы прерывания для модуля
                    interrupt_methods = self.config.get_module_interrupt_methods(module_name)
                    module_timeout = self.config.get_module_timeout(module_name)
                    
                    # Вызываем методы прерывания
                    for method_name in interrupt_methods:
                        if hasattr(module_instance, method_name):
                            method = getattr(module_instance, method_name)
                            
                            # Вызываем метод с таймаутом
                            try:
                                if asyncio.iscoroutinefunction(method):
                                    await asyncio.wait_for(method(), timeout=module_timeout)
                                else:
                                    method()
                                
                                logger.warning(f"🚨 Module {module_name}.{method_name} interrupted for {hardware_id}")
                                
                            except asyncio.TimeoutError:
                                logger.error(f"Timeout interrupting {module_name}.{method_name}")
                            except Exception as e:
                                logger.error(f"Error interrupting {module_name}.{method_name}: {e}")
                    
                    interrupted_modules.append(module_name)
                    
                except Exception as e:
                    logger.error(f"Error interrupting module {module_name}: {e}")
            
            # Вызываем callback функции
            for callback in self.interrupt_callbacks:
                try:
                    if asyncio.iscoroutinefunction(callback):
                        await callback(hardware_id)
                    else:
                        callback(hardware_id)
                except Exception as e:
                    logger.error(f"Error in interrupt callback: {e}")
            
            logger.info(f"Interrupted {len(interrupted_modules)} modules for {hardware_id}")
            
        except Exception as e:
            logger.error(f"Error interrupting modules: {e}")
        
        return interrupted_modules
    
    # Методы register_session и unregister_session оставлены для обратной совместимости,
    # но используют SessionRegistry, который уже обновляется через SessionTracker.
    # Фактически они становятся no-op или логгирующими заглушками, так как регистрация
    # происходит через SessionTracker.
    
    async def register_session(self, session_id: str, hardware_id: str, session_data: Dict[str, Any]) -> bool:
        """
        Регистрация активной сессии (Deprecated: используется SessionRegistry)
        """
        logger.debug(f"register_session called for {session_id}. Using centralized SessionRegistry.")
        return True
    
    async def unregister_session(self, session_id: str) -> bool:
        """
        Отмена регистрации сессии (Deprecated: используется SessionRegistry)
        """
        logger.debug(f"unregister_session called for {session_id}. Using centralized SessionRegistry.")
        return True

    async def register_module(self, module_name: str, module_instance: Any) -> bool:
        """
        Регистрация модуля для прерывания
        
        Args:
            module_name: Имя модуля
            module_instance: Экземпляр модуля
            
        Returns:
            True если регистрация успешна, False иначе
        """
        try:
            self.registered_modules[module_name] = module_instance
            logger.info(f"Module {module_name} registered for interrupt handling")
            return True
            
        except Exception as e:
            logger.error(f"Error registering module {module_name}: {e}")
            return False
    
    async def register_callback(self, callback: Callable) -> bool:
        """
        Регистрация callback функции для прерывания
        
        Args:
            callback: Функция обратного вызова
            
        Returns:
            True если регистрация успешна, False иначе
        """
        try:
            self.interrupt_callbacks.add(callback)
            logger.info("Callback registered for interrupt handling")
            return True
            
        except Exception as e:
            logger.error(f"Error registering callback: {e}")
            return False
    
    def should_interrupt(self, hardware_id: str) -> bool:
        """
        Проверка, нужно ли прерывать операцию для указанного hardware_id
        Делегирует проверку в GlobalFlagProvider.
        
        Args:
            hardware_id: ID оборудования
            
        Returns:
            True если нужно прерывать, False иначе
        """
        if not self.global_flag_provider:
            return False
        
        result = self.global_flag_provider.check_interrupt_flag(hardware_id)
        should_int = result.get("should_interrupt", False)
        
        # Автоматический сброс при таймауте
        if result.get("timeout_expired", False):
            logger.warning(f"Interrupt timeout for {hardware_id}, resetting flags")
            asyncio.create_task(self.global_flag_provider.reset_flags())
        
        return should_int
    
    async def _reset_interrupt_flags(self):
        """
        Сброс глобальных флагов прерывания через GlobalFlagProvider
        """
        if self.global_flag_provider:
            await self.global_flag_provider.reset_flags()
        logger.info("Global interrupt flags reset")
    
    def status(self) -> ModuleStatus:
        """
        Получение статуса модуля
        
        Returns:
            ModuleStatus с текущим состоянием модуля
        """
        return self._status
    
    async def cleanup(self) -> bool:
        """
        Очистка ресурсов модуля
        
        Returns:
            True если очистка успешна, False иначе
        """
        try:
            logger.info("Cleaning up Interrupt Manager...")
            
            # Сбрасываем флаги
            await self._reset_interrupt_flags()
            
            # Очищаем зарегистрированные модули
            self.registered_modules.clear()
            
            # Очищаем callback функции
            self.interrupt_callbacks.clear()
            
            # Очищаем провайдеры
            if hasattr(self, 'global_flag_provider') and self.global_flag_provider is not None:
                await self.global_flag_provider.cleanup()
            
            self._status = ModuleStatus(state=ModuleState.STOPPED, health="ok")
            self.is_initialized = False
            
            logger.info("Interrupt Manager cleaned up successfully")
            return True
            
        except Exception as e:
            logger.error(f"Error cleaning up Interrupt Manager: {e}")
            return False
    
    def get_statistics(self) -> Dict[str, Any]:
        """Получение статистики прерываний"""
        flag_status = {}
        if self.global_flag_provider:
            flag_status = self.global_flag_provider.get_flag_status()
        
        return {
            "total_interrupts": self.total_interrupts,
            "successful_interrupts": self.successful_interrupts,
            "failed_interrupts": self.failed_interrupts,
            "success_rate": (
                self.successful_interrupts / self.total_interrupts 
                if self.total_interrupts > 0 else 0
            ),
            "registered_modules": len(self.registered_modules),
            "registered_callbacks": len(self.interrupt_callbacks),
            "global_interrupt_flag": flag_status.get("global_interrupt_flag", False),
            "interrupt_hardware_id": flag_status.get("interrupt_hardware_id")
        }
