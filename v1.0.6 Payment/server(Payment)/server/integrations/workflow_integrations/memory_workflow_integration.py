#!/usr/bin/env python3
"""
MemoryWorkflowIntegration - управляет памятью параллельно основному потоку
"""

import asyncio
import logging
import traceback
from typing import Dict, Any, Optional
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)


class MemoryWorkflowIntegration:
    """
    Управляет памятью параллельно основному потоку обработки
    """
    
    def __init__(self, memory_manager=None):
        """
        Инициализация MemoryWorkflowIntegration
        
        Args:
            memory_manager: Модуль управления памятью
        """
        self.memory_module = memory_manager
        self.is_initialized = False
        self.memory_cache = {}  # Кэш для быстрого доступа
        self.cache_ttl = 300  # 5 минут TTL для кэша
        self.memory_fetch_timeout = 0.3  # Максимальное время ожидания памяти
        self.memory_update_timeout = 1.0  # Таймаут записи памяти
        self._memory_tasks = {}
        
        logger.info("MemoryWorkflowIntegration создан")
    
    async def initialize(self) -> bool:
        """
        Инициализация интеграции
        
        Returns:
            True если инициализация успешна, False иначе
        """
        try:
            logger.info("Инициализация MemoryWorkflowIntegration...")
            
            # Проверяем доступность модуля памяти
            if not self.memory_module:
                logger.warning("⚠️ MemoryManager не предоставлен")
            else:
                await self._warmup_memory_manager()
            
            self.is_initialized = True
            logger.info("✅ MemoryWorkflowIntegration инициализирован успешно")
            return True
            
        except Exception as e:
            logger.error(f"❌ Ошибка инициализации MemoryWorkflowIntegration: {e}")
            return False
    
    async def get_memory_context_parallel(self, hardware_id: str) -> Optional[Dict[str, Any]]:
        """
        Асинхронное получение контекста памяти (неблокирующее)
        
        Args:
            hardware_id: Идентификатор оборудования
            
        Returns:
            Контекст памяти или None при ошибке
        """
        if not self.is_initialized:
            logger.error("❌ MemoryWorkflowIntegration не инициализирован")
            return None
        
        try:
            logger.debug(f"Получение контекста памяти для {hardware_id}")
            
            # Проверяем кэш
            cached_context = self._get_cached_memory(hardware_id)
            if cached_context:
                logger.debug("✅ Используем кэшированный контекст памяти")
                return cached_context
            
            if not self.memory_module or not hasattr(self.memory_module, 'process'):
                logger.debug("MemoryModule не доступен или не поддерживает process()")
                return None

            # Если запрос уже выполняется, не создаём новый
            existing_task = self._memory_tasks.get(hardware_id)
            if existing_task and not existing_task.done():
                logger.debug("Запрос контекста памяти уже выполняется")
                return None

            logger.debug("Запускаем фоновой запрос контекста памяти")
            task = asyncio.create_task(self._fetch_and_cache_memory(hardware_id))
            self._memory_tasks[hardware_id] = task
            task.add_done_callback(lambda _: self._memory_tasks.pop(hardware_id, None))
            return None
            
        except Exception as e:
            logger.warning(f"⚠️ Ошибка получения контекста памяти: {e}")
            return None
    
    async def save_to_memory_background(self, data: Dict[str, Any]) -> bool:
        """
        Фоновое сохранение в память (неблокирующее)
        
        Args:
            data: Данные для сохранения
            
        Returns:
            True если сохранение запущено, False при ошибке
        """
        if not self.is_initialized:
            logger.error("❌ MemoryWorkflowIntegration не инициализирован")
            return False
        
        try:
            logger.debug("Запуск фонового сохранения в память")
            
            # Проверяем доступность MemoryManager
            if not self.memory_module or not hasattr(self.memory_module, 'process'):
                logger.warning("⚠️ MemoryModule не доступен для сохранения")
                return False
            
            # Запускаем сохранение в фоне
            asyncio.create_task(
                self._save_memory_background(data)
            )
            
            logger.debug("✅ Фоновое сохранение в память запущено")
            return True
            
        except Exception as e:
            logger.error(f"❌ Ошибка запуска фонового сохранения: {e}")
            return False
    
    async def _fetch_memory_context(self, hardware_id: str) -> Optional[Dict[str, Any]]:
        """
        Получение контекста памяти из MemoryManager
        
        Args:
            hardware_id: Идентификатор оборудования
            
        Returns:
            Контекст памяти
        """
        try:
            if not self.memory_module or not hasattr(self.memory_module, 'process'):
                return None
            
            response = await asyncio.wait_for(
                self._call_memory_module({"action": "get_context", "hardware_id": hardware_id}),
                timeout=self.memory_fetch_timeout
            )

            memory_context = self._extract_memory_from_response(response)
            
            if memory_context:
                logger.debug(f"Получен контекст памяти: {type(memory_context)}")
                return memory_context
            logger.debug("Контекст памяти пуст")
            return None
                
        except asyncio.TimeoutError:
            logger.warning(f"⚠️ Таймаут получения памяти для {hardware_id}")
            return None
        except Exception as e:
            logger.warning(f"⚠️ Ошибка получения контекста из MemoryModule: {e}")
            return None
    
    async def _save_memory_background(self, data: Dict[str, Any]):
        """
        Фоновое сохранение данных в память
        
        Args:
            data: Данные для сохранения
        """
        try:
            logger.debug("Выполнение фонового сохранения в память")
            
            # Подготавливаем данные для сохранения
            memory_data = self._prepare_memory_data(data)
            
            hardware_id = memory_data.get('hardware_id')
            prompt = memory_data.get('prompt') or memory_data.get('text')
            response = memory_data.get('response') or memory_data.get('processed_text')

            if not all([hardware_id, prompt, response]):
                logger.warning("⚠️ Недостаточно данных для обновления памяти: hardware_id/prompt/response")
                return

            await asyncio.wait_for(
                self._call_memory_module({
                    "action": "update_background",
                    "hardware_id": hardware_id,
                    "prompt": prompt,
                    "response": response
                }),
                timeout=self.memory_update_timeout
            )
            
            logger.debug("✅ Фоновое сохранение в память завершено")
            
        except asyncio.TimeoutError:
            logger.warning(f"⚠️ Таймаут фонового сохранения в память (timeout={self.memory_update_timeout}s)")
        except Exception as e:
            error_msg = str(e) if e else "Неизвестная ошибка"
            error_type = type(e).__name__
            logger.error(
                f"❌ Ошибка фонового сохранения в память: {error_type}: {error_msg}\n"
                f"Traceback: {''.join(traceback.format_exception(type(e), e, e.__traceback__))}"
            )

    async def _call_memory_module(self, payload: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Унифицированный вызов memory_module.process."""
        if not self.memory_module or not hasattr(self.memory_module, 'process'):
            logger.warning("⚠️ MemoryModule не доступен или не поддерживает process()")
            return None
        try:
            result = await self.memory_module.process(payload)
            if hasattr(result, "__aiter__"):
                return await self._first_from_async_iterator(result)
            return result
        except Exception as e:
            logger.error(f"❌ Ошибка вызова memory_module.process: {type(e).__name__}: {e}")
            raise

    async def _first_from_async_iterator(self, iterator) -> Optional[Any]:
        """Возвращает первый элемент из async iterator."""
        try:
            return await iterator.__anext__()
        except StopAsyncIteration:
            return None

    def _extract_memory_from_response(self, response: Any) -> Optional[Dict[str, Any]]:
        """Приводит ответ модуля памяти к словарю контекста."""
        if response is None:
            return None
        
        # Проверяем, не является ли response корутиной (недожидались await)
        if hasattr(response, '__await__'):
            logger.warning("⚠️ Получена корутина вместо результата - возможно забыт await")
            return None
        
        if isinstance(response, dict):
            if "memory" in response:
                return response.get("memory")
            return response
        
        # Если это строка (контекст памяти), оборачиваем в словарь
        if isinstance(response, str):
            return {"context": response}
        
        return response
    
    def _prepare_memory_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Подготовка данных для сохранения в память
        
        Args:
            data: Исходные данные
            
        Returns:
            Подготовленные данные
        """
        try:
            # Добавляем метаданные
            memory_data = {
                'timestamp': datetime.now().isoformat(),
                'hardware_id': data.get('hardware_id'),
                'session_id': data.get('session_id'),
                'text': data.get('text', ''),
                'prompt': data.get('prompt', ''),
                'response': data.get('response', ''),
                'screenshot': data.get('screenshot'),
                'processed_text': data.get('processed_text', ''),
                'audio_generated': data.get('audio_generated', False)
            }
            
            logger.debug(f"Подготовлены данные для сохранения: {len(memory_data)} полей")
            return memory_data
            
        except Exception as e:
            logger.warning(f"⚠️ Ошибка подготовки данных для памяти: {e}")
            return data

    async def _fetch_and_cache_memory(self, hardware_id: str):
        """Фоновое получение памяти с кэшированием и таймаутом."""
        if not self.memory_module or not hasattr(self.memory_module, 'process'):
            return None
        try:
            memory_context = await asyncio.wait_for(
                self._call_memory_module({"action": "get_context", "hardware_id": hardware_id}),
                timeout=self.memory_fetch_timeout
            )
            memory_context = self._extract_memory_from_response(memory_context)
            if memory_context:
                self._cache_memory(hardware_id, memory_context)
                logger.debug(
                    "✅ Фоново получен контекст памяти: %s элементов",
                    len(memory_context) if isinstance(memory_context, dict) else "unknown"
                )
            return memory_context
        except asyncio.TimeoutError:
            logger.warning("⚠️ Таймаут фонового запроса памяти для %s", hardware_id)
        except Exception as e:
            logger.warning("⚠️ Ошибка фонового запроса памяти для %s: %s", hardware_id, e)
        return None

    async def _warmup_memory_manager(self):
        """Прогрев MemoryModule, чтобы исключить задержки при первом запросе."""
        if not self.memory_module or not hasattr(self.memory_module, 'process'):
            return
        try:
            # Отправляем фиктивный запрос, чтобы инициализировать соединения
            try:
                result = await asyncio.wait_for(
                    self._call_memory_module({"action": "get_context", "hardware_id": "__warmup__"}),
                    timeout=self.memory_fetch_timeout
                )
                # Проверяем результат, но не обрабатываем его (это прогрев)
                if result is not None:
                    logger.debug("✅ MemoryModule прогрет")
            except Exception as e:
                # Игнорируем ошибки прогрева, т.к. hardware_id фиктивный
                logger.debug(f"⚠️ Ошибка прогрева MemoryModule (ожидаемо для __warmup__): {e}")
            logger.debug("✅ MemoryModule прогрев завершен")
        except asyncio.TimeoutError:
            logger.debug("⚠️ Таймаут прогрева MemoryModule (не критично)")
        except Exception as e:
            logger.debug(f"⚠️ Ошибка прогрева MemoryModule: {e}")
    
    def _get_cached_memory(self, hardware_id: str) -> Optional[Dict[str, Any]]:
        """
        Получение кэшированного контекста памяти
        
        Args:
            hardware_id: Идентификатор оборудования
            
        Returns:
            Кэшированный контекст или None
        """
        try:
            if hardware_id not in self.memory_cache:
                return None
            
            cache_entry = self.memory_cache[hardware_id]
            cache_time = cache_entry.get('timestamp')
            
            # Проверяем TTL
            if cache_time:
                cache_age = datetime.now() - cache_time
                if cache_age > timedelta(seconds=self.cache_ttl):
                    # Кэш устарел, удаляем
                    del self.memory_cache[hardware_id]
                    logger.debug(f"Кэш памяти для {hardware_id} устарел и удален")
                    return None
            
            logger.debug(f"Используем кэшированную память для {hardware_id}")
            return cache_entry.get('context')
            
        except Exception as e:
            logger.warning(f"⚠️ Ошибка получения кэшированной памяти: {e}")
            return None
    
    def _cache_memory(self, hardware_id: str, memory_context: Dict[str, Any]):
        """
        Кэширование контекста памяти
        
        Args:
            hardware_id: Идентификатор оборудования
            memory_context: Контекст памяти
        """
        try:
            self.memory_cache[hardware_id] = {
                'context': memory_context,
                'timestamp': datetime.now()
            }
            
            logger.debug(f"Контекст памяти для {hardware_id} закэширован")
            
        except Exception as e:
            logger.warning(f"⚠️ Ошибка кэширования памяти: {e}")
    
    async def cleanup(self):
        """Очистка ресурсов"""
        try:
            logger.info("Очистка MemoryWorkflowIntegration...")
            
            # Очищаем кэш
            self.memory_cache.clear()
            
            self.is_initialized = False
            logger.info("✅ MemoryWorkflowIntegration очищен")
            
        except Exception as e:
            logger.error(f"❌ Ошибка очистки MemoryWorkflowIntegration: {e}")
