"""
Unit тесты для ActionExecutor.

Feature ID: F-2025-016-mcp-app-opening-integration
"""

import asyncio
import pytest
from unittest.mock import AsyncMock, patch, MagicMock
from typing import Dict, Any

from modules.action_executor import ActionExecutor, ActionExecutorConfig, ActionResult


class TestActionExecutor:
    """Тесты для ActionExecutor."""

    def test_init(self):
        """Тест инициализации ActionExecutor."""
        config = ActionExecutorConfig(enabled=True, timeout_sec=5.0)
        executor = ActionExecutor(config)
        
        assert executor.is_enabled() is True
        assert executor._config.timeout_sec == 5.0
        assert executor._binary == "/usr/bin/open"

    def test_init_disabled(self):
        """Тест инициализации с disabled."""
        config = ActionExecutorConfig(enabled=False)
        executor = ActionExecutor(config)
        
        assert executor.is_enabled() is False

    def test_init_custom_binary(self):
        """Тест инициализации с кастомным binary."""
        config = ActionExecutorConfig(binary="/custom/path/open")
        executor = ActionExecutor(config)
        
        assert executor._binary == "/custom/path/open"

    def test_init_with_allowed_apps(self):
        """Тест инициализации с whitelist."""
        config = ActionExecutorConfig(allowed_apps=["Safari", "Calculator"])
        executor = ActionExecutor(config)
        
        assert "safari" in executor._allowed
        assert "calculator" in executor._allowed
        assert executor._allowed["safari"] == "Safari"

    @pytest.mark.asyncio
    async def test_execute_disabled(self):
        """Тест выполнения при disabled executor."""
        config = ActionExecutorConfig(enabled=False)
        executor = ActionExecutor(config)
        
        result = await executor.execute({"type": "open_app", "app_name": "Safari"})
        
        assert result.success is False
        assert result.error == "disabled"
        assert "disabled" in result.message.lower()

    @pytest.mark.asyncio
    async def test_execute_unsupported_action(self):
        """Тест выполнения неподдерживаемого типа действия."""
        config = ActionExecutorConfig(enabled=True)
        executor = ActionExecutor(config)
        
        result = await executor.execute({"type": "unknown_action"})
        
        assert result.success is False
        assert result.error == "unsupported_action"

    @pytest.mark.asyncio
    async def test_execute_missing_app_name_and_path(self):
        """Тест выполнения без app_name и app_path."""
        config = ActionExecutorConfig(enabled=True)
        executor = ActionExecutor(config)
        
        result = await executor.execute({"type": "open_app"})
        
        assert result.success is False
        assert result.error == "invalid_payload"

    @pytest.mark.asyncio
    async def test_execute_not_allowed_app(self):
        """Тест выполнения для приложения не из whitelist."""
        config = ActionExecutorConfig(
            enabled=True,
            allowed_apps=["Calculator"]
        )
        executor = ActionExecutor(config)
        
        result = await executor.execute({"type": "open_app", "app_name": "Safari"})
        
        assert result.success is False
        assert result.error == "not_allowed"
        assert "Safari" in result.message

    @pytest.mark.asyncio
    async def test_execute_allowed_app(self):
        """Тест выполнения для приложения из whitelist."""
        config = ActionExecutorConfig(
            enabled=True,
            allowed_apps=["Safari"]
        )
        executor = ActionExecutor(config)
        
        with patch('asyncio.create_subprocess_exec') as mock_subprocess:
            mock_process = AsyncMock()
            mock_process.communicate = AsyncMock(return_value=(b"", b""))
            mock_process.returncode = 0
            mock_subprocess.return_value = mock_process
            
            result = await executor.execute({"type": "open_app", "app_name": "Safari"})
            
            assert result.success is True
            assert "Safari" in result.message
            mock_subprocess.assert_called_once()
            args = mock_subprocess.call_args[0]
            assert args[0] == "/usr/bin/open"
            assert args[1] == "-a"
            assert args[2] == "Safari"

    @pytest.mark.asyncio
    async def test_execute_with_app_path(self):
        """Тест выполнения с app_path."""
        config = ActionExecutorConfig(enabled=True)
        executor = ActionExecutor(config)
        
        with patch('asyncio.create_subprocess_exec') as mock_subprocess:
            mock_process = AsyncMock()
            mock_process.communicate = AsyncMock(return_value=(b"", b""))
            mock_process.returncode = 0
            mock_subprocess.return_value = mock_process
            
            result = await executor.execute({
                "type": "open_app",
                "app_path": "/Applications/Safari.app"
            })
            
            assert result.success is True
            mock_subprocess.assert_called_once()
            args = mock_subprocess.call_args[0]
            assert args[0] == "/usr/bin/open"
            assert args[1] == "/Applications/Safari.app"

    @pytest.mark.asyncio
    async def test_execute_timeout(self):
        """Тест таймаута выполнения."""
        config = ActionExecutorConfig(enabled=True, timeout_sec=0.1)
        executor = ActionExecutor(config)
        
        with patch('asyncio.create_subprocess_exec') as mock_subprocess:
            mock_process = AsyncMock()
            # asyncio.wait_for оборачивает communicate, поэтому нужно замокать wait_for
            async def slow_communicate():
                await asyncio.sleep(1.0)  # Дольше чем timeout
                return (b"", b"")
            mock_process.communicate = slow_communicate
            mock_process.kill = MagicMock()
            mock_subprocess.return_value = mock_process
            
            result = await executor.execute({"type": "open_app", "app_name": "Safari"})
            
            assert result.success is False
            assert result.error == "timeout"
            mock_process.kill.assert_called_once()

    @pytest.mark.asyncio
    async def test_execute_command_failed(self):
        """Тест неудачного выполнения команды."""
        config = ActionExecutorConfig(enabled=True)
        executor = ActionExecutor(config)
        
        with patch('asyncio.create_subprocess_exec') as mock_subprocess:
            mock_process = AsyncMock()
            mock_process.communicate = AsyncMock(return_value=(b"", b"Error message"))
            mock_process.returncode = 1
            mock_subprocess.return_value = mock_process
            
            result = await executor.execute({"type": "open_app", "app_name": "Safari"})
            
            assert result.success is False
            assert result.error == "command_failed"

    @pytest.mark.asyncio
    async def test_execute_binary_not_found(self):
        """Тест отсутствия binary."""
        config = ActionExecutorConfig(enabled=True, binary="/nonexistent/open")
        executor = ActionExecutor(config)
        
        with patch('os.path.exists', return_value=False):
            result = await executor.execute({"type": "open_app", "app_name": "Safari"})
            
            assert result.success is False
            assert result.error == "binary_missing"

    def test_normalize_app_name(self):
        """Тест нормализации имени приложения."""
        config = ActionExecutorConfig()
        executor = ActionExecutor(config)
        
        assert executor._normalize_app_name("Safari") == "Safari"
        assert executor._normalize_app_name("Safari.app") == "Safari"
        assert executor._normalize_app_name("  Safari  ") == "Safari"
        assert executor._normalize_app_name(None) is None
        assert executor._normalize_app_name("") is None

    def test_normalize_path(self):
        """Тест нормализации пути."""
        config = ActionExecutorConfig()
        executor = ActionExecutor(config)
        
        assert executor._normalize_path("/Applications/Safari.app") == "/Applications/Safari.app"
        assert executor._normalize_path("  /path/to/app  ") == "/path/to/app"
        assert executor._normalize_path(None) is None
        assert executor._normalize_path("") is None

    @pytest.mark.asyncio
    async def test_build_command_with_app_name(self):
        """Тест формирования команды с app_name."""
        config = ActionExecutorConfig()
        executor = ActionExecutor(config)
        
        with patch('os.path.exists', return_value=True):
            cmd = await executor._build_command(app_name="Safari", app_path=None)
            
            assert cmd == ["/usr/bin/open", "-a", "Safari"]

    @pytest.mark.asyncio
    async def test_build_command_with_app_path(self):
        """Тест формирования команды с app_path."""
        config = ActionExecutorConfig()
        executor = ActionExecutor(config)
        
        with patch('os.path.exists', return_value=True):
            cmd = await executor._build_command(
                app_name=None,
                app_path="/Applications/Safari.app"
            )
            
            assert cmd == ["/usr/bin/open", "/Applications/Safari.app"]

    @pytest.mark.asyncio
    async def test_build_command_binary_not_found(self):
        """Тест формирования команды при отсутствии binary."""
        config = ActionExecutorConfig(binary="/nonexistent/open")
        executor = ActionExecutor(config)
        
        with patch('os.path.exists', return_value=False):
            cmd = await executor._build_command(app_name="Safari", app_path=None)
            
            assert cmd is None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

