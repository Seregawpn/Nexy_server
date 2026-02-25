#!/usr/bin/env python3
"""
InterruptWorkflowIntegration - управляет прерываниями на каждом этапе
"""

import asyncio
import logging
from typing import Dict, Any, Callable, Optional, AsyncGenerator
from datetime import datetime

from modules.session_management.core.session_registry import SessionRegistry

logger = logging.getLogger(__name__)


class InterruptException(Exception):
    """Исключение для прерываний"""
    pass


class InterruptWorkflowIntegration:
    """
    Управляет прерываниями на каждом этапе обработки
    """
    
    def __init__(self, interrupt_manager=None):
        """
        Инициализация InterruptWorkflowIntegration
        
        Args:
            interrupt_manager: Модуль управления прерываниями
        """
        self.interrupt_module = interrupt_manager
        self.is_initialized = False
        self.registry = SessionRegistry()  # Используем централизованный реестр
        
        logger.info("InterruptWorkflowIntegration создан")
    
    async def initialize(self) -> bool:
        """
        Инициализация интеграции
        
        Returns:
            True если инициализация успешна, False иначе
        """
        try:
            logger.info("Инициализация InterruptWorkflowIntegration...")
            
            # Проверяем доступность InterruptManager
            if not self.interrupt_module:
                logger.warning("⚠️ InterruptManager не предоставлен")
            
            self.is_initialized = True
            logger.info("✅ InterruptWorkflowIntegration инициализирован успешно")
            return True
            
        except Exception as e:
            logger.error(f"❌ Ошибка инициализации InterruptWorkflowIntegration: {e}")
            return False
    
    async def check_interrupts(self, hardware_id: str) -> bool:
        """
        Проверка активных прерываний

        Args:
            hardware_id: Идентификатор оборудования

        Returns:
            True если есть активные прерывания, False иначе
        """
        if not self.is_initialized:
            logger.error("❌ InterruptWorkflowIntegration не инициализирован")
            return False

        try:
            if not self.interrupt_module:
                logger.debug("InterruptManager не доступен, прерывания не проверяются")
                return False

            # Проверяем через InterruptModule
            response = await self._call_interrupt_module({
                "action": "check_interrupt",
                "hardware_id": hardware_id
            })

            should_interrupt = bool(response.get("interrupted") if isinstance(response, dict) else response)

            if should_interrupt:
                logger.info(f"🛑 Обнаружено прерывание для {hardware_id}")

            return should_interrupt

        except Exception as e:
            logger.warning(f"⚠️ Ошибка проверки прерываний: {e}")
            return False

    async def interrupt_session(self, hardware_id: str) -> Dict[str, Any]:
        """
        Прерывание сессии по hardware_id

        Args:
            hardware_id: Идентификатор оборудования

        Returns:
            Результат прерывания в формате:
            {
                'success': bool,
                'message': str,
                'interrupted_sessions': List[str]
            }
        """
        if not self.is_initialized:
            logger.error("❌ InterruptWorkflowIntegration не инициализирован")
            return {
                'success': False,
                'message': 'InterruptWorkflowIntegration not initialized',
                'interrupted_sessions': []
            }

        try:
            if not self.interrupt_module:
                logger.error("❌ InterruptManager не доступен")
                return {
                    'success': False,
                    'message': 'InterruptManager not available',
                    'interrupted_sessions': []
                }

            interrupt_result = await self._call_interrupt_module({
                "action": "interrupt_session",
                "hardware_id": hardware_id
            }) or {}

            logger.info(f"✅ Прерывание сессии для {hardware_id}: {interrupt_result}")
            return interrupt_result

        except Exception as e:
            logger.error(f"❌ Ошибка прерывания сессии: {e}")
            return {
                'success': False,
                'message': f'Error interrupting session: {str(e)}',
                'interrupted_sessions': []
            }
    
    async def process_with_interrupts(self, workflow_func: Callable, hardware_id: str, session_id: Optional[str] = None) -> AsyncGenerator[Any, None]:
        """
        Обработка с проверкой прерываний на каждом этапе
        
        Args:
            workflow_func: Функция для выполнения
            hardware_id: Идентификатор оборудования
            session_id: Идентификатор сессии (опционально)
            
        Returns:
            Результат выполнения workflow_func
            
        Raises:
            InterruptException: При обнаружении прерывания
        """
        if not self.is_initialized:
            logger.error("❌ InterruptWorkflowIntegration не инициализирован")
            raise InterruptException("InterruptWorkflowIntegration not initialized")
        
        try:
            # Проверяем прерывания в начале
            if await self.check_interrupts(hardware_id):
                logger.info(f"🛑 Прерывание активно для {hardware_id}, отменяем выполнение")
                raise InterruptException(f"Global interrupt active for {hardware_id}")
            
            logger.debug(f"Выполнение workflow для {hardware_id}")
            
            # Выполняем основную функцию как async generator
            async for result in workflow_func():
                # Проверяем прерывания перед каждым yield
                if await self.check_interrupts(hardware_id):
                    logger.info(f"🛑 Прерывание обнаружено во время выполнения для {hardware_id}")
                    raise InterruptException(f"Interrupted during processing for {hardware_id}")
                
                yield result
            
            # Проверяем прерывания после завершения
            if await self.check_interrupts(hardware_id):
                logger.info(f"🛑 Прерывание обнаружено после выполнения для {hardware_id}")
                raise InterruptException(f"Interrupted after processing for {hardware_id}")
            
            logger.debug(f"✅ Workflow завершен успешно для {hardware_id}")
            
        except InterruptException:
            # Перебрасываем InterruptException
            raise
        except Exception as e:
            logger.error(f"❌ Ошибка выполнения workflow: {e}")
            raise

    async def _call_interrupt_module(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Делегирует вызовы в interrupt_module.process."""
        if not self.interrupt_module or not hasattr(self.interrupt_module, 'process'):
            return {}
        result = await self.interrupt_module.process(payload)
        if hasattr(result, "__aiter__"):
            return await self._first_from_async_iterator(result) or {}
        return result or {}

    async def _first_from_async_iterator(self, iterator) -> Optional[Dict[str, Any]]:
        try:
            return await iterator.__anext__()
        except StopAsyncIteration:
            return None
    
    async def cleanup_on_interrupt(self, hardware_id: str, session_id: Optional[str] = None):
        """
        Очистка ресурсов при прерывании
        
        Args:
            hardware_id: Идентификатор оборудования
            session_id: Идентификатор сессии (опционально)
        """
        try:
            logger.info(f"🧹 Очистка ресурсов при прерывании для {hardware_id}")
            
            # Прерываем сессии через реестр
            sessions = self.registry.get_sessions_by_hardware_id(hardware_id)
            for session in sessions:
                if session.status == "active":
                    self.registry.interrupt_session(session.session_id, "workflow_interrupt")
            
            logger.info(f"✅ Ресурсы очищены для {hardware_id}")
            
        except Exception as e:
            logger.error(f"❌ Ошибка очистки ресурсов: {e}")
    
    def get_active_sessions(self, hardware_id: Optional[str] = None) -> Dict[str, Dict[str, Any]]:
        """
        Получение активных сессий из централизованного реестра
        
        Args:
            hardware_id: Фильтр по hardware_id (опционально)
            
        Returns:
            Словарь активных сессий
        """
        try:
            if hardware_id:
                sessions = self.registry.get_sessions_by_hardware_id(hardware_id)
            else:
                sessions = self.registry.get_all_sessions()
            
            result = {}
            for session in sessions:
                if session.status == "active":
                    result[session.session_id] = {
                        'hardware_id': session.hardware_id,
                        'start_time': session.created_at,
                        'status': session.status
                    }
            return result
                
        except Exception as e:
            logger.warning(f"⚠️ Ошибка получения активных сессий: {e}")
            return {}
    
    async def cleanup(self):
        """Очистка ресурсов"""
        try:
            logger.info("Очистка InterruptWorkflowIntegration...")
            self.is_initialized = False
            logger.info("✅ InterruptWorkflowIntegration очищен")
            
        except Exception as e:
            logger.error(f"❌ Ошибка очистки InterruptWorkflowIntegration: {e}")

