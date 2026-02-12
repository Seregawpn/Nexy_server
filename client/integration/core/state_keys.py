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
    FIRST_RUN_RESTART_SCHEDULED = "first_run_restart_scheduled"
    
    # Input keys
    PTT_PRESSED = "ptt_pressed"
    
    # Update keys
    UPDATE_IN_PROGRESS = "update_in_progress"

    # App lifecycle keys
    USER_QUIT_INTENT = "user_quit_intent"
    
    # Whatsapp keys
    WHATSAPP_STATUS = "whatsapp.status"

    # Network keys
    NETWORK_STATUS = "network.status"
