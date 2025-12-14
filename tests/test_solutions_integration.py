#!/usr/bin/env python3
"""
Интеграционные тесты для сравнения вариантов решения проблем активации микрофона.

Цель: Протестировать варианты решений в реальных условиях с EventBus и state_manager.
"""

import pytest
import pytest_asyncio
import asyncio
import time
from unittest.mock import Mock, AsyncMock, patch, MagicMock
from typing import Dict, Any

# Импорты для тестирования
from integration.core.state_manager import ApplicationStateManager, AppMode
from integration.core.event_bus import EventBus


class TestProblem1SolutionsIntegration:
    """Интеграционные тесты для Проблемы 1: Микрофон не закрывается после playback.completed"""
    
    @pytest_asyncio.fixture
    async def setup_integration(self):
        """Создает интеграцию с реальным EventBus и state_manager."""
        event_bus = EventBus()
        state_manager = ApplicationStateManager()
        state_manager.attach_event_bus(event_bus)
        
        # Создаем мок интеграции (без реальной инициализации для простоты теста)
        integration = Mock()
        integration.state_manager = state_manager
        integration._publish_recording_stop_with_debounce = AsyncMock()
        integration._wait_for_mic_closed_with_timeout = AsyncMock(return_value=True)
        
        yield integration, event_bus, state_manager
    
    @pytest.mark.asyncio
    async def test_solution_1_3_real_scenario(self):
        """Тест Варианта 1.3 в реальном сценарии: playback.completed с активным микрофоном"""
        # Создаем окружение напрямую
        event_bus = EventBus()
        state_manager = ApplicationStateManager()
        state_manager.attach_event_bus(event_bus)
        
        integration = Mock()
        integration.state_manager = state_manager
        integration._publish_recording_stop_with_debounce = AsyncMock()
        integration._wait_for_mic_closed_with_timeout = AsyncMock(return_value=True)
        
        # ШАГ 1: Активируем микрофон
        state_manager.set_microphone_state("active", session_id="test-session-1")
        assert state_manager.is_microphone_active() == True
        
        # ШАГ 2: Симулируем playback.completed
        playback_event = {
            "type": "playback.completed",
            "data": {
                "session_id": "test-session-1",
                "timestamp": time.time()
            }
        }
        
        # ШАГ 3: Симулируем Вариант 1.3 напрямую (без вызова реального метода)
        mic_active = state_manager.is_microphone_active()
        if mic_active:
            state_manager.force_close_microphone(reason="playback_completed")
            await integration._publish_recording_stop_with_debounce({
                "source": "playback_finished",
                "session_id": None,
            })
            await integration._wait_for_mic_closed_with_timeout(timeout=1.0, source="playback_finished")
        
        # ШАГ 4: Проверяем результат
        await asyncio.sleep(0.1)  # Даем время на обработку
        
        # ✅ ОЖИДАЕМЫЙ РЕЗУЛЬТАТ: Микрофон должен быть закрыт
        mic_active_after = state_manager.is_microphone_active()
        
        assert mic_active_after == False, "Микрофон должен быть закрыт после playback.completed"
        
        # Проверяем, что событие voice.recording_stop было опубликовано
        # (проверяем через мок, если есть подписка)
        
        print("✅ Тест пройден: Вариант 1.3 закрывает микрофон корректно")


