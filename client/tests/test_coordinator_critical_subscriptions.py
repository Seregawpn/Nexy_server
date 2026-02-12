"""
Unit-тесты для проверки правильной последовательности инициализации координатора.

Тестирует исправление race condition в событиях разрешений:
- Подписки на критичные события должны быть настроены ДО инициализации интеграций
- Событие permissions.first_run_completed не должно теряться
"""

import asyncio
from unittest.mock import AsyncMock, Mock

import pytest

from integration.core.event_bus import EventBus, EventPriority
from integration.core.simple_module_coordinator import SimpleModuleCoordinator


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
        - permissions.changed
        """
        # Создаём mock EventBus
        coordinator.event_bus = Mock(spec=EventBus)
        coordinator.event_bus.subscribe = AsyncMock()
        
        # Вызываем метод настройки критичных подписок
        await coordinator._setup_critical_subscriptions()
        
        # Проверяем что все критичные события подписаны
        expected_events = [
            "permissions.first_run_started",
            "permissions.first_run_completed",
            "permissions.first_run_failed",
            "permissions.changed",
        ]
        
        subscribe_calls = coordinator.event_bus.subscribe.call_args_list
        subscribed_events = [call[0][0] for call in subscribe_calls]
        
        for event in expected_events:
            assert event in subscribed_events, \
                f"Event '{event}' not subscribed. Subscribed events: {subscribed_events}"
        
        # permissions.changed должен быть HIGH, чтобы не терять UX-обновления
        changed_call = next(
            (call for call in subscribe_calls if call[0][0] == "permissions.changed"),
            None
        )
        assert changed_call is not None, "permissions.changed not found in subscriptions"
        assert changed_call[0][2] == EventPriority.HIGH, \
            "permissions.changed must have HIGH priority"

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
            "permissions.changed": coordinator._on_permissions_changed,
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
        coordinator.state_manager.set_first_run_state = Mock()
        
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
        
        # КРИТИЧНО: StateManager должен быть обновлен после получения события
        coordinator.state_manager.set_first_run_state.assert_called_with(
            in_progress=False,
            required=False,
            completed=True,
        )

    @pytest.mark.asyncio
    async def test_legacy_restart_pending_not_subscribed(self, coordinator):
        """
        Тест: Legacy-событие permissions.first_run_restart_pending больше не подписывается.
        """
        coordinator.event_bus = EventBus()
        await coordinator._setup_critical_subscriptions()
        await asyncio.sleep(0.05)

        subscribed_events = [event for event in coordinator.event_bus.subscribers.keys()]
        assert "permissions.first_run_restart_pending" not in subscribed_events


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
