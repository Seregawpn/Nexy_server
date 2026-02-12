"""
EventBus Event Type Constants

This module provides centralized constants for all EventBus event types
to prevent typos and ensure consistency across the codebase.

Usage:
    from integration.core.event_types import EventTypes

    # Subscribe
    await event_bus.subscribe(EventTypes.APP_STARTUP, handler)

    # Publish
    await event_bus.publish(EventTypes.APP_MODE_CHANGED, {"mode": new_mode})
"""


class EventTypes:
    """Constants for EventBus event type names."""

    # ==================== Application Lifecycle ====================
    APP_STARTUP = "app.startup"
    APP_SHUTDOWN = "app.shutdown"
    APP_MODE_CHANGED = "app.mode_changed"
    APP_STATE_CHANGED = "app.state_changed"

    # ==================== Mode Management ====================
    MODE_REQUEST = "mode.request"
    PROCESSING_TERMINAL = "processing.terminal"

    # ==================== Voice & Recording ====================
    VOICE_RECORDING_START = "voice.recording_start"
    VOICE_RECORDING_STOP = "voice.recording_stop"
    VOICE_MIC_OPENED = "voice.mic_opened"
    VOICE_MIC_CLOSED = "voice.mic_closed"
    VOICE_RECOGNITION_STARTED = "voice.recognition_started"
    VOICE_RECOGNITION_COMPLETED = "voice.recognition_completed"
    VOICE_RECOGNITION_FAILED = "voice.recognition_failed"
    VOICE_RECOGNITION_TIMEOUT = "voice.recognition_timeout"

    # ==================== Keyboard Input ====================
    KEYBOARD_PRESS = "keyboard.press"
    KEYBOARD_SHORT_PRESS = "keyboard.short_press"

    # ==================== gRPC Communication ====================
    GRPC_REQUEST_COMPLETED = "grpc.request_completed"
    GRPC_REQUEST_FAILED = "grpc.request_failed"
    GRPC_REQUEST_CANCEL = "grpc.request_cancel"
    GRPC_TTS_REQUEST = "grpc.tts_request"

    # ==================== Audio Playback ====================
    PLAYBACK_STARTED = "playback.started"
    PLAYBACK_COMPLETED = "playback.completed"
    PLAYBACK_CANCELLED = "playback.cancelled"
    PLAYBACK_FAILED = "playback.failed"
    PLAYBACK_SIGNAL = "playback.signal"
    PLAYBACK_RAW_AUDIO = "playback.raw_audio"

    # ==================== Screenshot ====================
    SCREENSHOT_CAPTURED = "screenshot.captured"
    SCREENSHOT_ERROR = "screenshot.error"

    # ==================== Permissions ====================
    PERMISSIONS_CHANGED = "permissions.changed"
    PERMISSIONS_CHECK_REQUIRED = "permissions.check_required"
    PERMISSIONS_REQUESTED = "permissions.requested"
    PERMISSIONS_STATUS_CHECKED = "permissions.status_checked"
    PERMISSIONS_INTEGRATION_READY = "permissions.integration_ready"
    PERMISSIONS_FIRST_RUN_STARTED = "permissions.first_run_started"
    PERMISSIONS_FIRST_RUN_COMPLETED = "permissions.first_run_completed"
    PERMISSIONS_FIRST_RUN_FAILED = "permissions.first_run_failed"
    PERMISSIONS_FIRST_RUN_RESTART_PENDING = "permissions.first_run_restart_pending"

    # ==================== System ====================
    SYSTEM_PERMISSIONS_READY = "system.permissions_ready"
    SYSTEM_READY_TO_GREET = "system.ready_to_greet"
    SYSTEM_NOTIFICATION = "system.notification"

    # ==================== Tray ====================
    TRAY_STATUS_UPDATED = "tray.status_updated"
    TRAY_QUIT_CLICKED = "tray.quit_clicked"
    TRAY_INTEGRATION_READY = "tray.integration_ready"

    # ==================== Updater ====================
    UPDATER_UPDATE_STARTED = "updater.update_started"
    UPDATER_UPDATE_COMPLETED = "updater.update_completed"
    UPDATER_UPDATE_FAILED = "updater.update_failed"
    UPDATER_UPDATE_SKIPPED = "updater.update_skipped"
    UPDATER_DOWNLOAD_PROGRESS = "updater.download_progress"
    UPDATER_INSTALL_PROGRESS = "updater.install_progress"

    # ==================== Hardware ====================
    HARDWARE_ID_REQUEST = "hardware.id_request"
    HARDWARE_ID_RESPONSE = "hardware.id_response"
    HARDWARE_ID_REFRESH = "hardware.id_refresh"

    # ==================== Network ====================
    NETWORK_STATUS_CHANGED = "network.status_changed"
    NETWORK_QUALITY_CHANGED = "network.quality_changed"

    # ==================== Instance Management ====================
    INSTANCE_CHECK_REQUEST = "instance.check_request"

    # ==================== Interrupt ====================
    INTERRUPT_REQUEST = "interrupt.request"

    # ==================== Payment & Subscription ====================
    PAYMENT_SYNC_REQUESTED = "payment.sync_requested"
    SUBSCRIPTION_STATUS_UPDATED = "subscription.status_updated"

    # ==================== Browser ====================
    BROWSER_PROGRESS = "browser.progress"
    BROWSER_STARTED = "browser.started"
    BROWSER_COMPLETED = "browser.completed"
    BROWSER_FAILED = "browser.failed"
    BROWSER_CANCELLED = "browser.cancelled"

    # ==================== Navigation ====================
    NAVIGATION_DEEP_LINK = "navigation.deep_link"
