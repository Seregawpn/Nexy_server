"""
Browser Use Module (Server Proxy)

Feature ID: F-2025-015-browser-use

This module proxies browser-use requests to the client for local execution.
Server no longer executes browser automation locally.
"""
import logging
import uuid
from typing import Dict, Any, AsyncIterator
from datetime import datetime

from modules.browser_use.constants import FEATURE_ID

logger = logging.getLogger(__name__)

# Stub for BROWSER_USE_AVAILABLE to prevent import errors if used elsewhere
BROWSER_USE_AVAILABLE = False 

class BrowserUseModule:
    """
    Server-side proxy for executing browser-use tasks on the client.
    """
    
    def __init__(self):
        self._config: Dict[str, Any] = {}
        self._active_tasks: Dict[str, Any] = {}
        self._initialized = False
        self._interrupt_workflow = None

    async def initialize(self, config: dict) -> None:
        self._config = config
        self._initialized = True
        logger.info(f"[{FEATURE_ID}] BrowserUseModule (Proxy) initialized. Execution delegated to client.")

    async def process(self, request: Dict[str, Any]) -> AsyncIterator[Dict[str, Any]]:
        """
        Proxies request to client.
        
        Yields:
             browser.use.request event
        """
        task_id = f"task_{uuid.uuid4().hex[:12]}"
        task = request.get('args', {}).get('task', 'Unknown task')
        session_id = request.get('session_id', 'unknown')
        
        logger.info(f"[{FEATURE_ID}] Proxying process request to client: task={task[:50]}, task_id={task_id}")
        
        # Yield request event for client to pick up
        yield {
            'type': 'browser.use.request',
            'task_id': task_id,
            'args': request.get('args'),
            'session_id': session_id,
            'timestamp': datetime.now().isoformat()
        }
        
    async def cleanup(self):
        pass

    def status(self):
        from integrations.core.module_status import ModuleStatus, ModuleState
        return ModuleStatus(state=ModuleState.READY, health="ok")

    def set_interrupt_workflow(self, interrupt_workflow):
        self._interrupt_workflow = interrupt_workflow

    # Stub methods that might be called
    async def _ensure_browser_installed(self):
        pass
