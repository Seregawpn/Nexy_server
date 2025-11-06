"""
Update Module Adapter
Обёртка для UpdateManager для соответствия паттерну адаптеров
"""

import logging
from typing import Dict, Any, Optional, AsyncGenerator

from integrations.core.universal_module_interface import UniversalModuleInterface
from integrations.core.module_status import ModuleStatus, ModuleState

from .core.update_manager import UpdateManager
from .config import UpdateConfig

logger = logging.getLogger(__name__)


class UpdateAdapter(UniversalModuleInterface):
    """
    Адаптер для Update Module

    Обёртка над UpdateManager для унифицированного доступа через ModuleCoordinator.
    UpdateManager уже реализует UniversalModuleInterface, поэтому адаптер
    просто делегирует вызовы к нему.
    """

    def __init__(self, config: Optional[UpdateConfig] = None):
        """Инициализация адаптера"""

        super().__init__(name="update")
        self._initial_config = config
        self._manager: Optional[UpdateManager] = None
        self._status = ModuleStatus(state=ModuleState.INIT, health="degraded")

        logger.info("UpdateAdapter создан")

    async def initialize(self, config: dict) -> None:
        """
        Инициализация update модуля

        Args:
            config: Конфигурация из unified_config
        """
        try:
            self._status = ModuleStatus(state=ModuleState.INIT, health="degraded")
            logger.info("Инициализация UpdateAdapter...")

            config_dict = config or {}
            update_config = self._initial_config or UpdateConfig.from_dict(config_dict)
            self._manager = UpdateManager(config=update_config)

            # Делегируем инициализацию в UpdateManager
            await self._manager.initialize(update_config.to_dict())

            if self._manager.is_initialized:
                self._status = ModuleStatus(state=ModuleState.READY, health="ok")
                logger.info("✅ UpdateAdapter инициализирован")
            else:
                self._status = ModuleStatus(
                    state=ModuleState.ERROR,
                    health="down",
                    last_error="UpdateManager initialization failed"
                )
                logger.error("❌ Ошибка инициализации UpdateAdapter")
                raise Exception("UpdateManager initialization failed")

        except Exception as e:
            self._status = ModuleStatus(
                state=ModuleState.ERROR,
                health="down",
                last_error=str(e)
            )
            logger.error(f"❌ Ошибка инициализации UpdateAdapter: {e}")
            raise

    async def process(self, request: Dict[str, Any]) -> AsyncGenerator[Dict[str, Any], None]:
        """
        Обработка запроса к update модулю

        Args:
            request: Запрос с action и параметрами

        Yields:
            Результаты обработки

        Поддерживаемые actions:
        - check_update: Проверка наличия обновлений
        - get_manifest: Получение манифеста
        - get_version: Получение текущей версии
        - get_stats: Получение статистики
        """
        try:
            if not self._manager:
                raise RuntimeError("UpdateManager не инициализирован")

            self._status = ModuleStatus(state=ModuleState.PROCESSING, health="ok")

            action = request.get('action')

            if action == 'check_update':
                # Проверка обновлений
                current_version = request.get('current_version', '0.0.0')
                result = await self._manager.check_update(current_version)
                yield {'success': True, 'data': result}

            elif action == 'get_manifest':
                # Получение манифеста
                platform = request.get('platform', 'macos')
                manifest = await self._manager.get_manifest(platform)
                yield {'success': True, 'data': manifest}

            elif action == 'get_version':
                # Получение версии
                version_info = self._manager.get_current_version()
                yield {'success': True, 'data': version_info}

            elif action == 'get_stats':
                # Статистика
                stats = self._manager.get_stats()
                yield {'success': True, 'data': stats}

            else:
                logger.error(f"Неизвестный action: {action}")
                yield {
                    'success': False,
                    'error': f'Unknown action: {action}'
                }

        except Exception as e:
            logger.error(f"Ошибка обработки в UpdateAdapter: {e}")
            yield {
                'success': False,
                'error': str(e)
            }
        finally:
            self._status = ModuleStatus(state=ModuleState.READY, health="ok")

    async def cleanup(self) -> None:
        """Очистка ресурсов update модуля"""
        try:
            logger.info("Очистка UpdateAdapter...")

            # Делегируем очистку в UpdateManager
            if self._manager:
                await self._manager.cleanup()

            self._status = ModuleStatus(state=ModuleState.STOPPED, health="down")
            logger.info("✅ UpdateAdapter очищен")

        except Exception as e:
            logger.error(f"❌ Ошибка очистки UpdateAdapter: {e}")
            self._status = ModuleStatus(
                state=ModuleState.ERROR,
                health="down",
                last_error=str(e)
            )

    def status(self) -> ModuleStatus:
        """
        Получение статуса update модуля

        Returns:
            ModuleStatus с текущим состоянием
        """
        return self._status

    def get_manager(self) -> Optional[UpdateManager]:
        """
        Получение внутреннего UpdateManager (для compatibility)

        Returns:
            UpdateManager instance

        Note: Этот метод нарушает инкапсуляцию и должен быть удалён
              после рефакторинга workflow integrations (TD-001)
        """
        return self._manager