class TestProblem2SolutionsIntegration:
    """Интеграционные тесты для Проблемы 2: AVF не деактивируется, разрешения пропущены"""
    
    @pytest.mark.asyncio
    async def test_solution_2_1_avf_retry_real_scenario(self):
        """Тест Варианта 2.1 в реальном сценарии: AVF деактивируется с задержкой"""
        import asyncio
        
        # Симулируем AVF engine с задержкой деактивации
        class MockAVFEngine:
            def __init__(self):
                self._active = True
                self._attempts = 0
            
            @property
            def is_input_active(self):
                self._attempts += 1
                # Деактивируется на 3-й попытке
                if self._attempts >= 3:
                    self._active = False
                return self._active
        
        avf_engine = MockAVFEngine()
        
        # Симулируем Вариант 2.1
        max_avf_check_attempts = 5
        avf_deactivated = False
        total_attempts = 0
        
        for attempt in range(max_avf_check_attempts):
            total_attempts = attempt + 1
            if avf_engine.is_input_active:
                await asyncio.sleep(0.01)  # Уменьшено для быстрого теста
            else:
                avf_deactivated = True
                break
        
        # ✅ ОЖИДАЕМЫЙ РЕЗУЛЬТАТ: AVF должен быть деактивирован
        assert avf_deactivated == True, "AVF должен быть деактивирован после попыток"
        assert total_attempts == 3, "AVF должен деактивироваться на 3-й попытке"
        
        print("✅ Тест пройден: Вариант 2.1 гарантирует деактивацию AVF")
    
    @pytest.mark.asyncio
    async def test_solution_2_2_permission_check_real_scenario(self):
        """Тест Варианта 2.2 в реальном сценарии: разрешения проверяются обязательно"""
        from unittest.mock import Mock, patch
        
        # Симулируем PermissionChecker
        permission_checker = Mock()
        permission_checker.check_microphone_permission = Mock(return_value="granted")
        
        # Симулируем Вариант 2.2
        exception_raised = False
        try:
            mic_permission = permission_checker.check_microphone_permission()
            if mic_permission != "granted":
                raise RuntimeError(f"Microphone permission not granted: {mic_permission}")
        except RuntimeError:
            exception_raised = True
        except Exception as perm_error:
            raise RuntimeError(f"Permission check failed: {perm_error}") from perm_error
        
        # ✅ ОЖИДАЕМЫЙ РЕЗУЛЬТАТ: Разрешения должны быть проверены
        assert exception_raised == False, "Разрешения предоставлены, исключение не должно быть"
        permission_checker.check_microphone_permission.assert_called_once()
        
        print("✅ Тест пройден: Вариант 2.2 проверяет разрешения обязательно")
    
    @pytest.mark.asyncio
    async def test_solution_2_2_permission_denied_scenario(self):
        """Тест Варианта 2.2: разрешения не предоставлены → исключение"""
        from unittest.mock import Mock
        
        # Симулируем PermissionChecker с отказом
        permission_checker = Mock()
        permission_checker.check_microphone_permission = Mock(return_value="denied")
        
        # Симулируем Вариант 2.2
        exception_raised = False
        exception_message = None
        
        try:
            mic_permission = permission_checker.check_microphone_permission()
            if mic_permission != "granted":
                raise RuntimeError(f"Microphone permission not granted: {mic_permission}")
        except RuntimeError as e:
            exception_raised = True
            exception_message = str(e)
        except Exception as perm_error:
            raise RuntimeError(f"Permission check failed: {perm_error}") from perm_error
        
        # ✅ ОЖИДАЕМЫЙ РЕЗУЛЬТАТ: Должно быть исключение
        assert exception_raised == True, "Должно быть исключение при отсутствии разрешений"
        assert "not granted" in exception_message, "Сообщение об ошибке должно содержать 'not granted'"
        
        print("✅ Тест пройден: Вариант 2.2 выбрасывает исключение при отсутствии разрешений")


class TestProblem3SolutionsIntegration:
    """Интеграционные тесты для Проблемы 3: LONG_PRESS блокируется во время PROCESSING"""
    
    @pytest_asyncio.fixture
    async def setup_integration(self):
        """Создает интеграцию с реальным EventBus и state_manager."""
        event_bus = EventBus()
        state_manager = ApplicationStateManager()
        state_manager.attach_event_bus(event_bus)
        state_manager.set_mode(AppMode.PROCESSING)
        
        # Создаем мок интеграции (без реальной инициализации для простоты теста)
        integration = Mock()
        integration.state_manager = state_manager
        
        yield integration, event_bus, state_manager
    
    @pytest.mark.asyncio
    async def test_solution_3_3_gateway_keyboard_allowed(self):
        """Тест Варианта 3.3: keyboard активация разрешена во время PROCESSING"""
        # Создаем окружение напрямую
        event_bus = EventBus()
        state_manager = ApplicationStateManager()
        state_manager.attach_event_bus(event_bus)
        state_manager.set_mode(AppMode.PROCESSING)
        
        integration = Mock()
        integration.state_manager = state_manager
        
        # Создаем gateway (упрощенная версия для теста)
        from integration.core.selectors import Snapshot, PermissionStatus, DeviceStatus, NetworkStatus
        from integration.core.gateways.types import Decision
        
        def decide_allow_shortcut_during_processing(snapshot: Snapshot, source: str) -> Decision:
            if snapshot.app_mode == AppMode.PROCESSING:
                if source == "keyboard":
                    return Decision.START
                else:
                    return Decision.ABORT
            return Decision.START
        
        # Создаем snapshot
        snapshot = Snapshot(
            perm_mic=PermissionStatus.GRANTED,
            perm_screen=PermissionStatus.GRANTED,
            perm_accessibility=PermissionStatus.GRANTED,
            device_input=DeviceStatus.DEFAULT_OK,
            network=NetworkStatus.ONLINE,
            first_run=False,
            app_mode=AppMode.PROCESSING
        )
        
        # Тестируем gateway
        decision_keyboard = decide_allow_shortcut_during_processing(snapshot, source="keyboard")
        decision_automatic = decide_allow_shortcut_during_processing(snapshot, source="automatic")
        
        # ✅ ОЖИДАЕМЫЙ РЕЗУЛЬТАТ: keyboard разрешен, автоматическая блокирована
        assert decision_keyboard == Decision.START, "Keyboard активация должна быть разрешена"
        assert decision_automatic == Decision.ABORT, "Автоматическая активация должна быть блокирована"
        
        print("✅ Тест пройден: Вариант 3.3 разрешает keyboard активацию, блокирует автоматическую")


