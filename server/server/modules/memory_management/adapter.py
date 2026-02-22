"""
Адаптер для MemoryManager - временный адаптер для использования через ModuleCoordinator
"""

import asyncio
import logging
from typing import Dict, Any, AsyncIterator, Union, Optional

from integrations.core.universal_module_interface import UniversalModuleInterface
from integrations.core.module_status import ModuleStatus, ModuleState

from modules.memory_management.core.memory_manager import MemoryManager

logger = logging.getLogger(__name__)


class MemoryManagementAdapter(UniversalModuleInterface):
    """
    Адаптер для MemoryManager
    
    Временный адаптер для использования существующего MemoryManager
    через ModuleCoordinator до полной миграции на UniversalModuleInterface.
    """
    
    def __init__(self):
        """Инициализация адаптера"""
        super().__init__(name="memory_management")
        self._manager: Optional[MemoryManager] = None
        self._config: Dict[str, Any] = {}
        self._status = ModuleStatus(ModuleState.INIT)
        self._db_manager = None  # Для установки после инициализации database
        self._cleanup_task: Optional[asyncio.Task] = None
        self._short_term_cleanup_enabled: bool = True
        self._short_term_cleanup_interval_seconds: int = 7200
        self._short_term_cleanup_idle_hours: int = 2
    
    async def initialize(self, config: dict) -> None:
        """
        Инициализация адаптера
        
        Args:
            config: Конфигурация модуля (из unified_config)
        
        Raises:
            Exception: Если инициализация не удалась
        """
        try:
            self._status = ModuleStatus(ModuleState.INIT)
            self._status.health = "degraded"
            logger.info(f"Инициализация адаптера {self.name}...")
            
            self._config = config
            self._short_term_cleanup_enabled = bool(config.get('short_term_cleanup_enabled', True))
            self._short_term_cleanup_interval_seconds = max(
                int(config.get('short_term_cleanup_interval_seconds', 7200)),
                60
            )
            self._short_term_cleanup_idle_hours = max(
                int(config.get('short_term_cleanup_idle_hours', 2)),
                1
            )
            
            # Инициализируем TokenUsageTracker
            token_tracker = None
            try:
                from integrations.core.token_usage_tracker import TokenUsageTracker
                token_tracker = TokenUsageTracker()
                logger.info("TokenUsageTracker initialized for MemoryManager")
            except Exception as e:
                logger.warning(f"Failed to initialize TokenUsageTracker: {e}")
            
            # Создаем менеджер (db_manager будет установлен позже)
            self._manager = MemoryManager(db_manager=self._db_manager, token_usage_tracker=token_tracker)
            
            # Инициализируем менеджер
            if await self._manager.initialize():
                self._status = ModuleStatus(ModuleState.READY)
                self._status.health = "ok"
                await self._start_background_tasks()
                logger.info(f"✅ Адаптер {self.name} инициализирован")
            else:
                raise Exception("Не удалось инициализировать MemoryManager")
                
        except Exception as e:
            self._status = ModuleStatus(ModuleState.ERROR)
            self._status.health = "down"
            self._status.last_error = str(e)
            logger.error(f"❌ Ошибка инициализации адаптера {self.name}: {e}")
            raise
    
    def set_database_manager(self, db_manager):
        """
        Установка DatabaseManager (для совместимости)
        
        Args:
            db_manager: Экземпляр DatabaseManager
        """
        self._db_manager = db_manager
        if self._manager and hasattr(self._manager, 'set_database_manager'):
            self._manager.set_database_manager(db_manager)
    
    async def process(self, request: Dict[str, Any]) -> Union[Dict[str, Any], AsyncIterator[Dict[str, Any]]]:
        """
        Обработка запроса
        
        Args:
            request: Запрос на работу с памятью
                - action: str - действие (get_memory, get_context, update_memory, update_background, analyze)
                - session_id: str - идентификатор сессии (для совместимости)
                - hardware_id: str - идентификатор устройства
                - prompt: str (опционально) - промпт
                - response: str (опционально) - ответ
        
        Returns:
            Результат обработки
        """
        try:
            if self._manager is None:
                raise Exception("MemoryManager not initialized")
            
            self._status = ModuleStatus(ModuleState.PROCESSING)
            self._status.health = "ok"
            
            action = request.get("action", "get_memory")
            session_id = request.get("session_id")
            hardware_id = request.get("hardware_id")

            # Аппаратный идентификатор считается источником правды, но для
            # обратной совместимости допускаем session_id.
            subject_id = hardware_id or session_id
            if action not in ("update_background", "analyze") and not subject_id:
                raise ValueError("hardware_id или session_id должны быть указаны")

            result = {}
            
            if action == "get_memory":
                # Получаем память для сессии
                if subject_id is None:
                    raise ValueError("hardware_id или session_id должны быть указаны")
                memory = await self._manager.get_memory_context(subject_id)
                result = {"memory": memory}
            elif action == "get_context":
                # Новый унифицированный action для получения памяти
                if subject_id is None:
                    raise ValueError("hardware_id или session_id должны быть указаны")
                memory = await self._manager.get_memory_context(subject_id)
                result = {"memory": memory}
            elif action == "update_background":
                prompt = request.get("prompt", "") or request.get("text", "")
                response = request.get("response", "") or request.get("processed_text", "")
                if not hardware_id:
                    raise ValueError("hardware_id обязателен для update_background")
                await self._manager.update_memory_background(hardware_id, prompt, response)
                result = {"success": True}
            elif action == "update_memory":
                # Обновляем память через update_memory_background
                if not session_id:
                    raise ValueError("session_id не указан")
                prompt = request.get("prompt", "")
                response = request.get("response", "")
                # Используем session_id как hardware_id для обратной совместимости
                await self._manager.update_memory_background(session_id, prompt, response)
                result = {"success": True}
            elif action == "analyze":
                # Анализируем память
                prompt = request.get("prompt", "")
                response = request.get("response", "")
                short_memory, long_memory = await self._manager.analyze_conversation(prompt, response)
                result = {"analysis": {"short_memory": short_memory, "long_memory": long_memory}}
            else:
                raise ValueError(f"Неизвестное действие: {action}")
            
            return result
                
        except Exception as e:
            self._status = ModuleStatus(ModuleState.ERROR)
            self._status.health = "down"
            self._status.last_error = str(e)
            logger.error(f"❌ Ошибка обработки в адаптере {self.name}: {e}")
            raise
        finally:
            # Возвращаем статус в READY после обработки
            if self._status.state == ModuleState.PROCESSING:
                self._status = ModuleStatus(ModuleState.READY)
                self._status.health = "ok"
    
    async def cleanup(self) -> None:
        """
        Очистка ресурсов адаптера
        """
        try:
            logger.info(f"Очистка адаптера {self.name}...")
            await self._stop_background_tasks()
            
            # MemoryManager не имеет метода cleanup, просто очищаем ссылку
            self._manager = None
            self._config = {}
            self._status = ModuleStatus(ModuleState.STOPPED)
            self._status.health = "down"
            
            logger.info(f"✅ Адаптер {self.name} очищен")
            
        except Exception as e:
            logger.error(f"❌ Ошибка очистки адаптера {self.name}: {e}")
            self._status = ModuleStatus(ModuleState.ERROR)
            self._status.health = "down"
            self._status.last_error = str(e)
    
    def status(self) -> ModuleStatus:
        """
        Получение статуса адаптера
        
        Returns:
            ModuleStatus с текущим состоянием
        """
        return self._status
    
    def get_manager(self) -> Optional[MemoryManager]:
        """
        Получение внутреннего менеджера (для совместимости)
        
        Returns:
            Экземпляр MemoryManager или None
        """
        return self._manager

    async def _start_background_tasks(self) -> None:
        """Запуск фоновых задач адаптера."""
        if not self._short_term_cleanup_enabled:
            logger.info("Short-term memory periodic cleanup disabled")
            return
        if self._cleanup_task and not self._cleanup_task.done():
            return
        self._cleanup_task = asyncio.create_task(self._short_term_cleanup_loop())
        logger.info(
            "Short-term memory cleanup loop started "
            f"(interval={self._short_term_cleanup_interval_seconds}s, idle_hours={self._short_term_cleanup_idle_hours})"
        )

    async def _stop_background_tasks(self) -> None:
        """Остановка фоновых задач адаптера."""
        if not self._cleanup_task:
            return
        self._cleanup_task.cancel()
        try:
            await self._cleanup_task
        except asyncio.CancelledError:
            pass
        finally:
            self._cleanup_task = None
        logger.info("Short-term memory cleanup loop stopped")

    async def _short_term_cleanup_loop(self) -> None:
        """Периодическая очистка краткосрочной памяти при неактивности."""
        while True:
            try:
                await asyncio.sleep(self._short_term_cleanup_interval_seconds)
                await self._run_short_term_cleanup_once()
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"Error in short-term memory cleanup loop: {e}")

    async def _run_short_term_cleanup_once(self) -> None:
        """Один проход очистки краткосрочной памяти."""
        if not self._manager:
            return
        cleaned_rows = await self._manager.cleanup_expired_memory(
            hours=self._short_term_cleanup_idle_hours
        )
        logger.info(
            "Short-term memory cleanup executed "
            f"(idle_hours={self._short_term_cleanup_idle_hours}, cleaned_rows={cleaned_rows})"
        )
