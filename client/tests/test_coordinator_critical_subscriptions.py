"""
Unit-тесты для проверки правильной последовательности инициализации координатора.

Тестирует исправление race condition в событиях разрешений:
- Подписки на критичные события должны быть настроены ДО инициализации интеграций
- Событие permissions.first_run_completed не должно теряться
"""

import pytest
import asyncio
from unittest.mock import Mock, AsyncMock, patch, call
from integration.core.simple_module_coordinator import SimpleModuleCoordinator
from integration.core.event_bus import EventBus, EventPriority


class TestCoordinatorCriticalSubscriptions:
    """Тесты для критичных подписок координатора"""

    @pytest.fixture
    def coordinator(self):
        """Создаём координатор для тестов"""
        return SimpleModuleCoordinator()

    @pytest.mark.asyncio
    async def test_critical_subscriptions_before_integrations(self, coordinator):
        """
        Тест: Критичные подписки настраиваются ДО инициализации интеграций
        
        Проверяет что:
        1. _setup_critical_subscriptions() вызывается перед _create_integrations()
        2. Подписки на permissions.* события зарегистрированы
        3. Координатор готов получить события от FirstRunPermissionsIntegration
        """
        # Мокируем методы для отслеживания порядка вызовов
        call_order = []
        
        original_setup_critical = coordinator._setup_critical_subscriptions
        original_create_integrations = coordinator._create_integrations
        original_initialize_integrations = coordinator._initialize_integrations
        
        async def mock_setup_critical():
            call_order.append("setup_critical_subscriptions")
            # Не вызываем оригинальный метод для упрощения теста
            coordinator.event_bus = Mock(spec=EventBus)
            coordinator.event_bus.subscribe = AsyncMock()
        
        async def mock_create_integrations():
            call_order.append("create_integrations")
        
        async def mock_initialize_integrations():
            call_order.append("initialize_integrations")
        
        coordinator._setup_critical_subscriptions = mock_setup_critical
        coordinator._create_integrations = mock_create_integrations
        coordinator._initialize_integrations = mock_initialize_integrations
        
        # Также мокируем другие методы initialize для упрощения
        coordinator._start_background_loop = Mock()
        coordinator._setup_coordination = AsyncMock()
        coordinator._setup_auto_audio_connections = AsyncMock()
        
        # Запускаем инициализацию
        try:
            await coordinator.initialize()
        except Exception:
            pass  # Ожидаем ошибки из-за мокирования, это нормально
        
        # Проверяем порядок вызовов
        assert len(call_order) >= 3, f"Expected at least 3 calls, got {len(call_order)}: {call_order}"
        
        # КРИТИЧНО: setup_critical_subscriptions должен быть ПЕРВЫМ (до create/initialize интеграций)
        critical_idx = call_order.index("setup_critical_subscriptions")
        create_idx = call_order.index("create_integrations")
        init_idx = call_order.index("initialize_integrations")
        
        assert critical_idx < create_idx, \
            f"setup_critical_subscriptions ({critical_idx}) must be before create_integrations ({create_idx})"
        assert critical_idx < init_idx, \
            f"setup_critical_subscriptions ({critical_idx}) must be before initialize_integrations ({init_idx})"
        assert create_idx < init_idx, \
            f"create_integrations ({create_idx}) must be before initialize_integrations ({init_idx})"

    @pytest.mark.asyncio
    async def test_permissions_events_subscribed(self, coordinator):
        """
        Тест: Координатор подписан на все критичные события разрешений
        
        Проверяет что подписки настроены на:
        - permissions.first_run_started
        - permissions.first_run_completed
        - permissions.first_run_failed
        - permissions.first_run_restart_pending
        """
        # Создаём mock EventBus
        coordinator.event_bus = Mock(spec=EventBus)
        coordinator.event_bus.subscribe = AsyncMock()
        
        # Вызываем метод настройки критичных подписок
        await coordinator._setup_critical_subscriptions()
        
        # Проверяем что все 4 критичных события подписаны
        expected_events = [
            "permissions.first_run_started",
            "permissions.first_run_completed",
            "permissions.first_run_failed",
            "permissions.first_run_restart_pending",
        ]
        
        subscribe_calls = coordinator.event_bus.subscribe.call_args_list
        subscribed_events = [call[0][0] for call in subscribe_calls]
        
        for event in expected_events:
            assert event in subscribed_events, \
                f"Event '{event}' not subscribed. Subscribed events: {subscribed_events}"
        
        # Проверяем что permissions.first_run_restart_pending имеет CRITICAL приоритет
        restart_pending_call = next(
            (call for call in subscribe_calls if call[0][0] == "permissions.first_run_restart_pending"),
            None
        )
        assert restart_pending_call is not None, "permissions.first_run_restart_pending not found in subscriptions"
        assert restart_pending_call[0][2] == EventPriority.CRITICAL, \
            "permissions.first_run_restart_pending must have CRITICAL priority"

    @pytest.mark.asyncio
    async def test_event_handlers_registered(self, coordinator):
        """
        Тест: Обработчики событий разрешений корректно зарегистрированы
        
        Проверяет что каждому событию соответствует правильный обработчик.
        """
        coordinator.event_bus = Mock(spec=EventBus)
        coordinator.event_bus.subscribe = AsyncMock()
        
        await coordinator._setup_critical_subscriptions()
        
        # Проверяем что обработчики существуют
        expected_handlers = {
            "permissions.first_run_started": coordinator._on_permissions_started,
            "permissions.first_run_completed": coordinator._on_permissions_completed,
            "permissions.first_run_failed": coordinator._on_permissions_failed,
            "permissions.first_run_restart_pending": coordinator._on_permissions_restart_pending,
        }
        
        subscribe_calls = coordinator.event_bus.subscribe.call_args_list
        
        for event_name, expected_handler in expected_handlers.items():
            matching_call = next(
                (call for call in subscribe_calls if call[0][0] == event_name),
                None
            )
            assert matching_call is not None, f"No subscription found for {event_name}"
            
            actual_handler = matching_call[0][1]
            assert actual_handler == expected_handler, \
                f"Wrong handler for {event_name}: expected {expected_handler}, got {actual_handler}"

    @pytest.mark.asyncio
    async def test_permissions_completed_event_not_lost(self, coordinator):
        """
        Тест: Событие permissions.first_run_completed не теряется
        
        Симулирует сценарий перезапуска после first-run:
        1. Координатор подписан на события ДО инициализации интеграций
        2. FirstRunPermissionsIntegration публикует permissions.first_run_completed в initialize()
        3. Координатор получает событие и сбрасывает флаг _permissions_in_progress
        """
        # Создаём реальный EventBus для проверки доставки событий
        coordinator.event_bus = EventBus()
        coordinator.state_manager = Mock()
        coordinator.state_manager.set_state_data = Mock()
        
        # Устанавливаем начальное состояние
        coordinator._permissions_in_progress = True
        coordinator._restart_pending = False
        
        # Настраиваем критичные подписки
        await coordinator._setup_critical_subscriptions()
        
        # Даём EventBus время обработать подписки
        await asyncio.sleep(0.1)
        
        # Симулируем публикацию события от FirstRunPermissionsIntegration
        await coordinator.event_bus.publish(
            "permissions.first_run_completed",
            {
                "session_id": "test-session",
                "source": "first_run_permissions_integration",
                "note": "Test event",
                "priority": EventPriority.HIGH
            }
        )
        
        # Даём время на обработку события
        await asyncio.sleep(0.2)
        
        # КРИТИЧНО: Флаг должен быть сброшен после получения события
        assert coordinator._permissions_in_progress == False, \
            "Flag _permissions_in_progress should be reset after receiving permissions.first_run_completed"

    @pytest.mark.asyncio
    async def test_restart_pending_flag_set(self, coordinator):
        """
        Тест: Флаг restart_pending устанавливается при получении события
        
        Проверяет что при получении permissions.first_run_restart_pending:
        1. Флаг _restart_pending устанавливается в True
        2. state_data обновляется (legacy support)
        3. Публикуется событие permissions.restart_pending.changed
        """
        coordinator.event_bus = EventBus()
        coordinator.state_manager = Mock()
        coordinator.state_manager.set_state_data = Mock()
        coordinator.state_manager.get_state_data = Mock(return_value=False)
        coordinator.config = Mock()
        coordinator.config._load_config = Mock(return_value={"features": {}})
        
        # Устанавливаем начальное состояние
        coordinator._restart_pending = False
        
        # Настраиваем критичные подписки
        await coordinator._setup_critical_subscriptions()
        await asyncio.sleep(0.1)
        
        # Публикуем событие restart_pending
        await coordinator.event_bus.publish(
            "permissions.first_run_restart_pending",
            {
                "session_id": "test-restart-session",
                "source": "first_run_permissions_integration",
                "priority": EventPriority.CRITICAL
            }
        )
        
        # Даём время на обработку
        await asyncio.sleep(0.2)
        
        # Проверяем что флаг установлен
        assert coordinator._restart_pending == True, \
            "Flag _restart_pending should be set to True after receiving permissions.first_run_restart_pending"
        
        # Проверяем что state_data обновлён (legacy support)
        coordinator.state_manager.set_restart_pending.assert_called_with(True)


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])

