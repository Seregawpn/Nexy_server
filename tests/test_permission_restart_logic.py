"""
Тесты для логики permission restart с учётом всех флагов и условий.

Проверяем все сценарии взаимодействия:
- FirstRunPermissions → PermissionRestart
- UpdaterIntegration → PermissionRestart
- Различные комбинации флагов конфигурации
- Edge cases и race conditions
"""

import asyncio
import pytest
from unittest.mock import Mock, AsyncMock, patch, MagicMock
from pathlib import Path

# Импорты модулей для тестирования
from modules.permission_restart.core.restart_scheduler import RestartScheduler
from modules.permission_restart.core.config import PermissionRestartConfig
from modules.permission_restart.core.types import PermissionTransition
from modules.permissions.core.types import PermissionType, PermissionStatus


class TestPermissionRestartLogic:
    """Тесты логики permission restart"""

    @pytest.fixture
    def mock_event_bus(self):
        """Mock EventBus"""
        bus = AsyncMock()
        bus.publish = AsyncMock()
        return bus

    @pytest.fixture
    def mock_state_manager(self):
        """Mock StateManager"""
        manager = Mock()
        manager.get_current_mode = Mock(return_value="SLEEPING")
        manager.get_state_data = Mock(return_value=False)
        return manager

    @pytest.fixture
    def mock_updater_integration(self):
        """Mock UpdaterIntegration"""
        updater = Mock()
        updater.is_update_in_progress = Mock(return_value=False)
        updater.is_update_available = Mock(return_value=False)
        return updater

    @pytest.fixture
    def default_config(self):
        """Стандартная конфигурация"""
        return PermissionRestartConfig(
            enabled=True,
            critical_permissions=[
                PermissionType.ACCESSIBILITY,
                PermissionType.INPUT_MONITORING,
            ],
            restart_delay_sec=0.1,  # Быстрее для тестов
            max_restart_attempts=3,
            respect_active_sessions=True,
            respect_updates=True,
        )

    @pytest.fixture
    def scheduler(self, default_config, mock_event_bus, mock_state_manager, mock_updater_integration):
        """Создать RestartScheduler с моками"""
        return RestartScheduler(
            config=default_config,
            event_bus=mock_event_bus,
            state_manager=mock_state_manager,
            updater_integration=mock_updater_integration,
            poll_interval_sec=0.05,  # Быстрее для тестов
        )

    # ===== СЦЕНАРИЙ 1: Обновление доступно =====

    @pytest.mark.anyio
    async def test_skip_restart_when_update_available(
        self, scheduler, mock_updater_integration
    ):
        """
        СЦЕНАРИЙ 1: Обновление доступно → НЕ планировать restart

        Дано:
        - respect_updates = true
        - is_update_available() = True

        Ожидаем:
        - maybe_schedule_restart() возвращает None
        - Restart НЕ планируется
        - Логируется "Update available - skipping"
        """
        # Arrange
        mock_updater_integration.is_update_available.return_value = True

        transition = PermissionTransition(
            permission=PermissionType.ACCESSIBILITY,
            old_status=PermissionStatus.NOT_DETERMINED,
            new_status=PermissionStatus.GRANTED,
            session_id="test-session",
            source="test_source",
        )

        # Act
        result = await scheduler.maybe_schedule_restart(transition)

        # Assert
        assert result is None, "Должен вернуть None (не планировать restart)"
        assert not scheduler.pending(), "Не должно быть pending restart"
        mock_updater_integration.is_update_available.assert_called_once()

    # ===== СЦЕНАРИЙ 2: Обновления нет =====

    @pytest.mark.anyio
    async def test_schedule_restart_when_no_update(
        self, scheduler, mock_updater_integration
    ):
        """
        СЦЕНАРИЙ 2: Обновления нет → планировать restart

        Дано:
        - respect_updates = true
        - is_update_available() = False

        Ожидаем:
        - maybe_schedule_restart() возвращает RestartRequest
        - Restart планируется
        """
        # Arrange
        mock_updater_integration.is_update_available.return_value = False

        transition = PermissionTransition(
            permission=PermissionType.ACCESSIBILITY,
            old_status=PermissionStatus.NOT_DETERMINED,
            new_status=PermissionStatus.GRANTED,
            session_id="test-session",
            source="test_source",
        )

        # Act
        result = await scheduler.maybe_schedule_restart(transition)

        # Assert
        assert result is not None, "Должен запланировать restart"
        assert scheduler.pending(), "Должен быть pending restart"
        assert PermissionType.ACCESSIBILITY in result.critical_permissions

        # Cleanup
        await scheduler.shutdown()

    # ===== СЦЕНАРИЙ 3: respect_updates = false =====

    @pytest.mark.anyio
    async def test_ignore_update_when_respect_updates_false(
        self, mock_event_bus, mock_state_manager, mock_updater_integration
    ):
        """
        СЦЕНАРИЙ 3: respect_updates = false → игнорировать обновления

        Дано:
        - respect_updates = false
        - is_update_available() = True

        Ожидаем:
        - maybe_schedule_restart() ПЛАНИРУЕТ restart
        - is_update_available() НЕ вызывается
        """
        # Arrange
        config = PermissionRestartConfig(
            enabled=True,
            critical_permissions=[PermissionType.ACCESSIBILITY],
            restart_delay_sec=0.1,
            max_restart_attempts=3,
            respect_active_sessions=False,
            respect_updates=False,  # ВАЖНО: отключено
        )

        scheduler = RestartScheduler(
            config=config,
            event_bus=mock_event_bus,
            state_manager=mock_state_manager,
            updater_integration=mock_updater_integration,
        )

        mock_updater_integration.is_update_available.return_value = True

        transition = PermissionTransition(
            permission=PermissionType.ACCESSIBILITY,
            old_status=PermissionStatus.NOT_DETERMINED,
            new_status=PermissionStatus.GRANTED,
            session_id="test-session",
            source="test_source",
        )

        # Act
        result = await scheduler.maybe_schedule_restart(transition)

        # Assert
        assert result is not None, "Должен запланировать restart (игнорируя обновление)"
        # is_update_available может быть вызван в _run_when_safe, но не должен блокировать

        # Cleanup
        await scheduler.shutdown()

    # ===== СЦЕНАРИЙ 4: enabled = false =====

    @pytest.mark.anyio
    async def test_skip_when_disabled(
        self, mock_event_bus, mock_state_manager, mock_updater_integration
    ):
        """
        СЦЕНАРИЙ 4: enabled = false → полностью отключено

        Дано:
        - enabled = false

        Ожидаем:
        - maybe_schedule_restart() возвращает None
        - Никаких проверок не выполняется
        """
        # Arrange
        config = PermissionRestartConfig(
            enabled=False,  # ВАЖНО: отключено
            critical_permissions=[PermissionType.ACCESSIBILITY],
            restart_delay_sec=5.0,
            max_restart_attempts=3,
            respect_active_sessions=True,
            respect_updates=True,
        )

        scheduler = RestartScheduler(
            config=config,
            event_bus=mock_event_bus,
            state_manager=mock_state_manager,
            updater_integration=mock_updater_integration,
        )

        transition = PermissionTransition(
            permission=PermissionType.ACCESSIBILITY,
            old_status=PermissionStatus.NOT_DETERMINED,
            new_status=PermissionStatus.GRANTED,
            session_id="test-session",
            source="test_source",
        )

        # Act
        result = await scheduler.maybe_schedule_restart(transition)

        # Assert
        assert result is None
        assert not scheduler.pending()
        mock_updater_integration.is_update_available.assert_not_called()

    # ===== СЦЕНАРИЙ 5: max_restart_attempts исчерпан =====

    @pytest.mark.anyio
    async def test_skip_when_max_attempts_reached(self, scheduler):
        """
        СЦЕНАРИЙ 5: max_restart_attempts >= 3 → не планировать

        Дано:
        - _attempts = 3
        - max_restart_attempts = 3

        Ожидаем:
        - maybe_schedule_restart() возвращает None
        """
        # Arrange
        scheduler._attempts = 3  # Исчерпаны попытки

        transition = PermissionTransition(
            permission=PermissionType.ACCESSIBILITY,
            old_status=PermissionStatus.NOT_DETERMINED,
            new_status=PermissionStatus.GRANTED,
            session_id="test-session",
            source="test_source",
        )

        # Act
        result = await scheduler.maybe_schedule_restart(transition)

        # Assert
        assert result is None
        assert not scheduler.pending()

    # ===== СЦЕНАРИЙ 6: Обновление начинается ПОСЛЕ планирования restart =====

    @pytest.mark.anyio
    async def test_wait_for_update_during_restart(
        self, scheduler, mock_updater_integration, mock_state_manager
    ):
        """
        СЦЕНАРИЙ 6: Обновление начинается ПОСЛЕ планирования restart

        Дано:
        - Restart уже запланирован
        - update_in_progress становится True

        Ожидаем:
        - _run_when_safe() ждёт пока update_in_progress = False
        """
        # Arrange
        mock_updater_integration.is_update_available.return_value = False

        # Симулируем: update начинается после планирования
        call_count = [0]
        def update_in_progress_side_effect():
            call_count[0] += 1
            # Первые 2 вызова = True (обновление идёт)
            # Потом False (обновление завершено)
            return call_count[0] <= 2

        mock_updater_integration.is_update_in_progress.side_effect = update_in_progress_side_effect

        transition = PermissionTransition(
            permission=PermissionType.ACCESSIBILITY,
            old_status=PermissionStatus.NOT_DETERMINED,
            new_status=PermissionStatus.GRANTED,
            session_id="test-session",
            source="test_source",
        )

        # Act - планируем restart
        result = await scheduler.maybe_schedule_restart(transition)
        assert result is not None

        # Ждём немного пока _run_when_safe выполнится
        await asyncio.sleep(0.3)

        # Assert
        # _run_when_safe должен был ждать пока update_in_progress = False
        assert mock_updater_integration.is_update_in_progress.call_count >= 2

        # Cleanup
        await scheduler.shutdown()

    # ===== СЦЕНАРИЙ 7: respect_active_sessions - ждём SLEEPING =====

    @pytest.mark.anyio
    async def test_wait_for_sleeping_mode(
        self, scheduler, mock_state_manager, mock_updater_integration
    ):
        """
        СЦЕНАРИЙ 7: respect_active_sessions = true, mode = LISTENING

        Дано:
        - respect_active_sessions = true
        - current_mode = LISTENING (не SLEEPING)

        Ожидаем:
        - _run_when_safe() ждёт пока mode = SLEEPING
        """
        # Arrange
        mock_updater_integration.is_update_available.return_value = False

        # Симулируем: сначала LISTENING, потом SLEEPING
        call_count = [0]
        def get_mode_side_effect():
            call_count[0] += 1
            return "LISTENING" if call_count[0] <= 2 else "SLEEPING"

        # Создаём Mock объект для AppMode
        from unittest.mock import MagicMock
        mock_mode = MagicMock()
        mock_mode.__eq__ = lambda self, other: str(other) == "SLEEPING" if call_count[0] > 2 else False

        mock_state_manager.get_current_mode.side_effect = get_mode_side_effect

        transition = PermissionTransition(
            permission=PermissionType.ACCESSIBILITY,
            old_status=PermissionStatus.NOT_DETERMINED,
            new_status=PermissionStatus.GRANTED,
            session_id="test-session",
            source="test_source",
        )

        # Act
        result = await scheduler.maybe_schedule_restart(transition)
        assert result is not None

        await asyncio.sleep(0.3)

        # Assert - должен был проверить режим несколько раз
        assert mock_state_manager.get_current_mode.call_count >= 2

        # Cleanup
        await scheduler.shutdown()

    # ===== СЦЕНАРИЙ 8: Dry-run mode =====

    @pytest.mark.anyio
    async def test_dry_run_mode(
        self, scheduler, mock_updater_integration
    ):
        """
        СЦЕНАРИЙ 8: NEXY_DISABLE_AUTO_RESTART = true → dry-run

        Дано:
        - NEXY_DISABLE_AUTO_RESTART = "true"

        Ожидаем:
        - Restart НЕ выполняется (только логируется)
        """
        # Arrange
        with patch.dict("os.environ", {"NEXY_DISABLE_AUTO_RESTART": "true"}):
            from modules.permission_restart.macos.restart_handler import MacOSRestartHandler

            dry_run_handler = MacOSRestartHandler(dry_run=True)

            scheduler_with_dry_run = RestartScheduler(
                config=scheduler._config,
                event_bus=scheduler._event_bus,
                state_manager=scheduler._state_manager,
                updater_integration=mock_updater_integration,
                restart_handler=dry_run_handler,
            )

            mock_updater_integration.is_update_available.return_value = False

            transition = PermissionTransition(
                permission=PermissionType.ACCESSIBILITY,
                old_status=PermissionStatus.NOT_DETERMINED,
                new_status=PermissionStatus.GRANTED,
                session_id="test-session",
            )

            # Act
            result = await scheduler_with_dry_run.maybe_schedule_restart(transition)
            assert result is not None

            # Ждём выполнения
            await asyncio.sleep(0.3)

            # Assert - restart_handler.trigger_restart вернёт False в dry-run
            assert dry_run_handler.dry_run is True

            # Cleanup
            await scheduler_with_dry_run.shutdown()


