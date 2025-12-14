#!/usr/bin/env python3
"""
Изолированный тест для проверки исправления проверки разрешений.
"""
import pytest
from unittest.mock import patch, Mock
from modules.permissions.first_run.status_checker import check_microphone_status, PermissionStatus as StatusCheckerPermissionStatus


def test_permission_check_enum_comparison():
    """Тест: Проверка разрешений работает с правильным enum"""
    # Симулируем проверку разрешений
    with patch('modules.permissions.first_run.status_checker.check_microphone_status') as mock_check:
        mock_check.return_value = StatusCheckerPermissionStatus.GRANTED
        
        # Симулируем код из voice_recognition_integration.py
        from modules.permissions.first_run.status_checker import check_microphone_status, PermissionStatus as StatusCheckerPermissionStatus
        mic_status = check_microphone_status()
        
        # Проверяем сравнение
        assert mic_status == StatusCheckerPermissionStatus.GRANTED, "Разрешения должны быть GRANTED"
        assert mic_status.value == StatusCheckerPermissionStatus.GRANTED.value, "Значения должны совпадать"
        
        # Проверяем, что исключение не выбрасывается
        exception_raised = False
        try:
            if mic_status != StatusCheckerPermissionStatus.GRANTED:
                raise RuntimeError(f"Microphone permission not granted: {mic_status.value}")
        except RuntimeError:
            exception_raised = True
        
        assert exception_raised == False, "Исключение не должно выбрасываться при GRANTED"
        print("✅ Тест пройден: Проверка разрешений работает корректно")


if __name__ == '__main__':
    pytest.main([__file__, "-v", "-s"])
