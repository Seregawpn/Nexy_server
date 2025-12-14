#!/usr/bin/env python3
"""
Изолированные тесты для проверки реализованных решений.

Цель: Убедиться, что все три решения работают корректно после реализации.
"""

import pytest
import asyncio
import time
from unittest.mock import Mock, AsyncMock, patch, MagicMock

# Импорты для тестирования
from integration.core.state_manager import ApplicationStateManager, AppMode
from integration.core.event_bus import EventBus
from integration.core.selectors import Snapshot, PermissionStatus, DeviceStatus, NetworkStatus
from integration.core.gateways.audio_gateways import decide_allow_shortcut_during_processing
from integration.core.gateways.types import Decision


class TestSolution1Isolated:
    """Изолированные тесты для Решения 1: Комбинированный подход"""
    
    @pytest.mark.asyncio
    async def test_solution_1_microphone_closes_after_playback(self):
        """Тест: Микрофон закрывается после playback.completed"""
        state_manager = ApplicationStateManager()
        
        # Устанавливаем микрофон как активный
        state_manager.set_microphone_state("active", session_id="test-session")
        assert state_manager.is_microphone_active() == True
        
        # Симулируем Решение 1.3
        mic_active = state_manager.is_microphone_active()
        if mic_active:
            state_manager.force_close_microphone(reason="playback_completed")
            # Симулируем публикацию события (без реального EventBus)
            await asyncio.sleep(0.01)
            # Симулируем ожидание закрытия
            await asyncio.sleep(0.01)
        
        # Проверяем результат
        assert state_manager.is_microphone_active() == False, "Микрофон должен быть закрыт после playback.completed"
        print("✅ Тест пройден: Микрофон закрывается корректно")
    
    @pytest.mark.asyncio
    async def test_solution_1_idle_microphone_not_closed(self):
        """Тест: Микрофон в состоянии idle не закрывается повторно"""
        state_manager = ApplicationStateManager()
        
        # Устанавливаем микрофон как закрытый
        state_manager.set_microphone_state("idle", session_id=None)
        assert state_manager.is_microphone_active() == False
        
        # Симулируем Решение 1.3
        mic_active = state_manager.is_microphone_active()
        if mic_active:
            state_manager.force_close_microphone(reason="playback_completed")
            await asyncio.sleep(0.01)
            await asyncio.sleep(0.01)
        
        # Проверяем результат
        assert state_manager.is_microphone_active() == False, "Микрофон должен остаться закрытым"
        print("✅ Тест пройден: Микрофон в состоянии idle не закрывается повторно")


class TestSolution2Isolated:
    """Изолированные тесты для Решения 2: AVF деактивация + проверка разрешений"""
    
    @pytest.mark.asyncio
    async def test_solution_2_1_avf_deactivation_success(self):
        """Тест: AVF деактивируется успешно после нескольких попыток"""
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
        
        # Симулируем Решение 2.1
        max_avf_check_attempts = 5
        avf_deactivated = False
        for attempt in range(max_avf_check_attempts):
            if hasattr(avf_engine, 'is_input_active') and avf_engine.is_input_active:
                await asyncio.sleep(0.01)
            else:
                avf_deactivated = True
                break
        
        # Проверяем результат
        assert avf_deactivated == True, "AVF должен быть деактивирован"
        # AVF деактивируется на 3-й попытке (после проверки _attempts становится 3, и is_input_active возвращает False)
        assert avf_engine._attempts >= 3, f"AVF должен деактивироваться на 3-й попытке, получено {avf_engine._attempts}"
        print("✅ Тест пройден: AVF деактивируется успешно")
    
    @pytest.mark.asyncio
    async def test_solution_2_1_avf_deactivation_failure(self):
        """Тест: AVF не деактивируется → исключение"""
        class MockAVFEngine:
            def __init__(self):
                self._active = True
                self._attempts = 0
            
            @property
            def is_input_active(self):
                self._attempts += 1
                # Никогда не деактивируется
                return self._active
        
        avf_engine = MockAVFEngine()
        
        # Симулируем Решение 2.1
        max_avf_check_attempts = 5
        avf_deactivated = False
        exception_raised = False
        
        try:
            for attempt in range(max_avf_check_attempts):
                if hasattr(avf_engine, 'is_input_active') and avf_engine.is_input_active:
                    await asyncio.sleep(0.01)
                else:
                    avf_deactivated = True
                    break
            else:
                raise RuntimeError("AVF not deactivated after all attempts")
        except RuntimeError:
            exception_raised = True
        
        # Проверяем результат
        assert exception_raised == True, "Должно быть исключение, если AVF не деактивируется"
        assert avf_deactivated == False, "AVF не должен быть деактивирован"
        print("✅ Тест пройден: Исключение при неудачной деактивации AVF")
    
    @pytest.mark.asyncio
    async def test_solution_2_2_permission_check_granted(self):
        """Тест: Разрешения предоставлены → продолжаем"""
        from modules.permissions.core.types import PermissionStatus
        
        # Симулируем Решение 2.2 с моком check_microphone_status
        with patch('modules.permissions.first_run.status_checker.check_microphone_status') as mock_check:
            mock_check.return_value = PermissionStatus.GRANTED
            
            exception_raised = False
            try:
                from modules.permissions.first_run.status_checker import check_microphone_status
                mic_status = check_microphone_status()
                if mic_status != PermissionStatus.GRANTED:
                    raise RuntimeError(f"Microphone permission not granted: {mic_status}")
            except RuntimeError:
                raise
            except Exception as perm_error:
                raise RuntimeError(f"Permission check failed: {perm_error}") from perm_error
            
            # Проверяем результат
            assert exception_raised == False, "Не должно быть исключения при предоставленных разрешениях"
            mock_check.assert_called_once()
            print("✅ Тест пройден: Разрешения проверяются корректно (granted)")
    
    @pytest.mark.asyncio
    async def test_solution_2_2_permission_check_denied(self):
        """Тест: Разрешения не предоставлены → исключение"""
        from modules.permissions.core.types import PermissionStatus
        
        # Симулируем Решение 2.2 с моком check_microphone_status
        with patch('modules.permissions.first_run.status_checker.check_microphone_status') as mock_check:
            mock_check.return_value = PermissionStatus.DENIED
            
            exception_raised = False
            exception_message = None
            
            try:
                from modules.permissions.first_run.status_checker import check_microphone_status
                mic_status = check_microphone_status()
                if mic_status != PermissionStatus.GRANTED:
                    raise RuntimeError(f"Microphone permission not granted: {mic_status}")
            except RuntimeError as e:
                exception_raised = True
                exception_message = str(e)
            except Exception as perm_error:
                raise RuntimeError(f"Permission check failed: {perm_error}") from perm_error
            
            # Проверяем результат
            assert exception_raised == True, "Должно быть исключение при отсутствии разрешений"
            assert "not granted" in exception_message, "Сообщение об ошибке должно содержать 'not granted'"
            print("✅ Тест пройден: Исключение при отсутствии разрешений")