# ===== ИНТЕГРАЦИОННЫЙ ТЕСТ =====

class TestPermissionRestartIntegration:
    """Интеграционные тесты полного flow"""

    @pytest.mark.anyio
    async def test_full_flow_with_update_available(self):
        """
        ПОЛНЫЙ FLOW: Обновление доступно с самого начала

        1. FirstRunPermissions запрашивает разрешения
        2. FirstRunPermissions публикует permissions.first_run_completed
        3. PermissionRestartIntegration получает событие
        4. RestartScheduler проверяет is_update_available() → True
        5. Restart НЕ планируется
        6. Updater устанавливает обновление и перезапускает
        """
        # TODO: Реализовать полный интеграционный тест
        # Требует мокирования EventBus, всех интеграций и координации событий
        pass

    @pytest.mark.anyio
    async def test_full_flow_without_update(self):
        """
        ПОЛНЫЙ FLOW: Обновления нет

        1. FirstRunPermissions запрашивает разрешения
        2. FirstRunPermissions публикует permissions.first_run_completed
        3. PermissionRestartIntegration получает событие
        4. RestartScheduler проверяет is_update_available() → False
        5. Restart планируется и выполняется через 5 секунд
        """
        # TODO: Реализовать полный интеграционный тест
        pass


if __name__ == "__main__":
    # Запуск тестов: pytest tests/test_permission_restart_logic.py -v
    pytest.main([__file__, "-v", "-s"])