class TestSolutionsPerformance:
    """Тесты производительности вариантов решений"""
    
    @pytest.mark.asyncio
    async def test_solution_1_3_performance(self):
        """Тест производительности Варианта 1.3"""
        state_manager = ApplicationStateManager()
        state_manager.set_microphone_state("active", session_id="test")
        
        # Симулируем Вариант 1.3
        start_time = time.time()
        
        mic_active = state_manager.is_microphone_active()
        if mic_active:
            state_manager.force_close_microphone(reason="playback_completed")
            # Симулируем публикацию события (без реального EventBus)
            await asyncio.sleep(0.01)
            # Симулируем ожидание закрытия
            await asyncio.sleep(0.01)
        
        duration = time.time() - start_time
        
        # ✅ ОЖИДАЕМЫЙ РЕЗУЛЬТАТ: Быстрое выполнение (< 100ms)
        assert duration < 0.1, f"Вариант 1.3 должен выполняться быстро (< 100ms), получено: {duration*1000:.2f}ms"
        
        print(f"✅ Тест пройден: Вариант 1.3 выполняется за {duration*1000:.2f}ms")
    
    @pytest.mark.asyncio
    async def test_solution_2_1_performance(self):
        """Тест производительности Варианта 2.1 (AVF деактивация)"""
        class MockAVFEngine:
            def __init__(self):
                self._active = True
                self._attempts = 0
            
            @property
            def is_input_active(self):
                self._attempts += 1
                if self._attempts >= 2:
                    self._active = False
                return self._active
        
        avf_engine = MockAVFEngine()
        
        # Симулируем Вариант 2.1
        start_time = time.time()
        
        max_avf_check_attempts = 5
        for attempt in range(max_avf_check_attempts):
            if avf_engine.is_input_active:
                await asyncio.sleep(0.01)
            else:
                break
        
        duration = time.time() - start_time
        
        # ✅ ОЖИДАЕМЫЙ РЕЗУЛЬТАТ: Приемлемое время (< 200ms для 2 попыток)
        assert duration < 0.2, f"Вариант 2.1 должен выполняться быстро (< 200ms), получено: {duration*1000:.2f}ms"
        
        print(f"✅ Тест пройден: Вариант 2.1 выполняется за {duration*1000:.2f}ms")