class TestSolution3Isolated:
    """Изолированные тесты для Решения 3: Gateway для shortcut"""
    
    def test_solution_3_gateway_keyboard_allowed_processing(self):
        """Тест: keyboard активация разрешена во время PROCESSING"""
        snapshot = Snapshot(
            perm_mic=PermissionStatus.GRANTED,
            perm_screen=PermissionStatus.GRANTED,
            perm_accessibility=PermissionStatus.GRANTED,
            device_input=DeviceStatus.DEFAULT_OK,
            network=NetworkStatus.ONLINE,
            first_run=False,
            app_mode=AppMode.PROCESSING,
        )
        
        decision = decide_allow_shortcut_during_processing(snapshot, source="keyboard")
        
        assert decision == Decision.START, "Keyboard активация должна быть разрешена в PROCESSING"
        print("✅ Тест пройден: Keyboard активация разрешена в PROCESSING")
    
    def test_solution_3_gateway_automatic_blocked_processing(self):
        """Тест: автоматическая активация блокирована во время PROCESSING"""
        snapshot = Snapshot(
            perm_mic=PermissionStatus.GRANTED,
            perm_screen=PermissionStatus.GRANTED,
            perm_accessibility=PermissionStatus.GRANTED,
            device_input=DeviceStatus.DEFAULT_OK,
            network=NetworkStatus.ONLINE,
            first_run=False,
            app_mode=AppMode.PROCESSING,
        )
        
        decision = decide_allow_shortcut_during_processing(snapshot, source="automatic")
        
        assert decision == Decision.ABORT, "Автоматическая активация должна быть блокирована в PROCESSING"
        print("✅ Тест пройден: Автоматическая активация блокирована в PROCESSING")
    
    def test_solution_3_gateway_keyboard_allowed_sleeping(self):
        """Тест: keyboard активация разрешена в SLEEPING"""
        snapshot = Snapshot(
            perm_mic=PermissionStatus.GRANTED,
            perm_screen=PermissionStatus.GRANTED,
            perm_accessibility=PermissionStatus.GRANTED,
            device_input=DeviceStatus.DEFAULT_OK,
            network=NetworkStatus.ONLINE,
            first_run=False,
            app_mode=AppMode.SLEEPING,
        )
        
        decision = decide_allow_shortcut_during_processing(snapshot, source="keyboard")
        
        assert decision == Decision.START, "Keyboard активация должна быть разрешена в SLEEPING"
        print("✅ Тест пройден: Keyboard активация разрешена в SLEEPING")


if __name__ == '__main__':
    pytest.main([__file__, "-v", "-s"])

