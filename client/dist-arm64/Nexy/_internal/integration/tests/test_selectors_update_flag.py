"""
Tests for is_update_in_progress selector.

Tests that the selector:
- Returns False by default
- Returns True when state_data is set
- Is resilient to exceptions
"""

import pytest
from unittest.mock import Mock, MagicMock

from integration.core.selectors import is_update_in_progress
from integration.core.state_manager import ApplicationStateManager


class TestIsUpdateInProgress:
    """Test is_update_in_progress selector."""

    def test_returns_false_by_default(self):
        """Test that selector returns False when state_data is not set."""
        state_manager = Mock(spec=ApplicationStateManager)
        state_manager.get_state_data = Mock(return_value=False)
        
        result = is_update_in_progress(state_manager)
        
        assert result is False
        state_manager.get_state_data.assert_called_once_with("update_in_progress", False)

    def test_returns_true_when_state_data_is_true(self):
        """Test that selector returns True when state_data is set to True."""
        state_manager = Mock(spec=ApplicationStateManager)
        state_manager.get_state_data = Mock(return_value=True)
        
        result = is_update_in_progress(state_manager)
        
        assert result is True
        state_manager.get_state_data.assert_called_once_with("update_in_progress", False)

    def test_handles_exception_gracefully(self):
        """Test that selector returns False when exception occurs."""
        state_manager = Mock(spec=ApplicationStateManager)
        state_manager.get_state_data = Mock(side_effect=Exception("State error"))
        
        result = is_update_in_progress(state_manager)
        
        assert result is False

    def test_handles_none_value(self):
        """Test that selector handles None value from state_data."""
        state_manager = Mock(spec=ApplicationStateManager)
        state_manager.get_state_data = Mock(return_value=None)
        
        result = is_update_in_progress(state_manager)
        
        assert result is False  # None is falsy

    def test_handles_string_true(self):
        """Test that selector handles string "true" value."""
        state_manager = Mock(spec=ApplicationStateManager)
        state_manager.get_state_data = Mock(return_value="true")
        
        result = is_update_in_progress(state_manager)
        
        assert result is True  # "true" is truthy

    def test_handles_numeric_one(self):
        """Test that selector handles numeric 1 value."""
        state_manager = Mock(spec=ApplicationStateManager)
        state_manager.get_state_data = Mock(return_value=1)
        
        result = is_update_in_progress(state_manager)
        
        assert result is True  # 1 is truthy




