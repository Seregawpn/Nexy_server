"""
Тесты для проверки порядка приоритетов механизма перезапуска.

Проверяем что:
- PRIORITY 1: open -n -a (packaged .app) используется первым
- PRIORITY 2: os.execve() используется как fallback
- PRIORITY 3: dev fallback используется только в dev-режиме
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
from pathlib import Path
import sys
import os
import logging

from modules.permission_restart.macos.permissions_restart_handler import (
    PermissionsRestartHandler,
)
from modules.permission_restart.core.config import PermissionRestartConfig


class TestRestartPriorityOrder:
    """Тесты порядка приоритетов перезапуска"""

    @pytest.fixture
    def handler_config(self):
        """Базовая конфигурация для handler"""
        return PermissionRestartConfig(
            handler_launch_delay_ms=100,
            packaged_launch_grace_ms=100,
            graceful_shutdown_timeout_sec=1.0,
            graceful_shutdown_poll_interval_sec=0.1,
        )

    @pytest.fixture
    def handler(self, handler_config):
        """Создать handler с моками"""
        with patch("modules.permission_restart.macos.permissions_restart_handler.get_user_cache_dir") as mock_cache:
            mock_cache.return_value = Path("/tmp/test_cache")
            handler = PermissionsRestartHandler(config=handler_config, dry_run=True)
            return handler

    def test_priority_1_packaged_app_first(self, handler):
        """
        PRIORITY 1: _launch_packaged_app() вызывается первым
        
        Дано:
        - packaged .app доступен
        - _packaged_unavailable = False
        
        Ожидаем:
        - _launch_packaged_app() вызывается первым
        - _exec_current_bundle() НЕ вызывается
        """
        # Arrange
        handler._packaged_unavailable = False
        handler._last_reason = "test_reason"
        handler._last_permissions = ("microphone",)
        
        with patch.object(handler, "_launch_packaged_app", return_value=True) as mock_launch:
            with patch.object(handler, "_exec_current_bundle", return_value=False) as mock_exec:
                with patch("os._exit") as mock_exit:
                    # Act
                    handler._perform_restart()
                    
                    # Assert
                    mock_launch.assert_called_once()
                    mock_exec.assert_not_called()
                    mock_exit.assert_called_once_with(0)

    def test_priority_2_execve_fallback(self, handler):
        """
        PRIORITY 2: _exec_current_bundle() используется как fallback
        
        Дано:
        - packaged .app недоступен (_packaged_unavailable = True)
        - sys.frozen = True (PyInstaller bundle)
        
        Ожидаем:
        - _launch_packaged_app() НЕ вызывается (уже помечен как unavailable)
        - _exec_current_bundle() вызывается как fallback
        """
        # Arrange
        handler._packaged_unavailable = True
        handler._last_reason = "test_reason"
        handler._last_permissions = ("microphone",)
        
        with patch.object(sys, 'frozen', True, create=True):
            with patch.object(handler, "_launch_packaged_app", return_value=False) as mock_launch:
                with patch.object(handler, "_exec_current_bundle", return_value=True) as mock_exec:
                    # Act
                    handler._perform_restart()
                    
                    # Assert
                    mock_launch.assert_not_called()
                    mock_exec.assert_called_once()

    def test_priority_3_dev_fallback(self, handler):
        """
        PRIORITY 3: dev fallback используется только в dev-режиме
        
        Дано:
        - packaged .app недоступен
        - sys.frozen = False (dev-режим)
        - _allow_dev_fallback = True
        
        Ожидаем:
        - _launch_dev_process() вызывается
        - _exec_current_bundle() НЕ вызывается (не frozen)
        """
        # Arrange
        handler._packaged_unavailable = True
        handler._allow_dev_fallback = True
        handler._last_reason = "test_reason"
        handler._last_permissions = ("microphone",)
        
        with patch.object(sys, 'frozen', False, create=True):
            with patch.object(handler, "_launch_packaged_app", return_value=False) as mock_launch:
                with patch.object(handler, "_exec_current_bundle", return_value=False) as mock_exec:
                    with patch.object(handler, "_launch_dev_process") as mock_dev:
                        with patch("time.sleep") as mock_sleep:
                            with patch("os._exit") as mock_exit:
                                # Act
                                handler._perform_restart()
                                
                                # Assert
                                mock_launch.assert_not_called()
                                mock_exec.assert_not_called()
                                mock_dev.assert_called_once()
                                mock_sleep.assert_called_once()
                                mock_exit.assert_called_once_with(0)

    def test_packaged_app_unavailable_marks_flag(self, handler):
        """
        Проверка что _packaged_unavailable устанавливается при неудаче
        
        Дано:
        - packaged .app недоступен (метод возвращает False)
        
        Ожидаем:
        - _packaged_unavailable устанавливается в True
        - Логируется сообщение о fallback на execve
        """
        # Arrange
        handler._packaged_unavailable = False
        handler._last_reason = "test_reason"
        handler._last_permissions = ("microphone",)
        
        with patch.object(handler, "_derive_bundle_path", return_value=Path("/Applications/Nexy.app")):
            with patch.object(handler, "_launch_packaged_app", return_value=False) as mock_launch:
                with patch.object(sys, 'frozen', True, create=True):
                    with patch.object(handler, "_exec_current_bundle", return_value=True) as mock_exec:
                        # Act
                        handler._perform_restart()
                        
                        # Assert
                        assert handler._packaged_unavailable is True
                        mock_launch.assert_called_once()
                        mock_exec.assert_called_once()

    def test_all_methods_fail_aborts_restart(self, handler):
        """
        Проверка что при неудаче всех методов перезапуск прерывается
        
        Дано:
        - packaged .app недоступен
        - execve недоступен (не frozen)
        - dev fallback отключен
        
        Ожидаем:
        - Логируется ошибка
        - os._exit() НЕ вызывается
        """
        # Arrange
        handler._packaged_unavailable = True
        handler._allow_dev_fallback = False
        handler._last_reason = "test_reason"
        handler._last_permissions = ("microphone",)
        
        with patch.object(sys, 'frozen', False, create=True):
            with patch.object(handler, "_launch_packaged_app", return_value=False):
                with patch.object(handler, "_exec_current_bundle", return_value=False):
                    with patch("os._exit") as mock_exit:
                        # Act
                        handler._perform_restart()
                        
                        # Assert
                        mock_exit.assert_not_called()

    def test_log_messages_reflect_priority(self, handler, caplog):
        """
        Проверка что логи отражают правильный порядок приоритетов
        
        Дано:
        - packaged .app доступен
        
        Ожидаем:
        - Лог содержит "full restart" (PRIORITY 1)
        - НЕТ логов о "execve fallback" или "dev fallback"
        """
        # Arrange
        handler._packaged_unavailable = False
        handler._last_reason = "test_reason"
        handler._last_permissions = ("microphone",)
        
        with caplog.at_level(logging.INFO):
            with patch.object(handler, "_launch_packaged_app", return_value=True):
                with patch("os._exit"):
                    # Act
                    handler._perform_restart()
                    
                    # Assert
                    logs = caplog.text
                    assert "full restart" in logs.lower() or "packaged app launch verified" in logs.lower()
                    assert "execve fallback" not in logs.lower()
                    assert "dev fallback" not in logs.lower()

    def test_execve_fallback_logged_when_packaged_unavailable(self, handler, caplog):
        """
        Проверка что логируется fallback на execve когда packaged .app недоступен
        
        Дано:
        - packaged .app недоступен
        
        Ожидаем:
        - Лог содержит "execve fallback"
        """
        # Arrange
        handler._packaged_unavailable = False
        handler._last_reason = "test_reason"
        handler._last_permissions = ("microphone",)
        
        with caplog.at_level(logging.INFO):
            with patch.object(handler, "_derive_bundle_path", return_value=Path("/Applications/Nexy.app")):
                with patch.object(handler, "_launch_packaged_app", return_value=False):
                    with patch.object(sys, 'frozen', True, create=True):
                        with patch.object(handler, "_exec_current_bundle", return_value=True):
                            # Act
                            handler._perform_restart()
                            
                            # Assert
                            logs = caplog.text
                            assert "execve fallback" in logs.lower() or "will use execve fallback" in logs.lower()


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])

