"""
BrowserProgressIntegration — обработка событий прогресса browser-use от сервера.

Подписывается на "browser.progress" и публикует события для UI/логирования.
Feature ID: F-2025-015-browser-use
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Optional, Dict, Any, Set

from integration.core.event_bus import EventBus, EventPriority
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler

from modules.browser_progress.core.types import BrowserProgressEvent, BrowserProgressType

logger = logging.getLogger(__name__)

FEATURE_ID = "F-2025-015-browser-use"


@dataclass
class BrowserProgressIntegrationConfig:
    """Config for browser progress integration"""
    enabled: bool = False  # Feature flag - disabled by default
    log_steps: bool = True
    log_terminal: bool = True


class BrowserProgressIntegration:
    """
    Integration for handling browser automation progress events.
    
    Subscribes to browser.progress events from gRPC layer and:
    - Logs progress steps
    - Tracks active browser tasks
    - Handles terminal events (completed/failed/cancelled)
    """
    
    def __init__(
        self,
        event_bus: EventBus,
        state_manager: ApplicationStateManager,
        error_handler: ErrorHandler,
        config: Optional[BrowserProgressIntegrationConfig] = None,
    ) -> None:
        self.event_bus = event_bus
        self.state_manager = state_manager
        self.error_handler = error_handler
        self.config = config or BrowserProgressIntegrationConfig()
        
        self._initialized = False
        self._running = False
        
        # Track active browser tasks by session_id to ensure idempotency
        self._active_tasks: Dict[str, str] = {}  # session_id -> task_id
        self._completed_tasks: Set[str] = set()  # task_ids that are terminal
    
    async def initialize(self) -> bool:
        """Initialize integration and subscribe to events"""
        if not self.config.enabled:
            logger.info(f"[{FEATURE_ID}] BrowserProgressIntegration disabled by config")
            self._initialized = True
            return True
        
        try:
            await self.event_bus.subscribe(
                "browser.progress",
                self._on_browser_progress,
                EventPriority.MEDIUM
            )
            
            self._initialized = True
            logger.info(f"[{FEATURE_ID}] BrowserProgressIntegration initialized")
            return True
            
        except Exception as e:
            logger.error(f"[{FEATURE_ID}] Init error: {e}")
            return False
    
    async def start(self) -> bool:
        """Start the integration"""
        self._running = True
        logger.info(f"[{FEATURE_ID}] BrowserProgressIntegration started")
        return True
    
    async def stop(self) -> bool:
        """Stop the integration"""
        self._running = False
        self._active_tasks.clear()
        logger.info(f"[{FEATURE_ID}] BrowserProgressIntegration stopped")
        return True
    
    async def _on_browser_progress(self, event: Dict[str, Any]) -> None:
        """Handle browser.progress event from gRPC layer"""
        if not self._running or not self.config.enabled:
            return
        
        try:
            data = (event or {}).get("data", {})
            if not data:
                data = event if isinstance(event, dict) else {}
            
            progress = BrowserProgressEvent.from_dict(data)
            
            # Idempotency: skip if task already terminal
            if progress.task_id in self._completed_tasks:
                logger.debug(f"[{FEATURE_ID}] Skipping duplicate terminal event for task={progress.task_id}")
                return
            
            # Track active task
            if progress.type == BrowserProgressType.TASK_STARTED:
                self._active_tasks[progress.session_id] = progress.task_id
                if self.config.log_steps:
                    logger.info(f"[{FEATURE_ID}] 🌐 Browser task started: {progress.task_id}")
            
            # Log step progress
            elif progress.type == BrowserProgressType.STEP_COMPLETED:
                if self.config.log_steps:
                    logger.info(
                        f"[{FEATURE_ID}] 🔄 Step {progress.step_number}: {progress.description}"
                        f"{' - ' + progress.url if progress.url else ''}"
                    )
            
            # Handle terminal events
            elif progress.is_terminal():
                self._completed_tasks.add(progress.task_id)
                self._active_tasks.pop(progress.session_id, None)
                
                if self.config.log_terminal:
                    if progress.type == BrowserProgressType.TASK_COMPLETED:
                        logger.info(f"[{FEATURE_ID}] ✅ Browser task completed: {progress.task_id}")
                    elif progress.type == BrowserProgressType.TASK_FAILED:
                        logger.warning(f"[{FEATURE_ID}] ❌ Browser task failed: {progress.error}")
                    elif progress.type == BrowserProgressType.TASK_CANCELLED:
                        logger.info(f"[{FEATURE_ID}] ⏹️ Browser task cancelled: {progress.task_id}")
        
        except Exception as e:
            logger.error(f"[{FEATURE_ID}] Error handling browser.progress: {e}")
    
    def get_status(self) -> Dict[str, Any]:
        """Get integration status"""
        return {
            "initialized": self._initialized,
            "running": self._running,
            "enabled": self.config.enabled,
            "active_tasks": len(self._active_tasks),
            "completed_tasks": len(self._completed_tasks),
        }