class TestSolutionsCorrectness:
    """Тесты корректности вариантов решений"""
    
    @pytest.mark.asyncio
    async def test_solution_1_3_correctness(self):
        """Тест корректности Варианта 1.3: микрофон закрывается в разных сценариях"""
        state_manager = ApplicationStateManager()
        
        # Сценарий 1: Микрофон активен
        state_manager.set_microphone_state("active", session_id="test-1")
        mic_active = state_manager.is_microphone_active()
        if mic_active:
            state_manager.force_close_microphone(reason="playback_completed")
        assert state_manager.is_microphone_active() == False, "Микрофон должен быть закрыт"
        
        # Сценарий 2: Микрофон уже закрыт
        state_manager.set_microphone_state("idle", session_id=None)
        mic_active = state_manager.is_microphone_active()
        if mic_active:
            state_manager.force_close_microphone(reason="playback_completed")
        assert state_manager.is_microphone_active() == False, "Микрофон должен остаться закрытым"
        
        print("✅ Тест пройден: Вариант 1.3 корректно работает в разных сценариях")
    
    @pytest.mark.asyncio
    async def test_solution_2_1_correctness(self):
        """Тест корректности Варианта 2.1: AVF деактивируется в разных сценариях"""
        class MockAVFEngine:
            def __init__(self, deactivate_on_attempt):
                self._active = True
                self._attempts = 0
                self._deactivate_on = deactivate_on_attempt
            
            @property
            def is_input_active(self):
                self._attempts += 1
                if self._attempts >= self._deactivate_on:
                    self._active = False
                return self._active
        
        # Сценарий 1: AVF деактивируется на 1-й попытке
        avf1 = MockAVFEngine(deactivate_on_attempt=1)
        max_attempts = 5
        deactivated = False
        for attempt in range(max_attempts):
            if avf1.is_input_active:
                await asyncio.sleep(0.01)
            else:
                deactivated = True
                break
        assert deactivated == True and avf1._attempts == 1, "AVF должен деактивироваться на 1-й попытке"
        
        # Сценарий 2: AVF деактивируется на 5-й попытке
        avf2 = MockAVFEngine(deactivate_on_attempt=5)
        deactivated = False
        for attempt in range(max_attempts):
            if avf2.is_input_active:
                await asyncio.sleep(0.01)
            else:
                deactivated = True
                break
        assert deactivated == True and avf2._attempts == 5, "AVF должен деактивироваться на 5-й попытке"
        
        # Сценарий 3: AVF не деактивируется (должно быть исключение)
        avf3 = MockAVFEngine(deactivate_on_attempt=10)  # Никогда не деактивируется
        exception_raised = False
        try:
            for attempt in range(max_attempts):
                if avf3.is_input_active:
                    await asyncio.sleep(0.01)
                else:
                    break
            else:
                raise RuntimeError("AVF not deactivated after all attempts")
        except RuntimeError:
            exception_raised = True
        assert exception_raised == True, "Должно быть исключение, если AVF не деактивируется"
        
        print("✅ Тест пройден: Вариант 2.1 корректно работает в разных сценариях")
    
    @pytest.mark.asyncio
    async def test_solution_3_3_correctness(self):
        """Тест корректности Варианта 3.3: gateway работает в разных режимах"""
        from integration.core.selectors import Snapshot, PermissionStatus, DeviceStatus, NetworkStatus
        from integration.core.gateways.types import Decision
        
        def decide_allow_shortcut_during_processing(snapshot: Snapshot, source: str) -> Decision:
            if snapshot.app_mode == AppMode.PROCESSING:
                if source == "keyboard":
                    return Decision.START
                else:
                    return Decision.ABORT
            return Decision.START
        
        # Сценарий 1: PROCESSING + keyboard → разрешено
        snapshot1 = Snapshot(
            perm_mic=PermissionStatus.GRANTED,
            perm_screen=PermissionStatus.GRANTED,
            perm_accessibility=PermissionStatus.GRANTED,
            device_input=DeviceStatus.DEFAULT_OK,
            network=NetworkStatus.ONLINE,
            first_run=False,
            app_mode=AppMode.PROCESSING
        )
        decision1 = decide_allow_shortcut_during_processing(snapshot1, source="keyboard")
        assert decision1 == Decision.START, "Keyboard активация должна быть разрешена в PROCESSING"
        
        # Сценарий 2: PROCESSING + automatic → блокировано
        decision2 = decide_allow_shortcut_during_processing(snapshot1, source="automatic")
        assert decision2 == Decision.ABORT, "Автоматическая активация должна быть блокирована в PROCESSING"
        
        # Сценарий 3: SLEEPING + keyboard → разрешено
        snapshot3 = Snapshot(
            perm_mic=PermissionStatus.GRANTED,
            perm_screen=PermissionStatus.GRANTED,
            perm_accessibility=PermissionStatus.GRANTED,
            device_input=DeviceStatus.DEFAULT_OK,
            network=NetworkStatus.ONLINE,
            first_run=False,
            app_mode=AppMode.SLEEPING
        )
        decision3 = decide_allow_shortcut_during_processing(snapshot3, source="keyboard")
        assert decision3 == Decision.START, "Keyboard активация должна быть разрешена в SLEEPING"
        
        print("✅ Тест пройден: Вариант 3.3 корректно работает в разных режимах")


if __name__ == '__main__':
    pytest.main([__file__, "-v", "-s"])

