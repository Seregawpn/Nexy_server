#!/usr/bin/env python3
"""
MemoryWorkflowIntegration - управляет памятью параллельно основному потоку
"""

import asyncio
import logging
from typing import Dict, Any, Optional, Tuple
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
        self._cache_lock = asyncio.Lock()  # Защита кэша
        self.cache_ttl = 600  # 10 минут TTL для кэша (увеличено с 5 минут)
        self.cache_hard_ttl = 86400  # 24 часа hard-TTL для stale fallback без блокировки запроса
        self.cache_refresh_before_expiry = 30  # Обновлять кэш за 30 сек до истечения
        self.memory_fetch_timeout = 0.35  # Короткий blocking fetch для текущего запроса
        self.memory_update_timeout = 1.0  # Таймаут записи памяти
        self._memory_tasks = {}
        self._tasks_lock = asyncio.Lock()  # Защита задач
        self._refresh_tasks = {}  # Задачи предобновления кэша
        
        logger.info("MemoryWorkflowIntegration создан")

    def _resolve_gate_bucket(self, user_input: Optional[str], apply_medium_gate: bool) -> str:
        if not apply_medium_gate:
            return "all"
        manager = None
        getter = getattr(self.memory_module, "get_manager", None)
        if callable(getter):
            manager = getter()
        gate_fn = getattr(manager, "should_include_medium_term", None)
        if callable(gate_fn):
            try:
                include_medium, _ = gate_fn(user_input)
                return "medium" if include_medium else "no_medium"
            except Exception:
                return "no_medium"
        return "no_medium"

    def _variant_key(self, hardware_id: str, user_input: Optional[str], apply_medium_gate: bool) -> Tuple[str, str]:
        return (str(hardware_id), self._resolve_gate_bucket(user_input, apply_medium_gate))
    
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
    
    async def get_memory_context_parallel(
        self,
        hardware_id: str,
        user_input: Optional[str] = None,
        apply_medium_gate: bool = True,
    ) -> Optional[Dict[str, Any]]:
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
            cached_context, is_stale, is_hard_expired = await self._get_cached_memory_state_async(
                hardware_id,
                user_input=user_input,
                apply_medium_gate=apply_medium_gate,
            )
            if cached_context:
                if is_stale:
                    logger.debug(
                        "♻️ Используем stale контекст памяти для %s (hard_expired=%s), обновляем в фоне",
                        hardware_id,
                        is_hard_expired,
                    )
                    await self._ensure_memory_refresh_task(
                        hardware_id,
                        user_input=user_input,
                        apply_medium_gate=apply_medium_gate,
                    )
                else:
                    logger.debug("✅ Используем кэшированный контекст памяти")
                return cached_context

            # На критическом пути НЕ ждём БД: запускаем только фоновое обновление.
            await self._ensure_memory_refresh_task(
                hardware_id,
                user_input=user_input,
                apply_medium_gate=apply_medium_gate,
            )
            # Opportunistic fast-path: если фоновая задача успела завершиться в тот же тик,
            # вернем контекст без дополнительного ожидания.
            await asyncio.sleep(0)
            task_key = self._variant_key(hardware_id, user_input, apply_medium_gate)
            async with self._tasks_lock:
                refresh_task = self._memory_tasks.get(task_key)
            if refresh_task and refresh_task.done():
                try:
                    result = refresh_task.result()
                except Exception:
                    result = None
                extracted = self._extract_memory_from_response(result)
                if extracted:
                    await self._cache_memory(
                        hardware_id,
                        extracted,
                        user_input=user_input,
                        apply_medium_gate=apply_medium_gate,
                    )
                    return extracted
            return None
            
        except Exception as e:
            logger.warning(f"⚠️ Ошибка получения контекста памяти: {e}")
            return None

    async def _ensure_memory_refresh_task(
        self,
        hardware_id: str,
        user_input: Optional[str] = None,
        apply_medium_gate: bool = True,
    ) -> None:
        if not self.memory_module or not hasattr(self.memory_module, 'process'):
            logger.debug("MemoryModule не доступен или не поддерживает process()")
            return

        task_key = self._variant_key(hardware_id, user_input, apply_medium_gate)
        async with self._tasks_lock:
            existing_task = self._memory_tasks.get(task_key)
            if existing_task and not existing_task.done():
                return
            task = asyncio.create_task(
                self._fetch_and_cache_memory(
                    hardware_id,
                    user_input=user_input,
                    apply_medium_gate=apply_medium_gate,
                )
            )
            self._memory_tasks[task_key] = task
            task.add_done_callback(lambda _: asyncio.create_task(self._remove_task(task_key)))
    
    async def save_to_memory_background(self, data: Dict[str, Any]) -> bool:
        """
        Сохранение памяти с подтверждением завершения update-path.
        Гарантирует последовательность:
        update_background -> DB write -> write-through cache.
        
        Args:
            data: Данные для сохранения
            
        Returns:
            True если update-path завершен успешно, False при ошибке
        """
        if not self.is_initialized:
            logger.error("❌ MemoryWorkflowIntegration не инициализирован")
            return False
        
        try:
            logger.debug("Запуск сохранения памяти (await)")
            
            # Проверяем доступность MemoryManager
            if not self.memory_module or not hasattr(self.memory_module, 'process'):
                logger.warning("⚠️ MemoryModule не доступен для сохранения")
                return False
            
            # Ждём завершения update-path, чтобы кэш и БД были согласованы
            await self._save_memory_background(data)
            
            logger.debug("✅ Сохранение памяти завершено (DB + cache)")
            return True
            
        except Exception as e:
            logger.error(f"❌ Ошибка сохранения памяти: {e}")
            return False
    
    async def _fetch_memory_context(
        self,
        hardware_id: str,
        user_input: Optional[str] = None,
        apply_medium_gate: bool = True,
    ) -> Optional[Dict[str, Any]]:
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
                self._call_memory_module(
                    {
                        "action": "get_context",
                        "hardware_id": hardware_id,
                        "user_input": user_input or "",
                        "apply_medium_gate": apply_medium_gate,
                    }
                ),
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

            # После проверки all() мы знаем, что hardware_id не None
            assert hardware_id is not None, "hardware_id should not be None after all() check"
            assert prompt is not None, "prompt should not be None after all() check"
            assert response is not None, "response should not be None after all() check"

            update_response = await asyncio.wait_for(
                self._call_memory_module({
                    "action": "update_background",
                    "hardware_id": hardware_id,
                    "prompt": prompt,
                    "response": response
                }),
                timeout=self.memory_update_timeout
            )

            updated_memory = self._extract_memory_from_response(update_response)
            if updated_memory:
                # Fast-path: кэшируем свежую память сразу из ответа update,
                # без дополнительного roundtrip get_context в БД.
                await self._cache_memory(hardware_id, updated_memory, apply_medium_gate=None)
                logger.debug("✅ Кэш памяти обновлен через fast-path из update_background")
            else:
                # Fallback: если update не вернул память, пробуем старый путь через fetch.
                logger.debug("Memory update не вернул контекст, используем fallback fetch")
                await self._fetch_and_cache_memory(hardware_id, apply_medium_gate=False)
                await self._fetch_and_cache_memory(hardware_id, apply_medium_gate=True)
            
            logger.debug("✅ Фоновое сохранение в память завершено")
            
        except Exception as e:
            logger.error(f"❌ Ошибка фонового сохранения в память: {e}")

    async def _call_memory_module(self, payload: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Унифицированный вызов memory_module.process."""
        if not self.memory_module or not hasattr(self.memory_module, 'process'):
            return None
        result = await self.memory_module.process(payload)
        if hasattr(result, "__aiter__"):
            return await self._first_from_async_iterator(result)
        return result

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
        if isinstance(response, dict):
            if "memory" in response:
                return response.get("memory")
            return response
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

    async def _fetch_and_cache_memory(
        self,
        hardware_id: str,
        user_input: Optional[str] = None,
        apply_medium_gate: bool = True,
    ):
        """Фоновое получение памяти с кэшированием и таймаутом."""
        if not self.memory_module or not hasattr(self.memory_module, 'process'):
            return None
        try:
            memory_context = await asyncio.wait_for(
                self._call_memory_module(
                    {
                        "action": "get_context",
                        "hardware_id": hardware_id,
                        "user_input": user_input or "",
                        "apply_medium_gate": apply_medium_gate,
                    }
                ),
                timeout=self.memory_fetch_timeout
            )
            memory_context = self._extract_memory_from_response(memory_context)
            if memory_context:
                await self._cache_memory(
                    hardware_id,
                    memory_context,
                    user_input=user_input,
                    apply_medium_gate=apply_medium_gate,
                )
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
                await asyncio.wait_for(
                    self._call_memory_module({"action": "get_context", "hardware_id": "__warmup__"}),
                    timeout=self.memory_fetch_timeout
                )
            except Exception:
                # Игнорируем ошибки прогрева, т.к. hardware_id фиктивный
                pass
            logger.debug("✅ MemoryModule прогрет")
        except asyncio.TimeoutError:
            logger.warning("⚠️ Таймаут прогрева MemoryModule")
        except Exception as e:
            logger.warning("⚠️ Ошибка прогрева MemoryModule: %s", e)
    
    async def _get_cached_memory_state_async(
        self,
        hardware_id: str,
        user_input: Optional[str] = None,
        apply_medium_gate: bool = True,
    ) -> tuple[Optional[Dict[str, Any]], bool, bool]:
        """
        Возвращает состояние кэша:
        - context
        - is_stale (soft TTL просрочен)
        - is_hard_expired (hard TTL просрочен; контекст всё равно можно вернуть как fallback)
        """
        try:
            async with self._cache_lock:
                cache_entry = self.memory_cache.get(
                    self._variant_key(hardware_id, user_input, apply_medium_gate)
                )
                if not cache_entry:
                    return None, False, False

                cache_time = cache_entry.get('timestamp')
                context = cache_entry.get('context')
                if not cache_time:
                    return context, False, False

                cache_age = datetime.now() - cache_time
                age_seconds = cache_age.total_seconds()
                is_stale = age_seconds > self.cache_ttl
                is_hard_expired = age_seconds > self.cache_hard_ttl
                return context, is_stale, is_hard_expired
        except Exception as e:
            logger.warning(f"⚠️ Ошибка чтения состояния кэша памяти: {e}")
            return None, False, False

    async def _get_cached_memory_async(
        self,
        hardware_id: str,
        user_input: Optional[str] = None,
        apply_medium_gate: bool = True,
    ) -> Optional[Dict[str, Any]]:
        """
        Получение кэшированного контекста памяти
        
        Args:
            hardware_id: Идентификатор оборудования
            
        Returns:
            Кэшированный контекст или None
        """
        try:
            context, _, is_hard_expired = await self._get_cached_memory_state_async(
                hardware_id,
                user_input=user_input,
                apply_medium_gate=apply_medium_gate,
            )
            if is_hard_expired:
                return None
            return context
        except Exception as e:
            logger.warning(f"⚠️ Ошибка получения кэшированной памяти: {e}")
            return None

    def _get_cached_memory(
        self,
        hardware_id: str,
        user_input: Optional[str] = None,
        apply_medium_gate: bool = True,
    ) -> Optional[Dict[str, Any]]:
        """
        Backward-compatible sync accessor used by tests/debug tooling.
        Runtime flow should call _get_cached_memory_async.
        """
        try:
            cache_entry = self.memory_cache.get(
                self._variant_key(hardware_id, user_input, apply_medium_gate)
            )
            if not cache_entry:
                return None
            cache_time = cache_entry.get('timestamp')
            if cache_time and (datetime.now() - cache_time) > timedelta(seconds=self.cache_hard_ttl):
                return None
            return cache_entry.get('context')
        except Exception:
            return None
    
    async def _cache_memory(
        self,
        hardware_id: str,
        memory_context: Dict[str, Any],
        user_input: Optional[str] = None,
        apply_medium_gate: Optional[bool] = True,
    ):
        """
        Кэширование контекста памяти
        
        Args:
            hardware_id: Идентификатор оборудования
            memory_context: Контекст памяти
        """
        try:
            async with self._cache_lock:
                now = datetime.now()
                if apply_medium_gate is None:
                    # write-through fast-path must not leak medium-term memory into
                    # the non-memory-intent cache bucket
                    self.memory_cache[self._variant_key(hardware_id, None, False)] = {
                        'context': dict(memory_context),
                        'timestamp': now
                    }
                    self.memory_cache[self._variant_key(hardware_id, None, True)] = {
                        'context': self._strip_medium_term_from_context(memory_context),
                        'timestamp': now
                    }
                else:
                    key = self._variant_key(
                        hardware_id,
                        user_input=user_input,
                        apply_medium_gate=apply_medium_gate,
                    )
                    self.memory_cache[key] = {
                        'context': memory_context,
                        'timestamp': now
                    }
            
            # Запускаем задачу предобновления кэша за 30 сек до истечения
            if apply_medium_gate is None:
                await self._schedule_cache_refresh(hardware_id, apply_medium_gate=False)
                await self._schedule_cache_refresh(hardware_id, apply_medium_gate=True)
            else:
                await self._schedule_cache_refresh(hardware_id, apply_medium_gate=apply_medium_gate)
            
            logger.debug(f"Контекст памяти для {hardware_id} закэширован")
            
        except Exception as e:
            logger.warning(f"⚠️ Ошибка кэширования памяти: {e}")

    def _strip_medium_term_from_context(self, memory_context: Dict[str, Any]) -> Dict[str, Any]:
        sanitized = dict(memory_context)
        sanitized['medium_term_context'] = ''
        return sanitized
    
    async def _schedule_cache_refresh(self, hardware_id: str, apply_medium_gate: bool = True):
        """
        Планирование предобновления кэша за 30 сек до истечения
        
        Args:
            hardware_id: Идентификатор оборудования
        """
        try:
            task_key = self._variant_key(hardware_id, None, apply_medium_gate)
            # Отменяем предыдущую задачу, если есть
            async with self._tasks_lock:
                if task_key in self._refresh_tasks:
                    task = self._refresh_tasks[task_key]
                    if not task.done():
                        task.cancel()
            
            # Вычисляем время до обновления
            refresh_delay = self.cache_ttl - self.cache_refresh_before_expiry
            
            # Создаем задачу предобновления
            async def refresh_cache():
                await asyncio.sleep(refresh_delay)
                logger.debug(f"Предобновление кэша памяти для {hardware_id}")
                await self._fetch_and_cache_memory(
                    hardware_id,
                    user_input="",
                    apply_medium_gate=apply_medium_gate,
                )
                await self._remove_refresh_task(task_key)
            
            task = asyncio.create_task(refresh_cache())
            async with self._tasks_lock:
                self._refresh_tasks[task_key] = task
            
        except Exception as e:
            logger.warning(f"⚠️ Ошибка планирования обновления кэша: {e}")
    
    async def prefetch_memory(self, hardware_id: str, user_input: Optional[str] = None) -> bool:
        """
        Предзагрузка памяти для hardware_id (для использования при создании сессии)
        
        Args:
            hardware_id: Идентификатор оборудования
            
        Returns:
            True если предзагрузка запущена, False при ошибке
        """
        if not self.is_initialized:
            logger.debug("MemoryWorkflowIntegration не инициализирован, пропускаем предзагрузку")
            return False
        
        try:
            # Проверяем, есть ли уже в кэше (stale тоже допустим, но его нужно обновить в фоне)
            cached_context, is_stale, _ = await self._get_cached_memory_state_async(
                hardware_id,
                user_input=user_input,
                apply_medium_gate=True,
            )
            if cached_context:
                if is_stale:
                    logger.debug(f"Память для {hardware_id} stale, запускаем фоновое обновление")
                    await self._ensure_memory_refresh_task(
                        hardware_id,
                        user_input=user_input,
                        apply_medium_gate=True,
                    )
                    return True
                logger.debug(f"Память для {hardware_id} уже в кэше, предзагрузка не нужна")
                return True
            
            # Запускаем предзагрузку в фоне
            logger.debug(f"Запуск предзагрузки памяти для {hardware_id}")
            await self._ensure_memory_refresh_task(
                hardware_id,
                user_input=user_input,
                apply_medium_gate=True,
            )
            return True
            
        except Exception as e:
            logger.warning(f"⚠️ Ошибка предзагрузки памяти для {hardware_id}: {e}")
            return False
    
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

    async def _remove_task(self, task_key: Tuple[str, str]) -> None:
        async with self._tasks_lock:
            self._memory_tasks.pop(task_key, None)

    async def _remove_refresh_task(self, task_key: Tuple[str, str]) -> None:
        async with self._tasks_lock:
            self._refresh_tasks.pop(task_key, None)
