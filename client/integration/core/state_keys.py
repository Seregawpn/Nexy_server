"""
StateManager Key Constants

This module provides centralized constants for all StateManager keys
to prevent typos and ensure consistency across the codebase.

Usage:
    from integration.core.state_keys import StateKeys
    
    # Get state
    value = state_manager.get_state_data(StateKeys.FIRST_RUN_IN_PROGRESS, False)
    
    # Set state
    state_manager.set_state_data(StateKeys.PTT_PRESSED, True)
"""


class StateKeys:
    """Constants for StateManager key names."""
    
    # First-run flow keys
    FIRST_RUN_IN_PROGRESS = "first_run_in_progress"
    FIRST_RUN_REQUIRED = "first_run_required"
    FIRST_RUN_COMPLETED = "first_run_completed"
    
    # Permission keys
    PERMISSIONS_RESTART_PENDING = "permissions_restart_pending"
    PERMISSIONS_RESTART_COMPLETED_FALLBACK = "permissions_restart_completed_fallback"
    
    # Input keys
    PTT_PRESSED = "ptt_pressed"
    
    # Update keys
    UPDATE_IN_PROGRESS = "update_in_progress"
    
    # Whatsapp keys
    WHATSAPP_STATUS = "whatsapp.status"

    # Network keys
    NETWORK_STATUS = "network.status"
